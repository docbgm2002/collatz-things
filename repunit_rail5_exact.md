# Exact Rail-5 Frequency Results for Base-3 Repunit Trajectories

**Building on:** `mersenne_repunit_reduction.md`, `Mod8_Rail_Descent.md`, `collatz_rail7_new_results.md`
**Author:** Dr. Bry (AI-assisted analysis)
**Date:** 2026-06-20
**Status:** Theorems R5.1–R5.6 are proved exactly. The density statement in R5.6 is a proved limiting density; the associated finite-range count is reported as observed, not asserted as a strict inequality. Theorem R5.7 (universal 12-step bound) is **empirical**, tested exhaustively to $n = 199$.
**License:** CC-BY 4.0

---

## 1. Introduction

The Mersenne–repunit reduction (`mersenne_repunit_reduction.md`) shows that the epoch of $2^n-1$ reduces to the first-passage time $\sigma(a_n)$ of the base-3 repunit $a_n = (3^n-1)/2$. This note establishes **exact structural theorems** on the rail-class (mod-8 residue) of $a_n$ and its immediate descendants, proving that rail 5 — the strongest-descent rail — is hit with **deterministic positive density** in the first two odd-steps. We also report an empirical universal bound (tested to $n = 199$) that all non-trivial repunit trajectories hit rail 5 within $\le 12$ odd-steps.

We are explicit throughout about the boundary between exact theorem and finite computation. The frequency statements proved here are *density* statements over the family of repunit indices; they are not, and do not claim to be, a bound on every trajectory.

---

## 2. Notation

For odd $x$, the odd-step map is $f(x) = (3x+1)/2^{v_2(3x+1)}$, where $v_2(\cdot)$ is the 2-adic valuation.

The **base-3 repunit** is $a_n = (3^n-1)/2 = \sum_{i=0}^{n-1} 3^i$.

The **base-9 repunit** is $b_m = (9^m-1)/8 = \sum_{i=0}^{m-1} 9^i$.

Rails are residue classes mod 8: $8y+1$ (rail 1), $8y+3$ (rail 3), $8y+5$ (rail 5), $8y+7$ (rail 7).

From `Mod8_Rail_Descent.md`:
- Rail 1: $f(8y+1) = 6y+1$ (strict descent for $y \ge 1$)
- Rail 3: bridge $8y+3 \mapsto 9y+4$; the genuine odd-step is $f(8y+3) = 12y+5$ followed by $f(12y+5) = 9y+4$ if $y$ odd, or a deeper drop if $y$ even
- Rail 5: $f(8y+5) \le 3y+2 < 8y+5$ (strict descent)
- Rail 7: finite escape with exact formulas from `collatz_rail7_new_results.md`

We use the **Lifting-the-Exponent (LTE) lemma** for $p=2$: for odd $a,b$ with $4 \mid (a-b)$,
$$v_2(a^k - b^k) = v_2(a-b) + v_2(k).$$
We also use the elementary fact that $v_2(3^k - 1) = v_2(3-1) + v_2(3+1) + v_2(k) - 1 = 2 + v_2(k)$ for even $k$, and $v_2(3^k-1)=1$ for odd $k$.

---

## 3. Exact theorems

### Theorem R5.1 (Repunit rail classification)

For odd $n$:
- If $n \equiv 1 \pmod 4$: $a_n \equiv 1 \pmod 8$ (rail 1).
- If $n \equiv 3 \pmod 4$: $a_n \equiv 5 \pmod 8$ (rail 5).

**Proof.** For odd $n$, $3^n \bmod 16$ has period 4 on the odd residues: $3^1 \equiv 3$, $3^3 \equiv 11$, $3^5 \equiv 3$, $3^7 \equiv 11 \pmod{16}$.
- If $n \equiv 1 \pmod 4$: $3^n \equiv 3 \pmod{16}$, so $a_n = (3^n-1)/2 \equiv 1 \pmod 8$.
- If $n \equiv 3 \pmod 4$: $3^n \equiv 11 \pmod{16}$, so $a_n = (3^n-1)/2 \equiv 5 \pmod 8$. $\blacksquare$

**Corollary.** Exactly half of repunit indices (those with $n \equiv 3 \pmod 4$) start on rail 5.

---

### Theorem R5.2 (First odd-step from repunit)

For odd $n$,
$$f(a_n) = \frac{a_{n+1}}{2^{\,2+v_2((n+1)/2)}}.$$

**Proof.** Since $3a_n + 1 = a_{n+1}$, we have $f(a_n) = a_{n+1}/2^{v_2(a_{n+1})}$. Now $a_{n+1} = (3^{n+1}-1)/2$, so $v_2(a_{n+1}) = v_2(3^{n+1}-1) - 1$. As $n$ is odd, $n+1$ is even, and by LTE for $p=2$,
$$v_2(3^{n+1}-1) = 2 + v_2(n+1) = 2 + 1 + v_2((n+1)/2) = 3 + v_2((n+1)/2),$$
using $v_2(n+1) = 1 + v_2((n+1)/2)$. Hence $v_2(a_{n+1}) = 2 + v_2((n+1)/2)$. $\blacksquare$

---

### Theorem R5.3 (Base-9 repunit structure for $n \equiv 1 \pmod 4$)

For $n \equiv 1 \pmod 4$, let $m = (n+1)/2$ (note $m$ is odd). Then
$$f(a_n) = b_m = \frac{9^m-1}{8}.$$
Moreover, $b_m \equiv m \pmod 8$.

**Proof.** When $n \equiv 1 \pmod 4$, $(n+1)/2 = m$ is odd, so $v_2((n+1)/2) = 0$ and Theorem R5.2 gives $f(a_n) = a_{n+1}/4 = (3^{n+1}-1)/8 = (9^{m}-1)/8 = b_m$.

For the congruence, write $9^m = (1+8)^m = \sum_{j\ge 0}\binom{m}{j}8^j = 1 + 8m + 64\binom{m}{2} + \cdots$. Therefore
$$b_m = \frac{9^m-1}{8} = m + 8\binom{m}{2} + 8^2\binom{m}{3}+\cdots \equiv m \pmod 8. \qquad \blacksquare$$

---

### Theorem R5.4 (v₂ pattern for the base-9 repunit, refined mod 16)

For odd $m$, the value $v_2(3b_m + 1)$ depends only on $m \bmod 16$:

| $m \bmod 16$ | $v_2(3b_m+1)$ |
|---|---|
| 1, 9 | $2$ |
| 3, 7, 11, 15 | $1$ |
| 13 | $3$ |
| 5 | $\ge 4$ |

In particular, for $m \equiv 5 \pmod 8$ we have $v_2(3b_m+1) \ge 3$, with the threshold $v_2 \ge 4$ achieved exactly when $m \equiv 5 \pmod{16}$ and $v_2 = 3$ exactly when $m \equiv 13 \pmod{16}$.

**Proof.** Since $8b_m = 9^m - 1$, we have $8(3b_m+1) = 3\cdot 9^m + 5$, i.e.
$$3b_m + 1 = \frac{3\cdot 9^m + 5}{8}.$$
Write $N_m := 3\cdot 9^m + 5$. Then $v_2(3b_m+1) = v_2(N_m) - 3$, provided $v_2(N_m)\ge 3$ (which we now show).

Compute $N_m \bmod$ powers of 2 using $9 \equiv 1 \pmod 8$. From the binomial expansion $9^m = 1 + 8m + 64\binom{m}{2} + \cdots$,
$$N_m = 3\cdot 9^m + 5 = 8 + 24m + 192\binom{m}{2} + \cdots = 8\big(1 + 3m + 24\binom{m}{2} + \cdots\big).$$
So $v_2(N_m) = 3 + v_2(1 + 3m + 24\binom{m}{2} + \cdots)$. Reducing the bracketed factor modulo small powers of 2:
- $1 + 3m \equiv 0 \pmod 2 \iff m$ odd (always true here); modulo 4, $1+3m \equiv 1+3m$, and $24\binom{m}{2}\equiv 0\pmod 4$, so the bracket $\equiv 1+3m \pmod 4$.
  - $m \equiv 1 \pmod 4 \Rightarrow 1+3m \equiv 0 \pmod 4$, raising $v_2(N_m)$ by at least 2.
  - $m \equiv 3 \pmod 4 \Rightarrow 1+3m \equiv 2 \pmod 4$, so $v_2(\text{bracket}) = 1$ and $v_2(N_m)=4$, giving $v_2(3b_m+1)=1$. This covers $m\equiv 3,7,11,15 \pmod{16}$, all with value $1$.

For the complete refinement, work modulo $128$. Since
$9^{16}\equiv1\pmod{128}$, the residue of $N_m$ modulo $128$ depends only on
$m\bmod16$. Direct evaluation on the eight odd classes gives

| $m\bmod16$ | $N_m=3\cdot9^m+5\bmod128$ | consequence |
|---|---|---|
| 1, 9 | $32,96$ | $v_2(N_m)=5$ |
| 3, 7, 11, 15 | $16,112,80,48$ | $v_2(N_m)=4$ |
| 13 | $64$ | $v_2(N_m)=6$ |
| 5 | $0$ | $v_2(N_m)\ge7$ |

Subtracting $3$ from these valuations proves the stated table for
$v_2(3b_m+1)$. $\blacksquare$

**Note (correction history).** An earlier draft claimed $v_2 \ge 4$ for *all* $m \equiv 5 \pmod 8$. This is **false**: the sub-class $m \equiv 13 \pmod{16}$ gives exactly $v_2 = 3$ (first witnessed at $m=13$). The corrected statement is $v_2 \ge 3$ on $m\equiv5\pmod8$, refined as above mod 16. The rail-5 *hit* results (R5.5–R5.7) are unaffected, because they depend only on which rail $b_m$ lands on (Theorem R5.3), not on the descent depth.

---

### Theorem R5.5 (First-step rail pattern for $n \equiv 1 \pmod 4$)

For $n \equiv 1 \pmod 4$, the first odd-step from $a_n$ lands on the rail determined by $n \bmod 16$:

| $n \bmod 16$ | $m \bmod 8$ | rail of $f(a_n)$ |
|---|---|---|
| 1 | 1 | 1 |
| 5 | 3 | 3 |
| **9** | **5** | **5** |
| 13 | 7 | 7 |

**Proof.** By Theorem R5.3, $f(a_n)=b_m$ with $m=(n+1)/2$, and $b_m \equiv m \pmod 8$. As $n$ ranges over $\{1,5,9,13\}\pmod{16}$, $m=(n+1)/2$ ranges over $\{1,3,5,7\}\pmod 8$, giving rails $\{1,3,5,7\}$ respectively. The $n\equiv 9 \pmod{16}$ row gives rail 5. $\blacksquare$

---

### Theorem R5.6 (Rail-5 density on the repunit family)

Among odd indices $n$, the natural density of those whose repunit $a_n$ reaches rail 5 on step 0 or step 1 is exactly
$$\tfrac12 + \tfrac18 = \tfrac58.$$

**Proof.** Two disjoint contributions:
1. $n \equiv 3 \pmod 4$ — density $\tfrac12$ of odd $n$ — start **on** rail 5 (Theorem R5.1).
2. $n \equiv 9 \pmod{16}$ — density $\tfrac18$ of odd $n$ — hit rail 5 on the first odd-step (Theorem R5.5).

The classes $n\equiv 3 \pmod 4$ and $n \equiv 9 \pmod{16}$ are disjoint ($9 \equiv 1 \pmod 4$), so the densities add: $\tfrac12 + \tfrac18 = \tfrac58$. $\blacksquare$

**Remark (finite ranges).** This is a *limiting* density, and it is approached from below on finite initial segments. Over $n \in [1,199]$ the observed fraction is $62/100 = 0.62$; over $n \in [1, 4000)$ it equals $0.62500$ to within rounding. Any finite-range verification should test the limiting value on a sufficiently large range, or assert the weaker observed bound $\ge 0.62$ on short ranges — not a strict $\ge \tfrac58$ on $[1,199]$, which **fails** by $0.005$.

---

## 4. Empirical result (strong, not proved)

### Observation R5.7 (Universal rail-5 hit — empirical)

For every repunit $a_n = (3^n-1)/2$ with odd $n$ in the range $3 \le n \le 199$, the trajectory hits rail 5 within at most **12 odd-steps**.

**Statistics (over odd $3\le n\le 199$):**
- Median steps to rail 5: **0** (half start on rail 5)
- Mean steps: **≈ 2.0**
- Maximum: **12** (achieved at $n = 17$ and $n = 61$)
- Fraction hitting rail 5 within 5 steps: **85/99 ≈ 85.9%**

**Status.** This is a finite computational observation, not a theorem. It is stated as an Observation rather than a Theorem precisely because no proof is offered.

**Why no proof follows from the structure above.** The proved results (R5.1–R5.6) control step 0 and step 1 for specific residue classes of $n$. They do **not** control the indices outside those classes (e.g. $n \equiv 5 \pmod{16}$, whose first step lands on rail 3, and $n\equiv 13\pmod{16}$, landing on rail 7). For those, rail 5 is reached only after a further sequence of odd-steps whose rail transitions are governed by 2-adic valuations of the *intermediate* iterates — not by any modular condition on $n$ alone. A heuristic "each rail-3 pass has a 50% chance of dropping to rail 5" describes the *frequency* of outcomes across the family but is not a deterministic argument for any individual trajectory, and is not used in any proof here. Closing this is discussed in §6.

---

## 5. Implications for the Mersenne epoch

**Corollary (Mersenne post-burn structure).** For $x_0 = 2^n - 1$ with odd $n$:
1. **Burn:** exactly $n$ odd-steps to $a_n = (3^n-1)/2$ (exact, from `mersenne_repunit_reduction.md`).
2. **To rail 5:** $a_n$ reaches rail 5 within $\le 1$ odd-step for a density-$\tfrac58$ set of indices (proved), and within $\le 12$ odd-steps for all tested $n \le 199$ (empirical).
3. **Rail-5 descent:** strict, with one-step ratio $\le 3y+2$ over $8y+5$, i.e. asymptotic ratio $\le \tfrac38$.

Structural decomposition:
$$\operatorname{epoch}(2^n-1) = \underbrace{n}_{\text{burn}} + \underbrace{\tau_n}_{\text{to rail 5}} + \underbrace{\sigma'_{\text{post-rail-5}}}_{\text{descent}},$$
where $\tau_n \le 1$ for a density-$\tfrac58$ set of indices (proved), and $\tau_n \le 12$ for all tested $n \le 199$ (empirical).

---

## 6. Honest assessment of the gap

The remaining obstacle to a Mersenne epoch bound $\sigma(a_n) = O(n)$ is:

> **Can the valuation conditions at successive rail-3 (and rail-7-escape) hits conspire to avoid rail 5 for arbitrarily many steps?**

Avoiding rail 5 indefinitely would require an infinite coordinated sequence of 2-adic valuation conditions on the intermediate iterates. Proving this cannot happen requires controlling the **joint behaviour** of infinitely many 2-adic digits along a trajectory. This is the standard wall:
- **Modular / automatic reasoning** (finite-state, Presburger-style) controls each step's rail but cannot bound the length of an arbitrary rail-avoiding run.
- **Full integer arithmetic** suffices in principle but is, for this question, of the same difficulty as the Collatz conjecture restricted to the Mersenne family.

The density-$\tfrac58$ statement (R5.6) is the strongest **provable** frequency result here. The 12-step universal bound (R5.7) is the strongest **empirical** one. The gap between them is genuine and is not closed by anything in this note.

---

## 7. Verification

The standalone verifier `verify_repunit_rail5.py` checks R5.1–R5.6 over
large finite ranges, verifies the complete modulo-$128$ table used in the
proof of R5.4, and reproduces the bounded observation R5.7 for odd
$3\le n\le199$.

```bash
python verify_repunit_rail5.py
```

The following is the core verification logic:

```python
# ============================================================
# Verification suite for the theorems above.
# Every assert must pass. Prints OK on success.
# ============================================================

def repunit(n):
    return (3**n - 1) // 2

def v2(n):
    return (n & -n).bit_length() - 1

def f(x):
    val = 3 * x + 1
    return val // (2 ** v2(val))

# ---- R5.1: repunit rail classification ----
for n in range(1, 2000, 2):
    a = repunit(n)
    assert a % 8 == (1 if n % 4 == 1 else 5)

# ---- R5.2 / R5.3: f(a_n) = b_m for n = 1 mod 4; b_m = m mod 8 ----
for n in range(1, 2000, 4):
    a = repunit(n)
    m = (n + 1) // 2
    b = (9**m - 1) // 8
    assert f(a) == b
    assert b % 8 == m % 8          # m is odd here

# ---- R5.4: v2(3 b_m + 1), refined mod 16 ----
expected = {1: 2, 9: 2, 3: 1, 7: 1, 11: 1, 15: 1, 13: 3}
for m in range(1, 4000, 2):
    b = (9**m - 1) // 8
    val = v2(3 * b + 1)
    r = m % 16
    if r == 5:
        assert val >= 4
    else:
        assert val == expected[r]
# coarse statement on m = 5 mod 8:
for m in range(5, 4000, 8):
    b = (9**m - 1) // 8
    assert v2(3 * b + 1) >= 3

# ---- R5.5: first-step rail for n = 1 mod 4 ----
firststep_rail = {1: 1, 5: 3, 9: 5, 13: 7}
for n in range(1, 4000, 4):
    a = repunit(n)
    assert f(a) % 8 == firststep_rail[n % 16]

# ---- R5.6: density = 5/8 (NOT a strict bound on short ranges) ----
def hit_fraction(hi):
    c = t = 0
    for n in range(1, hi, 2):
        t += 1
        a = repunit(n)
        if a % 8 == 5 or n % 16 == 9:
            c += 1
    return c / t

assert hit_fraction(200) >= 0.62              # honest short-range bound
assert abs(hit_fraction(4000) - 5/8) < 1e-9   # limiting density is exactly 5/8

# ---- R5.7: empirical universal 12-step bound, odd 3 <= n <= 199 ----
worst = 0
for n in range(3, 200, 2):
    x = repunit(n)
    steps = 0
    while x % 8 != 5:
        x = f(x)
        steps += 1
        assert steps <= 100
    assert steps <= 12
    worst = max(worst, steps)
assert worst == 12

print("ALL CHECKS PASS (worst rail-5 hit =", worst, "steps)")
```

---

## 8. Relation to other repo files

- `mersenne_repunit_reduction.md`: This note strengthens the post-burn analysis by classifying the landing rail of $a_n$ exactly and giving the base-9 repunit structure for $n \equiv 1 \pmod 4$.
- `Mod8_Rail_Descent.md`: Uses Lemmas 1–3 as building blocks.
- `recharge_nogo.md`: The rail-5 density result is compatible with the no-go theorem — it constructs no global potential, only a local/density structural bound.
- `collatz_rail7_new_results.md`: The closed-form rail-7 analysis applies to the $n \equiv 13 \pmod{16}$ first-step escape case.
- `stopping_time_density.md`: The $\tfrac58$ density is specific to this family and does not extend to "almost all" integers.

---

## References

- `mersenne_repunit_reduction.md` — exact reduction to repunit first-passage
- `Mod8_Rail_Descent.md` — rail classification and descent lemmas
- `collatz_rail7_new_results.md` — closed-form rail-7 analysis
- `recharge_nogo.md` — no-go for tau-based potentials
- `stopping_time_density.md` — Terras/Everett rederivation
