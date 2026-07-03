# The Mersenne Ancestry Tower

**Building on:** `latent_fuel_notes.md` (L1–L2, hierarchy conjecture),
`nlp2_alternation.md`, `no_local_potential.md`, `recharge_nogo.md`
**Status:** Theorems T1 and T2 are proved here; machine-checked in
`scripts/verify_tower.py`. T1 **resolves the hierarchy conjecture** of
`latent_fuel_notes.md` (in its e=2-uniform form) and T2 upgrades the
conditional NLP-$d$ of `nlp2_alternation.md` to an **unconditional**
theorem for every finite depth. Supersedes ledger row NLPD. Not a proof of
the Collatz conjecture.
**License:** CC-BY 4.0

---

## Abstract

For every depth $d\ge0$ there is an exact one-parameter family of odd
integers whose orbit descends the fuel hierarchy step by step into the
Mersenne spine:

$$
w_d(M)\;=\;\frac{2^{\,M+2d}-2^{\,2d+1}+3^{\,d}}{3^{\,d}},
\qquad M\equiv1\ \big(\mathrm{mod}\ 2\cdot3^{\,d-1}\big),
$$

with $f(w_d(M))=w_{d-1}(M)$ and hence $f^{\,d}(w_d(M))=2^M-1$, every step
an $e{=}2$ step dropping value by less than $\log_2\frac43$. The family
has an exact carry-free periodic binary normal form of period
$2\cdot3^{d-1}$ (via LTE: $v_3(2^{2\cdot3^{d-1}}-1)=d$), a frozen 2-adic
tail $\Lambda_d=1-2^{2d+1}3^{-d}$, and distinct towers separate at bit
$2\min(d,d')+1$ exactly. Levels $0,1,2$ recover the Mersennes, L1, and L2.
Consequence (Theorem T2): **no potential
$\log_2x+g(x\bmod2^m,\tau,\lambda_1,\dots,\lambda_d)$ is nonincreasing,
for any $m$, any finite set of tower detectors, and any $g$** — the
conditional NLP-$d$ is now unconditional. Each detector level costs the
obstruction one more $\log_2\frac43$; the burn liability remains
unbounded.

---

## 1. Theorem T1 (the tower)

Fix $d\ge1$, write $\mathrm{ord}_d=2\cdot3^{d-1}$, and let
$M=1+\mathrm{ord}_d\,s$ with $s\ge1$. Define $w_0(M)=2^M-1$ and $w_d(M)$
as above.

**T1(f) Domain.** $3^d$ divides the numerator iff
$M\equiv1\ (\mathrm{mod}\ \mathrm{ord}_d)$.

*Proof.* The numerator is $\equiv2^{2d}(2^M-2)\ (\mathrm{mod}\ 3^d)$, so
divisibility is $2^{M-1}\equiv1\ (\mathrm{mod}\ 3^d)$. Since $2$ is a
primitive root mod $9$ ($2^1,2^2,2^3=8,2^6\equiv1$; order $6=\varphi(9)$),
it is a primitive root mod $3^d$ for all $d\ge1$, so
$\mathrm{ord}_{3^d}(2)=\varphi(3^d)=2\cdot3^{d-1}$. $\;\blacksquare$

**T1(a) Basic form.** $w_d(M)=1+2^{\,2d+1}\dfrac{2^{M-1}-1}{3^{\,d}}$; it
is an odd integer $>1$ (for $s\ge1$) with $\tau(w_d(M))=1$ for $d\ge1$.

*Proof.* The identity is $2^{2d+1}(2^{M-1}-1)=2^{M+2d}-2^{2d+1}$. The
second summand is even, so $w_d$ is odd; $w_d+1=2\big(1+2^{2d}q\big)$ with
$2^{2d}q$ even for $d\ge1$, so $v_2(w_d+1)=1$. $\;\blacksquare$

**T1(b) Descent.** $3\,w_d(M)+1=4\,w_{d-1}(M)$; hence
$v_2(3w_d+1)=2$, $f(w_d(M))=w_{d-1}(M)$, and $f^{\,d}(w_d(M))=2^M-1$.

*Proof.* Clearing $3^{d-1}$: the two sides differ by
$3^{\,d}+3^{\,d-1}$ vs $4\cdot3^{\,d-1}$, which are equal. $w_{d-1}$ is
odd by T1(a) (or equals $2^M-1$ at $d=1$), so $v_2=2$ exactly. Iterate.
$\;\blacksquare$

**T1(c) Ratio.** $w_{d-1}(M)/w_d(M)=\tfrac34+\tfrac1{4w_d(M)}\in
(\tfrac34,1)$: every step of the chain drops $\log_2$-value by less than
$\log_2\tfrac43$.

**T1(d) Exact normal form.** By LTE,
$v_3\!\big(2^{\mathrm{ord}_d}-1\big)
=v_3(4-1)+v_3(3^{\,d-1})=d$, so
$B_d=(2^{\mathrm{ord}_d}-1)/3^{\,d}$ is an integer with
$0<B_d<2^{\mathrm{ord}_d}$. Then, base-$2^{\mathrm{ord}_d}$ repunit
expansion of $(2^{M-1}-1)/(2^{\mathrm{ord}_d}-1)$ gives

$$
w_d(1+\mathrm{ord}_d\,s)
=1+2^{\,2d+1}\cdot\underbrace{\big[\,\text{the }\mathrm{ord}_d\text{-bit
block of }B_d\,\big]^{\,s}}_{\text{repeated, no carries}},
$$

an **exactly periodic** binary word of period $2\cdot3^{d-1}$ — proving
the period formula conjectured in `latent_fuel_notes.md` ($2,6,18,\dots$).

**T1(e) 2-adic freeze and separation.** $w_d(M)\equiv
\Lambda_d:=1-2^{\,2d+1}3^{-d}\ (\mathrm{mod}\ 2^{\,M-1})$; and for
$d\ne d'$,

$$
v_2\big(\Lambda_d-\Lambda_{d'}\big)=2\min(d,d')+1 .
$$

*Proof.* $3^d\cdot\tfrac{2^{M-1}-1}{3^d}\equiv-1\
(\mathrm{mod}\ 2^{M-1})$ gives the freeze. For $d>d'$:
$\Lambda_d-\Lambda_{d'}=2^{\,2d'+1}3^{-d}\big(3^{\,d-d'}
-2^{\,2(d-d')}\big)$, and the bracket is odd. $\;\blacksquare$

Levels: $w_0=$ Mersennes; $w_1(M)=x'_M$ of `recharge_nogo.md` Lemma 2
($c_1=5$); $w_2(6k+1)=y_k$ of L2 ($c_2=23$); the numerator constants are
$c_d=2\cdot4^d-3^d$.

---

## 2. Detectors

For $d\ge1$ define the **level-$d$ detector**

$$
\lambda_d(x)=\max\{\,s\ge1:\ x\equiv w_d(1+\mathrm{ord}_d\,s)\
(\mathrm{mod}\ 2^{\,\beta_d(s)+1})\,\}\ \in\ \mathbb Z_{\ge1}\cup\{\bot\},
$$

where $\beta_d(s)$ is the bit length of the template (max over the empty
set is $\bot$). The definition of `nlp2_alternation.md` is the $d=1$ case
up to index shift ($\beta_1(s)+1=M+1=2\ell+4$).

**Lemma D (detector facts).**
1. *Self-reading:* $\lambda_d(w_d(1+\mathrm{ord}_d\,s))=s$ — unbounded
   along its own tower. (Match at $s$ is equality of two integers below
   the modulus; at $s'>s$ the modulus exceeds both operands, forcing
   equality of distinct integers.)
2. *Blindness on the spine and burn:* templates are $\equiv9\ (d{=}1)$ or
   $\equiv1\ (d{\ge}2)\ \bmod16$ (from $\Lambda_d$, and directly for the
   smallest template), while burn members $3^{\,j}2^{\,t}-1$ ($t\ge4$) and
   $2^M-1$ ($M\ge4$) are $\equiv15\bmod16$. Hence $\lambda_d=\bot$ on both,
   for every $d$.
3. *Cross-tower boundedness:* for $d\ne d'$, write $\nu=2\min(d,d')+1$
   (the separation bit of T1(e)). Then for all $M>\nu+1$ in the level-$d$
   progression, $\lambda_{d'}(w_d(M))\le\nu/\mathrm{ord}_{d'}$ — bounded
   uniformly in $M$.

   *Proof.* Suppose $x=w_d(M)$ matches the level-$d'$ template of index
   $s$, i.e. $x\equiv T_s\ (\mathrm{mod}\ 2^{\beta+1})$ with
   $T_s=w_{d'}(M')$, $M'=1+\mathrm{ord}_{d'}s$, and
   $\beta=\mathrm{bitlen}(T_s)\ge M'$ (since
   $T_s\ge2^{\,2d'+1}\cdot2^{\,M'-2}/3^{\,d'}\ge2^{\,M'-1}$). Assume
   toward a contradiction $M'-1\ge\nu+1$. Then the matching modulus
   refines $2^{\nu+1}$, and by T1(e) applied on both sides
   ($M-1\ge\nu+1$ by hypothesis, $M'-1\ge\nu+1$ by assumption):
   $x\equiv\Lambda_d$ and $T_s\equiv\Lambda_{d'}$ modulo $2^{\nu+1}$. The
   match then forces $\Lambda_d\equiv\Lambda_{d'}\ (\mathrm{mod}\
   2^{\nu+1})$, contradicting $v_2(\Lambda_d-\Lambda_{d'})=\nu$. Hence
   every match has $M'-1\le\nu$, i.e. $\mathrm{ord}_{d'}s\le\nu$. (For
   these small indices the template has not yet converged to
   $\Lambda_{d'}$, so whether a given small $s$ actually matches depends
   on the explicit template value; this affects which small values
   $\lambda_{d'}$ takes, never the bound.) $\;\blacksquare$

---

## 3. Theorem T2 (NLP-$d$, unconditional)

**Theorem T2.** Let $m\ge0$, let $S\subset\mathbb Z_{\ge1}$ be any finite
set of detector levels, and let $g$ be any real-valued function. Then

$$
P(x)=\log_2x+g\big(x\bmod2^m,\ \tau(x),\ (\lambda_i(x))_{i\in S}\big)
$$

is not nonincreasing along $f$ over odd $x>1$.

*Proof.* Suppose it is; write $\bot$ for the all-$\bot$ detector vector.

*(Burn.)* For $t\ge t_0=\max(m+1,5)$ the burn step
$3^{\,j}2^{\,t}-1\mapsto3^{\,j+1}2^{\,t-1}-1$ has both endpoints at
coordinates $(-1,\,t\ \text{resp.}\ t-1,\,\bot)$ (NLP1 Lemma 1 for
residue and $\tau$; Lemma D.2 for the detectors) and value ratio
$>\tfrac32$, so as in NLP1,

$$
g(-1,M,\bot)\ \ge\ g(-1,t_0,\bot)+(M-t_0)\log_2\tfrac32
\qquad\text{for all }M>t_0. \tag{1}
$$

*(Cap.)* Choose a level $L\notin S$, e.g. $L=\max(S)+1$, and let $M$ run
over the progression $M\equiv1\ (\mathrm{mod}\ 2\cdot3^{L-1})$, $M$ large.
Telescoping monotonicity down the chain
$w_L(M)\to w_{L-1}(M)\to\cdots\to w_0(M)=2^M-1$ ($L$ steps, each dropping
less than $\log_2\tfrac43$ by T1(c)) and using only the two endpoints:

$$
g(-1,M,\bot)\ \le\
g\big(\text{coords of }w_L(M)\big)+L\log_2\tfrac43 . \tag{2}
$$

The coordinate vector of $w_L(M)$ is confined to a **finite set**,
uniformly over the progression: the residue is frozen at
$\Lambda_L\bmod2^m$ for $M-1\ge m$ (T1(e)); $\tau=1$ (T1(a)); and every
$\lambda_i$ with $i\in S$ is bounded by Lemma D.3 (here $i\ne L$ is
guaranteed by the choice of $L$). Hence some single coordinate vector
recurs for infinitely many $M$ in the progression, and along that
subsequence the right side of (2) is one constant. This bounds
$g(-1,M,\bot)$ above along an infinite sequence of $M$, contradicting the
unbounded growth (1). $\;\blacksquare$

**Remarks.**
1. $S=\varnothing$ is NLP1; $S=\{1\}$ recovers NLP2 (with a cleaner proof:
   the subsequence device replaces the exact level-2 freeze computation).
2. The price list is now literal: detecting $d$ levels of latent fuel
   raises the adversary's cap by exactly $d\log_2\frac43$ against an
   unbounded liability. No finite tower of suffix-periodicity detectors —
   of any depths, in any combination, alongside any fixed-modulus window
   and the trailing-one count — supports a monotone one-step potential.
3. What remains genuinely open on this front: detectors reading the
   *high* end of $x$ (leading bits, fractional part of $\log_2x$),
   coordinates mixing low and high ends (e.g. the fuel fraction
   $\tau/\log_2x$), and multi-step potentials. T1's chains constrain these
   too — along the chain the fuel fraction is *visible* — so the no-go
   machinery genuinely stops here; that boundary is now sharp.

---

## 4. Structural remarks beyond the no-go

The tower is of independent interest to the repository's other programs:

* $B_d=(2^{2\cdot3^{d-1}}-1)/3^{\,d}$ is a Mersenne-over-$3$-power
  quotient whose integrality is an LTE statement — the same lemma
  driving the repunit rail analysis; the tower words are literally
  repunits in base $2^{\mathrm{ord}_d}$ with digit $B_d$.
* The tower exhibits, for each $d$, an infinite family whose first $d$
  odd steps are all $e=2$ (the slowest non-descending lane) terminating
  on the spine — exact witnesses for the corridor of `../density-cycles/corridor_rate.md`
  at maximal fuel.
* Density of tower members is zero (they are $O(1)$ per bit length per
  level), consistent with CYC3-style statements; nothing here bears on
  individual-trajectory claims.

---

## Appendix — Verification

`scripts/verify_tower.py` checks with exact integer arithmetic:
T1(f) both directions of the divisibility criterion; T1(a)–(c) oddness,
$\tau=1$, the identity $3w_d+1=4w_{d-1}$, the full $d$-step chain to
$2^M-1$, and both ratio bounds — for $d\le7$ over multiple $s$; T1(d) the
LTE valuation $v_3(2^{\mathrm{ord}_d}-1)=d$ for $d\le8$ and the exact
carry-free block normal form; T1(e) the 2-adic freeze and the exact
separation bit $2\min(d,d')+1$ for $d,d'\le5$; Lemma D.1–D.3 (self-reading,
mod-16 blindness on burn/spine, cross-tower boundedness on samples); and
the chain arithmetic of T2 for sampled $(m,S)$.

```bash
python3 scripts/verify_tower.py   # prints PASS for every claim above
```

## Proposed ledger rows

| ID | Claim | Status | Source | Verification |
|---|---|---|---|---|
| TWR1 | Exact ancestry tower $w_d(M)$, $f^{\,d}(w_d(M))=2^M-1$, period-$2\cdot3^{d-1}$ normal form, 2-adic separation | Proved here | `tower_theorem.md` | `scripts/verify_tower.py` |
| NLPD | No potential $\log_2x+g(x\bmod2^m,\tau,(\lambda_i)_{i\in S})$ is nonincreasing, any finite $S$ | Proved here (supersedes conditional NLPD) | `tower_theorem.md` | `scripts/verify_tower.py` |
| — | Hierarchy conjecture of `latent_fuel_notes.md` | RESOLVED by TWR1 (e=2-uniform form) | `tower_theorem.md` | — |
