# The Integral-Escape Residual Frontier

**Status:** New proof framework. IEF1--IEF5 and IEF7--IEF21 below are exact
statements about nested cylinders and the balanced affine maps. They do not
prove repunit-tail descent. IEF10 does discharge the one deterministic
infinite balanced itinerary for the qualitative positive-integer question;
IEF11 turns that argument into a reusable criterion and closes every fixed
phase shift, while IEF12 discharges every Sturmian intercept at the critical
slope. IEF13 discharges every bounded-critical-discrepancy word with
Diophantine exponent greater than \(1\), including every such word of linear
factor complexity. The open qualitative frontier has unbounded discrepancy
or superlinear complexity, with IEF14 additionally removing cases where
repetition surplus outruns the growing discrepancy budget. IEF15 finitely
reduces sustained negative-drift branches, and IEF16 rules out either sign of
nonzero linear lower drift. Quantitative plateau bounds remain necessary if
the target is \(\sigma(a_n)\le3n\). IEF17 consolidates the remaining
non-cyclic survivor conditions into one residual intersection. IEF18--IEF19
sharpen the repetition axis, IEF20 discharges fixed-surplus repetitions that
occur inside asymptotically critical drift windows, and IEF21 replaces that
full envelope by exact terminal draw-up and endpoint-loss costs.

## 1. Change of terminal objective

A residual-frontier proof need not eliminate every \(2\)-adic survivor.
It only needs to eliminate positive-integer survivors.

Valuation prefixes naturally define nested \(2\)-adic cylinders. Their
infinite intersection can be a nonempty Cantor-like set even when it contains
no ordinary positive integer. Trying to prove that the full \(2\)-adic
survivor is empty may therefore demand much more than the Collatz problem
requires.

The proposed terminal condition is:

> Every infinite branch left by the combined descent and merger rules keeps
> acquiring nonzero high binary digits. Hence it represents a genuinely
> non-integral \(2\)-adic exponent, not a positive integer.

This permits any finite or recursively generated collection of complementary
rules. Their job is to constrain the residual language, not necessarily to
close it one rule at a time.

## 2. Nested-cylinder setup

Let a residual branch carry nested exponent cylinders

\[
\mathcal C_m
=n_m+2^{E_m}\mathbb Z_2,
\qquad
0\le n_m<2^{E_m},
\qquad E_{m+1}>E_m,
\]

with

\[
n_{m+1}\equiv n_m\pmod{2^{E_m}}.
\]

Write

\[
n_{m+1}=n_m+z_m2^{E_m},
\qquad
0\le z_m<2^{E_{m+1}-E_m}.
\]

The integer \(z_m\) is the block of newly exposed exponent bits. The branch
determines one \(2\)-adic exponent

\[
n_*=\lim_m n_m\in\mathbb Z_2.
\]

## 3. IEF1: positive integers are exactly eventual plateaus

> **IEF1 (integral-escape criterion).** Assume \(E_m\to\infty\). The
> intersection \(\bigcap_m\mathcal C_m\) contains a positive integer \(n\)
> if and only if \(n_m\) is eventually the constant value \(n\).
> Equivalently, it contains a positive integer if and only if the exponent
> lifts satisfy \(z_m=0\) for every sufficiently large \(m\), with the
> stabilized residue positive.

**Proof.** If \(n\in\mathcal C_m\), then \(n_m\) is the canonical residue of
\(n\) modulo \(2^{E_m}\). Once \(2^{E_m}>n\), that canonical residue is \(n\)
itself, so \(n_m=n\) thereafter and every later lift is zero.

Conversely, if \(n_m=n>0\) eventually, nesting puts \(n\) in every earlier
cylinder as well, so \(n\in\bigcap_m\mathcal C_m\). The lift formulation is
equivalent to eventual constancy. \(\square\)

Thus an infinite residual branch may remain in \(\mathbb Z_2\) without being
an integer counterexample. It is harmless if it has infinitely many nonzero
lift blocks.

## 4. IEF2: frontier theorem

Let a **sound discharge rule** either prove descent of its case or merge it
into a strictly smaller exponent. Build a residual tree by applying any
ordered or adaptive collection of sound rules and refining every undischarged
case into nested cylinders.

Assume:

1. every positive integer counterexample would define an infinite branch of
   the residual tree;
2. cylinder depths tend to infinity along every infinite branch;
3. every infinite residual branch has \(z_m\ne0\) infinitely often.

Then there is no positive integer counterexample.

Indeed, a positive counterexample would give an infinite branch by item 1,
but IEF1 would force its lift blocks to be eventually zero, contradicting
item 3. This proves:

> **IEF2 (integral-escape frontier theorem).** A sound residual tree proves
> the target when every infinite survivor escapes the eventually-zero binary
> language, even if the \(2\)-adic survivor set itself is nonempty.

The number of discharge rules is irrelevant. Exhaustiveness is carried by
the residual-tree construction and the terminal integral-escape condition.

## 5. Application to the repunit exponent cylinders

PCD9 assigns every compatible finite valuation word of total valuation \(E\)
one odd repunit exponent class modulo \(2^E\). PCD11 extends a prefix by a
block of total valuation \(\delta\), and PCD13 writes its least exponent
representative as

\[
n_{m+1}=n_m+z_m2^{E_m},
\]

where

\[
z_m\equiv
(t_m-\kappa_m)[h_{E_m}(2x_m+1)]^{-1}
\pmod{2^\delta}.
\]

Here \(x_m\) is the canonical odd starting-state residue of the valuation
prefix; it is distinct from the exponent representative \(n_m\).

Consequently the IEF lift is exactly the existing PCD13 exponent lift. A
positive exponent surviving every prefix must eventually have

\[
\boxed{z_m=0}
\qquad\text{or equivalently}\qquad
\boxed{t_m=\kappa_m}
\]

at every subsequent extension.

The current roadmap asks for a sublinear or logarithmic bound on plateau
length. IEF1 separates two objectives:

- for a quantitative stopping bound such as \(\sigma(a_n)\le3n\), a
  quantitative plateau estimate is still needed;
- for universal eventual descent, it is enough to prove that no residual
  branch has an infinite terminal plateau.

The qualitative target is strictly weaker:

\[
\boxed{
z_m\ne0\text{ infinitely often on every infinite residual branch.}
}
\]

It allows arbitrarily long finite plateaus.

## 6. How this combines many theories

Use a hierarchical frontier rather than a flat percentage sum.

1. At the exponent level, discharge direct descents and exact mergers into
   smaller exponents.
2. On the primitive residual, pass to strict record-deficit prefixes.
3. Use PCD1 to split eligible, initial, blocked-concentrated, and
   blocked-diffuse ledgers.
4. Apply different sound rules to different branches: GPA reachability,
   controlled-height non-shadowing, concentration lemmas, or other exact
   mechanisms.
5. Encode every remaining infinite branch by its exponent-lift blocks.
6. Prove that the residual symbolic system has no eventually-zero lift tail.

The final survivor may have \(2\)-adic measure zero, positive Hausdorff
dimension, or even uncountably many points. None matters if its intersection
with the positive integers is empty.

## 7. Immediate balanced-\(q=3\) target

For the deterministic balanced obstruction, PCD14 says a zero-lift run is a
contiguous match between the affine endpoint-lift word and one
power-of-three carry. The revised terminal question is:

> Can that match continue forever after some finite prefix for a positive
> exponent, while the tail remains primitive and has not descended?

One does not initially need an \(O(\log m)\) run bound. It is enough to prove
that every assumed terminal match eventually triggers one of:

- a nonzero exponent lift;
- descent below the original Mersenne level;
- a merge into a smaller repunit tail;
- a contradiction in the exact affine/carry recursion.

An eventual plateau has additional structure unavailable in arbitrary finite
plateaus: the exponent is fixed, the high carry is eventually exhausted, and
the same positive repunit would have to realize the complete infinite
Sturmian valuation itinerary.

## 8. IEF3: the dual endpoint frontier

There is a second escape coordinate which reverses the roles of \(2\) and
\(3\). After \(L\) appended balanced blocks, write

\[
x_L=\frac{3^{R_L}x_0+B_L}{2^{E_L}},
\qquad E_L=R_L+2L.
\]

Every integral endpoint satisfies

\[
x_L\equiv q_L\pmod{3^{R_L}},
\qquad
q_L\equiv B_L2^{-E_L}\pmod{3^{R_L}},
\qquad 0\le q_L<3^{R_L}.
\]

The residue \(q_L\) depends only on the balanced word, not on \(x_0\).
PCD16 and the block maps

\[
\Phi_3(x)=\frac{27}{32}x+\frac{19}{32},
\qquad
\Phi_4(x)=\frac{81}{64}x+\frac{65}{64}
\]

give the uniform real bound

\[
x_L<\frac32x_0+\frac{195}{128}L.
\]

Indeed, the initial homogeneous term has multiplier below \(3/2\). Every
block injection is at most \(65/64\), and every suffix transports it by a
multiplier below \(3/2\).

If a fixed positive \(x_0\) realizes every balanced block, then \(x_L\) is a
positive integer for every \(L\). Since \(R_L\ge3L\), eventually

\[
0<x_L<3^{R_L}.
\]

The endpoint congruence then forces \(x_L=q_L\). Therefore:

> **IEF3 (dual endpoint escape).** If
>
> \[
> q_L-\frac{195}{128}L\longrightarrow+\infty,
> \]
>
> then no fixed positive integer can realize the complete infinite balanced
> \(q=3\) itinerary. In particular, \(q_L/L\to\infty\) is sufficient.

This converts the terminal balanced obstruction into a word-only least
representative problem modulo \(3^{R_L}\). It is different from PCD13: that
result follows exponent cylinders modulo powers of \(2\), whereas IEF3
follows the forced endpoint class modulo powers of \(3\).

The exact
[dual-frontier diagnostic](../../scripts/explore_balanced_q3_dual_frontier.py)
finds through \(L=10000\):

\[
q_L\ge2^{5L-1}.
\]

The largest observed bit-length deficit of \(q_L\) below \(3^{R_L}\) is only
\(12\), at \(L=2179\). The recurrence is independently reconstructed from the
full affine correction through \(L=2000\). These are finite observations, not
a universal lower bound. They identify a new theorem target:

> Prove any lower bound on \(q_L\) which eventually dominates \(L\); the
> observed exponential floor is far stronger than IEF3 actually requires.

## 9. IEF4: closed dual-residue recursion

The dual residue has a closed exact transition. Suppose the existing word has
\(R\) odd steps and endpoint residue \(q\pmod{3^R}\). Append a block with
odd-step length \(r\), valuation total \(\delta\), and affine correction \(b\).
Put

\[
a\equiv b2^{-\delta}\pmod{3^r},
\qquad 0\le a<3^r,
\qquad
d=\frac{2^\delta a-b}{3^r}.
\]

Write the new residue as \(q'=a+3^rh\). Applying the inverse block map gives

\[
\frac{2^\delta q'-b}{3^r}=d+2^\delta h.
\]

This must equal \(q\pmod{3^R}\), so

\[
\boxed{
h\equiv(q-d)2^{-\delta}\pmod{3^R},
\qquad
q'=a+3^rh.
}
\]

For the two balanced blocks:

\[
\begin{array}{c|c|c|c|c}
\text{block}&r&\delta&b&(a,d)\\
\hline
(1,1,3)&3&5&19&(20,23)\\
(1,1,1,3)&4&6&65&(20,15).
\end{array}
\]

Therefore the mechanical block word drives the one-dimensional cocycle

\[
q'=20+3^rh,
\qquad
h\equiv
\begin{cases}
(q-23)2^{-5}\pmod{3^R},&r=3,\\
(q-15)2^{-6}\pmod{3^R},&r=4.
\end{cases}
\]

> **IEF4 (closed dual frontier).** The displayed recurrence computes the
> exact least endpoint residue at every balanced prefix using only
> \((q,R)\) and the next mechanical block.

This supplies a genuinely closed growing-state system. The remaining theorem
target is to show that its canonical representatives cannot return to a
linear-size window infinitely often.

Writing

\[
2^\delta h=q-d+j3^R,
\qquad 0\le j<2^\delta,
\]

exposes one small **dual digit** \(j\) at every transition. The dangerous case
\(j=0\) is exactly

\[
q\equiv23\pmod{32}
\quad\text{or}\quad
q\equiv15\pmod{64},
\]

and then \(q'\) follows the corresponding real affine block map
\(\Phi_3(q)\) or \(\Phi_4(q)\). A nonzero digit places the next \(q'\) back at
the scale of its expanding modulus.

Through \(L=10000\), both dual-digit alphabets are full. Zero occurs \(185\)
times on the five-bit blocks and \(59\) times on the six-bit blocks; the
longest zero run is two. This rules out a local forbidden-digit explanation
in the finite sample. The correct qualitative target is the absence of an
**eventually all-zero tail**, not a fixed bound on finite zero runs.

## 10. IEF5: nonzero digits reset the frontier

Suppose a transition begins with modulus \(M=3^R\ge27\) and has dual digit
\(j\ge1\). Since \(0\le q<M\), \(d\le23\), and \(2^\delta\le64\),

\[
h=\frac{q-d+jM}{2^\delta}
\ge\frac{M-23}{64}
\ge\frac{M}{448}.
\]

If the appended block has length \(r\), its new modulus is \(M'=3^rM\), so

\[
q'=20+3^rh>\frac{M'}{448}.
\]

If the next \(H\) dual digits are zero, the corresponding \(q\)-values follow
the real balanced block maps. PCD16 gives homogeneous multiplier above
\(2/3\) over the complete zero suffix, and every affine injection is positive.
Therefore the endpoint after that suffix satisfies

\[
\boxed{
q_{\mathrm{end}}>\frac{M'}{672}.
}
\]

Let \(s(L)\) be the last nonzero dual-digit position at or before \(L\), and
let \(R_{s(L)}\) be the accumulated odd-step count just after that transition.
This proves:

> **IEF5 (reset bound).** Whenever \(s(L)\) exists beyond the initial
> modulus,
> \[
> q_L>\frac{3^{R_{s(L)}}}{672}.
> \]
> Consequently IEF3 follows from
> \[
> \frac{3^{R_{s(L)}}}{L}\longrightarrow\infty.
> \]

Since every balanced block has at least three odd steps,
\(R_s\ge3s\). It is therefore sufficient to prove

\[
\frac{27^{s(L)}}{L}\longrightarrow\infty.
\]

This is a very weak recurrence target. It does not require bounded,
logarithmic, or even polynomial zero runs. It only rules out gaps so enormous
that the last nonzero reset remains at essentially logarithmic depth compared
with the current block index.

## 11. IEF7: the integral bridge

The endpoint and starting-cylinder frontiers expose the same small digit.
Let \(W_L\) be the first \(L\) appended balanced blocks and write

\[
\Phi_{W_L}(x)=\frac{3^{R_L}x+B_L}{2^{E_L}}.
\]

There is one canonical starting residue

\[
u_L\equiv-B_L3^{-R_L}\pmod{2^{E_L}},
\qquad 0\le u_L<2^{E_L},
\]

for which the complete composition is integral. Write its nested lift as

\[
u_{L+1}=u_L+z_{L+1}2^{E_L},
\qquad 0\le z_{L+1}<2^\delta.
\]

Then the canonical endpoint is exactly the dual residue:

\[
\boxed{\Phi_{W_L}(u_L)=q_L.}
\]

Moreover, if the next block has parameters \((r,\delta,d)\), changing the
start from \(u_L\) to \(u_L+z2^{E_L}\) changes the old endpoint from \(q_L\)
to

\[
q_L+z3^{R_L}.
\]

The next block is integral exactly when

\[
q_L+z3^{R_L}\equiv d\pmod{2^\delta}.
\]

The dual digit \(j\) from IEF4 is defined by

\[
2^\delta h=q_L-d+j3^{R_L}.
\]

These two congruences have the same unique representative in
\(0\le z,j<2^\delta\). Hence

\[
\boxed{z_{L+1}=j_{L+1}.}
\]

The endpoint identity and the equality of digits follow together by
induction, starting from the empty word \(u_0=q_0=0\).

> **IEF7 (integral bridge).** The balanced starting-cylinder lift and dual
> endpoint digit streams agree exactly. A fixed positive integer can make
> every finite balanced affine composition integral only if this common
> digit stream is eventually zero. Conversely, eventual stabilization gives
> a fixed positive integer for which every such composition is integral.

The final equivalence is IEF1 applied to \(u_L\): once \(2^{E_L}\) exceeds a
fixed positive starting value, its canonical residue must equal that value.
Conversely, eventual stabilization at \(u>0\) makes every finite balanced
composition integral, with endpoint \(q_L\). This converse is deliberately
stated for the affine divisibility schedule: it need not certify that every
scheduled valuation is exact, because an endpoint may acquire an additional
power of two. The necessary direction is enough for exclusion. Any exact
positive Collatz realization would in particular make all these affine
compositions integral.

This gives two distinct sufficient targets:

- the quantitative route IEF3--IEF5 proves endpoint escape and can retain
  stopping-time information;
- the qualitative route IEF7 only has to prove
  \(j_L\ne0\) infinitely often. It permits gaps of arbitrary size and is
  enough to exclude a positive-integer realization of the infinite word.

The exact
[zero-cylinder diagnostic](../../scripts/explore_balanced_q3_zero_cylinders.py)
computes \(u_L\), \(z_L\), and the continued-fraction scales of the mechanical
word. Through \(L=10000\), its lift digits agree with the IEF6 dual-digit
certificate, as IEF7 predicts. This is the same finite evidence viewed
through the bridge, not an independent experiment.

The block-length word is the mechanical \(3/4\) word with indicator slope

\[
\beta=\frac{2}{\log_2(3/2)}-3.
\]

If \(Q_k\) are the continued-fraction denominators of \(\beta\), the focused
symbolic target

\[
\boxed{z_{Q_k}\ne0\text{ for infinitely many }k}
\]

would already prove non-stabilization. Standard-word decompositions at these
scales are therefore a natural place to seek a renormalization argument; no
statistical independence assumption is needed.

## 12. IEF8: Sturmian bridge renormalization

IEF7 has an exact concatenation law which removes the affine correction from
the state. For a finite block factor \(W\), put

\[
\mathcal G(W)=(A_W,C_W,u_W,q_W),
\qquad
A_W=3^{R_W},
\qquad
C_W=2^{E_W},
\]

where

\[
A_Wu_W+B_W=C_Wq_W,
\qquad
0\le u_W<C_W,
\qquad
0\le q_W<A_W.
\]

Let \(WV\) mean that \(W\) is followed by \(V\). Define

\[
s\equiv(u_V-q_W)A_W^{-1}\pmod{C_V},
\qquad 0\le s<C_V,
\]

and

\[
t=\frac{q_W+sA_W-u_V}{C_V}.
\]

The numerator defining \(t\) is divisible by \(C_V\). The canonical ranges
give \(0\le t<A_W\). Direct substitution then proves

\[
\boxed{
u_{WV}=u_W+sC_W,
\qquad
q_{WV}=q_V+tA_V.
}
\]

Thus \(\mathcal G(WV)\) is computed from \(\mathcal G(W)\) and
\(\mathcal G(V)\), without retaining \(B_W\) or expanding either factor.
The integer \(s\) is the complete cylinder-lift block exposed by appending
\(V\). In particular,

\[
s=0
\quad\Longleftrightarrow\quad
q_W\equiv u_V\pmod{C_V}.
\]

This proves:

> **IEF8 (bridge-pair concatenation).** Relaxed integral bridges form an exact
> mixed-radix concatenation system under the displayed formulas. A nonzero
> concatenation lift certifies that at least one constituent IEF7 digit in
> the appended factor is nonzero.

Skip the first appended balanced block. The remaining \(3/4\)-indicator word
is the characteristic Sturmian word of slope

\[
\beta=\frac{2}{\log_2(3/2)}-3.
\]

If

\[
\beta=[0;a_1,a_2,\ldots]
\]

and \(Q_k\) are its convergent denominators, its standard prefixes satisfy,
after the two initial seeds,

\[
S_k=S_{k-1}^{\,a_k}S_{k-2},
\qquad |S_k|=Q_k.
\]

This is the standard continued-fraction construction of the characteristic
mechanical word. It turns IEF8 into a genuine renormalization. Put

\[
P_k=S_{k-1}^{\,a_k},
\qquad
\Delta_k=q_{P_k}-u_{S_{k-2}}.
\]

The top-level lift in \(S_k=P_kS_{k-2}\) obeys

\[
s_k\equiv-\Delta_kA_{P_k}^{-1}
\pmod{2^{E_{k-2}}}.
\]

Since \(A_{P_k}\) is odd,

\[
v_2(s_k)=v_2(\Delta_k)
\]

whenever the residue is nonzero. Consequently:

> **IEF8 frontier reduction.** It is enough to prove
>
> \[
> v_2(\Delta_k)<E_{k-2}
> \]
>
> for infinitely many \(k\). Any uniform bound on \(v_2(\Delta_k)\), or even
> any bound growing more slowly than \(E_{k-2}\), would exclude an eventually
> zero bridge stream and hence exclude a positive-integer realization of the
> balanced itinerary.

This is narrower than proving \(q_L/L\to\infty\). It asks for one
cross-difference valuation at recursively generated scales.

There is a still smaller sufficient target. Every characteristic standard
prefix begins with the \(r=3\) block, whose relaxed starting class is

\[
u\equiv23\pmod{32}.
\]

Hence

\[
\boxed{
q_{P_k}\not\equiv23\pmod{32}
\quad\text{for infinitely many }k
}
\]

already forces \(v_2(\Delta_k)<5\) infinitely often and closes the qualitative
balanced branch. This is a five-bit output condition, but it is not yet a
five-bit closed dynamical system: PCD15 warns that endpoint updates consume
unseen high bits. IEF8 identifies the exact standard-word bridge state from
which those bits must be replenished.

The exact
[Sturmian renormalization diagnostic](../../scripts/explore_balanced_q3_sturmian_renormalization.py)
uses the concatenation law rather than expanding the standard words. Through
\(Q_k=111457\), all \(12\) tested top-level lifts are nonzero and

\[
\max v_2(\Delta_k)=4,
\]

while the corresponding tail depth reaches \(E_{k-2}=125743\). The standard
recursion is independently checked against expanded mechanical prefixes
through \(Q=4563\). These are finite facts only. In particular, the observed
bound \(v_2(\Delta_k)\le4\), equivalently the observed avoidance of
\(q_{P_k}\equiv23\pmod{32}\), is a candidate lemma, not a claim.

The next convergent \(Q=3097592\) has partial quotient \(27\). Exact
renormalization reaches a roughly \(16.8\)-million-bit state there, but the
current general-purpose modular inversion is not a useful proof experiment at
that scale. The symbolic valuation recurrence, rather than a larger census,
is the next target.

## 13. IEF9: the critical 2-adic Hecke--Mahler value

There is a direct analytic encoding of the complete balanced valuation word.
Use the shortcut map and let \(d_i\) be the position of its \(i\)-th odd
iterate, with \(d_0=0\). Put

\[
c=\log_2(3/2),
\qquad
\gamma=\frac c2.
\]

The valuation-three payouts occur at accelerated odd-step indices

\[
T_m=\left\lfloor\frac{2m}{c}\right\rfloor,
\qquad m\ge0.
\]

For \(i\ge1\), the number of payout indices \(T_m<i\) is
\(\lceil\gamma i\rceil\). Every payout contributes two additional even
shortcut steps. Therefore

\[
\boxed{
d_0=0,
\qquad
d_i=i+2\lceil\gamma i\rceil\quad(i\ge1).
}
\]

The number \(\gamma\) is irrational: rationality of \(c=p/q\) would give
\(3^q=2^{p+q}\).

For a shortcut parity vector whose ones occur at \(d_0,d_1,\ldots\), the
inverse parity conjugacy is

\[
\xi=-\sum_{i=0}^{\infty}\frac{2^{d_i}}{3^{i+1}}
\in\mathbb Z_2.
\]

Since \(\gamma i\) is never integral for \(i\ge1\),
\(\lceil\gamma i\rceil=\lfloor\gamma i\rfloor+1\). Substitution gives

\[
\boxed{
\xi
=-\frac13-\frac43
\sum_{i=1}^{\infty}
\left(\frac23\right)^i4^{\lfloor\gamma i\rfloor}.
}
\]

The series converges in \(\mathbb Q_2\), because the \(2\)-adic valuation of
its \(i\)-th summand tends to infinity. Its Archimedean parameters lie exactly
on the critical boundary:

\[
\frac23\,4^\gamma
=\frac23\,2^c
=1.
\]

Thus its complex summands do not even tend to zero. It is a genuinely
\(2\)-adic boundary value of a two-variable Hecke--Mahler series, not a value
inside the usual complex convergence domain.

> **IEF9 (critical Hecke--Mahler reduction).** If the displayed
> \(2\)-adic number \(\xi\) is irrational over \(\mathbb Q\), then no positive
> integer realizes the complete balanced valuation itinerary.

Indeed, every positive realization has the prescribed infinite shortcut
parity vector and therefore equals its unique inverse-conjugacy value
\(\xi\). Irrationality is more than is needed; proving merely
\(\xi\notin\mathbb Z_{>0}\) suffices.

The exact
[Hecke--Mahler verifier](../../scripts/verify_balanced_q3_hecke_mahler.py)
checks the Beatty position formula against the mechanical payout schedule and
checks both series expressions against the exact finite parity cylinder.
The default certificate covers \(5000\) accelerated odd steps and shortcut
depth \(7926\).

This opens a second theorem route from IEF8:

> **Critical \(2\)-adic Hecke--Mahler lemma.** Prove that
> \[
> -\frac13-\frac43
> \sum_{i\ge1}(2/3)^i4^{\lfloor\gamma i\rfloor}
> \notin\mathbb Q.
> \]

Existing Hecke--Mahler transcendence theorems do not directly supply this
lemma. Bugeaud and Laurent require the strict complex-domain condition
\(\lvert z_1z_2^\theta\rvert<1\)
([arXiv:2203.12901](https://arxiv.org/abs/2203.12901)); here the corresponding
quantity equals \(1\). Luca, Ouaknine, and Worrell treat fixed-base
Archimedean series with \(\lvert\beta\rvert>1\)
([arXiv:2412.07908](https://arxiv.org/abs/2412.07908)). Results about
\(p\)-adic numbers whose *digits themselves* are Sturmian also do not apply
without an additional argument: the IEF7 lift digits occupy their full finite
alphabets in the certificate.

For the stronger goal of proving \(\xi\) irrational, the promising adaptation
is a \(2\)-adic Subspace-Theorem or Mahler-method argument using the exact
standard-word repetitions from IEF8. IEF10 below shows that those periodic
approximants already suffice for the weaker—and presently required—claim
\(\xi\notin\mathbb Z_{>0}\).

## 14. IEF10: periodic approximants exclude an integer

For the positive-integer question, the full transcendence lemma in IEF9 is
unnecessary. Standard-word repetition and an ordinary size comparison suffice.

Move past the finite initial blocks so that the balanced \(3/4\)-indicator is
the characteristic word of slope

\[
\beta=\frac2{\log_2(3/2)}-3.
\]

Use the shortcut-parity morphism

\[
\chi(3)=11100,
\qquad
\chi(4)=111100.
\]

Let \(S_k\) be a standard block prefix, let

\[
W_k=\chi(S_k),
\qquad
E_k=|W_k|,
\qquad
R_k=|W_k|_1,
\]

and let the one-positions in \(W_k\) be

\[
0\le a_0<a_1<\cdots<a_{R_k-1}<E_k.
\]

Repeating \(W_k\) periodically gives the rational \(2\)-adic inverse value

\[
\rho_k
=\frac{N_k}{2^{E_k}-3^{R_k}},
\qquad
N_k=\sum_{j=0}^{R_k-1}2^{a_j}3^{R_k-1-j}.
\]

The denominator is odd, and remains odd after reducing the fraction.

### Height bound

For a one-position inside a balanced block prefix, write \(j=R_m+s\), where
\(m\) complete blocks precede it and \(s\) valuation-one steps have occurred
inside the next block. Then \(a_j=E_m+s\). PCD16 gives

\[
E_m-R_m\log_2 3<c,
\qquad c=\log_2(3/2),
\]

and \(1-\log_2 3=-c\). Hence

\[
a_j-j\log_2 3<c,
\qquad
\frac{2^{a_j}}{3^j}<2^c=\frac32.
\]

It follows that

\[
N_k<\frac{R_k}{2}3^{R_k}.
\]

PCD16 also gives \(3^{R_k}<\frac32\,2^{E_k}\), so

\[
\boxed{N_k<E_k2^{E_k}},
\qquad
\boxed{|2^{E_k}-3^{R_k}|<3\cdot2^{E_k}}.
\]

Thus the reduced numerator and denominator of \(\rho_k=p_k/q_k\) have
ordinary height at most \(3E_k2^{E_k}\).

### Extra \(2\)-adic agreement

The standard recursion starts the characteristic word with \(S_k\). After
that copy, the recursion supplies either \(S_{k-1}\) or another copy of
\(S_k\), depending on the next partial quotient. Since \(S_{k-1}\) is a
prefix of \(S_k\), in either case the characteristic word and \(S_k^\infty\)
agree for at least \(|S_k|+|S_{k-1}|\) block symbols. Consequently, the true
parity word and \(W_k^\infty\) agree for at least

\[
M_k=E_k+E_{k-1}
\]

binary positions. Their inverse parity values therefore satisfy

\[
x\equiv\rho_k\pmod{2^{M_k}}
\]

for any fixed integer \(x\) realizing the true infinite tail.

The two values are distinct. Otherwise injectivity of the parity conjugacy
would make the aperiodic characteristic parity word equal to the periodic
word \(W_k^\infty\).

Write \(\rho_k=p_k/q_k\) in lowest terms. Since \(q_k\) is odd,

\[
0\ne xq_k-p_k\equiv0\pmod{2^{M_k}}.
\]

Consequently, for all sufficiently large \(k\),

\[
2^{E_k+E_{k-1}}
\le |xq_k-p_k|
\le (3|x|+E_k)2^{E_k},
\]

and hence

\[
\boxed{2^{E_{k-1}}\le3|x|+E_k.}
\tag{1}
\]

### Continued-fraction growth

Only one standard fact about the specific logarithmic slope remains. Baker's
lower bound for a nonzero integer linear form in
\(\log(3/2)\) and \(\log2\) gives constants \(C>0\) and \(Q_0\) such that

\[
\left|\beta-\frac pq\right|>q^{-C}
\qquad(q\ge Q_0).
\]

Indeed,

\[
\beta-\frac pq
=\frac{2q\log2-(3q+p)\log(3/2)}
{q\log(3/2)}.
\]

For approximants with \(|\beta-p/q|<1\), the two integer coefficients in the
numerator are \(O(q)\). A Baker--Matveev bound therefore gives
\(|2q\log2-(3q+p)\log(3/2)|>q^{-C_0}\) for some fixed \(C_0\). Dividing by
the fixed factor \(\log(3/2)\) and by \(q\) gives
\(|\beta-p/q|>q^{-(C_0+1)}\); renaming the exponent gives the displayed
constant \(C\). This is the standard finite-irrationality-measure corollary
of a lower bound for linear forms in logarithms
([Matveev 2000](https://doi.org/10.1070/IM2000v064n06ABEH000314)). The
numerator is the nonzero linear form

\[
2q\log2-(3q+p)\log(3/2).
\]

For consecutive convergent denominators \(Q_{k-1},Q_k\), the standard upper
bound

\[
\left|\beta-\frac{P_{k-1}}{Q_{k-1}}\right|
<\frac1{Q_{k-1}Q_k}
\]

therefore implies

\[
Q_k<Q_{k-1}^{C-1}
\]

eventually. Since every block has shortcut length five or six,

\[
5Q_k\le E_k\le6Q_k.
\]

Thus

\[
\log E_k=O(\log E_{k-1}),
\qquad
\frac{E_{k-1}}{\log E_k}\longrightarrow\infty.
\]

This contradicts (1), because \(2^{E_{k-1}}\) eventually dominates
\(3|x|+E_k\).

> **IEF10 (balanced-itinerary exclusion).** No fixed positive integer can
> realize the complete deterministic balanced \(q=3\) valuation itinerary.

This discharges the infinite balanced word as a qualitative terminal branch.
It does not prove the quantitative bound \(\sigma(a_n)\le3n\), and it does not
discharge other residual valuation languages unless they admit the same
bounded-distortion, recurrent-prefix, and finite-irrationality-measure
structure.

The exact
[periodic-approximant verifier](../../scripts/verify_balanced_q3_periodic_approximants.py)
checks the standard prefix repetition, rational inverse formula, odd
denominator, height bounds, and \(2^{E_k+E_{k-1}}\) congruence. Through
\(Q_k=4563\), the final tested approximant has \(E_k=24727\), agreement depth
\(26835\), and reduced height bit-length \(24739\).

## 15. IEF11: a reusable periodic-prefix discharge rule

The preceding proof separates into a language-independent criterion. Let
\(v\) be an infinite shortcut-parity word, and suppose there are finite binary
words \(A_k,B_k\), with \(B_k\ne\varnothing\), and footprint
\(N_k=|A_k|+|B_k|\), such that:

1. \(v\) and \(A_kB_k^\infty\) agree in their first \(N_k+G_k\) positions;
2. the rational inverse \(\rho_k=p_k/q_k\) of \(A_kB_k^\infty\), in lowest
   terms, has \(q_k\) odd and
   \[
   |p_k|+|q_k|\le H(N_k)2^{N_k};
   \]
3. \(v\ne A_kB_k^\infty\), so the corresponding inverse values are distinct;
4. \(G_k-\log_2 H(N_k)\longrightarrow\infty\).

If a fixed integer \(x\) realized \(v\), agreement of the inverse values
would give

\[
0\ne xq_k-p_k\equiv0\pmod{2^{N_k+G_k}}.
\]

The height bound would also give

\[
|xq_k-p_k|
\le (|x|+1)H(N_k)2^{N_k}.
\]

After cancelling \(2^{N_k}\), these inequalities require

\[
2^{G_k}\le (|x|+1)H(N_k),
\]

contrary to condition 4.

> **IEF11 (eventually-periodic-prefix discharge criterion).** Any aperiodic
> residual parity word admitting eventually periodic approximants with
> agreement excess \(G_k\) and height factor \(H(N_k)\), where
> \(G_k-\log_2H(N_k)\to\infty\), has no fixed integer realization.

IEF10 is the instance \(A_k=\varnothing\), \(B_k=W_k\),
\(G_k=E_{k-1}\), and \(H(E_k)=O(E_k)\). The Baker input
is used only to prove that the standard-word denominators make
\(E_{k-1}/\log E_k\to\infty\); it is not part of IEF11 itself.

The criterion also closes every **fixed phase shift** of the balanced word.
Deleting a fixed prefix of \(b\) parity bits changes the agreement depth from
\(E_k+E_{k-1}\) to \(E_k+E_{k-1}-b\). The corresponding periodic
approximant is the fixed \(b\)-bit rotation of \(W_k\). Applying those fixed
shortcut steps to the rational inverse changes its numerator and denominator
by fixed affine integer operations, so its height is still
\(O_b(E_k2^{E_k})\). Thus the agreement excess is \(E_{k-1}-b\), and IEF11
applies unchanged. In particular, no suffix beginning after any fixed number
of balanced payout blocks can be the complete itinerary of a fixed positive
integer.

The periodic-approximant verifier accepts `--phase-blocks`; it rotates every
approximant by the exact parity length of that fixed block prefix and checks
the reduced agreement modulus and rational height directly.

This is the desired residual-frontier form of the argument. A new terminal
language need not equal the balanced word: it is discharged whenever one can
construct periodic approximants satisfying the four conditions above. The
remaining classification problem is therefore to prove that every infinite
blocked-diffuse branch either enters such a language or is assigned to a
separately named residual class.

## 16. IEF12: all balanced Sturmian intercepts are discharged

IEF11 closes more than fixed shifts. A theorem of Bugeaud and Kim supplies
the required eventually periodic prefixes for **every** Sturmian word,
including every intercept.

Let \(s\) be any Sturmian word in the block alphabet \(\{3,4\}\). Their
Theorem 3.4 and Lemma 10.3 imply the following combinatorial consequence.
There are arbitrarily large pairs of words \(U,V\), with
\(V\ne\varnothing\), for which \(s\) and \(UV^\infty\) agree for \(L\) block
symbols and

\[
L\ge 2.4\bigl(|U|+|V|\bigr).
\tag{2}
\]

Indeed, Theorem 3.4 gives

\[
\operatorname{rep}(s)\le\sqrt{10}-\frac32,
\]

and Lemma 10.3 converts this recurrence bound into the Diophantine exponent
bound

\[
\operatorname{dio}(s)\ge
\kappa:=\frac53+\frac{4\sqrt{10}}{15}=2.5099\ldots.
\]

Here \(\operatorname{dio}(s)\) is the supremum of the ratios
\(|UV^w|/(|U|+|V|)\) attained by arbitrarily long prefixes \(UV^w\). Such a
prefix agrees with \(UV^\infty\) for \(|UV^w|\) symbols. Taking any constant
below \(\kappa\), such as \(2.4\), therefore gives (2) infinitely often
([Bugeaud--Kim 2019](https://doi.org/10.1090/tran/7378),
[arXiv:1510.00279](https://arxiv.org/abs/1510.00279)).

Apply the nonuniform shortcut morphism

\[
\chi(3)=11100,
\qquad
\chi(4)=111100.
\]

Put \(A=\chi(U)\), \(B=\chi(V)\), and
\(N=|A|+|B|\). Since every block image has length five or six,

\[
N\le6(|U|+|V|),
\qquad
M:=|\chi(s_0s_1\cdots s_{L-1})|\ge5L.
\]

Equation (2) therefore gives

\[
M\ge12(|U|+|V|),
\qquad
G:=M-N\ge6(|U|+|V|)\ge N.
\tag{3}
\]

It remains to check the ordinary height of the inverse value of
\(AB^\infty\). Let \(a=|A|\), \(e=|B|\), and let \(r_A,r_B\) be their
one-counts. The periodic inverse of \(B^\infty\) has odd denominator
\(2^e-3^{r_B}\). PCD16 applies to every factor of every mechanical word of
this slope, so its numerator and denominator are \(O(e2^e)\). If its reduced
value is \(p_B/q_B\), prepending \(A\) gives

\[
\rho_{A,B}
=\frac{2^a p_B-C_Aq_B}{3^{r_A}q_B},
\]

where \(C_A\) is the affine correction of \(A\). The same bounded-distortion
estimate gives

\[
3^{r_A}=O(2^a),
\qquad
C_A=O(a2^a).
\]

All Sturmian words with a fixed slope have the same finite-factor language.
Hence PCD16 applies to every factor used here, not only to the characteristic
intercept. Consequently the reduced height satisfies

\[
\operatorname{height}(\rho_{A,B})=O(N^2 2^N).
\tag{4}
\]

The denominator remains odd. Since the codewords have uniquely recognizable
`00` block delimiters, an eventually periodic parity image would make its
block word eventually periodic. A Sturmian word is aperiodic, so its parity
image cannot equal \(AB^\infty\). Equations
(3)--(4) satisfy IEF11 with \(H(N)=O(N^2)\) and \(G\ge N\).

> **IEF12 (Sturmian-family discharge).** No fixed positive integer realizes
> the complete balanced \(q=3\) itinerary belonging to any Sturmian word of
> the critical slope, for any intercept.

This strictly enlarges the discharged residual from one characteristic word
and its countably many shifts to the entire uncountable Sturmian subshift of
that slope. The next frontier is no longer "unknown phase". It is whether an
infinite blocked-diffuse terminal branch must be Sturmian; if not, its first
departure from balance must be quantified and assigned to a new language.

The finite
[arbitrary-intercept diagnostic](../../scripts/explore_balanced_q3_sturmian_intercepts.py)
searches for eventually periodic completions at increasing footprints. For
five default intercepts it verifies the exact rational inverse, odd
denominator, agreement congruence, and height. This is a consistency check on
the transfer through \(\chi\), not evidence needed by IEF12.

## 17. IEF13: discrepancy versus repetition

The Sturmian hypothesis in IEF12 is stronger than necessary. The proof uses
only one real-arithmetic property and one word-combinatorial property.

Let \(w\) be an aperiodic infinite word over \(\{3,4\}\). For a finite block
factor \(W\), write \(R(W)\) for the sum of its letters and \(|W|\) for its
number of blocks. Define

\[
c=\log_2(3/2).
\]

Assume first that \(w\) has **bounded critical discrepancy**: there is a
constant \(D\) such that every finite factor satisfies

\[
\boxed{|cR(W)-2|W||\le D.}
\tag{5}
\]

Equivalently, every homogeneous block multiplier lies between two fixed
positive constants:

\[
2^{-D}
\le \frac{3^{R(W)}}{2^{R(W)+2|W|}}
\le2^D.
\]

Next use the Diophantine exponent of an infinite word. By definition,
\(\operatorname{dio}(w)\) is the supremum of the real numbers \(\rho\) for
which arbitrarily long prefixes of \(w\) have the form \(UV^t\), with
\(V\ne\varnothing\), and

\[
\frac{|UV^t|}{|UV|}\ge\rho.
\]

Here \(V^t\) denotes the appropriate fractional power, so this says exactly
that \(w\) and \(UV^\infty\) agree for at least \(\rho|UV|\) block symbols.

Condition (5) also controls the nonuniform code length. Put

\[
\lambda=\frac2c+2.
\tag{6}
\]

For every factor \(W\),

\[
\bigl||\chi(W)|-\lambda|W|\bigr|
=\left|R(W)-\frac{2|W|}{c}\right|
\le\frac Dc.
\]

Now suppose

\[
\boxed{\operatorname{dio}(w)>1.}
\tag{7}
\]

Choose \(\rho\) strictly between \(1\) and \(\operatorname{dio}(w)\), and put
\(n=|U|+|V|\). After applying \(\chi\), the eventually periodic parity
approximant has footprint and agreement depth satisfying

\[
N\le\lambda n+\frac{2D}{c},
\qquad
M\ge\lambda\rho n-\frac Dc.
\]

Thus its agreement excess obeys

\[
G=M-N
\ge\lambda(\rho-1)n-\frac{3D}{c}.
\tag{8}
\]

The coefficient is positive, so \(G\) grows linearly with \(N\).

Condition (5), applied to all factor prefixes and suffixes, gives the same
height calculation as IEF12. Partial codewords cost only an absolute fixed
factor. Therefore the inverse of
\(\chi(U)\chi(V)^\infty\) has odd denominator and height

\[
O_D(N^2 2^N).
\tag{9}
\]

Equations (8)--(9) meet IEF11: linear agreement excess dominates the
logarithm of the polynomial height factor. Recognizability of the `00`
delimiters transfers aperiodicity through \(\chi\), so the true inverse and
the eventually periodic approximants are distinct.

> **IEF13 (discrepancy--repetition discharge).** No fixed positive integer
> realizes an aperiodic \(q=3\) block itinerary that has bounded critical
> discrepancy and Diophantine exponent greater than \(1\).

This immediately extends IEF12 to a larger low-complexity class. Bugeaud and
Kim prove that every quasi-Sturmian word satisfies

\[
\operatorname{rep}(w)
\le\sqrt{10}-\frac32.
\]

Their Lemma 10.3 gives

\[
\operatorname{dio}(w)
=\frac{\operatorname{rep}(w)}{\operatorname{rep}(w)-1}
\ge\frac53+\frac{4\sqrt{10}}{15}
>1,
\]

with the infinite-exponent case interpreted in the usual way. Hence every
critical bounded-discrepancy quasi-Sturmian block word is discharged
([Bugeaud--Kim 2019](https://doi.org/10.1090/tran/7378), Sections 3 and 10).

IEF13 leaves a precise two-axis residual frontier. Any infinite
blocked-diffuse survivor must violate at least one of

\[
\text{bounded critical discrepancy},
\qquad
\operatorname{dio}(w)>1.
\]

In other words, it must accumulate unbounded multiplicative imbalance or
have the minimum possible prefix-repetition exponent.

There is an equivalent complexity formulation. Bugeaud and Kim's elementary
inequality

\[
p(n,w)\ge r(n,w)-n
\]

shows that linear factor complexity \(p(n,w)=O(n)\) forces finite repetition
exponent. Their Lemma 10.3 then gives \(\operatorname{dio}(w)>1\). Therefore:

> **IEF13 complexity corollary.** Every aperiodic critical
> bounded-discrepancy block word of linear factor complexity is discharged.
> A survivor must have unbounded critical discrepancy or superlinear factor
> complexity.

This is strictly sharper than the label "non-Sturmian" and supplies two
measurable predicates for the next portfolio split.

The finite
[residual-axis diagnostic](../../scripts/explore_balanced_q3_residual_axes.py)
reports the maximum factor discrepancy in a tested prefix and the best
eventually periodic prefix ratio at selected footprint scales. Its default
mechanical, sparse-defect, periodic-defect, and pseudorandom families
illustrate the split. Finite values on either axis are classification data,
not proofs of bounded discrepancy or of a Diophantine exponent.

## 18. IEF14: adaptive discrepancy--repetition tradeoff

Unbounded discrepancy alone does not put a language beyond IEF11. The
periodic-prefix surplus and the discrepancy cost can be compared at the same
finite approximants.

Suppose a prefix of an aperiodic block word agrees with \(UV^\infty\). Let
\(P\) be the agreed block prefix and define

\[
A=\chi(U),
\qquad B=\chi(V),
\qquad N=|A|+|B|,
\qquad M=|\chi(P)|,
\qquad G=M-N.
\]

Measure the local discrepancy budget by

\[
K(U,V)
=\max_{F\text{ factor of }UV}
\bigl|cR(F)-2|F|\bigr|.
\]

The bounded-height argument can now be made scale-dependent. A suffix of a
parity codeword consists of a partial \(3\)- or \(4\)-block followed by the
image of a block factor. The partial block contributes an absolute constant,
while the factor multiplier contributes at most \(2^{K(U,V)}\). Hence, if
\(B\) has parity length \(e\), its periodic inverse has numerator and odd
denominator bounded by

\[
O\!\left(e2^{e+K(U,V)}\right).
\]

The affine correction of \(A\), of length \(a\), is similarly

\[
O\!\left(a2^{a+K(U,V)}\right),
\qquad
3^{|A|_1}=O\!\left(2^{a+K(U,V)}\right).
\]

Prepending \(A\) to the periodic inverse of \(B\) therefore gives the safe
height bound

\[
\boxed{
\operatorname{height}(\rho_{A,B})
=O\!\left(N^2 2^{N+2K(U,V)}\right).
}
\tag{10}
\]

Now take a sequence of such prefix completions with \(N_k\to\infty\), and
write \(G_k\) and \(K_k\) for their agreement excess and discrepancy budget.
IEF11 applies whenever

\[
\boxed{
G_k-2K_k-2\log_2N_k\longrightarrow+\infty.
}
\tag{11}
\]

> **IEF14 (adaptive discrepancy--repetition discharge).** An aperiodic
> \(q=3\) block itinerary has no fixed positive-integer realization if it has
> eventually periodic prefix approximants satisfying (11).

IEF13 is the bounded-\(K_k\) special case with linear \(G_k\). IEF14 also
discharges unbounded-discrepancy languages whenever their useful repetition
surplus outruns twice the local discrepancy budget, up to the logarithmic
height term.

Thus the live residual is narrower than the union stated after IEF13. A
candidate with unbounded discrepancy survives this rule only if, along every
available periodic-prefix approximation,

\[
G_k\le2K_k+O(\log N_k).
\]

The residual-axis diagnostic reports the finite proxy
\(G-2K-2\log_2N\) for each selected approximation. Positive finite values do
not prove divergence to infinity, but they identify the correct quantity to
track.

## 19. IEF15: negative-drift partition discharge

IEF14 uses rational approximation. A separate rule is available when the
critical discrepancy makes sufficiently deep negative excursions.

For a block prefix \(r_1,\ldots,r_L\), define its cumulative logarithmic
multiplier

\[
S_L=\sum_{j=1}^L(cr_j-2),
\qquad S_0=0.
\]

The two block maps can be written

\[
\Phi_r(x)=2^{cr-2}x+b_r,
\qquad
b_3=\frac{19}{32},
\qquad
b_4=\frac{65}{64}.
\]

Iterating exactly gives

\[
x_L
=2^{S_L}x_0
+\sum_{j=1}^L b_{r_j}2^{S_L-S_j}.
\]

Introduce the suffix partition function

\[
Z_L=\sum_{j=1}^L2^{S_L-S_j}.
\]

It has the streaming recurrence

\[
Z_{L+1}=1+2^{cr_{L+1}-2}Z_L,
\qquad Z_0=0,
\]

and yields the uniform bound

\[
\boxed{x_L\le2^{S_L}x_0+\frac{65}{64}Z_L.}
\tag{12}
\]

Normalize a hypothetical counterexample to be the least positive integer on
its trajectory. Then \(x_L\ge x_0\) at every block boundary. If there is a
subsequence \(L_k\) for which

\[
S_{L_k}\longrightarrow-\infty,
\qquad
Z_{L_k}\le B,
\]

equation (12) forces

\[
\boxed{x_0\le\frac{65}{64}B.}
\tag{13}
\]

The entire infinite language is therefore reduced to a finite verification.
In particular, if convergence is already certified through \(X\), the branch
is discharged whenever \(65B/64\le X\).

> **IEF15 (negative-drift partition discharge).** A terminal block language
> with arbitrarily deep negative cumulative discrepancy and bounded suffix
> partition function along the same subsequence contains no minimal
> counterexample above \(65B/64\), and is fully discharged after verification
> through that finite bound.

A convenient sufficient condition is uniform negative suffix drift. If, at
the selected endpoints,

\[
S_L-S_j\le-\varepsilon(L-j)
\qquad(0\le j<L),
\]

then

\[
Z_L
\le\sum_{m=0}^{\infty}2^{-\varepsilon m}
=\frac1{1-2^{-\varepsilon}}.
\]

Thus any fixed negative drift rate gives an explicit finite cutoff. The live
high-discrepancy frontier must avoid both IEF14's approximation margin and
IEF15's bounded negative-drift partition function. Large discrepancy by
itself is not a surviving mechanism.

## 20. IEF16: density-critical necessity

There is also a known global restriction on either sign of linear drift.
LÃ³pez and Stoll prove that if a rational \(2\)-adic integer has a non-cyclic
Collatz trajectory, then its lower parity density is necessarily

\[
d_*:=\frac{\log2}{\log3}
=\frac1{\log_2 3}.
\]

This applies in particular to a hypothetical positive-integer counterexample
([LÃ³pez--Stoll](https://arxiv.org/abs/2101.12747)).

At balanced-block boundaries, the number of odd shortcut steps is \(R_L\)
and the total parity length is

\[
E_L=R_L+2L.
\]

Since block lengths are at most six, taking the lower density over all parity
positions or only over block boundaries gives the same limit inferior. Put
\(t_L=R_L/L\). Then

\[
\frac{R_L}{E_L}=\frac{t_L}{t_L+2},
\qquad
\frac{S_L}{L}=ct_L-2.
\]

The first function is strictly increasing, and

\[
\frac{(2/c)}{(2/c)+2}
=\frac1{1+c}
=\frac1{\log_2 3}.
\]

Therefore the LÃ³pez--Stoll necessary condition translates exactly to

\[
\boxed{
\liminf_{L\to\infty}\frac{S_L}{L}=0.
}
\tag{14}
\]

> **IEF16 (density-critical necessity).** Every rational non-cyclic survivor
> in the \(3/4\)-block language must satisfy (14). Any branch with strictly
> positive or strictly negative linear lower discrepancy is discharged.

IEF16 removes both signs of sustained density drift before the finer rules
are needed. The negative-drift role of IEF15 is now the genuinely critical
case: sublinear excursions \(S_{L_k}\to-\infty\) with
\(S_{L_k}/L_k\to0\), where density alone says nothing but a bounded suffix
partition still gives a finite reduction. Likewise, positive discrepancy can
survive the density test only through sublinear growth or oscillation with
critical lower envelope.

## 21. IEF17: the consolidated survivor profile

The residual-frontier proposal is now an exact intersection of necessary
conditions, rather than a list of potentially overlapping ideas.

Use FIN1, the repository's exhaustive certificate that every odd
\(x\le10^6\) descends below itself. Put

\[
X=10^6,
\qquad
B_X=\frac{64X}{65}=984615.38\ldots.
\]

Consider a non-cyclic positive-integer survivor whose terminal itinerary lies
in the \(3/4\)-block language. If it is not discharged by IEF13--IEF16 or the
directional refinement IEF18, all of
the following must hold simultaneously:

| frontier coordinate | necessary survivor condition | source |
|---|---|---|
| starting size | \(x_0>X\) | FIN1 |
| density drift | \(\liminf S_L/L=0\) | IEF16 |
| symbolic/drift axis | \(\operatorname{dio}(w)=1\), or \(\limsup S_L/L>0\) | IEF16 plus IEF19 |
| periodic-prefix margin | no approximant sequence has \(G_k-J(A_k)-J(B_k)-2\log_2N_k\to+\infty\); in particular, every fixed-surplus sequence retains linear IEF21 terminal draw-up or endpoint loss | contrapositives of IEF18 and IEF21 |
| negative excursions | along every \(L_k\) with \(S_{L_k}\to-\infty\), eventually \(Z_{L_k}>B_X\) | IEF15 plus FIN1 |

The last row is exact. If infinitely many such endpoints instead had
\(Z_{L_k}\le B_X\), IEF15 would give

\[
x_0\le\frac{65}{64}B_X=X,
\]

contradicting FIN1.

> **IEF17 (consolidated non-cyclic survivor profile).** Any non-cyclic
> positive-integer survivor in the \(3/4\)-block terminal language belongs to
> the intersection of all five residual predicates in the table above.

This theorem does not say that the intersection is empty. It identifies the
single residual frontier that remains after applying the current portfolio
in order. In particular, a viable survivor must be density-critical, resist
all useful exact periodic approximations, and replenish the suffix partition
above the verified finite cutoff whenever it makes an arbitrarily deep
negative excursion.

The cyclic branch is deliberately absent from IEF17. It remains governed by
the separate cycle ledger; CYC4 only establishes that a nontrivial cycle has
no element at most \(10^6\).

## 22. IEF18: directional-height discharge

The symmetric factor budget in IEF14 is safe but wasteful. The affine
correction attached to a parity word does not inspect every factor in both
directions; it sees only particular suffixes. This gives a sharper exact
budget.

For a finite parity word \(Y\), put

\[
\delta(Y)=|Y|_1\log_2 3-|Y|
\]

and define

\[
\kappa(Y)=\max_{T\text{ suffix of }Y}\delta(T),
\qquad
J(Y)=\max\{0,\delta(Y),\kappa(Y)\}.
\tag{15}
\]

Here the empty suffix may be included, so \(\kappa(Y)\ge0\). If \(Y\) has
length \(e\), the exact affine-correction convention is

\[
C_Y=\sum_{\substack{0\le i<e\\ y_i=1}}
2^i3^{|y_{i+1}\cdots y_{e-1}|_1}.
\]

For \(T=y_{i+1}\cdots y_{e-1}\), the corresponding summand has base-two
logarithm \(i+|T|+\delta(T)=e-1+\delta(T)\). Consequently each term is

\[
O\!\left(2^{e+\kappa(Y)}\right),
\]

and therefore

\[
C_Y=O\!\left(e2^{e+\kappa(Y)}\right).
\tag{16}
\]

Indeed, the purely periodic inverse is

\[
\rho_Y=\frac{C_Y}{2^e-3^{|Y|_1}}.
\]

The denominator has odd absolute value and is at most
\(2^{e+\max(0,\delta(Y))}\). Thus the numerator and odd denominator of the
periodic inverse of \(Y\), before or after reduction, are both

\[
O\!\left(e2^{e+J(Y)}\right).
\tag{17}
\]

Now use the notation of IEF14: a block prefix agrees with \(UV^\infty\),
with parity words \(A=\chi(U)\), \(B=\chi(V)\), footprint
\(N=|A|+|B|\), and agreement excess \(G\). Prepending \(A\) to the periodic
inverse of \(B\) combines four factors: the correction of \(A\), its
multiplier \(3^{|A|_1}\), and the numerator and denominator from \(B\).
Equations (16)--(17) give

\[
\boxed{
\operatorname{height}(\rho_{A,B})
=O\!\left(N^2 2^{N+J(A)+J(B)}\right).
}
\tag{18}
\]

Hence IEF11 applies to any sequence of prefix completions for which

\[
\boxed{
G_k-J(A_k)-J(B_k)-2\log_2N_k\longrightarrow+\infty.
}
\tag{19}
\]

> **IEF18 (directional-height discharge).** An aperiodic \(q=3\) block
> itinerary has no fixed positive-integer realization if it has a sequence
> of eventually periodic prefix approximants with \(N_k\to\infty\)
> satisfying (19).

For full \(3/4\)-block words the directional budget has an exact block
formula. Let \(W=r_1\cdots r_L\), put \(s_0=0\), and set

\[
s_j=\sum_{i=1}^j(cr_i-2).
\]

Since \(\chi(r)=1^r00\), a parity suffix beginning in either terminal zero
has smaller drift than the suffix beginning at the next block. A suffix
beginning inside the run \(1^r\) is also dominated by the suffix beginning at
the start of that run, because each additional retained one contributes
\(\log_2 3-1>0\). The maximizing suffix therefore starts at a block boundary,
and

\[
\boxed{
J(\chi(W))=s_L-\min_{0\le j\le L}s_j.
}
\tag{20}
\]

In particular, \(J(A)+J(B)\le2K(U,V)\), and IEF14 follows as a coarser
corollary without an additive partial-block loss. The improvement can be
strict because large negative factor deviations and positive deviations that
occur only internally do not inflate the rational height.

The residual-axis diagnostic now reports three finite margins: the coarse
IEF14 bound, the directional bound (19), and the exact agreement minus the
bit length of the computed rational height. It also reports the IEF20 envelope
proxy \(D_k/n_k\) and the IEF21 draw-up and endpoint-loss ratios. The
exact-height margin is useful for locating slack in (18), but favorable finite
values are still not a proof of an infinite criterion.

IEF17 can consequently be sharpened by replacing its periodic-prefix row
with the contrapositive of IEF18: a survivor admits no approximant sequence
whose directional margin (19) tends to infinity.

## 23. IEF19: sublinear-drift repetition discharge

IEF18 removes the need for the uniform factor-discrepancy hypothesis in
IEF13. It is enough for the discrepancy of prefixes to be sublinear.

Let \(w=r_1r_2\cdots\) be a \(3/4\)-block word and retain

\[
S_L=\sum_{j=1}^L(cr_j-2).
\]

Suppose

\[
S_L=o(L)
\tag{21}
\]

and \(\operatorname{dio}(w)>1\). By the definition of the Diophantine
exponent, there is a fixed \(\rho>1\) and arbitrarily long prefixes agreeing
with \(U_kV_k^\infty\) for at least
\(\rho(|U_k|+|V_k|)\) blocks. Put

\[
\lambda=\frac2c+2.
\]

The \(5/6\)-bit block-length bounds alone would not prove positive parity-bit
surplus for every \(\rho>1\). The needed sharper conversion also comes from
(21). If \(E(j)=|\chi(r_1\cdots r_j)|\), then exactly

\[
E(j)=R_j+2j=\lambda j+\frac{S_j}{c}.
\tag{22}
\]

Condition (21) is uniform over the earlier prefix positions at the same
scale:

\[
\max_{0\le j\le n}|S_j|=o(n).
\tag{23}
\]

Indeed, after fixing an \(\varepsilon\), all sufficiently large \(j\) obey
\(|S_j|\le\varepsilon j\), while the finitely many earlier values contribute
\(o(n)\). The discrepancy of any factor whose endpoints are at most \(n\)
is a difference \(S_j-S_i\). The suffix of a parity code may begin inside
one block, but that partial block adds only an absolute constant.
Consequently (23) gives

\[
J(\chi(U_k))+J(\chi(V_k))=o(N_k).
\]

Write \(n_k=|U_k|+|V_k|\), and truncate the agreed prefix, if necessary, to
\(m_k=\lfloor\rho n_k\rfloor\) blocks. Equations (21)--(23) give

\[
N_k=\lambda n_k+o(n_k),
\qquad
M_k=\lambda m_k+o(n_k),
\]

and hence

\[
G_k=M_k-N_k
=\lambda(\rho-1)n_k+o(n_k).
\]

The directional margin in (19) is therefore a positive linear term minus
\(o(N_k)\), so it tends to infinity.

> **IEF19 (sublinear-drift repetition discharge).** No fixed positive integer
> realizes an aperiodic \(3/4\)-block itinerary satisfying
> \(S_L=o(L)\) and \(\operatorname{dio}(w)>1\).

This strictly broadens the usable hypothesis of IEF13: factor discrepancy
may be unbounded, provided its prefix envelope is sublinear. In particular,
critical density convergence together with linear factor complexity is enough
for discharge, even without balanced factors.

Combining IEF19 with IEF16 gives a concise survivor bifurcation. IEF16 forces
\(\liminf S_L/L=0\). If also \(\limsup S_L/L=0\), then (21) holds and IEF19
excludes every word with Diophantine exponent greater than one. Therefore

\[
\boxed{
\operatorname{dio}(w)=1
\quad\text{or}\quad
\limsup_{L\to\infty}\frac{S_L}{L}>0
}
\tag{24}
\]

for every non-cyclic positive-integer survivor in the terminal language.
Thus a repetitive survivor cannot merely have unbounded sublinear
discrepancy: it must make positive excursions of genuinely linear size.
This is the sharpened symbolic/drift row recorded in the IEF17 table.

## 24. IEF20: critical-window repetition discharge

The proof of IEF19 is local in scale. Global sublinear drift is stronger than
necessary and can be replaced by a critical envelope only along the useful
periodic-prefix approximants.

Suppose \(w\) agrees with \(U_kV_k^\infty\) for \(m_k\) blocks, put
\(n_k=|U_k|+|V_k|\to\infty\), and assume that for some fixed
\(\varepsilon>0\),

\[
m_k\ge(1+\varepsilon)n_k.
\tag{25}
\]

Define the drift envelope of that agreed window by

\[
D_k=\max_{0\le j\le m_k}|S_j|.
\tag{26}
\]

Assume

\[
D_k=o(n_k).
\tag{27}
\]

Using (22) at \(j=n_k,m_k\), the parity footprint and agreement excess obey

\[
N_k=\lambda n_k+O(D_k),
\qquad
G_k\ge\lambda\varepsilon n_k-O(D_k).
\tag{28}
\]

Every block-boundary suffix drift of \(\chi(U_k)\) or \(\chi(V_k)\) is a
difference of two prefix values \(S_j-S_i\). A suffix beginning inside one
of the two fixed codewords contributes only an absolute constant. Therefore

\[
J(\chi(U_k))+J(\chi(V_k))=O(D_k+1)=o(n_k).
\tag{29}
\]

Equations (28)--(29) make the IEF18 margin a positive linear quantity minus
\(o(n_k)\), so it tends to infinity.

> **IEF20 (critical-window repetition discharge).** No fixed positive integer
> realizes an aperiodic \(3/4\)-block itinerary having fixed-surplus periodic
> prefix approximants satisfying (25)--(27).

IEF20 contains IEF19: when \(S_L=o(L)\) and
\(\operatorname{dio}(w)>1\), choose \(1+\varepsilon\) below the Diophantine
exponent, truncate agreement to \(m_k=\lfloor(1+\varepsilon)n_k\rfloor\),
and obtain \(D_k=o(n_k)\). Its new content is on the other residual branch:
\(\limsup S_L/L>0\) is allowed, provided useful repetitions recur at later
scales where all preceding excursions are negligible relative to the new
footprint. Thus a survivor in the positive-excursion branch must keep every
fixed-surplus periodic-prefix family away from such critical windows.

The exponent-one branch also has an exact symbolic cost. In the notation of
Bugeaud--Kim, \(p(n,w)\ge r(n,w)-n\), and finite
\(\liminf p(n,w)/n\) forces finite repetition exponent and hence
\(\operatorname{dio}(w)>1\). Consequently

\[
\operatorname{dio}(w)=1
\quad\Longrightarrow\quad
\frac{p(n,w)}n\longrightarrow\infty.
\tag{30}
\]

This is a residual classification, not a discharge rule: terminal PCD or
cylinder ancestry has not yet been proved to forbid the superlinear
complexity in (30).

All of IEF18--IEF21 are stated for aperiodic itineraries. This is the correct
qualification for the non-cyclic frontier: under the parity conjugacy, an
eventually periodic parity tail has a unique rational periodic inverse, so a
positive integer realizing it is preperiodic to an integer cycle. Such a
trajectory belongs to the separate cycle ledger, not to IEF17.

## 25. IEF21: directional-valley transition discharge

Formula (20) removes the full-envelope hypothesis from IEF20. Suppose an
aperiodic word agrees with \(U_kV_k^\infty\) for \(m_k\) blocks. Write

\[
u_k=|U_k|,
\qquad
n_k=|U_k|+|V_k|\to\infty,
\]

and assume for some fixed \(\varepsilon>0\) that

\[
m_k\ge(1+\varepsilon)n_k.
\tag{31}
\]

Define the two terminal draw-ups at the preperiod and period cuts by

\[
H_k=
\left(S_{u_k}-\min_{0\le j\le u_k}S_j\right)
+\left(S_{n_k}-\min_{u_k\le j\le n_k}S_j\right),
\tag{32}
\]

and define the loss of drift from the footprint endpoint to the agreement
endpoint by

\[
L_k=(S_{n_k}-S_{m_k})_+.
\tag{33}
\]

Assume

\[
H_k=o(n_k),
\qquad
L_k=o(n_k).
\tag{34}
\]

Formula (20) is exact on the two factors, so

\[
J(\chi(U_k))+J(\chi(V_k))=H_k.
\tag{35}
\]

The code-length identity (22) also gives the exact agreement excess

\[
G_k
=\lambda(m_k-n_k)+\frac{S_{m_k}-S_{n_k}}c
\ge\lambda\varepsilon n_k-\frac{L_k}{c}.
\tag{36}
\]

Thus (34)--(36) make the IEF18 margin grow linearly.

> **IEF21 (directional-valley transition discharge).** No fixed positive
> integer realizes an aperiodic \(3/4\)-block itinerary having fixed-surplus
> periodic-prefix approximants satisfying (31)--(34).

IEF21 contains IEF20 because \(D_k=o(n_k)\) bounds both terminal draw-ups and
the endpoint loss. It is strictly less pessimistic about oscillation: an
arbitrarily large positive internal excursion creates no height cost if the
preperiod and period cuts return near their respective past minima, and it
creates no agreement penalty if the drift has not fallen linearly farther by
the agreement endpoint. Consequently a survivor in the positive-excursion
branch must keep a linear terminal draw-up or a linear post-footprint loss on
every fixed-surplus periodic approximation. Large peaks by themselves are no
longer a residual predicate.

## 26. Relation to the critical parity-density boundary

Under the shortcut map, a balanced prefix has \(R_L\) odd steps among
\(E_L=R_L+2L\) total steps. The mechanical definition gives

\[
\frac{R_L}{E_L}\longrightarrow\frac1{\log_2 3}
=\frac{\log 2}{\log 3}.
\]

This is the known critical boundary for rational \(2\)-adic divergence.
López and Stoll prove that a divergent rational \(2\)-adic trajectory must
have lower parity density exactly \(\log 2/\log 3\), and they explicitly study
Sturmian parity vectors at that boundary
([arXiv:2101.12747](https://arxiv.org/abs/2101.12747)). Their result explains
why a strict real-drift argument does not remove the balanced word; it does
not prove or refute the IEF3 least-representative bound.

## 27. Guardrails

- Finite occurrence of nonzero lifts does not prove integral escape.
- Density zero of eventually-zero paths does not prove their absence.
- A rule that merely classifies a branch is not a discharge rule.
- The residual tree must retain primitivity and prior-descent information;
  PCD9 shows that finite cylinder compatibility alone is automatic.
- If the goal remains an explicit linear stopping-time bound, the weaker IEF
  terminal condition is not sufficient by itself.
- The finite exponential growth of the dual residues is evidence only. A
  proof must control their least positive representatives, not merely the
  size of the moduli \(3^{R_L}\).
- IEF7 shows that the two finite digit censuses are the same certificate;
  they must not be counted as independent evidence.
- The bridge cylinder enforces at least the scheduled divisibility. Eventual
  stabilization alone does not prove exact intermediate valuations.
- The finite bound \(v_2(\Delta_k)\le4\) is not promoted. IEF8 promotes only
  the exact concatenation law and the conditional valuation reduction.
- Complex Hecke--Mahler transcendence inside
  \(\lvert z_1z_2^\theta\rvert<1\) cannot be quoted at the equality boundary.
  IEF9 requires a genuinely \(2\)-adic value theorem or a direct
  irrationality proof.
- IEF10 eliminates the one deterministic infinite balanced itinerary. It
  must not be promoted to repunit-tail descent until the residual portfolio
  proves that every other infinite branch is discharged or reduced to it.
- IEF11 eliminates every fixed phase shift and any other language satisfying
  its four hypotheses. It does not prove that all terminal PCD branches have
  those approximants; that classification remains open.
- IEF12 eliminates every Sturmian intercept at the critical slope. It does
  not prove that every blocked-diffuse branch is Sturmian; equal asymptotic
  density alone is far weaker than balance and factor complexity \(n+1\).
- IEF13 requires uniform discrepancy on every finite factor, not merely
  convergence to the critical asymptotic density. Taken alone, its
  complementary frontier is unbounded discrepancy or superlinear complexity;
  IEF19 subsequently removes the sublinear-prefix-drift part when
  \(\operatorname{dio}(w)>1\).
- IEF14 can discharge some unbounded-discrepancy languages, but only from an
  infinite sequence for which the adaptive margin in (11) tends to infinity.
  A positive margin in a finite diagnostic is not a proof.
- IEF15 is a finite-reduction theorem. Its conclusion requires an actual
  convergence certificate through \(65B/64\), and the negative discrepancy
  and bounded partition function must occur on the same subsequence.
- IEF16 is a necessary density condition imported from LÃ³pez--Stoll. It does
  not by itself discharge sublinear unbounded discrepancy or prove that
  critical lower density is sufficient for a counterexample; IEF19
  additionally needs repetition exponent greater than one. IEF16 concerns
  non-cyclic trajectories; the separate cycle ledger is still required.
- IEF17 is an intersection of necessary conditions, not a proof that the
  residual intersection is empty. Its numerical partition cutoff uses this
  repository's FIN1 certificate through \(10^6\), not a larger external
  verification claim.
- IEF18 sharpens the height estimate but still requires an infinite sequence
  on which (19) diverges. Neither a positive finite directional margin nor a
  positive exact-height diagnostic is a discharge theorem by itself.
- IEF19 requires full sublinear prefix drift \(S_L=o(L)\), not merely the
  lower-envelope equality \(\liminf S_L/L=0\). Its complementary repetitive
  branch has positive linear limsup; IEF19 does not yet discharge that branch.
- IEF20 only discharges a positive-excursion word when fixed-surplus periodic
  approximants occur along scales with the full earlier drift envelope
  \(D_k=o(n_k)\). IEF21 is sharper: internal peaks do not matter by
  themselves, but both terminal draw-up \(H_k\) and post-footprint endpoint
  loss \(L_k\) must be sublinear on the same approximant sequence.
- IEF21 does not prove that every oscillatory itinerary supplies suitable
  periodic approximants. Its exact residual is the alternative that every
  fixed-surplus approximant has linear terminal draw-up or linear endpoint
  loss along a subsequence.
- The implication \(\operatorname{dio}(w)=1\Rightarrow p(n,w)/n\to\infty\)
  classifies the exponent-one branch but does not discharge it. No terminal
  Collatz ancestry theorem currently rules out that complexity growth.

The framework changes the proof target, not the standard of proof: the final
disjointness from positive integers must be deterministic and exact.
