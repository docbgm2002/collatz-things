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
`repunit/repunit_extremal_principle.md` and
`repunit/primitive_ancestry_lemma.md`, then read
`repunit/general_payout_ancestry.md`,
`repunit/payout_concentration_diffusion.md`, and the ordered research plan in
`repunit/next_generation_attack_program.md`. The separate
`repunit/repunit_equidistribution_reframing.md` is an empirical strategic
diagnosis for a shortcut-map stopping-time target, not a theorem and not a
replacement for the accelerated-map proof target.
