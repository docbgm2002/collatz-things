# Baker Non-Shadowing for the Repunit Enemy Branch

**Building on:** `repunit_low_prefix_obstruction.md`,
`repunit_tail_merge_reduction.md`
**Status:** The fixed enemy-branch bound is a consequence of known effective
\(p\)-adic logarithmic-form estimates. The general extension is limited by
the height of the induced enemy constant.
**License:** CC-BY 4.0

---

## 1. The problem

For odd \(n\), write

\[
a_n=\frac{3^n-1}{2}.
\]

`repunit_low_prefix_obstruction.md` constructs an explicit adversarial
valuation word

\[
\mathbf e_K=(2,\underbrace{1,\ldots,1}_{K-1})
\]

on nested exponent classes converging in \(\mathbb Z_2\) to the ghost
solution

\[
3^{\alpha+1}=-7.
\]

Every finite prefix occurs on positive exponents, so finite modular
compatibility alone cannot exclude the branch. The required statement is
positive-integer non-shadowing: one fixed positive exponent cannot follow
this ghost branch for a window proportional to its size.

---

## 2. Enemy-branch equivalence

**Theorem 1 (restatement).** For odd \(n\ge3\), the repunit tail \(a_n\)
has initial valuation word \((2,1^{K-1})\) if and only if

\[
v_2(3^{n+1}+7)\ge K+3.
\]

*Proof.* This is Theorem 4 of `repunit_low_prefix_obstruction.md`.
\(\blacksquare\)

Thus long shadowing is exactly a deep \(2\)-adic alignment of
\(3^{n+1}\) with the fixed integer \(-7\).

---

## 3. The \(p\)-adic logarithmic-form input

**Known theorem (fixed-\(d\) consequence of Yu).** Fix a nonzero odd integer
\(d\). Effective lower bounds for \(2\)-adic linear forms in logarithms give
an effective constant \(C_d>0\) such that, whenever \(m\ge2\) and
\(3^m+d\ne0\),

\[
v_2(3^m+d)\le C_d\log m.
\]

*Reference.* Kunrui Yu, *\(p\)-adic logarithmic forms and group varieties
II*, Acta Arithmetica **89** (1999), 337-378,
doi: [10.4064/aa-89-4-337-378](https://doi.org/10.4064/aa-89-4-337-378).
This note uses only the standard fixed-\(d\) consequence. It does not derive
or optimize a numerical value of \(C_d\).

**Corollary 2.** For fixed nonzero odd \(d\), the set

\[
\{m\in\mathbb N:v_2(3^m+d)\ge m\}
\]

is finite.

*Proof.* Such an \(m\) satisfies \(m\le C_d\log m\), which has only finitely
many solutions. \(\blacksquare\)

---

## 4. Fixed-branch non-shadowing

**Theorem 3.** Let odd \(n\ge3\) have repunit-tail prefix
\((2,1^{K-1})\). Then

\[
K+3\le C_7\log(n+1),
\]

and hence \(K=O(\log n)\).

*Proof.* Theorem 1 gives

\[
K+3\le v_2(3^{n+1}+7).
\]

Apply the fixed-\(d\) theorem with \(d=7\) and \(m=n+1\).
\(\blacksquare\)

This improves the elementary \(K=O(n)\) ordinary-size bound in REPLOW4 to
\(K=O(\log n)\) for this structured branch.

**Corollary 4.** Let \(g(n)/\log(n+1)\to\infty\). For all sufficiently large
odd \(n\), the tail of \(a_n\) cannot begin with
\((2,1^{g(n)-1})\).

In particular, it cannot begin with \((2,1^{3n-1})\).

---

## 5. What this proves

- A positive integer exponent can shadow the fixed
  \(3^{\alpha+1}=-7\) ghost branch for only \(O(\log n)\) steps.
- The arbitrarily long finite ghost truncations and this theorem are
  compatible: the positive representatives grow rapidly as the truncation
  deepens.
- This removes the explicit \((2,1^*)\) branch as a possible linear-window
  obstruction.

It does **not** prove:

- \(\sigma_n\le Cn\) for all odd \(n\);
- non-shadowing for every moving low-surplus pattern;
- off-diagonal merger or a block-surplus theorem;
- universal Mersenne descent.

---

## 6. General prefixes and the height gate

For a realised prefix ending at time \(K\), write the exact normal form as

\[
x_K=\frac{3^{n+K}+A_K}{2^{E_K+1}}.
\]

Since \(x_K\) is odd,

\[
v_2(3^{n+K}+R_K)\ge E_K+2,
\qquad
R_K=A_K+2^{E_K+1}.
\]

Remove the largest power of \(3\) from \(R_K\):

\[
R_K=3^{r_K}d_K,\qquad 3\nmid d_K.
\]

Whenever \(n+K-r_K>0\), the prefix therefore induces

\[
v_2(3^{n+K-r_K}+d_K)\ge E_K+2.
\]

This is the correct general Baker normalization. Its usefulness is controlled
by the logarithmic height of \(d_K\), not merely by the block length or
valuation deficit.

For \((2,1^{K-1})\), cancellation leaves the fixed constant \(d_K=7\), so
the estimate is strong. For generic primitive prefixes, the finite diagnostic
`explore_baker_enemy_height.py` finds
\(\operatorname{bitlength}|d_K|\) comparable to \(E_K\). A variable-\(d\)
bound then feeds the unknown valuation mass back into its own upper bound and
does not by itself prove non-shadowing.

### Revised target BAKER-GEN

1. Classify prefix families whose reduced enemy height \(\log|d_K|\) is
   bounded or small relative to the required valuation.
2. Apply \(p\)-adic logarithmic-form estimates to those low-height families.
3. Send high-height moving patterns to the merger, variable-window surplus,
   or correction-state programmes.

This height gate prevents the fixed-\(7\) success from being promoted into a
universal claim without the missing cancellation.

---

## 7. Finite diagnostics

`verify_repunit_baker_nonshadowing.py` checks only the exact enemy equivalence
and a finite logarithmic envelope:

1. nested classes \(K=1,\ldots,64\) and \(K=256\) realise
   \((2,1^{K-1})\) iff \(v_2(3^{n+1}+7)\ge K+3\);
2. the same bidirectional equivalence on odd \(7\le n\le 50001\) via modular
   prefix replay (no full-orbit tracing);
3. the empirical envelope
   \[
   K\le30\log_2(n+1)+10
   \]
   on that range.

The envelope is a finite diagnostic, not a certification of Yu's constant.

`explore_baker_enemy_height.py` measures the reduced height
\(\operatorname{bitlength}|d_K|/E_K\) on primitive tails and documents why
generic prefixes do not inherit the fixed-\(7\) cancellation.

`repunit_baker_applicability_census.md` and
`explore_baker_applicability.py` refine this to active pre-descent states.
They introduce the enemy coordinate \((m_K,d_K)\), prove that it is invariant
through valuation-one runs, and identify the finite low-height families.

```bash
python verify_repunit_baker_nonshadowing.py
python explore_baker_enemy_height.py --limit 2001
python explore_baker_applicability.py --limit 5001
```
