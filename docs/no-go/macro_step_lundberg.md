# Macro-Step Lundberg Programme

**Status:** Exact macro-step identities (MAC1–MAC3), a homogeneous-multiplier
martingale (LUN1A–LUN2), and ancestry capacity (ANC1). The claimed
identification of the multiplier with actual orbit growth is withdrawn.
The counting route to SD1 is unsupported by these results. Its finite
escape-set diagnostics remain evidence, with the qualifications in §6.
This is not a proof of the Collatz conjecture.

**Correction (2026-10-05).** The macro-step starting at 9 follows
$9\to7\to11\to17$. Its actual ratio is $17/9$, whereas its homogeneous
multiplier is $27/16$. Earlier versions omitted the affine terms and used
the multiplier martingale to claim an actual-orbit escape bound. This note
now separates those objects and revises the dependent DISC1/WALSH1 claims.
The example refutes the identification, not the proposed density bound itself.

**Building on:** [fuse burn](../fuse/fuse_burn_attack.md),
[comparison dynamics](avenue_a_comparison_dynamics.md),
[local potential obstruction](no_local_potential.md), and the
[attack programme](../repunit/next_generation_attack_program.md).

**License:** CC-BY 4.0

---

## Abstract

We decompose the accelerated odd Collatz map into macro-steps between
fuel-exhausted states. Each macro-step is an exact affine map $x\mapsto Ax+b$.
Its homogeneous multiplier $A$ has mean one under Haar measure conditioned
on a fuel-exhausted start, and $\log_2 A$ has Lundberg exponent $\ln 2$.
Ville's inequality bounds the maximum of products of these multipliers.
It does not, without additional affine control, bound the maximum of an
actual positive-integer orbit. We retain the elementary ancestry capacity
lemma and finite escape-set diagnostics, with their probability spaces stated
separately.

## 0. Notation and probability spaces

As in [NOTATION.md](../../NOTATION.md),
$f(x)=(3x+1)/2^{v_2(3x+1)}$ for positive odd $x$ (including the fixed point 1),
$\tau(x)=v_2(x+1)$, and $\alpha=\log_2 3-1$.
Write $\mathcal B=\{x\in\mathbb Z_2:x\equiv1\pmod4\}$.

Statements about real size and logarithms of values concern positive
integers. MAC2 and LUN1A–LUN2 use normalized Haar measure on $\mathcal B$,
and their real-valued random variables depend on finite valuation words.
Haar-null exceptional states with infinite valuations are excluded.
There is no ordered real size for a general $2$-adic point. The finite
integer-domain escape frequencies of §6 are not this Haar probability.

---

## 1. Macro-step decomposition

### MAC1 (Fuel partition). — **proved**

Every positive odd $x$ is in exactly one of two classes:

- **Class A (fuel-burning):** $\tau(x)=L\ge2$. Write $x=2^L m-1$ with
  $m$ odd. Then $v_2(3x+1)=1$, $f(x)=3\cdot2^{L-1}m-1$, and
  $\tau(f(x))=L-1$. The homogeneous log-multiplier is $\alpha$; the
  actual log-ratio is $\alpha+\log_2(1+1/(3x))$.
- **Class B (fuel-exhausted):** $\tau(x)=1$, equivalently $x\equiv1\pmod4$.
  Then $v_2(3x+1)\ge2$.

A macro-step starts at Class B, takes one payout step with valuation $v$
and new fuel $K=\tau(f(x))$, then takes exactly $K-1$ Class A steps,
returning to Class B. The fixed point 1 has $v=2,K=1$.

*Proof.* The Class A identity is the suffix-burn identity. For Class B,
$3(4k+1)+1=4(3k+1)$. Iterating the fuel decrement gives the return.
$\blacksquare$

Here "recharge" means the Class B event that creates new fuel; "burn"
means a Class A step that consumes it.

---

## 2. Independence theorem

### MAC2 (Independence of payout and new fuel). — **proved**

For Haar-uniform $x$ conditioned on $\mathcal B$, $v=v_2(3x+1)$ and
$K=\tau(f(x))$ are independent, with

$$\Pr(v=j)=2^{-(j-1)}\quad(j\ge2),\qquad
\Pr(K=i)=2^{-i}\quad(i\ge1).$$

Thus $\mathbb E[v]=3$ and $\mathbb E[K]=2$.

*Proof.* Write $x=4k+1$, $u=v-2=v_2(3k+1)$, and $3k+1=2^u m$.
Conditional on $u$, division by $2^u$ after the affine bijection gives
normalized Haar measure on odd $m$. Hence $K=v_2(m+1)$ is geometric
and independent of $u$. $\blacksquare$

---

## 3. Exact affine endpoint and multiplier drift

### MAC3 (Affine endpoint and homogeneous drift). — **proved**

For a macro-step starting at a positive Class B integer $x$, put

$$A=\frac{3^K}{2^{v+K-1}},\qquad
b=\frac{3^{K-1}(1+2^v)-2^{v+K-1}}{2^{v+K-1}}.$$

Then

$$x_{\rm out}=Ax+b,\qquad
\Delta:=\log_2 A=K\alpha+1-v.$$

The additive term is positive: $b=(3/2)^{K-1}(1+2^{-v})-1>0$.
Consequently the actual log-ratio is, writing $x_i=f^i(x)$,

$$\log_2\frac{x_{\rm out}}x
=\Delta+\log_2\left(1+\frac{b}{Ax}\right)
=\Delta+\sum_{i=0}^{K-1}\log_2\left(1+\frac1{3x_i}\right).$$

*Proof.* Set $y=(3x+1)/2^v$. The $K-1$ burn steps give
$x_{\rm out}=(3/2)^{K-1}(y+1)-1$; expansion gives the endpoint formula.
Multiplication of the exact odd-step ratios gives the logarithmic identity.
$\blacksquare$

Only the homogeneous drift has the expectation computed from MAC2:

$$\mathbb E[\Delta]=2\alpha+1-3=2\log_2 3-4\approx-0.830075.$$

**Counterexample to the former identity.** At $x=9$,
$v=2,K=3,A=27/16,b=29/16$, and $x_{\rm out}=17$.
Thus $x_{\rm out}/x=17/9\ne27/16=A$. The affine correction cannot be
discarded in an exact statement.

---

## 4. Lundberg exponent and multiplier escape bound

### LUN1A (Mean-one homogeneous multiplier). — **proved**

Under the MAC2 law, $\mathbb E[A]=1$.

*Proof.* Independence gives
$$\mathbb E[(3/2)^K]=\sum_{i\ge1}(3/4)^i=3,\qquad
\mathbb E[2^{1-v}]=4\sum_{j\ge2}4^{-j}=\tfrac13.$$
Their product is one. $\blacksquare$

This calculation concerns $A$, not $x_{\rm out}/x=A+b/x$.
It does not make actual Collatz values a martingale. The Jensen gap
$\log_2\mathbb E[A]-\mathbb E[\log_2 A]\approx0.83$ bits is a statement
about the multiplier law.

### LUN1 (Closed-form Lundberg exponent). — **proved**

The moment generating function of $\Delta=\log_2 A$ is

$$M(\theta)=\frac{e^{\theta(\alpha-1)}}
{(2-e^{\theta\alpha})(2-e^{-\theta})},
\qquad -\ln2<\theta<\frac{\ln2}{\alpha}.$$

Both restrictions are required for the two geometric series to converge.
The unique positive root of $M(\theta)=1$ is $\theta^*=\ln2$.

*Proof.* Evaluate the independent geometric sums from MAC2.
LUN1A gives $M(\ln2)=\mathbb E[A]=1$; explicitly it is
$(3/4)/((1/2)(3/2))=1$.
Strict convexity of $\log M$, $M(0)=1$, and $M'(0)<0$ give uniqueness.
$\blacksquare$

### LUN2 (Haar multiplier bound via Ville). — **proved**

Start with normalized Haar measure on $\mathcal B$. Let
$S_N=\sum_{i=1}^N\Delta_i$ over consecutive macro-steps.
Then $W_N=2^{S_N}=\prod_{i=1}^N A_i$ is a nonnegative martingale and

$$\Pr_{\mathcal B}\left(\sup_{N\ge0}S_N\ge a\right)\le2^{-a},
\qquad a>0.$$

*Proof.* Let $\mu_{\rm odd}$ and $\mu_{\mathcal B}$ denote normalized
Haar measure on odd $2$-adics and on $\mathcal B$, respectively. Continue
the MAC2 decomposition by writing the post-payout state as $m=2^Kq-1$.
Conditional on $v=j$, $m$ has law $\mu_{\rm odd}$. Conditioning further
on $K=i$, the affine bijection $m\mapsto(m+1)/2^i$ sends the normalized
restriction to that valuation class to $\mu_{\rm odd}$. Thus, for every
measurable set $E$ of odd $2$-adics and $j\ge2$, $i\ge1$,

$$\Pr_{\mathcal B}(v=j,K=i,q\in E)
=2^{-(j-1)}2^{-i}\mu_{\rm odd}(E).$$

In particular, $q$ is independent of the pair $(v,K)$, not just
Haar-uniform marginally. The endpoint after burning is
$R(x)=2\cdot3^{K-1}q-1$. For each fixed $i$, multiplication by
$3^{i-1}$ preserves $\mu_{\rm odd}$, and $q\mapsto2q-1$ sends
$\mu_{\rm odd}$ to $\mu_{\mathcal B}$. Therefore, for every measurable
$C\subseteq\mathcal B$,

$$\Pr_{\mathcal B}(v=j,K=i,R(x)\in C)
=2^{-(j-1)}2^{-i}\mu_{\mathcal B}(C).$$

Although the return formula depends on $K$, its conditional law does not:
the return state is Haar on $\mathcal B$ and independent of $(v,K)$.
Iterating this identity shows that after each macro-step the return state
is Haar and independent of the entire preceding pair history. Hence the
macro-step pairs are independent and identically distributed. With
$\mathcal F_N=\sigma((v_i,K_i):1\le i\le N)$, LUN1A gives
$\mathbb E[A_{N+1}\mid\mathcal F_N]=1$, so $W_N$ is a nonnegative
martingale with respect to $(\mathcal F_N)$, with $W_0=1$. Ville's
inequality gives the displayed bound. $\blacksquare$

**Scope.** This is a bound on multiplier products starting in Class B.
An initial Class A burn is not included in that probability space.
Actual endpoint ratios contain the positive affine corrections of MAC3;
$W_N$ is not the orbit ratio.

The distinction changes the escape event. The full orbit
$9\to7\to11\to17\to13\to5\to1$ has peak ratio $17/9>7/4$,
whereas the maximum cumulative homogeneous multiplier is $27/16<7/4$.
Continuing at the fixed point cannot increase either maximum.
Thus the two threshold events are not equivalent even for a Class B start.

Within a macro-step a positive Class B step decreases the value unless
$x=1$, and the subsequent burn steps increase it. The maximum is therefore
at one of its two endpoints. This observation does not remove the affine
terms. No actual-orbit density bound, or new derivation of a
Terras/Everett theorem, follows here from LUN2 alone.

**Novelty:** unchecked for this packaging of the multiplier law. The
earlier claimed value-martingale identity is withdrawn, not a literature
priority claim.

---

## 5. Ancestry capacity

### ANC1 (One preimage per bit-length). — **proved**

Let $z$ be odd with $3 \nmid z$. The set of odd preimages of $z$ under $f$ is
$\{x_v = (2^v z - 1)/3 : v \geq 1,\ v \equiv v_0(z) \pmod{2}\}$, where
$v_0(z)$ is the unique parity with $(-1)^{v_0} z \equiv 1 \pmod{3}$.
Consecutive preimages satisfy

$$\frac{x_{v+2}}{x_v} = 4 + \frac{3}{2^v z - 1} > 4,$$

so their bit-lengths differ by at least $2$. In particular:

> For every $n \geq 1$, there is **at most one** odd $x$ with
> $\operatorname{bitlen}(x) = n$ and $f(x) = z$.

*Proof.* Integrality of $x_v$ requires $2^v z \equiv 1 \pmod{3}$, a parity
condition on $v$; oddness of $x_v$ is automatic since $2^v z - 1$ is odd.
The ratio identity is algebra. If $y \geq 4x \geq 4$ then
$\operatorname{bitlen}(y) \geq \operatorname{bitlen}(x) + 2$. $\blacksquare$

**Corollary (reverse-tree capacity).** For every odd $z$ with $3 \nmid z$ and
every $n$, the number of odd $x$ with $\operatorname{bitlen}(x) \leq n$ and
$f(x) = z$ is at most $\lceil n/2 \rceil$: the admissible $v$ form one parity
class, and consecutive admissible preimages are separated by at least two
bits.

> **Why this may be the one part of this note with downstream use.**
> `obstruction_map.md` §4 item 3 (primitive ancestry-amortization) needs to
> charge present deficit against something the local data does not contain,
> and §4's closing remark identifies the difficulty as needing a *non-local*
> resource. A capacity bound on the reverse tree is at least the right type of
> object for an amortization argument: it caps how much ancestry can be
> spent per bit of height. Whether the cap is tight enough to charge against
> the repunit deficit is untested — see `obstruction_map.md` §4.3.
>
> Novelty is doubtful: the preimage family
> $x_v = (2^v z - 1)/3$ and its parity condition are standard, and
> reverse-tree growth rates are studied (Applegate–Lagarias). The
> bit-length separation is elementary. Treat ANC1 as a convenient packaging,
> not a new result, unless a literature check says otherwise.

---

## 6. Finite escape-set diagnostics and the unsupported counting route

Earlier versions used LUN2 to bound actual escape frequencies and then
declared DISC1/WALSH1 settled. That transfer is not justified. The
normalization errors identified in the earlier tables remain errors, but
their correction does not supply the missing probability argument.

Define the actual positive-integer event

$$E_a^+=\{x\in\mathbb Z_{>0}\text{ odd}:\exists j\ge0,\ f^j(x)\ge2^a x\}.$$

For the numerical tables use $D_B=\{2j+1:0\le j<2^B\}$ and the bounded event
$E_{a,B,T}$ where the threshold must be reached within $T$ odd steps.
Write $\mu_D=|E_{a,B,T}|/2^B$. In the tables $B=14,T=4000$.
This is a finite uniform frequency. LUN2 does not prove $\mu_D\le2^{-a}$
or give a Haar measure for $E_a^+$.

### 6.1 The counting obstruction

Cylinder depth alone does not establish equidistribution across a coarser
modulus. Any revived counting argument must state its domain, the actual
escape event, and a proved estimate connecting them. Multiplier-only
large deviations do not provide that connection.

### 6.2 FUEL1 (Deterministic integer escape from fuel). — **proved**

Let $t_a=\lceil a/\alpha\rceil+1$. Every positive odd $x$ with
$\tau(x)\ge t_a$ belongs to $E_a^+$, and reaches the threshold within
$t_a-1$ steps.

*Proof.* The first $t_a-1$ steps are Class A. Each has ratio
$3/2+1/(2x_i)>3/2$, so their product exceeds
$(3/2)^{t_a-1}\ge2^a$. $\blacksquare$

For $B\ge t_a-1$ and $T\ge t_a-1$, $E_{a,B,T}$ therefore contains
the entire class $x\equiv-1\pmod{2^{t_a}}$ within $D_B$.
Its density inside that class is one, and its relative density compared
with the whole sample is $1/\mu_D$. The further lower bound $2^a$
previously asserted for this ratio is not proved here.

**DISC1 status.** The finite sample is not equidistributed modulo
$2^{a+2}$ (see §6.4). FUEL1 alone does not refute an asymptotic claim at
that specific modulus: $t_a$ can exceed $a+2$, and fine-class containment
does not determine all coarse-class densities. A universal
equidistribution claim needs a precise formulation and separate analysis.

### 6.3 WALSH1: finite identities and conditional consequences

Normalize the Walsh transform in $j=(x-1)/2$ coordinates as in
[scripts/verify_walsh1.py](../../scripts/verify_walsh1.py), with indicator
$A(j)=1_{E_{a,B,T}}(2j+1)$. Then $\widehat A(0)=\mu_D$ and

$$|\widehat A(\eta)|\le\mu_D.$$

**Literal bound.** A bound $|\widehat A(\eta)|\le C2^{-a}$ with $C=1$
would follow from $\mu_D\le2^{-a}$, but this premise is not supplied by
LUN2. The earlier unconditional WALSH1 claim is withdrawn.

**Cylinder lower bound.** Under the FUEL1 conditions on $B,T$, the forced
class fixes $t_a-1$ low bits of $j$. Let $V$ be its
$2^{t_a-1}$ supported Walsh frequencies. Expanding the cylinder indicator
in characters and using containment gives
$\sum_{\eta\in V}\chi_\eta(c)\widehat A(\eta)=1$.
Subtracting the zero-frequency term and applying the triangle inequality
yields

$$\max_{\eta\ne0}|\widehat A(\eta)|
\ge\frac{1-\mu_D}{2^{t_a-1}-1}.$$

The $t_a-1$ exponent accounts for the odd domain: its parity bit is already
fixed. This finite inequality is checked using integer Walsh coefficients
in the script.

**White-noise status.** For fixed $a$, the lower bound obstructs
$\max_{\eta\ne0}|\widehat A(\eta)|=o(\mu_D)$ along any growing-domain
sequence with $\mu_D$ bounded away from one. That density condition is
not proved here. The unconditional asymptotic refutation is therefore
replaced by this conditional statement and the finite observations below.

### 6.4 Why the original computation looked supportive

Reproduced by `scripts/verify_walsh1.py` on the domain
$D = \{2j+1 : j < 2^{14}\}$ with a $4000$-step cap:

| $a$ | $\mu_D$ | $\mu/2^{-a}$ | $\max_{\eta\neq0}\|\hat A\|$ | ratio to $2^{-a}$ | ratio to $\mu$ | random baseline | observed / random |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | 0.4323 | 0.865 | 0.2210 | 0.442 | 0.511 | 0.01705 | 12.96 |
| 2 | 0.2065 | 0.826 | 0.1022 | 0.409 | 0.495 | 0.01393 | 7.34 |
| 3 | 0.1045 | 0.836 | 0.0529 | 0.423 | 0.506 | 0.01053 | 5.02 |
| 4 | 0.0507 | 0.812 | 0.0279 | 0.446 | 0.550 | 0.00755 | 3.69 |
| 5 | 0.0231 | 0.740 | 0.0130 | 0.416 | 0.562 | 0.00517 | 2.51 |

Three corrections to the earlier reading:

1. **The old §6.2 table is superseded.** It used a different, unstated domain
   ($b = a+12$ bit integers), so its frequencies cannot be compared with
   the old §6.3 table without matching domains and step caps.
   Its $a = 5$ row was also internally impossible: a *maximum* over residue classes cannot fall below the mean,
   which under its own normalization was $\mu/2^{-a} - 1 = -0.251$, yet it
   reported $-0.430$.

2. **"Max excess" was normalized against $2^{-a}$, not $\mu_D$.** Since
   $\mu_D$ is only $0.74$–$0.87$ of $2^{-a}$ and that ratio *falls* with
   $a$, a uniformly deficient set reads as increasingly equidistributed. The
   apparent improvement, and the sign change at $a = 4$, were entirely this
   artifact. Renormalized against $\mu_D$, the residue distribution mod
   $2^{a+2}$ is grossly non-uniform and gets worse with $a$:

   | $a$ | richest class | its relative density | empty classes |
   | :-- | :-- | :-- | :-- |
   | 1 | $7 = 2^3-1$ | 2.31 | 0 / 4 |
   | 3 | $31 = 2^5-1$ | 4.82 | 0 / 16 |
   | 5 | $127 = 2^7-1$ | 11.99 | 15 / 64 |

   The richest class is $2^{a+2}-1$ at every tested threshold — the maximal trailing-one
   class, consistent with the fuel mechanism — and at $a = 5$ nearly a quarter of the odd residue classes have no
   observed escape within this finite domain and step cap.

3. **The flat ratio was the tell.** $\max|\hat A|$ tracks $\mu_D$ at a
   ratio of $0.50$–$0.56$ that does not decay with $a$ (and if anything
   rises). White noise would scale like $\sqrt{\mu/N}$, not like $\mu$.
   Reading the ratio against $2^{-a}$ instead produced the flat $\approx 0.44$
   that was mistaken for a clean bound; it is flat because the coefficients
   are proportional to the measure, which is the signature of structure.
   Consistently, the argmax sits at $\eta \in \{1, 3, 4\}$ — the *lowest*
   frequencies, i.e. the bottom bits of $x$, i.e. $\tau$.

---

## 7. Scope of the results

The retained results give exact affine endpoints, a mean-one homogeneous
multiplier and its maximal inequality on the Class B Haar space, elementary
reverse-tree capacity, deterministic high-fuel escape, and finite
Walsh/residue diagnostics. They do not prove a bound for the actual
integer escape set from the multiplier bound, establish SD1, or prove the
Collatz conjecture. The live storage-dominance programme is unchanged.

## 8. What remains for the counting route

The actual and homogeneous escape events require separate treatment.
High trailing-one fuel forces actual growth and produces explicit finite
residue structure, but the claimed universal equidistribution and spectral
closures used an unproved actual-growth density bound.
The corresponding entry in [obstruction_map.md](obstruction_map.md) is
therefore a limitation of this argument, not a universal impossibility
theorem for counting methods.

A fuel-level decomposition would still need an actual-orbit estimate for
the residual event and a valid recursion or stopping rule. LUN2 does not
already solve that residual problem.

## 9. Verification

[scripts/verify_macro_step_lundberg.py](../../scripts/verify_macro_step_lundberg.py)
compares directly iterated macro-step endpoints with MAC3 in exact integer
arithmetic, checks the $x=9$ counterexample and distinct threshold events,
checks the multiplier moments numerically, verifies ANC1 on its stated
finite domain, and prints a separately labelled finite orbit probe.

[scripts/verify_walsh1.py](../../scripts/verify_walsh1.py) reproduces the
finite tables, checks FUEL1 on the sampled residue classes, and verifies
the finite Walsh lower bound with integer coefficients. Neither script
promotes finite observations to universal actual-orbit probability bounds.

## 10. Next targets

1. Establish an explicitly stated actual-orbit estimate controlling the
   affine corrections before using this programme in a counting proof.
2. Assess ANC1 in the ancestry-amortization programme, independently of
   the withdrawn escape-set inference.
3. If pursuing spectral or equidistribution claims, specify the finite
   domains or limiting density and the hypotheses needed for the
   conditional statements of §6.
