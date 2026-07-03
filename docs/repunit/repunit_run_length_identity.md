# The Fuel-Enemy Bridge and an Exact Run-Length Identity

**Building on:** `repunit_baker_applicability_census.md`,
`repunit_extremal_principle.md`, `repunit_baker_nonshadowing.md`,
`../core/Block_Fracture_Lemma.md`
**Status:** Exact identities, proved here and machine-checked. They do not by
themselves bound the trajectory; they unify three existing pictures and
isolate one Diophantine crux.
**License:** CC-BY 4.0

---

## 1. Setup

For odd \(n\), let \(a_n=(3^n-1)/2\), \(x_K=f^{(K)}(a_n)\), and use the
repunit normal form

\[
x_K=\frac{3^{n+K}+A_K}{2^{E_K+1}},
\qquad
A_{K+1}=3A_K+2^{E_K+1},
\qquad
E_{K+1}=E_K+e_K.
\]

Put

\[
R_K=A_K+2^{E_K+1},
\qquad
R_K=3^{r_K}d_K\ (3\nmid d_K),
\qquad
m_K=n+K-r_K,
\]

so \((m_K,d_K)\) is the enemy coordinate of
`repunit_baker_applicability_census.md`. Write the trailing-ones fuel

\[
\tau(x)=v_2(x+1).
\]

---

## 2. The fuel-enemy bridge

**Theorem 1.** For every \(K\) before first descent,

\[
\boxed{\;\tau(x_K)=v_2\bigl(3^{m_K}+d_K\bigr)-E_K-1.\;}
\]

**Proof.** Since \(x_K\) is a positive odd integer,

\[
x_K+1=\frac{3^{n+K}+R_K}{2^{E_K+1}}
=\frac{3^{r_K}\bigl(3^{m_K}+d_K\bigr)}{2^{E_K+1}}.
\]

The factor \(3^{r_K}\) is odd, so

\[
v_2(x_K+1)=v_2\bigl(3^{m_K}+d_K\bigr)-(E_K+1).\qquad\blacksquare
\]

The left side is a property of the current value; the right side is a
\(2\)-adic linear-form valuation minus the accumulated valuation. This is the
exact dictionary between the **fuel/burn** language
(`../core/Block_Fracture_Lemma.md`) and the **enemy-coordinate/Baker** language.

---

## 3. Valuation-one runs are trailing-one burns

**Lemma 2.** If \(e_K=1\) then

\[
\tau(x_{K+1})=\tau(x_K)-1,
\]

and the enemy coordinate is unchanged: \((m_{K+1},d_{K+1})=(m_K,d_K)\).
Moreover

\[
e_K=1\iff\tau(x_K)\ge2,
\qquad
e_K\ge2\iff\tau(x_K)=1.
\]

**Proof.** For the accelerated map an \(e_K=1\) step is
\(x_{K+1}=(3x_K+1)/2\), hence

\[
x_{K+1}+1=\frac{3x_K+3}{2}=\frac{3(x_K+1)}2,
\]

so \(v_2(x_{K+1}+1)=v_2(x_K+1)-1\). The parity facts are
\(e_K=v_2(3x_K+1)=1\iff x_K\equiv3\pmod4\iff\tau(x_K)\ge2\), and the
complementary case \(x_K\equiv1\pmod4\iff\tau(x_K)=1\) forces \(e_K\ge2\).
Invariance of \((m,d)\): from
\(R_{K+1}=3R_K+2^{E_K+1}(2^{e_K}-2)\) and \(2^{1}-2=0\) we get
\(R_{K+1}=3R_K\), so \(r_{K+1}=r_K+1\), \(d_{K+1}=d_K\), and
\(m_{K+1}=n+(K+1)-(r_K+1)=m_K\). \(\blacksquare\)

---

## 4. The exact run-length identity

**Theorem 3.** A maximal valuation-one run beginning at step \(K_0\) has
length exactly

\[
\boxed{\;
L=\tau(x_{K_0})-1
=v_2\bigl(3^{m_{K_0}}+d_{K_0}\bigr)-E_{K_0}-2.
\;}
\]

**Proof.** By Lemma 2 the fuel drops by exactly \(1\) on each \(e=1\) step,
and the run continues while \(\tau\ge2\), terminating with a payout when
\(\tau=1\). Hence the number of \(e=1\) steps is \(\tau(x_{K_0})-1\).
Substitute Theorem 1. \(\blacksquare\)

Both identities are checked exactly in `scripts/verify_repunit_run_length.py` for odd
\(3\le n\le201\) (14392 step checks; 3601 closed runs; no deviation).

---

## 5. Why this matters

The valuation deficit \(D_K=K\log_23-E_K\) increases only on \(e=1\) steps
(`repunit_extremal_principle.md` §1), by \(\log_2 3-1\) each. Therefore each
deficit excursion is exactly

\[
\Delta D_{\text{run}}=(\log_2 3-1)\,L
=(\log_2 3-1)\bigl(v_2(3^{m}+d)-E_0-2\bigr).
\]

So **the entire extremal/deficit behaviour is governed by one quantity**: how
far the enemy valuation \(v_2(3^{m_K}+d_K)\) exceeds the accumulated
valuation \(E_K\). Equivalently, writing
\(d\equiv-3^{m}\pmod{2^{E_0+2}}\) and
\(s=(3^{m}+d)/2^{E_0+2}\),

\[
L=v_2(s).
\]

The run is long precisely when the residual \(s\) is highly \(2\)-divisible.

### Unification

- **Ghost branch \(d=7\)** (`repunit_baker_nonshadowing.md`): height of
  \(d\) is \(O(1)\), so Yu's \(p\)-adic logarithmic-form bound gives
  \(v_2(3^{m}+d)=O(\log n)\), hence \(L=O(\log n)\). Proved.
- **General enemy constants:** Theorem 3 shows the same statement
  (\(L=O(\log n)\)) is exactly what is needed, uniformly in the enemy
  coordinates the trajectory generates.

### The crux, in one line

\[
\textbf{Uniform run bound (open):}\quad
v_2\bigl(3^{m_K}+d_K\bigr)-E_K=o(n)
\quad\text{uniformly along every primitive tail.}
\]

This implies linear-window descent. The ghost-branch case is the bounded-height
instance; the open content is the high-height instances.

---

## 6. The obstruction is genuine roughness, not hidden structure

`scripts/explore_repunit_enemy_factorization.py` factors the enemy constants
\(d_K\) at primitive record-deficit states. Through odd \(n\le4001\):

- low reduced height (\(h_K/E_K\le0.9\)) almost always coincides with
  \(d_K\) being \(10^6\)-smooth (112 smooth vs 5 rough-prime, 0 composite);
- a real population of high-height-but-smooth constants exists (47 cases),
  so smoothness is **not** merely a proxy for low height;
- but the **largest** deficits are carried by high-height **rough primes**
  (e.g. \(n=997\), \(D\approx8.64\); \(n=2189\), \(D\approx7.17\)), which are
  maximally unstructured.

**Consequence.** A multi-term Baker bound obtained by *factoring* \(d_K\) into
small-height pieces cannot control the worst records: those \(d_K\) are large
primes. Any proof of the uniform run bound for the dangerous states must use
how \(d_K\) was *generated by the trajectory* (its payout/shell ancestry,
`repunit_extremal_principle.md` §4), not its prime factorization.

This redirects the surplus programme away from per-constant transcendence and
toward the collision/ancestry route for high-height states, while Baker remains
responsible only for the low-height (equivalently smooth) branches.

---

## 7. Empirical scale

Through odd \(n\le10001\) (215 primitive tails) the maximum deficit excursion
is \(D^\star\approx8.6436\) bits, attained at \(n=997\) and never exceeded; the
longest valuation-one run observed is \(16\). The ratio \(D^\star/\log_2 n\) is
non-increasing over the tested ranges, consistent with the \(O(\log n)\)
prediction of the uniform run bound. These are finite observations, not a
proof.

---

## 8. Verification

```bash
python scripts/verify_repunit_run_length.py --limit 201
python scripts/explore_repunit_enemy_factorization.py --limit 4001 --bound 1000000
```
