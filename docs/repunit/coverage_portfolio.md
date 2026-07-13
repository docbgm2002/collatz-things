# A Coverage Portfolio for the Repunit-Tail Problem

**Status:** Research framework. This note proves only the elementary portfolio
lemma below. It does not prove universal repunit-tail descent. Percentages
quoted from finite certificates are diagnostics, not asymptotic claims.

## 1. Target and motivation

For odd (n>1), put

\[
a_n=\frac{3^n-1}{2},
\qquad M_n=2^n-1,
\]

and let (P(n)) be the statement that some accelerated iterate of (a_n)
is below (M_n).

A proof of every (P(n)) need not use one uniform mechanism. It may use a
portfolio of rules, provided that the rules are individually sound and their
domains cover every case. Percentages are useful for discovering and
prioritizing such rules, but they are not the covering argument.

## 2. Exact portfolio lemma

Let (U) be a well-ordered set of cases. For each rule (i), let (R_i(x))
be its applicability predicate. Suppose:

1. for every (x\in U), at least one (R_i(x)) holds;
2. whenever (R_i(x)) holds, the rule either proves (P(x)) directly or
   reduces it to (P(y)) for some (y<x).

Then (P(x)) holds for every (x\in U).

This is immediate by well-founded induction. Rules may overlap, and no
density calculation is needed once exhaustive coverage is proved.

For repunit tails, an exact merge into the trajectory of a smaller exponent
is an inductive discharge rule. A direct fall below (M_n) is a direct
discharge rule. A classification, density theorem, or finite observation is
not a discharge rule unless it supplies one of those implications.

## 3. Why percentages alone do not close the proof

Three percentages summing to (100\%\) need not describe a cover because the
rules may remove the same cases. Even a proved union of natural density one
may leave an infinite exceptional set. The rail-(5) survivor set is an
explicit warning in this repository: it has measure zero and positive
(2)-adic Hausdorff dimension, and positive-integer membership beyond the
trivial index remains open.

There are three safe ways to use percentages:

1. **Disjoint partition:** define mutually exclusive predicates and prove
   that their union is the whole universe.
2. **Residual accounting:** after rule (i), measure its conditional coverage
   only on the cases not discharged by earlier rules.
3. **Recursive cover:** prove that every residual branch either terminates or
   decreases a well-founded rank. The displayed percentages then measure the
   efficiency of the proof tree, not its validity.

All rules compared at one stage must also have the same universe. This
repository reports percentages of exponents, tails, active states, strict
record prefixes, episodes, mergers, and payout-ledger mass. Those quantities
cannot be added to one another. They belong at different levels of a
hierarchical cover.

A finite-modulus residue cover is a special case of the first method. The
corridor-rate theorem shows why direct forced-descent residue rules alone are
unlikely to give a small finite cover: their undischarged frontier grows with
branching factor (1.9318\ldots). A portfolio can still work if structurally
different rules discharge that frontier.

## 4. Current rule inventory

| mechanism | exact logical role | present coverage status |
|---|---|---|
| direct descent | proves (P(n)) | bounded computation only for the full repunit family |
| same-diagonal merge | reduces (P(n)) to a smaller exponent | exact when a merge is found; (4783/4998=95.70\%\) through odd (7\le n\le10001), but no universal coverage theorem |
| rail-(5) hitting | gives a strict next-step decrease of the current state | density one for eventual hitting, but does not by itself imply a fall below (M_n) |
| fixed-enemy Baker non-shadowing | bounds one structured low-valuation shadow | universal on its stated branch, not a classification of every primitive tail |
| REPANC/GPA correction equality | forces a merge to a smaller repunit tail | universal conditional rule; no theorem says every eligible correction matches |
| PCD1 ledger trichotomy | partitions record ledgers into eligible, initial, blocked-concentrated, and blocked-diffuse branches | exhaustive classification, but its branches are not yet discharge rules |
| balanced (q=3) cylinders | exhibit the hard blocked residual family | every finite prefix is realized; the needed plateau non-shadowing theorem remains open |

This table changes the interpretation of the headline percentages. The
finite (95.70\%\) merger rate is genuinely suggestive because merger is a
sound inductive mechanism. The rail-(5) density and the PCD branch shares
measure useful structure, but they are not percentages of cases already
proved to satisfy (P(n)).

### Bounded residual ledgers already available

The merger certificate gives a genuine ordered ledger on its finite domain:

| stage | newly discharged | residual |
|---|---:|---:|
| odd (7\le n\le10001) | -- | (4998) |
| exact merge into a smaller tail | (4783) | (215) |
| exact computed first descent of a primitive tail | (215) | (0) |

This exhausts only the printed finite domain. The second row has the desired
inductive proof shape; the third is bounded trajectory computation, not a
uniform symbolic rule.

PCD2 supplies a different, also disjoint, residual ledger for the (110)
dangerous primitive record prefixes through (n=5001):

| ordered PCD1 branch | records |
|---|---:|
| eligible mass at least (1/3) | (88) |
| initial mass at least (1/3), after removing eligible | (0) |
| blocked-concentrated | (16) |
| blocked-diffuse | (6) |

These four rows really do exhaust that finite record set without overlap,
because they are evaluated in order. They are classifications rather than
discharges. This is currently the cleanest scaffold for the proposed
multi-rule proof: replace each classification row by one or more sound rules,
and recompute the residual after every addition.

## 5. Proposed covering architecture

The natural hierarchy is:

\[
\text{odd exponent}
\longrightarrow
\begin{cases}
\text{direct descent},\\
\text{merge to a smaller exponent},\\
\text{primitive residual tail},
\end{cases}
\]

followed, on the primitive residual, by a partition of the relevant strict
record prefixes. In a minimal-counterexample proof, the merge branch is
automatically discharged by induction: every smaller exponent already
descends. The remaining counterexample must therefore stay in the primitive
branch, where PCD1 can be applied to each dangerous record ledger.

Work at a strict primitive record-deficit prefix and apply the following
ordered rules. The order makes all reported percentages conditional on the
current residual set.

1. **Merge discharge.** Remove every prefix that has already merged into a
   smaller repunit tail.
2. **Reachable-ancestry discharge.** In the GPA-eligible ledger branch, seek a
   correction equality and apply GPA1.
3. **Controlled-height discharge.** Send a precisely quantified low-height
   enemy family to a Baker or Archimedean non-shadowing estimate.
4. **Blocked concentration discharge.** Pair dominance with record
   extremality to force either a noncanonical smaller ancestor or a bound on
   the subsequent record deficit.
5. **Blocked diffusion discharge.** Use the exact PCD7 valuation charge. If
   the history is the deterministic infinite balanced \(q=3\) obstruction,
   invoke IEF10 for qualitative exclusion. IEF11 also excludes every fixed
   phase shift and any other aperiodic language with sufficiently deep,
   controlled-height periodic approximants. IEF12 applies this rule to every
   Sturmian intercept at the critical slope. IEF13 discharges the wider class
   with bounded critical factor discrepancy and Diophantine exponent greater
   than \(1\), including all such words of linear factor complexity. For a
   quantitative stopping bound, a plateau-rate theorem is still required.
   IEF14 also covers growing discrepancy when agreement surplus beats twice
   the local discrepancy budget. Otherwise route the survivor to the bounded
   adaptive-margin or superlinear-complexity ledger. IEF15 separately sends
   sustained negative drift with bounded suffix partition to a finite check.
   IEF16 removes either sign of nonzero linear lower drift outright.

The desired theorem is not that these five rules have empirical percentages
adding to (100\%\). It is the exhaustive implication

\[
\text{primitive record}
\Longrightarrow
R_{\rm ancestry}\lor R_{\rm lowheight}\lor
R_{\rm concentrated}\lor R_{\rm balanced},
\]

followed by one sound discharge lemma for each predicate.

PCD1 already supplies the beginning of this partition. The balanced family
shows what the final residual predicate must retain: finite valuation-cylinder
membership is too weak, so the cover state must include least exponent,
primitivity or prior merger, and the PCD13 power-of-three carry.

## 6. Coverage ledger protocol

For every proposed rule, record:

- its exact applicability predicate;
- whether it proves descent, proves a smaller-exponent merge, or merely
  classifies a case;
- its dependencies and quantifiers;
- overlap with earlier rules;
- its conditional finite coverage on the current residual set;
- the smallest uncovered example;
- the symbolic description of the residual family.

A computational coverage report should output both a Venn-style overlap
count and an ordered residual count. It must never label a density result,
classification, or empirically observed recovery as a proof discharge.

## 7. Immediate research consequence

The portfolio viewpoint supports the present roadmap rather than replacing
it. Most easy finite cases are already absorbed by mergers. The remaining
work is to turn the PCD partition into discharge rules. IEF10 supplies the
qualitative terminal rule for the exact deterministic balanced word, while
IEF11 turns its proof into a reusable periodic-prefix rule and closes all
fixed phase shifts. IEF12 closes the entire Sturmian subshift at the critical
slope, and IEF13 supplies the exact discrepancy--repetition split beyond it.
IEF14 makes that split adaptive rather than merely bounded/unbounded.
IEF15 supplies a real-drift discharge for the negative side.
IEF16 first restricts every rational non-cyclic survivor to density-critical
lower drift \(\liminf S_L/L=0\).
IEF17 records the resulting five-coordinate intersection and is now the
canonical terminal residual ledger. New rules should shrink that intersection
rather than recount already-overlapping branches. IEF18 does so on the
periodic-prefix coordinate: it replaces the symmetric \(2K\) cost by the
smaller directional cost \(J(A)+J(B)\), with IEF14 retained as a corollary.
IEF19 converts that improvement into a cleaner terminal split: sublinear
prefix drift plus repetition exponent greater than one is discharged, so a
non-cyclic survivor has exponent one or positive linear drift excursions.
IEF20 then reaches into the second branch by discharging fixed-surplus
repetitions whose full preceding drift envelope is sublinear at the footprint
scale. Thus positive limsup alone is not residual protection; the excursions
must remain directionally visible at every useful recurrence scale.
IEF21 identifies "directionally visible" exactly: the two preperiod/period
cuts must retain a linear terminal draw-up, or the agreement endpoint must
lose linear drift after the footprint. Internal peaks followed by returns to
the relevant local valleys do not protect a branch.
The narrowest missing portfolio statement is:

> Prove that every infinite blocked-diffuse terminal branch is discharged by
> IEF13--IEF21 or lies in the exact residual union
> \(\operatorname{dio}(w)=1\) or \(\limsup S_L/L>0\), while also keeping the
> IEF18 directional margin bounded along every useful approximant; then
> discharge that intersection.

For the stronger quantitative target, the former task remains: bound balanced
cylinder plateau length using the coupled endpoint and carry, with enough
primitivity or prior-descent information to exclude the finite-cylinder
tautology.

`integral_escape_frontier.md` weakens the terminal requirement when the goal
is universal eventual descent rather than an explicit linear stopping bound.
The full \(2\)-adic residual need not be empty: it is enough to prove that
every infinite residual branch has infinitely many nonzero exponent-lift
blocks. By IEF1, a positive integer would instead force its canonical exponent
representatives to become permanently constant. This turns the final cover
condition from "no infinite survivor" into "no eventually-zero integral
survivor."

IEF10 proves this non-integral-survivor statement for the deterministic
balanced itinerary, and IEF12 extends it to the whole critical-slope Sturmian
family. IEF13 extends it to a broad non-Sturmian class. This is a substantial
portfolio discharge, not evidence that the remaining high-discrepancy or
low-repetition residual union is empty.
