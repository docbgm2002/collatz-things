import assert from "node:assert/strict";
import { mkdir, readFile, writeFile } from "node:fs/promises";
import { createRequire } from "node:module";
import { tmpdir } from "node:os";
import { join } from "node:path";
const require = createRequire(import.meta.url);
const { chromium } = require(process.env.PLAYWRIGHT_MODULE || "playwright");
const baseURL = process.env.BASE_URL || "http://127.0.0.1:8767";
const out = process.env.QA_OUTPUT_DIR || join(tmpdir(), "orbit-mission-qa");
await mkdir(out, { recursive: true });
const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({
  viewport: { width: 1440, height: 1000 },
  acceptDownloads: true,
  reducedMotion: "no-preference",
});
const page = await context.newPage();
const errors = [];
const checks = [];
page.on("pageerror", (error) => errors.push(error.message));
page.on("console", (message) => {
  if (message.type() === "error") errors.push(message.text());
});
const state = () =>
  page.evaluate(() => JSON.parse(window.render_game_to_text()));
const text = (selector) => page.locator(selector).innerText();
const check = async (name, fn) => {
  try {
    await fn();
    checks.push({ name, result: "PASS" });
  } catch (error) {
    checks.push({ name, result: "FAIL", message: error.message });
  }
};
const end = async () => {
  await page.locator("#timeline").evaluate((node) => {
    node.value = node.max;
    node.dispatchEvent(new Event("input", { bubbles: true }));
  });
};
const launch = async ({
  seed = "9",
  rule = "classic",
  mode = "standard",
  multiplier,
  offset,
} = {}) => {
  await page.locator('[data-tab="mission"]').click();
  await page.locator("#seed").fill(seed);
  await page.locator("#rule-select").selectOption(rule);
  await page.locator("#map-mode").selectOption(mode);
  if (multiplier) await page.locator("#multiplier").selectOption(multiplier);
  if (offset) await page.locator("#offset").selectOption(offset);
  await page.locator('#lab-form button[type="submit"]').click();
};
try {
  await page.goto(baseURL);
  await page.waitForFunction(
    () => typeof window.render_game_to_text === "function",
  );
  await check("default mission and arithmetic", async () => {
    assert.equal((await state()).number, "9");
    assert.match(await text("#equation"), /3 × 9 \+ 1 = 28/);
    assert.equal(await text("#step-total"), "19");
    await page.screenshot({
      path: `${out}/desktop-initial.png`,
      fullPage: true,
    });
  });
  await check("play, pause, next, previous and restart", async () => {
    await page.locator("#play").click();
    assert.equal((await state()).mode, "playing");
    await page.evaluate(() => window.advanceTime(1000));
    assert.equal((await state()).number, "28");
    await page.locator("#play").click();
    const stopped = await state();
    assert.equal(stopped.mode, "paused");
    await page.evaluate(() => window.advanceTime(3000));
    assert.equal((await state()).number, stopped.number);
    await page.locator("#next").click();
    assert.equal((await state()).number, "14");
    await page.locator("#back").click();
    assert.equal((await state()).number, "28");
    await page.locator("#restart").click();
    assert.equal((await state()).number, "9");
  });
  await check(
    "outward animation increases radius throughout 9 to 28",
    async () => {
      await page.locator('[data-mission="home"]').click();
      const initial = await state();
      const initialRadius = Math.hypot(
        initial.ship.x - initial.home.x,
        initial.ship.y - initial.home.y,
      );
      await page.locator("#next").click();
      const radii = await page.evaluate(() =>
        Array.from({ length: 9 }, () => {
          window.advanceTime(60);
          const s = JSON.parse(window.render_game_to_text());
          return Math.hypot(s.ship.x - s.home.x, s.ship.y - s.home.y);
        }),
      );
      assert.ok(
        radii[0] >= initialRadius,
        "first movement must increase radius",
      );
      for (let i = 1; i < radii.length; i++)
        assert.ok(
          radii[i] >= radii[i - 1] - 1e-8,
          `radius decreased: ${radii}`,
        );
      assert.ok(radii.at(-1) > initialRadius);
      await page.locator("#restart").click();
    },
  );
  await check("prediction game evaluates outward and inward", async () => {
    await page.locator("#guess-out").click();
    assert.equal((await state()).number, "28");
    assert.match(await text("#guess-feedback"), /Correct/);
    await page.locator("#guess-in").click();
    assert.equal((await state()).number, "14");
    assert.deepEqual((await state()).predictionScore, {
      correct: 2,
      attempted: 2,
    });
  });
  await check("classic 9 completes through playback and replays", async () => {
    await page.locator("#restart").click();
    await page.locator("#play").click();
    await page.evaluate(() => window.advanceTime(20000));
    const s = await state();
    assert.equal(s.number, "1");
    assert.equal(s.step, 19);
    assert.equal(s.mode, "home");
    assert.match(
      await text("#result-text"),
      /19 displayed moves \(19 elementary steps\)/,
    );
    assert.equal(await page.locator("#next").isDisabled(), true);
    await page.locator("#play").click();
    assert.equal((await state()).number, "9");
    await page.locator("#play").click();
    await end();
    await page.locator("#save-result").click();
    assert.match(await text("#save-notice"), /Flight saved/);
  });
  await check("3n-1 gives the five-move cycle", async () => {
    await page.locator('[data-mission="loop"]').click();
    assert.equal((await state()).number, "5");
    await page.locator("#play").click();
    await page.evaluate(() => window.advanceTime(6000));
    const s = await state();
    assert.equal(s.number, "5");
    assert.equal(s.step, 5);
    assert.equal(s.outcome.type, "cycle");
    assert.equal(s.outcome.cycleLength, 5);
    await page.locator("#save").click();
  });
  await check(
    "odd mode 9 gives six displayed and nineteen elementary moves",
    async () => {
      await launch({ mode: "odd" });
      await page.locator("#next").click();
      assert.equal((await state()).number, "7");
      assert.match(await text("#equation"), /divide by 2\^2 → 7/);
      await end();
      assert.equal((await state()).step, 6);
      assert.equal((await state()).elementarySteps, 19);
      assert.equal(await text("#peak"), "17");
      await page.locator("#save").click();
    },
  );
  await check(
    "invalid seed errors do not replace active experiment",
    async () => {
      const prior = await state();
      await launch({ seed: "2", mode: "odd" });
      assert.match(await text("#form-error"), /odd starting number/);
      assert.equal((await state()).number, prior.number);
      await launch({ seed: "0" });
      assert.match(await text("#form-error"), /positive/);
      await launch({ seed: "3.14" });
      assert.match(await text("#form-error"), /decimal integer/);
    },
  );
  await check(
    "custom rule leaving positive integers is explained without moving",
    async () => {
      await launch({
        seed: "3",
        rule: "custom",
        multiplier: "3",
        offset: "-9",
      });
      assert.equal((await state()).mode, "invalid");
      assert.equal((await state()).number, "3");
      assert.equal((await state()).step, 0);
      assert.match(
        await text("#result-text"),
        /3 × 3 − 9 = 0.*move was not taken/,
      );
      assert.equal(await page.locator("#play").isDisabled(), true);
    },
  );
  await check(
    "same-number prediction detects an odd-mode fixed loop",
    async () => {
      await launch({
        seed: "3",
        rule: "custom",
        multiplier: "3",
        offset: "-3",
        mode: "odd",
      });
      await page.locator("#guess-same").click();
      const s = await state();
      assert.equal(s.number, "3");
      assert.equal(s.step, 1);
      assert.equal(s.outcome.type, "cycle");
      assert.equal(s.outcome.cycleLength, 1);
      assert.deepEqual(s.predictionScore, { correct: 1, attempted: 1 });
      assert.match(await text("#explanation"), /stays the same/);
    },
  );
  await check("5n+1 hits bounded limit and labels it unresolved", async () => {
    await launch({ seed: "9", rule: "five" });
    await end();
    assert.equal((await state()).step, 600);
    assert.equal((await state()).mode, "limit");
    assert.match(await text("#result-text"), /600-step limit.*unresolved/);
  });
  let evidence;
  await check("export contains a complete valid replay", async () => {
    await launch();
    const downloadPromise = page.waitForEvent("download");
    await page.locator("#export").click();
    const download = await downloadPromise;
    await download.saveAs(`${out}/replay.json`);
    evidence = JSON.parse(await readFile(`${out}/replay.json`, "utf8"));
    assert.equal(evidence.run.frames.length, 20);
    assert.equal(evidence.run.frames[19].value, "1");
    assert.equal(evidence.run.config.seed, "9");
  });
  await check(
    "saved flights survive reload and compare with explicit move conventions",
    async () => {
      await page.reload();
      await page.waitForFunction(
        () => typeof window.render_game_to_text === "function",
      );
      assert.equal((await state()).savedFlights, 3);
      await page.locator('[data-tab="log"]').click();
      assert.equal(await page.locator(".log-row").count(), 3);
      await page.locator(".check-label input").nth(0).check();
      await page.locator(".check-label input").nth(2).check();
      assert.equal(await page.locator("#comparison").isVisible(), true);
      assert.match(await text("#comparison"), /Odd moves/);
      assert.match(await text("#comparison"), /Every move/);
      assert.match(await text("#comparison"), /omits even values/);
      await page.screenshot({
        path: `${out}/desktop-comparison.png`,
        fullPage: true,
      });
      await page.locator(".log-row .secondary-button").nth(0).click();
      assert.equal((await state()).rule.mode, "odd");
      assert.equal((await state()).number, "9");
    },
  );
  await check(
    "valid import accepted and tampered arithmetic rejected",
    async () => {
      assert.ok(evidence);
      await page.locator('[data-tab="log"]').click();
      await page.locator("#import").setInputFiles(`${out}/replay.json`);
      await page.waitForFunction(() =>
        document
          .getElementById("import-notice")
          .textContent.includes("Every calculation verified"),
      );
      const count = (await state()).savedFlights;
      const changed = structuredClone(evidence);
      changed.run.frames[1].value = "29";
      await page
        .locator("#import")
        .setInputFiles({
          name: "tampered.json",
          mimeType: "application/json",
          buffer: Buffer.from(JSON.stringify(changed)),
        });
      await page.waitForFunction(() =>
        document
          .getElementById("import-notice")
          .textContent.includes("Replay rejected"),
      );
      assert.match(
        await text("#import-notice"),
        /differs from an exact replay/,
      );
      assert.equal((await state()).savedFlights, count);
      await page
        .locator("#import")
        .setInputFiles({
          name: "bad.json",
          mimeType: "application/json",
          buffer: Buffer.from("{"),
        });
      await page.waitForFunction(() =>
        document
          .getElementById("import-notice")
          .textContent.includes("Replay rejected"),
      );
    },
  );
  await check("help pauses playback and dismisses", async () => {
    await launch();
    await page.locator("#play").click();
    await page.locator("#help-button").click();
    assert.equal((await state()).mode, "paused");
    assert.equal(await page.locator("#help").isVisible(), true);
    assert.match(await text("#help"), /does not simulate gravity/);
    await page.locator("#start-playing").click();
    assert.equal(await page.locator("#help").isVisible(), false);
  });
  await check("fullscreen toggles the simulation panel", async () => {
    await page.locator("#fullscreen").click();
    await page.waitForFunction(
      () => document.fullscreenElement?.id === "flight-deck",
    );
    assert.equal(
      await page.evaluate(() => document.fullscreenElement?.id),
      "flight-deck",
    );
    await page.locator("#fullscreen").click();
    await page.waitForFunction(() => !document.fullscreenElement);
    assert.equal(
      await page.evaluate(() => Boolean(document.fullscreenElement)),
      false,
    );
  });
  await check(
    "history contains repository links and provenance explanation",
    async () => {
      await page.locator('[data-tab="history"]').click();
      assert.ok((await page.locator(".history-item").count()) >= 3);
      assert.match(
        await text("#history-panel"),
        /not independently verified model attribution/,
      );
      for (const href of await page
        .locator(".history-item a")
        .evaluateAll((nodes) => nodes.map((n) => n.href)))
        assert.match(
          href,
          /^https:\/\/github.com\/docbgm2002\/collatz-things\/(commit\/[a-f0-9]{40}|pull\/\d+)$/,
        );
    },
  );
  for (const width of [375, 320]) {
    await check(`mobile ${width}px fits mission, log and help`, async () => {
      await page.setViewportSize({ width, height: 812 });
      for (const tab of ["mission", "log", "history"]) {
        await page.locator(`[data-tab="${tab}"]`).click();
        const sizing = await page.evaluate(() => ({
          scroll: document.documentElement.scrollWidth,
          viewport: innerWidth,
        }));
        assert.equal(
          sizing.scroll,
          sizing.viewport,
          `${tab} horizontal overflow`,
        );
      }
      await page.locator('[data-tab="mission"]').click();
      await page.screenshot({
        path: `${out}/mobile-${width}.png`,
        fullPage: true,
      });
      const clipped = await page.locator(".transport").evaluate((node) => {
        const deck = document
          .getElementById("flight-deck")
          .getBoundingClientRect();
        return [...node.querySelectorAll("button,select")]
          .filter((control) => {
            const r = control.getBoundingClientRect();
            return r.width > 0 && (r.left < deck.left || r.right > deck.right);
          })
          .map((control) => control.id);
      });
      assert.deepEqual(
        clipped,
        [],
        "transport controls must fit inside the flight deck",
      );
      await page.locator("#help-button").click();
      const bounds = await page.locator("#help").boundingBox();
      assert.ok(bounds.x >= 0 && bounds.x + bounds.width <= width);
      await page.locator("#start-playing").click();
    });
  }
  await check(
    "large integer remains exact and expandable on a narrow screen",
    async () => {
      const seed = "9".repeat(60);
      await launch({ seed, rule: "five" });
      assert.equal((await state()).number, seed);
      assert.equal(
        await page.locator("#exact-value-details").isVisible(),
        true,
      );
      await page.locator("#exact-value-details summary").click();
      assert.equal(await text("#exact-value"), seed);
      await end();
      const s = await state();
      assert.equal(await text("#exact-value"), s.number);
      assert.equal(
        await page.evaluate(() => document.documentElement.scrollWidth),
        320,
      );
      await page.screenshot({
        path: `${out}/mobile-large-number.png`,
        fullPage: true,
      });
    },
  );
  await check("no browser JavaScript errors", async () =>
    assert.deepEqual(errors, []),
  );
} finally {
  await writeFile(
    `${out}/report.json`,
    JSON.stringify({ checks, errors }, null, 2),
  );
  console.log(JSON.stringify({ checks, errors }, null, 2));
  await browser.close();
}
if (checks.some((c) => c.result === "FAIL")) process.exitCode = 1;
