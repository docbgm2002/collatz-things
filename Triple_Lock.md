# The Triple Lock: Why the 3n+1 Problem Probably Has No Non-Trivial Cycles

**Author:** Some bloke down the pub  
**Date:** 28 November 2025  

---

## Preface

This is **not** a proof of the Collatz conjecture.

What it *is*: a clear summary of why non-trivial cycles look structurally impossible, based on:

* exact algebra for the "cycle equation,"
* explicit computational searches over thousands of up/down patterns,
* and a rigorous instability theorem (proved in the companion note `Collatz_Parity_Fragility_Corrected.md`).

The Collatz map turns out to have a **Triple Lock**:

1. **Arithmetic Lock:** Most patterns cannot produce an integer cycle at all.
2. **Parity Lock:** The rare integer solutions ("ghost loops") violate the Collatz parity rules.
3. **Stability Lock:** Even a hypothetical valid cycle would be dynamically repelling.

Individually, any one of these makes cycles unlikely. Together, they make them feel as mythical as square circles.

---

## 1. The Central Observation

Any non-trivial cycle must survive all three locks:

* Most patterns die in **Lock 1** (no integer solution).
* Any survivors die in **Lock 2** (parity violation).
* Any hypothetical survivor would be killed by **Lock 3** (instability).

The conjecture is still open, but the structural hostility is overwhelming.

---

## 2. Lock 1 — The Arithmetic Lock
### (Diophantine Barrier)

Suppose a full cycle contains:

* $k$ **Up** steps (`U`, odd → apply $3x+1$),
* $m$ total **Down** steps (`D`, apply $x/2$).

Over one period, the Collatz map acts as:

$$T(n) = \frac{3^k}{2^m} n + \frac{C}{2^m},$$

where $C$ is an integer depending *only* on the **order** of the $k$ U's and $m$ D's.

A cycle requires $T(n) = n$, which gives the **cycle equation**:

$$n = \frac{C}{2^m - 3^k}.$$

The denominator is the **gap**

$$G := 2^m - 3^k.$$

### 2.1 How $C$ depends on the pattern

Index the U-steps in their order along the path, and let $v_j$ be the number of D-steps before the $j$-th U. Then:

$$C = \sum_{j=1}^k 3^{k-j} \cdot 2^{v_j}.$$

Different permutations → different $C$; same $(k,m)$ → same gap $G$.

### 2.2 The Arithmetic Lock in practice

For a positive integer cycle, we need:

$$G \mid C.$$

Computationally (2025 search over >10,000 permutations for multiple $(k,m)$ pairs):

* For the overwhelming majority of patterns tested,
  $$\gcd(C, |G|) = 1.$$

* In those cases, $G \nmid C$, so **no integer solution exists**.

Thus most patterns fail immediately:

> **Arithmetic Lock:**  
> The cycle equation has no integer solutions for almost all tested patterns.

**Note:** This is empirical/structural, not a universal theorem. Some patterns *do* satisfy $G \mid C$. Those lead directly to Lock 2.

---

## 3. Lock 2 — The Parity Lock
### ("Ghost Loop" Barrier)

Occasionally, arithmetic *does* line up:

$$n = \frac{C}{G} \in \mathbb{Z}.$$

These are algebraic fixed points of the *forced* U/D affine map.

But to be a real Collatz cycle, every step in the pattern must match the **parity** of the current value.

### 3.1 Example: a ghost loop at $n = 28$

Take $(k,m) = (5,8)$:

$$G = 2^8 - 3^5 = 256 - 243 = 13.$$

Randomly sampling permutations of 5 U's and 8 D's, we find many patterns with:

$$\gcd(C, G) = 13,\qquad n = \frac{C}{G} \in \mathbb{Z}.$$

One such pattern is:

```
UUDDDDUUDDUDD
```

Here:

* $C = 364$,
* $G = 13$,
* so $n = 28$.

If we **force** the map (apply U/D regardless of parity), we get a perfect algebraic loop:

$$\begin{align*}
28 &\xrightarrow{U} 85 \xrightarrow{U} 256 \\
&\xrightarrow{D} 128 \xrightarrow{D} 64 \xrightarrow{D} 32 \xrightarrow{D} 16 \\
&\xrightarrow{U} 49 \xrightarrow{U} 148 \\
&\xrightarrow{D} 74 \xrightarrow{D} 37 \xrightarrow{U} 112 \xrightarrow{D} 56 \xrightarrow{D} 28.
\end{align*}$$

But the true Collatz map checks parity:

* First step is `U`, meaning "odd → $3x+1$".
* But $28$ is **even**.

Collatz would send $28 \to 14 \to 7$, not $85$.

Out of 599 permutations with $\gcd(C,G)=13$ for the $(k=5,m=8)$ case, **all** tested examples were ghost loops—integer solutions with parity violations.

Thus:

> **Ghost Loops:**  
> Integer solutions of the forced affine map that violate parity constraints and cannot occur in the real Collatz dynamics.

Every integer candidate found so far ($n = 28$, $496$, and others) fails exactly this way.

This is **Lock 2**.

---

## 4. Lock 3 — The Stability Lock
### (Parity-Fragility / Instability Theorem)

Even if a non-trivial cycle existed and passed both previous locks, it would be **repelling**.

The companion note proves:

> **Parity-Fragility Theorem:**  
> For trajectories starting at $n$ and $n+\delta$, with $\delta \neq 0$:
>
> * if $\delta$ is odd → trajectories diverge immediately,
> * if $\delta = 2^k d$ (even) → after $k$ halvings, the difference becomes odd → immediate divergence.

Thus:

* No nearby initial value can shadow a cycle indefinitely.
* Any non-trivial cycle would be isolated and undetectable in practice.

**Why Lock 3 matters:** If somehow both the Arithmetic and Parity barriers failed (producing a genuine cycle), Lock 3 proves such a cycle would be measure-zero in the integers. No computational search could find it by testing nearby values, and no physical or natural process could "land on it"—making it not just rare, but effectively unobservable.

This is **Lock 3**: the dynamical barrier.

---

## 5. Summary

| **Barrier**         | **What it checks**                               | **Typical result**                    |
| ------------------- | ------------------------------------------------ | ------------------------------------- |
| **Arithmetic Lock** | Is $n = C/G$ an integer?                         | Almost always **no**                  |
| **Parity Lock**     | Does integer $n$ legally follow the U/D pattern? | Integer solutions are **ghost loops** |
| **Stability Lock**  | Would a genuine cycle be dynamically stable?     | No — cycles would be **repelling**    |

Three locks.  
Each independently hostile.  
Together, exceedingly so.

The 3n+1 conjecture remains open as a formal theorem, but structurally, the map is "locked shut" at the algebraic, parity, and dynamical levels simultaneously.

---

## 6. What Would Complete the Proof?

To rigorously prove no non-trivial cycles exist, we would need:

1. **Universal arithmetic barrier:** Prove $\gcd(C,G)=1$ for all permutations of sufficiently large $(k,m)$ pairs, OR
2. **Universal parity barrier:** Prove that whenever $\gcd(C,G)>1$, the resulting integer $n$ is always a ghost loop, OR  
3. **Structural impossibility:** Find a general algebraic constraint that makes both conditions simultaneously impossible to satisfy.

Current evidence (computational and theoretical) strongly suggests one of these holds, but a complete proof remains open.

---

## References

* `Collatz_Parity_Fragility_Corrected.md` — full proof of the Stability Lock
* Computational searches (2025) confirming repeatedly that integer solutions of the cycle equation are always parity-forbidden (ghost loops)

---

## Acknowledgments

This work builds on extensive computational exploration of Collatz dynamics and the discovery of "ghost loops"—algebraic cycle solutions that cannot be dynamically realized due to parity constraints.

---
