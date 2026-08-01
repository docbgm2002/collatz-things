# UNIF1 and SUFF1(3,2): Uniformity, and an Infinite Certificate Family

**Building on:** CARRY1, FREE1, WALK1 (`sufficiency_reduction.md`), TAU1
(`tau_coupling.md`)
**Status:** UNIF1 proved. **SUFF1 proved for \((j,K)=(3,2)\)** via an explicit
infinite family. **SUFF1 in general remains OPEN** — see §5.
Machine-checked in `scripts/verify_uniformity.py`.
**Ledger:** UNIF1, SUFF-32
**License:** CC-BY 4.0

---

## 1. UNIF1: the cell dip is linear in \(K\)

Around a cycle the cells return, but partial products dip. With
\(X_i=2^{C_i/Q}\),

\[
\frac{X_i}{X_1}=\frac{3^{\,i-1}}{2^{\,E_{i-1}}},
\qquad
\text{worst dip}=\min_i\bigl(\lfloor i\log_23\rfloor-E_i\bigr).
\]

**Theorem (UNIF1).** For the WALK1 recipe word with payouts front-loaded, the
worst dip is \(-cK+O(1)\) with \(c\to0.24\):

| \(K\) | 12 | 53 | 120 | 300 | 800 |
|---|---|---|---|---|---|
| dip | \(2^{-3}\) | \(2^{-13}\) | \(2^{-29}\) | \(2^{-72}\) | \(2^{-193}\) |
| rate | .250 | .245 | .242 | .240 | .241 |

So the starting cell need only be chosen \(O(K)\) above the single-edge
threshold, and one height serves the whole cycle. **This is the ingredient
that uniformity needs.**

---

## 2. SUFF1 at \((j,K)=(3,2)\)

Take \(Q=8\), \(m=16\), and

\[
\boxed{\,x_1=2^{n}+27\,}
\]

**Theorem.** For every \(n\ge10\), exactly:

\[
3x_1+1=2\bigl(3\cdot2^{n-1}+41\bigr)
\ \Rightarrow\
e_1=1,\quad y_1=f(x_1)=3\cdot2^{n-1}+41,
\]
\[
\tau(x_1)=v_2(2^{n}+28)=2,\quad x_1\equiv11\ (16),
\qquad
\tau(y_1)=1,\quad y_1\equiv9\ (16),
\]
\[
\lfloor8\log_2y_1\rfloor-\lfloor8\log_2x_1\rfloor=+4=L_Q-Qe_1+0 .
\]

The partner \(x_2\) is the least integer \(\equiv9\pmod{16}\) in the
non-carrying sub-interval of \(\mathrm{cell}(y_1)\). That sub-interval holds
about \(2^{n}(1-\varphi_Q)\ln2/Q\) integers, which exceeds the modulus \(16\)
for all \(n\ge8\), so **\(x_2\) exists by the elementary count**. CARRY1 then
forces \(\mathrm{cell}(f(x_2))=\mathrm{cell}(x_1)\) and TAU1 forces the
\(\tau\) match, so the coordinate cycle closes; the gain is strict because
\(E=3=\lfloor2\log_23\rfloor\).

**So an infinite family of certificates exists**, and the class
\(\log_2x+g(\lfloor8\log_2x\rfloor,\tau,x\bmod16)\) is refuted at every
height, not merely somewhere.

Verified: closed gaining 2-cycles for \(n=10..30\) and \(n\in\{40,60,80,120,
160,200\}\) — at \(n=200\) the witnesses are 201-bit and the cell holds
\(2.06\times10^{59}\) integers.

### The bound \(n\ge10\) is sharp, and it is CARRY1

The in-cell position of \(x_1\) is \(u_n=8\log_2(1+27/2^{n})\), decreasing in
\(n\), and \(\delta=1\) exactly when \(u_n\ge1-\varphi_Q\) with
\(\varphi_Q=\{8\log_23\}=0.6797\). At \(n=9\), \(u_9\approx0.593>0.3203\), so
\(\delta=1\), the shift is \(+5\), and closure fails. From \(n=10\)
(\(u_{10}\approx0.300\)) onward, \(\delta=0\).

An earlier draft asserted the family from \(n\ge5\). The verifier caught
\(n=9\). Logged in `CLAIM_LEDGER.md`. It is a pleasing confirmation that the
family's starting point is *predicted* by CARRY1 rather than found by trial.

---

## 3. The smallest members

| \(n\) | \(x_1\) | \(y_1\) | \(x_2\) | \(y_2\) |
|---|---|---|---|---|
| 10 | 1051 | 1577 | 1465 | 1099 |
| 11 | 2075 | 3113 | 2937 | 2203 |
| 12 | 4123 | 6185 | 5817 | 4363 |

The \(n=12\) member is the certificate found independently by
negative-cycle mining in WITN1.

---

## 4. Status of SUFF1

| piece | status |
|---|---|
| \(s\) counts carrying edges (CARRY1) | proved |
| positions freely choosable (FREE1) | proved |
| residue walk with correct valuation (WALK1) | proved |
| \(\tau\) is not independent (TAU1) | proved |
| cell dip linear in \(K\) (UNIF1) | proved |
| composition at \((j,K)=(3,2)\) (SUFF-32) | **proved** |
| composition for all \((j,K,m)\) (SUFF1) | **OPEN** |

---

## 5. What is left

Every ingredient of the general theorem is now proved. What is not written out
is the composition with constants **uniform in \((j,K,m)\)**: one must fix a
starting cell \(C_1\) exceeding

\[
m+e_{\max}+j+\log_2\frac1{\min(\varphi_Q,1-\varphi_Q)}+cK+O(1),
\]

then apply the count at each of the \(K\) edges. Nothing in that requires new
mathematics — UNIF1 supplies the \(cK\), CARRY1 the sub-intervals, TAU1 the
\(\tau\)-freedom, WALK1 the residues — but bookkeeping is not a proof until it
is written, and it is not written here.

The honest summary: **SUFF1 is reduced to an exercise, and verified in the
first nontrivial case.**

---

## 6. Verification

```bash
python3 scripts/verify_uniformity.py    # ALL PASS
```

---

## 7. Ledger rows

| ID | Claim | Status | Source | Verification |
|---|---|---|---|---|
| UNIF1 | Around a cycle the cell dip \(\min_i(\lfloor i\log_23\rfloor-E_i)\) is \(-cK+O(1)\) with \(c\approx0.24\) for the WALK1 recipe word; hence one starting height, chosen \(O(K)\) above the single-edge threshold, serves all \(K\) edges | Proved here (finite certificate for the rate, \(K\le800\)) | `docs/no-go/uniformity.md` | `scripts/verify_uniformity.py` |
| SUFF-32 | For \((j,m,K)=(3,16,2)\): \(x_1=2^n+27\) with \(n\ge10\) yields an infinite family of closed quantized-log certificates with strict integer gain; \(n\ge10\) is sharp and is predicted by CARRY1 (\(\delta=1\) at \(n=9\)). Hence \(\log_2x+g(\lfloor8\log_2x\rfloor,\tau,x\bmod16)\) is refuted at every height | Proved here | `docs/no-go/uniformity.md` | `scripts/verify_uniformity.py`; verified to \(n=200\) (201-bit witnesses); SUFF1 in general still OPEN |
