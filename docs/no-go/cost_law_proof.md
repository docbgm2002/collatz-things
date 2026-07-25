# COST1: Proof of the Diophantine Cost Law

**Building on:** `docs/no-go/general_cost_law.md` (QLG-GEN, DICH1)
**Status:** Proved here, modulo one classical input (step 6), which is
attributed and not reproved. Upgrades the cost law from a finite certificate
over ten maps to a theorem. Machine-checked step by step in
`scripts/verify_cost_law_proof.py`.
**Ledger:** COST1
**License:** CC-BY 4.0

---

## 1. Statement

Let \(\beta=\log_c a\) be **irrational** (by DICH1 this is exactly the
non-degenerate case), let \(Q\ge1\), and write

\[
E_K=\lfloor K\beta\rfloor,\quad L_Q=\lfloor Q\beta\rfloor,\quad
\varphi_Q=\{Q\beta\},\quad
s(Q,K)=E_KQ-KL_Q .
\]

Call \(K\) *admissible at \(Q\)* if \(0\le s(Q,K)\le K\), and let
\(K_{\min}(Q)\) be the least such \(K\).

**Theorem (COST1).** \(K_{\min}(Q)\) exists, satisfies
\(K_{\min}(Q)\le Q\), and \(E_{K_{\min}}/K_{\min}\) is a best approximation
to \(\beta\) **from below**. Consequently \(K_{\min}(Q)\) is the denominator
of a semiconvergent of \(\beta\) lying below \(\beta\).

---

## 2. Proof

**Step 0 (the identity).** For every real \(\beta\) and all \(Q,K\ge1\),

\[
s=K\varphi_Q-Q\{K\beta\} .
\]

Indeed \(K\varphi_Q=KQ\beta-KL_Q\) and \(Q\{K\beta\}=QK\beta-QE_K\);
subtracting gives \(E_KQ-KL_Q\). (Lemma L1 of `general_cost_law.md`.)

**Step 1 (the upper half of the window is vacuous).** \(\beta\) irrational
gives \(\varphi_Q\in(0,1)\). Then

\[
s\le K
\iff
K(\varphi_Q-1)\le Q\{K\beta\},
\]

whose left side is strictly negative and whose right side is nonnegative.
So \(s\le K\) holds **always**, and

\[
\text{admissible}\iff s\ge0 .
\]

*This is a simplification of the manuscript's Theorem E criterion.* The
stated window \(s\in[0,K]\) is correct but not tight: only the lower bound
has content. Logged as a simplification, not a correction.

**Step 2 (reduction to under-approximation).**

\[
s\ge0\iff E_KQ\ge KL_Q\iff \frac{E_K}{K}\ \ge\ \frac{L_Q}{Q} .
\]

Equivalently, since \(\{K\beta\}/K=\beta-E_K/K\), the criterion is
\(\{K\beta\}/K\le\{Q\beta\}/Q\): the fraction \(E_K/K\) under-approximates
\(\beta\) at least as well as \(L_Q/Q\) does. **The map has disappeared
entirely.**

**Step 3 (existence).** \(K=Q\) satisfies \(E_Q/Q\ge L_Q/Q\) with equality.
So the admissible set is nonempty and \(K_{\min}(Q)\le Q\).

**Step 4 (minimality forces a record).** Write \(K^\star=K_{\min}(Q)\). Every
\(K<K^\star\) is inadmissible, so \(E_K/K<L_Q/Q\le E_{K^\star}/K^\star\).
Hence

\[
\frac{E_{K^\star}}{K^\star}>\frac{E_K}{K}\qquad\text{for all }1\le K<K^\star,
\]

i.e. \(K^\star\) is a **strict record** of \(K\mapsto E_K/K\).

**Step 5 (records are best under-approximations).** Since \(\beta\) is
irrational, \(E_K/K<\beta<(E_K+1)/K\); so \(E_K/K\) is the largest fraction
with denominator exactly \(K\) lying below \(\beta\). A record at
\(K^\star\) therefore says that \(E_{K^\star}/K^\star\) is the largest
fraction with denominator **at most** \(K^\star\) lying below \(\beta\) —
which is precisely the definition of a best approximation to \(\beta\) from
below.

**Step 6 (classical input).** The best approximations from below to an
irrational \(\beta\) are exactly the intermediate fractions
(semiconvergents) \(\frac{p_{k-1}+tp_k}{q_{k-1}+tq_k}\), \(1\le t\le
a_{k+1}\), that lie below \(\beta\).

*Reference.* A. Ya. Khinchin, *Continued Fractions*, theory of intermediate
fractions and one-sided best approximation. **Not reproved here**; used as a
known theorem, and checked as an inclusion over ten maps in the verifier.

Combining steps 4-6, \(K_{\min}(Q)\) is a semiconvergent-below denominator.
\(\blacksquare\)

---

## 3. Corollaries

**C1.** \(K_{\min}(Q)\le Q\): refuting at precision \(Q\) never costs more
than \(Q\) witnesses.

**C2.** \(K_{\min}\) is monotone nondecreasing in the order induced by
\(L_Q/Q\), and is piecewise constant, jumping only at semiconvergent
denominators. This is the structure observed in the Collatz data
(\(2,2,2,7,7,12,12,12,53,665,\dots\)) and now explained rather than tabulated.

**C3.** The refutation cost is governed by the *one-sided* approximation
quality of \(\beta\) from below, not by two-sided approximation. For
\(\log_23\) the two nearly coincide, which is why the Collatz sequence looked
like a pure convergent sequence; \(\log_25\) separates them visibly
(\(K_{\min}=1,4,4,16,16,16,28,\dots\) against convergent denominators
\(1,3,28,59,\dots\)).

---

## 4. What is still not proved

**Sufficiency.** COST1 characterises when the closure criterion *can* be
met. It does not construct integer witnesses; that still requires the shadow
of SHG1 plus mining. The criterion is necessary, and a general
witness-construction theorem remains open. This is the single largest gap in
the general track.

---

## 5. Verification

`scripts/verify_cost_law_proof.py` checks each step separately:

- (P) 200-digit decimal floors agree with exact integer floors, and every
  floor evaluation asserts separation \(>10^{-50}\) from an integer;
- (S1) no \((\text{map},Q,K)\) with \(s>K\) — the window is vacuous above;
- (S2) the criterion equivalence, 0 mismatches;
- (S3)/(S4) \(K_{\min}\le Q\) and strict-record property, 110 \((\text{map},Q)\)
  pairs;
- (S5) every record is a best under-approximation;
- (S6) every record is a semiconvergent-below denominator, 10 maps;
- (A) the \((3,2)\) instance reproduces QLG1's pairs and still rejects the
  \((12,53)\) regression.

```bash
python3 scripts/verify_cost_law_proof.py    # ALL PASS
```

---

## 6. Ledger row

| ID | Claim | Status | Source | Verification |
|---|---|---|---|---|
| COST1 | For irrational \(\beta=\log_c a\): admissibility is equivalent to \(\lfloor K\beta\rfloor/K\ge\lfloor Q\beta\rfloor/Q\) (the upper window bound \(s\le K\) is vacuous); \(K_{\min}(Q)\le Q\); and \(K_{\min}(Q)\) is the denominator of a semiconvergent of \(\beta\) lying below \(\beta\) | Proved here (steps 0-5); step 6 is a known theorem applied (Khinchin, one-sided best approximation) | `docs/no-go/cost_law_proof.md` | `scripts/verify_cost_law_proof.py`; supersedes the finite-certificate status of the QLG-GEN cost law; sufficiency (witness construction) still NOT proved |
