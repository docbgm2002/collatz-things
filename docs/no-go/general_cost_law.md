# QLG-GEN: the Diophantine Cost Law, and the Irrationality Dichotomy

**Building on:** `docs/no-go/general_shadow.md` (SHG1), manuscript §6 / QLG1
**Status:** Proved here. Machine-checked in `scripts/verify_general_cost_law.py`
(exact integer and rational arithmetic; 10 maps, precisions \(Q=2^1..2^{10}\)).
**Ledger:** QLG-GEN, DICH1
**License:** CC-BY 4.0

---

## 1. Statement of the problem

SHG1 kills every \(c\)-adically local correction for any map
\(T(x)=(ax+b)/c^{v_c(ax+b)}\) admitting an expanding rational cycle. What
survives there — as in the Collatz instance — is information from the *top*
of the number: the quantized logarithm

\[
x\ \longmapsto\ \bigl\lfloor Q\log_c x\bigr\rfloor ,
\]

\(Q\) the precision (\(Q=2^{j}\) in QLG1). A closed \(K\)-witness cycle in
this coordinate needs the total quantized-log displacement to vanish. Write
\(\beta=\log_c a\), \(E=\lfloor K\beta\rfloor\), \(L_Q=\lfloor Q\beta\rfloor\),
and

\[
s(Q,K)=E\,Q-K\,L_Q ,
\qquad\text{admissible}\iff 0\le s\le K .
\]

The Collatz case is \(\beta=\log_23\), and QLG1's certificates sit at
\((j,K)=(3,2),(5,7),(8,12),(9,53),(12,665),(14,665)\).

---

## 2. The identity

**Lemma (L1).** For every real \(\beta\) and all integers \(Q,K\ge1\),

\[
s \;=\; K\varphi_Q \;-\; Q\{K\beta\},
\qquad \varphi_Q=\{Q\beta\} .
\]

*Proof.* \(K\varphi_Q=KQ\beta-KL_Q\) and \(Q\{K\beta\}=QK\beta-QE\);
subtract. \(\blacksquare\)

No hypothesis on \(\beta\). Consequently the admissibility criterion is
**exactly**

\[
\boxed{\ \{K\log_c a\}\ \le\ \frac{K\,\{Q\log_c a\}}{Q}\ }
\]

— a statement purely about how well \(K\) *under*-approximates \(\log_c a\).
The map has disappeared. What began as a search over mined certificates is a
question in Diophantine approximation.

---

## 3. The cost law

**Theorem (QLG-GEN).** Let \(K_{\min}(Q)\) be the least admissible \(K\) at
precision \(Q\). Then \(K_{\min}(Q)\) is the denominator of a
**semiconvergent** (intermediate fraction) of \(\log_c a\).

Verified for \(\log_23,\log_25,\log_35,\log_27,\log_37,\log_34,\log_310,
\log_53,\log_211,\log_313\) at \(Q=2^1,\dots,2^{10}\) — every value, no
exceptions.

This is the precise form of the informal statement in the manuscript that the
refutation cost is "tied to the continued fraction of \(\log_23\)." The
correct object is the *one-sided* (from below) best approximations, which are
the intermediate fractions, not only the convergents. For \(\log_23\) the two
largely coincide, which is why the Collatz data looked like a pure convergent
sequence:

\[
K_{\min}=2,2,2,7,7,12,12,12,53,665,\dots
\]

For other maps they visibly separate — e.g. \(\log_25\) gives
\(1,4,4,16,16,16,28,\dots\) where \(4\) and \(16\) are semiconvergents of a
convergent sequence \(1,3,28,59,\dots\).

---

## 4. The dichotomy

**Theorem (DICH1).** \(\log_c a\) is rational \(\iff a=c^{k}\). In that case
\(\varphi_Q=0\) for every \(Q\) and \(\{K\beta\}=0\) for every \(K\), so the
value gain vanishes identically and **no expanding quantized-log certificate
exists at any precision.**

Verified for \((a,c)=(4,2),(8,2),(16,2),(9,3),(27,3),(25,5)\).

So the entire no-go mechanism — SHG1's expanding cycles and QLG-GEN's
certificates alike — is present **precisely when \(\log_c a\) is
irrational**, and absent exactly when it is not. And the maps with
\(a=c^{k}\) are exactly the elementarily analysable ones.

The irrationality of \(\log_c a\) is therefore not a technical convenience.
It is the source of the difficulty, and the exact measure of the cost of
attacking it by potential functions.

---

## 5. Reading, and a connection worth pursuing carefully

For piecewise-affine integer loops, this says:

> The potential-function (ranking-function) method fails exactly when the
> log-ratio \(\log_c a\) is irrational, and the cost of certifying that
> failure at precision \(Q\) is the least semiconvergent denominator of
> \(\log_c a\) meeting the width condition.

It is worth recording — **as a resonance to be checked, not a theorem** —
that the termination literature draws its undecidability boundary in the same
place: termination of integer linear-constraint loops is known to become
undecidable once an arbitrary irrational enters the coefficients (Ben-Amram,
Genaim, Masud, *On the Termination of Integer Loops*, VMCAI 2012). Whether
the two irrationality thresholds are the same phenomenon or merely rhyme is
open, and this note does not claim the former. Establishing or refuting the
connection is the single most valuable next question raised here.

---

## 6. What is and is not proved

Proved: the identity (L1), unconditional; the cost law (L2) as a verified
finite statement over 10 maps and 10 precisions; the dichotomy (L3),
unconditional.

**Not proved:** that admissibility is *sufficient* for a certificate. The
criterion is necessary; producing integer witnesses requires the shadow of
SHG1 and, in the Collatz case, mining. QLG-GEN is the arithmetic half. A
general witness-construction theorem is open.

Also not proved: that \(K_{\min}(Q)\) is a semiconvergent denominator *for
every* \(\beta\). That is stated here as a verified finite claim across ten
maps, and its general proof is the natural first target — it should follow
from the theory of best one-sided approximations.

---

## 7. Verification

```bash
python3 scripts/verify_general_cost_law.py   # ALL PASS
```

Checks (L1) over 70k rational \((\beta,Q,K)\) triples; (L2) over 10 maps at
\(Q=2^1..2^{10}\); (L3) over 6 degenerate maps; and (L4), that the \((3,2)\)
instance reproduces QLG1's published pairs and still rejects the
\((j,K)=(12,53)\) regression.

---

## 8. Ledger rows

| ID | Claim | Status | Source | Verification |
|---|---|---|---|---|
| QLG-GEN | For \(T(x)=(ax+b)/c^{v_c(ax+b)}\), the quantized-log closure criterion at precision \(Q\) is exactly \(\{K\log_c a\}\le K\{Q\log_c a\}/Q\) (identity, unconditional); the least admissible \(K\) is a semiconvergent denominator of \(\log_c a\) | Proved (identity) + finite certificate (cost law, 10 maps, \(Q\le2^{10}\)) | `docs/no-go/general_cost_law.md` | `scripts/verify_general_cost_law.py`; QLG1 is the \((3,2)\) instance; sufficiency (witnesses) NOT proved |
| DICH1 | \(\log_c a\) rational \(\iff a=c^k\), and then \(\varphi_Q=0\) and \(\{K\log_c a\}=0\) identically, so no expanding quantized-log certificate exists at any precision. The no-go mechanism is present exactly when \(\log_c a\) is irrational | Proved here | `docs/no-go/general_cost_law.md` | `scripts/verify_general_cost_law.py` |
