# Noncanonical Shell-Fan Ancestry

**Status:** NSF1--NSF3 are proved here and checked by
`scripts/verify_noncanonical_shell_fan.py`; NSF4 is a finite certificate.
Closed as a main proof avenue after the literature gate in Section 8.  The
fan-capacity statement in Section 6 is retained as a reopening condition, not
an active claim.

**Building on:** GAPMRG1, REPANC1--REPANC3, GPA1--GPA2.

## 1. Motivation

GPA2 rules out the canonical shell partner when the payout satisfies

\[
q\equiv3,4\pmod6.
\]

That obstruction includes the dominant dangerous payout \(q=3\).  It does
not, however, rule out the other odd partners of the same successor.  If
\(X\) is odd, then for every \(h\ge1\)

\[
Y_h=4^hX+\frac{4^h-1}{3}
\]

is odd and satisfies

\[
3Y_h+1=4^h(3X+1),\qquad f(Y_h)=f(X).
\]

The canonical choice \(h=\lfloor q/2\rfloor\) is only one member of this
shell fan.  The purpose of this note is to retain every member whose lower
cumulative valuation can support an aligned smaller repunit source.

## 2. Exact shell fan

Suppose a realised high repunit tail has pre-payout step count \(j\),
cumulative valuation \(E\), payout \(q=e_j\ge2\), and post-payout state

\[
X=x_{j+1}(n)
=\frac{3^d+A_{j+1}}{2^{F+1}},
\qquad
d=n+j+1,
\qquad
F=E+q.
\]

For any integer \(h\ge1\) with \(u_h=F-2h\ge0\), put

\[
T_h=\frac{4^h-1}{3},
\qquad
C_h=A_{j+1}+2^{u_h+1}T_h.
\]

Then

\[
\boxed{3^d+C_h=2^{u_h+1}Y_h}.
\]

This is the same collision shell as GAPMRG1, viewed at every possible lower
valuation rather than only at the payout's canonical height.

> **NSF1 (exact shell fan).** Every \(h\ge1\) with \(u_h\ge0\) gives the odd
> shell partner \(Y_h\), the displayed correction \(C_h\), and
> \(f(Y_h)=f(X)\).

## 3. Automatic smaller-tail realisation

Let \(\mathbf v\) be a positive valuation word of length \(i\), total
valuation \(u_h\), and correction \(A_i(\mathbf v)\).  If

\[
A_i(\mathbf v)=C_h,
\]

set \(m=d-i\).  Exactly as in GPA1,

\[
3^ia_m+c(\mathbf v)
=\frac{3^d+C_h}{2}
=2^{u_h}Y_h.
\]

Since \(Y_h\) is odd, the accumulated numerator has exact valuation \(u_h\).
The exact-itinerary criterion forces \(a_m\) to realise \(\mathbf v\), with

\[
f^i(a_m)=Y_h.
\]

The source is a positive smaller odd exponent precisely under the familiar
alignment conditions

\[
\boxed{
j+2\le i\le\min(u_h,d-1),
\qquad i\equiv j+1\pmod2.
}
\]

> **NSF2 (fan realisation).** A correction match for any shell-fan height at
> an admissible aligned source length realises the complete smaller repunit
> word and forces a next-step merge.  For a fixed high valuation cylinder,
> match or nonmatch depends only on the word; every sufficiently large
> exponent representative inherits each match.

Because the parity condition excludes \(i=j+2\), the useful fan heights are

\[
\mathcal H(E,j,q)
=\{h\ge1:E+q-2h\ge j+3\}.
\]

The source-length condition, not the identity \(f(Y_h)=f(X)\), makes the fan
finite.

## 4. The canonical modulo-three obstruction is not stable

The post-payout correction satisfies

\[
A_{j+1}=3A_j+2^{E+1}.
\]

Modulo \(3\), therefore,

\[
C_h
\equiv
2^{E+1}\left(1+2^{q-2h}T_h\right)
\equiv
2^{E+1}\left(1+2^qT_h\right).
\]

Here a negative exponent in the factored expression is interpreted in
\(\mathbb F_3^\times\); multiplication by \(2^{-2h}=1\) is legitimate.

Since

\[
T_h\equiv
\begin{cases}
1,&h\equiv1\pmod3,\\
2,&h\equiv2\pmod3,\\
0,&h\equiv0\pmod3,
\end{cases}
\]

we obtain

\[
\boxed{
C_h\equiv0\pmod3
\iff
\begin{cases}
h\equiv1\pmod3,&q\text{ odd},\\
h\equiv2\pmod3,&q\text{ even}.
\end{cases}}
\]

> **NSF3 (fan residue split).** Exactly one residue class of shell heights
> modulo \(3\) is excluded by the universal source-correction obstruction.
> The other two classes are not excluded modulo \(3\).

In particular, canonical \((q,h)=(3,1)\) is blocked but \((3,2)\) is not;
canonical \((4,2)\) is blocked but \((4,1)\) is not.  GPA2 remains correct,
but its eligible/blocked classification is specific to the canonical member
of the fan.

## 5. Logical role and limitations

NSF1--NSF3 are exact ancestry rules, but they do not assert that a correction
match exists.  A primitive prefix necessarily avoids every admissible fan
match already exposed before its record time.  The new information is the
simultaneous family of nonmembership conditions

\[
C_h\notin
\bigcup_{\substack{j+2\le i\le u_h\\i\equiv j+1\ (2)}}
\mathcal A(i,u_h)
\qquad(h\in\mathcal H(E,j,q)).
\]

Unlike the residual-atlas language, these conditions apply to arbitrary
valuation words, including mixed-payout tails.

Possible failure modes are explicit:

1. all noncanonical targets may be eliminated by one higher congruence;
2. the admissible fan may be too short at the dangerous record times;
3. correction layers may be too sparse for simultaneous avoidance to force
   exponent growth.

Any of these is a reason to retire the fan rather than enlarge a census.

## 6. Fan-capacity target

> **Noncanonical fan-capacity lemma (open).** There is an effective function
> \(G(r)\to\infty\) such that a primitive record prefix with at least \(r\)
> modulo-three-eligible fan heights either has already descended, has merged
> through another ancestor, or its least positive exponent representative is
> at least \(G(r)\) relative to the available diagonal scale.

The first bounded phase is narrower:

1. compute the exact modulo-\(3^s\) source-layer sieve for the fan;
2. determine whether a uniform obstruction appears at small \(s\);
3. if not, measure whether distinct fan heights impose genuinely distinct
   higher congruence conditions;
4. only then test record-extremal examples.

The falsifier is a family with arbitrarily long admissible fans whose
eligible targets all fail for the same bounded local reason while the least
exponent representative remains small.  Such a family would show that fan
size has no arithmetic capacity content.

## 7. First finite checkpoint

`scripts/explore_noncanonical_shell_fan_records.py --limit 5001
--max-power 10` applies the exact source-layer residue recursion to the
highest dangerous exceptional record on each PCD2 tail.  This is a targeted
diagnostic, not a universal coverage claim.

- Eight blocked ancestors have a nonempty modulo-three-eligible fan.
- They supply 19 admissible fan targets.
- The surviving target counts modulo
  \(3,3^2,\ldots,3^{10}\) are
  \(17,14,12,9,8,6,3,1,1,1\).
- The sole target surviving modulo \(3^{10}=59049\) is on \(n=471\):
  \(j=27,q=3,h=2,u=40\).  At that precision only source length \(i=30\)
  remains possible.
- Exact reverse correction recursion nevertheless proves
  \(C_{h=2}\notin\mathcal A(30,40)\).  The recursion is exhaustively checked
  against all small correction layers before it is applied to this target.
  Its first failing digit is exactly \(3^{13}\): the target survives modulo
  \(3^{12}\) and fails modulo \(3^{13}\).  The compatible suffix tree has at
  most 21 live states.

Thus there is no uniform low-modulus obstruction across the named records,
but the residue sieve is strongly selective.  Define the obstruction depth

\[
r(C;i,u)=\min\{s\ge1:
C\bmod3^s\notin\mathcal A(i,u)\bmod3^s\},
\]

with \(r=\infty\) for an exact match.  The final prototype has \(r=13\).
A continuation theorem must relate large obstruction depth across
the fan to record extremality or the least exponent representative.  Merely
showing that each individual primitive target eventually fails is tautological.

## 8. Literature gate and decision

The shell fan must not be presented as a new kind of Collatz inverse
structure.  Its basic ingredients sit inside established work:

- Böhm--Sontacchi parity-vector formulae already encode finite trajectories
  by exact affine sums of powers of two and three
  ([1978 article record](https://eudml.org/doc/290184)).
- Wirsching represents predecessor sets by finite integer sequences and
  develops “small sequences” and their combinatorics
  ([1996 paper](https://doi.org/10.1016/0012-365X(94)00243-C)).
- Applegate--Lagarias study pruned backward trees and their dependence on
  residue classes modulo powers of three
  ([1995 paper](https://doi.org/10.1080/10586458.1995.10504321)).
- Kontorovich--Lagarias survey accelerated backward iteration as branching
  trees and emphasize the gap between symbolic or probabilistic information
  and exceptional integer trajectories
  ([arXiv:0910.1944](https://arxiv.org/abs/0910.1944)).

In that language, \(Y_h\) is a sibling in the accelerated predecessor tree,
and the obstruction-depth calculation is a specialized modulo-\(3^s\)
predecessor sieve.  The repository-specific feature is narrower: both the
high state and a proposed sibling source must lie on aligned odd-repunit
diagonals, so correction equality forces a smaller-exponent merge by NSF2.
No prior treatment of that exact repunit-aligned intersection was located in
the bounded search, but no theorem here yet converts it into uniform descent.

**Decision:** demote the fan as a main avenue.  Retain NSF1--NSF4 as exact
machinery and attribution-correct finite evidence.  Do not enlarge the fan
census.  Reopen only after proving, independently of computation, that
record extremality or least-exponent size forces obstruction depth across
more than one fan member.  Without that repunit-specific correlation, the
programme is another pass through the classical predecessor tree.
