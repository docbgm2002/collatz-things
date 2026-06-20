# Collision-Defect Dynamics and Its Non-Closure

**Building on:** `repunit_gap_merger_analysis.md`,
`repunit_multigap_sync_union.md`
**Status:** Exact normalized recurrence plus an explicit repunit-tail
counterexample to deterministic relative-state closure.
**License:** CC-BY 4.0

---

## 1. Relative aligned-tail coordinates

At a common diagonal \(d\), compare two normal-form states

\[
(d,E,A),
\qquad
(d,F,B).
\]

Set

\[
u=\min(E,F),
\qquad
\delta=E-F.
\]

Because

\[
A-B
=2^{E+1}x-2^{F+1}y
\]

for odd aligned states \(x,y\), the difference is divisible by
\(2^{u+1}\). Define

\[
\boxed{
z=\frac{A-B}{2^{u+1}}.
}
\]

Let

\[
\alpha=\max(\delta,0),
\qquad
\beta=\max(-\delta,0).
\]

The normalized one-step collision defect is

\[
\boxed{
c=3z+2^\alpha-2^\beta.
}
\]

Indeed,

\[
3(A-B)+2^{E+1}-2^{F+1}
=2^{u+1}c.
\]

Thus the two aligned states merge on their next steps exactly when

\[
c=0.
\]

---

## 2. Exact recurrence

Let the outgoing valuations of the two states be \(e\) and \(f\). Their
successor cumulative valuations are

\[
E'=E+e,
\qquad
F'=F+f.
\]

Therefore

\[
\boxed{
\delta'=\delta+e-f.
}
\]

The successor correction difference is precisely the previous collision
defect:

\[
A'-B'
=3(A-B)+2^{E+1}-2^{F+1}
=2^{u+1}c.
\]

Also

\[
\min(E',F')
=u+\min(\alpha+e,\beta+f).
\]

Consequently:

**Theorem 1 (normalized defect recurrence).**

\[
\boxed{
z'
=
\frac{3z+2^\alpha-2^\beta}
{2^{\min(\alpha+e,\beta+f)}}.
}
\]

The divisibility is automatic because \(z'\) is the normalized difference of
the successor correction terms.

This recurrence exactly reproduces the collision shells. If \(c=0\), then
the successor corrections agree and the trajectories merge.

---

## 3. Why the recurrence does not close

The recurrence still requires the individual outgoing valuation pair
\((e,f)\). A hoped-for compression was that the relative state
\((\delta,z)\), perhaps augmented by the diagonal and cumulative valuations,
would determine that pair.

This is false even on actual repunit tails.

**Theorem 2 (explicit non-closure).** At diagonal

\[
d=3320,
\]

the following two aligned gap-\(2\) pairs have the same compressed state:

\[
E=F=128,
\qquad
\delta=0,
\qquad
z=-6.
\]

They are:

\[
\bigl(x_{61}(3259),x_{63}(3257)\bigr),
\]

and

\[
\bigl(x_{59}(3261),x_{61}(3259)\bigr).
\]

However, their outgoing valuation pairs are respectively

\[
(e,f)=(1,2)
\]

and

\[
(e,f)=(3,1).
\]

Therefore even

\[
(d,E,F,\delta,z)
\]

does not determine the next relative state.

*Verification.* `verify_repunit_collision_defect.py` reconstructs both exact
normal-form pairs and checks the stated coordinates and valuations.
\(\blacksquare\)

The two pairs are consecutive spacings in a three-tail configuration. Their
equal normalized correction differences do not imply equal absolute
corrections, and the outgoing valuations detect that missing absolute phase.

---

## 4. Finite branching census

For odd \(n\le1001\), gaps \(2,4,6\), and the first \(64\) aligned steps:

- \(84{,}488\) aligned transitions were examined;
- \(35{,}730\) distinct \((\delta,z)\) states occurred;
- \(3{,}635\) of those states had more than one outgoing valuation pair;
- adding the diagonal modulo \(64\) still left \(2{,}625\) branching states.

At odd \(n\le2001\) and \(128\) aligned steps, adding the exact diagonal still
left \(1{,}193\) branching states.

At smaller ranges, adding one absolute cumulative valuation appeared to
remove branching, but Theorem 2 shows that this was a finite-window
coincidence.

---

## 5. Strategic consequence

The collision defect is valuable as:

- an exact merger test;
- a normalization of the collision shells;
- an accounting variable for aligned-tail comparisons.

It is not a self-contained dynamical state. To determine its transition one
must retain enough absolute information to recover the individual valuations.
Keeping one complete correction term \(A\), together with the relative data,
essentially restores the original two-state normal form.

This retires the simplest finite-dimensional defect-recurrence route.

The merger programme remains a strong inductive reduction, but neither:

- explicit synchronization-cylinder enumeration; nor
- relative collision-defect compression

currently explains the high eventual merger rate in theorem-ready form.

The most credible next move is to return to the sparse primitive tails and
seek a cumulative surplus theorem there, while retaining proved
synchronization families and Baker non-shadowing as reductions.

---

## 6. Reproduction

```bash
python explore_repunit_collision_defect.py \
    --limit 1001 --gaps 2,4,6 --steps 64
python verify_repunit_collision_defect.py
```
