# Nested-Anchor / Mersenne Route: Final Assessment

**Status:** Research wrap-up. Exact lemmas and finite certificates are
separated below from conjectures and unresolved targets.

## 1. Starting idea

For the shortcut Collatz map

\[
U(x)=
\begin{cases}
x/2,&x\text{ even},\\
(3x+1)/2,&x\text{ odd},
\end{cases}
\]

a length-\(k\) parity prefix containing \(\rho\) odd positions satisfies

\[
U^k(a+2^km)=U^k(a)+3^\rho m.
\]

This makes nested anchors an exact affine residue-tree construction.

## 2. Exact results obtained

### 2.1 Anchor identities

The shortcut identity above is exact. For the accelerated odd-only map,
if a valuation prefix has total valuation \(E\) and length \(j\), then

\[
f^j(x+2^{E+1}q)=f^j(x)+2\cdot3^jq.
\]

The extra bit is necessary to preserve the final exact valuation.

### 2.2 Tree interpretation

For \(r>1\), an odd shortcut residue class \(r\bmod2^K\) is uniformly
discharged by depth \(K\) if and only if the representative \(r\) itself has
stopping time at most \(K\). Thus the anchor tree is an exact prefix-code
organization of stopping-time certificates, not an independent proof
mechanism.

At depth \(22\), the finite tree discharges

\[
2{,}003{,}930/2{,}097{,}152=95.55\%
\]

of odd classes.

### 2.3 All-ones branch

The nested all-ones classes

\[
2^K-1\pmod{2^K}
\]

converge \(2\)-adically to \(-1\). No positive integer remains on this branch
through every depth. This removes the all-ones branch as a literal positive
infinite path, but finite Mersenne exits remain difficult.

### 2.4 Mersenne budget

For odd \(n\), \(M_n=2^n-1\) reaches

\[
a_n=\frac{3^n-1}{2}
\]

after exactly \(n+1\) shortcut steps. If \(H(n)\) is the shortcut time from
\(a_n\) to below \(M_n\), then

\[
\sigma_U(M_n)=n+1+H(n).
\]

Finite computation for every odd \(7\le n\le10001\) gives

\[
H(n)\le5n-2,
\qquad
\sigma_U(M_n)\le6n-1.
\]

The record is exactly

\[
H(23)=113=5\cdot23-2,
\qquad
\sigma_U(M_{23})=137=6\cdot23-1.
\]

This is a finite certificate, not a universal theorem.

### 2.5 Odd-density reduction

For every odd \(n\ge9\), survival of the repunit tail through \(5n-2\)
shortcut steps requires more than

\[
\left\lfloor\frac{11n}{4}\right\rfloor
\]

odd positions. The proof is exact for \(9\le n\le17\) and uses a uniform
analytic bound for \(n\ge19\).

The corresponding possible-survivor classes have exponentially small density,
bounded asymptotically by

\[
2^{-(0.0361277\ldots+o(1))n}.
\]

The unresolved issue is non-concentration of the algebraic repunit sequence
inside this thin set.

### 2.6 Enemy coordinates and scaling merger

A shortcut prefix has exact normal form

\[
U^t(a_n)=\frac{3^{n+\rho}+D_t}{2^{t+1}}.
\]

Writing

\[
D_t=3^rd,\qquad m=n+\rho-r,
\]

gives

\[
v_2(3^m+d)\ge t+1.
\]

If two prefix states have equal \((m,d,r)\), they differ by a power of two.
The larger state therefore reaches the smaller after forced even shortcut
steps. This is an exact scaling-merger lemma.

The finite census verifies:

- \(168\) scaling-merger pairs through odd \(n\le2001\);
- \(271\) scaling-merger pairs through odd \(n\le3001\).

## 3. Final finite stress test

Extending the high-odd-density census from \(n\le2001\) to \(n\le3001\)
produced no new near-budget records. The uniquely close cases remain:

| \(n\) | \(H(n)\) | slack in \(5n-2\) |
|---:|---:|---:|
| 23 | 113 | 0 |
| 17 | 82 | 1 |
| 25 | 120 | 3 |
| 11 | 46 | 7 |

All four have reduced enemy height approximately equal to the full modulus
depth. Direct fixed-height Baker/Yu estimates therefore do not control them.

At the same time, many later high-height states fall into exact scaling-merger
families. This shows real inheritance structure, but no theorem currently
forces every near-budget high-height state into such a family.

## 4. Where the route stalls

The remaining desired dichotomy is:

> Every near-budget high-odd-density prefix either has low reduced enemy
> height, hence is Baker-controllable, or shares an inheritable collision
> coordinate with a smaller controlled state.

The finite evidence supports both mechanisms separately but does not prove
their exhaustiveness. The isolated record cases remain high-height and do not
display the scaling collision used by the proved merger lemma.

Further census enlargement is unlikely to resolve this logical gap. It would
mostly add larger merger families while leaving the need for a universal
classification theorem unchanged.

## 5. Recommendation

Pause this route as a completed exploratory branch.

Retain:

1. the exact anchor identities;
2. the corrected residue-certificate boundary;
3. the shortcut tree and its finite coverage;
4. the conjectural \(6n\) Mersenne target;
5. the \(55\%\) odd-density reduction;
6. the enemy-coordinate normal form;
7. the exact scaling-merger lemma.

Do not promote:

1. \(H(n)\le5n-2\) beyond the verified finite range;
2. the high-odd-density non-concentration statement;
3. an exhaustive Baker-or-merger dichotomy.

The line becomes worth reopening only if a new theorem supplies either:

- a non-concentration estimate for powers of \(3\) against adaptive parity
  prefix sets; or
- an ancestry theorem forcing high-height enemy coordinates to merge.

## 6. Reproducibility

```bash
python scripts/verify_nested_anchor_work.py
python scripts/explore_shortcut_anchor_tree.py
python scripts/explore_mersenne_shortcut_budget.py --limit 10001
python scripts/explore_high_odd_repunit_prefixes.py --limit 3001
```
