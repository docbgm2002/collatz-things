# CONN1: the Suffix Automaton is Strongly Connected

**Building on:** WALK1, SUFF1
**Status:** Proved here — both halves are algebraic. Removes the last
hypothesis from SUFF1, which is now **unconditional for the \(3x+1\) map**.
Machine-checked in `scripts/verify_connectivity.py`.
**Ledger:** CONN1
**License:** CC-BY 4.0

---

## 1. The hub

Let \(m\ge2\) and set

\[
\boxed{\,h_m=3^{-1}\bigl(2^{m-1}-1\bigr)\ \bmod 2^{m}\,}
\]

\(3\) is invertible mod \(2^{m}\) and \(2^{m-1}-1\) is odd, so \(h_m\) exists,
is unique, and is **odd**. By construction \(3h_m+1\equiv2^{m-1}
\pmod{2^{m}}\), hence

\[
v_2(3h_m+1)=m-1<m,
\]

so \(h_m\) is a **live** node carrying the largest possible valuation.

\(h_4=13,\ h_5=5,\ h_6=53,\ h_7=21,\ h_8=213,\ h_9=85,\ h_{10}=853,\dots\)
— alternately \((4^{k}-1)/3\) and its \(11\!\cdot\!(01)^{k}\) companion.

---

## 2. (H1) The hub reaches everything in one step

The successor set of a node with valuation \(e\) is a **full class mod
\(2^{\,m-e}\)** (the quotient \((3r+1)/2^{e}\) is determined mod
\(2^{\,m-e}\); the top \(e\) bits are free). At \(e=m-1\) this is a class
mod \(2^{1}\) — that is, **every odd residue**.

\[
h_m\ \longrightarrow\ \text{all odd residues mod }2^{m}.
\]

---

## 3. (H2) Everything reaches the hub in \(\le m-1\) steps

**Class-growth lemma.** The set reachable from \(r\) in \(k\) steps contains
a full class mod \(2^{\,m-E_k}\), where \(E_k\) is the total valuation along
the path.

*Proof.* Induction. For \(k=1\) the successor set is a class mod
\(2^{\,m-e_1}\). Suppose the reachable set contains a class \(C\) mod
\(2^{\,m-E_k}\). The map \(r\mapsto3r+1\) is an affine injection mod
\(2^{m}\), so it carries \(C\) to a class mod \(2^{\,m-E_k}\); dividing by
\(2^{e}\) gives a class mod \(2^{\,m-E_k-e}\); and each element contributes
its own full class mod \(2^{\,m-e}\). Since \(m-E_k-e\le m-e\), the union is
a full class mod \(2^{\,m-E_k-e}=2^{\,m-E_{k+1}}\). \(\blacksquare\)

Every valuation satisfies \(e_i\ge1\), so \(E_k\ge k\). At \(k=m-1\) the
class is mod \(2^{1}\) — all odd residues — which contains \(h_m\).

**The bound is sharp.** It is attained at the all-ones residue \(2^{m}-1\),
whose burn (TAU1) descends \(\tau=m,m-1,\dots,1\) taking exactly \(m-1\)
steps. Verified for \(m=4,6,8,10,12\); and the measured eccentricity to the
hub is exactly \(m-1\) for every \(m=3..14\).

---

## 4. CONN1

**Theorem.** For every \(m\ge3\) the live subgraph of the mod-\(2^{m}\)
suffix automaton is strongly connected: every live node reaches \(h_m\) in at
most \(m-1\) steps by (H2), and \(h_m\) reaches every live node in one step
by (H1). \(\blacksquare\)

---

## 5. Consequence

SUFF1 was stated conditional on exactly this hypothesis. **It is therefore
unconditional for the \(3x+1\) map:**

> For every \(j\), every admissible \(K\), and every \(m\ge3\), a closed
> quantized-log certificate of length \(K\) exists, with witnesses from
> \(\Theta=m+K+j+\log_2\bigl(1/\min(\varphi_Q,1-\varphi_Q)\bigr)+K/4+O(1)\)
> bits.

Combined with COST1 (which says exactly which \(K\) are admissible, and that
the least is a semiconvergent denominator of \(\log_23\)), the quantized-log
class is now completely settled: **necessary and sufficient, with an explicit
cost.**

The Question posed in `\section{The boundary}` of the manuscript is answered
in full, not merely for the values of \(j\) that were mined.

---

## 6. What this does not close

CONN1 is proved for \(a=3,c=2\). The general \((a,b,c)\) form needs the
analogous hub \(h=a^{-1}(c^{\,m-1}-1)\bmod c^{m}\), which exists whenever
\(\gcd(a,c)=1\) — the argument should transfer verbatim, but it is not
written here.

---

## 7. Verification

```bash
python3 scripts/verify_connectivity.py     # ALL PASS
```

---

## 8. Ledger row

| ID | Claim | Status | Source | Verification |
|---|---|---|---|---|
| CONN1 | The mod-\(2^m\) suffix automaton is strongly connected for every \(m\ge3\), via the explicit hub \(h_m=3^{-1}(2^{m-1}-1)\bmod2^m\): \(v_2(3h_m+1)=m-1\) so \(h_m\) reaches all odd residues in one step, and the class-growth lemma gives every live node a path to \(h_m\) in \(\le m-1\) steps (sharp, attained at \(2^m-1\)). **Removes the last hypothesis from SUFF1** | Proved here | `docs/no-go/connectivity.md` | `scripts/verify_connectivity.py`; general \((a,b,c)\) hub not written |
