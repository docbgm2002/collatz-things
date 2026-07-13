# Payout Concentration Versus Diffusion

**Status:** PCD1 is an exact ledger trichotomy. PCD2 is a finite certificate
through odd exponent \(5001\). PCD3--PCD6 resolve the proposed short
shell-pairing mechanism, ultimately as a structural no-go. PCD7 begins the
amortized branch with an exact effective-count charge, while PCD8 proves that
spacing and ledger data alone cannot amplify it to a uniform deficit bound.
PCD9 shows that finite repunit-cylinder realization does not remove the
balanced obstruction. PCD10 reduces least-representative growth to a plateau
bound for the nested balanced cylinders, and PCD11 gives an exact cylinder
extension recursion. PCD12 records the resulting finite local-lift
distribution, PCD13 gives the exact plateau cocycle, and PCD14 identifies the
multi-block carry shift. PCD15 rules out fixed-width endpoint compression,
and PCD16 proves that balanced block compositions have uniformly bounded
real distortion. PCD17 converts that distortion bound into exact linear
growth of normalized correction storage. None proves repunit-tail descent.

**Building on:** repunit_extremal_principle.md,
general_payout_ancestry.md

## 1. Exact integer ledger weights

At record time \(K\), the integer correction ledger is

\[
R_K
=3^K+
\sum_{\substack{j<K\\e_j>1}}
3^{K-1-j}2^{E_j+1}(2^{e_j}-2).
\]

Treat the initial term as an ancestor of weight

\[
W_{-1}=3^K
\]

and a payout \(e_j=q\) as an ancestor of transported weight

\[
W_j=3^{K-1-j}2^{E_j+1}(2^q-2).
\]

These are positive integers and

\[
W_{-1}+\sum_jW_j=R_K.
\]

Normalize by \(p_{-1}=W_{-1}/R_K\) and \(p_j=W_j/R_K\).

GPA2 divides the payout ancestors into:

- eligible classes \(\mathcal G=\{j:e_j\not\equiv3,4\pmod6\}\), for which
  canonical reachability is not excluded by the modulo-\(3\) obstruction;
- blocked classes \(\mathcal B=\{j:e_j\equiv3,4\pmod6\}\), whose canonical
  partners are impossible.

Put

\[
I=p_{-1},\qquad
G=\sum_{j\in\mathcal G}p_j,\qquad
B=\sum_{j\in\mathcal B}p_j.
\]

Then

\[
\boxed{I+G+B=1.}
\]

For the blocked mass define

\[
b_*=\max_{j\in\mathcal B}p_j,
\qquad
N_B=\frac{B^2}{\sum_{j\in\mathcal B}p_j^2},
\]

with \(N_B=0\) when \(B=0\).

## 2. PCD1: exact concentration trichotomy

At least one of \(I,G,B\) is at least \(1/3\). This yields three primary
branches:

1. \(G\ge1/3\): a fixed ledger fraction lies in payout classes not excluded
   by GPA2;
2. \(I\ge1/3\): the formal initial ancestor remains large;
3. \(B>1/3\): GPA2-blocked payouts carry a fixed ledger fraction.

The blocked branch has a scale-free concentration alternative. For every
\(0<\eta<1\), either

\[
b_*\ge\eta B,
\]

or

\[
N_B>\frac1\eta.
\]

Indeed, if every blocked share is less than \(\eta B\), then

\[
\sum_{j\in\mathcal B}p_j^2
<
\eta B\sum_{j\in\mathcal B}p_j
=\eta B^2.
\]

At \(\eta=1/2\), every blocked-majority record is therefore either:

- **blocked-concentrated:** one blocked ancestor carries at least half of
  \(B\); or
- **blocked-diffuse:** \(N_B>2\), so the blocked ledger genuinely requires
  more than two effective ancestors.

This proves:

> **PCD1.** Every record ledger lies in an initial, GPA2-eligible, blocked
> concentrated, or blocked diffuse branch, with the quantitative effective
> count alternative above.

The lemma is elementary, but it prevents the single-ancestor and diffuse
cases from being conflated.

## 3. PCD2: finite primitive-record census

The exact census in scripts/explore_payout_concentration.py uses integer
weights for every branch comparison. Through odd exponent \(5001\), it finds
\(165\) tails classified as primitive by the finite merger scan and \(110\)
strict record prefixes satisfying \(D_K\ge2\). The records split as follows:

| branch | records |
|---|---:|
| \(G\ge1/3\) | 88 |
| \(I\ge1/3\) after the eligible branch is removed | 0 |
| blocked-concentrated | 16 |
| blocked-diffuse | 6 |

All six blocked-diffuse records lie on the single tail \(n=471\), at

\[
K=31,33,34,35,37,38.
\]

At \(K=38\), its largest blocked shares are produced by

\[
(j,q)=(14,3),(0,4),(13,3),(27,3)
\]

with respective ledger shares approximately

\[
32.10\%,\quad21.35\%,\quad12.04\%,\quad2.64\%.
\]

The largest blocked-concentrated example in this range is \(n=3881\),
\(K=36\): a \(q=4\) payout at \(j=1\) carries approximately \(79.62\%\) of
the complete ledger.

The percentages are for presentation only. Membership in every branch and
the threshold \(D_K\ge2\) are tested by exact integer inequalities.

## 4. What the census changes

The GPA2 obstruction does not force most dangerous records into the blocked
branch: \(88\) of \(110\) retain at least one-third of their ledger in payout
classes where direct canonical reachability remains possible. Attack 2,
correction-set geometry, is therefore still relevant to most records.

The remaining records are highly structured:

- blocked-concentrated records demand a two-ancestor or payout-charge theorem
  for one dominant \(q=3\) or \(q=4\) atom;
- the only blocked-diffuse tail currently observed is \(n=471\), whose four
  significant blocked ancestors provide a concrete test case for the
  spacing and pair equations in primitive_ancestry_lemma.md.

This is useful narrowing, not a universal classification. A larger census
may reveal further diffuse patterns.

## 5. PCD3: consecutive \(q=3\) shell fusion

The diffuse test case contains consecutive \(q=3\) payouts at \(j=13,14\).
This instance belongs to a universal shell identity.

If the first payout has pre-payout valuation \(E\), its canonical displacement
is \(S(E+1,2)\). After one time step it is transported by a factor \(3\). The
second payout has pre-payout valuation \(E+3\), so its displacement is
\(S(E+4,2)\). Direct calculation gives

\[
\begin{aligned}
S(E+4,2)-3S(E+1,2)
&=2^{E+5}-3\cdot2^{E+2}\\
&=5\cdot2^{E+2}\\
&=S(E+1,4).
\end{aligned}
\]

Thus:

> **PCD3.** Two consecutive \(q=3\) canonical shells have an exact transported
> difference equal to a height-\(4\) collision shell.

This is a fusion identity, not a reachability theorem. Nor does GPA2
automatically block the fused object: GPA2 concerns the complete canonical
correction created by an actual payout, whereas the identity above concerns
only a shell displacement. The base correction of the combined two-ancestor
target must be derived before its residue or reachability can be decided.

## 6. PCD4: mixed blocked/eligible shell fusions

The exact mixed-pair classifier transports an earlier canonical displacement
to a later payout time and tests

\[
\left|3^{q-p}S(u_p,2h_p)-S(u_q,2h_q)\right|
=S(V,2H).
\]

Through odd exponent \(5001\), the \(110\) dangerous primitive records contain
\(671\) distinct pairs with one GPA2-blocked and one eligible payout. Exactly
\(43\) differences are collision shells. Every fusion belongs to one of six
valuation-block types.

For a common pre-payout valuation \(E\), the identities are:

\[
\begin{array}{rcll}
(2,3):&
S(E+3,2)-3S(E,2)&=S(E,4),\\
(3,2):&
S(E+3,2)-3S(E+1,2)&=S(E+1,2),\\
(4,2):&
S(E+4,2)-3S(E,4)&=S(E,2),\\
(3,1,2):&
9S(E+1,2)-S(E+4,2)&=S(E+1,2),\\
(2,1,1,3):&
S(E+5,2)-27S(E,2)&=S(E,4),\\
(3,a,b,2),\ a+b=3:&
S(E+6,2)-27S(E+1,2)&=S(E+1,4).
\end{array}
\]

All six follow by substituting

\[
S(u,2)=2^{u+1},\qquad S(u,4)=5\cdot2^{u+1}.
\]

This proves the six displayed identities universally. The statement that
they are the only mixed fusion patterns in the stated primitive census is a
finite certificate, not a universal classification.

The identities show that mixed shell fusion is common and rigid at short
valuation blocks. They still concern displacement differences only. To turn
one into a merger, the paired construction must specify a complete target
correction and then meet the automatic-realisation criterion.

## 7. PCD5: displacement fusion does not lift naively

Let a short fusion block have first canonical correction \(C_0\), final
canonical correction \(C_r\), and \(r\) intervening diagonal increments. The
most direct attempt to attach a base correction to the transported pair is

\[
L=C_r-3^rC_0.
\]

The initial correction cancels from \(L\), but the affine injections between
the two payouts do not. For the PCD4 blocks one obtains

| valuation block | first/later lower valuations | \(L/2^{E+1}\) |
|---|---:|---:|
| \((2,3)\) | \(E,\ E+3\) | \(9\) |
| \((3,2)\) | \(E+1,\ E+3\) | \(10\) |
| \((4,2)\) | \(E,\ E+4\) | \(17\) |
| \((3,1,2)\) | \(E+1,\ E+4\) | \(38\) |
| \((2,1,1,3)\) | \(E,\ E+5\) | \(81\) |
| \((3,1,2,2)\) | \(E+1,\ E+6\) | \(194\) |
| \((3,2,1,2)\) | \(E+1,\ E+6\) | \(242\) |

When the lower-valuation gap is odd, no collision shell can connect the two
formal states. In the two even-gap cases:

\[
\begin{array}{c|c|c}
\text{block}&\text{required displacement}&\text{actual }L\\
\hline
(3,2)&S(E+1,2)=2\cdot2^{E+1}&10\cdot2^{E+1}\\
(4,2)&S(E,4)=5\cdot2^{E+1}&17\cdot2^{E+1}.
\end{array}
\]

Neither matches. Therefore:

> **PCD5.** None of the seven short mixed-fusion blocks lifts to a collision
> by transporting the first complete canonical correction as \(3^rC_0\).

This is a no-go theorem for the naive lift only. It does not exclude a
backward construction with a different base correction or a genuinely
multi-state ancestry relation. It does show that shell atoms cannot be
treated as independently persistent virtual states: the intervening affine
injections are essential.

## 8. PCD6: affine-aware shells annihilate after one step

PCD5 omits the intervening affine injections. Putting them back does not
repair the multi-payout construction; instead, it exposes why a canonical
shell cannot persist to a later payout.

Let a high state after a payout have correction \(A\), cumulative valuation
\(F\), and canonical partner correction

\[
C=A+S(u,2h),\qquad F=u+2h.
\]

The partner's next valuation is larger than the high state's next valuation
by \(2h\), because

\[
3\left(4^hX+\frac{4^h-1}{3}\right)+1=4^h(3X+1).
\]

Consequently the correct affine injection for the partner correction is
\(2^{u+1}\), whereas the high correction receives \(2^{F+1}\). The shell
identity gives

\[
3S(u,2h)+2^{u+1}=2^{u+2h+1}=2^{F+1}.
\]

Therefore

\[
\boxed{
3C+2^{u+1}=3A+2^{F+1}.
}
\]

The two complete corrections are identical after one correctly aligned
affine step. This is the correction-coordinate form of the already known
odd-state merger, but it has an additional methodological consequence:

> **PCD6.** Every canonical collision shell is annihilated by its first
> correct affine transport. It cannot survive as an independent virtual
> correction to be paired with a later payout shell.

Thus there are only two choices. Transporting a shell as a homogeneous term
\(3^rS\) creates the formal PCD3--PCD4 fusion identities but does not follow a
complete correction state. Transporting the complete state with its correct
affine injection makes it merge with the high state immediately and leaves no
second shell at a later payout. This closes the canonical-shell version of
the proposed backward-state construction for all heights, not only the seven
short census patterns.

PCD6 does not rule out a noncanonical inverse branch, a state with additional
memory, or a construction pairing ancestors before their canonical mergers.
Those would be genuinely new mechanisms rather than refinements of the
current shell ledger.

## 9. PCD7: blocked effective count consumes valuation budget

Put

\[
Q_K=\sum_{t<K}(e_t-1)
=\sum_{\substack{t<K\\e_t>1}}(e_t-1).
\]

The deficit definition gives the exact valuation budget

\[
\boxed{
D_K+Q_K=K\log_2(3/2).
}
\]

Let \(M_B\) be the number of GPA2-blocked payouts before time \(K\). Every
such payout has \(e_t\equiv3,4\pmod6\), hence \(e_t-1\ge2\). If

\[
Q_B=\sum_{t\in\mathcal B}(e_t-1),
\]

then

\[
2M_B\le Q_B\le Q_K.
\]

The blocked effective count satisfies \(N_B\le M_B\) by Cauchy--Schwarz:

\[
\left(\sum_{t\in\mathcal B}p_t\right)^2
\le M_B\sum_{t\in\mathcal B}p_t^2.
\]

Combining these facts yields

\[
\boxed{
2N_B\le Q_B\le Q_K,
\qquad
D_K+2N_B\le K\log_2(3/2).
}
\]

Therefore:

> **PCD7.** Blocked diffusion has a universal amortized price. Every unit of
> blocked effective ancestry consumes at least two units of the valuation
> excess budget, and the remaining budget is exactly the current deficit.

In the diffuse branch of PCD1, \(N_B>1/\eta\), so immediately

\[
D_K<K\log_2(3/2)-\frac2\eta.
\]

This is only an additive improvement to the trivial linear deficit ceiling;
it does not bound \(D_K\) independently of \(K\). Its value is that it gives
the diffuse statistic an exact arithmetic consequence. A successful next
lemma must amplify this paid effective count using historical spacing,
primitivity, or correction-set geometry.

## 10. PCD8: balanced blocked spacing is not enough

PCD7 might suggest that many comparable blocked ancestors should force an
ever larger spacing cost. There is an explicit abstract valuation-word family
showing that this cannot follow from deficit levels and payout spacing alone.

Put

\[
c=\log_2(3/2),
\qquad
T_m=\left\lfloor\frac{2m}{c}\right\rfloor
\quad(m\ge1),
\qquad T_0=0.
\]

Because \(3<2/c<4\), every gap

\[
r_m=T_m-T_{m-1}
\]

is either \(3\) or \(4\). Construct a valuation word with a \(q=3\) payout
at each time \(T_m\), filling every intervening position with valuation one.
Between consecutive post-payout states, the deficit changes by

\[
r_mc-2.
\]

After the \(m\)-th payout its value relative to the initial state is exactly

\[
D_{T_m}-D_0=cT_m-2m.
\]

The floor definition gives

\[
-c<cT_m-2m\le0.
\]

Thus arbitrarily many blocked \(q=3\) payouts can have all their post-payout
deficit levels in one interval of width \(c<1\). Their ledger weights are

\[
w_m=\frac34,2^{-D_{T_m}},
\]

so the largest is less than \(2^c=3/2\) times the smallest. For \(M\) such
payouts,

\[
N_B
=\frac{(\sum_mw_m)^2}{\sum_mw_m^2}
\ge\frac{M}{(3/2)^2}
=\frac49M.
\]

The deficit throughout the balanced phase is uniformly bounded: between two
payouts there are at most three valuation-one steps. After any finite prefix,
append an arbitrarily long valuation-one run. Each appended step raises the
deficit by \(c\), so after a bounded transient the appended states are strict
records and their deficits are unbounded.

Therefore:

> **PCD8.** Abstract valuation words can have unbounded blocked effective
> ancestry concentrated in a sub-one-bit historical deficit band and still
> admit arbitrarily large later record deficits. No theorem using only payout
> counts, comparable ledger weights, historical deficit levels, and their
> spacing can turn PCD7 into a uniform deficit bound.

This is deliberately an abstract-word no-go. It does not assert that the
constructed words occur on primitive repunit tails. Rather, it proves that a
successful amplification must use precisely the data omitted by the
construction: repunit-cylinder realization, primitivity, correction-set
membership, or another arithmetic constraint of comparable strength.

## 11. PCD9: odd-repunit cylinders realize every compatible word

The PCD8 construction was stated first as an abstract valuation word. Its
compatible phase can in fact be placed on the odd repunit curve at every
finite depth.

Let \(\mathbf e=(e_0,\ldots,e_{K-1})\) be any positive valuation word of total
\(E\), and let \(r\pmod{2^{E+1}}\) be its unique odd starting-value residue.
The word begins with \(e_0\ge2\) exactly when

\[
r\equiv1\pmod4.
\]

An odd-indexed repunit \(a_n=(3^n-1)/2\) lies in this starting cylinder
exactly when

\[
3^n\equiv2r+1\pmod{2^{E+2}}.
\]

For \(E+2\ge3\), the subgroup generated by \(3\) modulo \(2^{E+2}\) has
order \(2^E\) and consists exactly of the units congruent to \(1\) or
\(3\pmod8\). If \(e_0\ge2\), then \(2r+1\equiv3\pmod8\), so the congruence
has a unique solution

\[
n\equiv n_0\pmod{2^E},
\]

and \(n_0\) is odd. Conversely, every odd \(n\) has
\(a_n\equiv1\pmod4\), so its first valuation is at least two. Therefore:

> **PCD9.** A finite positive valuation word is realised by an odd-indexed
> repunit tail if and only if its first valuation is at least two. When it is
> realised, exactly one odd exponent class modulo \(2^E\) realises it.

Start the balanced PCD8 language with a \(q=3\) payout and then use the same
mechanical gaps three and four. Every finite prefix, including any appended
terminal run of ones, begins with valuation three and hence has an odd
repunit-exponent cylinder. Thus PCD8 can be strengthened: for every finite
number of comparable blocked ancestors and every finite target record
deficit, some odd repunit exponent realises the corresponding prefix.

This still does not produce a primitive counterfamily. The least positive
exponent can be enormous, and the tail may descend or merge into a smaller
repunit tail before the terminal record. The exact lifted-discrete-log
diagnostic in scripts/explore_balanced_q3_cylinders.py computes these classes
without a table. Its first 40 balanced prefixes are all present, as PCD9
requires; this finite output is a regression check, not evidence for
primitivity.

## 12. PCD10: cylinder plateaus control exponent size

Let \(n_m\in[0,2^{E_m})\) be the least representative of the odd exponent
class realising the first \(m\) balanced payouts. Prefix nesting gives

\[
n_{m+1}\equiv n_m\pmod{2^{E_m}}.
\]

Consequently, either \(n_{m+1}=n_m\), or

\[
n_{m+1}\ge2^{E_m},
\qquad
\operatorname{bitlen}(n_{m+1})\ge E_m+1.
\]

Call a maximal consecutive interval on which \(n_m\) is constant a
**cylinder plateau**. In the balanced word, each new payout block has gap
three or four and adds a \(q=3\) payout, so its total-valuation increment is
at most six. If the plateau ending at \(m\) has length \(\ell\) and is not the
initial plateau, the most recent cylinder change gives

\[
\boxed{
\operatorname{bitlen}(n_m)\ge E_m-6\ell+1.
}
\]

Therefore:

> **PCD10.** If balanced-cylinder plateaus have a universal length bound
> \(L\), then
> \(\operatorname{bitlen}(n_m)\ge E_m-6L+1\). More generally, if their
> lengths are \(o(m)\), then
> \(\operatorname{bitlen}(n_m)/E_m\to1\).

Since \(E_m\) is linear in the balanced prefix length, either conclusion
makes the controlled prefix only logarithmic in its least exponent
representative. It would therefore prevent the PCD8 language from shadowing
a linear \(3n_m\) stopping window unless the same exponent remains on one
plateau for an exceptionally long time.

The exact lifted-discrete-log diagnostic finds, through the first \(300\)
balanced payout prefixes:

- every prefix has the PCD9 odd exponent class;
- the longest plateau has length \(2\);
- for \(m\ge10\), the minimum observed ratio
  \(\operatorname{bitlen}(n_m)/E_m\) is \(0.942029\), at \(m=26\).

These three bullets are a finite certificate, not a universal plateau bound.
PCD10 is the exact implication that explains why such a bound would matter.

A deeper exact run refutes the tempting extrapolation \(L=2\): the first
plateau of length three occurs at

\[
m=1198,1199,1200.
\]

Through \(m=1500\), the maximum observed plateau length is three. Thus the
live target should be sublinear plateau growth, not a universal bound of two.

## 13. PCD11: exact local cylinder extension

The deeper computation can be organized without enumerating all lifts. Let a
word of length \(K\), total valuation \(E\), starting residue
\(r\pmod{2^{E+1}}\), and correction \(c\) have canonical endpoint

\[
y=\frac{3^Kr+c}{2^E}.
\]

Append a suffix \(\mathbf v\) of total valuation \(\delta\), and let
\(s\pmod{2^{\delta+1}}\) be the suffix's unique starting residue. Every lift
of the old cylinder to the new modulus is

\[
r'=r+t2^{E+1},\qquad 0\le t<2^\delta.
\]

At the old endpoint this changes \(y\) to

\[
y+2t3^K.
\]

The lift realises the suffix exactly when this is congruent to \(s\) modulo
\(2^{\delta+1}\). Dividing the even difference by two and inverting the odd
number \(3^K\) gives the unique solution

\[
\boxed{
t\equiv
\frac{s-y}{2}\,3^{-K}
\pmod{2^\delta}.
}
\]

For the corresponding exponent cylinder, write

\[
n'=n+z2^E,qquad0\le z<2^\delta.
\]

Then \(z\) is the unique bounded discrete logarithm satisfying

\[
3^n\left(3^{2^E}\right)^z
\equiv2r'+1\pmod{2^{E+\delta+2}}.
\]

The generator can be updated without large exponentiation. If

\[
3^{2^k}=1+2^{k+2}h_k,
\]

then

\[
\boxed{h_{k+1}=h_k+2^{k+1}h_k^2.}
\]

Modulo any fixed power of two, \(h_k\) stabilizes once \(k\) is large enough.
Therefore:

> **PCD11.** Extending a valuation cylinder by a suffix of total valuation
> \(\delta\) requires one linear congruence modulo \(2^\delta\) for the
> starting-value lift and one discrete logarithm in a cyclic group of order
> \(2^\delta\) for the exponent lift. The displayed recurrences are exact.

For the balanced blocks, \(\delta\in\{5,6\}\), so every extension is a
uniformly bounded local calculation even when the accumulated cylinder is
very deep. This is what makes the \(m=1500\) plateau certificate practical.

## 14. PCD12: the local lift alphabet is full

Applying PCD11 through the first \(1500\) balanced payout prefixes gives
\(1499\) local exponent lifts. Separating them by suffix valuation yields:

| suffix valuation \(\delta\) | extensions | occupied lifts | zero lifts | count range |
|---:|---:|---:|---:|---:|
| 5 | 871 | 32 of 32 | 32 | 20--42 |
| 6 | 628 | 64 of 64 | 7 | 3--18 |

The same run has plateau histogram

\[
\{1:1423,\ 2:37,\ 3:1\}.
\]

This proves only the finite statement:

> **PCD12.** Through \(m=1500\), every possible 5-bit and 6-bit exponent
> lift occurs. The zero lift occurs \(39\) times, producing \(37\) plateaus
> of length two and one plateau of length three.

The counts are broadly compatible with a uniform heuristic, but no
independence, discrepancy, or equidistribution theorem is asserted. The full
alphabet rules out the simplest finite forbidden-residue approach to plateau
control. Any deterministic proof must use correlations between successive
lifts, not exclusion of individual lift values.

## 15. PCD13: the plateau carry cocycle

PCD11 can be linearized one step further. Suppose the old exponent cylinder is

\[
n\pmod{2^E},
\]

with starting residue \(r\), and append a suffix of total valuation
\(\delta\). Let \(t\pmod{2^\delta}\) be the PCD11 starting-cylinder lift, so

\[
r'=r+t2^{E+1}.
\]

Define the higher exponent carry

\[
\kappa
=\frac{3^n-(2r+1)}{2^{E+2}}
\pmod{2^\delta}.
\]

This is well defined because \(3^n\equiv2r+1\pmod{2^{E+2}}\). Write the new
exponent representative as

\[
n'=n+z2^E,qquad z\pmod{2^\delta}.
\]

Using

\[
3^{2^E}=1+2^{E+2}h_E
\]

and assuming \(E+2\ge\delta\), all quadratic binomial terms vanish modulo
\(2^{E+\delta+2}\). Hence

\[
3^{n'}
\equiv
(2r+1)+
2^{E+2}\left(\kappa+zh_E(2r+1)\right)
\pmod{2^{E+\delta+2}}.
\]

The new target is

\[
2r'+1=(2r+1)+t2^{E+2}.
\]

Since \(h_E\) and \(2r+1\) are odd, comparison gives the exact lift

\[
\boxed{
z\equiv
(t-\kappa)\left[h_E(2r+1)\right]^{-1}
\pmod{2^\delta}.
}
\]

Therefore:

> **PCD13.** Once \(E+2\ge\delta\), the exponent lift is the displayed linear
> function of the starting-cylinder lift and exponent carry. In particular,
> a cylinder plateau occurs exactly when
> \[
> \boxed{t=\kappa\pmod{2^\delta}.}
> \]

The implementation checks this identity on every balanced extension. It
replaces the local discrete logarithm by one subtraction and one inversion.
Conceptually, it identifies the real problem: plateau runs are consecutive
coincidences between two coupled digit streams, \(t_m\) from the affine
endpoint recursion and \(\kappa_m\) from higher power-of-three digits.

## 16. PCD14: a plateau shifts one fixed carry

The PCD13 carry can be taken as a full nonnegative integer:

\[
C=\frac{3^n-(2r+1)}{2^{E+2}}.
\]

After a suffix of total valuation \(\delta\), with starting lift \(t\) and
exponent lift \(z\), set

\[
G_E(z)=\frac{(3^{2^E})^z-1}{2^{E+2}}.
\]

Using \(3^{n+z2^E}=3^n(1+2^{E+2}G_E(z))\) and
\(2r'+1=(2r+1)+t2^{E+2}\), the new full carry is exactly

\[
\boxed{
C'=\frac{C-t+3^nG_E(z)}{2^\delta}.
}
\]

On a plateau \(z=0\), so PCD13 guarantees
\(C\equiv t\pmod{2^\delta}\) and

\[
\boxed{C'=\frac{C-t}{2^\delta}.}
\]

Thus a plateau removes the matched low \(\delta\) bits from one fixed carry
attached to the unchanged exponent. For \(\ell\) plateau extensions with
block sizes \(\delta_1,\ldots,\delta_\ell\) and starting lifts
\(t_1,\ldots,t_\ell\), iteration gives

\[
C\equiv
t_1+2^{\delta_1}t_2+\cdots+
2^{\delta_1+\cdots+\delta_{\ell-1}}t_\ell
\pmod{2^{\delta_1+\cdots+\delta_\ell}}.
\]

Therefore:

> **PCD14.** A plateau run is exactly a match between consecutive low-bit
> blocks of one fixed power-of-three carry and the concatenated affine
> starting-cylinder lifts.

The coincidences in PCD13 are therefore not independent local events. Across
one plateau they compare a single contiguous carry block with a word produced
by successive affine endpoint maps.

## 17. PCD15: fixed-width endpoint compression is not closed

For the two balanced suffixes, direct calculation gives

\[
\begin{array}{c|c|c|c}
\text{suffix}&\delta&c(\mathbf v)&s\pmod{2^{\delta+1}}\\
\hline
(1,1,3)&5&19&55\pmod{64}\\
(1,1,1,3)&6&65&79\pmod{128}.
\end{array}
\]

If the current canonical endpoint is \(y\) after \(K\) steps, PCD11 becomes

\[
t\equiv\frac{s-y}{2}3^{-K}\pmod{2^\delta}.
\]

The corresponding successor endpoint is

\[
F_{\mathbf v}(y,t)
=\frac{3^{|\mathbf v|}(y+2t3^K)+c(\mathbf v)}{2^\delta}.
\]

Fix any residue width \(M\ge\delta+1\). The endpoints \(y\) and
\(y+2^M\) are identical modulo \(2^M\), and their lift parameters are equal.
Both lifted states realise the same suffix. But their successors differ by

\[
\boxed{
F_{\mathbf v}(y+2^M,t)-F_{\mathbf v}(y,t)
=3^{|\mathbf v|}2^{M-\delta},
}
\]

which is nonzero modulo \(2^M\). Therefore:

> **PCD15.** No state consisting only of the Sturmian phase and a fixed-width
> residue \(y\pmod{2^M}\) has a well-defined successor residue of the same
> width for the balanced affine-lift dynamics. Every block consumes
> \(\delta\in\{5,6\}\) previously unseen high bits.

A viable transducer must replenish its endpoint window from the carry stream,
use a growing state, or prove a separate restriction on the missing high
bits. The obstruction is exact and holds at every fixed width.

## 18. PCD16: balanced blocks have bounded real distortion

The two balanced blocks act by

\[
\Phi_3(x)=\frac{27x+19}{32},
\qquad
\Phi_4(x)=\frac{81x+65}{64}.
\]

Consider any consecutive interval of \(L\) blocks in the mechanical word

\[
T_m=\left\lfloor\frac{2m}{c}\right\rfloor,
\qquad c=\log_2(3/2).
\]

If \(R=T_{m+L}-T_m\) is the total number of odd steps in those blocks,
their composition has the form

\[
\Phi_W(x)=\frac{3^R x+B_W}{2^{R+2L}},
\qquad B_W>0.
\]

Its homogeneous multiplier is

\[
\mu_W=\frac{3^R}{2^{R+2L}}=2^{cR-2L}.
\]

The floor discrepancy gives

\[
\left|R-\frac{2L}{c}\right|<1,
\]

so \(\lvert cR-2L\rvert<c\). Since \(2^c=3/2\), this proves

\[
\boxed{\frac23<\mu_W<\frac32.}
\]

Therefore:

> **PCD16.** Every consecutive balanced mechanical block composition has
> homogeneous multiplier strictly between \(2/3\) and \(3/2\), independently
> of its length.

The balanced system is a real near-isometry at every scale. Thus neither
exponential Archimedean contraction nor exponential expansion can control
the plateau length. Any successful argument must exploit arithmetic
transversality between endpoint and carry digits, rather than the sizes of
the affine derivatives alone.

## 19. PCD17: balanced correction storage grows linearly

The normalized ledger coordinate from the extremal principle is

\[
Z_K=\frac{R_K}{2^{E_K+1}},
\qquad
Z_{K+1}=1+\frac{3Z_K-2}{2^{e_K}}.
\]

Consequently, the two balanced blocks act on \(Z\) by

\[
\Psi_3(Z)=\frac{27}{32}Z+\frac34,
\qquad
\Psi_4(Z)=\frac{81}{64}Z+\frac34.
\]

Start immediately after the initial valuation-three payout, where
\(Z_0=15/16\), and append \(L\ge1\) mechanical balanced blocks. If
\(\mu_{i,L}\) is the homogeneous multiplier transporting the injection at
block \(i\) through the remaining suffix, then

\[
Z_L=\mu_{0,L}Z_0+\frac34\sum_{i=1}^{L}\mu_{i,L},
\qquad \mu_{L,L}=1.
\]

Every nonempty suffix is itself a consecutive mechanical interval, so PCD16
gives \(2/3<\mu_{i,L}<3/2\). Therefore

\[
\frac23Z_0+\frac34\left(1+(L-1)\frac23\right)
<Z_L<
\frac32Z_0+\frac34\left(1+(L-1)\frac32\right).
\]

Substituting \(Z_0=15/16\) yields

\[
\boxed{
\frac{L}{2}+\frac78
<Z_L<
\frac{9L}{8}+\frac{33}{32}.
}
\]

Therefore:

> **PCD17.** Along the balanced \(q=3\) obstruction, normalized correction
> storage grows linearly in the number of appended payout blocks.

This is a useful but deliberately limited conclusion. It shows that the raw
ledger coordinate cannot belong to a compact finite-state model; only a
renormalized coordinate such as \(Z_L/L\) can remain bounded. It does not
bound the PCD14 power-of-three carry, which may be vastly larger and still
controls cylinder plateaus.

## 20. Next symbolic target

For a blocked-concentrated record, pair the dominant blocked ancestor with the
largest remaining ancestor and transport both corrections to one diagonal.
The first question is whether their combined target correction remains zero
modulo \(3\), becomes a source-admissible nonzero class, or forces one of the
two-shell exponential equations already derived in the primitive ancestry
note.

For the blocked-diffuse branch, begin with the exact \(n=471\) profile and test
all pairs among its four blocked ancestors. Any proposed pair lemma must then
be tested against the concentrated examples \(n=3881\) and \(n=3105\), which
contain both \(q=3\) and \(q=4\) atoms.

PCD6 shows that inserting the correct affine injection makes each canonical
partner collapse into the high path after one step. A viable two-ancestor
construction must therefore use a noncanonical inverse branch or retain new
state beyond a canonical correction and its shell height.

PCD9 shows that repunit-cylinder realization alone imposes no further finite
restriction once the first valuation is at least two. The next lemma must
therefore use global information absent from a cylinder: prior descent,
merger into a smaller repunit tail, or a quantitative lower bound on the least
positive exponent representative relative to the balanced prefix length.

PCD10 makes a sublinear plateau theorem the immediate target for the
quantitative bound. For qualitative eventual descent, IEF10 already excludes
the exact infinite mechanical itinerary and IEF11 excludes all its fixed
phase shifts. IEF12 goes further and excludes every Sturmian intercept at the
critical slope. The missing qualitative step is now classification: show
that every infinite blocked-diffuse terminal branch is Sturmian, satisfies
the IEF11 periodic-prefix criterion by another mechanism, or name the
distinct non-Sturmian residual language it enters.

IEF13 makes "another mechanism" explicit. Uniformly bounded critical factor
discrepancy and \(\operatorname{dio}(w)>1\) already suffice. In particular,
all bounded-discrepancy languages of linear factor complexity are discharged.
Hence the qualitative PCD classification should record two new residual
flags: growing factor discrepancy and superlinear factor complexity.

IEF14 refines the first flag: growing discrepancy is discharged whenever the
periodic-prefix agreement surplus \(G\) beats \(2K+2\log_2N\). The remaining
PCD ledger should therefore retain this adaptive margin, not discrepancy in
isolation.

For negative discrepancy, also retain the IEF15 suffix partition
\(Z_L=1+2^{cr_L-2}Z_{L-1}\). Deep negative drift with bounded \(Z_L\) is a
finite discharge, so a surviving high-discrepancy ledger must show why this
partition function replenishes.

Finally, IEF16 forces \(\liminf S_L/L=0\) on any rational non-cyclic survivor.
The PCD ledger can therefore discard linear density drift of either sign and
reserve the carry analysis for sublinear or critical-envelope fluctuations.

IEF17 is the resulting terminal ledger. Any non-cyclic PCD survivor must meet
all five of its coordinates simultaneously; new carry or ancestry rules
should be measured against that intersection rather than against the original
blocked-diffuse population.

IEF18 sharpens the ledger's periodic-prefix coordinate: the rational height
depends on total and suffix-positive drift of the chosen preperiod and period,
not on the full symmetric factor discrepancy. Thus a PCD branch survives this
axis only if every useful approximant has bounded directional margin
\(G-J(A)-J(B)-2\log_2N\).

IEF19 gives the corresponding asymptotic split. Sublinear cumulative drift
and repetition exponent greater than one force that directional margin to
diverge. Hence a non-cyclic PCD survivor must have repetition exponent one or
positive linear limsup drift, in addition to satisfying the remaining ledger
coordinates.

IEF20 reaches into the positive-limsup side: fixed-surplus repetitions are
still discharged if they recur at scales where the entire earlier drift
envelope is sublinear relative to the new footprint. The complementary PCD
branch must keep every useful recurrence scale coupled to a directionally
visible excursion. Exponent one separately forces superlinear factor
complexity, but no ancestry theorem here yet rules that out.

IEF21 computes that directional visibility exactly. The height cost of a full
block factor is its terminal draw-up from the factor minimum; the agreement
surplus separately pays only for drift lost after the footprint. Thus a PCD
survivor must retain a linear terminal draw-up or linear endpoint loss on
every fixed-surplus approximant. An internal high-drift phase that returns to
the relevant valley before the cut is discharged rather than residual.

The uniform proposal \(L=2\) is refuted at \(m=1200\), and random-like exponent
digits would be expected to have unbounded but logarithmic plateaus. PCD11
reduces each plateau decision to a bounded local exponent lift. For the
quantitative target, view PCD13--PCD14 as a word-matching cocycle driven by the mechanical gap word.
The gap sequence is the Sturmian coding of the rotation defined by
\(T_m=\lfloor2m/c\rfloor\). Seek a deterministic bound on consecutive
equalities \(t_m=\kappa_m\), such as \(O(\log m)\), or anything \(o(m)\).
PCD12 shows that the argument must control correlations; it cannot assume
digit independence or forbid zero locally. A useful route would be a
Baker-type non-shadowing estimate or a carry-augmented transducer. PCD15 rules
out a fixed-width endpoint-only machine: it must explicitly model how carry
bits replenish the window. PCD16 also rules out extracting a long-scale real
contraction from the balanced word: arithmetic separation must do the work.
PCD17 shows that normalized ledger storage itself grows linearly, so an
induced record state must either retain this unbounded scale or normalize it
without losing the carry/endpoint coupling.
Mechanical pairing of canonical shell atoms stops here.

## 21. Reproduction

    python scripts/explore_payout_concentration.py --limit 5001 --top 0
    python scripts/explore_mixed_shell_pairs.py --limit 5001 --top 100
    python scripts/explore_balanced_q3_cylinders.py --payouts 40 --show 40
    python scripts/explore_balanced_q3_cylinders.py --payouts 1500 --show 3

| ID | Claim | Status | Verification |
|---|---|---|---|
| PCD1 | The exact initial/eligible/blocked trichotomy and blocked concentration-effective-count alternative hold for every payout ledger | Proved here | Positivity, normalization, pigeonhole, and the displayed square-sum inequality |
| PCD2 | Through odd \(n\le5001\), the \(110\) primitive records with \(D_K\ge2\) split \(88/0/16/6\) across the four ordered branches, and all six diffuse records belong to \(n=471\) | Finite certificate | Exact integer comparisons in scripts/explore_payout_concentration.py |
| PCD3 | Consecutive \(q=3\) canonical shells satisfy \(S(E+4,2)-3S(E+1,2)=S(E+1,4)\) | Proved here | Direct shell algebra; scripts/verify_repunit_general_payout_ancestry.py |
| PCD4 | The six displayed mixed blocked/eligible valuation blocks have exact shell-fusion identities; they account for all \(43\) mixed fusions among \(671\) distinct pairs in the dangerous primitive census through \(n=5001\) | Proved identities plus finite classification | Direct algebra; scripts/verify_repunit_general_payout_ancestry.py and scripts/explore_mixed_shell_pairs.py |
| PCD5 | None of the seven short mixed-fusion blocks lifts to a collision under the naive complete-correction transport \(C_r-3^rC_0\) | Proved here | Exact affine recurrences; scripts/verify_repunit_general_payout_ancestry.py |
| PCD6 | Every canonical shell correction becomes the original high correction after one correctly aligned affine step, so it cannot persist as an independent state for later shell pairing | Proved here | One-step correction identity; scripts/verify_repunit_general_payout_ancestry.py |
| PCD7 | The blocked effective count obeys \(2N_B\le Q_B\le Q_K\), hence \(D_K+2N_B\le K\log_2(3/2)\) | Proved here | Cauchy--Schwarz, minimum blocked-payout cost, and the exact deficit budget; scripts/verify_repunit_general_payout_ancestry.py |
| PCD8 | There are abstract valuation words with \(M\) blocked \(q=3\) payouts in a historical deficit band of width \(\log_2(3/2)\), \(N_B\ge4M/9\), and arbitrarily large later record deficits | Proved here | Mechanical floor construction; scripts/verify_repunit_general_payout_ancestry.py checks finite prefixes |
| PCD9 | A finite positive valuation word of total \(E\) is realised by exactly one odd repunit exponent class modulo \(2^E\) iff its first valuation is at least two | Proved here | Power-of-three subgroup modulo \(2^{E+2}\); scripts/verify_repunit_general_payout_ancestry.py |
| PCD10 | A balanced-cylinder change forces \(n_{m+1}\ge2^{E_m}\); hence a plateau bound \(L\) gives \(\operatorname{bitlen}(n_m)\ge E_m-6L+1\); the proposed universal value \(L=2\) first fails at the plateau \(m=1198,1199,1200\) | Proved implication plus finite refutation | Nested exponent classes; scripts/explore_balanced_q3_cylinders.py |
| PCD11 | Appending a suffix of total valuation \(\delta\) gives the unique starting-cylinder lift by the displayed linear congruence modulo \(2^\delta\), followed by a bounded exponent lift using the displayed normalized-power recurrence | Proved here | Exact affine cylinder algebra; scripts/explore_balanced_q3_cylinders.py |
| PCD12 | Through \(m=1500\), all \(32\) five-bit and all \(64\) six-bit exponent lifts occur; zero occurs \(39\) times and the plateau histogram is \(\{1:1423,2:37,3:1\}\) | Finite certificate | scripts/explore_balanced_q3_cylinders.py |
| PCD13 | For \(E+2\ge\delta\), the exponent lift is \(z\equiv(t-\kappa)[h_E(2r+1)]^{-1}\pmod{2^\delta}\); a plateau occurs exactly when \(t=\kappa\pmod{2^\delta}\) | Proved here | Binomial truncation modulo \(2^{E+\delta+2}\); checked on every extension by scripts/explore_balanced_q3_cylinders.py |
| PCD14 | During a plateau the full carry obeys \(C'=(C-t)/2^\delta\); a plateau run therefore matches consecutive carry bits against the concatenated affine starting lifts | Proved here | Exact full-carry algebra and iteration |
| PCD15 | For either balanced suffix and every fixed width \(M\ge\delta+1\), endpoints equal modulo \(2^M\) have the same lift but successors differing by \(3^{|\mathbf v|}2^{M-\delta}\not\equiv0\pmod{2^M}\); fixed-width endpoint state is not closed | Proved here | Exact affine transition; scripts/verify_repunit_general_payout_ancestry.py |
| PCD16 | Every consecutive interval of the balanced mechanical block word has homogeneous multiplier \(\mu_W\) satisfying \(2/3<\mu_W<3/2\), independently of its length | Proved here | Mechanical floor discrepancy; scripts/verify_repunit_general_payout_ancestry.py |
| PCD17 | After the initial valuation-three payout and \(L\ge1\) balanced mechanical blocks, normalized correction storage satisfies \(L/2+7/8<Z_L<9L/8+33/32\) | Proved here | Affine storage recursion plus PCD16; scripts/verify_repunit_general_payout_ancestry.py |
