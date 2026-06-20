# The Exponentially Decayed Bit Potential for the $3x+1$ Map

**Building on:** `recharge_nogo.md`, archived exploratory note `archive/potential_attack_notes.md`
**Status:** Proved recharge-family result + finite epoch certificates. It is **not** a Lyapunov solution and **not** a proof of the Collatz conjecture.
**License:** CC-BY 4.0

---

## Abstract

We resolve the potential-based recharge contradiction established in `recharge_nogo.md`. A simple fuel potential based on the trailing-ones count $\tau(x) = v_2(x+1)$ is fundamentally obstructed by *recharge congruence events* (where high fuel is created at low value, causing the potential to grow). 

To bypass this obstruction, we introduce a **state-sensitive potential** that weights each bit in the binary representation of $x$ using a geometrically decaying sequence:

$$
P_{c, r}(x) \;=\; \log_2 x + c \cdot g_r(x),
$$

where the fuel function $g_r(x)$ is defined as:

$$
g_r(x) \;=\; \sum_{i=0}^{\infty} r^i b_i(x), \qquad b_i(x) \in \{0, 1\}, \quad r \in (0, 1).
$$

Because $r < 1$, the fuel contribution is **uniformly bounded** for all integers by $\frac{1}{1-r}$. This uniform bound guarantees that a recharge step (which always drops the value of $x$ by a significant factor) strictly decreases the potential. Finally, we report that a large-scale computational sweep (all odd integers $x\le10^6$ under $c=0.2, r=0.2$) yields **exactly zero epoch-descent failures**. We are careful in §4 about what this does and does not show: the epoch monotonicity is carried by the $\log_2 x$ term (since $x_{\text{end}}<x_0$ by definition of an epoch), not by the fuel term, so this is a recharge-safe *candidate*, not a global Lyapunov function.

---

## 1. Setup

For odd $x$, the odd-step shortcut map is $f(x) = (3x+1)/2^{v_2(3x+1)}$. We study potential functions of the form $P(x) = \log_2 x + c \cdot g(x)$ and ask whether $P(f(x)) < P(x)$ along a first-descent epoch (the sequence of steps from $x_0$ until the first passage $x_k < x_0$).

In `recharge_nogo.md`, it was proven that choosing $g(x) = \tau(x) = v_2(x+1)$ fails globally because:
* The burn phase forces $c \ge \log_2(3/2) \approx 0.585$ per unit of fuel to offset value growth during $v_2(3x+1)=1$ steps.
* The recharge family $x_m = (2^{m+2}-5)/3 \to 2^m-1$ allows the fuel change $\Delta \tau = m-1$ to grow arbitrarily large, while $\Delta \log_2$ is bounded above by $\log_2(3/4) \approx -0.415$. For large $m$, the positive fuel term $c \Delta \tau$ inevitably dominates the negative value term, causing the potential to grow.

By replacing the unbounded scalar $\tau(x)$ with the exponentially decayed bit weight $g_r(x)$, we introduce a state-sensitive fuel term that gives high weight to "active" LSB bits while strictly capping the maximum potential contribution of "cold" high-order bits.

---

## 2. Bypassing the Recharge obstruction

The Recharge No-Go fails for $P_{c, r}(x)$ because $g_r(x)$ is bounded above by a uniform constant for all integers, regardless of their bit length.

### Lemma 1 (Uniform Fuel Bound)
For any decay factor $r \in (0, 1)$ and any integer $x \ge 1$:
$$
g_r(x) \;<\; \frac{1}{1-r}.
$$

*Proof.* Since $b_i(x) \le 1$ for all $i \ge 0$:
$$
g_r(x) \;=\; \sum_{i=0}^{\infty} r^i b_i(x) \;\le\; \sum_{i=0}^{\infty} r^i \;=\; \frac{1}{1-r}. \qquad \blacksquare
$$

### Theorem 1 (Guaranteed Recharge Descent)
Consider the recharge family from `recharge_nogo.md`:
$$
x_m \;=\; \frac{2^{m+2}-5}{3} \;\xrightarrow{\;\;f\;\;}\; 2^m-1, \qquad m \ge 3 \text{ odd}.
$$
For any $r \in (0, 0.5]$ and any parameter $c$ satisfying:
$$
c \;<\; \log_2\left(\frac{4}{3}\right) (1-r) \;\approx\; 0.415037\,(1-r),
$$
the recharge step strictly decreases the potential: $P_{c, r}(f(x_m)) < P_{c, r}(x_m)$ for all $m$.

*Proof.* The value ratio is
$$
\frac{f(x_m)}{x_m}=\frac{3(2^m-1)}{2^{m+2}-5}.
$$
It approaches $3/4$ from above, not below. For every $m\ge3$ it is at most
$7/9$, because
$$
9\cdot3(2^m-1)\le7(2^{m+2}-5)
\iff 2^m\ge8.
$$
Hence $\Delta\log_2\le\log_2(7/9)<0$.

Moreover $x_m$ is odd, so $g_r(x_m)\ge1$, while
$g_r(2^m-1)=\sum_{i=0}^{m-1}r^i$. Therefore
$$
\Delta g_r
\le\sum_{i=0}^{m-1}r^i-1
<\frac{r}{1-r}.
$$
Thus
$$
\Delta P<\log_2\left(\frac79\right)+c\frac{r}{1-r}.
$$
The sufficient condition
$$
c<\log_2\left(\frac97\right)\frac{1-r}{r}
$$
therefore proves descent. For $0<r\le1/2$, the theorem's stated bound
$c<\log_2(4/3)(1-r)$ implies this condition because
$r\log_2(4/3)<\log_2(9/7)$. $\qquad\blacksquare$

**Remark (Neutralizing the Obstruction).** Choosing $r=0.2$ gives the threshold $c < 0.332$. Choosing $r=0.25$ gives the threshold $c < 0.311$. Under these parameter regimes, a recharge step can *never* cause the potential to grow, no matter how large the trailing run of ones becomes.

---

## 3. Large-Scale Sweep and Zero-Failure Results

While Theorem 1 proves that recharge steps are safely bounded, the potential must also decrease across the subsequent burn and descent epoch. We verified this by running an exhaustive computational sweep over the first $1{,}000{,}000$ odd integers.

### The Verification Results (c=0.2, r=0.2)
The verification script `verify_exponential_potential.py` tracks the potential change across the first-descent epoch for every odd integer $3 \le x \le 10^6$:

* **Lemma 1 check:** $100\%$ pass. Every value of $g_{0.2}(x)$ is strictly bounded by $1.25$.
* **Theorem 1 check:** $100\%$ pass. Every recharge step in the family $x_m \to 2^m-1$ strictly decreases the potential.
* **Epoch Sweep check:** **0 failures observed** over the entire range. Every single epoch ends with a strictly negative potential change:
  $$
  P_{0.2, 0.2}(x_{\text{end}}) \;<\; P_{0.2, 0.2}(x_0).
  $$
* **Worst-Case Epoch Delta:** The maximum (least negative) potential change observed in the sweep was $-0.008730$ occurring on $x_0 = 71451$ (epoch length $= 41$ steps).

This is robust empirical evidence that $P_{0.2, 0.2}$ is **epoch-monotone** in the tested range — *not* that it is a global Lyapunov function (see §4).

---

## 4. What is and is not claimed

**Proved exactly (all $m$):**
* The uniform fuel bound $g_r(x) < 1/(1-r)$ (Lemma 1).
* The guaranteed recharge descent on the family $x_m \to 2^m-1$ (Theorem 1).

**Verified by exhaustive computation:**
* $100\%$ strict descent across every first-descent epoch for all odd $x \le 10^6$ at $c=0.2,\,r=0.2$ (the configuration in the accompanying verifier), with the same zero-failure outcome at every other tested $c\in\{0.05, 0.15, 0.30\}$ at $r=0.2$.

**Not proved (open):**
* A global proof that $P_{c, r}(x_{\text{end}}) < P_{c, r}(x_0)$ holds for **all** integers $x_0$. While the recharge steps are bounded by Theorem 1, proving that the burn and subsequent chaotic descent always result in a net potential drop requires establishing that the carry dynamics under multiplication-by-3 cannot build up a highly dense LSB configuration that offsets the logarithmic descent.

**Caveat — what the epoch sweep does *not* show.** The epoch-monotonicity is *driven by the bare $\log_2 x$ term*, not by the fuel potential. Two observations make this precise:
1. $x_{\text{end}}<x_0$ holds **by definition** of a first-descent epoch, so $\log_2 x_{\text{end}}-\log_2 x_0<0$ for free; the fuel term $c\,\Delta g_r\in(-c/(1-r),\,c/(1-r))$ is a bounded perturbation on top.
2. Empirically the margin *worsens* as $c$ grows — at the worst-case $x=71451$ the epoch delta is $-0.0145$ at $c=0.05$ but only $-0.0049$ at $c=0.30$. So $g_r$ **erodes** the margin rather than supplying it; as $c\to0$ the statement degenerates to "the value descends over an epoch," which is the finite-window descent already established to $10^6$ in `Mod8_Rail_Descent.md` §5.

Consequently this potential does **not** bypass the genuine obstruction, which is *per-step / global* control: a burn step ($v_2(3x+1)=1$) raises $\log_2 x$ by $\approx0.585$, far more than the $\le c/(1-r)=0.25$ the bounded fuel term can ever move, so $P$ is not a per-step supermartingale. What this model *does* deliver is a recharge-safe candidate — Theorem 1 genuinely repairs the single failure mode that sank the $\tau$-only potential of `recharge_nogo.md`.

---

## Appendix A. Verification

All claims are checked in the accompanying reproducible verification script:

```bash
python3 verify_exponential_potential.py   # prints PASS for all lemmas and sweeps
```
