# Multi-Gap Synchronization-Tree Union

**Building on:** `repunit_gap2_sync_tree.md`,
`repunit_gap_merger_analysis.md`
**Status:** Exact symbolic construction with bounded depth and time.
The reported masses are finite lower bounds, not asymptotic densities.
**License:** CC-BY 4.0

---

## 1. General synchronization relation

For an even exponent gap \(g\), level \(s\) studies

\[
\boxed{x_s(n)=x_{s+g}(n-g).}
\]

The two states lie on the same diagonal because

\[
n+s=(n-g)+(s+g).
\]

For fixed predecessor valuation words of lengths \(s-1\) and \(s+g-1\),
the collision-shell identity gives an exact exponent cylinder. A cylinder is
a first hit at level \(s\) exactly when the predecessor cumulative valuations
are unequal.

`explore_repunit_sync_tree.py` now implements this construction for arbitrary
even \(g\). `explore_repunit_sync_union.py` compares several trees at a common
power-of-two depth.

---

## 2. Common bounded census

The main comparison uses:

\[
g\in\{2,4,6\},
\qquad
2\le s\le7,
\qquad
E,F\le20,
\]

with all cylinders lifted to the odd residue classes modulo \(2^{20}\).

There are

\[
2^{19}=524{,}288
\]

odd classes at this depth.

### Gap \(2\)

| level | cylinders | resolved classes | odd-class fraction |
|---:|---:|---:|---:|
| 2 | 1 | 16,384 | 3.125000% |
| 3 | 4 | 14,592 | 2.783203% |
| 4 | 17 | 11,008 | 2.099609% |
| 5 | 79 | 8,676 | 1.654816% |
| 6 | 316 | 6,859 | 1.308250% |
| 7 | 905 | 5,521 | 1.053047% |

The level sets are disjoint. Their union contains

\[
63{,}040
\]

classes, or \(12.023926\%\).

### Gap \(4\)

| level | cylinders | resolved classes | odd-class fraction |
|---:|---:|---:|---:|
| 2 | 1 | 256 | 0.048828% |
| 3 | 8 | 689 | 0.131416% |
| 4 | 42 | 892 | 0.170135% |
| 5 | 171 | 1,076 | 0.205231% |
| 6 | 354 | 1,088 | 0.207520% |
| 7 | 456 | 852 | 0.162506% |

The gap-\(4\) tree union contains \(4{,}853\) classes, or \(0.925636\%\).

### Gap \(6\)

| level | cylinders | resolved classes | odd-class fraction |
|---:|---:|---:|---:|
| 2 | 1 | 16 | 0.003052% |
| 3 | 7 | 25 | 0.004768% |
| 4 | 26 | 61 | 0.011635% |
| 5 | 33 | 65 | 0.012398% |
| 6 | 39 | 51 | 0.009727% |
| 7 | 11 | 12 | 0.002289% |

The gap-\(6\) tree union contains \(230\) classes, or \(0.043869\%\).

---

## 3. Cross-gap overlap

The pairwise intersections are:

| trees | intersection | odd-class fraction |
|---|---:|---:|
| gaps \(2,4\) | 1,609 | 0.306892% |
| gaps \(2,6\) | 53 | 0.010109% |
| gaps \(4,6\) | 35 | 0.006676% |

The triple intersection contains \(15\) classes.

By inclusion-exclusion, the combined union is

\[
\boxed{
66{,}441
}
\]

of the \(524{,}288\) odd classes:

\[
\boxed{
12.672615\%.
}
\]

Thus gaps \(4\) and \(6\) add only \(3{,}401\) classes, or approximately
\(0.648689\) percentage points, beyond the shallow gap-\(2\) tree.

---

## 4. Breadth versus temporal depth

At the same depth and through level \(7\), adding gaps \(8,10,12\) contributes
only one further resolved class. This is a bounded observation, but it shows
that merely adding more nearby exponent gaps at very early times does not
reproduce the \(95.70\%\) eventual merger rate seen through \(n\le10001\).

Extending gap \(2\) alone through level \(12\), still with cumulative
valuation cutoff \(20\), raises its resolved union to

\[
70{,}232/524{,}288
\approx13.395691\%.
\]

Later level masses become heavily truncated because the minimum possible
cumulative valuation grows with the word length. This figure is therefore a
lower bound, not evidence of saturation.

The comparison indicates that **temporal depth is the main missing
dimension** in this bounded census. The empirical merger phenomenon is not
explained by a handful of shallow synchronization families.

---

## 5. Strategic consequence

The synchronization-tree programme remains mathematically useful, but direct
enumeration faces two related growth problems:

1. the number of valuation-word cylinders grows rapidly with time;
2. a fixed cumulative-valuation cutoff omits an increasing fraction of later
   levels.

Continuing by simply increasing depth and time will produce larger finite
certificates without automatically yielding a theorem.

The next proof-oriented target should compress shell hitting into a recurrence
on a smaller state space. The most promising state is the relative
same-diagonal pair

\[
\Delta E=E-F,
\qquad
\Delta A=A-B,
\]

or the normalized collision defect

\[
\mathcal C
=
3(A-B)+2^{E+1}-2^{F+1}.
\]

A merger is exactly \(\mathcal C=0\). The objective is to derive how
\(\mathcal C\) evolves when the two aligned tails take one step together,
without enumerating their complete valuation words.

If that recurrence has a contracting, recurrent, or finite-quotient
structure, it could explain the high eventual merger rate. If it does not,
the merger-first programme may remain a strong reduction but not the final
proof mechanism.

---

## 6. Reproduction

```bash
python explore_repunit_sync_union.py \
    --gaps 2,4,6 --through-step 7 \
    --max-total 20 --common-depth 20
python verify_repunit_sync_union.py
```
