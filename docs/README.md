# Notes

Research notes are grouped by topic:

- [`core/`](core/) - base map identities, residue rails, and parity-vector notes.
- [`no-go/`](no-go/) - potential-function no-go theorems, tower/spine synthesis,
  and related certificate notes.
- [`density-cycles/`](density-cycles/) - survivor-density, stopping-time, and
  cycle-reduction notes.
- [`repunit/`](repunit/) - Mersenne-to-repunit structure, rail-5 analysis, tail
  merging, low-prefix obstructions, Baker diagnostics, and extremal ledgers.
- [`fuse/`](fuse/) - fuse-map and binary-fuel exploratory tracks.
- [`nested-anchor/`](nested-anchor/) - nested anchor escape and route diagnostics.
- [`diagnostics/`](diagnostics/) - broad exploratory diagnostics and probabilistic
  or entropy viewpoints.
- [`residual-atlas/`](residual-atlas/) - bounded side-project working notes for
  the residual-atlas checkpoint (`RESIDUAL_ATLAS.md`); not a claim chain.

The root [`README`](../README.md) and [`claim ledger`](../CLAIM_LEDGER.md)
remain the main entry points.

## Status hierarchy

- The claim ledger is authoritative for maintained mathematical claims.
- A note's status banner says whether it is proved, known/rederived, finite,
  conditional, open, or exploratory.
- Maintained ledger rows must already appear in the root ledger; note-local
  ledger tables are explanatory copies, not pending proposals.
- The roadmap is a chronological research record. Later checkpoints supersede
  earlier plans when they conflict.
- Files under `archive/` and root-level edit logs are provenance, not theorem
  dependencies.

## Current reading paths

For the mature no-go results, read `no-go/shadow_certificate.md`,
`no-go/leading_digit_nogo.md`, `no-go/tower_theorem.md`, and
`no-go/spine_synthesis.md`.

For the exact density result, read `density-cycles/corridor_rate.md`.

For the open repunit programme, start with
`repunit/repunit_extremal_principle.md`, then read the synchronized attack
status in `repunit/next_generation_attack_program.md` and the active PCD1--PCD17
development in `repunit/payout_concentration_diffusion.md`.
`repunit/primitive_ancestry_lemma.md` and
`repunit/general_payout_ancestry.md` supply the completed ancestry branches.
`repunit/coverage_portfolio.md` organizes these mechanisms as an ordered
residual cover and distinguishes genuine descent-or-merge rules from density
or classification results.
The root [`RESIDUAL_ATLAS.md`](../RESIDUAL_ATLAS.md) freezes IEF17 as the
live qualitative residual object and ranks the next coordinate-shrinking
lemmas. Bounded-phase working notes live in
[`residual-atlas/`](residual-atlas/).
`repunit/integral_escape_frontier.md` gives the terminal criterion: a
\(2\)-adic residual may remain nonempty if every surviving exponent acquires
nonzero high lift digits infinitely often and therefore is not a positive
integer. It also proves an exact bridge between the balanced starting-cylinder
lift and dual endpoint digit, reducing qualitative exclusion to showing that
one deterministic digit stream is not eventually zero. IEF10 completes that
step for the exact balanced itinerary using periodic Sturmian approximants and
a Baker growth bound. IEF11 extracts a general periodic-prefix discharge rule
and closes every fixed phase shift. IEF12 then uses the general repetition
theorem for Sturmian words to discharge every intercept at the critical
slope. IEF13 extends the rule to every bounded-critical-discrepancy language
with Diophantine exponent greater than \(1\), including every such language
of linear factor complexity. The remaining frontier is unbounded discrepancy
or superlinear complexity; IEF14 supplies an adaptive margin that also removes
some growing-discrepancy languages, while IEF15 finitely reduces sustained
negative-drift branches. IEF16 additionally forces every rational non-cyclic
survivor to have zero linear lower discrepancy. IEF17 records the exact
intersection left after all these rules, with cycles kept separate. IEF18
then sharpens the periodic-prefix coordinate using the directional drift that
actually contributes to rational height; IEF14 remains a coarser corollary.
IEF19 uses that estimate to discharge sublinear-drift words with repetition
exponent greater than one, leaving exponent one or positive linear excursions.
IEF20 additionally discharges fixed-surplus repetitions occurring in critical
drift windows, even when the global limsup is positive. IEF21 replaces the
full window envelope by exact terminal draw-up and endpoint-loss costs, so
internal peaks that return to a local valley are also covered.
The separate
`repunit/repunit_equidistribution_reframing.md` is an empirical strategic
diagnosis for a shortcut-map stopping-time target, not a theorem and not a
replacement for the accelerated-map proof target.
