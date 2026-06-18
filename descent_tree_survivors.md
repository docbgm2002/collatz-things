# The Descent-Tree Survivors Are the Spine

**Building on:** `verify_descent_tree.py`, `stopping_time_density.md`, `recharge_nogo.md`, `mersenne_repunit_reduction.md`
**Status:** Exploratory synthesis with one exact spine result and finite survivor certificates. The proposed universal density bound is not yet proved.
**License:** CC-BY 4.0

---

## Abstract

The branching certificate in `verify_descent_tree.py` discharges many residue classes mod $2^K$ but leaves a stubborn set undischarged at every tested depth. The survivors are valuation-deficient classes and are anchored by the **Mersenne spine**: the all-ones residue $2^K-1$ survives through its initial burn, where all valuations are \(1\). Finite computations show a decreasing survivor fraction bounded by \(\rho^K\) through the tested range. A proof of that bound for every \(K\) is still missing because tree depth counts known low bits, whereas the Cramér estimate in `stopping_time_density.md` counts a fixed number of odd-steps.

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

**Conjecture 1 (survivor-density bound).** $\operatorname{dens}(S_K)=|S_K|/2^{K-1}\le \rho^{K}$, with $\rho=e^{-I(\log_2 3)}=0.9465\ldots$, and the density is non-increasing.

The verifier confirms this for \(6\le K\le20\). The earlier attempted proof used the single-time event \(E_K\le\theta K\), but the symbol \(K\) played two different roles: modulus depth in the tree and odd-step count in the Cramér estimate. No valid containment between those events has yet been established.

(Verified: $\operatorname{dens}(S_K)$ runs from $0.53$ at $K=6$ to $0.14$ at $K=20$, always $\le\rho^K$.)

---

## 2. The spine is the anchor

**Proposition 2 (Mersenne survives every depth).** For all $K$, $2^K-1\in S_K$.

*Proof.* By the burn closed form (`recharge_nogo.md` Lemma 3 / `mersenne_repunit_reduction.md` Lemma R1), $2^K-1$ has $e_i=1$ for its first $K-1$ steps, so $E_j=j$ and $S_j=E_j-\theta j=(1-\theta)j<0$ throughout the burn — the descent line is never reached while the bits last, so $L(2^K-1)>K$. It is the **unique minimal-valuation orbit** ($E_j$ as small as possible), the extreme point of the lower tail. $\;\blacksquare$

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
| `verify_descent_tree.py` | residue classes undischarged at depth $K$ |
| `stopping_time_density.md` | fixed-step lower-tail "non-$K$-good" classes, density $\le\rho^K$ |
| spine notes | high-fuel / near-Mersenne classes, anchored by $2^K-1$ |

They overlap conceptually but have not been proved to be the same set. The
spine shows that no finite tree depth discharges every residue class: the
all-ones residue survives at each depth. The observed geometric shrinkage of
the remaining classes is a finite certificate and conjectural pattern.

---

## 4. What is and is not proved

**Proved:** the spine anchor $2^K-1\in S_K$ through its initial burn and its minimal initial valuation sequence.

**Finite certificate:** the measured survivor fractions are non-increasing and at most \(\rho^K\) for \(6\le K\le20\).

**Open:** the universal density bound and any exact identification of the tree survivors with the stopping-time lower-tail set.

**Not proved:** a measure formula for the limiting \(2\)-adic survivor set, or
that every positive integer eventually leaves the corresponding survivor
classes. The latter is part of the Collatz problem.

---

## Appendix — Verification

`verify_tree_survivors.py` checks: $\operatorname{dens}(S_K)\le\rho^K$ and non-increasing ($K=6..20$); $2^K-1\in S_K$ with $E_j=j$ on the burn ($K\le22$); survivors are higher-fuel than average.

```bash
python3 verify_tree_survivors.py    # prints PASS for every claim
```
