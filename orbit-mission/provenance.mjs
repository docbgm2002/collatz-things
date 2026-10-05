/**
 * Curated repository history, checked against git at sourceRevision.
 * Authors and titles are literal git metadata; descriptions explain scope.
 * This baseline identifies the research source, not the app's build commit.
 */
export const PROVENANCE = Object.freeze({
  appVersion: "0.1.0",
  sourceRevision: "fee9b8e613c05d5a35aebab757abc5c9e1d80a16",
  repository: "https://github.com/docbgm2002/collatz-things",
  changes: [
    {
      hash: "fee9b8e613c05d5a35aebab757abc5c9e1d80a16",
      author: "drbrym",
      date: "2026-10-05",
      title:
        "Merge pull request #4 from NiyiOke/Niyi/fix-macro-step-affine-drift",
      url: "https://github.com/docbgm2002/collatz-things/pull/4",
      meaning:
        "Merged the affine correction into the research repository. This is the research baseline used by Orbit Mission 0.1.0.",
    },
    {
      hash: "5728adb606a704c5e887586eddae4f795bed274d",
      author: "NiyiOke",
      date: "2026-10-05",
      title: "Fix macro-step affine drift and scope multiplier bounds",
      url: "https://github.com/docbgm2002/collatz-things/commit/5728adb606a704c5e887586eddae4f795bed274d",
      meaning:
        "Restored the accumulated +1 terms when comparing actual trajectories with multiplication alone, and narrowed the scope of the escape-bound claims. It corrects the explanation, not the classic Collatz rule.",
    },
    {
      hash: "7f40e95d13133af1ea0f89eadbeeb4b8b6c4f3aa",
      author: "Claude (session assistant)",
      date: "2026-07-25",
      title:
        "no-go: prove strong connectivity; SUFF1 becomes unconditional [CONN1]",
      url: "https://github.com/docbgm2002/collatz-things/commit/7f40e95d13133af1ea0f89eadbeeb4b8b6c4f3aa",
      meaning:
        "A model-labelled git author recorded a claim in the potential-function research track. The title is repository history; this app does not independently validate that claim or present it as a proof of Collatz.",
    },
    {
      hash: "bb21fd327dd0ef388f2eae9bc15503905d6d263f",
      author: "drbrym",
      date: "2026-07-13",
      title: "Develop integral escape residual frontier",
      url: "https://github.com/docbgm2002/collatz-things/commit/bb21fd327dd0ef388f2eae9bc15503905d6d263f",
      meaning:
        "Added research notes and exact computational tools for constrained families of Collatz steps. Those tools investigate specific arithmetic questions beyond this introductory game.",
    },
    {
      hash: "fcee770645889a047f316a6199e8ef6eb3dc6f6d",
      author: "drbrym",
      date: "2026-06-18",
      title:
        "fix(correctness): comprehensive overclaim and proof-error correction pass",
      url: "https://github.com/docbgm2002/collatz-things/commit/fcee770645889a047f316a6199e8ef6eb3dc6f6d",
      meaning:
        "Introduced the claim ledger and canonical notation, corrected proof errors, and separated conjectures and finite experiments from established results.",
    },
    {
      hash: "ba5afac0a7d2aab2a94fe08587e8604c38b933b5",
      author: "docbgm2002",
      date: "2025-11-28",
      title: "Initial commit",
      url: "https://github.com/docbgm2002/collatz-things/commit/ba5afac0a7d2aab2a94fe08587e8604c38b933b5",
      meaning:
        "Started the repository. Later corrections and the current claim ledger determine how its historical material should be read.",
    },
  ],
});

/** Curated choices for the odd branch; the even branch always divides by 2. */
export const RULES = Object.freeze([
  {
    id: "classic",
    title: "Classic · 3n + 1",
    multiplier: 3,
    offset: 1,
    description:
      "If the number is odd, multiply by 3 and add 1. If it is even, divide by 2. The Collatz conjecture asks whether every positive starting number eventually reaches 1.",
    status: "Classic rule",
  },
  {
    id: "minus",
    title: "Alternative · 3n − 1",
    multiplier: 3,
    offset: -1,
    description:
      "Change the odd move to multiply by 3 and subtract 1. Start at 5 to discover the standard-step cycle 5 → 14 → 7 → 20 → 10 → 5. This is a different recurrence.",
    status: "Experimental variant",
  },
  {
    id: "five",
    title: "Alternative · 5n + 1",
    multiplier: 5,
    offset: 1,
    description:
      "Change the odd move to multiply by 5 and add 1. Compare its route with the classic rule: some starts repeat in cycles away from 1. This is a different recurrence.",
    status: "Experimental variant",
  },
]);
