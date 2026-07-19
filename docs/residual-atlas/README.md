# Residual atlas side project

**Status:** Bounded research phase **closed for promotion** (demote-1).
Not the main programme bet. Local \(\mathcal L_{3/4}\) studies may continue
as classification only.

This folder holds working notes for the residual-atlas checkpoint described in
the root scoreboard [`RESIDUAL_ATLAS.md`](../../RESIDUAL_ATLAS.md).

## Why a separate folder

- Keep exploratory formalizations and falsification logs out of the proved
  `docs/repunit/` claim chain.
- Make promote / demote of the atlas a visible decision, not a silent drift
  of the main roadmap.
- Allow scripts and diagnostics here (or under `scripts/` with an `atlas_`
  prefix) without implying ledger claims.

## Contents

| File | Role |
|---|---|
| [`L1_coordinate_split.md`](L1_coordinate_split.md) | Bookkeeping partition of coordinate C |
| [`L5_terminal_language_target.md`](L5_terminal_language_target.md) | Exact statement L5 must prove |
| [`E_mix_seed.md`](E_mix_seed.md) | Failed normal-form attempt; supports demote-1 |
| [`falsification_log.md`](falsification_log.md) | Adversarial attempts at L2--L5 |
| [`PHASE_CHECKPOINT.md`](PHASE_CHECKPOINT.md) | **Demote-1 recorded** |

Supporting scripts:

- `scripts/explore_atlas_l5_language.py`
- `scripts/explore_atlas_emix_probe.py`
- `scripts/explore_atlas_l4_peak_crash.py`

## Phase order

1. Finish L1.
2. Freeze the L5 theorem target (even before a proof).
3. Falsify L2--L4 implications against constructed itineraries.
4. Record promote or demote in `PHASE_CHECKPOINT.md`.

## Relation to maintained claims

Nothing in this folder is a ledger claim until promoted through
`CLAIM_LEDGER.md` with the usual admission rule. IEF1--IEF21 remain in
`docs/repunit/integral_escape_frontier.md`.
