# Primitive Ancestry Lemma

**Building on:** `repunit_extremal_principle.md`,
`repunit_tail_merge_reduction.md`, `repunit_gap_merger_analysis.md`

**Status:** theory note. The bookkeeping lemmas below are exact; the
single-ancestor reachability lemma is the first proposed proof target.

---

## 1. Aim

The recent work suggests that the residual repunit-tail problem is not a
matter of finding one more finite pattern. The hard states are primitive
record-deficit states: tails that have not yet merged into a smaller exponent
and whose valuation deficit

\[
D_K=K\log_2 3-E_K
\]

is at a new record.

At such a state the normalized correction

\[
R_K=A_K+2^{E_K+1}
\]

stores the deficit. During valuation-one runs this storage grows at exactly
the same logarithmic rate as the deficit, so a local recovery argument cannot
work by itself. The only remaining structure is ancestry: the correction was
assembled by earlier payouts \(e_j>1\), and each payout is an exact
collision-shell atom.

The proposed route is therefore:

> A primitive record deficit is either low-height enough for Baker-type
> non-shadowing, or its dominant payout ancestry is forced to become an actual
> collision with a smaller repunit tail, or its ancestry is diffuse enough to
> give an amortized valuation bound.

This note isolates the first nontrivial part: the concentrated,
single-ancestor case.

---

## 2. Payout shares

For a repunit tail write

\[
x_K=f^{(K)}(a_n),\qquad
E_K=\sum_{i<K} e_i,\qquad
e_i=v_2(3x_i+1),
\]

and set

\[
B_K=\frac{Z_K}{2^{D_K}},
\qquad
Z_K=\frac{R_K}{2^{E_K+1}}.
\]

The exact payout ledger from `repunit_extremal_principle.md` is

\[
B_K=\frac12+\sum_{\substack{j<K\\e_j>1}}w_j,
\qquad
w_j=\left(1-2^{1-e_j}\right)2^{-D_{j+1}}.
\]

Define the payout share

\[
\pi_j(K)=\frac{w_j}{B_K}
\qquad(e_j>1).
\]

The initial term \(1/2\) may also be treated as a formal ancestor
\(\pi_{-1}(K)=(1/2)/B_K\). At a deep positive record deficit this initial
ancestor is usually small, but it should not be discarded silently.

---

## 3. Exact shell atom created by one payout

Suppose \(e_j=q\ge2\). Let

\[
X=x_{j+1},
\qquad
F=E_j+q,
\qquad
d=n+j+1.
\]

Put

\[
h=\left\lfloor\frac q2\right\rfloor,
\qquad
u=F-2h.
\]

The canonical virtual collision partner of \(X\) is

\[
Y=4^hX+\frac{4^h-1}{3}.
\]

Then

\[
3Y+1=4^h(3X+1),
\]

so \(f(Y)=f(X)\). In diagonal normal form,

\[
X=\frac{3^d+A_{j+1}}{2^{F+1}},
\]

and

\[
Y=\frac{3^d+A_{j+1}+S(u,2h)}{2^{u+1}},
\qquad
S(u,2h)=2^{u+1}\frac{2^{2h}-1}{3}.
\]

Thus the payout creates an exact lower-cumulative shell partner on the same
diagonal. The partner is virtual until we prove that it is realised by a
smaller repunit tail.

---

## 4. Reachability as the missing condition

The virtual partner \(Y\) is reachable from a smaller repunit exponent if
there exist odd \(m<n\) and \(i\ge0\) such that

\[
m+i=d,\qquad
E_i(m)=u,\qquad
A_i(m)=A_{j+1}+S(u,2h).
\]

If this holds, then the predecessor states lie on the collision shell and

\[
x_{i+1}(m)=x_{j+2}(n).
\]

Consequently the \(n\)-tail merges into a smaller tail, and descent is
inherited by the strong-induction theorem in `repunit_tail_merge_reduction.md`.

This converts the problem into a precise arithmetic question:

> When does a transported shell atom in the correction ancestry correspond to
> an actual earlier repunit state, rather than merely a formal algebraic
> displacement?

---

## 5. Candidate lemma: dominant payout reachability

The first theory target should be deliberately narrower than the full
primitive storage/collision lemma.

> **Single-ancestor reachability lemma (open).**  
> There are constants \(H>0\), \(\eta>0\), and \(r\ge1\) such that the
> following holds. Let \(K\) be a strict record-deficit time on a primitive
> active repunit tail. Suppose \(D_K\ge H\) and some payout ancestor
> \(j<K\) satisfies
> \[
> \pi_j(K)\ge\eta.
> \]
> Then either:
>
> 1. the reduced enemy constant at \(K\) has low enough height for an
>    effective Baker/Archimedean non-shadowing bound; or
> 2. within at most \(r\) ancestor transitions of \(j\), one of the associated
>    shell partners is reachable from a smaller repunit tail; or
> 3. the valuation paid at those ancestor transitions gives an explicit upper
>    bound for \(D_K\), contradicting \(D_K\ge H\) once \(H\) is chosen large
>    enough.

The important feature is the bounded ancestor depth \(r\). If a dominant
contribution can be chased backwards only indefinitely, the statement has not
converted storage into structure.

For a first attack, take the smallest plausible case:

\[
r=1,
\qquad
q=e_j\in\{2,3,4,5,6\}.
\]

The finite diagnostics suggest these payouts dominate many dangerous records,
but the lemma must be proved without assuming that larger \(q\) never occurs.

---

## 6. Why this is plausible

The dominant payout contributes a definite fraction of

\[
B_K=\frac{Z_K}{2^{D_K}}.
\]

At a record time, \(Z_K\) is the object carrying the accumulated deficit.
If one earlier payout carries a fixed share of that object, then a fixed
portion of the current high-height enemy constant has an explicit shell
origin.

The shell origin is not decorative. It gives a concrete partner

\[
Y=4^hX+\frac{4^h-1}{3}
\]

with the same next odd iterate as \(X\). Therefore the obstruction to merger
is no longer "find a miracle"; it is:

1. show that this \(Y\) lies on the smaller repunit curve, or
2. show that repeated failure to lie on that curve forces the exponent into
   a 2-adic branch whose positive integer representatives cannot shadow for
   linearly many steps, or
3. charge the failure to the payout valuations that created the shell atom.

This is exactly where primitivity matters. Without primitivity, a dominant
shell atom may simply be a copy of an already-merged orbit segment. With
primitivity, every reachable shell partner is a contradiction to being
primitive, so non-reachability must carry arithmetic information.

---

## 7. First sublemma to try

The most concrete sublemma is the \(q=2\), \(r=1\) case.

At a \(q=2\) payout, \(h=1\), \(u=E_j\), and

\[
S(u,2)=2^{u+1}.
\]

The virtual partner is

\[
Y=4X+1.
\]

In diagonal coordinates, if

\[
X=\frac{3^d+A}{2^{u+3}},
\]

then

\[
Y=\frac{3^d+A+2^{u+1}}{2^{u+1}}.
\]

Thus the reachability condition is:

\[
\exists\,m< n,\ i\ge0:
\quad
m+i=d,\quad
E_i(m)=u,\quad
A_i(m)=A+2^{u+1}.
\]

But this is exactly the smallest collision shell. The proved gap-merger
families are all instances of this condition.

> **Sublemma A (open).**  
> Let a primitive record-deficit state have a dominant \(q=2\) payout ancestor.
> If the associated smallest-shell partner is not reachable from a smaller
> repunit tail, then the non-reachability forces a quantitative lower bound
> on the least positive exponent representative of the valuation prefix
> containing \(n\).

This is weaker than immediate merger but still useful: if the least positive
representative grows faster than the available diagonal length, the branch
cannot support a linear-length primitive record deficit.

---

## 8. Reachable correction sets

For integers \(i\ge0\) and \(u\ge0\), define \(\mathcal A(i,u)\) to be the
set of correction terms \(C\) obtainable after \(i\) shortcut steps with
cumulative valuation \(u\), starting from the repunit initial correction
\(-1\):

\[
\mathcal A(i,u)=
\left\{
A_i:
A_0=-1,\quad
A_{t+1}=3A_t+2^{E_t+1},\quad
E_0=0,\quad E_i=u,\quad e_t=E_{t+1}-E_t\ge1
\right\}.
\]

Equivalently, for a valuation word
\(\mathbf e=(e_0,\ldots,e_{i-1})\) with total \(u\),

\[
A_i(\mathbf e)
=-3^i+\sum_{t=0}^{i-1}3^{i-1-t}2^{E_t+1},
\qquad
E_t=\sum_{s<t}e_s.
\]

The virtual partner in the \(q=2\) case is reachable from a smaller repunit
tail only if its correction lies in one of these sets:

\[
C=A+2^{u+1}\in \mathcal A(i,u)
\]

for some source step count \(i\). This condition is not yet sufficient by
itself; the corresponding exponent \(m=d-i\) must also realise the required
prefix congruences. But it is a clean first obstruction: a correction outside
all admissible \(\mathcal A(i,u)\) cannot be a smaller repunit-tail state.

The allowed step counts are sharply constrained. Since the smaller source has
diagonal \(d=m+i\) and \(m<n\), while the high state has \(d=n+j+1\), we must
have

\[
i>j+1.
\]

Also every valuation is at least \(1\), so \(i\le u\). Finally, because
\(m=d-i\) must be odd and \(n\) is odd,

\[
i\equiv j+1\pmod2.
\]

Thus \(q=2\) reachability can occur only for

\[
\boxed{
j+2\le i\le u,\qquad i\equiv j+1\pmod2.
}
\]

This is already useful. If \(u\le j+1\), the virtual partner cannot be a
smaller repunit-tail state for the elementary reason that no smaller odd
source has enough diagonal time while keeping total valuation \(u\).

---

## 9. Automatic parity of the smallest-shell partner

The correction-set obstruction is the real one; parity is not.

Suppose \(e_j=2\), \(u=E_j\), \(d=n+j+1\), and

\[
X=x_{j+1}=\frac{3^d+A}{2^{u+3}}.
\]

Because \(X\) is odd,

\[
v_2(3^d+A)=u+3.
\]

Let \(C=A+2^{u+1}\), the smallest-shell partner correction. Then

\[
3^d+C=(3^d+A)+2^{u+1}.
\]

Writing \(3^d+A=2^{u+3}s\) with \(s\) odd gives

\[
3^d+C=2^{u+1}(4s+1),
\]

and \(4s+1\) is odd. Therefore

\[
\boxed{
v_2(3^d+C)=u+1.
}
\]

So the virtual partner is automatically an odd normal-form state at
cumulative valuation \(u\). What remains is reachability from the repunit
initial correction:

\[
C\in\mathcal A(i,u)
\]

for an allowed \(i\), together with the exact prefix congruences for
\(m=d-i\).

This removes one possible distraction. The smallest-shell partner never fails
because of the final oddness condition; it fails only because the lower
correction state may not lie on the repunit-tail ancestry tree.

---

## 10. Composition form of reachability

The reachable correction sets have an explicit composition form. If
\(\mathbf e=(e_0,\ldots,e_{i-1})\) is a composition of \(u\) into \(i\)
positive parts, write

\[
Q_0=0,\qquad Q_s=e_0+\cdots+e_{s-1}\quad(1\le s\le i).
\]

Then

\[
A_i(\mathbf e)
=
-3^i
+2\sum_{s=0}^{i-1}3^{i-1-s}2^{Q_s}.
\]

Now fix a \(q=2\) high ancestor. Let the pre-payout high prefix have length
\(j\), cumulative valuation \(u\), partial sums

\[
P_0=0,\qquad P_t=e_0+\cdots+e_{t-1}\quad(1\le t\le j),
\]

and correction \(A_j\). Since the payout has \(e_j=2\),

\[
A_{j+1}=3A_j+2^{u+1},
\]

and the smallest-shell partner correction is

\[
C=A_{j+1}+2^{u+1}=3A_j+2^{u+2}.
\]

Substituting the composition formula for \(A_j\), reachability by a smaller
source word \(\mathbf f\) of length \(i\) and total \(u\) is equivalent to

\[
\boxed{
-3^i
+2\sum_{s=0}^{i-1}3^{i-1-s}2^{Q_s}
=
-3^{j+1}
+2\sum_{t=0}^{j-1}3^{j-t}2^{P_t}
+2^{u+2}.
}
\]

Equivalently,

\[
\boxed{
2\sum_{s=0}^{i-1}3^{i-1-s}2^{Q_s}
-2\sum_{t=0}^{j-1}3^{j-t}2^{P_t}
=
3^i-3^{j+1}+2^{u+2}.
}
\]

This is the exact ancestry equation for the \(q=2\) smallest shell. It is a
finite equation in two compositions of the same total \(u\), with the source
composition forced to have length

\[
j+2\le i\le u,\qquad i\equiv j+1\pmod2.
\]

This form is promising because it does not mention the large exponent \(n\)
directly. It asks whether the correction created by the high prefix can be
reassembled from a longer, lower-cumulative source prefix of the same total
valuation.

---

## 11. A first congruence obstruction

The ancestry equation immediately imposes a condition on the final valuation
of any reachable smaller source.

For every reachable correction \(A_i\),

\[
A_i\equiv 2^{Q_{i-1}+1}\pmod3,
\]

because the recurrence gives

\[
A_i=3A_{i-1}+2^{Q_{i-1}+1}.
\]

In the \(q=2\) smallest-shell case,

\[
C=3A_j+2^{u+2}\equiv2^{u+2}\pmod3.
\]

Thus any equality \(A_i=C\) forces

\[
2^{Q_{i-1}+1}\equiv2^{u+2}\pmod3.
\]

Since powers of \(2\) modulo \(3\) have period \(2\), this is equivalent to

\[
Q_{i-1}+1\equiv u+2\pmod2.
\]

Writing the final source valuation as

\[
\ell=u-Q_{i-1},
\]

we get

\[
\boxed{\ell\ \text{is odd}.}
\]

So a reachable \(q=2\) virtual partner cannot end with an even valuation in
the smaller source prefix. This does not prove reachability, but it removes
half of the candidate source compositions before any deeper arithmetic is
used.

The next congruence to inspect is modulo \(9\) or \(8\), where the last two
source valuations begin to appear. The hope is to turn failure of these
successive congruences into a nested 2-adic branch and then apply a
positive-integer size bound, as in the low-prefix obstruction.

---

## 12. Tail congruence sieve modulo powers of 3

The composition form has a useful asymmetry: modulo powers of \(3\), only the
last few source valuations are visible.

Fix \(r\ge1\). If \(i\ge r\), then

\[
A_i(\mathbf e)
\equiv
2\sum_{s=i-r}^{i-1}3^{i-1-s}2^{Q_s}
\pmod{3^r}.
\]

All earlier terms vanish modulo \(3^r\), and the initial term \(-3^i\) also
vanishes. Therefore membership

\[
C\in\mathcal A(i,u)
\]

forces a congruence involving only the last \(r\) partial sums of the source
composition.

For the \(q=2\) smallest-shell correction

\[
C=A_{j+1}+2^{u+1}=3A_j+2^{u+2},
\]

if \(j+1\ge r\), then

\[
C
\equiv
2^{u+2}
+2\sum_{t=j-r+1}^{j-1}3^{j-t}2^{P_t}
\pmod{3^r}.
\]

Thus the source tail of length \(r\) is constrained by the high-prefix tail of
length \(r-1\), plus the new shell term \(2^{u+2}\).

This is a genuine local test for reachability. It does not search over all
source words; it asks whether the last few valuations of any source word can
match the shell ancestry forced by the high word.

### The explicit modulo-9 test

Take \(r=2\). A reachable source word of length \(i\ge2\) must satisfy

\[
A_i
\equiv
3\cdot2^{Q_{i-2}+1}+2^{Q_{i-1}+1}
\pmod9.
\]

For a \(q=2\) high ancestor with \(j\ge1\),

\[
C
\equiv
3\cdot2^{P_{j-1}+1}+2^{u+2}
\pmod9.
\]

Let

\[
\ell=u-Q_{i-1}
\]

be the final source valuation,

\[
b=Q_{i-1}-Q_{i-2}
\]

the penultimate source valuation, and

\[
r_h=u-P_{j-1}=e_{j-1}
\]

the final high valuation before the \(q=2\) payout. Then the modulo-\(9\)
condition becomes

\[
\boxed{
3\cdot2^{u-\ell-b+1}+2^{u-\ell+1}
\equiv
3\cdot2^{u-r_h+1}+2^{u+2}
\pmod9.
}
\]

Together with the modulo-\(3\) result

\[
\ell\ \text{odd},
\]

this gives a two-symbol tail test for any reachable smallest-shell partner.
Because powers of \(2\) modulo \(9\) have period \(6\), the condition is a
restriction on \((\ell,b,r_h,u)\) modulo \(6\), with the extra parity already
forcing \(\ell\) into three residue classes.

Cancelling the common invertible factor \(2^{u-\ell-b+1}\) gives the cleaner
condition

\[
\boxed{
3+2^b
\equiv
3\cdot2^{\ell+b-r_h}+2^{\ell+b+1}
\pmod9.
}
\]

This condition is independent of \(u\). Checking the six residues of \(2\)
modulo \(9\) gives the following exact table:

| \(\ell\bmod6\) | allowed \(b\bmod6\) | allowed \(r_h\bmod6\) |
|---:|---:|---:|
| \(1\) | \(1,3,5\) | \(1,3,5\) |
| \(3\) | \(0,2,4\) | \(0,2,4\) |
| \(5\) | \(0,2,4\) | \(1,3,5\) |
| \(5\) | \(1,3,5\) | \(0,2,4\) |

Equivalently:

- if \(\ell\equiv1\pmod6\), then both \(b\) and \(r_h\) are odd;
- if \(\ell\equiv3\pmod6\), then both \(b\) and \(r_h\) are even;
- if \(\ell\equiv5\pmod6\), then \(b\) and \(r_h\) have opposite parity.

Thus the modulo-\(9\) sieve removes two thirds of the possible residue triples
\((\ell,b,r_h)\) after the basic \(\ell\)-odd condition. This is the first
real arithmetic pressure on the virtual partner: reachability forces the
last two source valuations to coordinate with the final high valuation before
the \(q=2\) payout.

The natural next step is to run the same argument modulo \(27\), not as a
large census but as a symbolic tail recursion. Modulo \(3^r\), the last \(r\)
source valuations must match the high-prefix tail of length \(r-1\) plus the
shell term. If increasing \(r\) forces many small valuations near the end of
the smaller source word, then non-reachability can be pushed toward a
low-prefix shadowing problem.

### The modulo-27 lift

Modulo \(27\), one more valuation appears on each side. Let

\[
c=Q_{i-2}-Q_{i-3}
\]

be the antepenultimate source valuation, and let

\[
a=P_{j-1}-P_{j-2}=e_{j-2}
\]

be the high valuation immediately before \(r_h=e_{j-1}\). After cancelling
the common unit \(2^{u-\ell-b-c+1}\), the congruence is

\[
\boxed{
9+3\cdot2^c+2^{c+b}
\equiv
9\cdot2^{\ell+b+c-a-r_h}
+3\cdot2^{\ell+b+c-r_h}
+2^{\ell+b+c+1}
\pmod{27}.
}
\]

The first surprise is that this is not a new large residue table. Once the
modulo-\(9\) condition holds, the modulo-\(27\) lift either fails by one
extra nonvanishing condition or chooses the parity of \(a\). The reason is
that the new term containing \(a\) is multiplied by 9, so it sees only

\[
2^{\ell+b+c-a-r_h}\pmod3.
\]

More explicitly, define

\[
\Delta
=
9+3\cdot2^c+2^{c+b}
-3\cdot2^{\ell+b+c-r_h}
-2^{\ell+b+c+1}.
\]

The modulo-\(9\) condition is exactly \(\Delta\equiv0\pmod9\). The lift to
modulo \(27\) is then equivalent to

\[
\boxed{
2^{\ell+b+c-a-r_h}
\equiv
\Delta/9
\pmod3.
}
\]

Thus:

- if \(\Delta/9\equiv0\pmod3\), then there is no modulo-\(27\) lift;
- if \(\Delta/9\equiv1\pmod3\), then
  \(\ell+b+c-a-r_h\) is even;
- if \(\Delta/9\equiv2\pmod3\), then
  \(\ell+b+c-a-r_h\) is odd.

In particular, modulo \(27\) first removes the cases with
\(\Delta/9\equiv0\pmod3\). In the surviving cases it imposes a parity rule
on the second-to-last high valuation \(a\), but no finer residue of \(a\)
modulo \(18\). A residue check over
\(\ell\) odd modulo \(18\) and \(b,c,r_h\) modulo \(18\) confirms the
interpretation: among the modulo-\(9\)-admissible quadruples
\((\ell,b,c,r_h)\), exactly two thirds lift to modulo \(27\), and for each
lifting quadruple exactly one parity class of \(a\) modulo \(18\) survives.

This is encouraging. The \(3^r\)-sieve appears to reveal one additional high
tail valuation at each lift, but only at the precision needed to match the
new source-tail valuation. That is a finite-state tail recursion, not an
unstructured explosion.

---

## 13. Crude interval bounds for reachable layers

The composition formula also gives simple bounds for each layer
\(\mathcal A(i,u)\). Since the partial sums satisfy

\[
s\le Q_s\le u-i+s
\qquad(0\le s\le i),
\]

we have

\[
2\sum_{s=0}^{i-1}3^{i-1-s}2^s
\le
A_i+3^i
\le
2\sum_{s=0}^{i-1}3^{i-1-s}2^{u-i+s}.
\]

Therefore

\[
\boxed{
3^i-2^{i+1}
\le
A_i
\le
2^{u-i+1}(3^i-2^i)-3^i.
}
\]

These bounds are intentionally crude, but they are theory-useful in two
ways:

1. if \(C\) lies outside this interval for every admissible \(i\), then the
   virtual partner is not reachable for size reasons inside the correction
   tree;
2. if \(C\) lies inside only for \(i\) very close to \(u\), then the smaller
   source prefix must have many valuation-one steps, which pushes the problem
   toward a low-prefix/non-shadowing argument.

The second alternative is more important. A pure interval exclusion is likely
too weak, but forcing \(i\) close to \(u\) would mean the smaller source has a
long low-valuation prefix. That is exactly the regime where ordinary size
bounds can defeat positive integer shadowing.

---

## 14. Refined form of Sublemma A

The previous version of Sublemma A can now be sharpened.

> **Sublemma A' (smallest-shell non-reachability).**  
> Let a primitive record-deficit state have a dominant \(q=2\) payout ancestor
> at time \(j\). Put \(u=E_j\), \(d=n+j+1\), and
> \(C=A_{j+1}+2^{u+1}\). If
> \[
> C\notin\mathcal A(i,u)
> \]
> for every
> \[
> j+2\le i\le u,\qquad i\equiv j+1\pmod2,
> \]
> or if the only such correction matches fail the exact exponent-prefix
> congruences for \(m=d-i\), then this failure forces a quantitative lower
> bound on the least positive representative of the \(n\)-prefix class.

The point of this formulation is that the obstruction is now discrete and
structural. We are not asking whether a smaller tail happens to appear in a
finite table; we are asking whether a specific correction \(C\) lies in a
specific finite layer of the correction tree.

The desired lower bound should use the failed membership in
\(\mathcal A(i,u)\), not merely the modulus size of the valuation prefix.
Otherwise the low-prefix example from `repunit_low_prefix_obstruction.md`
shows that the argument can be fooled by a compactly described high-modulus
2-adic branch.

---

## 15. Diffuse payout ancestry

The single-ancestor lemma handles the case where one payout carries a fixed
share of \(B_K\). The complementary case is that \(B_K\) is diffuse.

Write

\[
B_K=\frac12+\sum_{j\in P_K}w_j,
\qquad
P_K=\{j<K:e_j>1\},
\]

where

\[
w_j=\left(1-2^{1-e_j}\right)2^{-D_{j+1}}.
\]

Let

\[
W_K=\sum_{j\in P_K}w_j=B_K-\frac12,
\qquad
\rho_j=\frac{w_j}{W_K}
\]

when \(W_K>0\). The earlier share \(\pi_j=w_j/B_K\) is convenient when the
initial ancestor matters; \(\rho_j\) is cleaner for measuring diffusion among
actual payouts.

### Exact soft consequences

If no payout carries more than an \(\eta\)-share of \(W_K\), then at least
\(\lceil1/\eta\rceil\) payout ancestors are needed. More quantitatively, the
effective payout count

\[
N_{\rm eff}(K)=\frac{W_K^2}{\sum_{j\in P_K}w_j^2}
\]

satisfies

\[
\boxed{
N_{\rm eff}(K)\ge\frac1{\max_j\rho_j}.
}
\]

Thus diffuse storage is not a metaphor: it forces many distinct historical
payouts to participate in the correction.

There is also a dyadic layer version. For \(s\ge0\), define

\[
P_s(K)=
\left\{
j\in P_K:
2^{-(s+1)}W_K < w_j\le2^{-s}W_K
\right\}.
\]

Then

\[
W_K
\le
\sum_{s\ge0}|P_s(K)|2^{-s}W_K
\]

after ignoring empty layers and harmless endpoint conventions. Hence some
scale \(s\) must have many payout ancestors whenever no small collection of
large ancestors dominates. This lets a diffuse argument choose one scale and
work with comparable weights rather than all payouts at once.

### Historical depth

Each payout weight has the form

\[
\log_2 w_j
=
\log_2(1-2^{1-e_j})-D_{j+1}.
\]

Since

\[
0<1-2^{1-e_j}<1,
\]

large weights can only be created at times with negative or small
\(D_{j+1}\), i.e. at historical surplus states. Diffuse ancestry therefore
means not merely "many payouts"; it means many payouts whose post-payout
deficit depths \(D_{j+1}\) lie in comparable ranges.

For comparable weights \(w_j\asymp 2^{-s}W_K\), we have

\[
D_{j+1}
\approx
-\log_2 W_K+s
\]

with an error coming only from the bounded factor
\(\log_2(1-2^{1-e_j})\). More explicitly,

\[
-\log_2 w_j-1
<
D_{j+1}
<
-\log_2 w_j,
\]

because \(1/2\le1-2^{1-e_j}<1\) for \(e_j\ge2\). Thus one dyadic layer of
weights corresponds to a one-bit-thick band of historical deficit levels.

### Candidate diffuse lemma

The diffuse branch should not try to identify a collision partner for every
payout. Instead it should prove that many comparable historical surplus
payouts cannot all feed one later primitive record deficit without either
creating a reachable shell relation or paying enough valuation to bound the
record.

> **Diffuse ancestry lemma (open).**  
> Fix \(\eta,\alpha>0\). At a primitive record-deficit time \(K\), suppose no
> set of at most \(M\) payout ancestors carries \(\alpha W_K\). Then either:
>
> 1. some dyadic payout layer \(P_s(K)\) contains two ancestors whose
>    transported shell atoms force a reachable collision with a smaller
>    repunit tail; or
> 2. the comparable historical deficit levels \(D_{j+1}\) in that layer force
>    enough cumulative payout valuation between them to give an upper bound
>    on \(D_K\).

The attractive part is that the lemma would use spacing and comparability,
not the immediate terminal payout episode. This avoids the failure mode of
`repunit_enemy_episode_analysis.md`, where recovery could be delayed long
after a local run.

The first concrete symbolic target is a two-ancestor version: if two
comparable \(q=2\) or \(q=3\) payout atoms survive in the same dyadic layer,
compare their transported shell displacements. Either their difference is
itself a collision-shell displacement at a later diagonal, or the mismatch
should impose independent congruence conditions on the exponent \(n\).

---

## 16. Two comparable ancestors

The dyadic layer formulation gives a small but useful exact consequence.
Suppose two payout ancestors \(p<q<K\) lie in the same dyadic layer, so

\[
\frac12\le \frac{w_p}{w_q}\le2.
\]

Since

\[
w_j=(1-2^{1-e_j})2^{-D_{j+1}},
\]

and

\[
\frac12\le1-2^{1-e_j}<1
\qquad(e_j\ge2),
\]

we get the universal bound

\[
\boxed{
|D_{p+1}-D_{q+1}|<2.
}
\]

Thus comparable payout weight means comparable historical deficit depth. This
is stronger than just saying the payouts are both large: they were created at
nearly the same height in the deficit ledger.

Now

\[
D_{q+1}-D_{p+1}
=(q-p)\log_2 3-\sum_{t=p+1}^{q}e_t.
\]

Therefore same-layer ancestry forces

\[
\boxed{
\left|
(q-p)\log_2 3-\sum_{t=p+1}^{q}e_t
\right|<2.
}
\]

In words: the valuation block between two comparable payout ancestors must be
almost mean-balanced. It cannot be a long low-valuation drift, nor can it be a
large surplus block, unless the two payouts fall into different dyadic
ancestry layers.

This is the first amortization handle. If a diffuse record uses many
comparable payout ancestors, then the blocks between consecutive ancestors in
one layer are all nearly mean-balanced. A long record-deficit run after those
ancestors must therefore come from storage accumulated across many such
balanced blocks, not from a single unpaid low-valuation episode.

### Candidate spacing lemma

> **Balanced-spacing lemma (open).**  
> Fix a dyadic payout layer \(P_s(K)\), and list its ancestors as
> \(j_1<j_2<\cdots<j_M\). If the corresponding transported shell atoms do not
> force a reachable collision with a smaller tail, then the near-balance
> inequalities
> \[
> \left|
> (j_{r+1}-j_r)\log_2 3
> -\sum_{t=j_r+1}^{j_{r+1}}e_t
> \right|<2
> \]
> for many \(r\) force either:
>
> 1. a bounded record deficit \(D_K\); or
> 2. a long chain of almost-balanced valuation blocks whose endpoint
>    congruences impose a low-dimensional 2-adic shadowing branch.

This is deliberately softer than the single-ancestor reachability lemma. It
does not try to make every payout produce a collision. It says that if
collisions fail throughout a thick dyadic layer, then the valuation ledger
between the ancestors is too balanced to support an unbounded primitive
record deficit without creating a separate non-shadowing problem.

### Two-shell displacement comparison

There is also a concrete algebraic object attached to two ancestors. A payout
at time \(j\) contributes a transported shell atom of the form

\[
3^{K-j}S(U_j,2h_j)
\]

with the even-payout subtraction handled separately. For two same-layer
ancestors \(p<q\), compare after factoring out \(3^{K-q}\):

\[
3^{q-p}S(U_p,2h_p)-S(U_q,2h_q).
\]

If this difference equals another collision-shell displacement

\[
S(V,2h),
\]

then the two atoms combine into the same algebraic shape that drives a
one-step merger. If it does not, the failure is an explicit exponential
Diophantine condition involving \(3^{q-p}\), powers of \(2\), and the shell
heights.

This gives the diffuse branch a concrete next calculation:

1. first handle \(h_p=h_q=1\), the \(q=2\) smallest-shell case;
2. ask when
   \[
   3^{q-p}2^{U_p+1}-2^{U_q+1}
   =
   2^{V+1}\frac{2^{2h}-1}{3}
   \]
   is possible;
3. if impossible, record the resulting congruence obstruction as another
   non-shadowing condition on the exponent.

The hope is that same-layer comparability plus this two-shell equation will
replace the failed local recovery idea with a genuinely historical
amortization mechanism.

---

## 17. Smallest-shell pair equation

For the first two-ancestor calculation, take both payout atoms to be smallest
shells. Write

\[
r=q-p\ge1,\qquad
A=U_p+1,\qquad
B=U_q+1.
\]

The transported difference is

\[
L=3^r2^A-2^B.
\]

If this difference is a positive collision-shell displacement, then for some
\(V\) and \(h\ge1\),

\[
L=2^{V+1}\frac{2^{2h}-1}{3}.
\]

After removing the exact power of two from \(L\), this becomes one of three
Diophantine equations.

### Case 1: earlier atom has larger 2-height

If \(A>B\), put \(d=A-B\ge1\). Then

\[
L=2^B(3^r2^d-1),
\]

so the odd part must satisfy

\[
3^r2^d-1=\frac{2^{2h}-1}{3}.
\]

Equivalently,

\[
\boxed{
3^{r+1}2^d-2=2^{2h}.
}
\]

This case is almost rigid. If \(d\ge2\), the left side has exact 2-adic
valuation \(1\), and is larger than \(2\), so it cannot be a power of \(4\).
If \(d=1\), the equation becomes

\[
2(3^{r+1}-1)=2^{2h}.
\]

Thus \(3^{r+1}-1\) must be a power of two. The only solution with \(r\ge1\)
is

\[
\boxed{r=1,\quad d=1,\quad h=2.}
\]

Indeed, if \(m=r+1\) is odd and \(m>1\), then
\((3^m-1)/(3-1)\) is an odd factor greater than \(1\). If \(m=2s\), then
\(3^m-1=(3^s-1)(3^s+1)\). For \(s=1\) this gives \(m=2\). If
\(s>1\) is odd, then \((3^s-1)/(3-1)\) is an odd factor greater than
\(1\). If \(s\) is even, then \(3^s+1\equiv2\pmod8\) and
\(3^s+1>2\), so \(3^s+1\) has an odd factor greater than \(1\). Hence
only \(m=1,2\) give a power of two, and \(r\ge1\) leaves \(m=2\).

So a higher earlier smallest-shell atom can combine into a shell only in the
adjacent-time, one-height-offset case.

### Case 2: equal 2-heights

If \(A=B\), then

\[
L=2^A(3^r-1).
\]

Writing \(\operatorname{odd}(m)\) for the odd part of \(m\), the shell
condition is

\[
\boxed{
3\operatorname{odd}(3^r-1)+1=2^{2h}.
}
\]

The first solutions are

\[
r=1,\ h=1;\qquad r=2,\ h=1;\qquad r=4,\ h=2.
\]

No general classification is asserted here. The point is that equal-height
same-layer atoms reduce to a one-variable exponential condition.

### Case 3: later atom has larger 2-height

If \(A<B\), put \(g=B-A\ge1\). Positivity requires

\[
3^r>2^g.
\]

Then

\[
L=2^A(3^r-2^g),
\]

and the shell condition is

\[
\boxed{
3^{r+1}-3\cdot2^g+1=2^{2h}.
}
\]

The first small solutions are

\[
(r,g,h)=(1,1,1),\quad(2,3,1),\quad(2,2,2).
\]

Again, no full classification is claimed. But the important structural fact
is that a two-ancestor smallest-shell collision is not arbitrary: after the
common power of two is removed, it is governed by an exponential equation in
the time gap \(r\) and height gap \(|A-B|\).

### Consequence for the diffuse programme

If two comparable smallest-shell ancestors in one dyadic layer do not satisfy
one of these equations, then their transported shell atoms cannot combine
into a single collision-shell displacement. The failure is not vague; it is a
specific exponential obstruction. In the primitive setting, that obstruction
must either:

1. impose independent congruence restrictions on the exponent \(n\); or
2. be charged as part of the diffuse amortization budget.

This is the first place where the diffuse branch becomes a finite list of
symbolic arithmetic cases rather than a general appeal to "many payouts."

---

## 18. What not to prove

Avoid these tempting but false or unsupported statements:

- A fixed block of low valuations must be followed by a bounded local
  recovery. The enemy-episode experiment refutes this.
- A single payout always dominates \(B_K\). The finite diagnostic already has
  diffuse examples.
- A formal shell atom is automatically a reachable smaller repunit state.
  The word "virtual" in virtual collision partner is doing real work.
- A current positive surplus can be compared to a current positive deficit.
  They are negatives of each other in the same ledger.

The useful theorem must spend primitivity, reachability, or historical payout
valuation. Otherwise it is only another restatement of the bookkeeping.

---

## 19. Next proof move

Work on Sublemma A symbolically:

1. fix a \(q=2\) payout ancestor and write the exact valuation-prefix
   congruences for the high state \(X\);
2. write the congruences for the virtual partner \(Y=4X+1\);
3. compute the possible source-step window
   \(j+2\le i\le u,\ i\equiv j+1\pmod2\);
4. express reachability as membership of
   \(C=A_{j+1}+2^{u+1}\) in the reachable correction layer
   \(\mathcal A(i,u)\), plus the exact exponent-prefix congruences for
   \(m=d-i\);
5. use the ancestry equation, last-valuation parity, the modulo-\(3^r\) tail
   congruence sieve, and layer bounds above to reduce the possible source
   compositions;
6. prove that if the remaining source tails force a long low-valuation
   suffix or prefix, then positive integer size bounds prevent linear
   shadowing;
7. prove that if no such \(m\) exists up to the diagonal \(d\), then the
   surviving exponent class for \(n\) has least positive representative
   exceeding a function of \(u\) or \(d\);
8. compare that lower bound with the maximum length available before the
   proposed \(3n\) descent window closes.

This is a theory task. Computation should only be used afterward to test
which congruence obstruction appears in the symbolic work.
