# WITN1: Re-mined Quantized-Log Certificates, and the Sufficiency Gap

**Building on:** `docs/no-go/cost_law_proof.md` (COST1), manuscript §6 / QLG1
**Status:** Finite certificate (the certificates themselves, exactly verified)
plus an **exploratory** height law. Sufficiency is **not proved**.
Machine-checked in `scripts/verify_quantized_log_witnesses.py`.
**Ledger:** WITN1
**License:** CC-BY 4.0

---

## 1. Why

COST1 settles when the quantized-log closure criterion *can* be met. It says
nothing about whether integer witnesses realising it exist — that is the
sufficiency half, and it is the largest hole in the general track.

Separately, the original §6 mining and verification scripts are not in the
repository. Rather than restore an unreviewed copy, certificates were
**re-mined from scratch** by a different method and confirmed exactly.

---

## 2. What a certificate is

Fix \(Q=2^{j}\) and modulus \(m\). The coordinate is

\[
C(x)=\bigl(\lfloor Q\log_2x\rfloor,\ \tau(x),\ x\bmod m\bigr).
\]

A certificate is odd \(x_1,\dots,x_K\) with \(y_i=f(x_i)\) satisfying

\[
C(y_i)=C(x_{i+1})\ \ (i\bmod K),
\qquad
\prod_i y_i>\prod_i x_i .
\]

Summing the \(K\) monotonicity constraints cancels every \(g\)-term by
closure and leaves \(\prod y_i\le\prod x_i\), contradicting the gain. Note
the witnesses are **distinct integers**, not one orbit: each junction resets
the position inside the quantized-log cell, which is exactly how multi-witness
cycles evade the single-chain bound.

---

## 3. Method

Negative-cycle detection on the coordinate digraph: one node per realised
coordinate, one edge \(C(x)\to C(f(x))\) of weight \(\log x-\log f(x)\). A
negative cycle is a certificate. Bellman–Ford finds one; **floats are used for
guidance only**, and every promoted claim is re-checked in exact integers.

This realises the method sketched for the planned
`scripts/verify_nogo_certificate.py` in the README — no-go constraint systems
are difference-constraint systems, infeasible exactly when the coordinate
graph carries a cycle of ratio-product \(>1\).

**Exactness of the quantized log.** For integer \(Q\),
\(\lfloor Q\log_2x\rfloor=\mathrm{bitlen}(x^{Q})-1\). No logarithm is
evaluated numerically anywhere in the verification.

---

## 4. Certificates

All verified exactly: closure at every junction, strict gain as an integer
comparison of \(\prod y_i\) against \(\prod x_i\), distinct witnesses, and
\(K\) admissible under COST1.

| \(j\) | \(K\) | window | first witness | \(s\) | gain |
|---|---|---|---|---|---|
| 3 | 2  | \(2^{9}\)  | 953   | 0 | 1.125956 |
| 4 | 7  | \(2^{10}\) | 1529  | 1 | 1.069694 |
| 5 | 12 | \(2^{11}\) | 2203  | 8 | 1.015067 |
| 6 | 31 | \(2^{12}\) | 5387  | 5 | 1.099226 |
| 7 | 12 | \(2^{13}\) | 13305 | 8 | 1.014002 |
| 8 | 53 | \(2^{14}\) | 17243 | 39 | 1.002877 |

Witnesses are stored in `scripts/certificates_quantized_log_remined.json`.

The smallest, fully explicit at \(j=3\), \(m=16\):

\[
4123\mapsto6185,\qquad 5817\mapsto4363,
\]
with \(C(6185)=C(5817)=(100,1,9)\), \(C(4363)=C(4123)=(96,2,11)\), and
\(6185\cdot4363=26\,985\,155>23\,983\,491=4123\cdot5817\).

**Relation to QLG1.** These are independent certificates at
\(j\in\{3,\dots,8\}\), not the published ones. They **corroborate** QLG1's
claim for \(j\le8\) and do not reach \(j\in\{9,12,14\}\). QLG1's status is
unchanged; its own witnesses remain uncommitted.

---

## 5. The height law — exploratory

A counting heuristic predicts where witnesses must first appear. The cell
\(\lfloor Q\log_2x\rfloor=C\) is an interval of multiplicative width
\(2^{1/Q}\), containing about \(x\ln2/Q\) integers. An edge additionally
prescribes \(x\) modulo \(2^{\,m+e}\). Such a residue class is met once

\[
\frac{x\ln2}{Q}\gtrsim2^{\,m+e}
\qquad\text{i.e.}\qquad
\log_2x\ \gtrsim\ m+e+j .
\]

**Observed:** the first window containing a verified certificate is
\(2^{\,j+6}\) for every \(j\in\{3,\dots,8\}\) — the offset is *constant*, so
the slope in \(j\) is exactly the predicted 1.

This is **evidence, not proof**. It is labelled exploratory and no
unbounded claim is made from it.

---

## 6. What sufficiency would require

The counting argument above is not yet a theorem because the edge constraint
is finer than "residue class ∩ cell": the *outgoing* cell is fixed too, which
restricts \(x\) to a sub-interval of the cell whose relative width depends on
\(\varphi_Q=\{Q\log_23\}\). A proof needs:

1. a lower bound on that sub-interval's width, uniform around the cycle —
   this is where COST1's criterion should enter, since \(s\ge0\) is precisely
   the statement that the required sub-intervals are simultaneously nonempty;
2. the elementary count above, applied at height \(\log_2x\gtrsim m+e+j\);
3. control of \(e=v_2(3x+1)\), which is itself a congruence condition and so
   composes with (2).

None of these needs deep input. The obstruction is bookkeeping, not
mathematics, which makes **SUFF1** the most promising open target in the
general track.

---

## 7. Verification

```bash
python3 scripts/verify_quantized_log_witnesses.py    # ALL PASS
```

Checks the bit-length identity against \(2^n\le x^{Q}<2^{n+1}\); then for each
\(j\): witness count, oddness, closure at all \(K\) junctions, strict gain as
an exact integer comparison, distinctness, and COST1-admissibility of \(K\);
then the constancy of window − \(j\).

---

## 8. Ledger row

| ID | Claim | Status | Source | Verification |
|---|---|---|---|---|
| WITN1 | Independently re-mined quantized-log certificates for \((j,m)=(3,16),(4,16),(5,16),(6,16),(7,16),(8,16)\), each closing exactly and with strict integer gain, refuting \(\log_2x+g(\lfloor2^{j}\log_2x\rfloor,\tau,x\bmod16)\) for \(j\le8\). The first window containing a certificate is \(2^{\,j+6}\) throughout (**exploratory**) | Finite certificate; height law exploratory | `docs/no-go/quantized_log_witnesses.md` | `scripts/verify_quantized_log_witnesses.py`; corroborates but does not replace QLG1; sufficiency (SUFF1) NOT proved |
