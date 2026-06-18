# The Mersenne–Repunit Reduction for the $3x+1$ Map

**Building on:** `recharge_nogo.md` (burn closed form), `Mod8_Rail_Descent.md`, `collatz_rail7_new_results.md` (escape value $(3^n-1)/2$)
**Status:** Theorem R2 and Corollary R3 are exact; Observation R4 is empirical and explicitly *not* a proof. This note does **not** settle the Mersenne epoch (Conjecture G).
**License:** CC-BY 4.0

---

## Abstract

The Mersenne number $2^n-1$ is the worst case for the odd-step map: its trailing block of $n$ ones makes it grow for $n-1$ steps. We show that this growth terminates on a canonical point. For odd $n$,

$$
f^{(n)}\!\big(2^n-1\big)\;=\;\frac{3^n-1}{2}\;=\;1+3+3^2+\cdots+3^{n-1},
$$

the **base-3 repunit** $a_n$, reached in *exactly* $n$ odd-steps; for even $n$ the same step divides further, landing on $a_n/2^{\,1+v_2(n)}$. The repunits form a ladder $3a_m+1=a_{m+1}$. This yields an **exact reduction** of the Mersenne epoch to a single first-passage question for $a_n$ (Corollary R3). We then report — honestly as an empirical observation, not a theorem — that the descent *from* $a_n$ is statistically generic, so the spine's exact structure does **not** make the epoch bound tractable: Conjecture G is the general Collatz difficulty in disguise (Observation R4).

All exact claims are checked in `verify_repunit_reduction.py`.

---

## 0. Setup

For odd $x$, $f(x)=(3x+1)/2^{\,v_2(3x+1)}$ is the odd-step (shortcut) map. Write the **base-3 repunit**

$$
a_m \;=\; \frac{3^m-1}{2} \;=\; \sum_{i=0}^{m-1}3^i \qquad(a_0=0,\ a_1=1,\ a_2=4,\ a_3=13,\dots).
$$

For an odd $x$, its **epoch** is $\operatorname{epoch}(x)=\min\{t\ge1: f^{(t)}(x)<x\}$ (first passage strictly below the start).

---

## 1. The repunit ladder

**Lemma R0.** For every $m\ge0$, $\;3a_m+1=a_{m+1}$.

*Proof.* $3a_m+1=\dfrac{3(3^m-1)}{2}+1=\dfrac{3^{m+1}-3+2}{2}=\dfrac{3^{m+1}-1}{2}=a_{m+1}$. $\;\blacksquare$

So under the *bare* map $x\mapsto 3x+1$ the repunits climb forever; only the $2$-adic division of the odd-step map can leave the ladder.

---

## 2. The burn (recalled)

**Lemma R1 (burn closed form).** For $M_n=2^n-1$ and $0\le j\le n-1$,

$$
f^{(j)}(M_n)=x_j=3^{\,j}2^{\,n-j}-1,\qquad \tau(x_j)=n-j,\qquad v_2(3x_j+1)=1\ (j\le n-2),
$$

so after $n-1$ steps the orbit sits at the peak $x_{n-1}=2\cdot3^{\,n-1}-1$. The sequence $x_j=2^n(3/2)^j-1$ is strictly increasing, so $x_j\ge x_0$ throughout: *the orbit never dips below the start during the burn.*

*Proof.* `recharge_nogo.md`, Lemma 3. $\;\blacksquare$

---

## 3. The reduction

**Theorem R2 (Mersenne $\to$ repunit).** For $n\ge2$, the $n$-th odd-step satisfies $3x_{n-1}+1=2(3^n-1)$ and

$$
f^{(n)}(2^n-1)=\frac{3^n-1}{2^{\,v_2(3^n-1)}}=
\begin{cases}
\dfrac{3^n-1}{2}=a_n, & n\text{ odd},\\[2mm]
\dfrac{3^n-1}{2^{\,2+v_2(n)}}=\dfrac{a_n}{2^{\,1+v_2(n)}}, & n\text{ even}.
\end{cases}
$$

*Proof.* $3x_{n-1}+1=3(2\cdot3^{\,n-1}-1)+1=2\cdot3^{\,n}-2=2(3^n-1)$, so $v_2(3x_{n-1}+1)=1+v_2(3^n-1)$ and $f(x_{n-1})=(3^n-1)/2^{\,v_2(3^n-1)}$. By Lifting-the-Exponent, $v_2(3^n-1)=1$ for odd $n$ and $=2+v_2(n)$ for even $n$. Substituting gives the two cases; $a_n=(3^n-1)/2$ identifies the odd case as the repunit. $\;\blacksquare$

**Corollary R3 (epoch reduction).** For odd $n\ge3$,

$$
\operatorname{epoch}(2^n-1)=n+\sigma(a_n),\qquad
\sigma(a_n):=\min\{s\ge1: f^{(s)}(a_n)<2^n-1\}.
$$

*Proof.* By Lemma R1 the orbit stays $\ge x_0=2^n-1$ for the first $n-1$ steps; at step $n$ it is $a_n=(3^n-1)/2>2^n-1$ for $n\ge2$ (since $3^n/2\gg2^n$). So no passage below $x_0$ occurs in the first $n$ steps, and the first passage is the first passage of $a_n$ below $x_0$, shifted by $n$. $\;\blacksquare$

The Mersenne epoch problem is therefore *exactly* the question: **how fast does the base-3 repunit $a_n$ fall below $2^n-1$?** The first $n$ steps are completely solved; all remaining difficulty lives in $\sigma(a_n)$.

---

## 4. Where the difficulty goes (empirical)

**Observation R4 (the residual is generic — empirical, not proved).** Over odd $n\in[11,159]$, the descent of $a_n$ below $x_0$ is statistically indistinguishable from a generic odd orbit:

| quantity (post-$a_n$) | measured | generic model |
|---|---|---|
| $\Pr[v_2(3x+1)=k]$ | $1{:}0.499,\ 2{:}0.246,\ 3{:}0.125,\ 4{:}0.058,\ 5{:}0.038$ | $2^{-k}$ |
| mean $v_2(3x+1)$ | $2.016$ | $2.000$ |
| rails mod 8 | $\approx$ uniform | uniform |
| orbits exceeding the burn peak $2\cdot3^{\,n-1}-1$ | $28/75$ | — |
| $\sigma(a_n)/n$ | mean $1.37$, sd $0.46$, range $[0.55,2.74]$ | random-drift spread |

Consequences (heuristic): there is no monotone envelope past $a_n$ (orbits routinely climb back above the burn peak), and $\sigma(a_n)$ inherits the variance of a generic drift. Hence the spine's exact structure does **not** linearise the epoch: proving $\sigma(a_n)=O(n)$ — i.e. Conjecture G — is equivalent to a generic $O(\cdot)$ stopping-time bound, which is the open heart of the conjecture. We record this as the reason to pursue *density/average* control (where genericity is the asset) rather than a spine-specific epoch proof.

---

## 5. What is and is not proved

**Proved exactly:** the repunit ladder (R0); the burn closed form (R1, from `recharge_nogo.md`); the reduction $f^{(n)}(2^n-1)=(3^n-1)/2^{v_2(3^n-1)}$ for all $n\ge2$, equal to the base-3 repunit $a_n$ for odd $n$ (R2); and the exact epoch split $\operatorname{epoch}(2^n-1)=n+\sigma(a_n)$ (R3).

**Empirical only:** the genericity of $\sigma(a_n)$ (R4). No bound on $\sigma(a_n)$ — and hence no proof of the Mersenne epoch — is claimed.

---

## Appendix — Verification

`verify_repunit_reduction.py` checks with exact integer arithmetic:

* **R0:** $3a_m+1=a_{m+1}$ for $m\le500$.
* **R1:** $f^{(j)}(2^n-1)=3^j2^{\,n-j}-1$ and monotone $\ge x_0$, $n\le200$.
* **R2:** $f^{(n)}(2^n-1)=(3^n-1)/2$ for odd $n$, $=(3^n-1)/2^{2+v_2(n)}$ for even $n$, $n\le200$.
* **R3:** the first passage below $x_0$ occurs at step $n+\sigma(a_n)$, with no earlier passage, for odd $n\le120$.
* **R4 (empirical):** the post-$a_n$ statistics above are recomputed and reported (geometric $v_2$ law, mean $\approx2$, peak-exceedance count).

```bash
python3 verify_repunit_reduction.py   # PASS on R0-R3; prints the R4 statistics
```
