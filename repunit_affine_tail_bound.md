# An Affine-Tail Bound for the Repunit Descent Problem

**Building on:** `repunit_tail_attack.md`, `stopping_time_density.md`
**Status:** Proved here. This controls the affine correction but does not prove
the required valuation surplus or the Mersenne epoch bound.
**License:** CC-BY 4.0

---

## 1. Setup

For odd \(n\), let

\[
a=a_n=\frac{3^n-1}{2},
\qquad
T=2^n-1,
\qquad
x_0=a,
\qquad
x_{i+1}=f(x_i).
\]

Write

\[
e_i=v_2(3x_i+1),
\qquad
E_i=\sum_{j<i}e_j.
\]

The affine accumulation formula is

\[
x_i=\frac{3^i a+c_i}{2^{E_i}},
\qquad
c_0=0,
\qquad
c_{i+1}=3c_i+2^{E_i}.
\]

Define the relative affine correction

\[
q_i=\frac{c_i}{3^i a}.
\]

Then

\[
x_i=\frac{3^i a(1+q_i)}{2^{E_i}}.
\]

---

## 2. Exact recurrence

**Lemma 1.** For every \(i\ge0\),

\[
q_{i+1}
=q_i+\frac{1+q_i}{3x_i},
\]

or equivalently

\[
1+q_{i+1}
=(1+q_i)\left(1+\frac1{3x_i}\right).
\]

**Proof.** From the affine recurrence,

\[
q_{i+1}
=\frac{3c_i+2^{E_i}}{3^{i+1}a}
=q_i+\frac{2^{E_i}}{3^{i+1}a}.
\]

The accumulated form for \(x_i\) gives

\[
2^{E_i}=\frac{3^i a(1+q_i)}{x_i}.
\]

Substitution yields

\[
q_{i+1}
=q_i+\frac{1+q_i}{3x_i}.
\]

Adding \(1\) and factoring proves the product form. \(\blacksquare\)

**Corollary 2 (exact product).**

\[
1+q_K=\prod_{i=0}^{K-1}\left(1+\frac1{3x_i}\right).
\]

---

## 3. Uniform pre-descent bound

**Theorem 3.** Suppose the repunit trajectory has not descended below the
Mersenne target before step \(K\):

\[
x_i\ge T\qquad(0\le i<K).
\]

Then

\[
1+q_K
\le
\left(1+\frac1{3T}\right)^K
\]

and hence the affine penalty satisfies

\[
\boxed{
\log_2(1+q_K)
\le
K\log_2\left(1+\frac1{3T}\right)
<
\frac{K}{3T\ln2}.
}
\]

**Proof.** Corollary 2 and \(x_i\ge T\) give

\[
1+q_K
=\prod_{i<K}\left(1+\frac1{3x_i}\right)
\le
\prod_{i<K}\left(1+\frac1{3T}\right)
=\left(1+\frac1{3T}\right)^K.
\]

Take base-\(2\) logarithms. The strict upper bound follows from
\(\ln(1+u)<u\) for \(u>0\). \(\blacksquare\)

For every linear window \(K\le Cn\), this is exponentially small in \(n\):

\[
\log_2(1+q_K)
<
\frac{Cn}{3(2^n-1)\ln2}.
\]

---

## 4. Exact surplus criterion

Define the raw surplus

\[
S_K(n)
=E_K-K\log_2 3
-\log_2\left(\frac{a_n}{2^n-1}\right).
\]

The exact descent margin is

\[
\log_2\left(\frac{T}{x_K}\right)
=S_K(n)-\log_2(1+q_K).
\]

**Corollary 4 (affine-safe descent criterion).** If

\[
S_K(n)
>
K\log_2\left(1+\frac1{3(2^n-1)}\right),
\]

then the repunit trajectory descends below \(2^n-1\) by time \(K\).

**Proof.** If an earlier iterate is below the target, the conclusion already
holds. Otherwise Theorem 3 applies through step \(K\), and the assumed raw
surplus exceeds the affine penalty. Therefore the exact margin is positive,
so \(x_K<T\). \(\blacksquare\)

This removes the affine term as a substantial obstruction in the repunit
problem. The remaining task is to force the valuation surplus \(S_K(n)\)
positive by more than an exponentially small allowance.

---

## 5. What this does and does not prove

**Proved:**

- an exact multiplicative product for the relative affine correction;
- an exponentially small pre-descent bound in every linear window;
- a rigorous surplus threshold that implies actual descent.

**Not proved:**

- that the valuation surplus crosses this threshold by \(K\le3n\);
- any universal linear bound for \(\sigma(a_n)\);
- the Collatz conjecture.

The result closes the bookkeeping gap between raw valuation surplus and exact
descent. Future block-surplus lemmas may use Corollary 4 without silently
discarding \(c_K\).

---

## 6. Verification

`verify_repunit_affine_tail.py` checks the exact recurrence, product identity,
uniform bound, margin decomposition, and descent criterion over finite ranges.

```bash
python verify_repunit_affine_tail.py
```

