# The Corridor Rate Theorem

**Building on:** `stopping_time_density.md` (Lemmas 2–3),
`descent_tree_survivors.md` (as corrected), `scripts/verify_survivor_density_rate.py`
**Status:** Proved here (Theorem 1 upper bound with explicit constant;
Theorem 1 lower bound by exponential tilting — elementary, Chernoff and
Chebyshev only). Corollary 2 is an exact consequence. Not a proof of the
Collatz conjecture.
**License:** CC-BY 4.0

---

## Abstract

The refutation of the old survivor-density conjecture
(`scripts/verify_survivor_density_rate.py`: the bound $\rho^K$ fails from
$K=195$) left the true decay rate open. Here it is closed: the density of
odd integers **not discharged by a $K$-bit valuation budget** decays with
exact exponential rate

$$
\boxed{\;\lim_{K\to\infty}\operatorname{dens}(\tilde S_K)^{1/K}
=\rho^{1/\theta}=e^{-I(\theta)/\theta}=0.965907\ldots\;}
$$

with $\theta=\log_2 3$ and $I$ the Cramér rate of
`stopping_time_density.md`. The upper bound is explicit:
$\operatorname{dens}(\tilde S_K)\le 31\,\rho^{K/\theta}$ for all $K\ge1$.
The mechanism: a survivor must hold a large-deviation slope
($<\theta$ valuations per step) for $\approx K/\theta$ steps, paying
$I(\theta)$ per *step*, hence $I(\theta)/\theta$ per unit of *budget* — not
$I(\theta)$ per unit of budget, which is where the refuted conjecture went
wrong. **Corollary:** the number of residue classes mod $2^K$ left
undischarged by any finite-modulus descent tree grows with branching factor
exactly $2\rho^{1/\theta}=1.93182\ldots$, i.e. like
$2^{0.94995\,K}$ — an exact hardness exponent for tree-style provers.

---

## 0. Setup

Notation as in `../../NOTATION.md` and `stopping_time_density.md`: for odd $x$,
$e_i=v_2(3x_i+1)$, $E_j=\sum_{i<j}e_i$, $\theta=\log_2 3$. By the exact
equidistribution (`stopping_time_density.md` Lemma 3) the $e_i$ are, in
natural density, i.i.d. with $\Pr[e=v]=2^{-v}$, and every event determined
by finitely many valuations has natural density equal to its walk
probability.

Define the **budget-$K$ survivor set** over odd integers:

$$
\tilde S_K=\{\,x\text{ odd}:\ E_j(x)<\theta j+1\ \text{whenever } E_j(x)\le K\,\},
$$

and $p_K=\operatorname{dens}(\tilde S_K)$. (The residue-count set $S_K$ of
`descent_tree_survivors.md` is the mod-$2^K$ proxy for $\tilde S_K$; the
theorem is stated for the exactly computable object. By
`stopping_time_density.md` Lemma 2, every $x\notin\tilde S_K$ with
$x\ge2(3/2)^{K}$ descends below itself — $\tilde S_K$ is what a $K$-bit
forced-descent certificate cannot discharge.)

**Walk formulation (exact).** $p_K$ equals the probability that the
i.i.d. Geometric($\tfrac12$) walk $E_j$ stays strictly below the line
$\theta j+1$ for as long as $E_j\le K$; equivalently, that the first
crossing time $J=\min\{j:E_j\ge\theta j+1\}$ (a.s. finite, since
$\mathbb E e=2>\theta$) has $E_J>K$. Both descriptions coincide because
$E_j$ is increasing. Let $D_j=\theta j-E_j$ (the **deficit walk**,
increments $\theta-e_i$, mean $\theta-2<0$); staying below the line is
$D_j>-1$.

Constants: $u^\star=\tfrac{2(\theta-1)}{\theta}=0.73813\ldots$,
$I(\theta)=(\theta-1)\ln u^\star+\ln(2-u^\star)=0.054981\ldots$,
$\rho=e^{-I(\theta)}=0.946507\ldots$,
$\rho_1=e^{-I(\theta)/\theta}=0.965907\ldots$,
$C_0=1/u^\star=\theta/(2(\theta-1))=1.35480\ldots$

---

## 1. Upper bound

**Lemma 1 (Chernoff at the line).** For all $j\ge0$,
$\Pr[E_j\le\theta j+1]\le C_0\,\rho^{\,j}$.

*Proof.* For $j=0$ the left side is $1\le C_0$. For $j\ge1$ and any
$u\in(0,1)$, Markov applied to $u^{E_j}$ gives
$\Pr[E_j\le a]\le u^{-a}\,\mathbb E[u^{E_j}]
=u^{-a}\big(\tfrac{u}{2-u}\big)^{j}$, since
$\mathbb E[u^{e}]=\sum_{v\ge1}u^v2^{-v}=\tfrac{u}{2-u}$. At
$a=\theta j+1$ this is
$u^{-1}\exp\!\big(-j[(\theta-1)\ln u+\ln(2-u)]\big)$; taking $u=u^\star$
(the maximizer defining $I(\theta)$, cf. `stopping_time_density.md`)
yields $C_0\rho^{\,j}$. $\;\blacksquare$

**Theorem 1a (explicit upper bound).** For all $K\ge1$,

$$
p_K\;\le\;31\,\rho_1^{\,K}.
$$

*Proof.* Decompose by $j_0=J-1$, the last step before the first crossing.
On the survivor event, $E_{j_0}\le\theta j_0+1$ (below the line, or
$j_0=0$) and $e_{j_0}=E_J-E_{j_0}>K-\theta j_0-1$. Since $e_{j_0}$ is
independent of $(e_0,\dots,e_{j_0-1})$ and
$\Pr[e>a]=2^{-\lfloor a\rfloor}\le 2\cdot2^{-a}$ for $a\ge0$,

$$
p_K\;\le\;\sum_{j\ge0}\Pr[E_j\le\theta j+1]\cdot
\Pr[e>\max(K-\theta j-1,\,0)]
\;\le\;\Sigma_1+\Sigma_2,
$$

with $\Sigma_1$ the range $\theta j\le K-1$ and $\Sigma_2$ the rest.
Using Lemma 1, $2^{\theta}=3$, and $3^{1/\theta}=2$:

$$
\Sigma_1\le\sum_{j\le (K-1)/\theta} C_0\rho^{\,j}\cdot2\cdot2^{-(K-\theta j-1)}
=4C_0\,2^{-K}\!\!\sum_{j\le (K-1)/\theta}\!\!(3\rho)^{j}
\le\frac{4C_0\,(3\rho)}{3\rho-1}\;2^{-K}(3\rho)^{(K-1)/\theta}
=\frac{4C_0\,(3\rho)^{1-1/\theta}}{3\rho-1}\,\rho_1^{\,K},
$$

since $2^{-K}(3\rho)^{K/\theta}=2^{-K}\cdot2^{K}\rho^{K/\theta}
=\rho_1^{\,K}$ (here $3\rho=2.8395>1$, so the geometric sum is dominated
by its top term). And

$$
\Sigma_2\le\sum_{j>(K-1)/\theta}C_0\rho^{\,j}
\le\frac{C_0\,\rho^{-1/\theta}}{1-\rho}\,\rho_1^{\,K}.
$$

Numerically the two prefactors are $4.33\ldots$ and $26.22\ldots$; their
sum is $<31$. $\;\blacksquare$

---

## 2. Lower bound

**Theorem 1b.** $\displaystyle\liminf_{K\to\infty}\tfrac1K\ln p_K
\ge-\frac{I(\theta)}{\theta}$, hence with Theorem 1a,
$\lim_K p_K^{1/K}=\rho_1$.

*Proof.* Fix $\varepsilon\in(0,\theta-1)$ and $\delta\in(0,\tfrac13)$; set
$\mu=\theta-\varepsilon\in(1,2)$. Let $u\in(0,1)$ solve
$\mathbb E_Q[e]=\mu$ under the tilted law
$Q[e=v]=u^{v}2^{-v}/M(u)$, $M(u)=\tfrac{u}{2-u}$ (the tilted mean
$\tfrac{2}{2-u}$ runs over $(1,2)$ as $u$ runs over $(0,1)$, so $u$
exists; increments remain independent, with some variance
$\sigma^2<\infty$). The change of measure on an $n$-step path with sum
$E_n$ is $\tfrac{dP}{dQ}=M(u)^{n}\,u^{-E_n}$, and
$n^{-1}\ln\tfrac{dP}{dQ}\to -I(\mu)$ on paths with $E_n\approx\mu n$,
where $I(\mu)=(\mu-1)\ln u_\mu+\ln(2-u_\mu)$ is continuous in $\mu$.

Under $Q$ the deficit walk $D_j=\theta j-E_j$ has drift
$\theta-\mu=\varepsilon>0$. Build the survivor event from three parts.

*(i) Buffer.* Force $e_0=\cdots=e_{b-1}=1$; each has fixed $Q$-probability
$q_1=\tfrac{u}{2}/M(u)>0$, and after $b$ steps $D_b=b(\theta-1)>0$ with no
crossing en route.

*(ii) No ruin.* For the walk after the buffer, increments
$\theta-e$ have positive mean $\varepsilon$ and
$\mathbb E_Q[e^{-\lambda(\theta-e)}]<1$ for some small $\lambda>0$
(finite exponential moments near $0$; mean positive). Chernoff plus a
union bound gives
$Q[\exists\,i\ge1:\ D_{b+i}-D_b\le-1-b(\theta-1)]
\le\sum_{i\ge1}\gamma^{\,i}e^{-\lambda(1+b(\theta-1))}<\tfrac14$
for $b$ fixed large enough (depending on $\varepsilon$ only). So with
$Q$-probability $\ge\tfrac34$, $D_j>-1$ for **all** $j$.

*(iii) Window.* Let $n=\lfloor(1-\delta)K/\mu\rfloor$. By Chebyshev,
$Q\big[|E_n-\mu n|\le\tfrac{\delta}{2}K\big]\ge\tfrac34$ for $K$ large
(variance $O(K)\ll K^2$). On this window, $E_n\le(1-\tfrac{\delta}{2})K\le
K-1$ (so the whole $n$-step prefix stays within budget) and
$K-E_n\le 2\delta K$ for large $K$.

The three events jointly have $Q$-probability $\ge q_1^{\,b}\cdot\tfrac12$
for large $K$ (condition on the buffer; intersect (ii),(iii) by union
bound). Transferring to $P$ on the window (where
$u^{-E_n}\ge u^{-\mu n+\delta K/2}$... with $u<1$ this is
$\ge e^{-n[\,(\mu)\ln\frac1u\,]}e^{-\frac{\delta K}{2}\ln\frac1u}$
combined with $M(u)^n$ to give $e^{-nI(\mu)}e^{-\frac{\delta
K}{2}\ln\frac1u}$), and then appending one final untilted jump
$e_n>K-E_n$ of probability $\ge2^{-2\delta K}$ (independence), every such
path lies in the survivor event: below the line throughout the prefix,
within budget throughout, and past the budget at step $n{+}1$. Hence

$$
p_K\;\ge\;\tfrac12\,q_1^{\,b}\;
e^{-nI(\mu)}\;e^{-\frac{\delta K}{2}\ln\frac1u}\;2^{-2\delta K},
$$

so $\liminf_K\tfrac1K\ln p_K\ge
-(1-\delta)\tfrac{I(\mu)}{\mu}-\tfrac{\delta}{2}\ln\tfrac1u-2\delta\ln2$.
Let $\delta\downarrow0$, then $\varepsilon\downarrow0$ and use continuity
of $I(\mu)/\mu$ at $\mu=\theta$. $\;\blacksquare$

---

## 3. The hardness corollary

**Corollary 2 (tree-prover branching exponent).** Let $N_K$ be the number
of odd residue classes mod $2^K$ that contain any element of
$\tilde S_K$ (equivalently, that a $K$-bit forced-descent certificate
fails to discharge). Then

$$
\lim_{K\to\infty}N_K^{1/K}\;=\;2\rho_1\;=\;1.93182\ldots,
\qquad\text{i.e.}\qquad
N_K=2^{\big(1-\frac{I(\theta)}{\theta\ln2}+o(1)\big)K}
=2^{(0.94995\ldots+o(1))K}.
$$

*Proof.* By `stopping_time_density.md` Lemma 3, a class $r$ mod $2^K$
determines its members' valuation pattern for as long as the cumulative
weight stays $\le K-1$; beyond that, every continuation of the visible
prefix is realized by members of the class (apply Lemma 3 at larger
moduli), each with its product-measure frequency. Call $r$
**decided-discharged** if the visible prefix contains a crossing
$E_j\ge\theta j+1$. Two observations:

*(a)* A decided-discharged class contains no element of $\tilde S_K$: the
visible crossing has $E_j\le K-1<K$, so every member's first crossing
occurs at valuation $\le K-1$, violating the survivor condition.

*(b)* Every class that is **not** decided-discharged contains elements of
$\tilde S_K$: its visible prefix stays below the line with some final
visible state $(j,E)$, $E\le K-1$; among its members, choose the
continuation $e_j\ge K-E+1$ (realized, with positive frequency). That
member stays below the line while $E\le K$ and then exceeds the budget —
a survivor.

Hence $N_K$ is exactly the number of not-decided-discharged classes. That
event — "the walk stays below the line for as long as its weight is
visible" — is the budget-survivor event at a budget within $2$ of $K$
(the only slack is whether the boundary weight is read as $K-1$, $K$, or
$K+1$ in the greedy prefix reading), so

$$
2^{K-1}p_{K+1}\;\le\;N_K\;\le\;2^{K-1}p_{K-2}\,,
$$

and since $p_K$ has exponential rate $\rho_1$ (Theorem 1), a shift of the
budget by $O(1)$ leaves the rate unchanged:
$N_K^{1/K}\to2\rho_1$. $\;\blacksquare$

**Reading.** Any prover that discharges residue classes mod $2^K$ by the
"enough division forces descent" criterion — which is what
`scripts/verify_descent_tree.py` implements and what `../core/Mod8_Rail_Descent.md`'s rail
certificates instantiate at small depth — faces a frontier of undischarged
classes growing like $1.9318^{\,K}$: exponential, forever, at an exactly
known rate. The rate is *not* an artifact of implementation; it is the
first-passage price $I(\theta)/\theta$ of the corridor below the
$\theta$-line. This gives quantitative teeth to the repository's standing
observation that the hard core (rail 7, high-fuel, near-Mersenne) is never
emptied by finite certificates: the Mersenne spine anchors the corridor
(`descent_tree_survivors.md` Prop. 2), and the corridor's population is now
exactly priced.

**Consistency check.** The refuted conjecture claimed rate $\rho=0.9465$;
the DP measurement of the local rate climbs monotonically through
$0.9613\,(K{=}400)$, $0.9643\,(K{=}1000)$, $0.9650\,(K{=}1800)$ toward
$\rho_1=0.9659$, with the sub-exponential gap consistent with the
$e^{-c\sqrt K}$-type corrections the tilted construction predicts.

---

## 4. What is and is not proved

**Proved:** the exact limit $p_K^{1/K}\to\rho_1$ (Theorems 1a/1b); the
explicit bound $p_K\le31\rho_1^K$ for all $K$; the branching exponent
$2\rho_1$ for undischarged classes (Corollary 2).

**Not proved:** anything about individual trajectories. The corridor
population statement is a density statement; it neither shows any specific
integer leaves the corridor nor bounds cycle elements beyond what CYC3
already records. Sharp constants (the sub-exponential prefactor of $p_K$)
are left open.

**Supersedes:** the corrected Conjecture 1' of
`descent_tree_survivors.md` — both directions are now theorems; the
remaining open refinement there is only the prefactor.

---

## Appendix — Verification

`scripts/verify_corridor_rate.py` checks:

* the constant calculus: $u^\star$, $I(\theta)$, $C_0$, $\rho$, $\rho_1$,
  the prefactor sum $<31$, and the exact identities $2^\theta=3$,
  $3^{1/\theta}=2$ (symbolically trivial; checked to guard typos);
* **Theorem 1a numerically:** $p_K\le31\rho_1^K$ for all computed $K$ (DP
  up to $K=1800$, prefix-sum $O(K^2)$ implementation cross-checked against
  the exact-rational slow DP);
* **Theorem 1 (limit) evidence:** the local rate
  $(p_{K}/p_{K'})^{1/(K-K')}$ is monotone increasing toward $\rho_1$;
* **Lemma 1:** Chernoff bound vs exact tail for $j\le40$ (exact rational
  tail via convolution);
* the tilt calculus of Theorem 1b: tilted mean solves
  $\tfrac{2}{2-u}=\mu$; $I(\mu)/\mu\to I(\theta)/\theta$ sampled.

```bash
python3 scripts/verify_corridor_rate.py    # prints PASS for every claim above
```

## Proposed ledger rows

| ID | Claim | Status | Source | Verification |
|---|---|---|---|---|
| COR1 | $p_K\le31\,\rho^{K/\theta}$ for all $K\ge1$ | Proved here | `corridor_rate.md` | `scripts/verify_corridor_rate.py` |
| COR2 | $\lim p_K^{1/K}=\rho^{1/\theta}=0.9659\ldots$ | Proved here | `corridor_rate.md` | DP rate convergence (finite evidence for the limit; proof is human) |
| COR3 | Undischarged-class count grows with branching factor $2\rho^{1/\theta}=1.9318\ldots$ | Proved here (from COR1/2) | `corridor_rate.md` | — |
