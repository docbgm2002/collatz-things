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
| L6 tool request (\(\mathcal L_{3/4}\) alone) | **Discharged** | IEF22--IEF24 (2026-07-19) |

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
- [x] Named L6 tool request recorded for \(\mathcal L_{3/4}\) alone
      (discharged by IEF22--IEF24; see below)

### L6 local discharge (2026-07-19)

For itineraries already inside the mechanical terminal language
\(\mathcal L_{3/4}\), the Diophantine core formerly left as an L6-style
tool request is discharged by ledger claims:

- **IEF22** — Theorem G: the zero-digit residue graph \(\mathcal G\) is
  functional and has no infinite forward path;
- **IEF23** — the IEF4 dual-digit stream is never eventually zero;
- **IEF24** — with IEF7, no positive integer realizes an infinite
  \(\mathcal L_{3/4}\) itinerary in the integrality sense.

Thus \(\mathcal R\) contains no positive-integer survivor. This does **not**
reopen L5 or reverse demote-1: emptying \(\mathcal R\) remains classification
inside \(\mathcal L_{3/4}\), not a cover of blocked-diffuse primitives.

### Operational rules after demote-1

1. Do **not** present emptying \(\mathcal R\) as qualitative repunit-tail
   descent.
2. Retain IEF1--IEF24 as theorems about the mechanical \(3/4\)-block
   language (IEF22--IEF24 discharge the local residual).
3. Return the primary spine programme to
   `docs/no-go/avenue_a_comparison_dynamics.md` (first-descent
   storage-dominance SD1), with
   `docs/repunit/next_generation_attack_program.md` /
   `RESEARCH_ROADMAP.md` as the chronological programme.
4. Optional local atlas work: L2--L4 falsification **inside**
   \(\mathcal L_{3/4}\) only, scored as structure of that language, not as
   a cover of \(\mathcal B\).

## Notes

Main bet remains outside this folder until a future phase reopens with a
genuine cover lemma (new L5) or a real exotic normal form. Live spine work
is Avenue A / SD1 in `docs/no-go/avenue_a_comparison_dynamics.md`.
