/** Exact integer dynamics for Orbit Mission. No floating-point orbit arithmetic. */
export const ENGINE_VERSION = "1.0.0";

const SCHEMA = "orbit-mission-evidence/v1";
const MAX_STEPS = 1000;
const MAX_BITS = 4096;
const MAX_VALUE = (1n << BigInt(MAX_BITS)) - 1n;
const MAX_EVIDENCE_BYTES = 8 * 1024 * 1024;

function record(value, name) {
  if (value === null || typeof value !== "object" || Array.isArray(value)) {
    throw new TypeError(`${name} must be an object.`);
  }
  return value;
}

function integerText(value, name, signed = false) {
  if (typeof value === "number") {
    if (!Number.isSafeInteger(value))
      throw new TypeError(`${name} must be an exact integer.`);
    value = String(value);
  } else if (typeof value === "bigint") {
    value = String(value);
  }
  if (
    typeof value !== "string" ||
    value.length > 61 ||
    !(signed ? /^-?\d+$/ : /^\d+$/).test(value)
  ) {
    throw new TypeError(
      `${name} must be a decimal integer${signed ? "" : " without a sign"}.`,
    );
  }
  return value;
}

/** Return a canonical, JSON-safe configuration; invalid input throws. */
export function normalizeConfig(input = {}) {
  record(input, "Configuration");
  const seedText = integerText(input.seed ?? "9", "Starting number");
  if (seedText.length > 60)
    throw new RangeError("Starting number must have at most 60 digits.");
  const seed = BigInt(seedText);
  if (seed <= 0n) throw new RangeError("Starting number must be positive.");

  const multiplier = BigInt(
    integerText(input.multiplier ?? "3", "Multiplier", true),
  );
  if (multiplier < 1n || multiplier > 9n || multiplier % 2n !== 1n) {
    throw new RangeError("Multiplier must be an odd integer from 1 to 9.");
  }
  const offset = BigInt(integerText(input.offset ?? "1", "Offset", true));
  if (offset < -9n || offset > 9n || offset % 2n === 0n) {
    throw new RangeError("Offset must be an odd integer from -9 to 9.");
  }
  const mode = input.mode ?? "standard";
  if (mode !== "standard" && mode !== "odd") {
    throw new RangeError("Mode must be standard or odd.");
  }
  if (mode === "odd" && seed % 2n === 0n) {
    throw new RangeError("Odd-step mode requires an odd starting number.");
  }
  const maxSteps = input.maxSteps ?? 600;
  if (!Number.isInteger(maxSteps) || maxSteps < 1 || maxSteps > MAX_STEPS) {
    throw new RangeError(
      `Step limit must be a whole number from 1 to ${MAX_STEPS}.`,
    );
  }
  return {
    seed: String(seed),
    multiplier: String(multiplier),
    offset: String(offset),
    mode,
    maxSteps,
  };
}

function oddOperation(multiplier, value, offset, result) {
  return `${multiplier} × ${value} ${offset < 0n ? "−" : "+"} ${offset < 0n ? -offset : offset} = ${result}`;
}

/** Simulate until reaching 1, repeating a value, hitting a limit, or leaving positive integers. */
export function simulate(input = {}) {
  const config = normalizeConfig(input);
  const multiplier = BigInt(config.multiplier);
  const offset = BigInt(config.offset);
  let value = BigInt(config.seed);
  let peak = value;
  let elementarySteps = 0;
  const frames = [
    {
      value: String(value),
      step: 0,
      operation: `Start at ${value}`,
      kind: "start",
      divisions: 0,
      elementarySteps: 0,
    },
  ];
  const seen = new Map([[String(value), 0]]);
  let outcome =
    value === 1n
      ? {
          type: "home",
          message: "Reached 1. This mission stops at 1 by convention.",
        }
      : null;

  for (let step = 1; !outcome && step <= config.maxSteps; step += 1) {
    let next;
    let divisions = 0;
    let operation;
    let elementaryDelta = 1;
    if (value % 2n === 0n) {
      next = value / 2n;
      divisions = 1;
      operation = `${value} ÷ 2 = ${next}`;
    } else {
      next = multiplier * value + offset;
      operation = oddOperation(multiplier, value, offset, next);
      if (next <= 0n) {
        outcome = {
          type: "invalid",
          message: `${operation}. The rule left the positive integers; this move was not taken.`,
        };
        break;
      }
      if (next > MAX_VALUE) {
        outcome = {
          type: "limit",
          message: `The next calculation exceeds the ${MAX_BITS}-bit safety limit. Its behavior is unresolved.`,
        };
        break;
      }
      if (config.mode === "odd") {
        while (next % 2n === 0n) {
          next /= 2n;
          divisions += 1;
        }
        elementaryDelta += divisions;
        operation += `; divide by 2^${divisions} → ${next}`;
      }
    }
    elementarySteps += elementaryDelta;
    const kind = next > value ? "expand" : next < value ? "contract" : "steady";
    value = next;
    if (value > peak) peak = value;
    const text = String(value);
    frames.push({
      value: text,
      step,
      operation,
      kind,
      divisions,
      elementarySteps,
    });
    if (value === 1n) {
      outcome = {
        type: "home",
        message: "Reached 1. This mission stops at 1 by convention.",
      };
    } else if (seen.has(text)) {
      const cycleStart = seen.get(text);
      const cycleLength = step - cycleStart;
      outcome = {
        type: "cycle",
        cycleStart,
        cycleLength,
        message: `Repeated ${text}: a cycle of ${cycleLength} displayed ${cycleLength === 1 ? "step" : "steps"} begins at step ${cycleStart}.`,
      };
    } else {
      seen.set(text, step);
    }
  }
  if (!outcome) {
    outcome = {
      type: "limit",
      message: `Stopped at the ${config.maxSteps}-step limit. Behavior beyond this run is unresolved.`,
    };
  }
  return {
    config,
    frames,
    outcome,
    peak: String(peak),
    steps: frames.length - 1,
    elementarySteps,
  };
}

function sameValue(left, right) {
  if (left === right) return true;
  if (
    left === null ||
    right === null ||
    typeof left !== "object" ||
    typeof right !== "object"
  )
    return false;
  if (Array.isArray(left) !== Array.isArray(right)) return false;
  const keys = Object.keys(left);
  if (keys.length !== Object.keys(right).length) return false;
  return keys.every(
    (key) => Object.hasOwn(right, key) && sameValue(left[key], right[key]),
  );
}

function checkedMetadata(metadata) {
  record(metadata, "Evidence metadata");
  const createdAt = metadata.createdAt ?? new Date().toISOString();
  if (
    typeof createdAt !== "string" ||
    !/^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z$/.test(createdAt) ||
    !Number.isFinite(Date.parse(createdAt)) ||
    new Date(createdAt).toISOString() !== createdAt
  ) {
    throw new TypeError(
      "Evidence creation time must be a UTC ISO timestamp with milliseconds.",
    );
  }
  const sourceRevision = metadata.sourceRevision ?? null;
  const label = metadata.label ?? null;
  for (const [key, value] of Object.entries({ sourceRevision, label })) {
    if (value !== null && (typeof value !== "string" || value.length > 200)) {
      throw new TypeError(
        `${key} must be null or a string of at most 200 characters.`,
      );
    }
  }
  return { createdAt, sourceRevision, label };
}

/** Metadata records provenance supplied by the caller; it is not a signature or identity proof. */
export function makeEvidence(run, metadata = {}) {
  record(run, "Run");
  const recomputed = simulate(run.config);
  if (!sameValue(run, recomputed))
    throw new TypeError(
      "Run does not match an exact replay of its configuration.",
    );
  return {
    schema: SCHEMA,
    engineVersion: ENGINE_VERSION,
    ...checkedMetadata(metadata),
    run: recomputed,
  };
}

/** Recompute imported evidence; a successful check verifies arithmetic, not authorship. */
export function verifyEvidence(evidence) {
  try {
    record(evidence, "Evidence");
    const serialized = JSON.stringify(evidence);
    if (
      typeof serialized !== "string" ||
      new TextEncoder().encode(serialized).length > MAX_EVIDENCE_BYTES
    ) {
      throw new RangeError("Evidence is larger than the 8 MiB import limit.");
    }
    if (evidence.schema !== SCHEMA)
      throw new TypeError("Unsupported evidence schema.");
    if (evidence.engineVersion !== ENGINE_VERSION)
      throw new TypeError("Unsupported engine version.");
    const keys = Object.keys(evidence).sort();
    if (
      !sameValue(keys, [
        "createdAt",
        "engineVersion",
        "label",
        "run",
        "schema",
        "sourceRevision",
      ])
    ) {
      throw new TypeError("Evidence fields do not match this schema.");
    }
    const metadata = checkedMetadata(evidence);
    if (
      !sameValue(metadata, {
        createdAt: evidence.createdAt,
        sourceRevision: evidence.sourceRevision,
        label: evidence.label,
      })
    ) {
      throw new TypeError(
        "Evidence metadata fields must be explicit and canonical.",
      );
    }
    record(evidence.run, "Evidence run");
    const run = evidence.run;
    if (
      !Array.isArray(run.frames) ||
      run.frames.length < 1 ||
      run.frames.length > MAX_STEPS + 1
    ) {
      throw new TypeError("Evidence must contain between 1 and 1001 frames.");
    }
    const recomputed = simulate(run.config);
    if (!sameValue(run, recomputed)) {
      throw new TypeError(
        "Evidence differs from an exact replay of its configuration.",
      );
    }
    return { valid: true, run: recomputed };
  } catch (error) {
    return {
      valid: false,
      error: error instanceof Error ? error.message : "Invalid evidence.",
    };
  }
}
