# Mod-8 Rail Descent for the $3x+1$ Map

**Exact one-step descent on three residue rails, a deterministic bridge, and a machine-verified finite-window certificate**

**Author:** Dr. Bry
**Status:** Proved results + a finite certificate — *not* a proof of the Collatz conjecture
**License:** CC-BY 4.0

---

## Abstract

We organise the odd residues modulo $8$ into four *rails* and establish exact, elementary descent behaviour for three of them. For $x \equiv 1 \pmod 8$ the odd-step map sends $x = 8y+1$ to exactly $6y+1$; for $x \equiv 5 \pmod 8$ it sends $8y+5$ to at most $3y+2$; both are strict one-step descents (with the sole fixed point $x=1$). For $x \equiv 3 \pmod 8$ we give an exact two-step affine *bridge* $8y+3 \mapsto 9y+4$ that holds as a polynomial identity for every integer $y$. The remaining rail $x \equiv 7 \pmod 8$ is analysed via a closed-form "stay-in-rail" recursion: we prove the number of consecutive stays equals $\lfloor v_2(y+1)/2 \rfloor$, so every input escapes rail 7 in finitely many two-step blocks; the all-ones index family escapes by a deterministic rail-1/rail-3 alternation. Finally, we report an independent machine verification that **every** odd $x \le 10^6$ reaches a strictly smaller value within at most $111$ odd-steps. We are explicit throughout about the boundary between exact theorem and finite computation: the global ("window-free") statement remains open and is, in effect, equivalent to the Collatz conjecture itself.

---

## 1. Setup

For odd $x$ define the **odd-step map**
$$
f(x) \;=\; \frac{3x+1}{2^{\,v_2(3x+1)}},
$$
where $v_2(\cdot)$ is the $2$-adic valuation (the exponent of the largest power of $2$ dividing its argument). Because $3x+1$ is even for odd $x$, $f(x)$ is again odd; $f$ is the standard "shortcut" Collatz map restricted to odd integers. A single application of $f$ is one **odd-step**; we measure descent in odd-steps.

Every odd number lies in exactly one of four **rails** according to its residue modulo $8$: $8y+1,\ 8y+3,\ 8y+5,\ 8y+7$ (with $y \ge 0$). We treat each rail in turn. Rails $1$ and $5$ descend immediately; rail $3$ bridges deterministically; rail $7$ is the only one requiring a recursion, and that recursion has an exact closed form.

---

## 2. Rails $8y+1$ and $8y+5$: immediate descent

**Lemma 1 (Rail 1, exact image).** For every $y \ge 0$,
$$
3(8y+1)+1 = 24y+4 = 4\,(6y+1), \qquad 6y+1 \text{ odd},
$$
so $v_2(3(8y+1)+1) = 2$ exactly and
$$
f(8y+1) = 6y+1.
$$
In particular $f(8y+1) = 6y+1 < 8y+1$ for all $y \ge 1$; the case $y=0$ is the fixed point $x=1$.

*Proof.* $24y+4 = 4(6y+1)$ and $6y+1$ is odd, giving $v_2 = 2$ and image $6y+1$. The inequality $6y+1 < 8y+1$ is $0 < 2y$, i.e. $y \ge 1$. $\qquad\blacksquare$

**Lemma 2 (Rail 5, one-step descent).** For every $y \ge 0$,
$$
3(8y+5)+1 = 24y+16 = 8\,(3y+2),
$$
so $v_2(3(8y+5)+1) \ge 3$ and therefore
$$
f(8y+5) \le 3y+2 < 8y+5.
$$

*Proof.* $24y+16 = 8(3y+2)$, so at least three factors of $2$ divide $3x+1$; dividing by $2^{v_2} \ge 2^3$ gives $f(8y+5) \le (24y+16)/8 = 3y+2$, and $3y+2 < 8y+5$ for all $y \ge 0$. (When $3y+2$ is itself even, $v_2 > 3$ and the image is strictly smaller still.) $\qquad\blacksquare$

Together, Lemmas 1–2 give immediate strict descent on **half** of all odd integers (residues $1$ and $5$ modulo $8$), with the single exception of the fixed point.

---

## 3. Rail $8y+3$: an exact deterministic bridge

Rail $3$ does not descend in one step in general, but it maps to the auxiliary track $9y+4$ by a fixed sequence of divisions, as an exact identity.

**Lemma 3 (Bridge $8y+3 \to 9y+4$).** Apply $3x+1$ and divide by the *prescribed* powers $2^1$ then $2^2$ (a "fixed-division bridge"). Then for every integer $y$,
$$
8y+3 \;\xrightarrow{\;\div 2\;}\; 12y+5 \;\xrightarrow{\;\div 4\;}\; 9y+4 .
$$

*Proof.* Two exact computations:
$$
3(8y+3)+1 = 24y+10 = 2\,(12y+5),
\qquad
3(12y+5)+1 = 36y+16 = 4\,(9y+4).
$$
Both divisions are exact for every integer $y$ (the identities are polynomial in $y$, so they hold over $\mathbb{Z}$, including negative $y$). $\qquad\blacksquare$

**Remark (relation to the true odd-step).** The bridge fixes the divisions rather than dividing by the full $2^{v_2}$. Since
$$
36y+16=4(9y+4),
$$
we have $v_2(36y+16)=2+v_2(9y+4)$. If $y$ is odd, then $9y+4$ is odd, so the valuation is exactly $2$ and the true odd-step from $12y+5$ is $9y+4$. If $y$ is even, then $9y+4$ is even, so the valuation is at least $3$ and the true odd-step is the odd part of $9y+4$, which is at most $(9y+4)/2$. Thus the fixed bridge is an upper envelope for the true odd-step.

---

## 4. Rail $8y+7$: exact closed-form analysis and escape dynamics

Rail $7$ is the only rail that can map back into itself under two odd steps, so descent here requires a recursion. By developing an exact closed-form index tracker, we resolve the recursion completely and prove that all orbits escape to other rails in finite steps, except the all-ones class which escapes via a deterministic alternating pattern.

Write the **two-odd-step map** $f_2 = f \circ f$.

### Theorem 1 (Exact image for two odd steps)
For every integer $y \ge 0$, the two-odd-step image of $x = 8y+7$ is
$$
f_2(8y+7) \;=\; 18y+17.
$$

*Proof.* First, apply $3x+1$ and divide by $2^{v_2}$:
$$
3(8y+7)+1 = 24y+22 = 2\,(12y+11).
$$
Since $12y+11$ is odd, $f(8y+7) = 12y+11$ exactly.
Now apply the second odd step:
$$
3(12y+11)+1 = 36y+34 = 2\,(18y+17).
$$
Since $18y+17$ is odd, $f_2(8y+7) = 18y+17$ exactly. Both steps divide by exactly one factor of $2$. $\quad\blacksquare$

### The Stay-in-Rail Recursion
The image $18y+17$ lies on rail 7 if and only if:
$$
18y+17 \equiv 7 \pmod 8 \iff 2y+1 \equiv 7 \pmod 8 \iff y \equiv 3 \pmod 4.
$$
When $y \equiv 3 \pmod 4$, we can write $18y+17 = 8y' + 7$. Solving for the new index $y'$ gives the exact **stay-in-rail index recursion**:
$$
g(y) \;=\; \frac{9y+5}{4},
$$
which is valid exactly when $y \equiv 3 \pmod 4$.

### Theorem 2 (Closed form for repeated rail-7 stays)
Suppose the orbit remains on rail 7 for $d$ consecutive applications of $f_2$. Then the rail index after $d$ stays is
$$
y_d \;=\; \left(\frac{9}{4}\right)^d(y+1) - 1.
$$

*Proof.* We prove by induction on $d$. For $d=0$, we have $y_0 = y$, which matches the formula. Assume the formula holds for $d$. Then:
$$
y_{d+1} = \frac{9y_d+5}{4} = \frac{9\left[\left(\frac{9}{4}\right)^d(y+1) - 1\right]+5}{4} = \frac{9^{d+1}(y+1) - 9\cdot 4^d + 5\cdot 4^d}{4^{d+1}} = \left(\frac{9}{4}\right)^{d+1}(y+1) - 1,
$$
which completes the induction. $\quad\blacksquare$

### Theorem 3 (Exact survival depth)
For $x = 8y+7$, the number of consecutive returns to rail 7 under $f_2$ is
$$
D(y) \;=\; \left\lfloor \frac{v_2(y+1)}{2} \right\rfloor.
$$

*Proof.* A further stay occurs if and only if $y_d \equiv 3 \pmod 4$, which is equivalent to $y_d + 1 \equiv 0 \pmod 4$, or $v_2(y_d + 1) \ge 2$.
Using Theorem 2:
$$
v_2(y_d+1) = v_2\left(\frac{9^d(y+1)}{4^d}\right) = v_2(y+1) - 2d,
$$
since $9^d$ is odd. A stay is therefore possible if and only if $v_2(y+1) - 2d \ge 2$. The total number of completed stays is the largest integer $d$ satisfying this, which is exactly $D(y) = \lfloor v_2(y+1)/2 \rfloor$. $\quad\blacksquare$

### Escape Rails
Once the recursion stops after $D$ stays, the exit value is $x_{\text{exit}} = 18y_D + 17$. Modulo 8, this value is determined by the residue of $y_D \pmod 4$:
$$
x_{\text{exit}} \equiv 2y_D + 1 \pmod 8.
$$
Since $y_D \not\equiv 3 \pmod 4$ at the exit point, we obtain:
* If $y_D \equiv 0 \pmod 4$, then $x_{\text{exit}} \equiv 1 \pmod 8$ (escape to Rail 1, immediate descent).
* If $y_D \equiv 1 \pmod 4$, then $x_{\text{exit}} \equiv 3 \pmod 8$ (escape to Rail 3, deterministic bridge).
* If $y_D \equiv 2 \pmod 4$, then $x_{\text{exit}} \equiv 5 \pmod 8$ (escape to Rail 5, immediate descent).

### Mersenne Index Escape Alternation
Consider the all-ones Mersenne-index family $y_0 = 2^k - 1$ ($k \ge 2$), so $y_0 + 1 = 2^k$ and $v_2(y_0+1) = k$. By Theorem 3, the survival depth is $D = \lfloor k/2 \rfloor$.
* **Case 1 ($k = 2d$ even):** We have $D = d$ stays. Using Theorem 2:
  $$
  y_d = \left(\frac{9}{4}\right)^d 2^{2d} - 1 = 9^d - 1 \implies x_{\text{exit}} = 18\cdot 9^d - 1 \equiv 1 \pmod 8.
  $$
  So even $k$ exits to **Rail 1** (immediate descent).
* **Case 2 ($k = 2d+1$ odd):** We have $D = d$ stays. Using Theorem 2:
  $$
  y_d = \left(\frac{9}{4}\right)^d 2^{2d+1} - 1 = 2\cdot 9^d - 1 \implies x_{\text{exit}} = 18\cdot (2\cdot 9^d - 1) + 17 = 36\cdot 9^d - 1 \equiv 3 \pmod 8.
  $$
  So odd $k$ exits to **Rail 3** (deterministic bridge).

**Corollary (Mersenne alternation).** The all-ones family $y = 2^k-1$ escapes rail 7 via a deterministic alternating sequence based on the parity of $k$:
$$
k \text{ even} \implies \text{Rail } 1, \qquad k \text{ odd} \implies \text{Rail } 3.
$$
This removes any exception status from the all-ones numbers; they escape the rail via a completely predictable, closed-form pattern.

---

## 5. Finite-window certificate (machine-verified)

Combining §§2–4 reduces "does an odd number descend?" to a finite recursion on rail $7$. Carrying that recursion out to a fixed bound yields a finite certificate. We verified the following **independently** (the script enumerates every odd input and follows the true odd-step map, not a presupposed macro):

> **Finite-window result (machine-verified).** Every odd integer $x$ with $3 \le x \le 10^6$ reaches a strictly smaller value within at most $111$ odd-steps. The worst case in this range is $x = 626{,}331$. No exceptions occur; $x=1$ is the fixed point.

This is a statement about a finite range, established by exhaustive computation. It is *evidence for*, not a proof of, the conjecture.

---

## 6. What is and is not proved

**Proved exactly (all $y$):**
* The rail-$1$ image $f(8y+1)=6y+1$ (Lemma 1).
* The rail-$5$ descent $f(8y+5)\le 3y+2$ (Lemma 2).
* The bridge $8y+3\to 9y+4$ (Lemma 3).
* The rail-$7$ exact two-step image, stay-in-rail formula, exact stay formula, stay depth, and Mersenne alternation (Theorems 1–3 and Corollary).

**Established by finite computation:** 100% one-value descent for all odd $x \le 10^6$ within $\le 111$ odd-steps (§5); all rail-7 theorems checked exhaustively to $y \le 5\times10^5$.

**Not proved (open):** a *window-free* statement — that the finite recursion terminates for **all** odd integers without an a-priori bound. The natural route is a merge-certificate over all residues modulo a fixed $2^K$ (e.g. $K=12$): one would have to exhibit, for each odd residue $r \bmod 2^K$, a fixed macro and frozen valuation conditions under which the affine identity forces descent or merge for *all* $y \equiv r$. Completing such a program for every residue would constitute a proof of the Collatz conjecture; it is not a polishing step, and nothing here closes it.

Two honest caveats. First, the bridge of §3 controls rail $3$ only up to the $9y+4$ track; descent on $9y+4$ itself is part of the same open finite-to-infinite gap, not a separate easy lemma. Second, the rail-$7$ survival cap bounds how long an input *stays in rail 7*, not the full trajectory length; the global trajectory bound is exactly what remains open.

---

## Appendix A. Verification

All claims were checked by exact integer arithmetic (no floating point); a reproducible script accompanies this note.

- **Lemma 1:** $f(8y+1)=6y+1$ with no exceptions, and strict descent for $y\ge 1$, over $y < 3\times10^5$.
- **Lemma 2:** $f(8y+5)\le 3y+2$ and $f(8y+5) < 8y+5$, no exceptions, over $y < 3\times10^5$.
- **Lemma 3:** the two bridge identities $24y+10=2(12y+5)$ and $36y+16=4(9y+4)$ hold for all tested integers $y$ including negatives.
- **Theorems 1–3 and Corollary:** the stay formula, stay depth, and Mersenne escape alternation checked exhaustively over $y < 5\times10^5$, with $100\%$ match and zero exceptions.
- **§5:** exhaustive descent check over all odd $x\in[3,10^6]$; max odd-steps to first descent $=111$ at $x=626{,}331$; zero failures.
