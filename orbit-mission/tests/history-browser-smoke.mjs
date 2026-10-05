import assert from "node:assert/strict";
import { mkdir, writeFile } from "node:fs/promises";
import { createRequire } from "node:module";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { GITHUB_PULLS_URL } from "../pull-request-history.mjs";

const require = createRequire(import.meta.url);
const { chromium } = require(process.env.PLAYWRIGHT_MODULE || "playwright");
const baseURL = process.env.BASE_URL || "http://127.0.0.1:8767";
const out =
  process.env.QA_OUTPUT_DIR || join(tmpdir(), "orbit-mission-history-qa");
await mkdir(out, { recursive: true });
const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({
  viewport: { width: 1440, height: 1000 },
});
const page = await context.newPage();
const errors = [];
const checks = [];
const requests = [];
page.on("pageerror", (error) => errors.push(error.message));

const titlePayload = '<img src=x onerror="window.__historyTitleExecuted=true">';
const pull = (number, overrides = {}) => ({
  number,
  title: `Contribution ${number}`,
  user: { login: "contributor" },
  state: "open",
  draft: false,
  merged_at: null,
  updated_at: "2026-10-05T15:00:00Z",
  ...overrides,
});
const liveItems = [
  pull(6),
  pull(5, { state: "closed", merged_at: "2026-10-05T14:00:00Z" }),
  pull(7, { draft: true }),
  pull(8, {
    state: "closed",
    title: titlePayload,
    html_url: "javascript:alert(1)",
  }),
];
let response = { status: 200, body: liveItems };
let releaseFirstRequest;
const firstRequestGate = new Promise((resolve) => {
  releaseFirstRequest = resolve;
});
await context.route("https://api.github.com/**", async (route) => {
  requests.push(route.request().url());
  const current = response;
  if (requests.length === 1) await firstRequestGate;
  await route.fulfill({
    status: current.status,
    contentType: "application/json",
    body: JSON.stringify(current.body),
  });
});

const check = async (name, fn) => {
  try {
    await fn();
    checks.push({ name, result: "PASS" });
  } catch (error) {
    checks.push({ name, result: "FAIL", message: error.message });
  }
};
const row = (target, number) =>
  target.locator("#pull-request-list .pull-request-item").filter({
    has: target.locator(
      `a[href="https://github.com/docbgm2002/collatz-things/pull/${number}"]`,
    ),
  });
const status = (target, number) =>
  row(target, number).locator(".pr-status").innerText();
const waitStatus = (target, number, expected) =>
  target.waitForFunction(
    ({ number, expected }) => {
      const link = document.querySelector(
        `#pull-request-list a[href$="/pull/${number}"]`,
      );
      return (
        link?.closest(".pull-request-item")?.querySelector(".pr-status")
          ?.textContent === expected
      );
    },
    { number, expected },
  );
const ready = (target) =>
  target.waitForFunction(
    () => typeof window.render_game_to_text === "function",
  );

try {
  await page.goto(baseURL);
  await ready(page);
  await check(
    "GitHub is not requested before Project history opens",
    async () => {
      await page.locator('[data-tab="log"]').click();
      await page.locator('[data-tab="mission"]').click();
      await page.evaluate(
        () =>
          new Promise((resolve) =>
            requestAnimationFrame(() => requestAnimationFrame(resolve)),
          ),
      );
      assert.equal(requests.length, 0);
    },
  );
  await check(
    "dated snapshot remains visible while first live request is pending",
    async () => {
      const requested = page.waitForRequest(GITHUB_PULLS_URL);
      await page.locator('[data-tab="history"]').click();
      await requested;
      assert.equal(requests.length, 1);
      assert.equal(await status(page, 6), "Open · ready for review");
      assert.equal(await status(page, 5), "Merged");
      assert.match(
        await page.locator("#pull-request-status").innerText(),
        /snapshot|saved/i,
      );
      assert.match(
        await page.locator("#pull-request-status").innerText(),
        /2026/,
      );
    },
  );
  await check(
    "live API data distinguishes merged, ready, draft, and closed",
    async () => {
      releaseFirstRequest();
      await waitStatus(page, 8, "Closed");
      assert.equal(
        await page.locator("#pull-request-list .pull-request-item").count(),
        4,
      );
      assert.equal(await status(page, 5), "Merged");
      assert.equal(await status(page, 6), "Open · ready for review");
      assert.equal(await status(page, 7), "Draft");
      assert.equal(await status(page, 8), "Closed");
      assert.match(
        await page.locator("#pull-request-status").innerText(),
        /live|last.*check/i,
      );
      assert.deepEqual(requests, [GITHUB_PULLS_URL]);
      await page.screenshot({
        path: `${out}/history-desktop.png`,
        fullPage: true,
      });
    },
  );
  await check(
    "GitHub titles render as text and links remain within the project",
    async () => {
      assert.ok((await row(page, 8).innerText()).includes(titlePayload));
      assert.equal(await page.locator("#pull-request-list img").count(), 0);
      assert.equal(
        await page.evaluate(() => window.__historyTitleExecuted === true),
        false,
      );
      for (const href of await page
        .locator("#pull-request-list a")
        .evaluateAll((links) => links.map((link) => link.href))) {
        assert.match(
          href,
          /^https:\/\/github\.com\/docbgm2002\/collatz-things\/pull\/\d+$/,
        );
      }
    },
  );
  await check(
    "manual refresh updates a formerly open pull request to merged",
    async () => {
      response = {
        status: 200,
        body: liveItems.map((item) =>
          item.number === 6
            ? {
                ...item,
                state: "closed",
                merged_at: "2026-10-05T16:00:00Z",
                updated_at: "2026-10-05T16:00:00Z",
              }
            : item,
        ),
      };
      await page.locator("#refresh-history").click();
      await waitStatus(page, 6, "Merged");
      assert.equal(requests.length, 2);
      assert.equal(await status(page, 5), "Merged");
    },
  );
  await check(
    "403 refresh retains successful data and explains the stale result",
    async () => {
      const previous = await page.locator("#pull-request-list").innerText();
      response = { status: 403, body: { message: "API rate limit exceeded" } };
      await page.locator("#refresh-history").click();
      await page.waitForFunction(() =>
        document
          .getElementById("pull-request-status")
          .textContent.includes("403"),
      );
      assert.equal(
        await page.locator("#pull-request-list").innerText(),
        previous,
      );
      assert.equal(await status(page, 6), "Merged");
      const message = await page.locator("#pull-request-status").innerText();
      assert.match(message, /denied|rate.limit/i);
      assert.match(message, /last successful|last.*check/i);
      assert.equal(await page.locator("#refresh-history").isEnabled(), true);
    },
  );
  for (const width of [375, 320]) {
    await check(
      `Project history fits a ${width}px screen after a refresh error`,
      async () => {
        await page.setViewportSize({ width, height: 812 });
        assert.equal(
          await page.evaluate(() => document.documentElement.scrollWidth),
          width,
        );
        assert.equal(await page.locator("#refresh-history").isVisible(), true);
        await page.screenshot({
          path: `${out}/history-mobile-${width}.png`,
          fullPage: true,
        });
      },
    );
  }
  await check(
    "initial 403 retains the dated snapshot without implying a live check",
    async () => {
      const offlineContext = await browser.newContext({
        viewport: { width: 375, height: 812 },
      });
      try {
        await offlineContext.route("https://api.github.com/**", (route) =>
          route.fulfill({
            status: 403,
            contentType: "application/json",
            body: JSON.stringify({ message: "API rate limit exceeded" }),
          }),
        );
        const offline = await offlineContext.newPage();
        offline.on("pageerror", (error) => errors.push(error.message));
        await offline.goto(baseURL);
        await ready(offline);
        await offline.locator('[data-tab="history"]').click();
        await offline.waitForFunction(() =>
          document
            .getElementById("pull-request-status")
            .textContent.includes("403"),
        );
        assert.equal(await status(offline, 6), "Open · ready for review");
        assert.equal(await status(offline, 5), "Merged");
        const message = await offline
          .locator("#pull-request-status")
          .innerText();
        assert.match(message, /snapshot|saved/i);
        assert.match(message, /2026/);
        assert.doesNotMatch(message, /last successful check/i);
        assert.equal(
          await offline.locator("#refresh-history").isEnabled(),
          true,
        );
        assert.equal(
          await offline.evaluate(() => document.documentElement.scrollWidth),
          375,
        );
        await offline.screenshot({
          path: `${out}/history-initial-failure.png`,
          fullPage: true,
        });
      } finally {
        await offlineContext.close();
      }
    },
  );
  await check(
    "history interactions have no browser JavaScript errors",
    async () => assert.deepEqual(errors, []),
  );
} finally {
  releaseFirstRequest();
  await writeFile(
    `${out}/history-report.json`,
    JSON.stringify({ checks, errors, requests }, null, 2),
  );
  console.log(JSON.stringify({ checks, errors, requests }, null, 2));
  await browser.close();
}
if (checks.some((item) => item.result === "FAIL")) process.exitCode = 1;
