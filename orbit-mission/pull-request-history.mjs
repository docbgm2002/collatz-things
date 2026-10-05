export const GITHUB_PULLS_URL =
  "https://api.github.com/repos/docbgm2002/collatz-things/pulls?state=all&sort=updated&direction=desc&per_page=10";

const REPOSITORY_URL = "https://github.com/docbgm2002/collatz-things";
const malformed = () =>
  new Error("GitHub returned a malformed pull request response.");
const nonempty = (value) =>
  typeof value === "string" && value.trim().length > 0;
const timestamp = (value) => {
  if (
    typeof value !== "string" ||
    !/^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{1,3})?Z$/.test(value)
  )
    return false;
  const date = new Date(value);
  return (
    Number.isFinite(date.getTime()) &&
    date.toISOString().slice(0, 19) === value.slice(0, 19)
  );
};

/** Convert the REST list response without treating PR state as review approval. */
export function normalizePullRequests(raw) {
  if (!Array.isArray(raw)) throw malformed();
  const numbers = new Set();
  const requests = Array.from(raw, (item) => {
    if (
      !item ||
      typeof item !== "object" ||
      Array.isArray(item) ||
      !Number.isSafeInteger(item.number) ||
      item.number < 1 ||
      numbers.has(item.number) ||
      !nonempty(item.title) ||
      !nonempty(item.user?.login) ||
      !["open", "closed"].includes(item.state) ||
      typeof item.draft !== "boolean" ||
      !timestamp(item.updated_at) ||
      !(item.merged_at === null || timestamp(item.merged_at))
    ) {
      throw malformed();
    }
    numbers.add(item.number);
    return {
      number: item.number,
      title: item.title,
      url: `${REPOSITORY_URL}/pull/${item.number}`,
      author: item.user.login,
      status:
        item.merged_at !== null
          ? "merged"
          : item.state === "closed"
            ? "closed"
            : item.draft
              ? "draft"
              : "open",
      updatedAt: item.updated_at,
      mergedAt: item.merged_at,
    };
  });
  return requests.sort(
    (a, b) =>
      Date.parse(b.updatedAt) - Date.parse(a.updatedAt) || b.number - a.number,
  );
}

/** Fetch public project history; bound both the request and response-body read. */
export async function fetchPullRequests({
  fetchImpl = globalThis.fetch,
  timeoutMs = 8000,
} = {}) {
  if (typeof fetchImpl !== "function") {
    throw new Error("This browser cannot fetch live GitHub history.");
  }
  if (!Number.isFinite(timeoutMs) || timeoutMs <= 0) {
    throw new RangeError("The GitHub request timeout must be positive.");
  }
  const controller = new AbortController();
  const timeoutError = new Error(
    "GitHub request timed out. Try refreshing again.",
  );
  let timer;
  const timeout = new Promise((_, reject) => {
    timer = setTimeout(() => {
      controller.abort();
      reject(timeoutError);
    }, timeoutMs);
  });
  const load = async () => {
    let response;
    try {
      response = await fetchImpl(GITHUB_PULLS_URL, {
        credentials: "omit",
        cache: "no-store",
        headers: { Accept: "application/vnd.github+json" },
        signal: controller.signal,
      });
    } catch (error) {
      if (controller.signal.aborted) throw timeoutError;
      throw new Error(
        "Could not reach GitHub. Check your connection and try again.",
        { cause: error },
      );
    }
    if (
      !response ||
      typeof response.ok !== "boolean" ||
      !Number.isInteger(response.status) ||
      typeof response.json !== "function"
    ) {
      throw malformed();
    }
    if (!response.ok) {
      if (response.status === 403 || response.status === 429) {
        throw new Error(
          `GitHub denied or rate-limited the request (HTTP ${response.status}). Try again later.`,
        );
      }
      throw new Error(
        `GitHub returned HTTP ${response.status}. Try again later.`,
      );
    }
    let raw;
    try {
      raw = await response.json();
    } catch {
      if (controller.signal.aborted) throw timeoutError;
      throw malformed();
    }
    return normalizePullRequests(raw);
  };
  try {
    return await Promise.race([load(), timeout]);
  } finally {
    clearTimeout(timer);
  }
}
