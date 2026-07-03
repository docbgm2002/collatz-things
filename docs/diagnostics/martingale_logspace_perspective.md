# A Martingale and Large-Deviation Model for Collatz Valuations

**Building on:** `../density-cycles/stopping_time_density.md`

**Status:** Exact probability statements for Haar-random odd \(2\)-adic
starting states, followed by explicitly labelled asymptotic heuristics. No
claim is made that a fixed repunit trajectory is random or independent.

---

## 1. Probability space

For an odd starting state \(x\), write

\[
x_{j+1}=f(x_j)
=\frac{3x_j+1}{2^{e_j}},
\qquad
e_j=v_2(3x_j+1).
\]

Choose \(x\) according to normalized Haar measure on the odd ball
\(1+2\mathbb Z_2\). The exact valuation-pattern theorem gives

\[
\Pr(e_0=k_0,\ldots,e_{K-1}=k_{K-1})
=2^{-(k_0+\cdots+k_{K-1})}.
\]

Consequently the \(e_j\) are independent geometric variables with

\[
\Pr(e_j=k)=2^{-k},
\qquad k\ge1,
\]

and

\[
\mathbb E[e_j]=2,
\qquad
\operatorname{Var}(e_j)=2.
\]

This is an exact finite-dimensional distribution over starting residue
classes. It does not imply that the valuations of one named deterministic
orbit may be treated as fresh random draws for an unbounded argument.

---

## 2. The exact normalized multiplicative martingale

Define

\[
R_j=\frac{3}{2^{e_j}},
\qquad
M_K=\prod_{j<K}R_j=\frac{3^K}{2^{E_K}},
\qquad
E_K=\sum_{j<K}e_j.
\]

Since

\[
\mathbb E[R_j]
=\sum_{k\ge1}\frac3{2^k}2^{-k}
=3\sum_{k\ge1}4^{-k}
=1,
\]

independence gives

\[
\mathbb E[M_{K+1}\mid e_0,\ldots,e_{K-1}]
=M_K.
\]

Thus:

\[
\boxed{(M_K)_{K\ge0}\text{ is a nonnegative mean-one martingale}.}
\]

This martingale describes the homogeneous multiplier in the exact affine
formula

\[
x_K=\frac{3^Kx+c_K}{2^{E_K}}.
\]

It does **not** make \(x_K\) itself a martingale. The \(+1\) terms accumulate
in the positive affine correction \(c_K\).

At one formal step with a fixed value \(x\),

\[
\sum_{k\ge1}
\frac{3x+1}{x\,2^k}\,2^{-k}
=1+\frac1{3x}.
\]

This calculation is only a comparison model: for fixed \(x\), its actual
valuation is deterministic.

---

## 3. Logarithmic drift

In base-\(2\) units,

\[
\log_2 R_j=\log_2 3-e_j.
\]

Therefore

\[
\boxed{
\mathbb E[\log_2 R_j]
=\log_2 3-2
=-0.4150374992\ldots,
}
\]

and

\[
\boxed{\operatorname{Var}(\log_2R_j)=2.}
\]

In natural-log units the corresponding values are

\[
\mathbb E[\ln R_j]=\ln(3/4)=-0.2876820724\ldots,
\]

\[
\operatorname{Var}(\ln R_j)=2(\ln2)^2.
\]

The distinction between the two logarithm bases is essential.

The arithmetic mean of \(R_j\) is \(1\), while the mean logarithmic return is
negative. Rare small valuations support the arithmetic mean; a typical
product decays exponentially.

---

## 4. Central-limit and diffusion approximations

The classical central limit theorem gives

\[
\frac{\log_2 M_K-K(\log_2 3-2)}{\sqrt{2K}}
\Longrightarrow N(0,1).
\]

Equivalently, after diffusive scaling, the distribution of the log multiplier
is approximated by a Gaussian with drift.

In natural-log coordinates, the corresponding continuum density satisfies
the convection-diffusion equation

\[
\frac{\partial p}{\partial t}
=-\mu\frac{\partial p}{\partial y}
+\frac{\sigma^2}{2}\frac{\partial^2p}{\partial y^2},
\]

with

\[
\mu=\ln(3/4),
\qquad
\sigma^2=2(\ln2)^2.
\]

This PDE is a scaling limit of the independent-increment model. It is not an
exact evolution equation for the discrete Collatz map, and it supplies no
maximum principle for an individual integer orbit.

The resemblance to log-price diffusion is generic to multiplicative random
processes. No specifically financial machinery is needed here.

---

## 5. Exact large deviations for valuation surplus

Define the surplus increment

\[
Y=e-\log_2 3
\]

and the cumulative surplus

\[
S_K=E_K-K\log_2 3.
\]

For \(\theta<1\), the base-\(2\) cumulant generating function is

\[
\begin{aligned}
\Lambda(\theta)
&=\log_2\mathbb E[2^{\theta Y}]\\
&=-\theta\log_2 3
-\log_2(2^{1-\theta}-1).
\end{aligned}
\]

Let

\[
u=s+\log_2 3.
\]

The Cramér rate function for \(S_K/K\) is

\[
\boxed{
I(s)
=u+(u-1)\log_2(u-1)-u\log_2u
}
\]

when \(u>1\). At the lower endpoint,

\[
\boxed{I(1-\log_2 3)=1,}
\]

because attaining the minimum average requires every valuation to equal
\(1\), an event of probability \(2^{-K}\). For

\[
s<1-\log_2 3,
\]

the event is impossible and \(I(s)=+\infty\).

The mean surplus is

\[
\bar s=2-\log_2 3=0.4150374992\ldots,
\]

where \(I(\bar s)=0\).

For any fixed threshold

\[
1-\log_2 3<s<\bar s,
\]

Cramér's theorem gives

\[
\Pr(S_K/K\le s)
=2^{-K(I(s)+o(1))}.
\]

This is an exact asymptotic statement in the Haar-random model.

---

## 6. Relation to deterministic repunit tails

For

\[
a_n=\frac{3^n-1}{2},
\]

the valuation sequence is deterministic. The probability formulas above
measure the set of arbitrary odd starting residues realizing a bad valuation
prefix; they do not assign a probability to the named point \(a_n\).

Accordingly, the model can do two legitimate jobs:

1. quantify the Haar measure of low-surplus valuation words;
2. suggest which deterministic non-concentration theorem would be sufficient.

It cannot prove that the repunit curve avoids those words.

In particular, a z-score evaluated at the first-descent time is not a valid
test against the fixed-time Gaussian law. The stopping time is selected from
the same increments being measured, so the resulting sample is conditioned
and censored.

The remaining arithmetic problem is still:

> Control the intersection between the deterministic repunit-index curve and
> low-surplus residue cylinders whose depth grows with \(n\).

The martingale model describes the size of those cylinders, not their
membership.

---

## 7. What is proved and what is heuristic

**Proved in the Haar-random model:**

- independent geometric valuation patterns;
- the mean-one martingale \(M_K=3^K/2^{E_K}\);
- logarithmic mean and variance;
- the cumulant generating function and rate function;
- the fixed-time central limit theorem and Cramér large-deviation principle.

**Heuristic only:**

- treating one deterministic trajectory as an independent random path;
- using the diffusion PDE to predict an individual stopping time;
- inferring repunit non-concentration from the small Haar measure of bad
  cylinders.

---

## 8. Verification

`scripts/explore_martingale_repunit_drift.py` checks the formulas, exact finite
valuation-pattern counts, the rate-function boundary, and descriptive
fixed-window repunit data.

```bash
python scripts/explore_martingale_repunit_drift.py
```

Its repunit output is explicitly descriptive and is not used as evidence for
independence or a universal theorem.
