# TAU1: the τ-Coupling Dissolves

**Building on:** `docs/no-go/sufficiency_reduction.md` (CARRY1, FREE1, WALK1);
RUNLEN2 and the burn identity (MER1, Andaloro 2000)
**Status:** Proved here. Machine-checked in `scripts/verify_tau_coupling.py`.
Removes one of the two remaining obstacles to SUFF1; **SUFF1 is still OPEN**,
now down to a single uniformity statement (§5).
**Ledger:** TAU1
**License:** CC-BY 4.0

---

## 1. The obstacle, as stated

`sufficiency_reduction.md` §6 identified the residual gap as a coupling:
\(\tau(f(x_i))\) depends on the top bits of \(f(x_i)\), which are pinned by
the *cell* choice for \(x_i\), while \(\tau(x_{i+1})\) is pinned by the
*residue walk*. Making them agree looked like a genuine constraint.

It is not. \(\tau\) is not an independent coordinate at all.

---

## 2. Three facts

For odd \(x\) write \(\tau(x)=v_2(x+1)\) and \(e(x)=v_2(3x+1)\).

**(T1)** \(\tau(x)\ge2\iff e(x)=1\), and \(\tau(x)=1\iff e(x)\ge2\).

*Proof.* \(x\equiv3\pmod4\Rightarrow3x+1\equiv2\pmod4\); \(x\equiv1\pmod4
\Rightarrow4\mid3x+1\). \(\blacksquare\)

**(T2) Burn identity.** If \(e(x)=1\) then \(\tau(f(x))=\tau(x)-1\).

*Proof.* Write \(x=2^{t}-1+2^{t+1}k\) with \(t=\tau(x)\ge2\). Then
\(3x+1=2\bigl(3\cdot2^{t-1}-1+3\cdot2^{t}k\bigr)\), so
\(f(x)+1=3\cdot2^{t-1}(1+2k)\) and \(v_2(f(x)+1)=t-1\). \(\blacksquare\)

**(T3)** If \(e(x)\ge2\) then \(\tau(x)=1\) and \(\tau(f(x))\) is
unconstrained: for every \(t\ge1\) there is such an \(x\).

*Proof.* Solve \(3x+1=2^{e}y\) with \(y\equiv2^{t}-1\pmod{2^{t+1}}\);
\(e=2\) suffices, and the congruence \(2^{e}y\equiv1\pmod3\) is solvable.
Explicit witnesses for \(t=1,\dots,30\) are produced by the verifier
(\(t=5\to x=41\), \(t=12\to x=27305\)). \(\blacksquare\)

---

## 3. TAU1

**Theorem (TAU1).** Along any orbit the \(\tau\)-word is determined by the
\(e\)-word together with one free choice at each \(e\ge2\) step. Maximal runs
of \(e=1\) have length exactly \(\tau-1\) (RUNLEN2), and each payout resets
\(\tau\) freely. Consequently, for a cyclic \(e\)-word,

\[
\text{the }\tau\text{-closure is satisfiable}
\iff
\text{the }e\text{-word has at least one step with }e\ge2,
\]

and that is **automatic**, since \(\sum e_i=\lfloor K\log_23\rfloor\ge K+1\)
for \(K\ge2\).

So \(\tau\) imposes no constraint beyond the \(e\)-word. The coupling of
§6 does not exist.

---

## 4. Two confirmations

**The certificates.** All six re-mined certificates satisfy the burn identity
on every \(e=1\) edge and close in \(\tau\) at every junction.

**The WALK1 travel path is a burn.** The construction's connector
\(15\to7\to11\to1\) carries \(\tau=4,3,2,1\) — it is precisely a maximal
\(e=1\) run descending to a payout, exactly as (T2) requires. Residues
\(1\) and \(9\) both have \(\tau=1\), \(e\ge2\): payout residues where
\(\tau\) resets. The automaton construction and the \(\tau\)-structure were
derived independently and agree.

The cost is explicit: \(a\) consecutive self-loops at \(15\) need
\(\tau\ge a+4\) at entry, hence a witness of at least \(a+4\) bits. For
\(K=53\) that is \(\tau\ge23\); the verifier exhibits the run.

---

## 5. What remains for SUFF1

One statement, and it is uniformity rather than structure:

> Each witness needs (class mod \(2^{M}\)) ∩ (sub-interval of its cell), with
> \(M=\max(m,\tau_{\max}+1)\le\max(m,K+1)\). Existence for a **single** edge
> is the elementary count of `sufficiency_reduction.md` §4. The composition
> requires **one height to serve all \(K\) edges simultaneously**.

The cells differ by bounded factors around the cycle, so this is plausible,
but it is not written out. **SUFF1 remains open.**

---

## 6. A correction worth recording

The first draft of (T3) tested "does \(\tau(f(x))\) attain every value" by
scanning \(x<2\cdot10^{5}\). It **failed at \(t=16\)** — not because the
claim is false, but because high \(\tau\) is exponentially rare (observed
counts halve with \(t\): 25004, 12496, 6254, …). A bounded scan is the wrong
instrument for an existential claim. Replaced by direct construction. Logged
in `CLAIM_LEDGER.md`.

---

## 7. Verification

```bash
python3 scripts/verify_tau_coupling.py     # ALL PASS
```

---

## 8. Ledger row

| ID | Claim | Status | Source | Verification |
|---|---|---|---|---|
| TAU1 | \(\tau(x)\ge2\iff e=1\); \(e=1\Rightarrow\tau(f(x))=\tau(x)-1\); \(e\ge2\Rightarrow\tau(x)=1\) with \(\tau(f(x))\) attaining every value. Hence the \(\tau\)-word is a function of the \(e\)-word plus free payout choices, and \(\tau\)-closure of a cycle is automatic whenever some \(e_i\ge2\) — which holds since \(\sum e_i=\lfloor K\log_23\rfloor\ge K+1\). The \(\tau\)-coupling identified as blocking SUFF1 does not exist | Proved here | `docs/no-go/tau_coupling.md` | `scripts/verify_tau_coupling.py`; consistent with RUNLEN2 and the burn identity (Andaloro 2000) |
