# Collatz Parity Fragility and Near-Loop Instability (Corrected)

## 1. Context

This document is a corrected and sharpened version of the earlier **Parity-Fragility / Near-Loop** arguments.

What we keep as *rigorous*:

- The behaviour of the **difference** between two Collatz trajectories that start at nearby integers.
- A clear description of how **odd** and **even** initial differences evolve under the map.
- The conclusion that any hypothetical non-trivial cycle would be **repelling**: no perturbed starting value can stay on it forever.

What we **do not** claim here:

- We do **not** prove that non-trivial cycles are impossible.
- We do **not** assert that the cycle equation has no integer solutions beyond the trivial 1–4–2–1 loop.

This document is purely about **instability**, not global non-existence of cycles.


---

## 2. Setup and Definitions

We use the standard Collatz map on positive integers:

- If \(n\) is even: \(C(n) = n/2\)
- If \(n\) is odd: \(C(n) = 3n+1\)

We consider two trajectories:

- \(x_0 = n\)
- \(y_0 = n + \\delta\), where \(\\delta \\neq 0\)

At step \(i\), we define:

- \(x_{i+1} = C(x_i)\)
- \(y_{i+1} = C(y_i)\)
- **Difference:** \(\\Delta_i := y_i - x_i\)

We ask: *Can the two trajectories stay on the same “path” for a long time? Can a nonzero difference \(\\delta\) persist indefinitely or return to 0?*


---

## 3. Parity-Fragility Lemma (Odd Difference)

### Lemma 3.1 (Immediate divergence for odd difference)

Let \(x_0 = n\) and \(y_0 = n+\\delta\) with \(\\delta\) **odd**. Then:

- \(x_0\) and \(y_0\) have opposite parity.
- Therefore their very first Collatz step is different:
  - One uses \(3n+1\) (odd rule),
  - The other uses \(n/2\) (even rule).
- Hence the trajectories **diverge immediately** at step 1.

**Proof.**

If \(\\delta\) is odd, then \(n\) and \(n+\\delta\) have opposite parity. So:

- If \(n\) is odd, \(n+\\delta\) is even:
  - \(x_1 = C(n) = 3n+1\)
  - \(y_1 = C(n+\\delta) = (n+\\delta)/2\)

- If \(n\) is even, \(n+\\delta\) is odd:
  - \(x_1 = C(n) = n/2\)
  - \(y_1 = C(n+\\delta) = 3(n+\\delta)+1\)

In either case, \(x_1\) and \(y_1\) are computed by **different formulas**, and the equality \(y_1 = x_1\) cannot hold unless \(\\delta = 0\). Thus for \(\\delta\) odd, the paths diverge immediately. \(\\square\)


---

## 4. Even-Error Evolution

Now suppose \(\\delta\) is **even**. Then \(n\) and \(n+\\delta\) start with the same parity, so they initially follow the **same rule** (odd or even). This allows the trajectories to remain “synchronized” for a while.

Write:

\[
\\delta = 2^k d,
\]
where:

- \(d\) is odd,
- \(k \\ge 1\).

We track how \(\\Delta_i\) evolves under the two possible operations.

### 4.1 Effect of the odd step \(3x+1\)

If both \(x_i\) and \(y_i\) are odd, then:

- \(x_{i+1} = 3x_i + 1\)
- \(y_{i+1} = 3y_i + 1\)

So:

\[
\\Delta_{i+1} = y_{i+1} - x_{i+1} = (3y_i+1) - (3x_i+1) = 3(y_i - x_i) = 3\\Delta_i.
\]

Therefore, under an odd step:

- The difference is multiplied by 3.
- The 2-adic valuation (number of factors of 2) of \(\\Delta_i\) is unchanged.

### 4.2 Effect of the even step \(x/2\)

If both \(x_i\) and \(y_i\) are even, then:

- \(x_{i+1} = x_i / 2\)
- \(y_{i+1} = y_i / 2\)

So:

\[
\\Delta_{i+1} = y_{i+1} - x_{i+1} = \\frac{y_i}{2} - \\frac{x_i}{2} = \\frac{\\Delta_i}{2}.
\]

Therefore, under an even step:

- The difference is halved.
- If \(\\Delta_i = 2^r d\) with \(d\) odd, then \(\\Delta_{i+1} = 2^{r-1} d\).
- Each division step reduces the exponent of 2 by 1.

### 4.3 Consequence: eventual oddness of the difference

If a synchronized segment of the two trajectories includes **at least \(k\) halving steps**, then starting from \(\\Delta_0 = 2^k d\) with \(d\) odd, after those \(k\) divisions we have:

\[
\\Delta_j = 3^m d,
\]

for some integer \(m \\ge 0\). In particular, \(\\Delta_j\) is **odd**.

At that point, the **Parity-Fragility Lemma (odd case)** applies: the very next step cannot preserve the same operation on both sequences, and the trajectories must diverge.


---

## 5. Generalized Parity-Fragility Theorem (Instability of Nearby Trajectories)

We now combine the odd and even cases into one statement about the instability of any putative cycle or long synchronized segment.

### Theorem 5.1 (Instability of nonzero differences along a synchronized path)

Let two Collatz trajectories \((x_i)\) and \((y_i)\) share the **same sequence of operations** (same pattern of “odd steps” and “even steps”) for \(L\) steps, starting from:

- \(x_0 = n\)
- \(y_0 = n+\\delta\) with \(\\delta \\neq 0\).

Assume that among these \(L\) operations there are at least \(k\) halving steps, where \(\\delta = 2^k d\) with \(d\) odd and \(k \\ge 0\).

Then the trajectories cannot remain synchronized indefinitely: there exists some step \(j \\le L\) at which they must diverge.

**Proof.**

- If \(k = 0\) (\(\\delta\) odd), we are in the immediate divergence case of Lemma 3.1: the trajectories diverge at step 1.

- If \(k \\ge 1\) (\(\\delta\) even), then each odd step multiplies the difference by 3 and preserves its parity, while each halving step divides the difference by 2 and reduces its 2-adic valuation by 1. After the first \(k\) halving steps within the shared operation sequence, we obtain:

  \[
  \\Delta_j = 3^m d
  \]

  for some \(m \\ge 0\). Because \(d\) is odd, \(\\Delta_j\) is odd. At this moment the Parity-Fragility Lemma (odd case) applies to the pair \((x_j, y_j)\): their difference is odd, so they cannot both apply the same operation in the next step without contradiction. Hence the shared-path assumption fails and the trajectories diverge.

In all cases \(\\delta \\neq 0\) leads to divergence in finitely many steps. \(\\square\)


---

## 6. Interpretation for Near-Loops

A **Near-Loop** is a pair \((n,k)\) with:

- \(k > 0\),
- \(T^k(n) = n + \\delta\),
- where \(T\) is the Collatz map (or the odd-step map), and \(\\delta\) is “small” (e.g. \(|\\delta| \\le 4\)).

This theorem tells us:

- If \(\\delta \\neq 0\), then the trajectories from \(n\) and \(n+\\delta\) cannot forever follow the same operation sequence.
- Even when \(\\delta\) is even and small (like \(\\pm 2\), \(\\pm 4\)), the difference is gradually stripped of its powers of 2 by halving steps until it becomes odd; then immediate divergence follows.

So:

- Near-loops are **fragile**: they cannot form a stable “thickened” cycle.
- Any hypothetical exact loop (with \(\\delta = 0\)) would be **repelling**: an arbitrarily small nonzero perturbation cannot stay on the loop.


---

## 7. What This Does *Not* Prove

This instability analysis **does not** show that non-trivial cycles are impossible.

To rule out cycles entirely, one must solve the **cycle equation** for each possible step-pattern:

\[
n(2^m - 3^k) = C,
\]

where:

- \(m\) = total number of halving steps in one period,
- \(k\) = number of odd steps in one period,
- \(C\) is a constant determined by the pattern of odd steps and the additive +1 terms in \(3n+1\).

A non-trivial cycle would require an integer solution:

\[
n = \\frac{C}{2^m - 3^k} \\in \\mathbb{Z}, \\quad n > 1.
\]

The parity-fragility and even-error evolution arguments analysed here address the **stability** of such putative cycles, not their **existence**. They show:

- If such a non-trivial cycle exists, it is **isolated and unstable**.
- Nearby initial values cannot remain on it or shadow it forever.

But they do **not** yet demonstrate that **no such integer \(n\) exists** for all possible patterns \((m,k)\).

Thus the **non-existence of non-trivial cycles remains an open problem**, and requires additional diophantine arguments beyond what is provided in this document.


---

## 8. Summary

- We formalized how the difference \(\\Delta_i = y_i - x_i\) between two Collatz trajectories evolves under odd and even steps.
- We proved:
  - Odd initial difference (\\delta odd) ⇒ immediate divergence.
  - Even initial difference (\\delta even) ⇒ eventual odd difference after enough halving steps ⇒ divergence.
- We concluded that any hypothetical cycle is **repelling**: no nonzero perturbation can remain locked onto it.
- We **did not** prove that no cycle exists; that requires ruling out integer solutions of the cycle equation for all step patterns.

This document should be treated as a **corrected, fully rigorous statement of parity-based instability** for Collatz near-loops and nearby trajectories, without overclaiming a full proof of the Collatz conjecture.
