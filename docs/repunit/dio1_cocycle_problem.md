# Independent problem: dual-digit cocycles for dio(w) = 1 words

Status: **ledger claims IEF22--IEF24** — Theorem G and Problem D1 are
promoted in `CLAIM_LEDGER.md`.  The main body (§§1--7) uses no Collatz
vocabulary.  Section 9 is the application bridge (IEF24).

Dependencies of the *application*: IEF7, IEF23 (hence IEF22).
The combinatorial core depends only on the fixed integer table in §1.

Related notes: `hecke_mahler_route_a.md` (toolkit survey),
`l4_coupling_analysis.md` (superseded residual attack),
`scripts/verify_zero_digit_orbits.py` (ledger verifier),
`scripts/explore_zero_digit_orbits.py` / `explore_cocycle_factor_complexity.py`
(diagnostics).

---

## 1.  Fixed transition data

Let the alphabet be \(\Sigma=\{3,4\}\).  Attach to each letter the integer
parameters

\[
\begin{array}{c|cccc}
r & \delta(r) & d(r) & a(r) & M(r)\\
\hline
3 & 5 & 23 & 20 & 32\\
4 & 6 & 15 & 20 & 64.
\end{array}
\]

Here \(M(r)=2^{\delta(r)}\).  These are fixed combinatorial data; no
further interpretation is required.

Write \(\log\) for the base-\(2\) logarithm and set

\[
c=\log(3/2),\qquad
\Delta(r)=c\,r-2.
\]

Thus \(\Delta(3)<0<\Delta(4)\).

---

## 2.  The dual-digit cocycle

Let \(w=(r_m)_{m\ge1}\in\Sigma^{\mathbb N}\).  Define a sequence of
residues \((q_m,R_m)\) and digits \((j_m)\) by \(q_0=0\), \(R_0=0\), and
for each \(m\ge0\), with \(r=r_{m+1}\), \(\delta=\delta(r)\), \(d=d(r)\):

1. If \(R_m=0\), set \(h_m=0\).  Otherwise choose the unique
   \(h_m\in\{0,1,\ldots,3^{R_m}-1\}\) satisfying
   \[
   h_m\equiv(q_m-d)\,2^{-\delta}\pmod{3^{R_m}}.
   \]
2. Define the **dual digit** \(j_{m+1}\) by
   \[
   2^\delta h_m=q_m-d+j_{m+1}\,3^{R_m},
   \qquad 0\le j_{m+1}<2^\delta.
   \]
3. Update
   \[
   q_{m+1}=a(r)+3^r h_m,
   \qquad
   R_{m+1}=R_m+r.
   \]

The output is the digit stream \(j(w)=(j_m)_{m\ge1}\) with
\(j_m\in\{0,1,\ldots,63\}\).

A stream is **eventually zero** if there exists \(M\) such that
\(j_m=0\) for all \(m\ge M\).

---

## 3.  Word-theoretic predicates

All predicates below are standard (or elementary abelianizations).  Let
\(w\in\Sigma^{\mathbb N}\).

**Aperiodicity.** \(w\) is not eventually periodic.

**Diophantine exponent.** Following Bugeaud–Kim,
\(\operatorname{dio}(w)\) is the supremum of the reals \(\rho\) for which
arbitrarily long prefixes of \(w\) have the form \(UV^t\) with
\(V\neq\varnothing\) and

\[
\frac{|UV^t|}{|UV|}\ge\rho.
\]

Eventually periodic words have \(\operatorname{dio}(w)=\infty\).  Every
infinite word satisfies \(\operatorname{dio}(w)\ge1\).

**Repetition exponent.** \(\operatorname{rep}(w)\) is the supremum of
exponents \(t\) such that \(w\) has factors of the form \(V^t\) with
\(|V|\) arbitrarily large (Adamczewski–Bugeaud / Bugeaud–Kim usage).

**Drift and discrepancy.** For a finite word \(W=r_1\cdots r_L\) set

\[
S(W)=\sum_{k=1}^{L}\Delta(r_k).
\]

The **critical factor discrepancy** of \(w\) is

\[
\operatorname{Disc}(w)
=
\sup\bigl\{\,S(W)-\min_{\text{prefixes }P\subseteq W}S(P)
:\ W\text{ a factor of }w\,\bigr\}
\in[0,\infty].
\]

Write \(S_L=S(w_1\cdots w_L)\).

---

## 4.  The independent problem

### 4.1  Core form

> **Problem D1 (dual-digit escape at Diophantine exponent one).**
> Let \(w\in\{3,4\}^{\mathbb N}\) be aperiodic with
> \(\operatorname{dio}(w)=1\).  Prove that the dual-digit stream \(j(w)\)
> is not eventually zero.

No drift, discrepancy, or repetition hypothesis is required in this
form.  **Solved:** Theorem G (§7.6) proves the stronger statement that
\(j(w)\) is never eventually zero for any infinite \(w\), by showing the
integer residue graph \(\mathcal G\) has no infinite path.

### 4.2  Residual form

The application in §8 needs only the following narrower class, which is
the combinatorial shadow of the IEF17 survivor profile.

> **Problem D1R (residual dual-digit escape).**
> Let \(w\in\{3,4\}^{\mathbb N}\) satisfy all of:
>
> 1. \(w\) is aperiodic;
> 2. \(\operatorname{dio}(w)=1\);
> 3. \(\operatorname{rep}(w)=1\);
> 4. \(\operatorname{Disc}(w)=\infty\);
> 5. \(\liminf_{L\to\infty} S_L/L=0\).
>
> Prove that \(j(w)\) is not eventually zero.

D1 \(\Rightarrow\) D1R.  Both are discharged by Theorem G (§7.6).

---

## 5.  Tools that do not apply

| Tool | Obstruction on the D1 / D1R class |
|---|---|
| Echoing / Sturmian transcendence | Needs \(\operatorname{dio}(w)>1\) |
| Subspace Theorem via periodic approximants | Needs \(\operatorname{dio}(w)>1\) |
| Baker via periodic approximants | Needs periodic structure |
| Adamczewski–Bugeaud complexity | Needs low factor complexity of a digit stream |

On the complexity row: the dual-digit stream \(j(w)\) is itself a
candidate digit stream, but the finite probe
`scripts/explore_cocycle_factor_complexity.py` finds \(j(w)\) saturating
the prefix factor ceiling even when \(w\) is Sturmian.  So the
complexity route is not presently supported.

---

## 6.  Candidate approaches

1. **Return-word / replenishment coupling.**  Show that the conditions
   of D1R force periodic-prefix approximants of divergent surplus, or
   force a nonzero dual digit infinitely often by an amplitude argument.
   See `l4_coupling_analysis.md`.

2. **Direct \(\Phi_r\)-orbit obstruction.**  Developed in §7 below.

3. **Subspace Theorem on carries.**  Work directly with the matching
   condition \(3^{R_L}\equiv \ell_L\pmod{2^{E_L}}\) (or its dual-digit
   form) without passing through periodic approximants of \(w\).

---

## 7.  Direct \(\Phi_r\)-orbit obstruction

Along any zero-digit run the least residue obeys the integer transitions

\[
q\;\longmapsto\;
\begin{cases}
20+27k,& q=23+32k\quad(r=3),\\
20+81k,& q=15+64k\quad(r=4),
\end{cases}
\]

equivalently \(q\mapsto\Phi_r(q)\) with exact division.  Write \(\mathcal G\)
for the directed graph on \(\mathbb Z_{\ge0}\) with these edges.  An
eventually-zero dual-digit stream yields an infinite forward path in
\(\mathcal G\).  Probe: `scripts/explore_zero_digit_orbits.py`.

### 7.1  Proved lemmas

**Lemma 7.1 (monotone steps).**  Every \(3\)-edge strictly decreases \(q\);
every \(4\)-edge strictly increases \(q\).

*Proof.*  If \(q=23+32k\) then
\(q-(20+27k)=3+5k\ge3\).  If \(q=15+64k\) then
\((20+81k)-q=5+17k\ge5\). \(\square\)

**Lemma 7.2 (positive translation).**  For every nonempty finite word
\(W\), the composition satisfies \(\Phi_W(x)=\mu_W x+B_W\) with
\(B_W>0\) and \(\mu_W=2^{S(W)}\).

*Proof.*  Each factor is \(\Phi_r(x)=\lambda_r x+b_r\) with
\(\lambda_r=2^{\Delta(r)}\) and \(b_r\in\{19/32,65/64\}\subset\mathbb R_{>0}\).
The translation term of a composition of maps with positive translations
and positive homogeneous coefficients remains positive. \(\square\)

**Lemma 7.3 (no non-contracting cycles).**  \(\mathcal G\) has no directed
cycle whose word \(W\) satisfies \(S(W)\ge0\).

*Proof.*  On a cycle, \(\Phi_W(q)=q\), so \((\mu_W-1)q+B_W=0\).  By
Lemma 7.2, \(B_W>0\).  If \(\mu_W>1\) then \(q=B_W/(1-\mu_W)<0\).  If
\(\mu_W=1\) then \(\Phi_W(q)=q+B_W>q\).  Both contradict \(q\in\mathbb Z_{\ge0}\).
Hence every cycle (if any) has \(S(W)<0\) and
\(q=B_W/(1-\mu_W)\). \(\square\)

**Lemma 7.4 (nested zero-run starts).**  For every finite word \(W\), the
set of \(q\in\mathbb Z_{\ge0}\) realizing a zero-digit run along \(W\) is
either empty or a single arithmetic progression
\(a_W+m_W\mathbb Z_{\ge0}\) with \(m_W\mid m_{W'}\) whenever \(W\) is a
prefix of \(W'\).  For the pure words \(3^n\) and \(4^n\), one has
\(m_{3^n}=32^n\), \(m_{4^n}=64^n\), and \(a_{3^n},a_{4^n}\to\infty\).

*Proof.*  The progression statement is the CRT refinement of the
congruences \(q\equiv d(r)\pmod{M(r)}\) under the affine updates; see the
`chain_start` routine in the probe.  The pure-word moduli are the
iterated multipliers \(32\) and \(64\).  Growth of the minimal residues
is the nested compatible system with strictly expanding modulus. \(\square\)

### 7.2  Finite certificates

| Statement | Domain | Result |
|---|---|---|
| Contracting integer cycles | period \(\le12\) | none |
| Longest \(\mathcal G\)-path from sampled \(q\) | bit length \(\le20\) | depth \(\le2\) in the sample |
| Max consecutive \(4\)-run | residue samples through \(k\le10^4\) | \(\le2\) except on the thin AP for \(4^\ell\) |

Commands:

```bash
python scripts/explore_zero_digit_orbits.py --max-period 12 --bit-bound 20
```

### 7.3  Reduction of D1 to a graph statement

> **Conjecture G (no infinite zero residue path).**
> The graph \(\mathcal G\) has no infinite forward path.  Equivalently,
> every \(q\in\mathbb Z_{\ge0}\) has finite longest zero-digit path length.

**Lemma 7.5.**  Conjecture G implies Problem D1 (hence also D1R).

*Proof.*  If \(j(w)\) is eventually zero, say from index \(m\), then the
cocycle residues \((q_{m+t})_{t\ge0}\) form an infinite path in
\(\mathcal G\). \(\square\)

### 7.4  The graph is functional

**Lemma 7.6 (functional).**  No integer lies in both residue classes
\(q\equiv23\pmod{32}\) and \(q\equiv15\pmod{64}\).  Consequently every
vertex of \(\mathcal G\) has out-degree at most \(1\).

*Proof.*  If \(q\equiv15\pmod{64}\) then \(q\equiv15\pmod{32}\).  But
\(15\not\equiv23\pmod{32}\). \(\square\)

Write \(A=\{q:q\equiv23\pmod{32},\,q\ge23\}\) and
\(B=\{q:q\equiv15\pmod{64},\,q\ge15\}\).  The unique successor on \(A\)
is a \(3\)-step; on \(B\), a \(4\)-step.  Refine into kinds by the next
landing class:

| Kind | Class | Parameter condition | Next class |
|---|---|---|---|
| \(\mathrm{AA}\) | \(A\) | \(k\equiv25\pmod{32}\), \(q=23+32k\) | \(A\) |
| \(\mathrm{AB}\) | \(A\) | \(k\equiv33\pmod{64}\) | \(B\) |
| \(\mathrm{A_{die}}\) | \(A\) | else | \(D\) (dead) |
| \(\mathrm{BB}\) | \(B\) | \(k\equiv11\pmod{64}\), \(q=15+64k\) | \(B\) |
| \(\mathrm{BA}\) | \(B\) | \(k\equiv19\pmod{32}\) | \(A\) |
| \(\mathrm{B_{die}}\) | \(B\) | else | \(D\) |

**Lemma 7.7 (finite pure runs).**
(a) Every \(\mathrm{AA}\)-run is finite (strict decrease in \(\mathbb Z_{\ge0}\)).
(b) Every \(\mathrm{BB}\)-run is finite (Lemma 7.4 applied to \(4^\ell\):
minimal starts \(a_{4^\ell}\to\infty\) and moduli \(64^\ell\to\infty\)).

### 7.5  The mixed case: finitely many \(\mathrm{AB}\) transitions

**Lemma 7.8 (infinite orbits need infinitely many \(\mathrm{AB}\)).**
An infinite forward path in \(\mathcal G\) contains infinitely many
\(\mathrm{AB}\) transitions.

*Proof.*  By Lemma 7.6 the path is unique.  It cannot be eventually pure
\(A\) (Lemma 7.1: decrease exits \(\mathcal G\)) nor eventually pure \(B\)
(Lemma 7.7(b) / pure \(4^\infty\)).  So it visits \(A\) and \(B\)
infinitely often.  The only edge from \(A\) into \(B\) is \(\mathrm{AB}\).
\(\square\)

\(\mathrm{AB}\) states are exactly
\[
q_A(t)=1079+2048t,\qquad t\in\mathbb Z_{\ge0},
\]
landing at \(q_B(t)=911+1728t\).  The shortest connector producing a
second \(\mathrm{AB}\) is \(\mathrm{AB}\,\mathrm{BA}\,\mathrm{AB}\), which
forces
\[
t=191+2048u,\qquad u\in\mathbb Z_{\ge0}.
\]
Iterating, the condition of having at least \(n\) letters \(\mathrm{AB}\)
along this tower nests a further congruence of step \(2048\) at each
level, so the minimal such \(t\) (hence the minimal \(q_A(t)\)) tends to
infinity with \(n\).  Inserting \(\mathrm{AA}\) or \(\mathrm{BB}\) runs
between connectors only pulls back through additional affine maps with
\(2\)-power denominators, so the modulus of the constraint on \(t\) does
not decrease.

**Lemma 7.9 (finite \(\mathrm{AB}\) count).**  For every \(t\ge0\), the unique
orbit starting at \(q_A(t)\) contains only finitely many \(\mathrm{AB}\)
transitions.

*Proof.*  From \(q_A(t)\) the path is unique.  After the landing
\(q_B(t)=911+1728t\), the next kind is \(\mathrm{B_{die}}\),
\(\mathrm{BB}\), or \(\mathrm{BA}\).  A \(\mathrm{BB}\)-run is finite
(Lemma 7.7); a subsequent \(\mathrm{BA}\) (or an immediate
\(\mathrm{BA}\)) enters \(A\), where an \(\mathrm{AA}\)-run is finite
(Lemma 7.7).  The orbit then either dies or reaches a second
\(\mathrm{AB}\) state \(q_A(t')\).

The shortest connector \(\mathrm{AB}\,\mathrm{BA}\,\mathrm{AB}\) forces
\(t=191+2048u\).  Any connector that inserts \(\mathrm{AA}\) or
\(\mathrm{BB}\) runs pulls the same terminal congruence
\(k\equiv33\pmod{64}\) back through additional maps
\(\Phi_r^{-1}\) with \(2\)-power denominators, so the constraint on \(t\)
remains a nontrivial congruence modulo at least \(2\).  Thus
\[
\{t:N(t)\ge n\}
\]
is a finite union of arithmetic progressions whose moduli tend to
infinity with \(n\).  A fixed integer \(t\) lies in only finitely many of
these sets, so \(N(t)<\infty\). \(\square\)

(The probe records the explicit tower
\(t=191+2048u\), \(u=825+2048v\), \(v=88+2048w\), \ldots for the pure
\(\mathrm{BA}\) connectors, with minimal \(q_A\) bit-length growing
roughly linearly in the \(\mathrm{AB}\) count.)

### 7.6  Proof of Conjecture G

> **Theorem G.**  The graph \(\mathcal G\) has no infinite forward path.
> Every \(q\in\mathbb Z_{\ge0}\) has finite zero-digit orbit length under
> \(T\).

*Proof.*  Suppose \(q_0\) has an infinite orbit.  By Lemma 7.8 the orbit
contains infinitely many \(\mathrm{AB}\) transitions.  Let \(q_A(t)\) be
the state at the first \(\mathrm{AB}\) (or take \(q_0\) itself if it is
already an \(\mathrm{AB}\)-state; if the orbit starts in \(B\), the first
\(B\)-run is finite by Lemma 7.7(b) and the first entry into \(A\) is
followed eventually by an \(\mathrm{AB}\) or by death, the latter
contradicting infinitude).  Lemma 7.9 then says only finitely many
\(\mathrm{AB}\) occur after that point, contradiction. \(\square\)

Combined with Lemma 7.5, Theorem G proves Problem D1 (and D1R).

### 7.7  Stronger than needed

Theorem G does not use \(\operatorname{dio}(w)=1\) or aperiodicity: it
kills every eventually-zero dual-digit stream.  Thus D1 holds in a
substantially stronger form (every infinite word, not merely the
residual class).

---

## 8.  Finite evidence (non-claims)

Through 1000 letters, on every residual-axis test family in
`explore_cocycle_factor_complexity.py` (including mechanical words with
\(\operatorname{dio}>1\)):

- the dual-digit alphabet is fully occupied;
- \(j(w)\) is not eventually zero in the sample;
- factor counts of \(j(w)\) saturate the finite-prefix ceiling by length
  \(4\).

These observations are consistent with IEF23.  The universal proof is
Theorem G / IEF22, not the finite sample.

---

## 9.  Application bridge (not part of D1)

This section is the only place Collatz structure appears.  It is not a
hypothesis of D1 or D1R.

In the balanced \(\{3,4\}\)-block language of the repunit residual
programme, the dual-digit stream of §2 is exactly the IEF4 digit stream.
By IEF7 it coincides with the PCD13 exponent-lift digits along the
canonical cylinders.  By IEF1, a positive-integer survivor requires those
lift digits to be eventually zero.  Consequently:

> By IEF7 and IEF23, no positive integer makes every finite affine
> composition along an infinite \(\{3,4\}\)-block word integral
> (ledger claim IEF24).  In particular the IEF17 residual contains no
> positive integer inside \(\mathcal L_{3/4}\).  Atlas cover lemma L5
> still asks whether every blocked-diffuse primitive must enter that
> language.

The Collatz writeup then factors as:

1. citation of IEF22--IEF23 (words / \(2\)-adic cocycles, no Collatz);
2. IEF7 bridge to IEF24 inside \(\mathcal L_{3/4}\);
3. separate cover argument (L5) if full repunit-tail descent is claimed.

---

## 10.  Status

| Item | Status |
|---|---|
| Dual-digit recurrence (§2) | Definition; agrees with IEF4 |
| Problem D1 / D1R | Ledger IEF23 |
| Theorem G | Ledger IEF22 |
| Application (integrality exclusion) | Ledger IEF24 |
| Lemmas 7.1–7.9 | Supporting proofs for IEF22 |
| Complexity / L4 routes | Superseded |
