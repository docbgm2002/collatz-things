# High-Odd-Density Repunit Prefixes

**Building on:** `../nested-anchor/nested_anchor_escape_notes.md`,
`repunit_baker_nonshadowing.md`,
`repunit_tail_merge_reduction.md`

**Status:** Exact prefix identities plus finite diagnostics. No universal
\(6n\) Mersenne bound is claimed.

## 1. Exact shortcut normal form

For odd \(n\), put

\[
a_n=\frac{3^n-1}{2},
\qquad
T_n=2^n-1.
\]

After \(t\) shortcut steps containing \(\rho\) odd positions,

\[
U^t(a_n)=\frac{3^\rho a_n+c_t}{2^t}
=\frac{3^{n+\rho}+D_t}{2^{t+1}},
\qquad
D_t=2c_t-3^\rho.
\]

The correction satisfies

\[
c_{t+1}=
\begin{cases}
c_t,&\text{on an even shortcut step},\\
3c_t+2^t,&\text{on an odd shortcut step}.
\end{cases}
\]

Factor

\[
D_t=3^{r_t}d_t,\qquad3\nmid d_t,
\qquad
m_t=n+\rho-r_t.
\]

Integrality gives the exact enemy equation

\[
\boxed{
v_2(3^{m_t}+d_t)\ge t+1.
}
\]

This is the shortcut analogue of the accelerated repunit enemy coordinate.

## 2. Finite near-budget census

`scripts/explore_high_odd_repunit_prefixes.py` traces each repunit tail only until
first descent and ranks its final surviving prefix.

For odd \(7\le n\le2001\), the closest cases to

\[
H(n)\le5n-2
\]

are:

| \(n\) | \(H(n)\) | budget slack | last-survivor odd density |
|---:|---:|---:|---:|
| 23 | 113 | 0 | \(63/112=0.56250\) |
| 17 | 82 | 1 | \(46/81=0.56790\ldots\) |
| 25 | 120 | 3 | \(67/119=0.56302\ldots\) |
| 11 | 46 | 7 | \(25/45=0.55555\ldots\) |

These are exactly the kind of prefixes predicted by the odd-density
reduction: unusually long survival is accompanied by odd density above
\(55\%\).

## 3. Direct Baker bounds miss the dangerous cases

At the final surviving states for \(n=11,17,23,25\), the reduced enemy height

\[
h_t=\operatorname{bitlength}|d_t|
\]

satisfies

\[
\frac{h_t}{t+1}=1.02\ldots
\]

up to small fluctuations. Almost all the modulus-scale information is stored
inside \(d_t\). Consequently the fixed-height Baker/Yu argument that kills the
\((2,1^*)\) ghost branch does not directly control these near-budget cases.

This confirms the height gate from `repunit_baker_nonshadowing.md`: the
dangerous prefixes are high-height moving targets, not fixed-\(d\) families.

## 4. Repeated enemy coordinates

The finite census finds repeated reduced constants, and in many cases repeated
full coordinates \((m_t,d_t)\), across nearby exponents. For example, the
last-survivor states for \(n=193\) and \(n=195\) share

\[
m_t=627
\]

and the same \(797\)-bit reduced constant \(d_t\).

The remaining powers of \(3\) and \(2\) in

\[
U^t(a_n)
=
\frac{3^{r_t}(3^{m_t}+d_t)}{2^{t+1}}
\]

determine when the common coordinate gives a literal merger.

**Lemma (equal-\((m,d,r)\) scaling merger).** Suppose two prefix states have
the same \((m,d,r)\), at shortcut depths \(t_1>t_2\). Then

\[
X_2=2^{t_1-t_2}X_1.
\]

Consequently \(X_2\) takes \(t_1-t_2\) forced even shortcut steps and lands
exactly on \(X_1\).

*Proof.* Both states have the same numerator

\[
3^r(3^m+d).
\]

Their denominators are \(2^{t_1+1}\) and \(2^{t_2+1}\), giving the displayed
power-of-two ratio. Since \(X_1\) is an integer, the larger state is divisible
by \(2^{t_1-t_2}\), so the intervening shortcut steps are forced halvings.
\(\square\)

The explorer verifies many such mergers. In the leading family,

\[
n=939,941,943,945
\]

all merge by forced even steps into the displayed last-survivor state for
\(n=937\). Thus a whole cluster of high-height prefixes is inherited from one
lower-scale arithmetic state rather than representing independent bad
branches.

Repeated \((m,d)\) with unequal \(r\) still require additional analysis. The
useful remaining questions are whether they imply:

1. later shortcut coalescence;
2. inheritance of descent from the smaller exponent; or
3. a collision-shell relation already present in the accelerated merger
   theory.

## 5. Revised next target

The finite data disfavors a proof based solely on low-height ghost branches.
The stronger target is:

> **Enemy-coordinate inheritance target.** Extend the proved
> equal-\((m,d,r)\) scaling merger to repeated \((m,d)\) coordinates with
> unequal \(r\), or show that the unequal-\(r\) case has enough valuation
> surplus to be harmless.

If such inheritance handles the repeated high-height families, Baker/Yu can
remain responsible only for genuinely low-height isolated branches.

## 6. Verification

```bash
python scripts/explore_high_odd_repunit_prefixes.py --limit 2001
```
