
# Exact Results on the 8y+7 Rail in the Collatz 3x+1 Problem

**Building on:** docbgm2002/collatz-things (Mod-8 Rail Descent framework)  
**Date:** 2026-05-25  
**Status:** Theorems A-E are exact; Theorem F gives a post-bridge formula; Observations G-H are empirical/open

---

## 1. Introduction and Context

This document presents new exact theorems on the Collatz shortcut map restricted to the 8y+7 residue class ("rail 7"), building directly on the Mod-8 Rail Descent framework of [docbgm2002/collatz-things]. The original framework established:

- **Lemma 1:** Rail 1 (8y+1) maps exactly to 6y+1 (strict descent for y≥1)
- **Lemma 2:** Rail 5 (8y+5) maps to at most 3y+2 (strict descent)
- **Lemma 3:** Rail 3 (8y+3) has exact bridge 8y+3 → 12y+5 → 9y+4
- **Lemmas 4-5:** Rail 7 has finite escape with cap D(y) = ⌊v₂(y+1)/2⌋

Our contribution is a **closed-form solution** to the rail-7 recursion, enabling exact analysis of the Mersenne-like family and revealing a clean structural pattern in escape behavior.

---

## 2. Notation

For odd x, the **odd-step map** is:

$$f(x) = \frac{3x+1}{2^{v_2(3x+1)}}$$

The **two-odd-step map** is $f_2 = f \circ f$.

Rail 7: $x = 8y + 7$ with $y \geq 0$.

---

## 3. New Exact Theorems

### Theorem A (Closed-Form Two-Step Map on Rail 7)

For every integer $y \geq 0$:

$$f_2(8y + 7) = 18y + 17$$

**Proof.** Compute directly:
- $3(8y+7)+1 = 24y+22 = 2(12y+11)$. Since $12y+11$ is odd, $v_2 = 1$ and $f(8y+7) = 12y+11$.
- $3(12y+11)+1 = 36y+34 = 2(18y+17)$. Since $18y+17$ is odd, $v_2 = 1$ and $f_2(8y+7) = 18y+17$. ∎

**Corollary A1.** Both intermediate $v_2$ values are exactly 1 for all $y \geq 0$.

---

### Theorem B (Exact Stay Formula)

For $x = 8y + 7$, define $D(y) = \lfloor v_2(y+1)/2 \rfloor$. The number of consecutive returns to rail 7 under $f_2$ is exactly $D(y)$.

After $d$ stays ($0 \leq d \leq D(y)$), the value is:

$$y_d = \frac{9^d(y+1) - 4^d}{4^d} = \left(\frac{9}{4}\right)^d (y+1) - 1$$

**Proof.** By induction on $d$. The map $g(y) = (9y+5)/4$ (derived from $f_2(8y+7) = 18y+17 = 8y'+7$ giving $y' = (18y+10)/8 = (9y+5)/4$) satisfies:

$$y_{d+1} = \frac{9 \cdot \frac{9^d(y+1)-4^d}{4^d} + 5}{4} = \frac{9^{d+1}(y+1) - 9\cdot 4^d + 5\cdot 4^d}{4^{d+1}} = \frac{9^{d+1}(y+1) - 4^{d+1}}{4^{d+1}}$$

The stay condition $y_d \equiv 3 \pmod{4}$ is equivalent to $v_2(y+1) \geq 2(d+1)$. ∎

---

### Theorem C (Mersenne Escape Rail Alternation)

For the family $y_0 = 2^k - 1$ with $k \geq 2$:

- **If $k = 2d$ (even):** Escape to rail 1 with $x_{\text{escape}} = 18 \cdot 9^d - 1$
- **If $k = 2d+1$ (odd):** Escape to rail 3 with $x_{\text{escape}} = 36 \cdot 9^d - 1$

**Proof.** Substitute $y_0 + 1 = 2^k$ into Theorem B:
- For $k = 2d$: $y_d = 9^d - 1$, so $x_{\text{escape}} = 18(9^d-1) + 17 = 18\cdot 9^d - 1 \equiv 1 \pmod{8}$.
- For $k = 2d+1$: $y_d = 2\cdot 9^d - 1$, so $x_{\text{escape}} = 18(2\cdot 9^d-1) + 17 = 36\cdot 9^d - 1 \equiv 3 \pmod{8}$. ∎

---

### Theorem D (Rail-1 Descent for Even-k Mersenne Family)

For $k = 2d$ (even), after escaping to rail 1:

$$f(x_{\text{escape}}) = \frac{27 \cdot 9^d - 1}{2}$$

The descent ratio satisfies:

$$\frac{f(x_{\text{escape}})}{x_{\text{escape}}} = \frac{27 \cdot 9^d - 1}{36 \cdot 9^d - 2} \longrightarrow \frac{3}{4} \quad \text{as } d \to \infty$$

**Proof.** $x_{\text{escape}} = 18\cdot 9^d - 1 = 8y' + 1$ where $y' = (9^{d+1}-1)/4$. By Lemma 1 of Mod8_Rail_Descent.md, $f(8y'+1) = 6y'+1 = (27\cdot 9^d - 1)/2$. ∎

---

### Theorem E (Rail-3 Bridge Structure for Odd-k Mersenne Family)

For $k = 2d+1$ (odd), the exact bridge value is:

$$B_d = \frac{9^{d+2} - 1}{2}$$

The 2-adic valuation satisfies:
- If $d$ is odd: $v_2(B_d) = 2$
- If $d$ is even: $v_2(B_d) = 2 + v_2(d+2)$

**Proof.** The bridge formula follows from substituting $y' = (9^{d+1}-1)/2$ into $9y'+4$. For the valuation, apply LTE (Lifting The Exponent Lemma):

$$v_2(9^{d+2} - 1) = \begin{cases} 3 & \text{if } d+2 \text{ odd} \\ 3 + v_2(d+2) & \text{if } d+2 \text{ even} \end{cases}$$

Since $B_d = (9^{d+2}-1)/2$, subtract 1 from both cases. ∎

---

### Theorem F (Post-Bridge Entry Value for Odd-k Mersenne Family)

For $k = 2d+1$ (odd), after dividing $B_d$ by $2^{v_2(B_d)}$, the resulting odd entry value $E_d$ satisfies:

$$E_d = \frac{9^{d+2} - 1}{2^{v_2(B_d)+1}}$$

This is an exact normalization formula for the odd entry after the fixed rail-3 bridge. It does not, by itself, prove descent.

**Observation F1 (empirical).** For all tested $d \leq 19$, the first true odd-step from $E_d$ lands on rail 5 when $E_d \equiv 3 \pmod{8}$ with even $y$-coordinate, or on rail 1 when $E_d \equiv 3 \pmod{8}$ with odd $y$-coordinate.

---

## 4. Empirical Conjectures

### Conjecture G (Mersenne Epoch Bound)

For $x_0 = 2^{k+3} - 1$ (Mersenne numbers in rail 7), define the **epoch** as odd-steps until first value $< x_0$. Then:

$$\text{epoch}(x_0) \leq C \cdot k$$

for some absolute constant $C$ (empirically $C \approx 4-5$).

**Evidence:** Verified for all $k \leq 20$ ($x_0 \leq 2^{23}-1$). No counterexamples.

### Conjecture H (General Rail-7 Descent)

For **all** $x = 8y + 7$, the epoch is finite. Equivalently, no $y$ sustains rail-7 growth indefinitely.

**Status:** Equivalent to Collatz conjecture restricted to rail 7. The finite-escape result (Lemma 5) proves rail 7 is not a trap; the open question is whether post-escape descent always compensates for growth.

---

## 5. Why These Results Matter

1. **Closed form vs. inductive:** Theorems A-B replace the inductive description in the original repo with exact formulas, enabling precise asymptotic analysis.

2. **Mersenne rail-7 escape is fully characterized:** Theorems C-F give algebraic control over the escape phase and the first post-bridge normalization of this "worst case" family.

3. **Connection to LTE:** Theorem E connects Collatz dynamics to classical number theory via the Lifting The Exponent Lemma.

4. **Path to proof:** Proving Conjecture G would settle the Mersenne subfamily's descent epoch. A proof for all rail-7 numbers would still require Conjecture H, or a stronger residue/merge certificate covering every post-escape branch.

---

## 6. References

- docbgm2002/collatz-things: `Mod8_Rail_Descent.md`, `Block_Fracture_Lemma.md`; legacy summary `archive/Triple_Lock_Revised.md`
- Terence Tao, "Almost all orbits of the Collatz map attain almost bounded values" (2019)
- Hamed M. Pour, "Elementary Exponential Density Bounds for Collatz" (2025)
