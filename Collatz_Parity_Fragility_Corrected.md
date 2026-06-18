# **Collatz Parity Fragility and Instability of Near-Cycles**

> **Status: proved parity-itinerary result with corrected interpretation.**
> Distinct starts cannot share one parity-rule sequence indefinitely. The note
> does not prove non-merging, metric repulsion, or absence of basins.

*A friendly, clean write-up by a physicist who got interested in the Collatz map.*

**Author:** Dr. Bry  
**Date:** 28 November 2025  
**Context:** Part of the "Collatz" Framework

---

## 1. Introduction

This note collects a simple but important observation about the **instability** of nearby trajectories in the Collatz map. The idea is straightforward:

* Track two starting values that differ by a small offset.
* Ask whether their trajectories can stay “in sync” for long.
* Show that unless the offset is **exactly zero**, they eventually cease to
  follow the same parity-rule sequence.

This is **not** a proof of the Collatz conjecture.
It does **not** rule out non-trivial cycles.
It shows that two distinct starting values cannot follow the same parity-rule sequence indefinitely. This is a symbolic-instability statement only: trajectories may later merge, and the result does not establish metric repulsion or rule out basins.

The argument is elementary: just parity and powers of two.

---

## 2. Setup

The Collatz map is:

* If $n$ is even: $C(n) = n/2$
* If $n$ is odd: $C(n) = 3n + 1$

Take two starting points:

* $x_0 = n$
* $y_0 = n + \delta$, with $\delta \neq 0$

Define the difference:

$$
\Delta_i = y_i - x_i .
$$

We want to understand how $\Delta_i$ evolves while the two trajectories follow the **same odd/even rule sequence**.

---

## 3. Odd Differences: Immediate Divergence

If $\delta$ is **odd**, then $n$ and $n+\delta$ begin with opposite parity.

So:

* one applies $3n+1$,
* the other applies $n/2$.

Thus after one step:

$$
\Delta_1 = C(n+\delta) - C(n)
$$

cannot be zero unless $\delta = 0$.

> **Conclusion:** odd initial differences cause *immediate* divergence.

---

## 4. Even Differences and the Evolution of $\Delta$

Now suppose $\delta$ is **even**.
Then the two starting values have the same parity and begin by applying the same rule.

Write:

$$
\delta = 2^k d, \qquad d \text{ odd},\ k \ge 1.
$$

We study how $\Delta$ evolves when both trajectories apply the same rule.

### 4.1 Odd step: $3x + 1$

If both are odd:

$$
x_{i+1} = 3x_i + 1, \qquad y_{i+1} = 3y_i + 1
$$

so

$$
\Delta_{i+1} = 3\Delta_i .
$$

The parity (and $2$-adic valuation) of $\Delta$ is unchanged.

### 4.2 Even step: $x/2$

If both are even:

$$
x_{i+1} = \frac{x_i}{2}, \qquad y_{i+1} = \frac{y_i}{2},
$$

so

$$
\Delta_{i+1} = \frac{\Delta_i}{2} .
$$

This reduces the exponent of $2$ in $\Delta$ by one.

### 4.3 Summary Table

| Step type | Update rule               | Effect on $v_2(\Delta)$ |
| --------- | ------------------------- | ----------------------- |
| odd step  | $\Delta \mapsto 3\Delta$  | unchanged               |
| even step | $\Delta \mapsto \Delta/2$ | minus 1                 |

Eventually the halving steps remove all powers of 2, and $\Delta_i$ becomes **odd**.

Once $\Delta_i$ is odd, the next Collatz step cannot be the same for both trajectories — see Section 3.

---

## 5. Instability Theorem

> **Theorem (Instability of Nonzero Differences).**
> Let two Collatz trajectories start at $n$ and $n+\delta$ with $\delta \ne 0$.
> Suppose they follow the same parity-rule sequence for $L$ steps.
> Write $\delta = 2^k d$ with $d$ odd.
> If the shared rule sequence contains at least $k$ halving steps, then the trajectories must diverge at or before step $L$.

### Proof (short and direct)

* If $k=0$, the difference is odd and divergence is immediate.
* If $k\ge1$, each halving step reduces the $2$-adic valuation of $\Delta$.
* After the first $k$ halving steps:
  $$
  \Delta_j = 3^m d
  $$
  for some $m \ge 0$, and this number is **odd**.
* With an odd difference, the next step cannot remain synchronized: the two values now have opposite parity.

Therefore, no non-zero difference can remain synchronized indefinitely.
$\square$

---

## 6. Consequences for “Near-Cycles”

Suppose we have something that almost looks like a cycle:

$$
C^k(n) = n + \delta, \quad |\delta| \text{ small}.
$$

Then:

* if $\delta \ne 0$, the trajectory from $n$ and the trajectory from $n+\delta$ cannot stay synchronized indefinitely;
* the parity-fragility argument guarantees eventual divergence;
* this does not by itself determine whether a true cycle is attracting or repelling under any chosen metric.

It does not rule out merging trajectories or basins: losing a shared parity itinerary is weaker than never meeting again.

---

## 7. What This Does *Not* Prove

To eliminate cycles entirely, one must analyze the classical **cycle equation**:

$$
n = \frac{C}{2^m - 3^k},
$$

where $m$ and $k$ count how many halving and odd steps the hypothetical cycle uses.

This note does **not** tackle that.
All we have shown is:

* trajectories with non-zero offsets eventually cease to share one
  parity-rule sequence;
* no conclusion about attraction, repulsion, merging, or basin size follows from this argument alone.

The Collatz conjecture remains open.

---

## 8. Summary

* Odd difference → immediate divergence.
* Even difference → eventually stripped of powers of two → becomes odd → divergence.
* No non-zero $\Delta$ can remain synchronized forever.
* The result concerns shared parity itineraries, not cycle stability.
* This does *not* rule out non-trivial cycles; it only describes their **local instability**.

---
