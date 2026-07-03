# Repository edits — 2026-07-01 session

Four maintenance items plus one new proved note. Apply in order; each item
lists the file, the change, and the reason.

---

## 1. Reclassify PAR1 as a known theorem (Terras / Everett)

**Finding.** The theorem of `docs/core/Collatz_Parity_Fragility_Corrected.md`
(distinct starts cannot share one parity-rule sequence indefinitely) is the
classical parity-vector injectivity result: Terras (1976, *Acta
Arithmetica* 30, "A stopping time problem on the positive integers",
Theorem on parity vectors) proved that for the map
T(n) = (3n+1)/2 or n/2 the length-k parity vector is a bijection with
residues mod 2^k; Everett (1977, *Advances in Mathematics* 25) proved it
independently. Since each T-step contains exactly one halving, "k T-steps"
translates to "k halving steps" under the unaccelerated C-map — precisely
the note's divergence condition for offsets with v2(delta) = k. The note is
a valid elementary rederivation, not a new theorem.

**Edit to `CLAIM_LEDGER.md`, row PAR1:**
- Status: `Proved here` → `Known theorem rederived`
- Verification/dependency column, append: `Terras 1976 / Everett 1977
  parity-vector injectivity, restated for the C-map (k halvings in place
  of k T-steps)`

**Edit to `docs/core/Collatz_Parity_Fragility_Corrected.md`, status banner,
replace with:**

> **Status: known theorem rederived (Terras 1976 / Everett 1977), with
> corrected interpretation.** Distinct starts cannot share one parity-rule
> sequence indefinitely; this is the classical parity-vector injectivity
> result, restated for the unaccelerated map (the halving-step count here
> plays the role of the T-step count in Terras's formulation). The note
> does not prove non-merging, metric repulsion, or absence of basins.

**Edit to `README.md`:** in the parity-itinerary paragraph, insert "(a
rederivation of Terras/Everett parity-vector injectivity)" after "proves".

---

## 2. TREE2 / Conjecture 1 of `docs/density-cycles/descent_tree_survivors.md` is FALSE

**Finding.** The survivor density has an exact expression as a
first-passage probability for the i.i.d. Geometric(1/2) valuation walk
(by the equidistribution Lemma 3 of `docs/density-cycles/stopping_time_density.md`): a class
survives at budget K iff the walk stays strictly below the line
theta*j + 1 while its running sum is <= K. Computing this probability by
exact dynamic programming (`scripts/verify_survivor_density_rate.py`):

- dens(S_K) <= rho^K holds for K <= 194 and **first fails at K = 195**
  (confirmed in exact rational arithmetic);
- the ratio dens/rho^K then grows without bound: 1.08 at K=200, 1.24 at
  K=210, 4.6 at K=300;
- the empirical per-step decay rate trends to ~0.966, matching the
  Mogulskii first-passage heuristic rho^(1/theta) = e^{-I(theta)/theta}
  = 0.965907..., not rho = 0.946507....

The K <= 20 finite certificate was pre-asymptotic. The mechanism: a
survivor must remain a large-deviation path (slope < theta per step) for
roughly K/theta steps, paying rate I(theta) per *step*, hence
I(theta)/theta per unit of *budget* K — a strictly smaller exponent than
the fixed-step Cramer rate I(theta) per step at step count K.

Formulation caveat, stated for honesty: the DP computes the natural-density
(walk) formulation; the note's residue-count formulation agrees with it to
within ~0.5% in the enumerable range K <= 16, an error swamped by the
violation margin from K ~ 200 onward. The count formulation therefore also
fails, by K ~ 200 at the latest; only the exact first-failure index could
shift by a few units.

**Edits to `docs/density-cycles/descent_tree_survivors.md`:**

(a) Replace Conjecture 1 with:

> **Corrected Conjecture 1' (survivor-density rate).** dens(S_K) decays
> geometrically with asymptotic rate rho_1 = e^{-I(theta)/theta}
> = 0.965907...: there is C > 0 with dens(S_K) <= C * rho_1^K, and
> (1/K) log dens(S_K) -> log rho_1.
>
> **History note.** The original Conjecture 1 claimed dens(S_K) <= rho^K
> with rho = e^{-I(theta)} = 0.9465. This is FALSE: the exact
> first-passage computation (`scripts/verify_survivor_density_rate.py`) shows the
> bound holds only for K <= 194 (natural-density formulation) and the
> ratio dens/rho^K grows without bound thereafter. The K <= 20 finite
> certificate was pre-asymptotic and the conjectured constant was wrong;
> the two roles of K (modulus depth vs odd-step count) that the note
> already flagged are exactly the source of the discrepancy — the correct
> exponent is I(theta) per step over ~K/theta steps, not over K steps.

(b) Add a proof target with sketch (label: **Proof target — sketch, not
yet written to project standard**):

> **Claim (geometric decay, provable).** dens(S_K) <= C * rho_1^K for an
> explicit C.
> *Sketch.* Condition on j0, the last uncrossed step within budget
> (E_{j0} < theta*j0 + 1, E_{j0+1} > K). By Lemma 3 the valuations are
> i.i.d., so P <= sum over j0 of P(E_{j0} <= theta*j0 + 1) *
> P(e > K - theta*j0 - 1). For the range theta*j0 <= K - 1 the second
> factor is <= 2^{-(K - theta*j0 - 1)}; bounding the first by the Cramer
> estimate C0 * rho^{j0} and summing the geometric-type series (note
> rho * 2^theta = 3*rho > 1, so the series is dominated by its top index
> j0 ~ K/theta) gives O(rho^{K/theta}) = O(rho_1^K). The complementary
> range theta*j0 > K - 1 contributes sum_{j0 > (K-1)/theta} C0 rho^{j0}
> = O(rho_1^K) as well. Constants are explicit; the +1 offsets shift C
> only.

(c) In §4 "What is and is not proved": move the density bound from
"Finite certificate" framing to: finite certificate holds for the tested
range only and is now known NOT to extend with the constant rho; the
corrected rate statement is Conjecture 1' with the geometric-decay claim as
the promotable target.

**Edit to `CLAIM_LEDGER.md`, row TREE2:**
- Claim: `Tree-survivor density is universally bounded by rho^K` →
  `Tree-survivor density decays geometrically; conjectured rate
  rho^{1/theta} = 0.9659...`
- Status: `Conjecture / proof gap` → `Original rho^K bound REFUTED
  (exact computation, first failure K=195); corrected rate conjectured;
  geometric decay is a proof target with sketch`
- Verification: add `scripts/verify_survivor_density_rate.py`

**Edit to `scripts/verify_tree_survivors.py`:** the assertion
`frac <= RHO ** K` is now known to hold only in the tested range; add a
comment stating it certifies K = 6..20 only and referencing the
refutation, so a future reader does not mistake the passing assert for
support of the universal bound.

---

## 3. Literature note for `docs/density-cycles/cycle_reduction.md`

Append to the introduction or §"What is not proved":

> **Relation to prior computation and theory.** Convergence of all
> trajectories has been verified computationally far beyond the range used
> here (on the order of 2^68, Barina), so CYC4's 10^6 bound has no
> independent value beyond internal consistency of this repository's
> pipeline. Likewise, Baker-type transcendence bounds combined with the
> verified range exclude nontrivial cycles of very large minimum length
> (Steiner's 1-cycle theorem; Simons & de Weger's m-cycle exclusions).
> The finite certificates CYC2/CYC4 are maintained as machine-checked
> anchors for this repository's own claims, not as contributions to the
> state of the art.

---

## 4. New note: `docs/no-go/no_local_potential.md` (+ verifier)

New proved result generalizing RNG1: **no potential
log2(x) + g(x mod 2^m, tau(x)) is nonincreasing along f, for any m and any
g.** Both the burn family 3^j 2^t - 1 and the recharge family
(2^{M+2}-5)/3 -> 2^M - 1 are residue-frozen mod 2^m (residues -1 and
r* = -5 * 3^{-1} respectively), so fixed-modulus information cannot
separate hot from cold fuel; the RNG1 scissors then close on the single
sequence g(-1, M): forced linear growth (burn) vs a uniform cap
(recharge). RNG1 is the m = 0 case.

Files: `docs/no-go/no_local_potential.md`, `scripts/verify_no_local_potential.py`
(all checks pass; exact integer arithmetic).

**Edit to `CLAIM_LEDGER.md`, add row:**

| NLP1 | No potential \(\log_2 x + g(x \bmod 2^m, \tau(x))\) is
nonincreasing along \(f\), for any \(m\ge0\) and any \(g\) | Proved here
(pending final external literature check) | `docs/no-go/no_local_potential.md` |
`scripts/verify_no_local_potential.py`; generalizes RNG1 (the \(m=0\) case);
depends on `docs/no-go/recharge_nogo.md` Lemmas 1–2 |

**Edit to `README.md`:** add `docs/no-go/no_local_potential.md` to the
"Mersenne structure and potential limitations" bullet list, after
`docs/no-go/recharge_nogo.md`.

**Publication assessment.** RNG1 + NLP1 together form a self-contained
negative result ("Mersenne obstruction to local Lyapunov functions for the
Collatz map") of the kind absent from the literature: surveys state the
lack of a monotone invariant as folklore, but no published theorem
excluding a concrete class was found (searches 2026-07-01). Before any
submission: a deeper pass over Lagarias's annotated bibliography for prior
no-go statements is mandatory. Open extensions worth one paragraph in the
paper: high-end (leading-digit) corrections, mixed windows, multi-step
potentials.

---

## Status of session claims

- PAR1 reclassification: literature-verified (Terras 1976 / Everett 1977).
- TREE2 refutation: exact computation, rational-arithmetic confirmed at
  K = 195; formulation caveat stated above.
- Geometric-decay claim for survivors: sketch only — NOT yet at project
  standard; do not promote until written and verified.
- NLP1: proof complete and machine-checked; literature check at survey
  level only; one deeper bibliography pass required before calling it new.
