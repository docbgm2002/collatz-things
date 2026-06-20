# The Early Gap-\(2\) Synchronization Tree

**Building on:** `repunit_gap_merger_analysis.md`
**Status:** Exact synchronization cylinders and depth-truncated symbolic
census. The census does not prove that every exponent eventually
synchronizes with its gap-\(2\) predecessor.
**License:** CC-BY 4.0

---

## 1. Pairwise synchronization

At level \(s\), consider the exact relation

\[
x_s(n)=x_{s+2}(n-2).
\]

This must be studied independently of the first smaller source returned by a
global merger index. Several smaller tails may occupy the same diagonal
state. In particular, a tail may synchronize with \(n-2\) while being
recorded as first merging with \(n-4\).

For predecessor valuation words

\[
\mathbf e=(e_0,\ldots,e_{s-2}),
\qquad
\mathbf f=(f_0,\ldots,f_s),
\]

compute their normal-form states

\[
(E,A),\qquad(F,B).
\]

They produce a first synchronization at level \(s\) exactly when:

1. their exponent cylinders are compatible after shifting the second
   exponent by \(2\);
2. \(3A+2^{E+1}=3B+2^{F+1}\);
3. \(E\ne F\).

The final condition distinguishes a first collision from a pair that had
already synchronized one step earlier.

`explore_repunit_sync_tree.py` performs this enumeration symbolically in
valuation-word space.

---

## 2. Levels 2 and 3

Level \(2\) has the exact family

\[
n\equiv31\pmod{64}
\quad\Longrightarrow\quad
x_2(n)=x_4(n-2).
\]

Level \(3\) has four exact first-hit families:

\[
\begin{array}{rcl}
n&\equiv&79\pmod{128},\\
n&\equiv&199\pmod{256},\\
n&\equiv&323\pmod{512},\\
n&\equiv&1289\pmod{4096}.
\end{array}
\]

Each satisfies

\[
x_3(n)=x_5(n-2)
\]

on the smallest collision shell \(|E-F|=2\).

The \(1289\bmod4096\) family was hidden in the first-merger table because
these tails also meet the \((n-4)\)-tail at the same diagonal.

---

## 3. Level 4

The symbolic search through cumulative valuation depth \(24\) finds the
following 17 exact first-hit cylinders. Every one lies on
\(|E-F|=2\):

| residue | modulus | \(n\)-predecessor word | \((n-2)\)-predecessor word |
|---:|---:|---|---|
| 111 | \(2^8\) | \((5,1,2)\) | \((2,1,1,1,1)\) |
| 263 | \(2^9\) | \((4,3,2)\) | \((2,1,2,1,1)\) |
| 423 | \(2^{10}\) | \((4,2,4)\) | \((2,1,2,2,1)\) |
| 451 | \(2^{10}\) | \((3,5,2)\) | \((2,2,2,1,1)\) |
| 627 | \(2^{11}\) | \((3,2,6)\) | \((2,2,1,3,1)\) |
| 631 | \(2^{11}\) | \((4,1,6)\) | \((2,1,3,2,1)\) |
| 1795 | \(2^{11}\) | \((3,4,4)\) | \((2,2,2,2,1)\) |
| 383 | \(2^{12}\) | \((8,1,1)\) | \((2,1,1,2,6)\) |
| 731 | \(2^{12}\) | \((3,1,8)\) | \((2,3,1,3,1)\) |
| 1699 | \(2^{12}\) | \((3,3,6)\) | \((2,2,3,2,1)\) |
| 3257 | \(2^{13}\) | \((2,3,8)\) | \((4,1,2,3,1)\) |
| 6409 | \(2^{13}\) | \((2,9,2)\) | \((4,3,2,1,1)\) |
| 1889 | \(2^{14}\) | \((2,2,10)\) | \((6,1,1,1,3)\) |
| 4873 | \(2^{14}\) | \((2,8,4)\) | \((4,3,2,2,1)\) |
| 10889 | \(2^{14}\) | \((2,6,6)\) | \((4,3,1,3,1)\) |
| 969 | \(2^{15}\) | \((2,5,8)\) | \((4,4,1,3,1)\) |
| 6153 | \(2^{15}\) | \((2,7,6)\) | \((4,3,3,2,1)\) |

Each row is an exact infinite synchronization family:

\[
x_4(n)=x_6(n-2)
\]

for every positive odd exponent in the stated cylinder.

The enumeration is exhaustive only through the stated cumulative valuation
depth. Still deeper, sparser level-\(4\) cylinders are not excluded.

---

## 4. Depth-\(24\) level masses

At common modulus \(2^{24}\), the resolved first-hit masses are:

| level \(s\) | first-hit cylinders | resolved odd classes | fraction of odd classes | ratio to previous level |
|---:|---:|---:|---:|---:|
| 2 | 1 | 262,144 | 3.125000% | - |
| 3 | 4 | 233,472 | 2.783203% | 0.890625 |
| 4 | 17 | 176,128 | 2.099609% | 0.754386 |
| 5 | 80 | 138,817 | 1.654828% | 0.788160 |
| 6 | 372 | 110,065 | 1.312077% | 0.792878 |
| 7 | 1,616 | 91,467 | 1.090372% | 0.831027 |

The level sets are disjoint, as required for first synchronization. Their
resolved cumulative mass through level \(7\) is

\[
\frac{1{,}012{,}093}{8{,}388{,}608}
\approx12.0651\%
\]

of the odd residue classes modulo \(2^{24}\).

These are lower bounds because cylinders deeper than \(24\) are unresolved.
The decline is consistent with roughly geometric level mass over this short
range, but it does **not** show that the uncovered mass tends to zero. A
geometrically decreasing sequence of new hits may have a finite total.

---

## 5. Strategic consequence

The gap-\(2\) tree is mathematically real:

- its nodes are exact exponent cylinders;
- first-hit levels are automatically disjoint;
- all resolved early collisions use the smallest shell, apart from rare
  deeper-shell examples beginning at later levels.

But the current mass data does not support gap \(2\) as a complete merger
mechanism. Its apparent level decay may leave a large positive survivor set.

The next useful move is therefore comparative:

1. build the corresponding first-hit trees for gaps \(4\) and \(6\);
2. measure overlap between the different gap trees;
3. determine whether their union removes residue mass substantially faster;
4. reserve Baker and cumulative surplus for the common survivor set.

---

## 6. Reproduction

```bash
python explore_repunit_sync_tree.py --through-step 7 \
    --max-total 24 --common-depth 24
python verify_repunit_gap_mergers.py
```
