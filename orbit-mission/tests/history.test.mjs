import test from "node:test";
import assert from "node:assert/strict";
import {
  GITHUB_PULLS_URL,
  normalizePullRequests,
  fetchPullRequests,
} from "../pull-request-history.mjs";

const pull = (overrides = {}) => ({
  number: 5,
  title: "Add playable orbit experiments",
  user: { login: "contributor" },
  state: "open",
  draft: false,
  updated_at: "2026-10-05T13:00:00Z",
  merged_at: null,
  ...overrides,
});
const response = (raw, status = 200) => ({
  ok: status >= 200 && status < 300,
  status,
  json: async () => raw,
});

test("REST states distinguish merged, open, draft, and unmerged closed PRs", () => {
  const raw = [
    pull({ number: 1, state: "closed", merged_at: "2026-10-05T12:00:00Z" }),
    pull({ number: 2 }),
    pull({ number: 3, draft: true }),
    pull({ number: 4, state: "closed" }),
    pull({ number: 5, state: "closed", draft: true }),
  ];
  const statuses = new Map(
    normalizePullRequests(raw).map((item) => [item.number, item.status]),
  );
  assert.deepEqual(
    [...statuses].sort((a, b) => a[0] - b[0]),
    [
      [1, "merged"],
      [2, "open"],
      [3, "draft"],
      [4, "closed"],
      [5, "closed"],
    ],
  );
  assert.ok([...statuses.values()].every((status) => status !== "approved"));
});

test("history sorts by update time without changing its input", () => {
  const raw = [
    pull({ number: 1 }),
    pull({ number: 2, updated_at: "2026-10-05T14:00:00Z" }),
  ];
  const copy = structuredClone(raw);
  assert.deepEqual(
    normalizePullRequests(raw).map((item) => item.number),
    [2, 1],
  );
  assert.deepEqual(raw, copy);
});

test("links use the fixed project and numeric PR ID; titles remain plain data", () => {
  const title = '<img src=x onerror="alert(1)">';
  const [item] = normalizePullRequests([
    pull({ title, html_url: "javascript:alert(1)" }),
  ]);
  assert.deepEqual(item, {
    number: 5,
    title,
    url: "https://github.com/docbgm2002/collatz-things/pull/5",
    author: "contributor",
    status: "open",
    updatedAt: "2026-10-05T13:00:00Z",
    mergedAt: null,
  });
});

test("a genuine empty list succeeds while malformed or partial payloads fail", () => {
  assert.deepEqual(normalizePullRequests([]), []);
  for (const raw of [
    null,
    {},
    { message: "rate limited" },
    [null],
    Array(1),
    [pull(), {}],
    [pull(), pull()],
    [pull({ number: "5" })],
    [pull({ number: 0 })],
    [pull({ number: Number.MAX_SAFE_INTEGER + 1 })],
    [pull({ title: " " })],
    [pull({ user: null })],
    [pull({ user: { login: "" } })],
    [pull({ state: "approved" })],
    [pull({ draft: undefined })],
    [pull({ updated_at: "not a date" })],
    [pull({ updated_at: "1" })],
    [pull({ updated_at: "2026-02-30T12:00:00Z" })],
    [pull({ merged_at: "not a date" })],
    [pull({ merged_at: undefined })],
  ]) {
    assert.throws(() => normalizePullRequests(raw), /malformed/);
  }
});

test("fetch uses the public API without credentials or cached responses", async () => {
  let options;
  const result = await fetchPullRequests({
    fetchImpl: async (url, init) => {
      assert.equal(url, GITHUB_PULLS_URL);
      options = init;
      return response([pull()]);
    },
  });
  assert.equal(result[0].number, 5);
  assert.equal(options.credentials, "omit");
  assert.equal(options.cache, "no-store");
  assert.equal(options.headers.Accept, "application/vnd.github+json");
  assert.ok(options.signal instanceof AbortSignal);
  assert.equal(options.signal.aborted, false);
});

test("403 and 429 responses explain denied or rate-limited requests", async () => {
  for (const status of [403, 429]) {
    await assert.rejects(
      fetchPullRequests({
        fetchImpl: async () =>
          response({ message: "API rate limit exceeded" }, status),
      }),
      new RegExp(`rate-limited.*HTTP ${status}`),
    );
  }
});

test("HTTP errors, invalid JSON, and invalid response shapes cannot look like empty history", async () => {
  await assert.rejects(
    fetchPullRequests({ fetchImpl: async () => response(null, 500) }),
    /HTTP 500/,
  );
  await assert.rejects(
    fetchPullRequests({ fetchImpl: async () => response({}) }),
    /malformed/,
  );
  await assert.rejects(
    fetchPullRequests({ fetchImpl: async () => ({}) }),
    /malformed/,
  );
  await assert.rejects(
    fetchPullRequests({
      fetchImpl: async () => ({
        ok: true,
        status: 200,
        json: async () => {
          throw new SyntaxError("Invalid JSON");
        },
      }),
    }),
    /malformed/,
  );
});

test("network failures remain errors rather than successful empty history", async () => {
  await assert.rejects(
    fetchPullRequests({
      fetchImpl: async () => {
        throw new TypeError("offline");
      },
    }),
    /Could not reach GitHub/,
  );
});

test("timeout aborts and finishes even if fetch ignores its abort signal", async () => {
  let signal;
  await assert.rejects(
    fetchPullRequests({
      timeoutMs: 5,
      fetchImpl: async (_, options) => {
        signal = options.signal;
        return new Promise(() => {});
      },
    }),
    /timed out/,
  );
  assert.equal(signal.aborted, true);
});

test("timeout also bounds a stalled response body", async () => {
  await assert.rejects(
    fetchPullRequests({
      timeoutMs: 5,
      fetchImpl: async () => ({
        ok: true,
        status: 200,
        json: () => new Promise(() => {}),
      }),
    }),
    /timed out/,
  );
});

test("invalid fetch and timeout options fail explicitly", async () => {
  await assert.rejects(fetchPullRequests({ fetchImpl: null }), /cannot fetch/);
  for (const timeoutMs of [0, -1, Infinity, NaN]) {
    await assert.rejects(fetchPullRequests({ timeoutMs }), /must be positive/);
  }
});
