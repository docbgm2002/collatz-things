# Macro-Step Lundberg Programme

**Status:** Exact proved structure (MAC1–MAC3, LUN1–LUN2, ANC1). Not a proof
of the Collatz conjecture. **The counting route to SD1 is closed as a dead
end:** its equidistribution hypothesis DISC1 is not merely unproven but
*false*, and the spectral repair WALSH1 is either vacuous or false depending
on how it is read (§6). An earlier draft of this note reported computational
evidence *for* DISC1/WALSH1; that evidence was a normalization artifact and is
retracted here.

**Building on:** `../fuse/fuse_burn_attack.md`,
`avenue_a_comparison_dynamics.md`, `no_local_potential.md`,
`../repunit/next_generation_attack_program.md`.

**License:** CC-BY 4.0

---

## Abstract

We decompose the accelerated odd Collatz map into exact **macro-steps**
(renewal cycles between fuel-exhausted states) and prove that the macro-step
log-drift has a **closed-form Lundberg exponent** $\theta^* = \ln 2$. This
yields a Haar-measure escape bound $\mu(E_a) \leq 2^{-a}$ via Ville's
inequality, and a fully proved **ancestry capacity lemma** (ANC1): the reverse
map has at most one preimage per bit-length.

A counting argument would reduce the universal SD1 statement to an
equidistribution lemma (DISC1) for the escape set $E_a$. We show in §6 that
**DISC1 is false**: the burn identity forces $E_a$ to contain the entire
residue class $x \equiv -1 \pmod{2^{t_a}}$, $t_a = \lceil a/\alpha\rceil + 1$,
inside which its relative density is $1/\mu(E_a) \geq 2^a$. The proposed
spectral repair (WALSH1) does not survive either: read literally its bound is
a trivial corollary of LUN2, and read as a white-noise claim it is
contradicted by the same cylinder containment, which forces
$\max_{\eta \neq 0}|\hat{1}_{E_a}(\eta)| \geq (1-\mu)/(2^{t_a}-1)$, a bound
independent of the sampling domain.

The proved core (MAC1–MAC3, LUN1–LUN2, ANC1) is unaffected: it is a sharp
"almost all" theorem, and the obstruction to promoting it to "all" is the
same fuel-concentration phenomenon identified in `no_local_potential.md`.

---

## 0. Notation

As in `../../NOTATION.md`: $f(x) = (3x+1)/2^{v_2(3x+1)}$ for odd $x > 1$;
$\tau(x) = v_2(x+1)$ (trailing-one fuel);
$\operatorname{bitlen}(x) = \lfloor \log_2 x \rfloor + 1$.
Write $\alpha = \log_2 3 - 1 \approx 0.584963$.

---

## 1. Macro-step decomposition

### MAC1 (Fuel partition). — **proved**

Every odd $x$ is in exactly one of two classes:

- **Class A (fuel-burning):** $\tau(x) \geq 2$. Then $x = 2^L m - 1$ with
  $L \geq 2$, $v_2(3x+1) = 1$, $f(x) = 3 \cdot 2^{L-1} m - 1$, and
  $\tau(f(x)) = L - 1$. Log-drift: $\Delta_A = \log_2 3 - 1 = \alpha > 0$.

- **Class B (fuel-exhausted):** $\tau(x) = 1$, i.e. $x \equiv 1 \pmod{4}$.
  Then $v_2(3x+1) \geq 2$.

A **macro-step** starts at a Class B state, takes one Class B step (payout
$v$, new fuel $K = \tau(f(x))$), then exactly $K-1$ Class A steps, returning
to Class B.

*Proof.* Class A is the suffix-burn identity of `../fuse/fuse_burn_attack.md`
§1. For Class B: $x = 4k+1 \Rightarrow 3x+1 = 4(3k+1)$, so $v \geq 2$.
$\blacksquare$

> **Naming.** "Class A / fuel-burning" is the $\tau \geq 2$, $v = 1$ step;
> "Class B / fuel-exhausted" is the $\tau = 1$ step that pays out and
> recharges. Earlier drafts elsewhere in the repository called the Class A
> steps "recharge steps"; that usage is retired — a *recharge* is the Class B
> event that creates new fuel, and a *burn* consumes it.

---

## 2. Independence theorem

### MAC2 (Independence of payout and new fuel). — **proved**

Let $x$ be Haar-uniform in $\mathbb{Z}_2^{\mathrm{odd}}$ conditioned on
$\tau(x) = 1$. Let $v = v_2(3x+1)$ and $K = \tau(f(x))$. Then $v$ and $K$
are independent, with

$$\Pr(v = j) = 2^{-(j-1)} \ (j \geq 2), \qquad \Pr(K = i) = 2^{-i} \ (i \geq 1).$$

In particular $\mathbb{E}[v] = 3$ and $\mathbb{E}[K] = 2$.

*Proof.* Write $x = 4k+1$, $u = v - 2 = v_2(3k+1) \geq 0$, and
$3k+1 = 2^u m$ with $m$ odd. Since $3$ is a $2$-adic unit, the map
$k \mapsto m = (3k+1)/2^u$ is a measure-preserving bijection from the affine
subspace $\{k : v_2(3k+1) = u\}$ onto $\mathbb{Z}_2^\times$. Now
$K = v_2(m+1)$, and for Haar-uniform odd $m$,
$\Pr(v_2(m+1) = i) = 2^{-i}$, independent of $u$. Hence $K \perp v$.
The marginal for $v$ is immediate from $v = 2 + v_2(3k+1)$. $\blacksquare$

---

## 3. Macro-step drift

### MAC3 (Exact drift). — **proved**

The log-drift of one macro-step is

$$\Delta = (\log_2 3 - v) + (K-1)(\log_2 3 - 1) = K\alpha + 1 - v,$$

and

$$\mathbb{E}[\Delta] = \mathbb{E}[K]\alpha + 1 - \mathbb{E}[v]
= 2\alpha - 2 = 2\log_2 3 - 4 \approx -0.830075.$$

*Proof.* Linearity of expectation and MAC2. $\blacksquare$

---

## 4. Lundberg exponent and escape bound

The substance of this section is an exact identity, stated first; the
Lundberg exponent is its restatement.

### LUN1A (Macro-steps are value-neutral). — **proved**

Over one macro-step, the *value ratio itself* has expectation exactly one:

$$\mathbb{E}\!\left[\frac{x_{\text{out}}}{x_{\text{in}}}\right] = 1.$$

*Proof.* By MAC3 the ratio is $2^{\Delta} = 2^{K\alpha + 1 - v}
= (3/2)^K \cdot 2^{1-v}$. By MAC2 the two factors are independent, and both
series converge:

$$\mathbb{E}\big[(3/2)^K\big] = \sum_{i \geq 1} 2^{-i} (3/2)^i
= \sum_{i \geq 1} (3/4)^i = 3,$$

$$\mathbb{E}\big[2^{1-v}\big] = 2 \sum_{j \geq 2} 2^{-(j-1)} 2^{-j}
= 4 \sum_{j \geq 2} 4^{-j} = \tfrac13 .$$

Their product is $3 \cdot \tfrac13 = 1$. $\blacksquare$

> **Reading.** The accelerated odd map is a martingale **in value**, not
> merely a negative-drift walk in log-value. The two coexist because
> $\mathbb{E}[\log_2(\cdot)] = 2\log_2 3 - 4 < 0 = \log_2 \mathbb{E}[\cdot]$,
> a strict Jensen gap of $\approx 0.83$ bits per macro-step: the mean is
> carried entirely by rare high-$K$ excursions while the typical trajectory
> descends. This is the exact form of the classical heuristic that Collatz
> "should" descend, and it identifies precisely where the heuristic's
> expectation and its typical behaviour part company.

### LUN1 (Closed-form Lundberg exponent). — **proved**

The moment generating function of $\Delta$ is

$$M(\theta) = \mathbb{E}[e^{\theta \Delta}]
= \frac{e^{\theta(\alpha-1)}}{(2 - e^{\theta\alpha})(2 - e^{-\theta})},
\qquad \theta < \frac{\ln 2}{\alpha} \approx 1.1850,$$

and the unique positive solution of $M(\theta) = 1$ is

$$\theta^* = \ln 2.$$

*Proof.* Geometric-series evaluation of $\mathbb{E}[e^{\theta K \alpha}]$ and
$\mathbb{E}[e^{-\theta v}]$ gives the displayed formula. That $\theta^*=\ln 2$
is a root is LUN1A verbatim, since $e^{(\ln 2)\Delta} = 2^{\Delta}$ is the
value ratio; directly, at $\theta = \ln 2$ one has
$e^{\theta\alpha} = 3/2$, $e^{-\theta} = 1/2$, $e^{\theta(\alpha-1)} = 3/4$,
so $M(\ln 2) = \frac{3/4}{(1/2)(3/2)} = 1$. Uniqueness follows from strict
convexity of $\log M$ and $M(0) = 1$, $M'(0) = \mathbb{E}[\Delta] < 0$.
$\blacksquare$

> **Why the exponent is clean.** $\theta^* = \ln 2$ is not a numerical root
> that happens to land on a familiar constant: it is forced by LUN1A, because
> $e^{\theta \Delta}$ at $\theta = \ln 2$ *is* $x_{\text{out}}/x_{\text{in}}$.
> Any accelerated map whose one-step value ratio has mean $1$ has Lundberg
> exponent $\ln 2$ in base-$2$ log-drift coordinates.

**Novelty: unchecked.** The negative log-drift is classical
(Terras 1976, Everett 1977). The exact value-martingale identity LUN1A is not
something the repository's bibliography pass covers, and
`BIBLIOGRAPHY_PASS.md` has not been extended to it. Do not claim priority for
LUN1A without a literature check.

### LUN2 (Haar escape bound via Ville). — **proved**

For Haar-random odd $x_0 \in \mathbb{Z}_2$, let $S_N = \sum_{i=1}^N \Delta_i$
be the cumulative macro-step log-drift. Then $e^{(\ln 2) S_N}$ is a
non-negative martingale, and by Ville's inequality,

$$\Pr\left(\sup_{N \geq 0} S_N \geq a\right) \leq 2^{-a} \qquad (a > 0).$$

Equivalently: the Haar measure of starting points whose orbit ever reaches
$2^a$ times its initial value is at most $2^{-a}$.

*Proof.* Three steps; the first is the only substantive one and was elided in
an earlier draft.

**(i) The $\Delta_i$ are i.i.d.** MAC2 gives independence of $(v, K)$ at a
*single* step, for a Haar-uniform point conditioned on $\tau = 1$. The
martingale property needs more: that the state entering macro-step $i+1$ is
again Haar-uniform on $\{\tau = 1\}$ and independent of
$\mathcal{F}_i = \sigma(\Delta_1, \ldots, \Delta_i)$. This is supplied by the
standard $2$-adic conjugacy: the accelerated odd map extends to a
measure-preserving, ergodic map of $\mathbb{Z}_2$ that is topologically
conjugate to the one-sided shift, with the conjugacy $Q_\infty$ carrying Haar
measure to Haar measure (Lagarias 1985 §3; Bernstein–Lagarias 1996). Under
that conjugacy the macro-step decomposition of MAC1 cuts the digit stream into
consecutive disjoint blocks whose lengths are determined by the block contents
themselves, i.e. it is a renewal partition of an i.i.d. digit sequence. Hence
$\Delta_1, \Delta_2, \ldots$ are i.i.d. with the law of MAC3.

**(ii) The martingale.** By (i) and $M(\ln 2) = 1$ from LUN1,
$\mathbb{E}[e^{(\ln 2)\Delta_{i+1}} \mid \mathcal{F}_i] = 1$, so
$W_N := e^{(\ln 2) S_N}$ is a non-negative martingale with $W_0 = 1$.

**(iii) Ville.** $\Pr(\sup_N W_N \geq 2^a) \leq \mathbb{E}[W_0] \cdot 2^{-a}
= 2^{-a}$, and $W_N \geq 2^a \iff S_N \geq a$. $\blacksquare$

**Remark (the supremum really is the orbit maximum).** $S_N$ records the
log-ratio only at macro-step *endpoints*, but the stated corollary is about
the orbit ever reaching $2^a x_0$. These agree: within one macro-step the
Class B step multiplies by $3 \cdot 2^{-v}$ with $v \geq 2 > \log_2 3$, hence
strictly decreases the value, and the following $K-1$ Class A steps each
multiply by more than $3/2$, hence increase monotonically. So the maximum over
a macro-step is attained at its endpoint, and
$\sup_N S_N$ is the log of the true orbit maximum.

> **Reading.** LUN2 is an "almost-all" descent theorem: a Haar-random
> $2$-adic starting point descends with probability $1$. This recovers the
> Terras/Everett-type density results by a strictly sharper mechanism (exact
> exponent $\ln 2$, exact renewal structure). It is **not** a statement about
> any specific integer; bridging that gap is §5–§7.

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

## 6. The counting route to SD1 is a dead end

This section replaces the earlier §6, which reported computational evidence
*supporting* the equidistribution hypothesis DISC1. That evidence was an
artifact of normalizing against the Haar bound $2^{-a}$ instead of against the
observed measure $\mu(E_a)$; corrected, the same computation points the other
way. The hypothesis is refuted below by an exact argument, with the
computation serving only as illustration.

Throughout, fix the escape set

$$E_a = \{x \text{ odd} : \text{the orbit of } x \text{ ever reaches } \geq 2^a x\},$$

so that LUN2 reads $\mu(E_a) \leq 2^{-a}$.

### 6.1 The original obstruction (retained)

The counting skeleton assumed that equidistribution of $E_a$ follows from
cylinder depth. This is incorrect: the escape cylinders have depth
$L \approx 3.6a$ (expected total payout over the escape window), exceeding the
$b = a$ needed for the counting step, and the argument fails when $L > b$. So
DISC1 was left as an independent claim. §6.2 shows the independent claim is
false.

### 6.2 DISC1 is false — the burn family is entirely inside $E_a$

### FUEL1 (Deterministic escape from fuel). — **proved**

Let $t_a := \lceil a/\alpha \rceil + 1$, where $\alpha = \log_2 3 - 1$. Then

$$\tau(x) \geq t_a \implies x \in E_a,$$

equivalently $E_a \supseteq \{x : x \equiv -1 \pmod{2^{t_a}}\}$: a *full
residue class*, with no exceptions and no probabilistic content.

*Proof.* Let $\tau(x) = L \geq t_a$. By MAC1, the first $L-1$ steps are all
Class A, and each satisfies $f(y)/y = 3/2 + 1/(2y) > 3/2$
(`no_local_potential.md` Lemma 1). Composing, the value after $L-1$ steps
exceeds $x \cdot (3/2)^{L-1} = x \cdot 2^{\alpha(L-1)}$. Since
$L - 1 \geq t_a - 1 = \lceil a/\alpha \rceil \geq a/\alpha$, we get
$\alpha(L-1) \geq a$, so the orbit reaches at least $2^a x$. $\blacksquare$

**Consequence (DISC1 is false).** Within the class $x \equiv -1 \pmod{2^{t_a}}$
the relative density of $E_a$ is exactly $1$, while its global density is
$\mu(E_a) \leq 2^{-a}$. The relative density of $E_a$ in that one class is
therefore at least $2^a$ — it is overrepresented by a factor growing
exponentially in $a$. No equidistribution statement of the form assumed by the
counting argument can hold.

The mechanism is not new to this note: it is the *residue-freezing* of
`no_local_potential.md` §1, where the burn family $3^j 2^t - 1$ was shown to
sit in the single residue $-1$ however large its members grow. FUEL1 says that
this same frozen family is a subset of every escape set.

### 6.3 WALSH1 does not repair it

The spectral proposal was to replace DISC1 by a bound on the Walsh
coefficients of $1_{E_a}$. Normalize as in `scripts/verify_walsh1.py`, so that
$\hat A(0) = \mu(E_a)$. Then the proposal fails on both available readings.

**Reading 1 — literal. The stated bound is vacuous.** WALSH1-Analytic asked
for $|\hat A(\eta)| \leq C \cdot 2^{-a}$ for all $\eta \neq 0$. But for any
indicator function and any $\eta$,

$$|\hat A(\eta)| \;\leq\; \hat A(0) \;=\; \mu(E_a) \;\leq\; 2^{-a},$$

the last inequality being LUN2. So the bound holds with $C = 1$ as an
immediate corollary of a result already proved in §4, and cannot be "the
single remaining open problem." Any nonvacuous version must specify a $C$
strictly smaller than the observed ratio $\mu(E_a)/2^{-a} \approx 0.74$–$0.87$,
and the counting argument must be shown to close for that specific $C$ — which
it was never checked to do.

**Reading 2 — as intended. The white-noise claim is false.** The substantive
reading is that $E_a$ has no macroscopic structure, i.e.
$\max_{\eta \neq 0} |\hat A(\eta)| = o(\mu(E_a))$ as the sampling domain
grows. FUEL1 refutes this. Let $C \subseteq E_a$ be the cylinder of
codimension $t_a$ from FUEL1 and let $V$ be the $2^{t_a}$-element group of
Walsh frequencies supported on those $t_a$ coordinates. Expanding $1_C$ in
characters and using $C \subseteq E_a$,

$$2^{-t_a} = \mathbb{E}[1_{E_a} 1_C]
= 2^{-t_a} \sum_{\eta \in V} \chi_\eta(c)\, \hat A(\eta),$$

so $\sum_{\eta \in V} \chi_\eta(c) \hat A(\eta) = 1$. Splitting off
$\eta = 0$ and bounding the remaining $2^{t_a} - 1$ terms by their maximum,

$$\boxed{\;\max_{\eta \neq 0} |\hat A(\eta)| \;\geq\; \frac{1 - \mu(E_a)}{2^{t_a} - 1}\;}$$

The right-hand side depends only on $a$. It does **not** decay as the sampling
domain grows, whereas a genuinely random subset of density $\mu$ in a domain
of $N$ points has $\max_{\eta \neq 0}|\hat A| \approx
\sqrt{\mu(1-\mu)/N}\cdot\sqrt{2\ln N} \to 0$. So for every fixed $a$, taking
$N$ large enough makes the escape set provably *more* spectrally concentrated
than noise, by an unbounded factor. $E_a$ is not white noise at any scale.

### 6.4 Why the original computation looked supportive

Reproduced by `scripts/verify_walsh1.py` on the domain
$D = \{2j+1 : j < 2^{14}\}$ with a $4000$-step cap:

| $a$ | $\mu(E_a)$ | $\mu/2^{-a}$ | $\max_{\eta\neq0}\|\hat A\|$ | ratio to $2^{-a}$ | ratio to $\mu$ | random baseline | observed / random |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | 0.4323 | 0.865 | 0.2210 | 0.442 | 0.511 | 0.01705 | 12.96 |
| 2 | 0.2065 | 0.826 | 0.1022 | 0.409 | 0.495 | 0.01393 | 7.34 |
| 3 | 0.1045 | 0.836 | 0.0529 | 0.423 | 0.506 | 0.01053 | 5.02 |
| 4 | 0.0507 | 0.811 | 0.0279 | 0.446 | 0.550 | 0.00755 | 3.69 |
| 5 | 0.0231 | 0.740 | 0.0130 | 0.416 | 0.562 | 0.00517 | 2.51 |

Three corrections to the earlier reading:

1. **The old §6.2 table is superseded.** It used a different, unstated domain
   ($b = a+12$ bit integers) and disagreed with the old §6.3 table about
   $\mu(E_a)$, which is the same quantity. Its $a = 5$ row was also internally
   impossible: a *maximum* over residue classes cannot fall below the mean,
   which under its own normalization was $\mu/2^{-a} - 1 = -0.251$, yet it
   reported $-0.430$.

2. **"Max excess" was normalized against $2^{-a}$, not $\mu(E_a)$.** Since
   $\mu(E_a)$ is only $0.74$–$0.87$ of $2^{-a}$ and that ratio *falls* with
   $a$, a uniformly deficient set reads as increasingly equidistributed. The
   apparent improvement, and the sign change at $a = 4$, were entirely this
   artifact. Renormalized against $\mu(E_a)$, the residue distribution mod
   $2^{a+2}$ is grossly non-uniform and gets worse with $a$:

   | $a$ | richest class | its relative density | empty classes |
   | :-- | :-- | :-- | :-- |
   | 1 | $7 = 2^3-1$ | 2.31 | 0 / 4 |
   | 3 | $31 = 2^5-1$ | 4.82 | 0 / 16 |
   | 5 | $127 = 2^7-1$ | 11.99 | 15 / 64 |

   The richest class is $2^{a+2}-1$ at every scale — the maximal trailing-one
   class, exactly as FUEL1 predicts — and by $a = 5$ nearly a quarter of odd
   residue classes contain no escaping element at all.

3. **The flat ratio was the tell.** $\max|\hat A|$ tracks $\mu(E_a)$ at a
   ratio of $0.50$–$0.56$ that does not decay with $a$ (and if anything
   rises). White noise would scale like $\sqrt{\mu/N}$, not like $\mu$.
   Reading the ratio against $2^{-a}$ instead produced the flat $\approx 0.44$
   that was mistaken for a clean bound; it is flat because the coefficients
   are proportional to the measure, which is the signature of structure.
   Consistently, the argmax sits at $\eta \in \{1, 3, 4\}$ — the *lowest*
   frequencies, i.e. the bottom bits of $x$, i.e. $\tau$.

---

## 7. What this does and does not do

**Does:**

1. Gives the exact renewal structure of the map (MAC1–MAC3).
2. Gives the exact Lundberg exponent $\theta^* = \ln 2$ and the sharp Haar
   escape bound $2^{-a}$ (LUN1–LUN2), with the i.i.d. step supplied by the
   $2$-adic conjugacy.
3. Proves the single-preimage ancestry capacity (ANC1).
4. Proves that fuel alone forces escape (FUEL1), and thereby **refutes** the
   equidistribution hypothesis DISC1 and the white-noise reading of WALSH1.

**Does not:**

1. Prove SD1. The counting route is closed, not merely unfinished.
2. Prove the Collatz conjecture. LUN2 is an "almost all" theorem and the gap
   to "all" is untouched.
3. Supersede the live spine (Avenue A storage-dominance / 267-family). It is
   a parallel route; the two share the same bottleneck in different language.

**Novelty caveat.** LUN2 recovers Terras/Everett-type density results. The new
content is the exact exponent $\theta^* = \ln 2$ and the exact renewal
structure, not the "almost all" conclusion itself.

---

## 8. Where the obstruction actually sits

The counting route died for a reason worth recording, because it is the same
reason `no_local_potential.md` gives:

> Escape is driven by trailing-one fuel, fuel is a low-bit residue condition,
> and therefore the escape set is concentrated on frozen residue classes
> rather than spread across them. Any argument that needs $E_a$ to look
> generic mod $2^k$ is attacking the one property it demonstrably lacks.

This is recorded as **closure 6** in `obstruction_map.md` §2, which is the
intended point of reuse: it is cheap to state, permanent, and it redirects
effort away from a whole family of arguments.

**A decomposition of $E_a$ by fuel level was considered and is not
recommended.** One could ask whether $\mu(E_a \setminus \{\tau \geq t_a\})$ is
bounded by $c \cdot 2^{-a}$ with $c < 1$ and recurses on lower-$\tau$
cylinders. The residual set is escape by *accumulated* rather than initial
fuel — which is the large-deviations problem LUN2 already handles in
aggregate, and the recursion has no evident base case. Recorded here so the
question is not re-derived and re-attempted from scratch.

---

## 9. Verification

`scripts/verify_macro_step_lundberg.py` checks MAC2, MAC3, LUN1, LUN1A, ANC1
and prints an evidence-only escape-frequency probe.

`scripts/verify_walsh1.py` reproduces all tables of §6, checks FUEL1 by
exhaustive search over the relevant residue class, and prints the forced Walsh
lower bound of §6.3 against the random-subset baseline.

---

## 10. Next targets

Ranked, with honest expectations.

1. **Literature check on LUN1A** (§4). The value-martingale identity
   $\mathbb{E}[x_{\text{out}}/x_{\text{in}}] = 1$ is exact and clean, and the
   repository's bibliography pass does not cover it. Cheap; settles whether
   this note contains anything citable.
2. **Test ANC1 against ancestry-amortization** (`obstruction_map.md` §4 item
   3, §4.3). The reverse-tree capacity corollary in §5 is the only bridge from
   this note to a live open item. Modest odds, cheap to test.
3. **Retire the WALSH1 line.** No further effort on spectral properties of
   $E_a$; they are false, not unproven. This is an instruction to stop, not a
   task.

**Not** a next target: the fuel-level decomposition (§8), or anything
requiring $E_a$ to be generic mod $2^k$.
