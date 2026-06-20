# Baker Applicability Census

**Building on:** `repunit_baker_nonshadowing.md`,
`repunit_tail_merge_reduction.md`
**Status:** Exact identities plus finite diagnostics. No universal
non-shadowing theorem is claimed.
**License:** CC-BY 4.0

---

## 1. Purpose

The fixed branch \((2,1^{K-1})\) reduces to

\[
v_2(3^{n+1}+7)\ge K+3,
\]

so a fixed-\(d\) \(p\)-adic logarithmic-form estimate gives
\(K=O(\log n)\).

The census asks whether active primitive repunit tails contain other recurring
low-height enemy constants to which the same method can be applied.

Only states before first descent are included.

---

## 2. Enemy coordinates

At prefix length \(K\), write

\[
x_K=\frac{3^{n+K}+A_K}{2^{E_K+1}},
\qquad
R_K=A_K+2^{E_K+1}.
\]

Factor

\[
R_K=3^{r_K}d_K,\qquad 3\nmid d_K,
\]

and define

\[
m_K=n+K-r_K.
\]

Oddness gives the enemy equation

\[
v_2(3^{m_K}+d_K)\ge E_K+2.
\]

The pair

\[
\boxed{\mathcal B_K=(m_K,d_K)}
\]

is the **enemy coordinate** of the prefix.

---

## 3. Persistence is exactly a valuation-one run

The normal-form recurrence is

\[
A_{K+1}=3A_K+2^{E_K+1}.
\]

If the next valuation is \(e_K=1\), then \(E_{K+1}=E_K+1\), and hence

\[
\begin{aligned}
R_{K+1}
&=A_{K+1}+2^{E_{K+1}+1}\\
&=3A_K+2^{E_K+1}+2^{E_K+2}\\
&=3R_K.
\end{aligned}
\]

Therefore

\[
r_{K+1}=r_K+1,\qquad
d_{K+1}=d_K,\qquad
m_{K+1}=m_K.
\]

Thus \(\mathcal B_K\) is invariant through every consecutive run of
valuation \(1\). A fixed enemy constant is not an accidental numerical
feature: it is the exact algebraic coordinate of a low-valuation run.

Conversely, if \(d_{K+1}=d_K\), comparison of

\[
R_{K+1}=3R_K+2^{E_K+1}(2^{e_K}-2)
\]

shows why valuation \(1\) is the natural persistence mechanism. The finite
census verifies that every displayed consecutive same-\(d\) run is precisely
such a run.

---

## 4. Finite census through \(n\le5001\)

Run:

```bash
python explore_baker_applicability.py --limit 5001
```

The finite domain contains:

- \(165\) primitive tails;
- \(342{,}694\) active pre-descent prefix states;
- approximately \(341{,}551\) states with \(K\ge8\).

For those \(K\ge8\) states, with

\[
h_K=\operatorname{bitlength}|d_K|,
\]

the height-ratio counts are:

| range for \(h_K/E_K\) | states |
|---|---:|
| \(h_K/E_K>1\) | 236,488 |
| \(0.75<h_K/E_K\le1\) | 105,017 |
| \(0.50<h_K/E_K\le0.75\) | 37 |
| \(0.25<h_K/E_K\le0.50\) | 9 |

Hence generic active primitive prefixes retain essentially all their
valuation-scale information in \(d_K\). Direct variable-height Baker bounds
are not automatically strong enough.

The longest observed valuation-one run has length \(17\), on \(n=2429\),
ending at \(K=2730\). Its enemy constant has \(5326\) bits while
\(E_K=5339\), so it is a high-height family despite being fixed during the
run.

The strongest observed cancellations include:

| \(n\) | \(K\) | \(E_K\) | \(d_K\) | bits of \(d_K\) |
|---:|---:|---:|---:|---:|
| 173 | 9 | 10 | 7 | 3 |
| 25 | 10 | 13 | 23 | 5 |
| 3881 | 15 | 19 | 133 | 8 |
| 229 | 11 | 15 | 223 | 8 |
| 35 | 14 | 19 | 679 | 10 |

These are genuine Baker-applicable finite families, but the current data does
not show any one of them recurring across a broad collection of primitive
exponents.

---

## 5. Cross-exponent enemy-coordinate collisions

Among repeated reduced constants at \(K\ge8\), the census found \(91\)
families represented on two different primitive exponents. Every such
cross-exponent repetition also had the same \(m_K\).

Thus the observed repetition is of the full enemy coordinate
\((m_K,d_K)\), not merely of \(d_K\).

This does not imply exact trajectory merger. From

\[
x_K+1
=
\frac{3^{r_K}(3^{m_K}+d_K)}{2^{E_K+1}},
\]

two tails with the same \((m,d)\) can still have different \(r_K\) and
\(E_K\). Nevertheless, these collisions identify a shared arithmetic anchor
and are a natural interface with the merger programme.

---

## 6. Strategic conclusion

Baker/Yu should be used as a **family eliminator**, not as the sole global
argument:

1. detect a persistent enemy coordinate \((m,d)\);
2. if \(d\) has controlled height, bound the possible valuation-one run by a
   \(2\)-adic logarithmic-form estimate;
3. if \(d\) has generic height comparable to \(E\), send the state to a
   surplus or merger argument;
4. analyse repeated cross-exponent enemy coordinates for a weaker
   coalescence or inheritance relation.

The next theorem-shaped target is therefore:

> **Enemy-coordinate dichotomy.** An active primitive prefix either has
> controlled reduced enemy height, in which case Baker non-shadowing bounds
> its following valuation-one run, or its high-height enemy coordinate forces
> a surplus recovery or a collision with an earlier controlled coordinate.

The first half is now well formulated. The second half remains the central
proof target.
