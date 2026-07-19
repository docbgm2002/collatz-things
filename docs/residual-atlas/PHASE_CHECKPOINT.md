# Phase checkpoint — residual atlas

**Status:** **Demote outcome 1 (cover failure).** Bounded side-project phase
closed for promotion. Local work inside \(\mathcal L_{3/4}\) may continue as
classification only.

Parent scoreboard: [`RESIDUAL_ATLAS.md`](../../RESIDUAL_ATLAS.md) §7.

## Phase checklist

| Step | Status | Note |
|---|---|---|
| L1 established | Done | `L1_coordinate_split.md` |
| L5 theorem target formalized | Done | definitions frozen |
| L5 checklist completed | Done | §2 of L5 note |
| L5 eventual-entry with \(\mathcal E=\emptyset\) | **Falsified (F-01)** | \(n=471\) |
| \(\mathcal E_{\mathrm{mix}}\) normal form | **Failed** | `E_mix_seed.md`; full 732-step descent |
| L2 falsification attempts | Partial | F-02; continue only as local study |
| L3 falsification attempts | Partial | same |
| L4 falsification attempts | Done (F-04) | no falsifier; local wall only |
| Promote / demote decision | **Demote-1** | below |

## Decision

**Date:** 2026-07-14

**Decision:** demote-1 (cover failure)

**Evidence summary:**

- F-01: unique finite blocked-diffuse primitive seed \(n=471\) lies outside
  \(\mathcal L_{3/4}\) for every tested preperiod.
- Full-tail probe: descent at step 732; payout alphabet
  \(\{2,3,4,5,6,7,8\}\); no mechanical \(3/4\) suffix; no usable periodic
  payout/gap normal form (`E_mix_seed.md`).
- Therefore \(\mathcal R\) (defined inside \(\mathcal L_{3/4}\)) does not
  cover blocked-diffuse primitives, and \(\mathcal E_{\mathrm{mix}}\) was
  not upgraded from seed to named exotic class.

**Consequence for main programme:**

- [x] Atlas retained as classification framework only
- [x] Atlas remains side project only (not a descent route)
- [ ] Atlas promoted as qualitative descent route
- [ ] Named L6 tool request recorded (optional later, for \(\mathcal L_{3/4}\) alone)

### Operational rules after demote-1

1. Do **not** present emptying \(\mathcal R\) as qualitative repunit-tail
   descent.
2. Retain IEF1--IEF21 as theorems about the mechanical \(3/4\)-block
   language.
3. Return the primary spine programme to
   `docs/repunit/next_generation_attack_program.md` /
   `RESEARCH_ROADMAP.md` (ancestry, PCD non-atlas branches, surplus).
4. Optional local atlas work: L2--L4 falsification **inside**
   \(\mathcal L_{3/4}\) only, scored as structure of that language, not as
   a cover of \(\mathcal B\).

## Notes

Main bet remains outside this folder until a future phase reopens with a
genuine cover lemma (new L5) or a real exotic normal form.
