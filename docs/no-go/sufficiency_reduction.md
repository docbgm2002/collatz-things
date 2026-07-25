# Toward SUFF1: the Carry Lemma and the Sufficiency Reduction

**Building on:** `docs/no-go/cost_law_proof.md` (COST1),
`docs/no-go/quantized_log_witnesses.md` (WITN1)
**Status:** CARRY1, FREE1, WALK1 proved here. **SUFF1 itself remains OPEN**,
now reduced to a single coupling statement (§6). Machine-checked in
`scripts/verify_sufficiency_reduction.py`.
**Ledger:** CARRY1, WALK1
**License:** CC-BY 4.0

---

## 1. What s actually is

The most useful thing found here is an interpretation. Write \(Q=2^{j}\),
\(L_Q=\lfloor Q\log_23\rfloor\), \(\varphi_Q=\{Q\log_23\}\). For odd \(x\)
with cell \(C=\lfloor Q\log_2x\rfloor\) and in-cell position
\(u=Q\log_2x-C\in[0,1)\), and \(e=v_2(3x+1)\):

\[
Q\log_2f(x)=C+u+L_Q+\varphi_Q-Qe+Q\varepsilon,
\qquad \varepsilon=\log_2\Bigl(1+\tfrac1{3x}\Bigr),
\]

so the cell displacement is

\[
\lfloor Q\log_2f(x)\rfloor-C=L_Q-Qe+\delta,
\qquad
\delta=\lfloor u+\varphi_Q+Q\varepsilon\rfloor .
\]

**Theorem (CARRY1).** Under the height hypothesis

\[
x\ \ge\ \frac{Q}{3\ln2\,(1-\varphi_Q)}
\tag{H}
\]

we have \(\delta\in\{0,1\}\), with \(\delta=1\) exactly when \(u\) lies in
the top \(\varphi_Q\)-fraction of its cell. Consequently, around a closed
\(K\)-cycle the cells return and

\[
\sum_{i=1}^{K}\delta_i \;=\; QE-KL_Q \;=\; s .
\]

**So \(s\) is the number of carrying edges.** The manuscript's criterion
\(s\in[0,K]\) is exactly the statement that this is a legal count — which
is why (COST1, step 1) the upper bound is vacuous.

*Verified:* \(\sum\delta_i=s\) on all six re-mined certificates, with every
\(\delta_i\in\{0,1\}\).

### (H) is necessary — a correction

An earlier draft of CARRY1 omitted (H). It is **false** without it:
\(\delta=2\) requires \(u\ge2-\varphi_Q-Q\varepsilon\), possible with
\(u<1\) exactly when \(Q\varepsilon>1-\varphi_Q\), and \(Q\varepsilon\) is
large for small \(x\) at large \(j\) (at \(j=6\), \(x=3\) gives
\(Q\varepsilon\approx9.7\)). The verifier now checks both that \(\delta\le1\)
above the threshold (270{,}000 edges, zero violations) and that violations
**do** occur below it, so the hypothesis is not decorative. Logged in
`CLAIM_LEDGER.md`.

---

## 2. Position freedom (FREE1)

At a junction, \(x_{i+1}\) and \(f(x_i)\) are **distinct integers** required
only to share a coordinate. The in-cell position of \(x_{i+1}\) is therefore
*not* determined by edge \(i\) and may be chosen freely. Both targets —
\(u\in[0,1-\varphi_Q)\) for a non-carrying edge and \(u\in[1-\varphi_Q,1)\)
for a carrying one — are nonempty precisely because \(0<\varphi_Q<1\), i.e.
because \(\log_23\) is irrational (DICH1).

**So the archimedean half of the cycle is unobstructed:** choose any \(s\) of
the \(K\) edges to carry.

---

## 3. The arithmetic half (WALK1)

The remaining constraints are 2-adic: the residues must chain, and the
valuations must sum to \(E=\lfloor K\log_23\rfloor\).

**Theorem (WALK1).** The mod-16 suffix automaton admits a closed walk of
length \(K\) and total valuation exactly \(\lfloor K\log_23\rfloor\) for
every \(K\ge2\).

*Proof for \(K\ge5\), constructive.* The automaton has self-loops
\(15\to15\) of weight \(1\) and \(1\to1\) of weight \(2\), joined by
\(15\to7\to11\to1\) (length 3, weight 3) and \(1\to9\to15\) (length 2,
weight 4). Taking \(a\) loops at \(15\) and \(b\) loops at \(1\) gives a
closed walk of length \(a+b+5\) and weight \(a+2b+7\). Solving,

\[
b=\lfloor K\log_23\rfloor-K-2,
\qquad
a=2K-\lfloor K\log_23\rfloor-3 .
\]

\(b\ge0\) because \(\log_23>1\); \(a\ge0\) because \(\log_23<2\). Both hold
for \(K\ge5\). \(\blacksquare\)

\(K=2,3,4\) are checked by direct search.

**The mechanism is exactly \(1<\log_23<2\)** — self-loop weights straddling
the log-ratio. For a general map this is the condition that the automaton
carry self-loops of weight \(\lfloor\log_ca\rfloor\) and
\(\lceil\log_ca\rceil\) in one strongly connected component.

---

## 4. The counting bound

A witness must lie in a prescribed sub-interval of its cell **and** a
prescribed class mod \(2^{m}\). The sub-interval has multiplicative width at
least \(2^{\min(\varphi_Q,1-\varphi_Q)/Q}\), so it contains roughly
\(x\ln2\min(\varphi_Q,1-\varphi_Q)/Q\) integers, and meets a class mod
\(2^{m+e}\) once

\[
\log_2x\ \gtrsim\ m+e+j+\log_2\frac1{\min(\varphi_Q,1-\varphi_Q)} .
\]

Finite for each fixed \(Q\), and the same \(1/(1-\varphi_Q)\) factor that
appears in (H). Consistent with the observed height law of WITN1 (first
certificate in window \(2^{\,j+6}\)).

---

## 5. Status

| piece | status |
|---|---|
| \(s\) counts carrying edges (CARRY1) | **proved** (under (H)) |
| archimedean positions freely choosable (FREE1) | **proved** |
| residue walk with correct total valuation (WALK1) | **proved** (m=4, all \(K\)) |
| counting bound for a single witness | **proved** (elementary) |
| joint realisation (SUFF1) | **OPEN** |

---

## 6. The one remaining gap

\(\tau(f(x_i))\) depends on the top bits of \(f(x_i)\), which are pinned by
the *cell* choice for \(x_i\); \(\tau(x_{i+1})\) is pinned by the *residue
walk*. Making these agree simultaneously with the sub-interval and residue
constraints is not established here. That single coupling is now all that
separates the reduction from a proof of SUFF1.

It is plausibly removable by enlarging \(m\) so that \(\tau\) is always read
inside the determined bits, at the cost of a larger automaton — but the
automaton's successor sets lose \(e\) bits per step, so this needs an
argument, not an assertion.

---

## 7. Verification

```bash
python3 scripts/verify_sufficiency_reduction.py     # ALL PASS
```

---

## 8. Ledger rows

| ID | Claim | Status | Source | Verification |
|---|---|---|---|---|
| CARRY1 | Under (H), the quantized-log cell displacement is \(L_Q-Qe+\delta\) with \(\delta\in\{0,1\}\), \(\delta=1\) iff the in-cell position is in the top \(\varphi_Q\)-fraction; around a closed cycle \(\sum\delta_i=s\), so \(s\) counts carrying edges | Proved here | `docs/no-go/sufficiency_reduction.md` | `scripts/verify_sufficiency_reduction.py`; (H) shown necessary |
| WALK1 | The mod-16 suffix automaton admits a closed walk of length \(K\) with total valuation exactly \(\lfloor K\log_23\rfloor\) for every \(K\ge2\); constructive for \(K\ge5\) from self-loops of weight 1 and 2 in one SCC, the mechanism being \(1<\log_23<2\) | Proved here | `docs/no-go/sufficiency_reduction.md` | `scripts/verify_sufficiency_reduction.py` |
