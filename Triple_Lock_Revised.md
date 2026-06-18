# The Triple Lock: Three Structural Barriers to Non-Trivial Cycles in the $3x+1$ Problem

> **Status: exploratory structural summary.**
> Arithmetic and parity observations here are evidential. The former
> “stability lock” has been withdrawn as a cycle-stability theorem; the
> parity-itinerary result does not imply metric repulsion.

**Author:** Dr. Bry
**Date:** Revised 2026 (originally 28 November 2025)
**License:** CC-BY 4.0 (free to cite, share, and reuse with attribution)

---

## Preface

This is **not** a proof of the Collatz conjecture, and nothing below should be read as one. It is an expository account of three independent structural reasons why non-trivial cycles appear hostile to construct. Each barrier is stated at its true strength: where a claim is an exact theorem it is labelled as such; where it is computational evidence it is labelled as such; and the gap between the two is named explicitly rather than blurred.

The three barriers are:

1. **Arithmetic Lock** — most up/down patterns admit no integer cycle solution at all *(computational/structural; not universal)*.
2. **Parity Lock** — the rare integer solutions found are "ghost loops" that violate Collatz parity *(verified on all tested cases; not proven universal)*.
3. **Itinerary Fragility** — nearby starting values cannot follow the same
   parity-rule sequence indefinitely. This is not a theorem about metric
   attraction or repulsion.

A fourth, fully rigorous structural identity — the **Block-Fracture Identity** — is summarised in §5 and proved in the companion note `Block_Fracture_Lemma.md`. It is exact, but it constrains *growth mechanisms*, not cycles directly, so it is presented as supporting structure rather than as one of the three locks.

The honest summary: the conjecture remains open, several of these barriers are evidential rather than proven, and the document's value is in organising *why* cycles are hard to build, not in claiming they cannot exist.

---

## 1. The central observation

A non-trivial cycle would have to survive all three locks simultaneously:

* most patterns die in **Lock 1** (no integer solution),
* the survivors so far all die in **Lock 2** (parity violation),
* any genuine survivor would be eroded by **Lock 3** (instability).

This is a statement about *structural hostility*, not impossibility. The qualifiers in §0 are load-bearing.

---

## 2. Lock 1 — The Arithmetic Lock (Diophantine barrier)

Suppose a full cycle contains $k$ **Up** steps (odd $\to 3x+1$) and $m$ total **Down** steps ($x/2$). Over one period the map acts affinely:
$$
T(n) = \frac{3^k}{2^m}\,n + \frac{C}{2^m},
$$
where $C$ depends only on the *order* of the U's and D's. A cycle requires $T(n)=n$, the **cycle equation**
$$
n = \frac{C}{2^m - 3^k}, \qquad G := 2^m - 3^k .
$$

### 2.1 How $C$ depends on the pattern

Indexing the U-steps along the path and letting $v_j$ be the number of D-steps before the $j$-th U,
$$
C = \sum_{j=1}^{k} 3^{\,k-j}\,2^{\,v_j}.
$$
Different permutations give different $C$; a fixed $(k,m)$ gives a fixed gap $G$.

### 2.2 The Arithmetic Lock in practice

An integer cycle needs $G \mid C$. A 2025 search over $>10{,}000$ permutations across several $(k,m)$ pairs found that for the large majority of patterns $\gcd(C,|G|)=1$, so $G \nmid C$ and no integer solution exists.

> **Arithmetic Lock (evidential).** The cycle equation has no integer solution for almost all *tested* patterns.

**This is not a universal theorem.** Some patterns *do* satisfy $G\mid C$; those are exactly the ones that proceed to Lock 2. Promoting "almost all tested" to "all" is the principal open gap of this section, and it is essentially the hard part of the cycle problem.

---

## 3. Lock 2 — The Parity Lock ("Ghost Loop" barrier)

When arithmetic does line up, $n = C/G \in \mathbb{Z}$ is an algebraic fixed point of the *forced* U/D affine map. To be a real Collatz cycle, every step must also match the **parity** of the current value.

### 3.1 A worked ghost loop

Take the pattern `UUDDDDUUDDUDD`, which has $k=5$ U-steps and $m=8$ D-steps, so
$$
G = 2^8 - 3^5 = 256 - 243 = 13.
$$
The D-counts before each U are $v = (0,0,4,4,6)$, giving
$$
C = 3^4 2^0 + 3^3 2^0 + 3^2 2^4 + 3^1 2^4 + 3^0 2^6 = 364,
\qquad n = \frac{364}{13} = 28 .
$$
*(Arithmetic verified exactly.)* Forcing the map (applying U/D regardless of parity) yields a perfect algebraic loop through $28$. But the real Collatz map checks parity: the pattern's first step is `U` ("odd $\to 3x+1$"), while $28$ is **even** — Collatz sends $28 \to 14 \to 7$, not $28 \to 85$. The candidate is a *ghost loop*: an algebraic solution that is dynamically illegal.

Across the tested $(k,m)=(5,8)$ permutations with $\gcd(C,G)=13$, every integer solution found was a ghost loop of this kind.

> **Parity Lock (evidential).** Every integer solution of the cycle equation found so far violates Collatz parity and cannot occur in the true dynamics.

Again the qualifier matters: "every solution found so far" is not "every solution." A universal version would require proving that $\gcd(C,G)>1 \Rightarrow$ parity violation, for all $(k,m)$.

---

## 4. Lock 3 — The Stability Lock (Parity-Fragility / instability)

The companion note proves a narrower symbolic statement:

> **Parity-Fragility Theorem.** For trajectories from $n$ and $n+\delta$ with $\delta\neq 0$: if $\delta$ is odd the trajectories diverge at the first odd value; if $\delta = 2^a d$ with $d$ odd, they diverge after at most $a$ shared halvings, once the difference becomes odd.

Consequently no distinct nearby integer can follow exactly the same parity
itinerary indefinitely. It may later merge with the original trajectory, so
this does not establish metric instability, isolation, or absence of a basin.
It also says nothing about whether the cycle exists.

---

## 5. Supporting structure — The Block-Fracture Identity (exact)

The strongest fully-rigorous component of this project is not one of the three locks but an exact identity about the growth mechanism itself, proved in `Block_Fracture_Lemma.md`:

> **Block triple (exact).** For $L\ge 2$, $\;3(2^L-1) = \texttt{10}\,1^{L-2}\,\texttt{01}$ in binary. An isolated block of $L$ consecutive ones is mapped by multiplication-by-3 to an interior run of length $L-2$, framed by `10`…`01`, with the block's bit-count preserved.
>
> **Mersenne erosion (exact).** For $L\ge 2$, $\;v_2(3(2^L-1)+1)=1$ and the odd-step image is $\texttt{10}\,1^{L-1}$, so the leading run of ones drops from $L$ to $L-1$.

This corrects the earlier informal claim that blocks are "annihilated": they are not, the run contracts deterministically (by $2$ under $\times 3$, by $1$ per Mersenne odd-step). The identity bears on cycles only indirectly — it shows the bit-structure that would *fuel* sustained growth cannot sustain itself for free — and it is explicitly **not** a bound on the longest run of arbitrary integers (which can and does grow; see the companion note's §5).

---

## 6. Summary

| Barrier | What it checks | Status | Typical result |
|---|---|---|---|
| **Arithmetic Lock** | Is $n=C/G$ an integer? | Evidential | Almost always **no** |
| **Parity Lock** | Does an integer $n$ legally follow the U/D pattern? | Evidential | Solutions are **ghost loops** |
| **Itinerary Fragility** | Can a distinct start share one parity itinerary forever? | **Theorem** | No; no metric-stability conclusion |
| **Block-Fracture** (support) | What does $\times 3$ do to a run of ones? | **Exact identity** | Run contracts $L\to L-2$ |

Three barriers, each independently hostile to cycle construction; one exact structural identity underpinning the growth analysis. The $3x+1$ conjecture remains formally open. What this document establishes is organised, partly-rigorous *structural hostility*, with the evidential-versus-proven boundary drawn explicitly at every step.

---

## 7. What would close the gaps

1. **Universal arithmetic barrier:** prove $\gcd(C,G)=1$ for all permutations of sufficiently large $(k,m)$ — or
2. **Universal parity barrier:** prove $\gcd(C,G)>1 \Rightarrow$ the resulting $n$ is always a ghost loop — or
3. **Joint impossibility:** an algebraic constraint making both conditions unsatisfiable at once.

Each of these is, in effect, equivalent to resolving cycle non-existence; none is a polishing step. Current evidence is consistent with all three but proves none.

---

## References & companions

* `Block_Fracture_Lemma.md` — exact proof and verification of the Block-Fracture Identity and Mersenne erosion (§5 here).
* `Collatz_Parity_Fragility_Corrected.md` — proof of the Stability Lock (§4 here).
* Computational searches (2025) on the cycle equation; all arithmetic in §2–§3 independently re-verified.

---

## Acknowledgments

This work organises extensive computational exploration of Collatz dynamics, including the "ghost loop" phenomenon — algebraic cycle solutions that cannot be dynamically realised due to parity constraints — and corrects the earlier "block annihilation" heuristic into the exact identity of §5.
