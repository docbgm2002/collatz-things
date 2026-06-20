# Repunit Diagonal Survivor Notes

**Building on:** `repunit_tail_attack.md`, `repunit_affine_tail_bound.md`,
`repunit_normal_form_notes.md`
**Status:** Finite diagnostic results and next proof target. This note contains
no universal survivor classification.

---

## 1. Purpose

For odd \(n\), define

\[
\sigma_n=\min\{K\ge1:f^K(a_n)<2^n-1\},
\qquad
a_n=\frac{3^n-1}{2}.
\]

The diagonal survivor experiment studies the scaled sets

\[
\mathcal S_C(N)
=\{n\le N:n\text{ odd},\ \sigma_n>Cn\}.
\]

The aim is to determine whether unusually long repunit tails are governed by:

1. a small collection of exponent residue classes;
2. repeated valuation blocks;
3. a parametrised exceptional family; or
4. a cumulative inequality not visible from fixed low bits.

The accompanying program is
`explore_repunit_diagonal_survivors.py`.

---

## 2. Extended constant search

The exact finite sweep over odd \(7\le n\le10001\), with a search window
\(K\le3n\), finds:

- no unresolved exponent;
- no exception to \(\sigma_n\le2.75n\);
- the ratio record remains
  \[
  \frac{\sigma_{23}}{23}=\frac{63}{23}=2.739130\ldots;
  \]
- the ratio-record exponents are \(7,11,17,23\);
- the smallest exact first-descent margin is approximately
  \(0.000152208\) bits, at \(n=6035\), \(\sigma_n=8236\).

These are finite observations. They support retaining \(3n\) as a conservative
working window and \(2.75n\) as a sharper empirical benchmark, but prove
neither.

The near-zero margin is important: even though the ratio record stabilises in
this range, first descent can occur with almost no slack. Any proof based on a
uniform positive descent margin is therefore poorly matched to the data.

---

## 3. Affine correction separated

`repunit_affine_tail_bound.md` proves that before descent

\[
\log_2(1+q_K)
<
\frac{K}{3(2^n-1)\ln2}.
\]

Thus the near-zero margins at large \(n\) are not caused by uncontrolled growth
of the affine correction. The affine term is exponentially small in the
linear window. The thin margin reflects the valuation surplus itself passing
the target line very closely.

This closes one possible explanation and focuses the next stage on valuation
blocks.

---

## 4. Scaled survivor structure through \(n\le5001\)

The first structured scan gives:

| threshold \(C\) | count of \(\sigma_n>Cn\) |
|---|---:|
| \(1.5\) | 467 |
| \(1.75\) | 15 |
| \(2.0\) | 10 |
| \(2.25\) | 5 |
| \(2.5\) | 3 |
| \(2.7\) | 2 |
| \(2.73\) | 1 |

The three survivors beyond \(2.5n\) are \(n=17,23,25\). The survivors beyond
\(2.7n\) are \(n=17,23\), and only \(n=23\) exceeds \(2.73n\).

At the lower threshold \(1.5n\), survivors occupy:

- all four odd classes modulo \(8\);
- all eight odd classes modulo \(16\);
- all sixteen odd classes modulo \(32\);
- \(127\) of the \(128\) odd classes modulo \(256\).

So survival beyond \(1.5n\) is not explained by one simple low-bit congruence.

At the higher thresholds the sets are sparse, but their valuation prefixes
also separate rapidly:

- among the 15 survivors beyond \(1.75n\), all first eight-valuation blocks
  are distinct;
- among the 10 survivors beyond \(2n\), all first eight-valuation blocks are
  distinct;
- the five survivors beyond \(2.25n\) already have distinct first
  four-valuation blocks.

No repeated fixed prefix currently explains the long survivors.

---

## 5. Interpretation

The finite data does not support the simplest residue-family hypothesis:

> There is one fixed congruence class of exponents, or one fixed short
> valuation prefix, responsible for all long repunit tails.

The \(1.5n\) survivor set is broad in low-bit residue space, while the very long
survivors are isolated and quickly acquire unique prefixes.

This points toward a different object: a **moving block deficit**. Different
valuation words may produce the same cumulative shortage relative to the
required line even when their exact prefixes and exponent residues differ.

The next diagnostic should therefore classify blocks by quantitative state,
not literal word:

\[
\Delta_{i,L}
=\sum_{j=i}^{i+L-1}e_j-L\log_2 3,
\]

together with:

- starting surplus relative to the Mersenne target;
- minimum prefix surplus inside the block;
- ending surplus;
- maximum run of \(e_j=1\);
- correction state \(A_i\) modulo a selected power of two.

The goal is to find a finite collection of deficit block types that either:

1. recover within a bounded following window; or
2. force the exponent into a deeper residue restriction.

---

## 6. Next task

Extend the explorer with a block-deficit report:

1. choose block lengths \(L\in\{8,16,32,64\}\);
2. scan every block before first descent;
3. rank blocks by lowest mean valuation and lowest minimum-prefix surplus;
4. cluster by coarse quantitative signature;
5. test whether each severe deficit block is followed by a compensating
   payout within \(L\), \(2L\), or \(4L\) steps.

A candidate lemma should be formulated only after this report identifies a
stable recovery relation. Literal valuation-word enumeration should not be
used as the primary classifier.

---

## 7. Block-scale results

Primitive and active-tail scans produced the following finite hierarchy:

- negative 64-blocks occur and may require up to 140 steps from block start
  to recover nonnegative local surplus;
- the proposed nonnegative 128-block floor fails at \(n=2449\), where active
  128-blocks of total valuation \(197\) occur;
- every such negative 128-block recovers within 150 steps in the tested range;
- every active 256-block through odd \(n\le10001\) has total valuation at least
  \(425\), with a unique minimum at \(n=2449\), step \(306\).

This led to the conditional reduction in `repunit_256_block_target.md`.
