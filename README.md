# Collatz structural notes

This repository studies the accelerated odd Collatz map

\[
f(x)=\frac{3x+1}{2^{v_2(3x+1)}}\qquad(x\text{ odd}).
\]

It does **not** contain a proof of the Collatz conjecture. Its maintained
results are a mixture of exact identities, no-go theorems for
potential-function methods, a rederivation of known density theorems, an
exact survivor-density rate theorem, bounded computational certificates,
and explicitly labelled proof targets.

Start with:

- [`NOTATION.md`](NOTATION.md) for the canonical map and symbols.
- [`CLAIM_LEDGER.md`](CLAIM_LEDGER.md) for the authoritative status of every
  maintained claim.
- [`docs/README.md`](docs/README.md) for the topic-organized note index.
- [`mersenne_obstructions.tex`](mersenne_obstructions.tex) — the
  consolidated manuscript *No-Go Theorems for One-Step Lyapunov Potentials
  for the 3x+1 Map* (Theorems A–D below), with compiled PDF.

## Proved-results track

### No-go theorems for one-step potentials

- [`docs/no-go/shadow_certificate.md`](docs/no-go/shadow_certificate.md)
  **(SH1, master theorem).** Shadowing the expanding rational cycle
  \(-5\mapsto-7\) at positive integers \(x\equiv-5\bmod 2^N\) proves: no
  potential \(\log_2x+g(x\bmod2^m,\,\tau,\,\mathrm{len},\,
  \lambda_1..\lambda_d)\) is nonincreasing, for any modulus, any detector
  depths, and any \(g\). Smallest certificate:
  \(1275\mapsto1913\mapsto1435\). General principle: every expanding
  rational cycle (\(2^E<3^K\)) is a certificate factory.
- [`docs/no-go/leading_digit_nogo.md`](docs/no-go/leading_digit_nogo.md)
  **(SH2).** Iterating the shadow and applying Dirichlet approximation to
  \(\log_2\frac98\) extends the exclusion to corrections using any fixed
  number of leading binary digits.
- [`docs/no-go/spine_synthesis.md`](docs/no-go/spine_synthesis.md)
  **(BND1).** No potential \(\log_2x+G(x)\) with bounded \(G\), of
  arbitrary dependence, is nonincreasing (one paragraph from the Mersenne
  burn). Also **(SPN1)**: the complete exact lane — tower \(\to\) Mersenne
  \(\to\) burn \(\to\) repunit, length \(d+M+1\), with exact payout
  \(e^\star=2+v_2(1+3^{d-1}s)\); every tower member lies on rail \(8y+1\).
- [`docs/no-go/no_local_potential.md`](docs/no-go/no_local_potential.md) **(NLP1)** and
  [`docs/no-go/nlp2_alternation.md`](docs/no-go/nlp2_alternation.md) **(NLP2)** — the original
  family-method proofs (burn/recharge scissors) for the residue-and-fuel
  subclasses. Subsumed by SH1 as impossibility statements; retained for
  the exact price mechanism (each detector level costs a would-be
  potential exactly \(\log_2\frac43\) against an unbounded liability) and
  the historical proof path.
- [`docs/no-go/fuel_fraction_nogo.md`](docs/no-go/fuel_fraction_nogo.md) **(FFN1)** — the
  \((\tau,\mathrm{len})\) class by explicit 11-witness certificate.
  Subsumed by SH1; retained for the certificate method exposition.
- `scripts/verify_nogo_certificate.py` (not present in this checkout) — the
  planned logically independent verification: no-go constraint systems on
  finite coordinate windows are difference-constraint systems, infeasible iff
  the coordinate graph of raw orbit steps contains a cycle of ratio-product
  \(>1\); Bellman–Ford mining plus exact rational confirmation.

The surviving one-step class reads the quantized full logarithm
\(\lfloor2^j\log_2x\rfloor\); see the manuscript's boundary section. This
is where the no-go program terminates.

### The Mersenne ancestry tower

- [`docs/no-go/tower_theorem.md`](docs/no-go/tower_theorem.md)
  **(TWR1).** For every depth \(d\) and \(M\equiv1\bmod 2\cdot3^{d-1}\),
  \(w_d(M)=(2^{M+2d}-2^{2d+1}+3^d)/3^d\) satisfies
  \(f^d(w_d(M))=2^M-1\) with every step an \(e{=}2\) step; exact
  carry-free periodic binary normal form of period \(2\cdot3^{d-1}\)
  (via LTE); frozen 2-adic tails separating at bit \(2\min(d,d')+1\).
  Resolves the hierarchy conjecture of
  [`docs/no-go/latent_fuel_notes.md`](docs/no-go/latent_fuel_notes.md). Also **(NLPD)**, the
  unconditional detector no-go, now subsumed by SH1.

### Binary and residue structure

- [`docs/core/Block_Fracture_Lemma.md`](docs/core/Block_Fracture_Lemma.md)
  proves \(3(2^L-1)=\texttt{10}1^{L-2}\texttt{01}\), a protected interior
  consecutive-one window for an isolated block, and the exact first
  odd-step from a Mersenne number.
- [`docs/core/Mod8_Rail_Descent.md`](docs/core/Mod8_Rail_Descent.md)
  proves immediate descent on residues \(1\) and \(5\bmod8\), an exact
  fixed-division bridge on residue \(3\bmod8\), and the finite rail-\(7\)
  stay recursion.
- [`docs/core/collatz_rail7_new_results.md`](docs/core/collatz_rail7_new_results.md)
  gives the closed form for the rail-\(7\) recursion and its
  Mersenne-index escape formulas.

### Mersenne structure

- [`docs/no-go/recharge_nogo.md`](docs/no-go/recharge_nogo.md)
  proves the original \(\log_2x+g(v_2(x+1))\) no-go (now subsumed by SH1)
  and derives the exact Mersenne burn ledger. Attribution: the iterated
  burn identity \(2^tu-1\to3^tu-1\) is recorded by Andaloro (Fibonacci
  Quart. 38 (2000) 73–78); the coordinate-freezing use is this
  repository's.
- [`docs/repunit/mersenne_repunit_reduction.md`](docs/repunit/mersenne_repunit_reduction.md)
  reduces the Mersenne trajectory after its closed-form burn to the
  base-\(3\) repunit \((3^n-1)/2\) for odd \(n\).
- [`docs/repunit/repunit_rail5_exact.md`](docs/repunit/repunit_rail5_exact.md)
  classifies the initial mod-\(8\) rails of odd-indexed base-\(3\) repunits,
  proves that a natural-density \(5/8\) of the family reaches rail \(5\) on
  step \(0\) or \(1\), and records a separate bounded \(12\)-step observation.
- [`docs/repunit/repunit_rail5_density.md`](docs/repunit/repunit_rail5_density.md)
  extends the \(5/8\) result to every fixed time: the density avoiding rail
  \(5\) through step \(K\) is exactly
  \(\frac12(3/4)^K\), so almost every odd-indexed repunit eventually reaches
  rail \(5\).
- [`docs/repunit/repunit_rail5_survivor_geometry.md`](docs/repunit/repunit_rail5_survivor_geometry.md)
  identifies the infinite rail-\(5\) avoiders as a self-similar \(2\)-adic
  Cantor set conjugate to the full shift on valuation symbols \(\{1,2\}\).
  It has Haar measure zero and Hausdorff dimension
  \(\log_2((1+\sqrt5)/2)\); the same dimension holds for the corresponding
  repunit-index survivor set.
- [`docs/repunit/repunit_affine_tail_bound.md`](docs/repunit/repunit_affine_tail_bound.md)
  proves that the affine correction in the repunit-tail ledger is
  exponentially small throughout every pre-descent linear window.
- [`docs/repunit/repunit_tail_merge_reduction.md`](docs/repunit/repunit_tail_merge_reduction.md)
  gives the exact diagonal-state merge criterion and merge-inheritance
  induction principle.
- [`docs/repunit/repunit_gap_merger_analysis.md`](docs/repunit/repunit_gap_merger_analysis.md),
  [`docs/repunit/repunit_gap2_sync_tree.md`](docs/repunit/repunit_gap2_sync_tree.md),
  [`docs/repunit/repunit_multigap_sync_union.md`](docs/repunit/repunit_multigap_sync_union.md), and
  [`docs/repunit/repunit_collision_defect_dynamics.md`](docs/repunit/repunit_collision_defect_dynamics.md)
  develop collision-shell algebra, exact synchronization families, bounded
  shallow coverage, and a counterexample to an overcompressed relative-state
  recurrence.
- [`docs/repunit/repunit_256_block_target.md`](docs/repunit/repunit_256_block_target.md)
  isolates a conditional 256-valuation floor which would prove descent of
  every odd-indexed repunit tail.
- [`docs/repunit/repunit_low_prefix_obstruction.md`](docs/repunit/repunit_low_prefix_obstruction.md)
  constructs explicit low-valuation repunit prefixes, showing that any fixed
  block-floor proof must use off-diagonal merging or a recovery mechanism.
- [`docs/repunit/repunit_baker_nonshadowing.md`](docs/repunit/repunit_baker_nonshadowing.md)
- [`docs/repunit/repunit_baker_applicability_census.md`](docs/repunit/repunit_baker_applicability_census.md)
- [`docs/repunit/repunit_enemy_episode_analysis.md`](docs/repunit/repunit_enemy_episode_analysis.md)
  proves that positive integer exponents cannot shadow the
  \(3^{\alpha+1}=-7\) ghost branch for more than \(O(\log n)\) steps, via
  Yu's \(p\)-adic Baker theorem.
- [`docs/repunit/repunit_extremal_principle.md`](docs/repunit/repunit_extremal_principle.md)
  gives an exact payout ledger and shell-ancestry expansion for record
  valuation deficits, and isolates a primitive reachability lemma as the next
  proof target.
- [`docs/repunit/repunit_run_length_identity.md`](docs/repunit/repunit_run_length_identity.md)
  proves the fuel-enemy bridge \(\tau(x_K)=v_2(3^{m_K}+d_K)-E_K-1\) and the
  exact valuation-one run-length identity, unifying the burn, enemy-coordinate,
  and deficit pictures; an accompanying factorization probe shows the dangerous
  enemy constants are high-height rough primes.
- [`docs/no-go/Exponential_Decay_Potential.md`](docs/no-go/Exponential_Decay_Potential.md)
  proves descent of a bounded bit-weight potential on one explicit
  recharge family. Its global failure is now a theorem (BND1), not just
  an admission.

### Density and cycles

- [`docs/density-cycles/corridor_rate.md`](docs/density-cycles/corridor_rate.md)
  **(COR1–COR3).** The exact survivor-density rate: the density of odd
  integers not discharged by a \(K\)-bit valuation budget satisfies
  \(\lim p_K^{1/K}=\rho^{1/\theta}=0.965907\ldots\), with the explicit
  bound \(p_K\le31\,\rho^{K/\theta}\); consequently any finite-modulus
  forced-descent tree prover faces an undischarged frontier growing with
  branching factor exactly \(2\rho^{1/\theta}=1.9318\ldots\). Supersedes
  the refuted conjecture of `docs/density-cycles/descent_tree_survivors.md`.
- [`docs/density-cycles/stopping_time_density.md`](docs/density-cycles/stopping_time_density.md)
  gives a self-contained rederivation of the Terras/Everett
  almost-everywhere finite-stopping-time theorem with an explicit
  geometric bound. Known theorem, not a new resolution of the exceptional
  set.
- [`docs/density-cycles/cycle_reduction.md`](docs/density-cycles/cycle_reduction.md)
  proves the affine cycle equation and records carefully bounded finite
  searches. It does not exclude all nontrivial cycles; convergence is
  computationally verified in the literature to \(\sim2^{68}\) (Barina),
  which dominates the bounded searches here.

## Finite certificates

The following statements are exhaustive only over their stated bounds:

- Every odd \(x\le10^6\) descends below itself within at most 111
  odd-steps.
- The decayed-bit potential decreases across every tested first-descent
  epoch for odd \(x\le10^6\) with \(c=r=0.2\).
- The bounded cycle-pattern search documented in `docs/density-cycles/cycle_reduction.md`
  finds only \(x=1\).
- The measured descent-tree survivor fractions satisfy \(\le\rho^K\) for
  \(6\le K\le20\) **only**; the universal \(\rho^K\) bound is refuted
  (first failure \(K=195\), `scripts/verify_survivor_density_rate.py`), and the
  correct asymptotic rate is \(\rho^{1/\theta}\) (COR2).
- Mined no-go certificates cover the tested coordinate windows over odd
  \(x\le2\cdot10^6\); the uniform theorems are carried by the shadow
  families, not by the mining.
- Every tested odd-indexed repunit \(a_n\), \(3\le n\le199\), reaches rail
  \(5\bmod8\) within at most 12 odd-steps.

## Proof targets and exploratory work

These documents are useful research records but are not dependencies of
the proved-results track:

- [`docs/diagnostics/entropy_nonshadowing_theory.md`](docs/diagnostics/entropy_nonshadowing_theory.md) — alternative Entropy and Kolmogorov Complexity track.
- [`docs/density-cycles/descent_tree_survivors.md`](docs/density-cycles/descent_tree_survivors.md) — exact spine
  anchor; its original Conjecture 1 is **refuted** and superseded by
  COR1–COR3.
- [`docs/no-go/latent_fuel_notes.md`](docs/no-go/latent_fuel_notes.md) — discovery path for the
  tower; its hierarchy conjecture is **resolved** by TWR1.
- [`docs/repunit/repunit_tail_attack.md`](docs/repunit/repunit_tail_attack.md) and related repunit
  automaton/normal-form notes. The open residual \(\sigma(a_n)\) after
  the repunit landing is unchanged by all of the above.
- [`docs/repunit/primitive_ancestry_lemma.md`](docs/repunit/primitive_ancestry_lemma.md) - theory note
  isolating the dominant-payout ancestry/reachability lemma as the next
  symbolic target after `docs/repunit/repunit_extremal_principle.md`.
- [`docs/nested-anchor/near_threshold_episode_notes.md`](docs/nested-anchor/near_threshold_episode_notes.md) - finite
  diagnostic on the selected tight-margin repunit cases and their short
  near-threshold repair episodes (`scripts/explore_near_threshold_episodes.py`).
- [`docs/fuse/binary_fuel_bad_block_notes.md`](docs/fuse/binary_fuel_bad_block_notes.md) -
  exploratory 2-adic language for long low-surplus episodes via binary-fuel
  block coordinates and bad-block suffix gates
  (`scripts/explore_binary_fuel_blocks.py`).
- [`docs/diagnostics/diagnostics_attractor_sieve_spike.md`](docs/diagnostics/diagnostics_attractor_sieve_spike.md) -
  three diagnostics: the negative {A,B,C} motif attractor with its weak
  contraction constant, the q=2 smallest-shell reachability sieve and exact
  reach counts, and the Mersenne-spike recovery scan extended to R=999.
  Scripts: `scripts/explore_fuel_motif_attractor.py`,
  `scripts/explore_ancestry_reachability.py`, `scripts/explore_spike_recovery.py`.
- [`docs/fuse/fuse_map_theory.md`](docs/fuse/fuse_map_theory.md) and
  [`docs/fuse/fuse_burn_attack.md`](docs/fuse/fuse_burn_attack.md).
- [`docs/diagnostics/martingale_logspace_perspective.md`](docs/diagnostics/martingale_logspace_perspective.md) —
  exact Haar-random valuation martingale, logarithmic drift, corrected
  large-deviation rate function, and a carefully limited diffusion
  approximation.
- [`scripts/explore_martingale_repunit_drift.py`](scripts/explore_martingale_repunit_drift.py) —
  verifier for the martingale formulas and exact valuation-pattern counts,
  with a separately labelled fixed-window repunit diagnostic.
- Archived thermodynamic heuristics under [`archive/`](archive/README.md):
  fusion-fracture cycle, refractory-period barrier, recharge-density inverse
  law, Triple Lock notes, and potential-attack notes.

The parity-itinerary note
[`docs/core/Collatz_Parity_Fragility_Corrected.md`](docs/core/Collatz_Parity_Fragility_Corrected.md)
is a rederivation of Terras (1976) / Everett (1977) parity-vector
injectivity, restated for the unaccelerated map. It does **not** prove
that trajectories cannot later merge, or that hypothetical cycles are
metrically repelling.

## Archive

Superseded thermodynamic heuristics, legacy cycle summaries, and exploratory
precursors are retained under [`archive/`](archive/README.md). They are
historical records, not part of the maintained claim chain.

## Verification

All programs live under [`scripts/`](scripts/README.md) and use the Python
standard library; every assertion is exact integer or rational arithmetic.

```bash
# no-go program
python scripts/verify_shadow.py
python scripts/verify_leading_digit.py
python scripts/verify_tower.py
python scripts/verify_no_local_potential.py
python scripts/verify_nlp2.py
python scripts/verify_fuel_fraction.py
python scripts/verify_spine_synthesis.py

# density and rates
python scripts/verify_corridor_rate.py
python scripts/verify_survivor_density_rate.py
python scripts/verify_stopping_density.py
python scripts/verify_tree_survivors.py

# structure, cycles, legacy
python scripts/verify_block_fracture.py
python scripts/verify_mod8_rails.py
python scripts/verify_recharge_nogo.py
python scripts/verify_exponential_potential.py
python scripts/verify_repunit_reduction.py
python scripts/verify_repunit_rail5.py
python scripts/verify_repunit_rail5_density.py
python scripts/verify_repunit_rail5_survivor_geometry.py
python scripts/verify_repunit_affine_tail.py
python scripts/verify_repunit_tail_merges.py
python scripts/verify_repunit_gap_mergers.py
python scripts/explore_repunit_sync_tree.py --through-step 7 --max-total 24 --common-depth 24
python scripts/verify_repunit_sync_union.py
python scripts/verify_repunit_collision_defect.py
python scripts/verify_repunit_256_block.py
python scripts/verify_repunit_low_prefix.py
python scripts/verify_repunit_baker_nonshadowing.py
python scripts/explore_baker_applicability.py --limit 5001
python scripts/explore_repunit_enemy_episodes.py --limit 10001 --min-run 1
python scripts/verify_repunit_extremal_principle.py
python scripts/explore_repunit_extremal_prefixes.py --limit 2001
python scripts/verify_repunit_run_length.py --limit 201
python scripts/explore_repunit_enemy_factorization.py --limit 4001 --bound 1000000
python scripts/verify_entropy_balance.py
python scripts/verify_cycle_reduction.py
```

Interpret the output according to the claim ledger:

- symbolic identities and human proofs support universal claims;
- exhaustive loops support only their printed finite ranges;
- random sampling and `explore_*.py` output are evidence, not proofs;
- mined certificates prove infeasibility on their exact coordinate
  window; uniform statements require the designed families.

## Suggested reading order

1. `NOTATION.md`
2. `CLAIM_LEDGER.md`
3. `docs/no-go/shadow_certificate.md`
4. `docs/no-go/tower_theorem.md`
5. `docs/no-go/leading_digit_nogo.md`
6. `docs/core/Block_Fracture_Lemma.md`
7. `docs/density-cycles/corridor_rate.md`
8. `docs/no-go/spine_synthesis.md`
9. `docs/no-go/recharge_nogo.md`
10. `docs/core/Mod8_Rail_Descent.md`
11. `docs/repunit/mersenne_repunit_reduction.md`
12. `docs/repunit/repunit_rail5_exact.md`
13. `docs/repunit/repunit_rail5_density.md`
14. `docs/density-cycles/stopping_time_density.md`
15. `docs/density-cycles/cycle_reduction.md`

## Correction history (standard, not embarrassment)

- The universal survivor bound \(\rho^K\) (TREE2) was refuted by exact
  computation at \(K=195\) after passing its \(K\le20\) certificate; the
  corrected rate \(\rho^{1/\theta}\) is now a theorem (COR1–COR2).
- The parity-fragility theorem was reclassified as a rederivation of
  Terras/Everett after a literature pass.
- A draft of SPN1 overclaimed \(M\equiv1\bmod4\) uniformly; refuted by
  its verifier at \((d,s)=(1,1)\) and corrected before promotion.
- NLP1/NLP2/NLPD/FFN1 were superseded as impossibility statements by the
  strictly stronger and simpler SH1 within the same research arc; their
  structural content is retained.

## Contribution standard

A universal statement belongs in the proved-results track only when:

- its domain and quantifiers are explicit;
- the proof covers all edge cases;
- every dependency is already proved;
- the verifier tests the same claim the prose states;
- finite experiments are not used to replace an unbounded argument;
- the note states exactly what remains open.
