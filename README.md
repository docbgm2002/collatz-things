# Collatz structural notes

This repository studies the accelerated odd Collatz map

\[
f(x)=\frac{3x+1}{2^{v_2(3x+1)}}\qquad(x\text{ odd}).
\]

It does **not** contain a proof of the Collatz conjecture. Its maintained
results are a mixture of exact identities, a rederivation of a known density
theorem, bounded computational certificates, and explicitly labelled proof
targets.

Start with:

- [`NOTATION.md`](NOTATION.md) for the canonical map and symbols.
- [`CLAIM_LEDGER.md`](CLAIM_LEDGER.md) for the authoritative status of every
  maintained claim.

## Proved-results track

### Binary and residue structure

- [`Block_Fracture_Lemma.md`](Block_Fracture_Lemma.md)
  proves
  \(3(2^L-1)=\texttt{10}1^{L-2}\texttt{01}\), a protected interior
  consecutive-one window for an isolated block, and the exact first odd-step
  from a Mersenne number.
- [`Mod8_Rail_Descent.md`](Mod8_Rail_Descent.md)
  proves immediate descent on residues \(1\) and \(5\bmod8\), an exact
  fixed-division bridge on residue \(3\bmod8\), and the finite rail-\(7\)
  stay recursion.
- [`collatz_rail7_new_results.md`](collatz_rail7_new_results.md)
  gives the closed form for the rail-\(7\) recursion and its Mersenne-index
  escape formulas.

### Mersenne structure and potential limitations

- [`recharge_nogo.md`](recharge_nogo.md)
  proves that no potential of the form
  \(\log_2x+g(v_2(x+1))\) is globally nonincreasing, and derives the exact
  Mersenne burn ledger.
- [`mersenne_repunit_reduction.md`](mersenne_repunit_reduction.md)
  reduces the Mersenne trajectory after its closed-form burn to the base-\(3\)
  repunit \((3^n-1)/2\) for odd \(n\).
- [`repunit_rail5_exact.md`](repunit_rail5_exact.md)
  classifies the initial mod-\(8\) rails of odd-indexed base-\(3\) repunits,
  proves that a natural-density \(5/8\) of the family reaches rail \(5\) on
  step \(0\) or \(1\), and records a separate bounded \(12\)-step observation.
- [`repunit_rail5_density.md`](repunit_rail5_density.md)
  extends the \(5/8\) result to every fixed time: the density avoiding rail
  \(5\) through step \(K\) is exactly
  \(\frac12(3/4)^K\), so almost every odd-indexed repunit eventually reaches
  rail \(5\).
- [`repunit_affine_tail_bound.md`](repunit_affine_tail_bound.md)
  proves that the affine correction in the repunit-tail ledger is
  exponentially small throughout every pre-descent linear window.
- [`repunit_tail_merge_reduction.md`](repunit_tail_merge_reduction.md)
- [`repunit_gap_merger_analysis.md`](repunit_gap_merger_analysis.md)
- [`repunit_gap2_sync_tree.md`](repunit_gap2_sync_tree.md)
- [`repunit_multigap_sync_union.md`](repunit_multigap_sync_union.md)
- [`repunit_collision_defect_dynamics.md`](repunit_collision_defect_dynamics.md)
  gives an exact diagonal-state merge criterion and a merge-inheritance
  induction principle.
- [`repunit_256_block_target.md`](repunit_256_block_target.md)
  isolates a conditional 256-valuation floor which would prove descent of
  every odd-indexed repunit tail.
- [`repunit_low_prefix_obstruction.md`](repunit_low_prefix_obstruction.md)
  constructs explicit low-valuation repunit prefixes, showing that any fixed
  block-floor proof must use off-diagonal merging or a recovery mechanism.
- [`repunit_baker_nonshadowing.md`](repunit_baker_nonshadowing.md)
- [`repunit_baker_applicability_census.md`](repunit_baker_applicability_census.md)
- [`repunit_enemy_episode_analysis.md`](repunit_enemy_episode_analysis.md)
  proves that positive integer exponents cannot shadow the
  \(3^{\alpha+1}=-7\) ghost branch for more than \(O(\log n)\) steps, via
  Yu's \(p\)-adic Baker theorem.
- [`Exponential_Decay_Potential.md`](Exponential_Decay_Potential.md)
  proves descent of a bounded bit-weight potential on one explicit recharge
  family. Its epoch-wide behaviour is only a finite certificate, and it is not
  a global Lyapunov function.

### Density and cycles

- [`stopping_time_density.md`](stopping_time_density.md)
  gives a self-contained rederivation of the Terras/Everett almost-everywhere
  finite-stopping-time theorem with an explicit geometric bound. This is a
  known theorem, not a new resolution of the exceptional set.
- [`cycle_reduction.md`](cycle_reduction.md)
  proves the affine cycle equation and records carefully bounded finite
  searches. It does not exclude all nontrivial cycles.

## Finite certificates

The following statements are exhaustive only over their stated bounds:

- Every odd \(x\le10^6\) descends below itself within at most 111 odd-steps.
- The decayed-bit potential decreases across every tested first-descent epoch
  for odd \(x\le10^6\) with \(c=r=0.2\).
- The bounded cycle-pattern search documented in `cycle_reduction.md` finds
  only \(x=1\).
- The measured descent-tree survivor fractions satisfy the reported bounds
  for \(6\le K\le20\).
- Every tested odd-indexed repunit \(a_n\), \(3\le n\le199\), reaches rail
  \(5\bmod8\) within at most 12 odd-steps.

## Proof targets and exploratory work

These documents are useful research records but are not dependencies of the
proved-results track:

- [`entropy_nonshadowing_theory.md`](entropy_nonshadowing_theory.md) — alternative Entropy and Kolmogorov Complexity track.
- [`descent_tree_survivors.md`](descent_tree_survivors.md) — exact spine
  anchor plus a conjectural universal survivor-density bound.
- [`repunit_tail_attack.md`](repunit_tail_attack.md) and related repunit
  automaton/normal-form notes.
- [`fuse_map_theory.md`](fuse_map_theory.md) and
  [`fuse_burn_attack.md`](fuse_burn_attack.md).

The parity-itinerary note
[`Collatz_Parity_Fragility_Corrected.md`](Collatz_Parity_Fragility_Corrected.md)
proves that distinct starting values cannot share one parity-rule sequence
indefinitely. It does **not** prove that trajectories cannot later merge, or
that hypothetical cycles are metrically repelling.

## Archive

Superseded thermodynamic heuristics, legacy cycle summaries, and exploratory
precursors are retained under [`archive/`](archive/README.md). They are
historical records, not part of the maintained claim chain.

## Verification

All programs use the Python standard library.

```bash
python verify_block_fracture.py
python verify_mod8_rails.py
python verify_recharge_nogo.py
python verify_exponential_potential.py
python verify_repunit_reduction.py
python verify_repunit_rail5.py
python verify_repunit_rail5_density.py
python verify_repunit_affine_tail.py
python verify_repunit_tail_merges.py
python verify_repunit_gap_mergers.py
python explore_repunit_sync_tree.py --through-step 7 --max-total 24 --common-depth 24
python verify_repunit_sync_union.py
python verify_repunit_collision_defect.py
python verify_repunit_256_block.py
python verify_repunit_low_prefix.py
python verify_repunit_baker_nonshadowing.py
python explore_baker_applicability.py --limit 5001
python explore_repunit_enemy_episodes.py --limit 10001 --min-run 1
python verify_stopping_density.py
python verify_cycle_reduction.py
python verify_tree_survivors.py
python verify_entropy_balance.py
```

Interpret the output according to the claim ledger:

- symbolic identities and human proofs support universal claims;
- exhaustive loops support only their printed finite ranges;
- random sampling and `explore_*.py` output are evidence, not proofs.

## Suggested reading order

1. `NOTATION.md`
2. `CLAIM_LEDGER.md`
3. `Block_Fracture_Lemma.md`
4. `Mod8_Rail_Descent.md`
5. `recharge_nogo.md`
6. `mersenne_repunit_reduction.md`
7. `repunit_rail5_exact.md`
8. `repunit_rail5_density.md`
9. `stopping_time_density.md`
10. `cycle_reduction.md`

## Contribution standard

A universal statement belongs in the proved-results track only when:

- its domain and quantifiers are explicit;
- the proof covers all edge cases;
- every dependency is already proved;
- the verifier tests the same claim the prose states;
- finite experiments are not used to replace an unbounded argument;
- the note states exactly what remains open.
