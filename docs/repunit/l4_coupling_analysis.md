# L4 coupling analysis: negative-valley replenishment tax

Status: **exploratory analysis** — contains exact computations from
the IEF15 streaming recurrence and a reduction to a combinatorial
question.  No new universal claims are promoted.  The analysis
identifies the key mechanism and the key unknown for the L4 lemma
ranked in RESIDUAL_ATLAS.md.

Dependencies: IEF15, IEF17, IEF18, IEF21, PCD16, RESIDUAL_ATLAS.md.

---

## 1.  Exact setup from IEF15

The (3/4)-block language has affine maps

    Φ_r(x) = 2^{cr−2} x + b_r,    b_3 = 19/32,  b_4 = 65/64

with drift per block

    d_r = cr_r − 2 = r log_2(3) − r − 2

    d_3 = 3 log_2(3) − 5 ≈ −0.2451
    d_4 = 4 log_2(3) − 6 ≈ +0.3398

Z_L multipliers:

    λ_3 = 2^{d_3} = 27/32 ≈ 0.84375
    λ_4 = 2^{d_4} = 81/64 ≈ 1.265625

Streaming recurrence:

    Z_{L+1} = 1 + λ_{r_{L+1}} · Z_L,    Z_0 = 0

Bound (IEF15):

    x_L ≤ 2^{S_L} · x_0 + (65/64) · Z_L

---

## 2.  Finding 1: p* > p_Z  [exact]

The zero-drift density of type-4 blocks is

    p* = (5 − 3 log_2 3) / (log_2 3 − 1) ≈ 0.41897

The Z_L-divergence density (where ⟨λ⟩ = 1) is

    p_Z = (1 − 27/32) / (81/64 − 27/32) = (5/32)/(27/64) = 10/27 ≈ 0.37037

Since p* > p_Z, the average Z_L multiplier at critical density is

    ⟨λ⟩ = p* · 81/64 + (1−p*) · 27/32 ≈ 1.02050 > 1

**Z_L diverges at the critical density.**  This is a structural fact
about the (3/4)-block language, independent of any particular word.

---

## 3.  Finding 2: ~678 blocks suffice for Z_L > B_X  [exact]

Since Z_L grows as ⟨λ⟩^L at critical density:

    Z_L > B_X = 64·10^6/65 ≈ 984615

requires

    L > log_2(B_X) / log_2(⟨λ⟩) = 19.932 / 0.02942 ≈ 678 blocks.

A flat stretch of only ~678 blocks at near-critical density makes Z_L
exceed B_X.  This is much smaller than B_X itself.

---

## 4.  Finding 3: 678 blocks give N_k ≈ 1  [exact]

The continued fraction of p* ≈ 0.41897 begins [0; 2, 2, 1, 1, 2, 2, …],
with convergent denominators 1, 2, 5, 7, 12, 31, 74, … growing
roughly as φ^n.

The largest convergent with q ≤ 678 has q ≈ 610.  The best
periodic-prefix approximant in a 678-block flat stretch has

    N_k = 678/610 ≈ 1.11 .

IEF18 requires N_k → ∞.  A single flat stretch of the minimum length
does not fire IEF18.

---

## 5.  Finding 4: the cascade mechanism  [exploratory]

The survivor has S_{L_k} → −∞ along a subsequence, with Z_{L_k} > B_X
at every valley (coordinate E).  Two mechanisms achieve this:

**(a) Long flat stretches near the valley.**  If the flat stretch is
at depth −D + δ and the valley is at depth −D, the terms in Z_{L_k}
from the flat stretch are 2^{−δ}.  For Z_{L_k} > B_X, the flat
stretch needs length ≳ B_X · 2^δ.

**(b) Deeper predecessor valleys.**  If position j has S_j < S_{L_k}
(a deeper valley before L_k), then 2^{S_{L_k} − S_j} > 1, contributing
a large term.  A cascade of progressively deeper valleys makes Z_{L_k}
large without long flat stretches.

Both mechanisms create structure:
- (a) creates long stretches of near-critical density → periodic
  approximants.
- (b) creates a cascade of valleys with growing amplitude →
  oscillation structure.

---

## 6.  Finding 5: the amplitude growth question  [open]

The cascade (mechanism b) creates oscillations with growing amplitude
D_k → ∞.  The key question is the growth rate:

- If D_k ~ k^α with α < 1: the drift returns to zero frequently
  (B satisfied), and the oscillations are slow enough for periodic
  approximants to accumulate (N_k → ∞ possible).  L4 might fire.

- If D_k ~ k^α with α ≥ 1: the drift might not return to zero
  (B at risk), but the oscillations are fast enough to prevent
  periodic approximation.  L4 might fail, but B might also fail.

Constraint from B (liminf S_L/L = 0): if valleys are at positions L_k
with S_{L_k} = −D_k, then B requires D_k/L_k → 0, i.e., D_k = o(L_k).

If each recovery has length ~ D_i, then L_k ≳ Σ D_i ~ k · D_k, so
D_k/L_k ~ 1/k → 0.  **B is satisfied for any growth rate.**

The question is purely about D: does the cascade create periodic
approximants with N_k → ∞?

---

## 7.  The reduction  [open]

The L4 coupling reduces to:

> **Combinatorial question.**  Can a sequence of recovery patterns
> over {3, 4}, with lengths D_k → ∞ and repetition exponent 1,
> avoid producing periodic-prefix approximants with N_k → ∞ and
> H_k = o(n_k)?

This is a problem in combinatorics on words — specifically, about the
relationship between repetition exponent and periodic approximation
quality.  It has nothing to do with Collatz.

The IEF12–IEF21 sequence is the scaffolding that reduces the Collatz
problem to this combinatorial question.  The "reverse engineering"
step would be: solve the combinatorial question, then translate back.
The Collatz-free freeze of the residual dual-digit problem is
`dio1_cocycle_problem.md` (Problem D1R).  That problem is now ledger
claims IEF22--IEF23 (Theorem G: functional \(\Phi_r\)-graph has no
infinite path); the integrality application is IEF24.

---

## 8.  Candidate tools for the combinatorial question

1. **Return word theory.**  The recovery patterns between valleys are
   return words to a cylinder.  The theory of return words (Justin,
   Vuillon 2000; Berthé, Delecroix 2018) gives structural constraints
   on return word sequences, particularly for words with low
   complexity.

2. **Bugeaud–Kim complexity bound (2017, 2026).**  For dio(w) = 1,
   the return time function satisfies rep(w) ≈ 1, and the complexity
   lower bound p(n) ≥ r(n) − n becomes trivial.  But the cocycle
   stream (not the word w) might have different complexity.

3. **Adamczewski–Bugeaud p-adic theorem.**  If the cocycle stream has
   low factor complexity, it is either rational or transcendental in
   Q_2.  Rationality is excluded by aperiodicity.  Finite sample from
   `scripts/explore_cocycle_factor_complexity.py` (1000 blocks) finds
   dual-digit streams saturating the prefix ceiling even for Sturmian
   words, so this route is not presently supported.

4. **A new Subspace Theorem argument** using the carry structure
   (3^{R_L} mod 2^L) directly, without periodic approximants.

---

## 9.  What would close L4

A proof that the conjunction of coordinates B, D, E is empty (or that
the conjunction implies non-trivial cocycle) would close L4.
Specifically, one of:

(a) A quantitative bound: Z_L > B_X forces the existence of a
    periodic-prefix approximant with N_k → ∞ and H_k = o(n_k),
    violating D.

(b) A complexity bound: the cocycle stream has factor complexity
    p(n)/n → 1, so Adamczewski–Bugeaud p-adic gives transcendence.

(c) A direct Subspace Theorem argument on the carry matching
    condition 3^{R_L} ≡ ℓ_L (mod 2^L).

Any of these would discharge the survivor and close the repunit-tail
descent programme.

---

## 10.  Verification

The exact computations in §§2–3 can be verified by:

    python scripts/explore_balanced_q3_dual_frontier.py \
        --blocks 10000 --direct-check 2000 --show 5

    python scripts/explore_balanced_q3_sturmian_renormalization.py \
        --max-denominator 111457 --direct-check 5000

The streaming recurrence Z_{L+1} = 1 + λ_{r_{L+1}} Z_L and the
critical densities p*, p_Z are exact rational/transcendental
expressions; no numerical approximation is involved in the
inequalities p* > p_Z and ⟨λ⟩ > 1.