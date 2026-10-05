import test from "node:test";
import assert from "node:assert/strict";
import {
  ENGINE_VERSION,
  normalizeConfig,
  simulate,
  makeEvidence,
  verifyEvidence,
} from "../engine.mjs";

test("standard Collatz examples preserve elementary counts and peaks", () => {
  for (const [seed, steps, peak] of [
    ["9", 19, "52"],
    ["27", 111, "9232"],
  ]) {
    const run = simulate({ seed });
    assert.equal(run.outcome.type, "home");
    assert.equal(run.steps, steps);
    assert.equal(run.elementarySteps, steps);
    assert.equal(run.peak, peak);
    assert.equal(run.frames.at(-1).value, "1");
    assert.equal(run.frames.length, steps + 1);
  }
});

test("accelerated odd steps expose skipped divisions and correct elementary count", () => {
  const run = simulate({ seed: "9", mode: "odd" });
  assert.deepEqual(
    run.frames.map((frame) => frame.value),
    ["9", "7", "11", "17", "13", "5", "1"],
  );
  assert.deepEqual(
    run.frames.map((frame) => frame.divisions),
    [0, 2, 1, 1, 2, 3, 4],
  );
  assert.deepEqual(
    run.frames.map((frame) => frame.elementarySteps),
    [0, 3, 5, 7, 10, 14, 19],
  );
  assert.equal(run.steps, 6);
  assert.equal(run.elementarySteps, 19);
  assert.equal(run.peak, "17");
  assert.equal(run.frames[1].kind, "contract");
  assert.equal(run.frames[2].kind, "expand");
});

test("3n-1 detects a repeated value and records exact cycle boundaries", () => {
  const run = simulate({ seed: "5", offset: "-1" });
  assert.deepEqual(
    run.frames.map((frame) => frame.value),
    ["5", "14", "7", "20", "10", "5"],
  );
  assert.equal(run.outcome.type, "cycle");
  assert.equal(run.outcome.cycleStart, 0);
  assert.equal(run.outcome.cycleLength, 5);
  assert.equal(run.steps, 5);
});

test("5n+1 has a transient before its cycle in both display modes", () => {
  const standard = simulate({ seed: "5", multiplier: "5" });
  assert.equal(standard.outcome.type, "cycle");
  assert.equal(standard.outcome.cycleStart, 1);
  assert.equal(standard.outcome.cycleLength, 10);
  assert.equal(standard.frames.at(-1).value, "26");
  const odd = simulate({ seed: "5", multiplier: "5", mode: "odd" });
  assert.deepEqual(
    odd.frames.map((frame) => frame.value),
    ["5", "13", "33", "83", "13"],
  );
  assert.equal(odd.outcome.cycleStart, 1);
  assert.equal(odd.outcome.cycleLength, 3);
  assert.equal(odd.elementarySteps, 12);
});

test("1 is an explicit home convention including for alternate rules", () => {
  const run = simulate({ seed: "1", multiplier: "9", offset: "-9" });
  assert.equal(run.outcome.type, "home");
  assert.equal(run.steps, 0);
  assert.equal(run.frames.length, 1);
  assert.match(run.outcome.message, /convention/);
});

test("nonpositive outputs stop without introducing invalid positive-integer frames", () => {
  for (const mode of ["standard", "odd"]) {
    const zero = simulate({ seed: "3", multiplier: "1", offset: "-3", mode });
    assert.equal(zero.outcome.type, "invalid");
    assert.equal(zero.steps, 0);
    assert.match(zero.outcome.message, /= 0/);
    const negative = simulate({ seed: "6", multiplier: "1", offset: "-9" });
    assert.deepEqual(
      negative.frames.map((frame) => frame.value),
      ["6", "3"],
    );
    assert.equal(negative.outcome.type, "invalid");
    assert.equal(negative.elementarySteps, 1);
  }
});

test("terminal events at the budget boundary take precedence over an unresolved limit", () => {
  assert.equal(simulate({ seed: "2", maxSteps: 1 }).outcome.type, "home");
  assert.equal(
    simulate({ seed: "5", offset: "-1", maxSteps: 5 }).outcome.type,
    "cycle",
  );
  const run = simulate({ seed: "9", maxSteps: 2 });
  assert.equal(run.outcome.type, "limit");
  assert.equal(run.steps, 2);
  assert.deepEqual(
    run.frames.map((frame) => frame.value),
    ["9", "28", "14"],
  );
});

test("odd mode detects one-step fixed points away from home", () => {
  const run = simulate({
    seed: "3",
    multiplier: "1",
    offset: "3",
    mode: "odd",
  });
  assert.equal(run.outcome.type, "cycle");
  assert.equal(run.outcome.cycleLength, 1);
  assert.equal(run.frames[1].kind, "steady");
  assert.equal(run.frames[1].elementarySteps, 2);
});

test("configuration validation rejects unsafe, ambiguous, and out-of-bounds input", () => {
  const invalid = [
    { seed: 9007199254740993 },
    { seed: "0" },
    { seed: "-9" },
    { seed: "9.0" },
    { seed: "1e6" },
    { seed: " 9 " },
    { seed: "9".repeat(61) },
    { seed: "2", mode: "odd" },
    { multiplier: 0 },
    { multiplier: 2 },
    { multiplier: 11 },
    { offset: 0 },
    { offset: 2 },
    { offset: -11 },
    { mode: "fast" },
    { maxSteps: 0 },
    { maxSteps: 1001 },
    { maxSteps: 1.5 },
    { maxSteps: "10" },
  ];
  for (const config of invalid)
    assert.throws(
      () => normalizeConfig(config),
      undefined,
      JSON.stringify(config),
    );
  assert.deepEqual(
    normalizeConfig({ seed: "0009", multiplier: 3, offset: -1, maxSteps: 1 }),
    {
      seed: "9",
      multiplier: "3",
      offset: "-1",
      mode: "standard",
      maxSteps: 1,
    },
  );
  assert.equal(normalizeConfig({ seed: "9".repeat(60) }).seed.length, 60);
});

test("numbers beyond floating-point precision remain exact", () => {
  const seed = "9007199254740993";
  const run = simulate({ seed, maxSteps: 2 });
  assert.equal(run.frames[1].value, "27021597764222980");
  assert.equal(run.frames[2].value, "13510798882111490");
  assert.equal(run.peak, "27021597764222980");
});

test("accelerated values agree with filtering an independently implemented elementary trace", () => {
  for (const a of [1n, 3n, 5n, 7n, 9n]) {
    for (const b of [-3n, -1n, 1n, 3n]) {
      for (const seed of [3n, 5n, 9n, 27n]) {
        const run = simulate({
          seed,
          multiplier: a,
          offset: b,
          mode: "odd",
          maxSteps: 12,
        });
        let n = seed;
        let count = 0;
        for (const frame of run.frames.slice(1)) {
          n = a * n + b;
          count += 1;
          while (n % 2n === 0n) {
            n /= 2n;
            count += 1;
          }
          assert.equal(frame.value, String(n));
          assert.equal(frame.elementarySteps, count);
        }
      }
    }
  }
});

const provenance = {
  sourceRevision: "example-revision",
  createdAt: "2026-10-05T14:00:00.000Z",
  label: "Replayable example",
};

test("evidence round-trips a replay, with metadata separate from mathematical validation", () => {
  const run = simulate({ seed: "27", mode: "odd" });
  const evidence = JSON.parse(JSON.stringify(makeEvidence(run, provenance)));
  assert.equal(evidence.engineVersion, ENGINE_VERSION);
  assert.equal(evidence.sourceRevision, "example-revision");
  const result = verifyEvidence(evidence);
  assert.equal(result.valid, true);
  assert.deepEqual(result.run, run);
  evidence.label = "Metadata does not prove authorship";
  assert.equal(verifyEvidence(evidence).valid, true);
});

test("evidence replay rejects tampered arithmetic, limits, outcomes, totals, and extra fields", () => {
  const original = makeEvidence(
    simulate({ seed: "9", mode: "odd" }),
    provenance,
  );
  const mutations = [
    (e) => {
      e.run.frames[1].value = "8";
    },
    (e) => {
      e.run.frames[1].operation = "Trust me";
    },
    (e) => {
      e.run.frames[1].divisions = 3;
    },
    (e) => {
      e.run.frames[1].elementarySteps = 100;
    },
    (e) => {
      e.run.config.multiplier = "5";
    },
    (e) => {
      e.run.config.maxSteps = 0;
    },
    (e) => {
      e.run.config.seed = "9".repeat(61);
    },
    (e) => {
      e.run.config.seed = 9;
    },
    (e) => {
      e.run.outcome.type = "cycle";
    },
    (e) => {
      e.run.peak = "999";
    },
    (e) => {
      e.run.steps = 8;
    },
    (e) => {
      e.run.elementarySteps = 8;
    },
    (e) => {
      e.run.frames.pop();
    },
    (e) => {
      e.run.frames[0].untrusted = "extra";
    },
    (e) => {
      e.run.claim = "all numbers converge";
    },
    (e) => {
      e.engineVersion = "unrecognized";
    },
    (e) => {
      e.schema = "unrecognized";
    },
    (e) => {
      e.createdAt = "invalid";
    },
    (e) => {
      e.createdAt = null;
    },
    (e) => {
      e.sourceRevision = undefined;
    },
    (e) => {
      e.extra = true;
    },
    (e) => {
      delete e.label;
    },
  ];
  for (const mutate of mutations) {
    const evidence = structuredClone(original);
    mutate(evidence);
    assert.equal(verifyEvidence(evidence).valid, false, mutate.toString());
  }
  const reversed = Object.fromEntries(Object.entries(original).reverse());
  assert.equal(verifyEvidence(reversed).valid, true);
});

test("malformed or oversized imports fail safely and evidence creation rejects fabricated runs", () => {
  for (const value of [null, [], 3, "evidence", {}, { schema: "unknown" }]) {
    assert.equal(verifyEvidence(value).valid, false);
  }
  const evidence = makeEvidence(simulate({ seed: "9" }), provenance);
  evidence.label = "x".repeat(8 * 1024 * 1024);
  assert.equal(verifyEvidence(evidence).valid, false);
  const fabricated = simulate({ seed: "9" });
  fabricated.peak = "42";
  assert.throws(() => makeEvidence(fabricated, provenance), /exact replay/);
  assert.throws(
    () => makeEvidence(simulate(), { createdAt: "2026-02-31T00:00:00.000Z" }),
    /timestamp/,
  );
});
