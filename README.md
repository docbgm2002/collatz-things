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

## Proof targets and exploratory work

These documents are useful research records but are not dependencies of the
proved-results track:

- [`descent_tree_survivors.md`](descent_tree_survivors.md) — exact spine
  anchor plus a conjectural universal survivor-density bound.
- [`repunit_tail_attack.md`](repunit_tail_attack.md) and related repunit
  automaton/normal-form notes.
- [`fuse_map_theory.md`](fuse_map_theory.md) and
  [`fuse_burn_attack.md`](fuse_burn_attack.md).
- [`fusion_fracture_cycle.md`](fusion_fracture_cycle.md),
  [`refractory_period_barrier.md`](refractory_period_barrier.md), and
  [`recharge_density_inverse_law.md`](recharge_density_inverse_law.md).
- [`Triple_Lock.md`](Triple_Lock.md) and
  [`Triple_Lock_Revised.md`](Triple_Lock_Revised.md).

The parity-itinerary note
[`Collatz_Parity_Fragility_Corrected.md`](Collatz_Parity_Fragility_Corrected.md)
proves that distinct starting values cannot share one parity-rule sequence
indefinitely. It does **not** prove that trajectories cannot later merge, or
that hypothetical cycles are metrically repelling.

## Verification

All programs use the Python standard library.

```bash
python verify_block_fracture.py
python verify_mod8_rails.py
python verify_recharge_nogo.py
python verify_exponential_potential.py
python verify_repunit_reduction.py
python verify_stopping_density.py
python verify_cycle_reduction.py
python verify_tree_survivors.py
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
7. `stopping_time_density.md`
8. `cycle_reduction.md`

## Contribution standard

A universal statement belongs in the proved-results track only when:

- its domain and quantifiers are explicit;
- the proof covers all edge cases;
- every dependency is already proved;
- the verifier tests the same claim the prose states;
- finite experiments are not used to replace an unbounded argument;
- the note states exactly what remains open.
