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

## Current research status

The mature line is the one-step potential no-go programme, centred on SH1
and SH2, together with the exact Mersenne ancestry tower and the corridor-rate
theorem. The universal repunit-tail descent problem remains open. Its current
state is:

- exact affine, merger, collision-shell, and extremal-storage reductions are
  available;
- several tempting local, fixed-block, compressed-state, and shallow-merger
  routes have been refuted or shown insufficient;
- the shortcut-map `6n` data is consistent with neutral parity statistics,
  but this is an empirical diagnosis, not an equidistribution theorem;
- the live lemma is arithmetic non-shadowing between affine endpoint-lift
  digits and a power-of-three carry in the balanced \(q=3\) cylinder family;
  correction/cylinder transversality supplies the companion primitivity and
  least-representative constraints;
- the integral-escape reformulation supplies a new terminal route: it is
  enough to exclude eventually-zero exponent lifts, and the dual endpoint
  residue modulo \(3^{R_L}\) gives an explicit word-only least-representative
  target whose superlinear growth would rule out the infinite balanced word;
- broad computation is paused until it tests that lemma and the exact cylinder
  engine is made incremental, as recorded in
  `docs/repunit/next_generation_attack_program.md`.

`RESEARCH_ROADMAP.md` retains the chronological development. Its later
checkpoints supersede earlier proposed experiments where they conflict.
`RESIDUAL_ATLAS.md` is a demoted classification scoreboard for the mechanical
\(3/4\)-block language. Fresh outside-box architectures to try one at a time
are listed in
`docs/no-go/outside_box_avenue_portfolio.md` (closed barriers remain in
`docs/no-go/outside_box_avenue_triage.md`).

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
- A historical independent finite-window certificate check is described in
  `SELF_REVIEW.md`, but its script (`scripts/verify_nogo_certificate.py`) is
  not present in this checkout. Those reported runs are therefore provenance,
  not part of the reproducible verification suite.

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
  valuation deficits. Its primitive reachability lemma launched the completed
  REPANC/GPA ancestry branches and the active payout programme.
- [`docs/repunit/primitive_ancestry_lemma.md`](docs/repunit/primitive_ancestry_lemma.md)
  **(REPANC1).** In the smallest-shell \(q=2\) case, correction equality at
  an admissible aligned source length is already sufficient for reachability:
  it automatically realises the entire smaller repunit valuation word and
  forces a next-step merge. **(REPANC2)** places every such match in an
  explicit critical-density source-length window
  \(i<u/\log_2 3+O(j)\). **(REPANC3)** shows this is a cylinder-wise
  dichotomy: nonmembership does not create a new exponent congruence. The
  proposed least-representative correlation bound remains open. A focused
  primitive-record diagnostic through \(n=2001\) leaves only one nonvacuous
  dangerous dominant-\(q=2\) case, so it supports narrowing the lemma rather
  than extrapolating a quantitative law.
- [`docs/repunit/general_payout_ancestry.md`](docs/repunit/general_payout_ancestry.md)
  **(GPA1–GPA2).** Automatic shell-partner realisation extends from \(q=2\)
  to every payout \(q\ge2\). However, the canonical partner is identically
  unreachable when \(q\equiv3,4\pmod6\), because its correction is divisible
  by \(3\) while every positive-length source correction is not. In
  particular, the common dominant \(q=3\) branch must use multi-ancestor or
  amortized payout structure rather than the single canonical partner.
- [`docs/repunit/payout_concentration_diffusion.md`](docs/repunit/payout_concentration_diffusion.md)
  **(PCD1–PCD17).** The payout ledger has an exact
  initial/eligible/blocked trichotomy and effective-count alternative. In the
  primitive census through \(n=5001\), the \(110\) records with \(D_K\ge2\)
  split \(88/0/16/6\) across the eligible, initial, blocked-concentrated, and
  blocked-diffuse branches; all six diffuse records occur on \(n=471\).
  Consecutive \(q=3\) shell displacements fuse exactly into a height-\(4\)
  shell. This does not by itself determine the residue or reachability of the
  complete combined correction. Six short mixed blocked/eligible valuation
  blocks give universal shell-fusion identities and account for all \(43\)
  mixed fusions in the finite \(n\le5001\) dangerous-record census. None of
  these patterns lifts to a collision under the naive complete-correction
  transport. With the correct affine injection restored, every canonical
  shell annihilates into the high correction after one step, so it cannot
  persist as an independent state for later shell pairing. The remaining
  live branch is amortized payout charging and historical spacing. Its first
  exact bound is \(D_K+2N_B\le K\log_2(3/2)\): blocked effective ancestry is
  paid for by valuation excess, although this alone is not a uniform deficit
  bound. An explicit balanced \(q=3\) valuation language shows that historical
  spacing alone cannot strengthen it to one. Every finite word beginning with
  valuation at least two has exactly one odd repunit exponent cylinder, so
  finite realization does not eliminate the balanced language either. The
  least representatives form nested cylinders: every change jumps above the
  previous \(2^E\) scale, so a bound on constant-cylinder plateau length would
  force exponential exponent growth. The proposed fixed bound two fails at
  \(m=1200\), so the live target is sublinear plateau growth. Every extension
  now has an exact local recursion: one linear congruence and a discrete log
  of order at most \(64\). All local lift residues occur through \(m=1500\),
  reducing the problem to correlation and zero-run control for the resulting
  2-adic cocycle rather than a forbidden-residue argument. The cocycle
  linearizes exactly: a plateau occurs when the affine starting-cylinder lift
  equals the corresponding higher power-of-three carry. Across a plateau the
  carry shifts block by block, turning the run into one contiguous binary
  word match against a fixed power-of-three carry. Fixed-width endpoint
  residues are not closed under this dynamics; a transducer must replenish
  its state from the carry or grow its window. Moreover, every consecutive
  balanced mechanical block composition has real multiplier strictly between
  \(2/3\) and \(3/2\), regardless of length. The balanced obstruction is a
  near-isometry at every scale, so arithmetic carry/endpoint separation—not
  accumulated real contraction—is the remaining route. The same distortion
  bound shows that normalized correction storage grows linearly between
  \(L/2+7/8\) and \(9L/8+33/32\) after \(L\) balanced blocks; raw ledger
  storage is therefore not a compact state variable.
- [`docs/repunit/integral_escape_frontier.md`](docs/repunit/integral_escape_frontier.md)
  **(IEF1--IEF5, IEF7--IEF21).** A residual \(2\)-adic exponent branch
  contains a positive integer exactly when its canonical lift blocks are
  eventually zero. For the
  balanced \(q=3\) word, the dual endpoint residue modulo \(3^{R_L}\) gives a
  second escape route: any superlinear least-representative bound excludes a
  fixed positive orbit. The residue has a closed affine recursion, and every
  nonzero dual digit resets it to modulus scale. The quantitative reset-gap
  bound is still open, but IEF10 bypasses it for qualitative exclusion. The
  exact integral bridge identifies the dual digit with
  the starting-cylinder lift digit, so qualitative exclusion only requires
  proving that this common stream is not eventually zero. **(IEF6)** records
  the finite \(L\le10000\) diagnostic. IEF8 supplies an exact
  continued-fraction renormalization and reduces the next theorem to one
  cross-difference \(2\)-adic valuation at the standard Sturmian scales.
  IEF9 independently identifies the complete balanced start as one critical
  \(2\)-adic Hecke--Mahler value; proving that value irrational would close
  the branch. IEF10 needs less: periodic standard-word approximants, PCD16,
  and Baker's finite irrationality measure prove directly that no positive
  integer realizes the infinite deterministic balanced itinerary. IEF11
  isolates the reusable periodic-prefix discharge criterion and proves that
  every fixed phase shift is excluded as well. IEF12 combines that criterion
  with the Bugeaud--Kim repetition theorem to exclude every Sturmian word of
  the critical slope, for every intercept. The remaining qualitative
  frontier is therefore genuinely non-Sturmian. IEF13 identifies the broader
  mechanism: bounded critical factor discrepancy plus Diophantine exponent
  greater than \(1\) is enough. In particular, bounded discrepancy plus
  linear factor complexity is discharged. Thus any survivor must have
  unbounded discrepancy or superlinear symbolic complexity. IEF14 further
  discharges growing-discrepancy languages when periodic-prefix agreement
  surplus outruns twice their local discrepancy budget. IEF15 independently
  reduces sustained negative-drift languages to an explicit finite check via
  their bounded suffix partition function. IEF16 translates the known
  critical lower-parity-density theorem into \(\liminf S_L/L=0\), excluding
  either sign of linear density drift. IEF17 consolidates FIN1 and these rules
  into one five-coordinate non-cyclic survivor profile. IEF18 sharpens its
  periodic-prefix coordinate by charging only total and suffix-positive
  discrepancy, rather than twice the full symmetric factor discrepancy.
  IEF19 then discharges every itinerary having sublinear prefix drift and
  repetition exponent greater than one. A non-cyclic survivor must therefore
  have repetition exponent one or positive linear drift excursions. IEF20
  reaches into the latter branch by discharging fixed-surplus repetitions in
  asymptotically critical drift windows. IEF21 sharpens this to exact terminal
  draw-up and endpoint-loss costs, so large internal peaks alone do not protect
  a branch.
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
  proving the \(q=2\) ancestry reductions REPANC1--REPANC3; this is now a
  supporting side branch rather than the main bottleneck.
- [`docs/repunit/next_generation_attack_program.md`](docs/repunit/next_generation_attack_program.md) —
  ranked research programme covering general payouts, correction-set geometry,
  payout concentration versus diffusion, transversality, ancestry capacity,
  induced record maps, transfer operators, and computer-assisted lemma
  discovery, with explicit stopping rules and a synchronized attack-status
  table through PCD17.
- [`docs/repunit/coverage_portfolio.md`](docs/repunit/coverage_portfolio.md) —
  ordered residual-cover framework for combining any number of individually
  sound descent-or-smaller-merge rules without double-counting overlaps or
  mixing percentages from different case universes.
- [`RESIDUAL_ATLAS.md`](RESIDUAL_ATLAS.md) — live qualitative residual
  scoreboard: freezes the IEF17 survivor intersection as the sole atlas
  object and ranks coordinate-shrinking lemmas L1--L6.
- [`docs/repunit/integral_escape_frontier.md`](docs/repunit/integral_escape_frontier.md)
  — terminal residual criterion: the surviving \(2\)-adic set may be nonempty
  provided every infinite branch has nonzero exponent lifts infinitely often,
  excluding every positive-integer exponent.
- [`docs/repunit/repunit_equidistribution_reframing.md`](docs/repunit/repunit_equidistribution_reframing.md) —
  capstone diagnostic for the distinct shortcut-map `6n` target. Exact
  bookkeeping is combined with finite data consistent with parity density
  \(1/2\); no convergence or equidistribution theorem is claimed.
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
  `scripts/explore_ancestry_reachability.py`,
  `scripts/explore_primitive_q2_correlation.py`,
  `scripts/explore_spike_recovery.py`.
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
# ledger governance
python scripts/verify_claim_ledger.py

# Avenue A finite check
python scripts/verify_repunit_storage_dominance.py --limit 5001

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
python scripts/verify_repunit_ancestry_realization.py
python scripts/verify_repunit_general_payout_ancestry.py
python scripts/explore_repunit_extremal_prefixes.py --limit 2001
python scripts/explore_primitive_q2_correlation.py
python scripts/explore_payout_concentration.py --limit 5001 --top 0
python scripts/explore_mixed_shell_pairs.py --limit 5001 --top 100
python scripts/explore_balanced_q3_cylinders.py --payouts 1500 --show 3
python scripts/explore_balanced_q3_dual_frontier.py --blocks 10000 --direct-check 2000 --show 5
python scripts/explore_balanced_q3_zero_cylinders.py --blocks 10000 --phase 0 --show 5
python scripts/explore_balanced_q3_sturmian_renormalization.py --max-denominator 111457 --direct-check 5000
python scripts/verify_balanced_q3_hecke_mahler.py --odd-steps 5000 --precision 100
python scripts/verify_balanced_q3_periodic_approximants.py --max-denominator 4563 --precision 120
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

For the open repunit programme after that proved-results sequence, read
`docs/repunit/repunit_extremal_principle.md`, the completed ancestry branches
`docs/repunit/primitive_ancestry_lemma.md` and
`docs/repunit/general_payout_ancestry.md`, then the active
`docs/repunit/payout_concentration_diffusion.md` and
`docs/repunit/next_generation_attack_program.md`. The portfolio view is in
`docs/repunit/coverage_portfolio.md`. The explicitly empirical
`docs/repunit/repunit_equidistribution_reframing.md` is a separate capstone.

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
