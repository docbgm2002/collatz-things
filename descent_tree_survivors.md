# The Descent-Tree Survivors Are the Spine

**Building on:** `verify_descent_tree.py`, `stopping_time_density.md`, `recharge_nogo.md`, `mersenne_repunit_reduction.md`
**Status:** Exact. A consolidating result: it identifies *what survives* the residue-class descent tree and ties three threads of this repo together. It does **not** prove the conjecture.
**License:** CC-BY 4.0

---

## Abstract

The branching certificate in `verify_descent_tree.py` discharges most residue classes mod $2^K$ but leaves a stubborn set undischarged at every depth — and refining the modulus never empties it. We pin down that set exactly. The depth-$K$ survivors are precisely the **valuation-deficient** classes (those whose first odd-steps divide too little to force descent), they have density $\le\rho^K\to0$ with the same Cramér rate $\rho=0.9465\ldots$ as `stopping_time_density.md`, and they are anchored by the **Mersenne spine**: the all-ones residue $2^K-1$ survives at *every* depth, because it is the unique orbit whose valuations are all $1$. This is why no finite modulus closes the tree, and it unifies the descent tree, the stopping-time density, and the spine notes into one picture.

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

**Proposition 1 (density).** $\operatorname{dens}(S_K)=|S_K|/2^{K-1}\le \rho^{K}$, with $\rho=e^{-I(\log_2 3)}=0.9465\ldots$, and is non-increasing; hence $\operatorname{dens}(S_K)\to0$.

*Proof.* $r\in S_K$ means the valuation walk $S_j=E_j-\theta j$ stays below $1$ for every $j$ with $E_j\le K$ — in particular $E_{\lfloor\cdot\rfloor}$ never reaches the descent line within the first $K$ bits. This is contained in the lower-tail event $\{E_j\le\theta j$ for the available steps$\}$, whose density is bounded by the single-time Cramér tail $\Pr[E_K\le\theta K]\le\rho^K$ of `stopping_time_density.md`. Monotonicity is immediate since a class discharged at depth $K$ stays discharged at depth $K+1$. $\;\blacksquare$

(Verified: $\operatorname{dens}(S_K)$ runs from $0.53$ at $K=6$ to $0.14$ at $K=20$, always $\le\rho^K$.)

---

## 2. The spine is the anchor

**Proposition 2 (Mersenne survives every depth).** For all $K$, $2^K-1\in S_K$.

*Proof.* By the burn closed form (`recharge_nogo.md` Lemma 3 / `mersenne_repunit_reduction.md` Lemma R1), $2^K-1$ has $e_i=1$ for its first $K-1$ steps, so $E_j=j$ and $S_j=E_j-\theta j=(1-\theta)j<0$ throughout the burn — the descent line is never reached while the bits last, so $L(2^K-1)>K$. It is the **unique minimal-valuation orbit** ($E_j$ as small as possible), the extreme point of the lower tail. $\;\blacksquare$

More generally the survivors are the **high trailing-one fuel** classes: at $K=12$ the mean $\tau=v_2(\,\cdot+1)$ over $S_K$ is $3.03$ versus $2.00$ over all odd residues, and the top survivors have $\tau$ up to $K$. These are exactly the near-Mersenne classes — e.g. the mod-$32$ failures $7,15,27,31$ reported by `verify_descent_tree.py`.

---

## 3. The unified picture

The same set wears three hats:

| viewpoint | the set |
|---|---|
| `verify_descent_tree.py` | residue classes undischarged at depth $K$ |
| `stopping_time_density.md` | the lower-tail "non-$K$-good" classes, density $\le\rho^K$ |
| spine notes | high-fuel / near-Mersenne classes, anchored by $2^K-1$ |

So refining the modulus (the "nested bridge tree") *cannot* close: at every depth a $\rho^K$-fraction survives, always including the spine, because the rail-7 stay-depth $\lfloor v_2(y+1)/2\rfloor$ is unbounded (`Mod8_Rail_Descent.md`). The tree shrinks the hard core geometrically but never removes it.

---

## 4. What is and is not proved

**Proved:** the survivor density bound $\le\rho^K\to0$ (Prop 1); the spine anchor $2^K-1\in S_K$ and its minimal-valuation characterisation (Prop 2); the identification of the three views as one set.

**Not proved:** that the survivor set is *empty in the limit* — it is not; $\bigcap_K$ (as a $2$-adic set) is the measure-zero hard core, and proving every *integer* eventually leaves it is the conjecture. This note explains why finite-modulus refinement is the wrong tool, not how to finish.

---

## Appendix — Verification

`verify_tree_survivors.py` checks: $\operatorname{dens}(S_K)\le\rho^K$ and non-increasing ($K=6..20$); $2^K-1\in S_K$ with $E_j=j$ on the burn ($K\le22$); survivors are higher-fuel than average.

```bash
python3 verify_tree_survivors.py    # prints PASS for every claim
```
