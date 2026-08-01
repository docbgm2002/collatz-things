# SUFF1: Sufficiency, Composed

**Building on:** CARRY1, FREE1, WALK1 (`sufficiency_reduction.md`), TAU1
(`tau_coupling.md`), UNIF1 and SUFF-32 (`uniformity.md`), COST1
(`cost_law_proof.md`)
**Status:** Proved for every \(j\), every admissible \(K\), and every \(m\)
for which the mod-\(2^m\) automaton is strongly connected — **verified for
\(m=3..14\)**. Strong connectivity for all \(m\) is **not proved**; that one
graph-theoretic statement is what remains. Machine-checked in
`scripts/verify_suff1_composition.py`.
**Ledger:** SUFF1
**License:** CC-BY 4.0

---

## 1. Statement

Let \(Q=2^{j}\), \(\beta=\log_23\), \(L_Q=\lfloor Q\beta\rfloor\),
\(\varphi_Q=\{Q\beta\}\), \(E=\lfloor K\beta\rfloor\), and let \(K\) be
admissible: \(s=QE-KL_Q\in[0,K]\).

**Theorem (SUFF1).** Suppose the mod-\(2^{m}\) suffix automaton is strongly
connected on its live nodes. Then there exist \(K\) distinct odd integers
forming a closed cycle in

\[
C(x)=\bigl(\lfloor Q\log_2x\rfloor,\ \tau(x),\ x\bmod2^{m}\bigr)
\]

with strict gain — so no potential \(\log_2x+g(C(x))\) is nonincreasing. All
witnesses may be taken of bit-length at least

\[
\Theta=m+K+j+\log_2\frac1{\min(\varphi_Q,1-\varphi_Q)}+\tfrac14K+O(1).
\]

---

## 2. Proof

**(1) The \(e\)-word and residues.** By WALK1 the automaton has a self-loop of
weight 1 at \(2^{m}-1\) and of weight 2 at \(1\). These are now *identities*,
not searches:

\[
3(2^{m}-1)+1=2\bigl(3\cdot2^{m-1}-1\bigr)
\Rightarrow e=1,\ \ \mathrm{succ}=\{2^{m-1}-1,\ 2^{m}-1\},
\]
\[
3\cdot1+1=4\Rightarrow e=2,\ \ \mathrm{succ}=\{1+t2^{m-2}:t=0..3\}\ (m\ge3).
\]

By strong connectivity they lie in one component, so taking \(a\) loops at
\(2^{m}-1\) and \(b\) loops at \(1\) plus the connecting paths gives a closed
walk of length \(K\) and total valuation \(E\), with
\(b=E-K-O(1)\ge0\) because \(\beta>1\) and \(a=2K-E-O(1)\ge0\) because
\(\beta<2\). Fix its residues \(r_1..r_K\) and valuations \(e_1..e_K\).

**(2) The \(\tau\)-word.** By TAU1, \(\tau\) is a function of the \(e\)-word
plus a free choice at each payout: it descends by 1 on each \(e=1\) step and
resets arbitrarily at each \(e\ge2\) step. The \(a\)-run at \(2^{m}-1\) needs
\(\tau\ge m+a\) at entry, which a payout supplies (T3). So
\(\tau_{\max}\le m+K\), and every witness constraint is a single congruence
modulo \(2^{M}\) with \(M\le m+K+1\).

**(3) The carry pattern.** Choose any \(s\) of the \(K\) edges to carry. By
CARRY1 the cell displacements are \(L_Q-Qe_i+\delta_i\) and sum to
\(KL_Q-QE+s=0\), so the cells close. By FREE1 the required in-cell
sub-intervals are nonempty, since \(0<\varphi_Q<1\).

**(4) Height.** By UNIF1 the cells dip at most \(\tfrac14QK+O(Q)\) below
\(C_1\). Choose \(C_1/Q\ge\Theta\). Each sub-interval then holds at least
\(2^{\Theta-\frac14K}\min(\varphi_Q,1-\varphi_Q)\ln2/Q>2^{M}\) integers, so it
meets the class mod \(2^{M}\) — in fact in at least two integers, giving
distinctness.

**(5) Gain.** With \(y_i=(3x_i+1)/2^{e_i}\),

\[
\frac{\prod y_i}{\prod x_i}
=\frac{3^{K}}{2^{E}}\prod_i\Bigl(1+\frac1{3x_i}\Bigr)
>\frac{3^{K}}{2^{E}}>1,
\]

the last step because \(E=\lfloor K\beta\rfloor\) gives \(3^{K}>2^{E}\).
**No estimate of any \(\varepsilon\) is needed anywhere** — a simplification
over the manuscript's Theorem E(b), whose hypothesis \(\sum\varepsilon_i<1\)
is not required for sufficiency.

Summing the \(K\) monotonicity constraints cancels every \(g\)-term by (3) and
contradicts (5). \(\blacksquare\)

---

## 3. Explicit heights

| \(j\) | \(K\) | \(m\) | witnesses suffice from |
|---|---|---|---|
| 3 | 2 | 4 | 16 bits |
| 3 | 12 | 4 | 28 bits |
| 5 | 53 | 6 | 84 bits |
| 8 | 665 | 8 | 854 bits |
| 12 | 665 | 8 | 863 bits |

At \((j,K,m)=(3,2,4)\) the bound gives 16 bits; SUFF-32 exhibits the family
from 11 bits, so the bound is correct but not tight.

---

## 4. What is not proved

**Strong connectivity of the mod-\(2^{m}\) automaton for all \(m\).**
Verified for \(m=3..14\) (up to 8191 live nodes). The self-loops are proved
for all \(m\); only their being joined is verified. This is a finite-graph
statement about the map \(r\mapsto(3r+1)/2^{v_2(3r+1)}\) on odd residues, and
is the last remaining item.

Also: the composition is stated for \(\beta=\log_23\). The general
\((a,b,c)\) form should follow with \(\lfloor\log_ca\rfloor\) and
\(\lceil\log_ca\rceil\) replacing 1 and 2 in step (1), but is not written.

---

## 5. Verification

```bash
python3 scripts/verify_suff1_composition.py    # ALL PASS
```

(A) self-loop closed forms, \(m=3..20\); (B) strong connectivity, \(m=3..14\);
(C) walk availability over 528 admissible \((m,j,K)\) triples; (D)
\(3^{K}>2^{E}\) for \(K\le799\); (E) finiteness of \(\Theta\).

---

## 6. Ledger row

| ID | Claim | Status | Source | Verification |
|---|---|---|---|---|
| SUFF1 | For every \(j\), every admissible \(K\), and every \(m\) with the mod-\(2^m\) automaton strongly connected: a closed quantized-log certificate of length \(K\) exists, with witnesses from \(\Theta=m+K+j+\log_2(1/\min(\varphi_Q,1-\varphi_Q))+K/4+O(1)\) bits. Strict gain is automatic from \(3^K>2^{\lfloor K\log_23\rfloor}\); no \(\varepsilon\) hypothesis is needed | Proved here, conditional on strong connectivity (**verified \(m=3..14\), not proved in general**) | `docs/no-go/suff1.md` | `scripts/verify_suff1_composition.py`; self-loops proved for all \(m\ge3\); general \((a,b,c)\) form not written |
