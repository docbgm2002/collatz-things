# An Extremal Principle for Primitive Repunit Tails

**Building on:** `repunit_tail_merge_reduction.md`,
`repunit_low_prefix_obstruction.md`,
`repunit_baker_applicability_census.md`

**Status:** Exact bookkeeping lemmas and a sharpened proof target. The
primitive storage/collision lemma stated below is open.

---

## 1. Why look only at deficit records?

For an odd repunit exponent \(n\), write

\[
x_K=f^{(K)}(a_n),\qquad
E_K=\sum_{i<K}e_i,\qquad
e_i=v_2(3x_i+1).
\]

Define the valuation deficit

\[
D_K=K\log_2 3-E_K.
\]

Then

\[
D_{K+1}-D_K=\log_2 3-e_K.
\]

Because \(e_K\) is a positive integer, a strict new deficit record can occur
only when

\[
\boxed{e_K=1.}
\]

Thus the extremal states are not spread arbitrarily through the trajectory.
They occur inside valuation-one runs, precisely where the enemy coordinate
from `repunit_baker_applicability_census.md` is constant.

This is the first useful compression: any proof controlling record deficits
automatically controls every intermediate deficit.

---

## 2. The exact storage coordinate

Use the repunit normal form

\[
x_K=\frac{3^{n+K}+A_K}{2^{E_K+1}},
\qquad
A_{K+1}=3A_K+2^{E_K+1}.
\]

Set

\[
R_K=A_K+2^{E_K+1},
\qquad
Z_K=\frac{R_K}{2^{E_K+1}}.
\]

Since \(R_0=1\) and

\[
R_{K+1}
=3R_K+2^{E_K+1}(2^{e_K}-2),
\]

we have \(R_K>0\) for every \(K\). Moreover,

\[
\boxed{
Z_{K+1}
=1+\frac{3Z_K-2}{2^{e_K}}.
}
\]

The normal form becomes

\[
\boxed{
x_K+1
=\frac{3^{n+K}}{2^{E_K+1}}+Z_K.
}
\]

The quantity \(Z_K\) is the normalized correction stored by the valuation
history.

---

## 3. Exact conservation during an extremal run

If \(e_K=1\), then

\[
Z_{K+1}=\frac32 Z_K.
\]

Hence over a valuation-one run of length \(L\),

\[
Z_{K+L}=\left(\frac32\right)^L Z_K
\]

and

\[
D_{K+L}-D_K
=L(\log_2 3-1)
=\log_2 Z_{K+L}-\log_2 Z_K.
\]

Therefore

\[
\boxed{
D_K-\log_2 Z_K
\text{ is constant throughout every valuation-one run.}
}
\]

This gives a literal interpretation of a growing deficit: it is not free
growth. During every extremal run, exactly the same number of bits is placed
into the normalized correction \(Z_K\).

At a payout \(q=e_K\ge2\),

\[
\boxed{
Z_{K+1}=1+\frac{3Z_K-2}{2^q}.
}
\]

Thus a payout both earns valuation surplus and damps the inherited
\(3Z_K\) contribution by the factor \(2^{-q}\). Because the
recurrence also adds \(1-2^{1-q}\), \(Z_{K+1}\) need not be smaller than
\(Z_K\) when \(Z_K\) itself is small. The exact statement is damping of the
inherited correction, not unconditional contraction of \(Z_K\).

---

## 4. Exact payout decomposition

Put

\[
B_K=\frac{Z_K}{2^{D_K}}.
\]

Since

\[
D_{K+1}=D_K+\log_2 3-e_K,
\]

the recurrence for \(Z_K\) gives

\[
\boxed{
B_{K+1}
=B_K+
\left(1-2^{1-e_K}\right)2^{-D_{K+1}}.
}
\]

Because \(B_0=1/2\), iteration yields the exact ledger

\[
\boxed{
B_K
=\frac12+
\sum_{\substack{0\le j<K\\e_j>1}}
\left(1-2^{1-e_j}\right)2^{-D_{j+1}}.
}
\]

Equivalently,

\[
\boxed{
Z_K
=2^{D_K}\left[
\frac12+
\sum_{\substack{0\le j<K\\e_j>1}}
\left(1-2^{1-e_j}\right)2^{-D_{j+1}}
\right].
}
\]

Thus:

- \(B_K\) is positive and nondecreasing;
- it changes only at payouts \(e_j>1\);
- a payout made after a deep surplus, meaning very negative \(D_{j+1}\),
  creates a large permanent contribution to \(B_K\);
- later valuation-one runs amplify the entire stored budget uniformly by
  \(2^{D_K}\).

There is also an integer form:

\[
\boxed{
R_K
=3^K+
\sum_{j<K}
3^{K-1-j}2^{E_j+1}(2^{e_j}-2).
}
\]

Only payout times contribute to the sum.

### Collision-shell decomposition of each payout

Let

\[
P(E,q)=2^{E+1}(2^q-2)
\]

be the correction injected by a payout \(q>1\) when the pre-payout
cumulative valuation is \(E\). Define

\[
S(u,2h)=2^{u+1}\frac{2^{2h}-1}{3},
\]

the exact displacement occurring in the collision-shell theorem.

If \(q\) is odd, put \(2h=q-1\) and \(u=E+1\). Then

\[
\boxed{P(E,q)=3S(E+1,q-1).}
\]

If \(q\) is even, put \(2h=q\) and \(u=E\). Then

\[
\boxed{P(E,q)=3S(E,q)-S(E,2),}
\]

because \(S(E,2)=2^{E+1}\). Consequently, after transport from payout time
\(j\) to time \(K\), its contribution to \(R_K\) is

\[
3^{K-j}S(E_j+1,e_j-1)
\qquad(e_j\ {\rm odd}),
\]

or

\[
3^{K-j}S(E_j,e_j)
-3^{K-1-j}S(E_j,2)
\qquad(e_j\ {\rm even}).
\]

Thus every payout carries an exact collision-shell atom. Odd payouts are pure
transported shell atoms; even payouts are a positive transported shell atom
minus one transported smallest-shell atom. In particular, a \(q=2\) payout
is simply

\[
P(E,2)=2S(E,2).
\]

For every payout time \(j\), define

\[
(U_j,V_j)=
\begin{cases}
\bigl(S(E_j+1,e_j-1),0\bigr),&e_j\text{ odd},\\
\bigl(S(E_j,e_j),S(E_j,2)\bigr),&e_j\text{ even}.
\end{cases}
\]

Then the entire correction has the exact shell-ancestry expansion

\[
\boxed{
R_K
=3^K+
\sum_{\substack{j<K\\e_j>1}}3^{K-j}U_j
-
\sum_{\substack{j<K\\e_j>1}}3^{K-1-j}V_j.
}
\]

This is an algebraic bridge, not yet a shell-hitting theorem. A shell atom
inside the correction expansion does not by itself produce a second
repunit-tail state at the required diagonal.

### Canonical virtual collision partner

Suppose the payout \(e_j=q\ge2\) sends the tail to

\[
X=x_{j+1}
=\frac{3^d+A_{j+1}}{2^{F+1}},
\qquad
d=n+j+1,
\qquad
F=E_j+q.
\]

Put

\[
h=\left\lfloor\frac q2\right\rfloor,
\qquad
u=F-2h
=
\begin{cases}
E_j+1,&q\text{ odd},\\
E_j,&q\text{ even}.
\end{cases}
\]

Define

\[
\boxed{
Y=4^hX+\frac{4^h-1}{3}.
}
\]

Then \(Y\) is odd and

\[
3Y+1=4^h(3X+1),
\]

so

\[
\boxed{f(Y)=f(X).}
\]

Moreover,

\[
Y
=\frac{3^d+A_{j+1}+S(u,2h)}{2^{u+1}}.
\]

Thus \(X\) and \(Y\) are exactly the high- and low-cumulative states on the
collision shell selected by the payout. Every payout \(q\ge2\) therefore
creates a canonical **virtual collision partner** one odd step away from
coalescence.

The word “virtual” is essential. The integer \(Y\) need not lie on the
pre-descent tail of any smaller repunit exponent. Establishing that
reachability, or proving that repeated failure of reachability forces
surplus, is the remaining arithmetic problem.

Finally, the state itself has the exact decomposition

\[
\boxed{
x_K+1
=2^{D_K}\left(\frac{3^n}{2}+B_K\right).
}
\]

This is an exact conservation law, not an approximation. The ordinary
exponential \(3^n/2\), the current deficit \(2^{D_K}\), and the accumulated
payout budget \(B_K\) account for the whole state.

---

## 5. The enemy equation revisited

Factor

\[
R_K=3^{r_K}d_K,\qquad 3\nmid d_K,
\]

and put

\[
m_K=n+K-r_K.
\]

Oddness of \(x_K\) gives

\[
\boxed{
v_2(3^{m_K}+d_K)\ge E_K+2.
}
\]

During a valuation-one run, \(R\) is multiplied by \(3\). Consequently
\((m_K,d_K)\) stays fixed while \(E_K\), \(D_K\), and \(\log_2 Z_K\) each
advance predictably.

There are therefore two genuinely different extremal regimes:

1. **Low reduced height.**  The integer \(d_K\) is small relative to
   \(2^{E_K}\). When its height is fixed or otherwise controlled,
   Archimedean size and \(2\)-adic logarithmic-form estimates can bound the
   run. The fixed-\(7\) ghost branch is the model case.
2. **High reduced height.**  Most of the required \(2\)-adic information is
   carried by \(d_K\). Modulus size alone says nothing; the way \(d_K\) was
   created by earlier payouts must be used.

The second case is the real residual problem.

---

## 6. Candidate primitive storage/collision lemma

The next theorem should not assert a fixed block floor or a local recovery
time. Both formulations are defeated by the nested low-prefix classes.

A viable statement must use the full correction ancestry and primitivity:

> **Primitive storage/collision lemma (open).**  
> Let \(K\) be a strict record time for \(D_K\) on an active repunit tail.
> Trace \(R_K\) backwards through its most recent payout transitions. Then
> either:
>
> 1. the reduced enemy constant has sufficiently low height for an effective
>    Archimedean/Baker non-shadowing bound; or
> 2. the high-height part of \(R_K\) contains an earlier correction state
>    satisfying one of the exact affine collision-shell relations with a
>    smaller exponent; or
> 3. the payouts that created that high-height part already contribute enough
>    cumulative valuation to prevent \(K\) from being an extremal obstruction
>    in a linear window.

This is deliberately a three-way statement. The existing episode experiment
rules out replacing item 3 by a bound involving only the immediately
preceding valuation-one run.

The proof problem is now algebraic: decompose

\[
R_K
=3^K+
\sum_{j<K}3^{K-1-j}2^{E_j+1}(2^{e_j}-2)
\]

and show that a large surviving summand is either paid for by its valuation
\(e_j\) or reproduces a collision-shell correction from an earlier repunit
tail.

The payout-shell decomposition sharpens the unresolved part. Every correction
is assembled from transported collision-shell displacements, but a formal
linear combination of shell displacements is not automatically a reachable
state from a smaller exponent. The missing theorem is therefore a
reachability or ancestry statement, not merely another algebraic
factorization.

---

## 7. First finite diagnostic

`scripts/explore_repunit_extremal_prefixes.py` removes all tails that merge into
smaller exponents, then reports only strict record times of \(D_K\).

For odd \(n\le2001\), it finds:

- \(117\) primitive tails;
- \(262\) strict record-deficit prefixes, where \(D_0=0\) is included in the
  comparison;
- every record increment occurs at valuation \(1\), as the exact lemma
  predicts;
- the largest record deficits generally have reduced enemy height comparable
  to or exceeding \(E_K\);
- low-height records do occur, including the fixed-\(7\) family, but they are
  not the generic extremal case;
- payout storage is often concentrated, but not universally in one term:
  among the \(262\) record prefixes, the largest payout contribution supplies
  at least half of \(B_K\) in \(110\) cases and less than one quarter in
  \(17\) cases;
- the three largest payout contributions supply at least half of \(B_K\) in
  \(259\) of the \(262\) cases. The three exceptions have record deficit at
  most \(1.3234\) bits; among records with deficit at least \(2\) bits, the
  observed minimum top-three share is \(53.24\%\).
- odd payouts do not universally dominate dangerous records: among records
  with \(D_K\ge2\), the observed odd-payout share can be zero. The
  smallest-shell subtraction in the even-payout decomposition is therefore
  essential rather than a negligible exceptional term.
- among the \(71\) records with \(D_K\ge2\), the dominant payout valuation is
  \(3\) in \(47\) cases, \(2\) in \(11\), \(6\) in \(7\), and \(4\) in \(6\).
  No other dominant payout occurs in this finite range. This supports testing
  a small shell-ancestry alphabet, but is not a universal restriction.
- through odd \(n\le2001\), \(452\) of \(881\) observed first mergers
  (\(51.31\%\)) use the canonical virtual partner selected by the incoming
  payout of the high-cumulative predecessor state. Of these, \(445\) are
  incoming-\(q=2\), gap-\(2\) mergers and \(7\) are incoming-\(q=5\),
  gap-\(4\) mergers. The remaining mergers show that canonical
  immediately-preceding-payout reachability is substantial but not universal.

This small diagnostic rejects a two-case strategy in which every record
prefix is expected to be directly Baker-applicable. It also rejects a theorem
which assumes that one payout always dominates the stored correction. The
right object is a short or amortized payout ancestry, not necessarily a
single ancestor.

This suggests a sharper optional sublemma:

> Above a fixed dangerous deficit threshold, either a bounded number of
> payout ancestors carries a definite fraction of \(B_K\), or the diffuse
> ancestry itself forces enough cumulative payout valuation to rule out a
> primitive extremal obstruction.

The bounded-number alternative would reduce the collision search to a small
set of explicit ancestral corrections. The diffuse alternative is the
natural place for an amortized inequality.

Run:

```bash
python scripts/explore_repunit_extremal_prefixes.py --limit 2001
```

---

## 8. Immediate proof task

The next calculation should be symbolic, not a larger census:

1. expand \(R_K\) exactly by its payout times;
2. normalize each payout contribution by \(2^{E_K+1}\);
3. rewrite each contribution using its transported shell atoms;
4. identify when two dominant contributions differ by
   \[
   2^{u+1}\frac{2^{2h}-1}{3},
   \]
   the proved collision-shell quantity;
5. seek an amortized inequality charging every non-colliding high-height
   contribution to the valuation \(q\) that created it.

If such a charging inequality exists, it would convert “high enemy height”
from an obstruction into stored, already-paid surplus. That is the most
plausible elegant bridge currently visible between the surplus and merger
programmes.

---

## 9. Payout-ledger concentration versus diffusion

The storage identity also gives a useful no-go statement. Since

\[
D_K=K\log_2 3-E_K,
\qquad
Z_K=2^{D_K}B_K,
\]

and every valuation-one step satisfies

\[
\Delta D=\Delta\log_2 Z=\log_2(3/2),
\]

deficit storage is not locally more expensive than deficit accumulation: the
exchange rate is exactly one. Therefore no argument using only a
valuation-one run can prove that storing deficit is intrinsically
unsustainable. Any strict inequality must use the payout ancestry contained
in \(B_K\), together with primitivity, correction arithmetic, or collision
structure.

Write the individual payout contributions as

\[
w_j=
\left(1-2^{1-e_j}\right)2^{-D_{j+1}}
\qquad(e_j>1),
\]

so that

\[
B_K=\frac12+\sum_{j<K,\ e_j>1}w_j.
\]

This suggests a concentration--diffusion dichotomy at primitive
record-deficit times:

1. **Concentrated ancestry.** A bounded number of \(w_j\) carry a definite
   fraction of \(B_K\). Their transported shell atoms should then reduce the
   problem to finitely many explicit collision or reachability relations with
   smaller repunit tails.
2. **Diffuse ancestry.** No bounded collection dominates \(B_K\). Then many
   payouts were needed to create the stored correction. Seek an amortized
   inequality showing that their cumulative valuation, spacing, or recovery
   bounds the depth or duration of any later record deficit.

The corresponding open target is:

> **Primitive ancestry-amortization theorem.** At every sufficiently deep
> record-deficit time on a primitive repunit tail, either the reduced
> correction has effectively bounded height, a bounded set of dominant payout
> ancestors forces a collision with a smaller tail, or diffuse payout ancestry
> gives an explicit upper bound on the attainable record deficit.

The conclusion must be a bound on \(D_K\), a descent, or a merge. It must not
assert that current surplus and current deficit are both large, since
\(S_K=-D_K\). The role of amortization is historical: charge the present
stored correction to the earlier payouts that created \(B_K\).
