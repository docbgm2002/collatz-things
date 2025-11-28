# The Algebraic Fracture Lemma: Structural Instability of High-Density Blocks

**Author:** Some Bloke Down the Pub (who happens to know docbgm, but is better than him at maths)  
**Date:** 28 November 2025  
**Context:** Part of the "Collatz" Framework

---

## 1. Introduction

A central difficulty in the Collatz conjecture is the behavior of numbers with high binary density (many `1` bits). These numbers can grow under the odd step, raising the worry that a trajectory could maintain a stable block of 1s indefinitely.

This document proves the **Algebraic Fracture Lemma**, which states:

> **Any contiguous block of 1s is fractured (broken) by the multiplication-by-3 step in the Collatz map.**

This makes high-density states structurally unstable.

---

## 2. Definitions

### **Definition 2.1 — Contiguous Block**

A number (n) contains a **block of (k) ones starting at bit (m)** if its binary expansion has:

* bits (m) through (m+k-1): all 1
* bit (m-1): 0
* bit (m+k): 0

This can be expressed as:

```math
n = A \cdot 2^{m+k+1} + (2^k - 1) \cdot 2^m + B
```

where (0 \le B < 2^{m-1}).

---

### **Definition 2.2 — The Map**

We study:

```math
T(n) = 3n + 1
```

Since `+1` only affects the low bits (the "fuse"), the **fracture** comes entirely from multiplying by 3.

---

## 3. Theorem 1 — Mersenne Fracture (Base Case)

**Theorem.**
If (n = 2^k - 1) (a Mersenne number of (k) ones), then for any (k \ge 2):

> **The binary expansion of (3n) contains no block of (k) consecutive 1s.**

---

### **Proof**

Compute:

```math
3n = 3(2^k - 1) = 3\cdot 2^k - 3.
```

Expand:

```math
3 \cdot 2^k = 2^{k+1} + 2^k.
```

Binary form:

```
11 followed by k zeros
```

Subtract 3:

* This flips the bottom bits
* But crucially introduces a `0` at the position where the original block would have continued

The resulting binary pattern is:

```
1 0 1 1 ... 1 0 1
```

The longest block of consecutive 1s in this pattern has length **k-2**.

Adding the `+1` step:

```
3n + 1 = 1011...101 + 1 = 1011...110
```

This does NOT fix the fracture at bit `k`.

✔ **Mersenne blocks always fracture.**

---

## 4. Theorem 2 — Internal Block Fracture

**Theorem.**
Let (n) contain an internal block of (k \ge 3) ones starting at position (m):

```
... 0  [111...111]  0 ...
      m           m+k-1
```

Then in `3n`, **bit m+k is always 0**, meaning the block cannot shift upward intact.

---

### **Proof**

Write:

* `n` has 1s at bits `m` to `m+k-1`, 0 at `m-1`, `m+k`
* `2n` is `n` shifted left by 1

Hence:

| Bit index | n     | 2n    | Carry in | Sum   | Carry out |
| --------- | ----- | ----- | -------- | ----- | --------- |
| m-1       | 0     | ?     | ?        | ?     | → cₘ      |
| m         | 1     | 0     | cₘ       | 1+cₘ  | → cₘ₊₁    |
| m+1       | 1     | 1     | cₘ₊₁     | cₘ₊₁  | → 1       |
| ...       | 1     | 1     | 1        | 1     | → 1       |
| m+k-1     | 1     | 1     | 1        | 1     | → 1       |
| **m+k**   | **0** | **1** | **1**    | **0** | → 1       |
| m+k+1     | 0     | 0     | 1        | 1     | → 0       |

At the critical fracture bit:

```math
s_{m+k} = 0 + 1 + 1 = 2 \equiv 0 \pmod{2}.
```

Thus bit `m+k` is **forced to be 0**.

✔ The block breaks at its upper boundary.

---

## 5. Corollary — The Infinite Regress Problem

To keep a block of ones intact, one would have to *repair* the forced 0 at bit `m+k`.

That would require:

```math
1 + 1 + 1 = 3
```

But this is impossible because:

1. the bit of `n` is 0 by definition
2. the bit of `2n` is 1 by definition
3. the carry is forced and cannot be manipulated

Also, the low bits ("fuse") are constantly destroyed by repeated odd steps, so there is no supply of rightward 1s that could maintain the block.

✔ **Blocks cannot be repaired; they always shrink.**

---

## 6. Conclusion

The Algebraic Fracture Lemma shows:

* Mersenne blocks fracture
* Internal blocks fracture
* Fracture cannot be repaired
* Long blocks cannot survive the Collatz map

This provides a **rigorous foundation** for the Recharge Funnel model:
high-density structures collapse, sending trajectories toward states where halving dominates.

---
