# PRED: Predecessor-density exponents from Krasikov-type inequalities, pushed past k = 11

**Building on:** `cycle_reduction.md` (the predecessor tree), the standard
difference-inequality method of Krasikov (1989), Applegate–Lagarias (1995)
and Krasikov–Lagarias (2003).
**Status:** Theorem PRED1 proved here (comparison principle; short, written in
full below). Exponents PRED2 are **computer-certified** in exact integer
arithmetic by `scripts/verify_predecessor_exponent.py`. **Not human-reviewed.**
The papers of Applegate–Lagarias and Krasikov–Lagarias were not accessible
from the session; the inequality system was reconstructed from their
published description and reproduces their exponents at \(k=9\) (\(0.817\),
cf. \(0.81\)) and \(k=11\) (\(0.8418\), cf. \(0.84\)).
**Ledger:** PRED1, PRED2
**License:** CC-BY 4.0

---

## 1. Setting

\(T(n)=n/2\) for even \(n\), \((3n+1)/2\) for odd \(n\). For \(a\ge1\) let
\(P(a)=\{n\ge1:\ T^{j}(n)=a\text{ for some }j\ge0\}\) be the set of
*predecessors* of \(a\) (including \(a\)), and
\[
\pi_a(X)=\#\bigl(P(a)\cap[1,X]\bigr).
\]
The immediate predecessors of \(a\) are \(2a\) and, when \(a\equiv2\pmod3\),
the odd number \(b(a)=(2a-1)/3\). Call \(a\) *non-cyclic* if \(a\) does not
lie on a cycle of \(T\); then \(a\notin\{1,2\}\) and no element of \(P(a)\)
is cyclic either (a cycle through \(n\in P(a)\) would contain \(a\)).

**Lemma 1 (exact recursion).** For non-cyclic \(a\) and \(X\ge a\),
\[
\pi_a(X)=1+\pi_{2a}(X)+[a\equiv2\ (3)]\,\pi_{b(a)}(X),
\]
with \(\pi_{2a}(X)=0\) when \(2a>X\).

*Proof.* \(P(a)=\{a\}\sqcup P(2a)\sqcup P(b(a))\): every \(n\in P(a)\),
\(n\ne a\), enters \(a\) for the first time from \(2a\) or from \(b(a)\); the
three sets are disjoint because a number in two of them would force the orbit
to return to \(a\), i.e.\ \(a\) cyclic. \(\square\)

For \(a\equiv0\pmod3\), \(P(a)=\{2^{j}a\}\) and \(\pi_a(X)=\lfloor\log_2(X/a)\rfloor+1\).

**Residue bookkeeping.** If \(a\equiv m\pmod{3^{k}}\) then
\(2a\equiv2m\pmod{3^{k}}\), and for \(m\equiv2\pmod3\),
\(b(a)\equiv(2m-1)/3\pmod{3^{k-1}}\), so \(b(a)\) lies in one of the three
classes
\[
c_j(m)=\frac{2m-1}{3}+j\,3^{k-1}\pmod{3^{k}},\qquad j=0,1,2,
\]
all with the same residue modulo \(3\).

## 2. The inequality system and the theorem

Fix \(k\ge1\), \(\gamma\in(0,1)\), and a vector \(v=(v_m)\) indexed by the
unit classes \(m\pmod{3^{k}}\), with \(v_m\ge0\); extend by \(v_m=0\) for
\(3\mid m\). Say \(v\) satisfies \((S_k^{\gamma})\) if for every unit class \(m\)
\[
v_m\ \le\ 2^{-\gamma}\,v_{2m}\;+\;[m\equiv2\ (3)]\,(3/2)^{\gamma}\min_{j=0,1,2}v_{c_j(m)} .
\tag{S}
\]

**Theorem PRED1.** Let \(v\) satisfy \((S_k^{\gamma})\) with \(v_m>0\) on all
unit classes, and put \(c=2^{-\gamma}/\max_mv_m\). Then for every non-cyclic
\(a\ge3\) with \(3\nmid a\) and every \(X\ge a\),
\[
\pi_a(X)\ \ge\ c\,v_{a\bmod3^{k}}\Bigl(\frac Xa\Bigr)^{\gamma}-1 .
\]
In particular \(\#\{n\le X:\ n\text{ reaches }1\}\ \ge\ \pi_4(X)\ \ge\ c\,v_{4\bmod3^k}(X/4)^{\gamma}-1\).

*Proof.* Fix \(X\) and let \(V=P(a)\cap[1,X]\), a finite set. For \(p\in V\)
write \(g(p)=\pi_p(X)\). Every \(p\in V\) is non-cyclic, so Lemma 1 gives
\(g(p)=1+g(2p)[2p\le X]+g(b(p))[p\equiv2\ (3)]\); note \(b(p)<p\), so
\(b(p)\in V\) whenever it exists. Define the operator \(A\) on functions on
\(V\) by \((Au)(p)=u(2p)[2p\le X]+u(b(p))[p\equiv2\ (3)]\). Then \(g=1+Ag\),
\(A\) is monotone, and \(A\) is nilpotent: \(A^{n}=0\) once \(n\) exceeds the
depth of the finite forest \(V\) under the parent map \(T\).

*Comparison principle.* If \(u\ge0\) on \(V\) satisfies \(u\le1+Au\), then
iterating, \(u\le1+A1+\dots+A^{n-1}1+A^{n}u=g\) for \(n\) large. So it
suffices to exhibit a subsolution.

*Subsolution.* Put \(u(p)=\max\bigl(0,\ c\,v_{m(p)}(X/p)^{\gamma}-1\bigr)\),
where \(m(p)=p\bmod3^{k}\) (so \(u=0\) on classes divisible by \(3\)). Let
\(p\in V\) with \(u(p)>0\), \(r=X/p\). Since \(c\,v_m2^{\gamma}\le1\), \(r\ge2\),
so \(2p\in V\). Set \(\alpha=c\,v_{2m}(r/2)^{\gamma}\) and, if \(p\equiv2\ (3)\)
and \(b(p)\) is in a unit class, \(\beta=c\,v_{m(b(p))}(X/b(p))^{\gamma}\),
otherwise \(\beta=0\). As \(b(p)\le2p/3\), \(X/b(p)\ge3r/2\), and
\(m(b(p))\in\{c_j(m)\}\), so by (S)
\[
c\,v_m r^{\gamma}\ \le\ \alpha+\beta .
\]
Hence
\(u(p)=c\,v_mr^{\gamma}-1\le\alpha+\beta-1
=1+(\alpha-1)+(\beta-1)\le1+u(2p)+u(b(p))\),
using \(u(2p)\ge\alpha-1\), \(u(b(p))\ge\beta-1\) (and \(u(b(p))\ge0\ge\beta-1\)
when \(\beta=0\)). So \(u\le1+Au\) on \(V\), and \(g\ge u\). \(\square\)

**Lemma 2 (monotonicity in \(k\)).** If \(v\) satisfies \((S_k^{\gamma})\) then
its lift \(v'_M=v_{M\bmod3^{k}}\) satisfies \((S_{k+1}^{\gamma})\): the three
classes \(c_j(M)\) modulo \(3^{k+1}\) all lie over the single class
\((2M-1)/3\bmod3^{k}\), which is one of the \(c_j(m)\), so the minimum can only
rise. Hence \(\gamma_k:=\sup\{\gamma:\ (S_k^{\gamma})\text{ has a positive solution}\}\)
is nondecreasing in \(k\).

## 3. Computing \(\gamma_k\)

For fixed \(\gamma\) the right side of (S) defines a map \(A_\gamma\) on
nonnegative vectors that is monotone, concave and homogeneous of degree one.
Positive solutions of \(v\le A_\gamma v\) exist iff the cone spectral radius
of \(A_\gamma\) is at least \(1\); it is computed by nonlinear power iteration
and \(\gamma_k\) by bisection (`scripts/explore_predecessor_exponent.py`).
The exponents obtained:

| \(k\) | unit classes | \(\gamma_k\) (float) |
|---|---|---|
| 2 | 6 | 0.4366 |
| 3 | 18 | 0.6113 |
| 4 | 54 | 0.6891 |
| 5 | 162 | 0.7336 |
| 6 | 486 | 0.7608 |
| 7 | 1458 | 0.7826 |
| 8 | 4374 | 0.8032 |
| 9 | 13122 | 0.8168 |
| 10 | 39366 | 0.8296 |
| 11 | 118098 | 0.8418 |
| 12 | 354294 | 0.8531 |
| 13 | 1062882 | 0.8630 |
| 14 | 3188646 | 0.8725 |
| 15 | 9565938 | 0.8812 |

Krasikov–Lagarias (2003) report \(x^{0.84}\) at \(k=11\), Applegate–Lagarias
(1995) \(x^{0.81}\); the \(k=9\) and \(k=11\) rows agree with those values,
which is the evidence that the reconstructed system is theirs.

## 4. Certified exponents (PRED2)

A certificate is a pair \((k,\gamma)\) with an integer vector \(V\) for which
`scripts/verify_predecessor_exponent.py --k k --gamma gamma` verifies (S)
exactly, with \(2^{-\gamma}\) and \((3/2)^{\gamma}\) replaced by rational
lower bounds (so the verified inequalities are stronger than (S)), all
products in 64-bit integers that provably do not overflow. Verified:

| \(k\) | certified \(\gamma\) | inequalities | min relative slack | constant \(c\) for \(a=4\) |
|---|---|---|---|---|
| 11 | 0.8417 | 118098 | \(8.9\times10^{-8}\) | \(1.46\times10^{-2}\) |
| 12 | 0.8530 | 354294 | \(1.4\times10^{-7}\) | \(9.72\times10^{-3}\) |
| 13 | 0.8629 | 1062882 | \(6.8\times10^{-8}\) | \(6.64\times10^{-3}\) |
| 14 | 0.8723 | 3188646 | \(6.4\times10^{-8}\) | \(4.60\times10^{-3}\) |
| 15 | 0.8811 | 9565938 | \(4.0\times10^{-8}\) | \(3.17\times10^{-3}\) |

Each certified row is a theorem by PRED1:
\(\#\{n\le X:\ n\to1\}\ \ge\ c\,(X/4)^{\gamma}-1\) for all \(X\ge4\), with the
printed constant \(c\).

## 5. What is and is not new

- The method is Krasikov's; the comparison-principle proof in §2 is a
  self-contained version of the "positive feasible solution gives an
  exponential lower bound" step, with the constant \(-1\) absorbing the
  boundary.
- The published record is \(x^{0.84}\) (Krasikov–Lagarias 2003, \(k=11\)).
  Every certified row with \(k\ge12\) and \(\gamma>0.8418\) improves it. The
  improvement comes only from solving the same family of systems at larger
  \(k\) with a cheap solver (nonlinear power iteration instead of nonlinear
  programming); the number of classes grows by a factor \(3\) per level and
  the exponent gain per level shrinks slowly (\(0.0112,0.0099,0.0095,0.0087\) for \(k=12,\dots,15\)).
- Krasikov conjectured \(\gamma_k\to1\). The increments here are consistent
  with slow convergence but do not decide it.
- A density-one or natural-density statement does not follow at any
  \(\gamma<1\); see `kl_rail_restricted_tree.md` §0 (W4-B).

## 6. Verification

```bash
python3 scripts/explore_predecessor_exponent.py --kmin 2 --kmax 11      # exponents, floats
python3 scripts/verify_predecessor_exponent.py --k 11 --gamma 0.8417 --count-check
python3 scripts/verify_predecessor_exponent.py --k 13 --gamma 0.8629
python3 scripts/verify_predecessor_exponent.py --k 14 --gamma 0.8723   # ~2 min
python3 scripts/verify_predecessor_exponent.py --k 15 --gamma 0.8811   # ~10 min, 1 GB
```

## 7. Ledger rows

| ID | Claim | Status | Source | Verification |
|---|---|---|---|---|
| PRED1 | For every positive solution \(v\) of the Krasikov-type system \((S_k^{\gamma})\) on unit classes mod \(3^k\), every non-cyclic \(a\ge3\), \(3\nmid a\), and \(X\ge a\): \(\pi_a(X)\ge2^{-\gamma}(v_a/\max v)(X/a)^{\gamma}-1\). Proof: subsolution + nilpotent comparison on the finite predecessor forest | Proved here (not human-reviewed) | `docs/density-cycles/predecessor_exponent.md` §2 | the recursion and forest structure are elementary; `scripts/verify_predecessor_exponent.py --count-check` cross-checks the bound against a BFS count for \(a=4\) |
| PRED2 | Certified exponents: \((k,\gamma)=(11,0.8417),(12,0.8530),(13,0.8629),(14,0.8723),(15,0.8811)\). Hence \(\#\{n\le X: n\to1\}\ge c\,X^{\gamma}\) for those \(\gamma\), improving the published \(x^{0.84}\) | Finite certificate (exact integer check of \(2\cdot3^{k-1}\) inequalities) | `docs/density-cycles/predecessor_exponent.md` §4 | `scripts/verify_predecessor_exponent.py` |
