# The 2-Adic Geometry of the Rail-5 Survivor Set

**Building on:** `repunit_rail5_density.md`

**Status:** Proved here. This note determines the symbolic dynamics, Haar
measure, and Hausdorff dimension of the infinite rail-5 survivor set. It does
not determine all positive integer points in that set.

---

## 1. The survivor set

Let

\[
f(x)=\frac{3x+1}{2^{v_2(3x+1)}}
\]

on odd integers. The same formula is defined on odd \(2\)-adic integers
except at \(x=-1/3\), where \(3x+1=0\).

Rail \(5\) is characterized by

\[
x\equiv5\pmod8
\quad\Longleftrightarrow\quad
v_2(3x+1)\ge3.
\]

Define the infinite survivor set

\[
\mathcal S
=
\left\{
x\in1+2\mathbb Z_2:
v_2(3f^{(j)}(x)+1)\in\{1,2\}
\text{ for every }j\ge0
\right\}.
\]

Thus \(\mathcal S\) consists exactly of the odd \(2\)-adic starting states
whose accelerated trajectories avoid rail \(5\) forever. The exceptional
point \(-1/3\) is not in \(\mathcal S\).

---

## 2. Exact inverse branches

For \(e\in\{1,2\}\), define

\[
\phi_e(y)=\frac{2^e y-1}{3}
\qquad(y\in1+2\mathbb Z_2).
\]

Since \(3\) is a unit in \(\mathbb Z_2\), each \(\phi_e(y)\) is an odd
\(2\)-adic integer. Moreover,

\[
3\phi_e(y)+1=2^e y.
\]

Because \(y\) is odd,

\[
v_2(3\phi_e(y)+1)=e,
\qquad
f(\phi_e(y))=y.
\]

The two images are disjoint:

\[
\phi_1(1+2\mathbb Z_2)
=\{x:v_2(3x+1)=1\},
\]

\[
\phi_2(1+2\mathbb Z_2)
=\{x:v_2(3x+1)=2\}.
\]

They are also exact similarities in the standard \(2\)-adic metric:

\[
|\phi_e(y)-\phi_e(z)|_2
=2^{-e}|y-z|_2.
\]

Consequently

\[
\boxed{\mathcal S=\phi_1(\mathcal S)\mathbin{\dot\cup}\phi_2(\mathcal S).}
\]

---

## 3. Symbolic coding

Let

\[
\Omega=\{1,2\}^{\mathbb N}.
\]

For a finite word

\[
w=(e_0,\ldots,e_{K-1}),
\qquad
E(w)=\sum_{j<K}e_j,
\]

put

\[
\phi_w=\phi_{e_0}\circ\cdots\circ\phi_{e_{K-1}}.
\]

The cylinder

\[
I_w=\phi_w(1+2\mathbb Z_2)
\]

is one odd residue ball of relative Haar measure \(2^{-E(w)}\) and diameter

\[
\operatorname{diam}(I_w)
=2^{-E(w)}\operatorname{diam}(1+2\mathbb Z_2).
\]

It consists exactly of the states whose first \(K\) valuations are
\((e_0,\ldots,e_{K-1})\).

For every infinite word \(\omega=(e_0,e_1,\ldots)\), the nested balls

\[
I_{\omega|K}
\]

have diameters tending to zero, because \(E(\omega|K)\ge K\). Completeness of
\(\mathbb Z_2\) therefore gives a unique point

\[
\pi(\omega)=\bigcap_{K\ge1}I_{\omega|K}.
\]

Distinct words first differ in one valuation and then lie in the disjoint
images of \(\phi_1\) and \(\phi_2\). Hence \(\pi\) is injective. Every point
of \(\mathcal S\) supplies its valuation itinerary, so \(\pi\) is also
surjective.

Therefore:

\[
\boxed{
\pi:\{1,2\}^{\mathbb N}\longrightarrow\mathcal S
\text{ is a homeomorphism},
}
\]

and under this coding the map \(f\) is conjugate to the left shift:

\[
f\circ\pi=\pi\circ\sigma.
\]

In particular, \(\mathcal S\) is a compact, perfect, totally disconnected
\(2\)-adic Cantor set.

---

## 4. Haar measure

Let

\[
\mathcal S_K
=
\bigcup_{w\in\{1,2\}^K}I_w.
\]

The cylinders are disjoint. Relative to Haar measure on the odd ball,

\[
\mu(I_w)=2^{-E(w)}.
\]

Thus

\[
\mu(\mathcal S_K)
=
\sum_{w\in\{1,2\}^K}2^{-E(w)}
=
\left(2^{-1}+2^{-2}\right)^K
=
\left(\frac34\right)^K.
\]

Since

\[
\mathcal S=\bigcap_{K\ge1}\mathcal S_K,
\]

continuity from above gives

\[
\boxed{\mu(\mathcal S)=0.}
\]

This is the geometric form of the fixed-time avoidance law already proved in
`repunit_rail5_density.md`.

---

## 5. Hausdorff dimension

Let \(s\) be the unique positive solution of

\[
2^{-s}+2^{-2s}=1.
\]

Writing \(u=2^{-s}\), this becomes

\[
u+u^2=1,
\qquad
u=\frac{\sqrt5-1}{2}=\frac1{\varphi},
\]

where

\[
\varphi=\frac{1+\sqrt5}{2}.
\]

Therefore

\[
\boxed{
s=\log_2\varphi
=0.6942419136\ldots.
}
\]

The maps \(\phi_1,\phi_2\) are similarities with contraction ratios
\(1/2\) and \(1/4\), and their images are disjoint. The \(2\)-adic
self-similar-set theorem therefore gives

\[
\boxed{
\dim_H\mathcal S=\log_2\varphi.
}
\]

For completeness, the two inequalities can be seen directly.

For any \(t>s\),

\[
\sum_{w\in\{1,2\}^K}
\operatorname{diam}(I_w)^t
=
\operatorname{diam}(1+2\mathbb Z_2)^t
\left(2^{-t}+2^{-2t}\right)^K
\longrightarrow0,
\]

so \(\dim_H\mathcal S\le s\).

For the reverse inequality, assign the symbolic probabilities

\[
p_1=2^{-s},
\qquad
p_2=2^{-2s},
\qquad
p_1+p_2=1.
\]

The resulting Bernoulli measure satisfies

\[
\nu(I_w)=2^{-sE(w)},
\]

which is a fixed constant multiple of
\(\operatorname{diam}(I_w)^s\). The ultrametric nesting of residue balls
then gives a Frostman bound

\[
\nu(B)\le C\,\operatorname{diam}(B)^s
\]

for all sufficiently small \(2\)-adic balls \(B\). Hence
\(\dim_H\mathcal S\ge s\).

---

## 6. Transfer to repunit indices

For odd \(m\in\mathbb Z_2\), define the \(2\)-adic base-\(9\) repunit map

\[
b(m)=\frac{9^m-1}{8}.
\]

The binomial series for \(9^m=(1+8)^m\) converges on \(\mathbb Z_2\).
The isometry theorem from `repunit_rail5_density.md` extends by continuity:

\[
v_2(b(m)-b(\ell))=v_2(m-\ell)
\qquad(m\ne\ell,\ m,\ell\text{ odd}).
\]

For an odd repunit index \(n\), avoiding rail \(5\) at time \(0\) forces

\[
n\equiv1\pmod4.
\]

Write

\[
m=\frac{n+1}{2}.
\]

Then \(m\) is odd and

\[
f(a_n)=b(m).
\]

For \(2\)-adic odd \(n\), the repunit itself extends continuously as

\[
a(n)=\frac{3\cdot9^{(n-1)/2}-1}{2}.
\]

The displayed first-step identity extends with it.

Define the infinite repunit-index survivor set

\[
\mathcal N
=
\left\{
n\in1+4\mathbb Z_2:
a(n)\text{ avoids rail }5\text{ at every odd-step}
\right\}.
\]

It has the exact representation

\[
\boxed{
\mathcal N
=
\{\,2m-1:m\in1+2\mathbb Z_2,\ b(m)\in\mathcal S\,\}.
}
\]

The map \(b\) is an isometry and \(m\mapsto2m-1\) is a similarity.
Therefore

\[
\boxed{
\mu(\mathcal N)=0,
\qquad
\dim_H\mathcal N=\log_2\varphi.
}
\]

Thus the exceptional repunit indices form, up to one fixed metric scaling, an
isometric copy of the self-similar Cantor set \(\mathcal S\), even though
their positive integer membership is not completely understood.

---

## 7. Arithmetic boundary

The geometric theorem does not imply that \(\mathcal S\), or
\(\mathcal N\), contains no positive integers.

Indeed,

\[
1\in\mathcal S
\]

with constant valuation itinerary \((2,2,2,\ldots)\), since \(f(1)=1\).
Correspondingly \(n=1\) lies in \(\mathcal N\).

The remaining arithmetic question is:

> Does \(\mathcal N\) contain any positive odd integer \(n>1\)?

Equivalently, does any nontrivial positive odd-indexed base-\(3\) repunit
avoid rail \(5\) forever?

The present theorem does not answer this. Hausdorff dimension strictly
between \(0\) and \(1\), and even Haar measure zero, do not exclude isolated
or countably many positive integer points.

---

## 8. Verification

`scripts/verify_repunit_rail5_survivor_geometry.py` checks:

- the two inverse-branch identities and their exact valuations;
- disjoint first-level images;
- exact valuation-word cylinders and their residue counts;
- the recurrence for weighted cylinder sums;
- the golden-ratio dimension equation;
- transfer through the base-\(9\) repunit isometry on finite residue rings.

```bash
python scripts/verify_repunit_rail5_survivor_geometry.py
```
