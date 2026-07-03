# The Descent-Tree Survivors Are the Spine

**Building on:** `scripts/verify_descent_tree.py`, `stopping_time_density.md`, `../no-go/recharge_nogo.md`, `../repunit/mersenne_repunit_reduction.md`
**Status:** Exploratory synthesis with one exact spine result and finite survivor certificates. The original $\rho^K$ density bound is refuted; the correct decay rate is proved in `corridor_rate.md`.
**License:** CC-BY 4.0

---

## Abstract

The branching certificate in `scripts/verify_descent_tree.py` discharges many residue classes mod $2^K$ but leaves a stubborn set undischarged at every tested depth. The survivors are valuation-deficient classes and are anchored by the **Mersenne spine**: the all-ones residue $2^K-1$ survives through its initial burn, where all valuations are \(1\). Finite computations through $K=20$ show a decreasing survivor fraction bounded by $\rho^K$, but that bound is pre-asymptotic: exact first-passage computation (`scripts/verify_survivor_density_rate.py`) refutes the universal $\rho^K$ claim at $K=195$. The correct exponential rate $\rho_1=e^{-I(\theta)/\theta}=0.9659\ldots$ is proved in `corridor_rate.md`.

---

## 0. Setup

For odd $x$, $f(x)=(3x+1)/2^{v_2(3x+1)}$, with per-step valuations $e_i=v_2(3x_i+1)$ and partial sums $E_j=\sum_{i<j}e_i$. From `stopping_time_density.md` (Lemma 2), descent of the whole class is *forced* once the accumulated valuation crosses the line $E_j\ge\theta j+1$, $\theta=\log_2 3$. Define the **discharge level**

$$
L(r)=E_J,\qquad J=\min\{j\ge1: E_j(r)\ge \theta j+1\},
$$

the cumulative valuation — hence (by the exact equidistribution, `stopping_time_density.md` Lemma 3) the number of low bits — needed to discharge the class of $r$. The depth-$K$ tree discharges $r\bmod 2^K$ iff $L(r)\le K$; the **survivor set** is

$$
S_K=\{\,r\text{ odd}\bmod 2^K : L(r)>K\,\}.
$$

---

## 1. The survivors are a vanishing lower-tail set

**Theorem (survivor-density rate, proved in `corridor_rate.md`).** Let $\tilde S_K$ be the budget-$K$ survivor set in the natural-density (valuation-walk) formulation of `corridor_rate.md` §0. Then $\operatorname{dens}(\tilde S_K)^{1/K}\to\rho_1=e^{-I(\theta)/\theta}=0.965907\ldots$ as $K\to\infty$, with explicit bound $\operatorname{dens}(\tilde S_K)\le31\,\rho_1^{\,K}$ for all $K\ge1$. Undischarged residue classes mod $2^K$ grow with branching factor $2\rho_1=1.93182\ldots$ (Corollary 2 of `corridor_rate.md`).

**History note.** The original Conjecture 1 claimed $\operatorname{dens}(S_K)\le\rho^{K}$ with $\rho=e^{-I(\theta)}=0.9465\ldots$. This is **FALSE**: `scripts/verify_survivor_density_rate.py` shows the bound holds only for $K\le194$ (walk formulation) and the ratio $\operatorname{dens}/\rho^K$ grows without bound thereafter. The $K\le20$ finite certificate was pre-asymptotic; the two roles of $K$ (modulus depth vs odd-step budget) are exactly the source of the discrepancy — the correct exponent is $I(\theta)$ per step over $\approx K/\theta$ steps, not over $K$ steps.

(Verified for $6\le K\le20$: $\operatorname{dens}(S_K)$ runs from $0.53$ to $0.14$, always $\le\rho^K$ in that range only.)

---

## 2. The spine is the anchor

**Proposition 2 (Mersenne survives every depth).** For all $K$, $2^K-1\in S_K$.

*Proof.* By the burn closed form (`../no-go/recharge_nogo.md` Lemma 3 / `../repunit/mersenne_repunit_reduction.md` Lemma R1), $2^K-1$ has $e_i=1$ for its first $K-1$ steps, so $E_j=j$ and $S_j=E_j-\theta j=(1-\theta)j<0$ throughout the burn — the descent line is never reached while the bits last, so $L(2^K-1)>K$. It is the **unique minimal-valuation orbit** ($E_j$ as small as possible), the extreme point of the lower tail. $\;\blacksquare$

In the finite data, survivors are biased toward **high trailing-one fuel**:
at $K=12$ the mean $\tau=v_2(\,\cdot+1)$ over $S_K$ is $3.03$ versus
$2.00$ over all odd residues, and the top survivors have $\tau$ up to $K$.
This motivates the “near-Mersenne” description but is not an exact
classification.

---

## 3. A comparison of viewpoints

Three related constructions appear:

| viewpoint | the set |
|---|---|
| `scripts/verify_descent_tree.py` | residue classes undischarged at depth $K$ |
| `stopping_time_density.md` | fixed-step lower-tail "non-$K$-good" classes, density $\le\rho^K$ |
| spine notes | high-fuel / near-Mersenne classes, anchored by $2^K-1$ |

They overlap conceptually but have not been proved to be the same set. The
spine shows that no finite tree depth discharges every residue class: the
all-ones residue survives at each depth. The observed geometric shrinkage of
the remaining classes is a finite certificate and conjectural pattern.

---

## 4. What is and is not proved

**Proved:** the spine anchor $2^K-1\in S_K$ through its initial burn and its minimal initial valuation sequence.

**Finite certificate:** the measured survivor fractions are non-increasing and at most $\rho^K$ for $6\le K\le20$ only; this does **not** extend with constant $\rho$ (refuted at $K=195$).

**Proved elsewhere:** geometric decay at rate $\rho_1=e^{-I(\theta)/\theta}$ for the walk formulation (`corridor_rate.md`, claims COR1–COR2).

**Open:** sharp prefactors; exact identification of the mod-$2^K$ residue-count set $S_K$ with the walk formulation in the limit (agreement to $\lesssim0.5\%$ for $K\le16$).

**Not proved:** a measure formula for the limiting \(2\)-adic survivor set, or
that every positive integer eventually leaves the corresponding survivor
classes. The latter is part of the Collatz problem.

---

## Appendix — Verification

`scripts/verify_tree_survivors.py` checks: $\operatorname{dens}(S_K)\le\rho^K$ and non-increasing ($K=6..20$); $2^K-1\in S_K$ with $E_j=j$ on the burn ($K\le22$); survivors are higher-fuel than average.

```bash
python3 scripts/verify_tree_survivors.py    # prints PASS for every claim
```
