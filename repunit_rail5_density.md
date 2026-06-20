# A Rail-5 Density Theorem for Base-3 Repunit Trajectories

**Building on:** `repunit_rail5_exact.md`, `stopping_time_density.md`
**Status:** Proved here. This is a density theorem, not a universal
rail-hitting result and not a proof of the Collatz conjecture.
**License:** CC-BY 4.0

---

## Abstract

Let

$$
a_n=\frac{3^n-1}{2}\qquad(n\text{ odd})
$$

and let \(T(n)\) be the first odd-step time at which the trajectory of \(a_n\)
lies on rail \(5\bmod8\), with \(T(n)=\infty\) if no such time exists.
The one-step classification in `repunit_rail5_exact.md` gives
\(\Pr(T\le1)=5/8\) in natural density. Here we extend that result to every
fixed time:

$$
\boxed{\operatorname{dens}\{n\text{ odd}:T(n)>K\}
=\frac12\left(\frac34\right)^K}
$$

and hence

$$
\boxed{\operatorname{dens}\{n\text{ odd}:T(n)\le K\}
=1-\frac12\left(\frac34\right)^K.}
$$

The proof has two ingredients. First, after restricting to the half of the
indices that do not start on rail 5, the first iterate is a base-9 repunit
\(b_m=(9^m-1)/8\); the map \(m\mapsto b_m\) is a 2-adic isometry and therefore
permutes odd residue classes at every power of two. Second, exact shortcut
valuation patterns have product density, and avoiding rail 5 at a state is
equivalent to its next valuation belonging to \(\{1,2\}\), an event of density
\(1/2+1/4=3/4\).

Consequently almost every odd-indexed repunit eventually reaches rail 5, and
the exceptional set has natural density zero. This does not show that every
repunit reaches rail 5.

---

## 1. Setup

For odd \(x\), write

$$
f(x)=\frac{3x+1}{2^{v_2(3x+1)}}.
$$

For odd \(n\), set \(x_0=a_n\) and \(x_j=f^{(j)}(a_n)\). Define

$$
T(n)=\min\{j\ge0:x_j\equiv5\pmod8\},
$$

when this set is nonempty.

For \(K\ge0\), let

$$
A_K=\{n\text{ odd}:T(n)>K\}.
$$

Thus \(A_K\) consists of indices whose repunit trajectory avoids rail 5 at
each of the states \(x_0,x_1,\ldots,x_K\).

---

## 2. The base-9 repunit map is a 2-adic isometry

For odd \(m\), define

$$
b_m=\frac{9^m-1}{8}.
$$

**Lemma 1.** For distinct odd positive integers \(m,\ell\),

$$
v_2(b_m-b_\ell)=v_2(m-\ell).
$$

Consequently, for every \(q\ge1\), the map

$$
m\bmod2^q\longmapsto b_m\bmod2^q
$$

is a bijection on the odd residue classes modulo \(2^q\).

**Proof.** Assume \(m>\ell\). Then

$$
b_m-b_\ell
=\frac{9^\ell(9^{m-\ell}-1)}8.
$$

Both \(m\) and \(\ell\) are odd, so \(d=m-\ell\) is even. By LTE,

$$
v_2(9^d-1)=v_2(9-1)+v_2(d)=3+v_2(d).
$$

Since \(9^\ell\) is odd, division by \(8\) gives

$$
v_2(b_m-b_\ell)=v_2(d)=v_2(m-\ell).
$$

In particular, two odd inputs are congruent modulo \(2^q\) exactly when their
images are. The induced map on the finite set of odd classes modulo \(2^q\)
is injective and hence bijective. \(\blacksquare\)

This is stronger than mere equidistribution: the base-9 repunit map preserves
the full 2-adic distance between odd indices.

---

## 3. Rail 5 is the large-valuation rail

Let

$$
e(x)=v_2(3x+1)
$$

for odd \(x\).

**Lemma 2.** For odd \(x\),

$$
x\equiv5\pmod8
\quad\Longleftrightarrow\quad
e(x)\ge3.
$$

Thus \(x\) avoids rail 5 exactly when \(e(x)\in\{1,2\}\).

**Proof.** We have \(e(x)\ge3\) exactly when \(3x+1\equiv0\pmod8\).
Since \(3^{-1}\equiv3\pmod8\), this is equivalent to

$$
x\equiv-3\equiv5\pmod8.
$$

\(\blacksquare\)

---

## 4. Exact valuation-pattern density

The following is the valuation-pattern lemma used in
`stopping_time_density.md`.

**Lemma 3.** Fix \(K\ge1\) and positive integers
\((e_1,\ldots,e_K)\). Among odd integers, the shortcut valuation pattern

$$
v_2(3x_{j-1}+1)=e_j,\qquad x_j=f(x_{j-1}),
$$

has natural density

$$
2^{-(e_1+\cdots+e_K)}.
$$

Equivalently, the valuations are exactly distributed as independent
geometric variables with

$$
\Pr(e_j=r)=2^{-r}\qquad(r\ge1).
$$

**Proof.** A one-step valuation \(e_1=r\) selects one odd residue class modulo
\(2^{r+1}\), of relative density \(2^{-r}\) among odd integers. On that class,
the affine shortcut map is a bijection onto odd residue classes of the
remaining modulus. Iterating gives one class for each prescribed pattern and
multiplies the relative densities:

$$
2^{-e_1}\cdots2^{-e_K}=2^{-\sum e_j}.
$$

This is the exact residue-class statement behind the Terras/Everett
equidistribution, not a probabilistic independence assumption.
\(\blacksquare\)

**Corollary 4.** The density of odd \(x\) whose first \(K\) states
\(x,f(x),\ldots,f^{(K-1)}(x)\) all avoid rail 5 is

$$
\sum_{(e_1,\ldots,e_K)\in\{1,2\}^K}
2^{-(e_1+\cdots+e_K)}
=\left(\frac12+\frac14\right)^K
=\left(\frac34\right)^K.
$$

---

## 5. The density theorem

**Theorem 5 (Rail-5 hitting density).** For every integer \(K\ge0\),

$$
\operatorname{dens}(A_K)
=\operatorname{dens}\{n\text{ odd}:T(n)>K\}
=\frac12\left(\frac34\right)^K.
$$

Equivalently,

$$
\operatorname{dens}\{n\text{ odd}:T(n)\le K\}
=1-\frac12\left(\frac34\right)^K.
$$

**Proof.** By `repunit_rail5_exact.md`, Theorem R5.1:

- \(n\equiv3\pmod4\) gives \(a_n\equiv5\pmod8\), so \(T(n)=0\);
- \(n\equiv1\pmod4\) gives \(a_n\equiv1\pmod8\), so the initial state avoids
  rail 5.

The second class has relative density \(1/2\) among odd indices. Write
\(n=4s+1\) and

$$
m=\frac{n+1}{2}=2s+1.
$$

Then \(m\) runs through the odd integers, and Theorem R5.3 gives

$$
x_1=f(a_n)=b_m=\frac{9^m-1}{8}.
$$

By Lemma 1, \(m\mapsto b_m\) bijects the odd residue classes modulo every
power of two. Therefore density questions about any fixed number of shortcut
steps starting at \(x_1=b_m\) are identical to the corresponding density
questions for arbitrary odd starting values.

The condition \(T(n)>K\), after the already-safe initial state \(x_0\), is
that the \(K\) states \(x_1,\ldots,x_K\) avoid rail 5. By Corollary 4 this has
conditional density \((3/4)^K\). Multiplying by the initial factor \(1/2\)
gives

$$
\operatorname{dens}(A_K)
=\frac12\left(\frac34\right)^K.
$$

Taking the complement proves the hitting formula. \(\blacksquare\)

For \(K=1\), the theorem recovers the earlier density

$$
1-\frac12\cdot\frac34=\frac58.
$$

---

## 6. Consequences

**Corollary 6 (Almost-everywhere rail-5 hit).** The set of odd indices whose
repunit trajectory never reaches rail 5 has natural density zero.

**Proof.** For every \(K\),

$$
\{n:T(n)=\infty\}\subseteq A_K,
$$

whose density is \(\frac12(3/4)^K\). Letting \(K\to\infty\) gives density
zero. \(\blacksquare\)

**Corollary 7 (Exact hitting-time distribution).** In natural density,

$$
\Pr(T=0)=\frac12,
$$

and for \(k\ge1\),

$$
\Pr(T=k)
=\frac18\left(\frac34\right)^{k-1}.
$$

The density-average hitting time is therefore

$$
\mathbb E[T]
=\sum_{K\ge0}\Pr(T>K)
=\sum_{K\ge0}\frac12\left(\frac34\right)^K
=2.
$$

These are distributional statements over the repunit indices. They do not
bound \(T(n)\) for an individual index.

---

## 7. What this does and does not prove

**Proved:**

- exact geometric density for avoiding rail 5 through any fixed number of
  odd-steps;
- natural density one for eventual rail-5 hitting;
- the exact density distribution and density-average of the first hit time.

**Not proved:**

- that every odd-indexed repunit reaches rail 5;
- the empirical 12-step bound from `repunit_rail5_exact.md`;
- that a rail-5 step sends the trajectory below the original Mersenne number
  \(2^n-1\);
- a uniform or linear bound for the full Mersenne epoch.

The surviving exceptional indices form a geometrically shrinking family of
2-adic residue classes. Eliminating every member of their intersection, rather
than merely proving density zero, remains the hard point.

---

## 8. Verification

`verify_repunit_rail5_density.py` checks:

- the isometry \(v_2(b_m-b_\ell)=v_2(m-\ell)\);
- the induced permutation of odd residue classes modulo powers of two;
- the exact finite count \(3^K\) rail-avoiding classes among the \(4^K\) odd
  classes modulo \(2^{2K+1}\);
- the corresponding repunit-index count through the base-9 isometry;
- direct complete-period counts using the actual repunits for small \(K\);
- agreement with the formula
  \(1-\frac12(3/4)^K\) over finite index samples.

```bash
python verify_repunit_rail5_density.py
```
