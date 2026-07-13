# General-Payout Shell Ancestry

**Status:** GPA1 and GPA2 are proved here and machine-checked. Their
consequence is partly negative: the canonical single-partner mechanism is
blocked for payouts \(q\equiv3,4\pmod6\), including \(q=3\).

**Building on:** repunit_extremal_principle.md,
primitive_ancestry_lemma.md

## 1. Setup

Let a realised high repunit tail have pre-payout word length \(j\), cumulative
valuation \(E\), and payout \(q=e_j\ge2\). Put

\[
F=E+q,\qquad
h=\left\lfloor\frac q2\right\rfloor,\qquad
u=F-2h=E+(q\bmod2),\qquad
d=n+j+1.
\]

If \(X=x_{j+1}(n)\), the canonical shell partner from REPEXT5 is

\[
Y=4^hX+\frac{4^h-1}{3},\qquad f(Y)=f(X),
\]

and its correction is

\[
C=A_{j+1}+S(u,2h),\qquad
S(u,2h)=2^{u+1}\frac{2^{2h}-1}{3}.
\]

The normal form is

\[
3^d+C=2^{u+1}Y,
\]

with \(Y\) odd.

## 2. GPA1: automatic realisation for every payout

Let \(\mathbf f=(f_0,\ldots,f_{i-1})\) be a positive valuation word of total
\(u\), and suppose

\[
A_i(\mathbf f)=C.
\]

Set \(m=d-i\). With

\[
c(\mathbf f)=\frac{A_i(\mathbf f)+3^i}{2},\qquad
a_m=\frac{3^m-1}{2},
\]

we obtain

\[
3^ia_m+c(\mathbf f)
=\frac{3^{m+i}+A_i(\mathbf f)}2
=\frac{3^d+C}{2}
=2^uY.
\]

The accumulated numerator has exact valuation \(u\), because \(Y\) is odd.
The exact-itinerary criterion therefore proves that \(a_m\) realises the
entire word \(\mathbf f\), and

\[
f^i(a_m)=Y.
\]

Whenever \(m\) is a positive odd integer smaller than \(n\), this gives

\[
f^{i+1}(a_m)=f(Y)=f(X)=f^{j+2}(a_n).
\]

As in the \(q=2\) case, those conditions are equivalent to

\[
\boxed{
j+2\le i\le\min(u,d-1),\qquad
i\equiv j+1\pmod2.
}
\]

> **GPA1.** For every realised payout \(q\ge2\), equality of its canonical
> shell-partner correction with a source correction in an admissible aligned
> layer automatically realises the complete smaller repunit valuation word
> and forces a next-step merge. No additional source-prefix congruence is
> required.

The proof of REPANC1 was therefore not intrinsically a \(q=2\) argument.

## 3. GPA2: an exact modulo-\(3\) obstruction

Every nonempty source correction layer avoids zero modulo \(3\). Indeed,

\[
A_i=3A_{i-1}+2^{E_{i-1}+1}
\]

gives

\[
\boxed{A_i\not\equiv0\pmod3.}
\]

Now write

\[
T_h=\frac{4^h-1}{3}.
\]

Since \(4^h\pmod9\) has period three,

\[
T_h\equiv
\begin{cases}
1\pmod3,&h\equiv1\pmod3,\\
2\pmod3,&h\equiv2\pmod3,\\
0\pmod3,&h\equiv0\pmod3.
\end{cases}
\]

Let \(\delta=q\bmod2\). Using \(u=E+\delta\), the target correction satisfies

\[
C
=3A_j+2^{E+1}+2^{E+\delta+1}T_h
\equiv
2^{E+1}\left(1+2^\delta T_h\right)
\pmod3.
\]

If \(q\) is even, this vanishes exactly when \(h\equiv2\pmod3\), or
\(q\equiv4\pmod6\). If \(q\) is odd, it vanishes exactly when
\(h\equiv1\pmod3\), or \(q\equiv3\pmod6\). Therefore

\[
\boxed{
C\equiv0\pmod3
\iff
q\equiv3\text{ or }4\pmod6.
}
\]

Combining this with \(A_i\not\equiv0\pmod3\) proves:

> **GPA2.** If \(q\equiv3,4\pmod6\), the canonical shell partner cannot be
> reached from any positive-length repunit correction word, at any source
> layer or exponent.

In particular, every \(q=3\) canonical partner is structurally unreachable.
This is not a sparse finite phenomenon and cannot be repaired by searching
larger correction layers.

## 4. Strategic consequence

The general-\(q\) extension succeeds algebraically but exposes a no-go result
for the most common dangerous payout in the finite record census. The
single-canonical-partner route must split by payout class:

- \(q\equiv0,1,2,5\pmod6\): correction equality remains arithmetically
  possible, so direct shell reachability may be pursued;
- \(q\equiv3,4\pmod6\): direct reachability is impossible modulo \(3\), so
  progress must come from a different shell choice, bounded multi-ancestor
  combinations, or a quantitative payout charge.

This sends the dominant \(q=3\) population directly to the
concentration-versus-diffusion and two-ancestor attacks. It also provides a
clean regression condition for any proposed general-payout lemma.

## 5. Verification and ledger entries

The verifier scripts/verify_repunit_general_payout_ancestry.py checks the
modulo-\(3\) classification for payouts through \(q=30\), exhausts small
correction layers, and verifies every realised aligned match in its stated
range by following both exact integer tails to the common next odd iterate.

    python scripts/verify_repunit_general_payout_ancestry.py

| ID | Claim | Status | Verification |
|---|---|---|---|
| GPA1 | Automatic shell-partner realisation holds for every payout \(q\ge2\) at an admissible aligned correction match | Proved here | Exact-itinerary proof; verifier checks small layers and realised matches |
| GPA2 | Canonical shell reachability is impossible for \(q\equiv3,4\pmod6\) | Proved here | Exact modulo-\(3\) argument; verifier checks source and target residues |
