# Binary Fuel and Bad-Block Suffix Gates

**Building on:** `recharge_nogo.md`, `martingale_logspace_perspective.md`,
`entropy_nonshadowing_theory.md`

**Status:** Exploratory / proof target. This note records a possible
2-adic language for long low-surplus episodes. It does not prove Collatz and
is not a dependency of the proved-results track.

---

## 1. Block coordinates

For an odd integer \(x\), write

\[
x=2^t u-1,\qquad u\text{ odd},\qquad t=v_2(x+1).
\]

The first \(t-1\) odd-steps are the deterministic trailing-one burn from
`recharge_nogo.md`: while the trailing-one count is at least \(2\), the
valuation is \(1\). Collapsing the whole burn plus the terminal payout gives

\[
x^+=\frac{3^t u-1}{2^a},
\qquad
a=v_2(3^t u-1).
\]

If the next state has new fuel

\[
x^+=2^r u^+-1,\qquad r=v_2(x^+ + 1),
\]

then the block is encoded by the triple

\[
(t,a,r).
\]

The block has \(t\) odd-steps and total valuation \(t+a\). Its log-space
surplus over the break-even multiplier \(3^t\) is

\[
\Delta(t,a)=t+a-t\log_2 3
=a-t\log_2(3/2).
\]

Call a block **bad** when

\[
a<t\log_2(3/2).
\]

Bad blocks are precisely those that create 2-debt at the collapsed
burn/payout scale.

The exact value change across one block is

\[
\log_2\frac{x^+}{x}
=t\log_2(3/2)-a+\varepsilon(x)
=-\Delta(t,a)+\varepsilon(x),
\]

where

\[
\varepsilon(x)=
\log_2
\frac{1-\frac1{3^t u}}
     {1-\frac1{2^t u}}
>0.
\]

Thus cumulative block surplus is the negative of log-growth, up to a positive
finite-size correction. Descent over a block interval is forced once

\[
\sum \Delta(t_i,a_i)>\sum \varepsilon(x_i).
\]

For large states the correction is tiny; for a proof it must still be bounded
explicitly.

A crude useful bound is available before descent. Since

\[
\varepsilon(x)
=\log_2\left(1+
\frac{(3^t-2^t)u}{3^t u(2^t u-1)}\right),
\]

one has, for \(x=2^t u-1\) large enough,

\[
0<\varepsilon(x)\le \frac{4}{(x+1)\ln2}.
\]

Therefore, over any pre-descent interval of \(B\) blocks from a start \(x_0\),

\[
\sum\varepsilon(x_i)\le \frac{4B}{(x_0+1)\ln2}.
\]

This is very weak but sufficient to explain why the correction is
exponentially tiny in the Mersenne-spike tests: the spike starts have
\(x_0\asymp 2^R\).

---

## 2. The recharge gate

The equation

\[
\frac{3^t u-1}{2^a}=2^r u^+-1
\]

is equivalent to

\[
3^t u+2^a-1=2^{a+r}u^+.
\]

Thus a block with prescribed \((t,a,r)\) forces the exact 2-adic residue

\[
u\equiv (1-2^a)3^{-t}\pmod{2^{a+r}}.
\]

For the common bad case \(a=1\), this becomes

\[
u\equiv -3^{-t}\pmod{2^{1+r}}.
\]

So a bad/recharge block has binary suffix shape

\[
x = \underbrace{11\cdots1}_{t\text{ bits}}\;[\text{low bits of }-3^{-t}]
\]

in least-significant-bit order. Long dangerous episodes therefore require
nested inverse-power-of-3 suffix templates, not merely long runs of ones.

The forward transition on the free tail is

\[
u^+=\frac{3^t u+2^a-1}{2^{a+r}}.
\]

Equivalently, if

\[
u=(1-2^a)3^{-t}+2^{a+r}w
\]

in \(\mathbb Z_2\), then \(u^+\) is an affine function of the free tail \(w\).
Each block peels off a forced low-bit template and passes the remaining tail
forward.

---

## 3. Finite chains have an exact backward form

For a finite block chain

\[
(t_0,a_0,r_0),\ldots,(t_{N-1},a_{N-1},r_{N-1}),
\]

the backward transition is

\[
u_i=\frac{2^{a_i+r_i}u_{i+1}-2^{a_i}+1}{3^{t_i}}.
\]

Composing gives

\[
u_0=\frac{A u_N+B}{3^T},
\qquad
T=t_0+\cdots+t_{N-1},
\]

where \(A\) is a power of \(2\) and \(B\in\mathbb Z\). Therefore finite-chain
realizability by positive integers is reduced to one congruence:

\[
A u_N+B\equiv0\pmod{3^T}.
\]

Since \(A\) is invertible modulo \(3^T\), there is one residue class for the
free terminal odd part \(u_N\). Choosing its least positive odd representative
gives the least positive start for that exact block chain.

This exactly reconstructs the finite record bad-block chains observed by the
diagnostic. For example:

| chain source | least start recovered |
|---|---:|
| \((2,1,5),(5,1,1)\) | \(27\) |
| \((6,3,2),(2,1,3),(3,1,4),(4,1,1)\) | \(63\) |
| the 7-block record chain | \(4591\) |
| the 11-block record chain | \(1464571\) |

Thus long bad-block shadowing is an arithmetic progression problem in the
terminal tail \(u_N\), with modulus \(3^T\), together with the 2-adic suffix
gates from the forward view.

The exact backward form also gives a practical search method: enumerate
candidate bad-block words, compute the least positive \(u_N\) in the required
class modulo \(3^T\), and recover the least positive start. A bounded beam
search in `explore_binary_fuel_blocks.py` rediscovers the finite record chains
and proposes longer finite shadows. For instance it finds

\[
5520123
\]

with 12 consecutive bad blocks:

\[
\begin{aligned}
&(2,1,2),(2,1,3),(3,1,2),(2,1,2),(2,1,4),(4,2,2),\\
&(2,1,2),(2,1,2),(2,1,4),(4,1,5),(5,1,6),(6,1,1),
\end{aligned}
\]

followed by the good block \((1,1,1)\). This is a diagnostic only; the beam
search is not exhaustive unless its truncation parameters are justified.

With a wider beam it also finds

\[
23974592507
\]

with 16 consecutive bad blocks:

\[
\begin{aligned}
&(2,1,2),(2,1,2),(2,1,2),(2,1,4),(4,1,2),(2,1,2),\\
&(2,1,2),(2,1,3),(3,1,2),(2,1,2),(2,1,2),(2,1,3),\\
&(3,1,4),(4,2,6),(6,2,4),(4,1,2),
\end{aligned}
\]

followed by the good block \((2,4,2)\). The long examples are dominated by
cheap near-neutral moves such as \((2,1,2)\) and \((2,1,3)\), with occasional
larger recharge/payout blocks. This supports the view that the remaining
enemy is a nonperiodic near-threshold path, not an obvious high-debt periodic
cycle.

The cheap motifs themselves still obey the negative-ghost rule when closed
periodically. For example, the fuel cycle

\[
(2,1,3),(3,1,2)
\]

has affine action on the odd part

\[
u\mapsto \frac{243}{128}u+\frac{43}{128},
\]

so its fixed odd part is

\[
u=-\frac{43}{115}.
\]

The diagnostic command

```bash
python explore_binary_fuel_blocks.py --inspect-chain "2,1,3;3,1,2"
```

prints this affine map and its least positive finite shadower \(x=603\).

A still wider beam finds the verified 20-bad-block shadower

\[
162188907526907,
\]

whose bad prefix is

\[
\begin{aligned}
&(2,1,2),(2,1,3),(3,1,2),(2,1,2),(2,1,2),(2,1,3),\\
&(3,1,2),(2,1,2),(2,1,2),(2,1,2),(2,1,2),(2,1,2),\\
&(2,1,4),(4,1,2),(2,1,2),(2,1,3),(3,1,2),(2,1,2),\\
&(2,1,2),(2,1,1),
\end{aligned}
\]

followed by the good block \((1,4,4)\). This example is almost entirely
assembled from the two cheap motifs \((2,1,2)\) and
\((2,1,3),(3,1,2)\), reinforcing the near-threshold symbolic picture.

It is useful to name the smallest motifs:

\[
A=(2,1,2),\qquad B=(2,1,3),(3,1,2),\qquad
C=(2,1,4),(4,1,2).
\]

Their affine actions on the odd part \(u\) are

\[
A:u\mapsto \frac98u+\frac18,
\]

\[
B:u\mapsto \frac{243}{128}u+\frac{43}{128},
\]

\[
C:u\mapsto \frac{729}{256}u+\frac{113}{256}.
\]

Each has slope \(>1\) and positive intercept, hence each has a negative real
fixed point. More generally, any periodic word in bad motifs that returns to
the same fuel level has slope \(3^T/2^E>1\) and positive intercept, hence a
negative real fixed point. The verified 20-block example parses essentially
as

\[
ABAABAAAAACABAA
\]

followed by the terminal bad block \((2,1,1)\) and then the good escape
\((1,4,4)\).

For this reduced alphabet there is a stronger observation. The inverse maps
are

\[
A^{-1}:u\mapsto \frac89u-\frac19,
\]

\[
B^{-1}:u\mapsto \frac{128}{243}u-\frac{43}{243},
\]

\[
C^{-1}:u\mapsto \frac{256}{729}u-\frac{113}{729}.
\]

They are real contractions with negative offsets. Therefore every infinite
backward word over \(\{A,B,C\}\) converges in the real topology to a negative
odd-part ghost. Positive finite shadows in this subsystem can only occur by
choosing a sufficiently large terminal tail \(u_N\) before pulling back
through the inverse contractions.

This gives a concrete mini-version of the desired non-shadowing principle:
the most common near-threshold bad loops already form a negative real
iterated-function system. A positive infinite counterexample must either
leave this reduced subsystem infinitely often or exploit a more delicate
nonperiodic balance of larger fuel states.

The same sign mechanism applies to any **return motif**: a finite bad block
word that starts and ends at the same fuel level. Its action on the odd part
has the form

\[
u\mapsto \frac{3^T}{2^H}u+\beta,\qquad \beta>0,
\]

where \(T\) is the total burned fuel and \(H=\sum_i(a_i+r_i)\) is the total
division in the odd-part coordinate. For a return motif, \(H\) differs from
the full odd-step valuation \(E\) only by the common endpoint fuel, so
negative block surplus gives \(3^T/2^H>1\). The fixed odd part is then

\[
u=\frac{\beta}{1-3^T/2^H}<0.
\]

A finite enumeration of return motifs from fuel \(2\) back to fuel \(2\)
through four blocks and fuel states \(\le8\) shows only this negative-fixed
point behaviour. This is expected from the sign argument, not evidence of a
special finite accident.

### High-recharge spike family

Large fuel excursions are possible at surprisingly small cost. The single
bad block

\[
(2,1,R)
\]

has backward equation

\[
u_0=\frac{2^{R+1}u_1-1}{9}.
\]

Thus \(u_1\) is determined modulo \(9\) by

\[
2^{R+1}u_1\equiv1\pmod9.
\]

When \(R\equiv5\pmod6\), the least positive odd choice is \(u_1=1\), giving

\[
x_0=4\frac{2^{R+1}-1}{9}-1,
\qquad
x_1=2^R-1.
\]

So a cheap bad block can recharge directly to the Mersenne spine. Examples:

\[
27\to31,\qquad 1819\to2047,\qquad 116507\to131071.
\]

The following Mersenne burn block is \((R,1,1)\) for odd \(R\), adding large
2-debt. This family shows that "large recharge forces a huge start" is only
true up to exponential scale and periodic constants; high recharges can occur
through very structured low-height gates. Any proof target must account for
these Mersenne-spike excursions.

Finite recovery diagnostic. For \(R\equiv5\pmod6\), \(5\le R\le299\), the
script finds that the first block time at which cumulative block surplus
becomes positive enough to beat the correction is exactly the first block
time at which the orbit descends below the spike start \(x_0\). In this
range, the first nonnegative cumulative surplus already suffices. No
exception occurs in this range. The worst tested recovery length is 239
blocks at \(R=299\).

This suggests a possible spike-recovery lemma:

> In the exact Mersenne-spike family, descent below the spike start occurs
> when the post-spike block-surplus ledger first exceeds the accumulated
> finite-size correction; empirically, the first nonnegative surplus crossing
> already does this in the tested range.

Such a lemma would not prove Collatz, but it would remove a major unbounded
fuel excursion family from the bad-shadowing enemy set.

---

## 4. Periodic bad ghosts are negative

Suppose a block or valuation pattern repeats periodically. Across one period
let \(T\) be the number of odd-steps and \(E\) the total valuation. The
composed map has the affine form

\[
x\mapsto \frac{3^T x+C}{2^E},\qquad C>0.
\]

A fixed point satisfies

\[
x=\frac{3^T x+C}{2^E},
\qquad
x=\frac{C}{2^E-3^T}.
\]

If the period is bad, then \(E<T\log_2 3\), equivalently \(2^E<3^T\). Hence

\[
2^E-3^T<0
\]

and the real fixed point is negative.

Thus periodic bad suffix patterns naturally define 2-adic ghosts, but their
ordinary real value lies on the negative side. A positive counterexample
would have to follow a nonperiodic infinite bad/recharge path, or else
accumulate enough 2-surplus on some interval to force descent.

Example: the repeated block \((t,a,r)=(4,1,4)\) gives

\[
x=16u-1,\qquad x^+=\frac{81u-1}{2}.
\]

The fixed block equation \(x^+=x\) gives

\[
u=-1/49,\qquad x=-65/49.
\]

The finite residues of this negative 2-adic rational appear as projected
cycles in low-bit suffix graphs, but ordinary positive representatives do not
remain on the bad cycle.

---

## 5. Infinite low-surplus ghosts

For a prescribed infinite odd-step valuation path

\[
e_0,e_1,e_2,\ldots,
\qquad E_j=e_0+\cdots+e_{j-1},
\]

the corresponding starting residue classes converge in \(\mathbb Z_2\) to
the ghost

\[
x_*=-\sum_{j=0}^{\infty}\frac{2^{E_j}}{3^{j+1}}.
\]

The 2-adic convergence is automatic because \(E_j\to\infty\). As an ordinary
real series, every term inside the sum is positive. Hence whenever the real
series converges, its real value is negative.

A sufficient real-convergence condition is persistent 2-debt, for example

\[
E_j-j\log_2 3\le -\epsilon j
\]

eventually. Thus any path with strong permanent 2-debt defines a negative
real ghost, not a positive integer.

The remaining dangerous case is the near-threshold regime where

\[
E_j-j\log_2 3
\]

keeps returning upward. But those upward returns are precisely the accumulated
2-surplus events that can force descent once the affine correction is
controlled. This suggests the dichotomy:

1. persistent 2-debt \(\Rightarrow\) negative real ghost;
2. recurring 2-surplus \(\Rightarrow\) interval-descent pressure.

The hard part is proving the second branch with enough control over the
affine \(+1\) correction.

---

## 6. Periodic block words

The single-block example is not special. Any periodic block word has an
affine period map

\[
x\mapsto \frac{3^T x+C}{2^E},\qquad C>0,
\]

where \(T\) is the period's total odd-step length and \(E\) is its total
valuation. If the period has negative block surplus,

\[
E<T\log_2 3,
\]

then the real fixed point is negative. Consequently every eventually
periodic bad-block suffix path lands on a negative rational 2-adic ghost.

This leaves only nonperiodic bad-block paths as possible positive
shadowing obstructions.

---

## 7. Finite suffix-graph diagnostic

The script `explore_binary_fuel_blocks.py` treats resolved low-bit residues
modulo \(2^M\) as states. A state has a fully resolved bad edge only when the
available low bits determine \(t,a,r\), the next residue, and
\(\Delta(t,a)<0\). Otherwise it is counted as good or ambiguous.

The finite diagnostic through \(M=18\) shows no fully resolved bad-only
cycles. At \(M=20\), the first projected bad cycle is the fixed residue of
the repeated \((4,1,4)\) ghost above; exact integer replay immediately leaves
the projected cycle after more high bits are exposed.

This supports, but does not prove, the heuristic:

> Bad blocks peel forced suffix templates. Infinite bad suffix paths exist in
> \(\mathbb Z_2\), but the evident periodic ones are negative real ghosts.
> A positive orbit must either leave the bad graph or follow a nonperiodic
> ghost path.

---

## 8. Proof target

A useful next theorem would be a non-shadowing statement for positive
integers:

> No positive integer can follow an infinite bad-block suffix path.

A weaker but still useful version would show that every sufficiently long
positive bad-block chain either:

1. reaches a block with enough positive surplus to force interval descent; or
2. shadows an eventually periodic bad 2-adic ghost, hence a negative rational
   fixed point.

The return-motif sign argument suggests a more focused target:

> Any infinite bad-block path with bounded fuel states decomposes into
> infinitely many bad return motifs, and therefore has a negative real
> backward limit.

If true, a positive counterexample would need unbounded fuel excursions while
remaining near the surplus threshold. That would be a much narrower
arithmetic problem: control the 2-adic gates required to create arbitrarily
large recharges without allowing a compensating payout.

The present note only isolates the block coordinates and the exact 2-adic
gates where such a proof might live.
