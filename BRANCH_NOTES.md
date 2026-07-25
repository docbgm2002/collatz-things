# Branch `no-go-general` — read this first

**Not human-reviewed.** Machine-verified only. Ten verifiers, all exact integer or
rational arithmetic, all passing. A passing verifier is not a proof read.

## What this branch does

It answers the open Question posed in `\section{The boundary}` of
`mersenne_obstructions.tex`, and refutes the claim made just above it.

That section currently states that a closed certificate over
`(⌊2^j log₂x⌋, τ, x mod 2^m)` needs total gain in `(0, 2^{-j})`, which "pure shadows
cannot supply", with "no uniform construction known". This is refuted by construction:
the bound holds for single-witness chains only. Multi-witness cycles reset in-cell
position at every junction, and the correct criterion is exact and integral.

The section then asks whether a nonincreasing potential of that form exists. Answer:
**no**, for j ≤ 8 by explicit certificates, and at (j,m) = (3,16) at *every height* by
the infinite family x₁ = 2ⁿ + 27, n ≥ 10.

## Two things went further than expected

- **SHG1** — SH1's proof uses nothing about 3 and 2. It generalises to any
  `T(x) = (ax+b)/c^{v_c(ax+b)}` with an expanding rational cycle. The pair (3,2) enters
  at exactly one point, the `len` coordinate, where it becomes the dichotomy
  `a^K/c^E < c`. This makes the result a ranking-function non-existence theorem for
  piecewise-affine integer loops, which is a live open area in program verification.
- **DICH1** — the whole mechanism is present precisely when `log_c a` is irrational, and
  absent (`a = c^k`) exactly when the map is elementarily analysable.

## Read in this order

1. `docs/no-go/suff1.md` — step 4 is the least carefully argued line on the branch.
2. `docs/no-go/cost_law_proof.md` — step 6 is Khinchin applied, not reproved.
3. `docs/no-go/uniformity.md` — the 0.24 rate is a finite certificate for one word
   ordering, not a theorem about all orderings.

## Run everything

```bash
for s in scripts/verify_general_shadow.py scripts/verify_general_cost_law.py \
         scripts/verify_cost_law_proof.py scripts/verify_quantized_log_criterion.py \
         scripts/verify_quantized_log_witnesses.py scripts/verify_sufficiency_reduction.py \
         scripts/verify_tau_coupling.py scripts/verify_uniformity.py \
         scripts/verify_suff1_composition.py scripts/verify_storage_exchange_rate.py; do
  printf "%-46s " "$s"; python3 "$s" | tail -1
done
```

## Known-open

- Strong connectivity of the mod-2^m automaton for **all** m (verified 3..14).
- The general (a,b,c) form of the SUFF1 composition.
- Manuscript §6 / Theorem E LaTeX is still not written; QLG1's row says so.

## A caveat about how this was produced

This branch was generated in a single assistant session. That is structurally the same
pattern flagged as an audit concern for the 2026-07-03 rail-5 commit: a large block of
"Proved here" landing at once without a human proof read. The verifiers caught three
errors during the session (a missing height hypothesis, a bounded scan used to test an
existential claim, and a wrong starting index) — evidence they work, and equally
evidence that errors were being produced at a rate that matters. Treat the labels as
provisional until read.
