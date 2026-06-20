# Entropy and Kolmogorov Complexity in the Collatz Map

**Status:** Alternative research track; theoretical formulation. The
conservation identity is exact. The enemy branch \((2,1^*)\) is now killed by
`repunit_baker_nonshadowing.md` (Yu/Baker). General deficit patterns remain
open; modulus size alone cannot prove non-shadowing.
**License:** CC-BY 4.0

---

## Abstract

We formalise a global conservation perspective on the accelerated odd Collatz map. While local potential functions $P(x) = \log_2 x + g(\tau(x))$ are fundamentally obstructed by the recharge mechanism, we show that recharge is not a free source of growth. Every recharge step of payout valuation $s$ and new fuel $m$ resolves exactly $s+m$ bits of the initial state, while the state grows in magnitude by at most $s - \log_2 3$ bits (in log space). 

We establish an exact **Information Conservation Law** relating the total valuation weight $E_K$ to the log-magnitude growth. Using this law, we prove that sustaining a growing trajectory requires a continuous sequence of highly restrictive $2$-adic alignments. Because the base-$3$ repunit sequence $a_n = (3^n-1)/2$ has low Kolmogorov complexity ($K(a_n) \le \log_2 n + O(1)$), we conjecture that it cannot contain the high-entropy information required to shadow the non-descending "survivor" set through a window as long as $3n$.

---

## 1. Setup and Map Notation

For an odd positive integer $x$, the accelerated odd-step map is:
$$
f(x) = \frac{3x+1}{2^{v_2(3x+1)}}.
$$
Let the trajectory starting at $x_0$ be $x_0, x_1, \dots, x_K$, with:
$$
e_i = v_2(3x_i+1), \qquad E_K = \sum_{i<K} e_i.
$$
The exact affine accumulation formula (`stopping_time_density.md` Lemma 1) is:
$$
x_K = \frac{3^K x_0 (1+q_K)}{2^{E_K}},
$$
where the relative affine correction $q_K$ is:
$$
1+q_K = \prod_{i=0}^{K-1} \left(1 + \frac{1}{3x_i}\right).
$$

---

## 2. The Information Conservation Law

### Theorem 1 (Conservation Identity)
For any starting odd integer $x_0$ and step count $K \ge 1$:
$$
E_K \;+\; \log_2\left(\frac{x_K}{x_0}\right) \;=\; K \log_2 3 \;+\; \log_2(1+q_K).
$$

*Proof.* Taking the base-2 logarithm of the exact accumulation formula gives:
$$
\log_2 x_K \;=\; K \log_2 3 \;+\; \log_2 x_0 \;+\; \log_2(1+q_K) \;-\; E_K.
$$
Rearranging the terms yields the identity. $\quad\blacksquare$

### Interpretation: The Entropy Balance
Let us define the **Entropy Balance** (or **Information Margin**) $B_K(x_0)$ as:
$$
B_K(x_0) \;=\; E_K \;-\; \log_2\left(\frac{x_K}{x_0}\right).
$$
Using Theorem 1, we can write:
$$
B_K(x_0) \;=\; 2E_K \;-\; K \log_2 3 \;-\; \log_2(1+q_K).
$$
* \(E_K\) is the total valuation weight. A complete valuation prefix selects a
  residue class of relative density \(2^{-E_K}\) among odd starts; this is the
  precise residue-counting meaning of its information cost.
* $\log_2(x_K/x_0)$ represents the **Magnitude Gain**: the increase in the bit-length of the value.
* $B_K(x_0)$ measures the "dissipated" entropy. For a trajectory to descend below its start ($x_K < x_0$), we must have $\log_2(x_K/x_0) < 0$, which requires:
  $$
  E_K \;>\; K \log_2 3 \;+\; \log_2(1+q_K).
  $$

---

## 3. Exact monotonicity of the balance

The balance is strictly increasing, but this fact is elementary and weaker
than descent.

**Theorem 2.** For every odd \(x_i\),

\[
B_{i+1}-B_i
=2e_i-\log_2\left(3+\frac1{x_i}\right)>0.
\]

For \(x_i>1\), the increment is at least

\[
\log_2(6/5)=0.2630\ldots.
\]

**Proof.** Since

\[
\frac{x_{i+1}}{x_i}
=\frac{3+1/x_i}{2^{e_i}},
\]

substitution into \(B_{i+1}-B_i=e_i-\log_2(x_{i+1}/x_i)\) gives the formula.
If \(e_i=1\), then \(x_i\equiv3\pmod4\), so \(x_i\ge3\) and
\(3+1/x_i\le10/3\). If \(e_i\ge2\), the lower bound is larger.
\(\blacksquare\)

This monotonicity mostly repackages the elementary fact \(e_i\ge1\); it does
not force \(x_K<x_0\).

---

## 4. Exact residue encoding

A complete valuation prefix of total weight \(E\) determines one odd starting
class modulo \(2^{E+1}\). For the repunit family, intersection with
\(a_n=(3^n-1)/2\) becomes a discrete-log congruence for \(n\) modulo a power
of two.

This is exact and useful computationally. However:

- survival gives an **upper** bound on accumulated valuation, not a lower
  bound;
- a modulus larger than \(n\) may determine \(n\) uniquely, but uniqueness is
  not a contradiction;
- a uniquely selected residue can have a short algebraic description.

`repunit_low_prefix_obstruction.md` makes this explicit. For every \(K\), a
short algorithm constructs an exponent class with valuation prefix
\((2,1^{K-1})\), even though the modulus has \(K+1\) binary exponent bits.

Therefore Kolmogorov complexity alone cannot establish non-shadowing.

---

## 5. Correct non-shadowing target

The useful global target is quantitative:

> **Small-representative non-shadowing.** Show that any active low-valuation
> prefix of length \(K\) selects exponent residues whose least positive
> representatives grow faster than the linear diagonal \(K/C\), unless the
> trajectory merges into a smaller controlled tail.

For a proposed bound \(K=Cn\), this would prevent the actual positive exponent
\(n\) from occupying the required survivor class.

The explicit low-prefix branch is consistent with this target: its least
representatives grow roughly exponentially with prefix depth, so it creates
arbitrarily long finite prefixes but does not by itself shadow for a number of
steps proportional to the representative exponent.

---

## 6. Relation to merging

The maintained exact merge statements are in
`repunit_tail_merge_reduction.md`. No logarithmic upper bound on merger
valuation is asserted here.

The information track may still help by describing how exponent residue
classes split or coalesce across diagonal layers, but every such claim must be
derived from the exact normal-form state rather than inferred from modulus
size.

---

## 7. Current programme

1. Compute least positive exponent representatives for active survivor
   classes.
2. Compare representative growth with diagonal depth.
3. Separate classes that merge into smaller tails.
4. Seek a lower bound on representative size for the remaining primitive
   classes.

This is a concrete arithmetic discrepancy problem. The conservation identity
supports its bookkeeping, but does not solve it.
