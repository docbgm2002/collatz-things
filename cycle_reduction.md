# A Cycle Reduction for the $3x+1$ Map

**Building on:** `stopping_time_density.md` (affine accumulation, descent density), `Mod8_Rail_Descent.md`
**Status:** C1 is an exact identity; C2/C4 are machine-verified finite results; C3 is an exact corollary; C5 states the wall. This note does **not** exclude nontrivial cycles.
**License:** CC-BY 4.0

---

## Abstract

The exact affine accumulation of `stopping_time_density.md` turns the cycle question into one explicit equation. A $K$-odd-step cycle through $x$ forces

$$
x\,(2^{E_K}-3^K)=c_K,\qquad c_K=\sum_{i=0}^{K-1}3^{\,K-1-i}2^{E_i}>0,
$$

so $2^{E_K}>3^K$ and $x=c_K/(2^{E_K}-3^K)$ (C1). From this we get, elementarily: only the fixed point $x=1$ for $K\le8$ by exhaustive search (C2); **cycle minima have natural density $0$** as a corollary of the stopping-time density theorem (C3); and **no nontrivial cycle has an element $\le10^6$** by machine check (C4). We are explicit that excluding *all* cycles reduces to lower-bounding the gap $|2^{E_K}-3^K|$ — the transcendence-theoretic wall handled by Steiner (1977) and Simons–de Weger (2005), which our elementary machinery does not reach (C5).

---

## 0. Setup

For odd $x$, $f(x)=(3x+1)/2^{v_2(3x+1)}$. A **nontrivial cycle** is an odd $x>1$ with $f^{(K)}(x)=x$ for some $K\ge1$ ($K$ = number of odd-steps). Recall (`stopping_time_density.md`, Lemma 1) the accumulation $f^{(K)}(x)=(3^Kx+c_K)/2^{E_K}$ with $c_K=\sum_{i<K}3^{K-1-i}2^{E_i}$, $E_K=\sum_{i<K}e_i$, $\theta=\log_2 3$.

---

## 1. The cycle equation (C1)

**Theorem C1.** If $f^{(K)}(x)=x$ then

$$
x\,(2^{E_K}-3^K)=c_K,\qquad\text{equivalently}\qquad x=\frac{c_K}{2^{E_K}-3^K}.
$$

In particular $c_K>0$ forces $2^{E_K}>3^K$, i.e. $E_K\ge\lceil K\log_2 3\rceil$.

*Proof.* Set $f^{(K)}(x)=x$ in $x_K=(3^Kx+c_K)/2^{E_K}$: then $x\,2^{E_K}=3^Kx+c_K$. Since $c_K>0$, $2^{E_K}-3^K=c_K/x>0$. $\;\blacksquare$

The fixed point realises it: $K=1$, $e_0=2$, $c_1=1$, $x=1/(2^2-3)=1$.

**Bounds.** With $3^{K-1}\le c_K<(3/2)^K2^{E_K}$ (`stopping_time_density.md`, Lemma 1), a cycle element satisfies $\dfrac{3^{K-1}}{2^{E_K}-3^K}\le x<\dfrac{(3/2)^K2^{E_K}}{2^{E_K}-3^K}$ — so element sizes are governed entirely by the gap $2^{E_K}-3^K$.

---

## 2. No small cycles (C2)

**Result C2 (machine-verified).** Enumerating the equation over all valuation patterns for $K\le8$ — every increasing $0=E_0<\dots<E_{K-1}<E_K$ with $2^{E_K}>3^K$, testing whether $c_K/(2^{E_K}-3^K)$ is a positive odd integer that genuinely cycles — yields **only $x=1$**.

---

## 3. Cycle minima have density zero (C3)

**Corollary C3.** The set of minima of nontrivial cycles (a fortiori, of all cycle elements) has natural density $0$.

*Proof.* A cycle's minimum $m$ never goes below itself, so its stopping time is infinite: $\sigma(m)=\infty$. By `stopping_time_density.md`, $\{\sigma=\infty\}\subseteq\{\text{not }K\text{-good}\}$ for every $K$, a set of density $\le\rho^K$; hence $\operatorname{dens}\{\sigma=\infty\}\le\inf_K\rho^K=0$. Cycle minima form a subset, so density $0$. $\;\blacksquare$

This places nontrivial-cycle starting points inside the same vanishing hard core as `descent_tree_survivors.md` — almost no integer can begin a cycle.

---

## 4. Finite exclusion (C4)

**Result C4 (machine-verified).** Every odd $m\in[3,10^6]$ descends below itself within $\le111$ odd-steps. Since a cycle element is its own non-descender, **no nontrivial cycle has any element $\le10^6$.** (The same exhaustive descent sweep underlies `Mod8_Rail_Descent.md` §5.)

---

## 5. The wall (C5)

To exclude cycles outright, C1 shows it suffices to prevent $x=c_K/(2^{E_K}-3^K)$ from being a consistent positive integer for any $K$. With $E_K=\lceil K\theta\rceil$ the gap $2^{E_K}-3^K$ can be tiny — exactly when $2^{E_K}/3^K$ is a near-convergent of $\theta=\log_2 3$ — making the bound on $x$ enormous. Controlling this gap is a statement about the **irrationality measure of $\log_2 3$**: Steiner (1977) excluded $1$-circuit cycles and Simons–de Weger (2005) excluded cycles of up to $68$ circuits, both via Baker-type linear-forms-in-logarithms bounds. Our elementary machinery cleanly *reduces* cycle exclusion to that gap bound but does not supply it; that transcendence input is the wall.

---

## 6. What is and is not proved

**Proved / verified:** the cycle equation C1 (exact); only $x=1$ for $K\le8$ (C2); cycle minima have density $0$ (C3, exact corollary of the density theorem); no cycle element $\le10^6$ (C4).

**Not proved:** the nonexistence of nontrivial cycles. That needs a lower bound on $|2^{E_K}-3^K|$ (transcendence theory), which this note isolates but does not establish.

---

## Appendix — Verification

`verify_cycle_reduction.py` checks: C1 the cycle equation as an exact identity (fixed point + $x_K=x\iff x(2^{E_K}-3^K)=c_K$); C2 the $K\le8$ search returns only $\{1\}$; C4 every odd $m\le10^6$ descends (so no cycle element $\le10^6$); C3 stated as the corollary.

```bash
python3 verify_cycle_reduction.py   # prints PASS for every claim
```
