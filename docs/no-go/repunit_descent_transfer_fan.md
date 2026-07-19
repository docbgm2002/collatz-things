# The Repunit Descent-Transfer Fan

**Status:** Exact inductive transfer lemma plus a finite negative diagnostic.
The single gap-two comparison has substantial finite coverage, but widening it
to a bounded fan of smaller exponents adds no new certificates on its residual.

## 1. Exact transfer lemma

Put

\[
a_n=\frac{3^n-1}{2},\qquad M_n=2^n-1,
\]

and write \(x_i(n)\) for the accelerated odd trajectory of \(a_n\).
Let \(g\ge2\) be even and suppose the \((n-g)\)-tail has a descent

\[
x_s(n-g)<M_{n-g},\qquad s\ge g.
\]

The states \(x_{s-g}(n)\) and \(x_s(n-g)\) lie on the same repunit
diagonal.  Since

\[
2^gM_{n-g}+(2^g-1)=M_n,
\]

the inequality

\[
\boxed{
x_{s-g}(n)\le 2^g x_s(n-g)+(2^g-1)
}
\]

implies \(x_{s-g}(n)<M_n\).  Thus it transfers descent from a smaller
exponent without requiring an exact trajectory merger.

This is a sound strong-induction rule.  It is an inequality analogue of the
same-diagonal merger criterion.

## 2. Why the idea looked promising

For \(g=2\), the comparison is especially simple:

\[
x_{s-2}(n)\le4x_s(n-2)+3.
\]

Through odd \(9\le n\le5001\), evaluated at the first descent time of the
\((n-2)\)-tail, this inequality holds for 2169 of 2497 tested exponents
(86.86%).  Existing earlier exact merges or descents discharge most of the
remaining cases.

The comparison also arose from a temporal diagnostic.  At fixed gap two,
the range of the aligned cumulative-valuation difference through the observed
outcome has median 22 on merged tails and median 115 on primitive descending
tails.  This suggested a possible dichotomy between bounded discrepancy
(merger) and large discrepancy (descent).

## 3. The bounded-fan falsifier

After removing every case discharged either by the gap-two transfer or by an
earlier independently known outcome, 134 exponents remain through
\(n\le5001\).

For each residual exponent, test every even gap

\[
4\le g\le80
\]

at the first descent time of the \((n-g)\)-tail.  The result is:

- **zero** genuine additional transfer inequalities;
- 45 apparent wins occur only after the \(n\)-tail's already-known outcome,
  so they add no certificate;
- 89 exponents remain untouched;
- the untouched set includes the hard exponent \(n=471\).

The useful comparator gaps also keep growing rather than stabilizing. This
rejects a fixed bounded fan, but the unrestricted calculation below shows
that it does not reject the complete fan.

## 4. The unrestricted fan

For each odd $9\le n\le5001$, test every even gap $2\le g\le n-3$ for which
the first descent time $s$ of the smaller tail satisfies $s\ge g$. The exact
census gives:

- 2169 gap-two certificates;
- 244 additional certificates from larger gaps;
- 84 exponents with no certificate at any gap;
- total coverage $2413/2497=96.6360\%$;
- nine rescues whose smallest successful gap exceeds 80;
- largest smallest-successful gap 264, at $n=4853$.

Thus the cutoff at 80 missed genuine exact induction certificates. The hard
exponent $n=471$ nevertheless remains a strong falsifier: all 140 admissible
smaller-tail comparators fail. The full output is reproduced by
`scripts/explore_repunit_full_descent_transfer_fan.py`.

## 5. Same-diagonal surplus wedge

Put $P_i(n)=E_i(n)-i$. For a comparator with smaller exponent $m=n-g$,
smaller first descent time $s$, and aligned high time $t=s-g$, define

\[
H_g=P_s(m)-P_t(n)=E_s(n-g)-E_{s-g}(n)-g.
\]

This is the payout-surplus difference at the same diagonal $m+s=n+t$.
Across all admissible comparisons through $n=5001$:

| condition | transfer fails | transfer holds |
|---|---:|---:|
| $H_g>0$ | 1,744,783 | 0 |
| $H_g\le0$ | 2 | 74,393 |

Both exceptions have $H_g=0$: $(n,g)=(219,2)$ and $(3099,4)$. Strict surplus
ordering therefore predicts the transfer inequality perfectly on this
census; only the equality boundary retains an affine-correction dependence.
For $n=471$, every admissible comparator has $H_g\ge23$.

> **Strict surplus-transfer target.** At aligned first-descent comparators,
> $H_g<0$ forces the transfer inequality and $H_g>0$ forbids it; when $H_g=0$,
> the sign is decided by the exact correction order.

This target has a short conditional proof. Write

\[
x_i(r)+1=L_i(r)+Z_i(r),\qquad
L_i(r)=\frac{3^{r+i}}{2^{E_i(r)+1}},\qquad
Z_i(r)=\frac{R_i(r)}{2^{E_i(r)+1}}.
\]

At the aligned diagonal $d=n+t=m+s$, put $X=x_t(n)$ and $Y=x_s(m)$.
Then

\[
2^g(Y+1)
=2^{-H_g}L_t(n)+2^gZ_s(m).
\]

Suppose both compared corrections obey the **storage-dominance bound**

\[
0<R_i(r)<3^{r+i},
\tag{SD}
\]

equivalently $0<Z_i(r)<L_i(r)$. If $H_g\le-1$, the first term on the
right is at least $2L_t(n)$, while $X+1<2L_t(n)$; hence the transfer holds.
If $H_g\ge1$, the two right-hand terms are each strictly below
$L_t(n)/2$ after putting them over the aligned denominator, while
$X+1>L_t(n)$; hence transfer fails. For $H_g=0$, cancellation of the common
homogeneous term leaves the exact correction order.

Thus (SD) proves the strict sign law. An exact scan finds no violation of
(SD) at any state through and including first descent for every odd
$3\le n\le5001$
(`scripts/verify_repunit_storage_dominance.py`). This finite fact is not
promoted to a theorem. The active writeup is
`avenue_a_comparison_dynamics.md`. The new proof target is:

> **First-descent storage-dominance lemma (open).** Every odd repunit tail
> satisfies $0<R_i(n)<3^{n+i}$ through and including its first descent below
> $M_n$.

The bound is sharp in time: on every small odd seed, and on $n=471$, the
first failure of $R_i<3^{n+i}$ occurs strictly after first descent. Relative
storage admits the exact series in the Avenue A note; the open step is to
estimate that payout sum under the prefix constraint $x_j\ge M_n$.

The unconstrained correction-layer maximum is

\[
R_K\le3^K\left(2^{E_K-K+1}-1\right).
\]

It proves (SD) under the sufficient cumulative-surplus condition

\[
2^{E_K-K+1}-1<3^n.
\]

That condition is much too coarse. At the first descent of $n=193$ one has
$K=434$, $E_K=800$, and $E_K-K=366$; the sufficient inequality misses by
about 61 bits, while the actual correction still satisfies (SD). Therefore a
proof cannot use total surplus alone. It must exploit payout placement and
the prefix constraints saying that every earlier state stayed above $M_n$.
This is exactly the constrained extremal content of the storage-dominance
lemma.

If proved, an all-gap failure becomes a **surplus wedge** against every
admissible smaller exponent. This uses actual smaller repunit trajectories
and does not suffer from the virtual-word mismatch of the correction fan.

## 6. Earlier decision, revised

Do not search for another fixed gap cutoff. Continue only through the
same-diagonal surplus coordinate. The acceptable next results are:

1. a proof of the strict surplus-transfer target;
2. a monotone envelope showing that some smaller first-descent surplus must
   fall below the high-tail surplus; or
3. a structural implication turning a universal surplus wedge into an exact
   merge or quantitative later payout.

The exponent \(n=471\) and the 84 full-fan failures should be used as early
falsifiers.

## 7. Literature gate

Pairwise coalescence, predecessor trees, affine trajectory formulae, and
mixed-base rewriting are established human approaches to the Collatz
problem.  No direct prior use of the displayed repunit descent-transfer
inequality was found in the literature check. Generic pairwise comparison is
human-trodden territory, but the repunit-specific first-descent surplus wedge
is sufficiently exact and selective to justify the narrow continuation above.
