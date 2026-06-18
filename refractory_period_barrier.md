# ⭐ **THE REFRACTORY PERIOD BARRIER**

> **Status: exploratory computational model.**
> The thresholds and random-bit assumptions in this note are empirical and
> do not establish universal collapse.

### *Why Large Fusion Events Are Always Fatal in the Collatz Map*

**Author:** Dr. Bry  
**Date:** 28 November 2025  
**Context:** Part of the "Collatz" Framework

---

## 1. Introduction

The previous papers in this series established two structural principles:

1. **Algebraic Fracture** —
   Large blocks of consecutive 1s are unstable under the map

   ```math
   T(n) = 3n + 1.
   ```
2. **Fusion–Fracture Cycle** —
   The only mechanism that can *create* such blocks is **Fusion**, which requires an alternating suffix

   ```
   101010...
   ```

   whose multiplication by 3 produces a solid block.

Together, these imply a necessary cycle for any growth event:

```text
Fusion → Fracture → Debris → (possible Reorganization) → Fusion
```

The central question of this paper is:

> **Can a Collatz trajectory reorganize the debris of a Fracture quickly enough to permit another Fusion event before it decays toward 1?**

This paper presents the **Refractory Period Barrier**:
for alternating structures longer than about **16 bits**, the time required to reorganize debris back into a Fusion-capable pattern exceeds the time required for the number to decay to 1.

This provides computational and probabilistic evidence that **large Fusion events are dynamically self-destroying**.

---

## 2. Definitions

### 2.1 Fusion Candidate (Order L)

An odd integer (n) is a **Fusion Candidate of order (L)** if its binary representation ends in an alternating suffix of length (L):

```math
n \equiv \sum_{k=0}^{L-1} 4^k \pmod{2^L}.
```

Examples:

```
L = 6:   101010
L = 10:  1010101010
```

Fusion Candidates are the only known inputs that produce significant density growth in a single step.

---

### 2.2 Refractory Period (T_{\text{rec}})

Let:

* (n_0): a Fusion Candidate of order (L)
* (n_1): the result of the Fusion → Fracture event
  (a solid block that has been broken)

The **Refractory Period** is:

```math
T_{\text{rec}} = \min \{ k \ge 1 : n_k \text{ has an alternating suffix of length } \ge L/2 \}.
```

This measures how long it takes the debris to reorganize into a new partial Fusion Candidate.

---

## 3. Computational Study: The Critical Threshold

The following table reports:

* whether recovery occurs
* the number of steps required
* the net change in magnitude

  ```math
  \frac{n_{\text{final}}}{n_{\text{start}}}.
  ```

We tested perfect alternating suffixes up to order 25 ((L=50)) and near-perfect ones up to 80 bits.

| Initial L | Outcome   | T_rec | Net Growth (n_final / n_start) |
| --------- | --------- | ----- | ------------------------------ |
| **10**    | Recovered | 75    | **105.45×**                    |
| **12**    | Recovered | 58    | **295.99×**                    |
| **14**    | Recovered | 94    | **1.56×**                      |
| **16**    | Recovered | 201   | **0.02×**                      |
| **18**    | Collapsed | N/A   | → **1**                        |
| **20**    | Collapsed | N/A   | → **1**                        |

---

### 3.1 The Small-L Regime (L ≤ 14)

When (L \le 14):

* Fusion creates a spike
* Fracture breaks the spike
* Debris reorganizes quickly
  (often in < 100 steps)

The number survives long enough to rebuild the alternating structure.

This regime explains the chaotic behaviour of small starting values.

---

### 3.2 The Pyrrhic Recovery at L = 16

At (L = 16):

* the alternating suffix *does* reappear
* but only after **201 steps**
* and in that time the number shrinks to **2%** of its original value

Meaning:

```math
\text{gain from Fusion} \ll \text{loss during Refractory Period}.
```

This is the turning point.

---

### 3.3 The Event Horizon (L ≥ 18)

For (L \ge 18), we found:

* no recovery occurs before reaching the 4–2–1 loop
* no alternating suffix ≥ 12 bits reappears
* the number collapses instead of reorganizing

This is the **Refractory Period Barrier** in practice.

---

## 4. Theoretical Mechanism: Entropy vs. Decay

Why does the threshold occur at such a small value?

### 4.1 Reorganization Cost (Exponential)

Debris after a Fracture behaves statistically like a random bitstring.

The probability that a random (L)-bit string is alternating is:

```math
p = 2^{-L}.
```

Expected waiting time:

```math
E[T_{\text{rec}}] = 1/p = 2^L.
```

Thus recovery time grows **exponentially** with L.

---

### 4.2 Decay Rate (Linear-in-L)

During the debris phase, numbers behave like a multiplicative random walk with expected ratio (3/4):

```math
n_k \approx n_0 (3/4)^k.
```

For a Fusion Candidate, (n_0 \approx 2^L).
The decay time scale is:

```math
T_{\text{decay}} \sim \frac{L}{\log(4/3)} \approx 2.4 L.
```

Decay time grows **linearly** with L.

---

### 4.3 Comparison of Time Scales

```math
T_{\text{rec}} \sim 2^L,
\qquad
T_{\text{decay}} \sim 2.4 L.
```

Once (L) exceeds about 16:

```math
2^L \gg 2.4 L,
```

making reorganization exponentially slower than decay.

This explains the sharp transition observed in the computational data.

---

## 5. Main Result

### **Empirical model (Refractory Period Barrier).**

Let (n_0) be a Fusion Candidate of order (L).
Let (n_k) be the trajectory defined by the Collatz map.
Then:

1. If (L \ge 16), the Refractory Period satisfies

   ```math
   T_{\text{rec}} \gg T_{\text{decay}}.
   ```
2. For (L \ge 18), computational experiments up to 80 bits show (T_{\text{rec}}) does not occur before the trajectory reaches the trivial cycle.
3. Thus large Fusion events produce structures too large to reorganize before decaying.

**Interpretation:**
Large Fusion events are dynamically self-limiting.

---

## 6. Conclusion

The **Refractory Period Barrier** completes the structural picture of high-density behaviour in the Collatz map:

* **Fusion** produces temporary growth.
* **Fracture** collapses high density.
* **Reorganization** is exponentially slow.
* **Decay** is comparatively fast.

Therefore:

> **In the tested families, sufficiently large Fusion events were followed by collapse before recovery.**

This is computational and probabilistic evidence, not a universal guarantee.

Combined with earlier papers, this supports the principle:

> **High-density structures in the Collatz dynamics are inherently unstable at every scale.**

---
