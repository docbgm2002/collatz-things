# Route A: Hecke–Mahler identification and the dio(w) = 1 barrier

Status: **analysis note** — contains one proved identity, one literature
survey, and one open-problem formulation.  No new universal claims are
promoted; the note clarifies the relationship between IEF9, IEF10, and
the known transcendence toolkit, and states the independent problem
stripped of Collatz language.

Dependencies: IEF1–IEF5, IEF9, IEF10, IEF12, IEF17, PCD16.

---

## 1.  The Hecke–Mahler function and the mechanical word

### 1.1  Setup

The Hecke–Mahler function is

    f(α, β) = Σ_{n≥0} β^n ⌊α(n+1)⌋ .

In Z_2, take β = 2 (since |2|_2 = 1/2 < 1, the series converges).
The balanced slope is α = log_2(3) − 1 ≈ 0.58496.

### 1.2  Identity: f(α, 2) = −ξ_mech  [proved]

Define the mechanical word of slope α:

    s_m = ⌊α(m+1)⌋ − ⌊αm⌋ ∈ {0, 1} .

Since 0 < α < 1, telescoping gives ⌊α(n+1)⌋ = Σ_{m=0}^{n} s_m.
Substituting into f and exchanging the order of summation:

    f(α, 2) = Σ_{n≥0} 2^n Σ_{m=0}^{n} s_m
            = Σ_{m≥0} s_m Σ_{n=m}^{∞} 2^n .

In Z_2 the geometric series gives Σ_{n=m}^{∞} 2^n = −2^m, so

    f(α, 2) = −Σ_{m≥0} s_m 2^m = −ξ_mech ,

where ξ_mech is the 2-adic integer whose binary digits are s_0, s_1, …

### 1.3  Trivial irrationality  [proved]

Since α is irrational, (s_m) is a Sturmian word, hence aperiodic.
A 2-adic integer is rational iff its digit sequence is eventually
periodic.  Therefore ξ_mech ∉ Q, hence f(α, 2) ∉ Q.

No Baker theorem, no Hecke–Mahler theorem, no transcendence theory
of any kind is required.  The proof is one line:

    irrational slope ⟹ aperiodic mechanical word ⟹ irrational 2-adic number.

### 1.4  This is NOT the IEF9 value

The IEF9 "complete balanced start" is the inverse parity conjugacy
value

    ξ_IEF9 = −1/3 − (4/3) Σ_{i≥1} (2/3)^i · 4^{⌊γi⌋},
             γ = ½ log_2(3/2) .

This involves the carry structure (powers of 3, base 2/3), not just
the mechanical word digits.  The two objects are provably different:

    f(α, 2) mod 2^100 = 409239094872214716550681809558
    ξ_IEF9  mod 2^100 = 185313456791844325941675045693

(verified by scripts/verify_balanced_q3_hecke_mahler.py).

The trivial aperiodicity argument does NOT extend to ξ_IEF9, because
the "digits" in base 2/3 are 4^{⌊γi⌋}, which grow exponentially, and
the 2-adic digits of ξ_IEF9 are a complex function of these
coefficients involving carries through the 3^i denominators.

---

## 2.  The boundary obstruction

The terms of the IEF9 series satisfy

    |(2/3)^i · 4^{⌊γi⌋}|_R ≈ 1      (the series diverges in R)
    |(2/3)^i · 4^{⌊γi⌋}|_2 → 0       (the series converges in Z_2)

because (2/3)^i · 4^{γi} = (2/3)^i · (3/2)^i = 1.

The series sits exactly on the convergence boundary.  This is why the
known Hecke–Mahler theorems do not fire:

- Bugeaud–Laurent need |z_1 z_2^θ| < 1; here it equals 1.
- Luca–Ouaknine–Worrell treat |β| > 1 (Archimedean); here |β|_2 < 1.
- Sturmian digit results do not apply because the lift digits
  occupy full finite alphabets, not {0,1}.

---

## 3.  What IEF10 actually proves

IEF10 sidesteps the full irrationality question.  It proves the
weaker claim ξ_IEF9 ∉ Z_{>0} using:

1. Standard-word periodic approximants (continued fraction
   convergents of the Beatty sequence).
2. PCD16 near-isometry (real multiplier ∈ (2/3, 3/2)).
3. Baker's finite irrationality measure for
   β = 2/log_2(3/2) − 3.

This is sufficient for the Collatz application (we only need to
exclude positive integers, not all rationals).

Full irrationality ξ_IEF9 ∉ Q remains open.

---

## 4.  The dio(w) > 1 barrier: literature survey

### 4.1  The transcendence toolkit

Every known transcendence or irrationality theorem for numbers
defined by digit expansions requires dio(w) > 1 or an equivalent
structural condition:

| Tool                        | Requires              | Reference              |
|-----------------------------|-----------------------|------------------------|
| Ferenczi–Mauduit (1997)     | Sturmian digits       | [FM97]                 |
| Bugeaud–Kim (2015)          | dio(w) > 1            | [BK15]                 |
| Kebis "echoing" (2024)      | Echoing word + alg. β | [Keb24]                |
| Adamczewski–Bugeaud (2007)  | Sublinear complexity  | [AB07]                 |
| Luca–Ouaknine–Worrell (2022)| Sturmian + |β| > 1  | [LOW22]                |

[FM97]  Ferenczi, Mauduit. "Transcendence of numbers with a Sturmian
        digit expansion." J. Number Theory 70 (1997).
[BK15]  Bugeaud, Kim. "On the Diophantine exponent of a Sturmian
        word." Acta Arith. 167 (2015).
[Keb24] Kebis. "Echoing words and transcendence." 2024.
[AB07]  Adamczewski, Bugeaud. "On the complexity of algebraic
        numbers II." Ann. of Math. 165 (2007).
[LOW22] Luca, Ouaknine, Worrell. "On the transcendence of
        Sturmian-type numbers." 2022.

### 4.2  The common mechanism

All these tools use the same three-step mechanism:

1. dio(w) > 1 ⟹ good periodic-prefix approximants exist
   (shifts r_n → ∞ with agreement length s_n ≥ c · r_n).
2. These approximants produce rational approximations to ξ that are
   "too good" for an algebraic number.
3. The Subspace Theorem (or Ridout, or Baker) gives a contradiction.

The echoing criterion (Kebis 2024) formalises step 1: an echoing
word has self-similar prefixes with mismatches confined to few, small
intervals with expanding gaps.  Every Sturmian word is echoing, and
echoing ⟹ dio(w) > 1.

### 4.3  The dio(w) = 1 gap

From Kebis (2024): 1 ≤ Dio(u) ≤ ∞ for all infinite words u, and
eventually periodic words have Dio(u) = ∞.

A 2026 paper confirms: "there are many examples of infinite words
over a finite alphabet whose refined Diophantine exponent is equal
to 1."

There is no known transcendence or irrationality theorem that works
for dio(w) = 1.  The entire periodic-approximant mechanism breaks
down because there are no good periodic approximants to feed into it.

### 4.4  The Bugeaud–Kim complexity bound

Bugeaud and Kim (2017, sharpened 2026) proved:

    liminf_{n→∞} p(n, ξ, b)/n ≥ 1 + (−μ³+2μ²+μ−1)/(μ⁴−2μ³+3μ²−3μ+1)

where μ = μ(ξ) is the irrationality exponent.  For algebraic
irrationals (μ = 2 by Roth): liminf p(n)/n ≥ 8/7.

For dio(w) = 1, the return time function satisfies rep(w) ≈ 1, and
the complexity lower bound p(n) ≥ r(n) − n becomes trivial.

### 4.5  The p-adic extension

Adamczewski and Bugeaud also proved: the Hensel (p-adic) expansion
of every irrational algebraic p-adic number cannot have low
complexity.

Potential relevance: if the 2-adic cocycle stream has low factor
complexity, then it is either rational or transcendental in Q_2.
Rationality is excluded by aperiodicity (non-cyclic word).  So the
cocycle stream would be transcendental, hence irrational, hence the
lift blocks are not eventually zero.

Open question: does the cocycle stream have low complexity?  The
PCD16 near-isometry suggests complexity close to the word w, but
"close" in the real metric does not control symbolic complexity.

**Finite diagnostic (2026-07-19).**  The explore script
`scripts/explore_cocycle_factor_complexity.py` measures factor complexity
of the IEF4 dual-digit stream on the residual-axis families.  Through
1000 blocks, every tested family — including mechanical/Sturmian, where
the block word has \(p(n)=n+1\) — has dual-digit alphabet fully occupied
(64/64) and dual-digit factor counts saturating the finite-prefix ceiling
already at length \(n=4\).  The zero/nonzero projection stays somewhat
thinner but still has \(p(n)/n\) growing.  Conclusion of the sample:
symbolic cocycle complexity is **not** inherited from low word
complexity, so the Adamczewski–Bugeaud p-adic route is not supported by
the finite evidence.  This is not a proof that every infinite dual-digit
stream has superlinear complexity.

---

## 5.  The IEF sequence as a dio(w) > 1 discharge programme

Every IEF12–IEF21 discharge exploits structure that gives dio(w) > 1
or an equivalent periodic approximation:

| IEF lemma | Structural condition              | Tool                    |
|-----------|-----------------------------------|-------------------------|
| IEF12     | Sturmian (dio > 1)                | Bugeaud–Kim repetition  |
| IEF13     | Bounded discrepancy + lin. compl. | Adamczewski–Bugeaud     |
| IEF14     | Growing discrepancy + prefix surp.| Periodic-prefix discharge|
| IEF16     | Linear density drift              | Parity-density theorem  |
| IEF19     | Sublinear drift + rep. exp. > 1   | Repetition theory       |
| IEF20–21  | Fixed-surplus repetitions         | Draw-up / endpoint cost |

The IEF17 survivor is specifically designed to evade all these tools:
dio(w) = 1, repetition exponent 1, unbounded discrepancy, non-cyclic.

---

## 6.  The independent problem, stated cleanly

The Collatz-free freeze lives in
[`dio1_cocycle_problem.md`](dio1_cocycle_problem.md).  In brief:

> **D1.**  Every aperiodic \(w\in\{3,4\}^{\mathbb N}\) with
> \(\operatorname{dio}(w)=1\) has dual-digit stream \(j(w)\) (defined by
> the fixed integer table and residue recurrence in that note) not
> eventually zero.
>
> **D1R.**  The same conclusion under the narrower residual hypotheses
> \(\operatorname{rep}(w)=1\), unbounded critical discrepancy, and
> \(\liminf S_L/L=0\).

The dual-digit stream is defined from \(w\) alone; Collatz appears only
in the application bridge of that note (§8).

Known tools that fail: echoing (needs dio > 1), Subspace Theorem via
periodic approximants (needs dio > 1), Adamczewski–Bugeaud complexity
(needs low complexity of the digit stream), Baker's theorem via
periodic approximants (needs periodic structure).

Candidate tools that might work:

1. **L4 coupling** (combinatorial-ergodic): replenishment after
   valleys creates structure that violates the margin condition.
   Exploits anti-structure.  See l4_coupling_analysis.md.

2. **Adamczewski–Bugeaud p-adic** (if the cocycle stream has low
   complexity): transcendence via complexity.  Needs a complexity
   bound on the cocycle stream.  Finite sample currently opposes
   that hypothesis; see §4.5 diagnostic.

3. **A new Subspace Theorem argument** that does not use periodic
   approximants but instead uses the carry structure (3^{R_L} mod 2^L)
   directly.

4. **Direct \(\Phi_r\)-orbit obstruction** (dio1_cocycle_problem.md §7):
   an eventually-zero tail yields a path in the functional integer graph
   \(\mathcal G\) of \(\Phi_3,\Phi_4\) transitions.  Theorem G proves no
   infinite path exists (mixed case via finite \(\mathrm{AB}\) nesting),
   hence D1; probe in `scripts/explore_zero_digit_orbits.py`.

---

## 7.  Summary of claim statuses

| Claim                                          | Status   |
|------------------------------------------------|----------|
| f(α, 2) = −ξ_mech                             | Proved   |
| ξ_mech ∉ Q (trivial, by aperiodicity)         | Proved   |
| ξ_IEF9 ≠ f(α, 2) (different objects)          | Proved   |
| ξ_IEF9 ∉ Z_{>0} (IEF10, Baker)                | Proved   |
| ξ_IEF9 ∉ Q (full irrationality)               | Open     |
| dio(w) = 1 evades all known transcendence tools| Survey   |
| Problems D1 / D1R / Theorem G                  | Ledger IEF22--IEF23 |
| Integrality exclusion in \(\mathcal L_{3/4}\)  | Ledger IEF24 |
| L4 coupling mechanism                          | Exploratory |
| Adamczewski–Bugeaud p-adic route               | Open; finite sample opposes low cocycle complexity |