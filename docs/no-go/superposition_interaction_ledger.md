# Additive superposition and the interaction ledger  [W1]

**Task:** `OPUS5_WIDE_TASKS.md` W1, deliverables (i)–(iii) (session 5 of the
recommended order).
**Building on:** `../repunit/repunit_affine_tail_bound.md` (the cylinder /
affine identity), `outside_box_avenue_triage.md` §§3, 12, 14 (barriers 3 and
4), `certificate_semigroup.md` (W2, which already closed the multiplicative
cousin of this idea).
**Verifier:** `scripts/verify_superposition_ledger.py` (9 checks; exact
integer and rational arithmetic).
**Status:** **Avenue closed.** All three deliverables complete; the kill
criterion fires on both of its clauses.
**License:** CC-BY 4.0

---

## 0. Verdict

W1 asked, in Dr Bry's formulation: split \(n=b_1+\cdots+b_r\) with each part
already certified, and combine the certificates. The task's own honest
framing localised the content in the **interaction ledger**

\[
I_T(a,b)\;=\;C^{(T)}(a+b)-C^{(T)}(a)-C^{(T)}(b),
\]

and predicted the failure mode would be "carry propagation between the
parts". The exact expansion shows the failure is worse than that, and of a
different type.

> **W1-KILL.** \(C^{(T)}\) is affine on each parity cylinder, with slope
> \(\lambda_w=6^{o_w}/2^{T}\) that **depends on the cylinder**. Hence
> \[
> I_T(a,b)=(\lambda_u-\lambda_w)\,a+(\lambda_u-\lambda_v)\,b
> +(\rho_u-\rho_w-\rho_v),
> \]
> and the defect is carried by the *slope* mismatch, not by the intercepts.
> Since \(o_u\ne o_w\) forces
> \(|\lambda_u-\lambda_w|\ge\frac56\max(\lambda_u,\lambda_w)\), the
> interaction term is **of the same size as the trajectories themselves** the
> moment the words diverge — it is not a small carry ledger.
>
> The avenue is then caught in a pincer:
>
> - **actual parts diverge immediately.** For odd \(n=a+b\), exactly one of
>   \(a,b\) is odd, so \(w(a)\) and \(w(b)\) differ in the *first letter*.
>   The closed-form ("all three words agree") regime is empty at \(T=1\) for
>   every two-part decomposition of every odd number. And where the regime is
>   nonempty at all (even \(n\)), it is vacuous: over all \(a,b<200\),
>   \(T\le8\), all \(6581\) agreeing triples have the all-zeros word, so
>   \(\rho_u=0\) and \(I_T=0\) trivially.
> - **the one exact regime uses a virtual part.** \(n=a+2^{N}t\) with
>   \(N\ge E_K(a)+1\) reproduces the repo's cylinder/affine identity exactly —
>   but the part \(b=2^{N}t\) never has its own trajectory computed, only its
>   residue. That is a *virtual* part, void under barrier 4 and under this
>   file's own global kill rule for W1/W8.

The census confirms both clauses quantitatively: over every two-part
decomposition of every odd \(n\le501\), the interaction ledger is never
smaller than the raw correction ledger it was meant to replace — the best
decomposition still has \(\max_T|I_T|/\rho_T\ge11.8\).

---

## 1. Deliverable (ii): the exact expansion

For the raw map \(C\) and a parity word \(w\in\{0,1\}^{T}\) (\(w_i=1\) when
the \(i\)-th iterate is odd), \(C^{(T)}\) restricted to the cylinder of \(w\)
is affine:

\[
C^{(T)}(x)=\lambda_w x+\rho_w,
\qquad
\lambda_w=\frac{3^{o_w}}{2^{\,T-o_w}}=\frac{6^{o_w}}{2^{T}},
\qquad
\rho_w=\sum_{i:\,w_i=1}\frac{6^{\,o_{>i}}}{2^{\,T-1-i}},
\]

where \(o_w=\sum_i w_i\) and \(o_{>i}\) counts the ones after position \(i\).
(The form \(6^{o}/2^{T}\) is worth keeping: it makes the slope a single power
of \(6\), which is what drives §1.2.)

> **W1-A (proved here).** With \(u=w(n)\), \(w=w(a)\), \(v=w(b)\) the three
> length-\(T\) parity words of \(n=a+b\), \(a\), \(b\),
> \[
> \boxed{\;
> I_T(a,b)=(\lambda_u-\lambda_w)\,a+(\lambda_u-\lambda_v)\,b
> +(\rho_u-\rho_w-\rho_v).\;}
> \]

Verified exactly (rational arithmetic) for all odd \(n<300\), all
decompositions, and \(T\in\{1,3,5,8,11\}\).

### 1.1 Corollary: the agreeing case is the raw ledger

If \(u=w=v\) then \(\lambda\) cancels and

\[
I_T=-\rho_u .
\]

So in the only regime where superposition is exact, the interaction ledger
**is** the raw correction ledger, with the sign flipped. This is the kill
criterion's first clause in closed form: \(I_T\) is \(c_K\) bookkeeping
re-partitioned, exactly as triage §3's scalar-flux collapse predicted.

### 1.2 Corollary: divergent words give a full-size defect

\(\lambda_w=6^{o_w}/2^{T}\), so \(o_u\ne o_w\) forces

\[
|\lambda_u-\lambda_w|
=\frac{|6^{o_u}-6^{o_w}|}{2^{T}}
\ \ge\ \frac56\,\max(\lambda_u,\lambda_w),
\]

verified for all \(o_u,o_w<12\). When \(o_u>\max(o_w,o_v)\) both coefficients
are positive and

\[
I_T\ \ge\ \tfrac56\,\lambda_u(a+b)-|\rho\text{-terms}|
\ \approx\ \tfrac56\,C^{(T)}(n),
\]

i.e. the interaction is a constant fraction of the whole trajectory.

**This is the substantive finding.** The task expected the obstruction to be
"binary carry propagation between the parts", i.e. an additive nuisance of
ledger size. It is not: carries change the *number of odd steps*, hence the
*multiplier*, so the defect is multiplicative in \(6^{\Delta o}\). Additivity
fails at the level of the slope, and a slope defect cannot be absorbed into a
correction term.

---

## 2. Deliverable (i): W1.a, in two forms

### 2.1 W1.a-1 — the agreeing regime is empty, and vacuous where nonempty

> **W1.a-1 (proved here).** Let \(n\) be odd and \(n=a+b\) with
> \(a,b\ge1\). Then exactly one of \(a,b\) is odd, so \(w(a)_1\ne w(b)_1\)
> and the three words cannot agree, for any \(T\ge1\).

Trivial, but it is the whole story: the closed-form regime of §1.1 is empty
for every two-part decomposition of every odd number, so \(I_T\) is *never*
in the well-behaved case.

For even \(n\) the regime is nonempty, and there it is vacuous. Searching all
\(1\le a\le b<200\) and \(T\le8\):

| agreeing triples \((a,b,T)\) with \(u=w=v\) | of those with \(\rho_u\ne0\) |
|---:|---:|
| 6581 | **0** |

Every agreeing triple has the all-zeros word, i.e. all three numbers are
being halved throughout, and \(I_T=0\) for the trivial reason that \(C^{(T)}\)
is *linear* (not merely affine) there. The closed-form regime carries no
content anywhere.

*Why.* The cylinder of a word is a single residue class mod \(2^{z^*}\)
(\(z^*\) the number of even steps, plus one if the word ends odd). If
\(a\equiv b\equiv n\equiv r\) in that class and \(n=a+b\), then
\(r\equiv2r\), so \(r\equiv0\): all three are divisible by \(2^{z^*}\), and a
number divisible by \(2^{z^*}\) whose word has \(z^*\) even steps spends all
of them halving.

### 2.2 W1.a-2 — the exact regime is virtual

The task's own preamble gives the one regime where superposition is exact:
for \(n=a+2^{N}t\) with \(a\equiv n\ (\mathrm{mod}\ 2^{N})\) and
\(N\ge E_K(a)+1\), the itineraries of \(n\) and \(a\) agree for \(K\)
accelerated steps and

\[
x_K(n)=x_K(a)+3^{K}2^{\,N-E_K}\,t .
\]

Verified here on 64 000 cases (odd \(a<4000\), \(K\le8\), \(t\in\{1,2,3,7\}\)).

> **W1.a-2.** This is the repo's cylinder/affine identity
> (`repunit_affine_tail_bound.md`) restated as a decomposition. It adds
> nothing, and it is not a superposition of certificates: the part
> \(b=2^{N}t\) never has its own trajectory computed or used — only its
> residue enters. It is a **virtual part**.

This file's global kill rule reads: "any W1/W8 statement whose 'parts' do not
each carry an actual computed trajectory is void (barrier 4)". W1.a-2 is
exactly such a statement. So the pincer closes: the non-void regime never has
agreeing words (§2.1), and the agreeing regime is void (§2.2).

---

## 3. Deliverable (iii): the census

**Family (stated exactly).** Every \(n=a+b\) with \(1\le a\le n/2\) and
\(a,b\) positive integers. Every such part reaches \(1\) by FIN1, so every
decomposition is a genuine pair of certificates. (The task's phrase "both odd
parts \(\le n/2\)" cannot be met for a two-part decomposition of an odd
\(n\): odd + odd is even. That impossibility is W1.a-1.)

**Statistic.** The kill criterion asks whether the interaction ledger can grow
*more slowly* than the raw correction ledger, so we measure

\[
M(a,b)=\max_{1\le T\le H}\frac{|I_T(a,b)|}{\rho_{u,T}},
\qquad H=\max(\sigma_C(n),20),
\]

and minimise over the decomposition. \(M\ge1\) means no gain.

| \(n\) | \(\min_a M\) | at \(a\) | \(|I_T|/\text{trajectory}\) | \(H\) |
|---:|---:|---:|---:|---:|
| 3 | 25.60 | 1 | 1.0000 | 20 |
| 7 | **11.80** | 2 | 1.0000 | 20 |
| 27 | 28.52 | 8 | 0.9997 | 96 |
| 31 | 35.87 | 8 | 0.9998 | 91 |
| 71 | 84.42 | 12 | 0.9997 | 83 |
| 101 | 40.42 | 16 | 0.9318 | 20 |
| 251 | 167.92 | 64 | 0.9961 | 44 |
| 351 | 352.99 | 80 | 0.8711 | 20 |
| 471 | 268.69 | 64 | 0.8541 | 20 |
| 501 | 107.89 | 32 | 0.9690 | 20 |

> **W1-B (finite certificate).** Over every odd \(3\le n\le501\) and every
> two-part decomposition,
> \[
> \min_a\max_T\frac{|I_T|}{\rho_{u,T}}\ \ge\ 11.80,
> \]
> the minimum attained at \(n=7\). At the minimising decomposition the
> interaction is still at least \(0.775\) of the trajectory. So no
> decomposition brings the interaction below the ledger it was introduced to
> replace; the interaction *is* the trajectory, as §1.2 predicts.

**One incidental observation.** In 172 of the 250 cases the minimising part
\(a\) is a power of two. The best a decomposition can do is make one part
trivial (all halvings) — which is the degenerate direction of W1.a-2, i.e.
the pincer's virtual side. There is no third option.

---

## 4. The \(n=471\) testbed

The task's concrete testbed: decompose repunit states as (tower/Mersenne
part) + (remainder). Taking the first pre-descent states of \(a_{471}\)
(746 bits) and \(A=2^{k-1}-1\) or \(2^{k-1}\) with \(k=\operatorname{bitlen}\):

| state | decomposition | \(\max_T|I_T|/\rho_T\) | \(\max_T|I_T|/\text{traj}\) |
|---:|---|---:|---:|
| 0 | \(2^{k-1}-1\) | \(2.1\times10^{226}\) | 1.193 |
| 0 | \(2^{k-1}\) | \(4.6\times10^{224}\) | 0.699 |
| 1 | \(2^{k-1}-1\) | \(1.3\times10^{225}\) | 0.970 |
| 2 | \(2^{k-1}-1\) | \(1.2\times10^{225}\) | 0.955 |

> The \(n=471\) clause of the kill criterion — "if no decomposition of
> \(a_{471}\)'s pre-descent states admits sub-ledger interaction growth, close
> the avenue" — **fires**.

*Scope.* Only the \(d=0\) (Mersenne) member of the tower family is tested
directly. By W2-A the tower member \(w_d(M)=P_2^{\,d}(2^M-1)\) sits within a
factor \((4/3)^d\) of a Mersenne, so it lies in a different parity cylinder
from the state for the same reason, and §1.2 applies unchanged. Testing
higher \(d\) would add data, not a new mechanism.

---

## 5. Barrier check

1. *Finite-state information.* Not invoked.
2. *Density / entropy.* Not invoked; §3 is an exhaustive census over a
   finite family, reported as a finite certificate.
3. *Variable-height Diophantine.* Not invoked.
4. **Virtual sources.** This is the binding barrier, and §2.2 is a clean
   instance: the only exact superposition regime has a part whose trajectory
   is never computed. Recording it here means the naive additive idea does
   not need to be re-triaged.

**Relation to W2.** W2 (session 2) closed the *multiplicative* version of
this idea — orbits of certified numbers under certificate-preserving maps.
W1 closes the *additive* version. The two failures are different: W2's
generators are thin (\(\Theta((\log X)^2)\)); W1's interaction is not thin but
full-size. Together they close the "combine certificates" family in both of
its natural directions.

**Explicit non-claims.** Nothing here bears on Avenue A, storage dominance,
the IEF frontier, or the plateau problem. W1-A is an identity; W1.a-1 and
W1.a-2 are structural negatives; W1-B is a finite census supporting them.

---

## 6. Falsifier

- **W1-A** is falsified by any \((n,a,T)\) at which the displayed identity
  fails. Checked for all odd \(n<300\), all decompositions, five values of
  \(T\), in exact rational arithmetic.
- **W1.a-1** is falsified by an agreeing triple \((a,b,T)\) with
  \(\rho_u\ne0\). None exists with \(a,b<200\), \(T\le8\); the residue-class
  argument of §2.1 explains why.
- **W1-B** is falsified by a decomposition of some odd \(n\) with
  \(\max_T|I_T|/\rho_T<1\) — i.e. an interaction that really is sub-ledger.
  The census found none, with a margin of \(11.8\).
- **The kill as a whole** is falsified by a decomposition family in which the
  three parity words agree for a *growing* number of steps while both parts
  carry actual trajectories. §2.1 shows this is impossible for two parts;
  \(r\ge3\) parts is untested here and is the only remaining door (see §7).

---

## 7. What is left, and why it is not promising

Decompositions into \(r\ge3\) parts are not covered by W1.a-1 (odd + odd +
odd is odd, so three odd parts are possible). But the expansion generalises
verbatim: with words \(u,w^{(1)},\dots,w^{(r)}\),

\[
I_T=\Bigl(\lambda_u-\textstyle\sum_j\lambda_{w^{(j)}}\Bigr)\text{-type terms}
+\Bigl(\rho_u-\textstyle\sum_j\rho_{w^{(j)}}\Bigr),
\]

and the slope mismatch is now generically *larger*, since \(r\) independent
words must all match \(u\). The agreeing regime requires all \(r+1\) words to
coincide, which by the §2.1 argument forces \(2^{z^*}\) to divide every part
and their sum. Nothing suggests \(r\ge3\) improves matters, and the census
cost grows as \(n^{r-1}\). Recorded as **not worth a session** unless a
specific \(r\)-part family with a proved common cylinder is exhibited first.

---

## 8. Verification

```bash
python3 scripts/verify_superposition_ledger.py               # odd n <= 501
python3 scripts/verify_superposition_ledger.py --nmax 151    # faster
```

Prints `SUPERPOSITION-LEDGER: PASS`.

---

## 9. Suggested ledger rows (not applied)

| ID | Statement | Status | Source |
|---|---|---|---|
| SIL1 | \(C^{(T)}(x)=\lambda_wx+\rho_w\) with \(\lambda_w=6^{o_w}/2^T\), and \(I_T(a,b)=(\lambda_u-\lambda_w)a+(\lambda_u-\lambda_v)b+(\rho_u-\rho_w-\rho_v)\) | Proved here | §1 (W1-A) |
| SIL2 | For odd \(n=a+b\) the three parity words never agree; and every agreeing triple with \(a,b<200\), \(T\le8\) has \(\rho_u=0\), so \(I_T=0\) trivially | Proved here / finite certificate | §2.1 |
| SIL3 | \(o_u\ne o_w\Rightarrow|\lambda_u-\lambda_w|\ge\frac56\max(\lambda_u,\lambda_w)\): the superposition defect is a multiplier defect, of trajectory size, not a carry ledger | Proved here | §1.2 |
| SIL4 | Over every odd \(n\le501\) and every two-part decomposition, \(\min_a\max_T|I_T|/\rho_T\ge11.8\) | Finite certificate | §3 (W1-B) |

SIL3 is the row worth keeping: it is the reason the additive idea cannot be
repaired by better bookkeeping.
