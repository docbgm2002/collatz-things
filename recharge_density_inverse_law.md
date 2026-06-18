# ⭐ **THE RECHARGE–DENSITY INVERSE LAW**

> **Status: exploratory / retired from the proved-results track.**
> This note incorrectly identifies \(3k+1\) with the next odd iterate when
> additional factors of \(2\) may remain. Its probability and global-growth
> conclusions must not be cited as theorems. See `recharge_nogo.md`.

### *Why Collatz Trajectories Cannot Explode*

**Author:** Dr. Bry  
**Date:** 28 November 2025  
**Context:** Part of the “Collatz” Framework

---

## 1. Introduction

In the “Fuse–Chaos” model of the Collatz map, every odd integer is decomposed into two regions:

* a **fuse**: its trailing block of 1s
* a **chaos seed**: the upper bits that determine long-term behaviour

Two fundamental facts govern their evolution:

1. **Fuse Burn:**
   If an odd number has fuse length (f > 1), then the next odd number in its trajectory has fuse length (f-1).

2. **Fuse Recharge:**
   The fuse can only increase when (f = 1), and only if the number satisfies a strict modular congruence that aligns the bits so that (3n+1) produces a longer trailing block of ones.

This document proves the **Recharge–Density Inverse Law**, which states:

> **High-density numbers always lose density, and numbers that gain density must be low-density to begin with.
> No integer can maintain both high density and persistent growth.**

This creates a *self-limiting dynamical cycle*:
the fuse can grow only from low density, but growing the fuse produces a high-density state that is then forced to decay.

---

## 2. Preliminaries: Fuse Burn

Let an odd integer (n) have fuse length (f(n)), i.e. it ends in (f(n)) consecutive 1s.

Under the odd step,

```math
T(n) = 3n + 1,
```

the following holds:

**Fuse Burn Lemma.**
If (f(n) > 1), then

```math
f(T(n) / 2^v) = f(n) - 1,
```

where (v) is the number of trailing zeros in (3n+1).

This is a purely structural consequence of binary addition:
the low bits of (3n+1) always end with exactly one 0 followed by the (shifted) previous fuse.

Thus **every large fuse must decay linearly**:

```
f → f-1 → f-2 → ... → 1.
```

There is no mechanism for direct high-density growth.

---

## 3. The Mersenne Decay Theorem

*(High-Density Inputs Cannot Grow)*

### **Theorem 3.1 — Mersenne Fuse Decay**

Let

```math
n = 2^k - 1,
```

a pure block of (k) ones (a perfect high-density integer).
Let (n') be the next odd integer in its trajectory:

```math
n' = (3n + 1) / 2^v .
```

Then:

```math
f(n') = k - 1.
```

### **Proof**

Compute:

```math
3n + 1 = 3(2^k - 1) + 1 = 3 \cdot 2^k - 2.
```

In binary, (3\cdot 2^k) is:

```
11 followed by k zeros
```

Subtracting 2 yields a number ending in:

```
...1110
```

so the intermediate fuse has length (k-1).
Division by 2 removes the trailing 0, producing:

```
...111
```

a block of exactly (k-1) ones.

Thus:

```math
f(n') = k - 1.
```

High-density (large (k)) **forces** density loss.

---

## 4. The Recharge Constraint

*(Fuse Growth Requires Low Density)*

Fuse growth only occurs when the current fuse has length (1).
Write:

```math
n = 4k + 1,
```

i.e. binary ending in `01`.

Under the odd step:

```math
3n + 1 = 12k + 4 = 4(3k + 1),
```

so dividing by 4 gives the next odd number:

```math
n_{\text{next}} = 3k + 1.
```

To obtain a fuse of length (L), we require:

```math
n_{\text{next}} = m \cdot 2^{L+1} + (2^L - 1).
```

Thus:

```math
3k + 1 \equiv 2^L - 1 \pmod{2^{L+1}}.
```

Rewriting:

```math
3k \equiv 2^L - 2 \pmod{2^{L+1}}.
```

or equivalently:

```math
n \equiv \frac{2^{L+1} - 2}{3} \pmod{2^{L+1}}.
```

This congruence has **exactly one solution mod (2^{L+1})**.
Therefore:

> Producing a fuse of length (L) requires hitting a 1-in-(2^{L+1}) modular window.

This is a **probability of order (2^{-L})**.

---

## 5. The Recharge–Density Inverse Law

*(Fuse Growth Requires Low Density, but Fuse Growth Creates High Density)*

We now state the central result.

### **Theorem 5.1 — Recharge–Density Inverse Law**

For any odd integer in a Collatz trajectory:

1. **If it is high density (large fuse), its fuse must decrease.**
2. **If its fuse increases, the integer must have been low density to begin with.**
3. **Larger fuse increases require exponentially rarer modular alignments.**

### **Proof**

1. From the Mersenne Decay Theorem and Fuse Burn Lemma:
   large fuse (f) deterministically maps to (f-1).
   High density ⇒ forced decay.

2. From the recharge congruence:
   fuse growth (1 \to L) requires
   (n \equiv (2^{L+1}-2)/3 \mod 2^{L+1}).
   This window has measure (2^{-L}).
   Thus growth ⇒ low-density input + rare alignment.

3. Combining both:
   growing fuse produces high density,
   high density forces fuse burn,
   fuse burn returns the system to (f=1),
   where a recharge attempt can occur again.

The system therefore alternates:

```
Low density (f=1) --[rare recharge]--> High density (f=L)
High density (f=L) --[deterministic burn]--> f=1
```

Fuse growth is rare and unstable; fuse decay is universal and stable.

---

## 6. The Recharge Funnel

*(A One-Way Flow Toward Low Density)*

Putting all components together:

1. **Recharge events (1 → L)** are exponentially rare.
2. **Burn events (L → 1)** are guaranteed and linear.
3. **Any high-density state immediately enters a decay chain.**
4. **Every trajectory spends most of its life in low-density states.**

Visually:

```
           L (very high density)
            ▲   rare: ~ 2^-L
            │
            │
        f = 1  (low density)
            │
            ▼
      deterministic burn
        L → L-1 → ... → 1
```

This is the **Recharge Funnel**:
a dynamical trap preventing long-term growth of binary density.

---

## 7. Conclusion

The Collatz map cannot sustain high-density configurations.

* Every large fuse collapses.
* Fuse growth requires low density.
* Large fuse growth is exponentially rare.
* Fuse decay is certain.

Thus:

> **The Collatz system cannot achieve explosive growth.
> High-density ascent is self-defeating, and long-term behaviour is forced toward lower density.**

This does **not** prove the Collatz conjecture,
but it describes a strong structural instability that constrains the dynamics and supports global downward drift.

---
