# Explicit-constants audit of every Baker-gated threshold  [W9]

**Task:** `OPUS5_WIDE_TASKS.md` W9 (session 1 of the recommended order).
**Building on:** `../repunit/repunit_baker_nonshadowing.md`,
`../repunit/repunit_baker_applicability_census.md`,
`avenue_a_comparison_dynamics.md` (Lemmas SD-L1-\*-Baker / -window-gap),
`../repunit/integral_escape_frontier.md` §"Continued-fraction growth",
`../density-cycles/cycle_reduction.md` §5.
**Verifier:** `scripts/verify_baker_explicit_constants.py` (36 checks, all
in exact integer / rational arithmetic; floats appear only in printing).
**Status of the note:** mixed — see the per-row status column. Nothing here
is promoted to `CLAIM_LEDGER.md` by this note.
**License:** CC-BY 4.0

---

## 0. Summary

The repository invokes transcendence theory generically in five places. The
audit finds that **every one of them is a linear form in exactly two
logarithms**, and in four of the five the two logarithms are \(\log2\) and
\(\log3\). This matters because:

- the generic multi-log inputs actually cited (Yu's \(p\)-adic theorem,
  Baker–Matveev) carry astronomically bad constants;
- for the two-log \(\{\log2,\log3\}\) case there is a *fully explicit*
  published bound with no unspecified constant — Rhin's proposition, the
  same input Simons–de Weger use for Collatz \(m\)-cycles;
- and inside any bounded range the exact continued fraction of
  \(\theta=\log_23\) beats every theorem by tens of orders of magnitude,
  and is itself an exactly verifiable finite object.

Two rows close outright.

1. **Avenue A, the \(L=1\) height/valuation gates.** The Baker hypothesis
   is eliminated. Lemmas SD-L1-e2-preimage-Baker, SD-L1-s4-Baker and
   SD-L1-s-Baker (for \(3\)-smooth \(s\)) previously read "standard lower
   bounds … give … for all large \(n\), whenever \(K_\downarrow=n^{O(1)}\)".
   They now read: *for every odd \(n\ge161\), by Rhin's theorem alone, with
   the concrete hypothesis \(K_\downarrow(n)\le6n\)* — and \(161\) is inside
   the existing scan range, so nothing is left over. See §3.

2. **BAKER1–3.** The fixed-\(d=7\) enemy branch has an exact closed form,
   \(v_2(3^m+7)=2+v_2(m-\alpha)\) for even \(m\), where \(\alpha\in\mathbb Z_2\)
   is the unique solution of \(3^\alpha=-7\). Consequently the prefix
   envelope needs **no transcendence input at all inside any finite range**:
   the least \(n\) admitting the prefix \((2,1^{K-1})\) is computed in closed
   form. The repo's empirical envelope \(K\le30\log_2(n+1)+10\) is slack by
   a factor of roughly \(30\); the exact maximum over odd \(n\le50001\) is
   \(K=17\), attained at \(n=1197\). See §4.

The three remaining rows are recorded with their sharpest applicable
theorem and their obstruction (§5).

---

## 1. The inventory

| # | Site | Invocation as written | Actual form | Logs |
|---|---|---|---|---|
| B1 | `repunit_baker_nonshadowing.md` §3, BAKER2/3 | "fixed-\(d\) consequence of Yu, \(p\)-adic logarithmic forms", constant \(C_7\) unspecified | \(v_2(3^m+7)\) | 2, \(2\)-adic |
| B2 | `avenue_a_comparison_dynamics.md`, SD-L1-e2-preimage-Baker | "standard lower bounds for linear forms in \(\log2\) and \(\log3\) give \(\gg H^{-C}\)" | \(|(E_i{+}n{+}5)\log2-(i{+}n{+}1)\log3|\) | 2, real |
| B3 | same, SD-L1-s4-Baker | idem | \(|(E_i{+}n{+}5)\log2-(i{+}n)\log3|\) | 2, real |
| B4 | same, SD-L1-s-Baker (fixed \(s\)) | idem | \(|(E_i{+}n{+}2)\log2-i\log3-\log(a_n/s)|\) | 2 if \(s\) is \(3\)-smooth, else 3 |
| B5 | same, EC1-large | "reduced to Baker/linear forms" | large-collision gap | 2, real |
| B6 | `integral_escape_frontier.md`, IEF10 | "a Baker–Matveev bound therefore gives …", constants \(C,C_0,Q_0\) unspecified | \(|(5q{+}p)\log2-(3q{+}p)\log3|\) | 2, real |
| B7 | `cycle_reduction.md` §5 (CYC5) | "needs a lower bound on \(|2^{E_K}-3^K|\) (transcendence theory)" | \(|E_K\log2-K\log3|\) | 2, real |
| B8 | `mersenne_obstructions.tex` §, `leading_digit_nogo.md` | "\(\beta=\log_2\frac98\) is irrational" | \(\|q\log_2\tfrac98\|=\|2q\theta\|\) | 2, real |

**Observation (the reason the audit is cheap).** The Collatz system is
built from the primes \(2\) and \(3\) only, so every Archimedean gate is a
\(\mathbb Z\)-linear form in \(\log2\) and \(\log3\). B8 is not even a new
object: \(\log_2\frac98=2\theta-3\), so \(\|q\log_2\frac98\|=\|2q\theta\|\)
and its irrationality measure is that of \(\theta\) with \(q\mapsto2q\).

---

## 2. The two explicit inputs

### 2.1 Rhin's proposition (real, two logs, fully explicit)

> **Known theorem (Rhin 1987).** For integers \(u_0,u_1,u_2\) with
> \(H=\max(|u_1|,|u_2|)\ge2\),
> \[
> |u_0+u_1\log2+u_2\log3|\;\ge\;H^{-13.3}.
> \]

This is the form used, with the same numeral, by Simons–de Weger for
\(m\)-cycles and restated as Lemmas 10 and 12 of
[Simons, arXiv:2205.10582](https://arxiv.org/abs/2205.10582). Reference:
G. Rhin, *Approximants de Padé et mesures effectives d'irrationalité*,
Séminaire de Théorie des Nombres, Paris 1985–86, Progr. Math. **71**,
Birkhäuser (1987), 155–164.

**Specialisation used here.** Take \(u_0=0\), \(u_2=-q\), and \(u_1=p\) the
nearest integer to \(q\theta\); then \(|p\log2-q\log3|=(\log2)\|q\theta\|\)
and \(p\le q\theta+\tfrac12\le2.085\,q\), so

\[
\boxed{\ \|q\theta\|\;\ge\;\frac{(2.085\,q)^{-13.3}}{\log2}\ }
\qquad(q\ge1),
\qquad \theta=\log_23 .
\tag{R}
\]

Equivalently \(\theta\) has effective irrationality measure \(\mu\le14.3\)
with an explicit constant. The verifier evaluates the right-hand side of
(R) exactly, using \(x^{13.3}\le x^{13}\lceil x^{1/3}\rceil\) and a
self-certified rational bracket for \(\log2\).

**Honest caveat, recorded so it is not rediscovered.** Rhin's paper also
contains the *sharper* inequality (8), quoted verbatim as Lemma 5.3 of
[Lagarias–Soundararajan, arXiv:math/0509175](https://arxiv.org/abs/math/0509175):
\(|u_0+u_1\log2+u_2\log3|\ge C\,H^{-7.616}\). Its exponent is much better
but the constant \(C\) is **not made explicit**, so it cannot produce a
numeral and is useless for W9's purpose. Any future sharpening of this row
should start by making that \(C\) explicit; it would roughly halve every
crossover below.

### 2.2 The exact continued fraction of \(\theta\) (finite, but sharp)

Computed by integer power comparisons only (no floating point):

\[
\theta=\log_23=[1;1,1,2,2,3,1,5,2,23,2,2,1,1,\dots]
\]

with convergent denominators \(1,2,5,12,41,53,306,665,15601,31867,79335,\dots\)
(the verifier computes 14 partial quotients; \(q_{13}=111202\) and
\(q_{14}=190537\) are reachable in seconds, the next is \(\sim10^7\)).
The verifier certifies two-sided rational brackets for \(|q_k\theta-p_k|\)
by evaluating \(\log_2(3^{q_k}/2^{p_k})\) with the exact inequalities
\((r-1)/r\le\ln r\le r-1\). By the best-approximation theorem
(Hardy–Wright ch. 10), for \(1\le q\le Q\) the minimum of \(\|q\theta\|\) is
attained at the largest convergent denominator \(\le Q\), so the table gives
a certified lower bound for \(\min_{q\le Q}\|q\theta\|\).

At \(Q=10^4\), (R) gives \(3.66\times10^{-58}\) while the certified
continued-fraction bound gives \(\min_{q\le Q}\|q\theta\|\ge6.30\times10^{-5}\).
**The continued fraction beats Rhin by \(53.2\)
orders of magnitude in the range that Avenue A actually uses.** That is why
the finite certificate reaches all the way down to \(n=7\) while the
theorem-only route starts at \(n=161\).

---

## 3. Row B2–B4: the Avenue A \(L=1\) gates close

### 3.1 The exact inequality

Lemma SD-L1-\*-window gives, for a hit \(x_i=\mathrm{target}\) at index
\(i\ge1\) with \(x_j\ge T=2^n-1\) for all \(j<i\),

\[
L_i\le2^{E_i}\le L_i\Bigl(1+\frac1{3T}\Bigr)^i,
\qquad L_i=\frac{3^ia_n}{\mathrm{target}} .
\]

Taking \(\log_2\) and using \(a_n=(3^n-1)/2\):

\[
0\;\le\;(E_i+A)-(i+B)\theta-\delta_n\;\le\;i\log_2\Bigl(1+\frac1{3T}\Bigr),
\]

with integers \(A,B\) depending only on the target, and \(\delta_n\)
exponentially small. Since \(E_i+A\in\mathbb Z\), **a hit forces**

\[
\boxed{\ \bigl\|(i+B)\,\theta\bigr\|\;\le\;\Delta(n,i)
:=|\delta_n|+i\log_2\Bigl(1+\frac1{3(2^n-1)}\Bigr).\ }
\tag{W}
\]

The three targets:

| target | \(A\) | \(B\) | \(\delta_n\) |
|---|---|---|---|
| \(x^\star(n)=(2^{n+4}-5)/3\) | \(n+5\) | \(n+1\) | \(\log_2(1-3^{-n})-\log_2(1-5\cdot2^{-(n+4)})\) |
| \(M_{n+4}=2^{n+4}-1\) | \(n+5\) | \(n\) | \(\log_2(1-3^{-n})-\log_2(1-2^{-(n+4)})\) |
| \(y_n(s)=s2^{n+2}-1\), \(s=2^a3^b\) | \(n+3+a\) | \(n-b\) | \(\log_2(1-3^{-n})-\log_2\bigl(1-\tfrac1{s2^{n+2}}\bigr)\) |

**Applicability gate (new, and worth recording).** \(A\) is an integer only
when \(\log_2s\in\mathbb Z\theta+\mathbb Z\), i.e. only when \(s\) is
\(3\)-smooth. For \(s\) with a prime factor \(\ge5\) the form has a *third*
logarithm and Rhin does not apply; that sub-family needs Matveev and gets a
much worse constant. The two explicit cases already in the repo, \(s=4\) and
\(s=6\), are both \(3\)-smooth, so both are covered here. This is the exact
analogue, on the Archimedean side, of the height gate that
`repunit_baker_nonshadowing.md` §6 imposes on the \(p\)-adic side.

Note also \(y_n(4)=2^{n+4}-1=M_{n+4}\); the two rows coincide, which the
verifier reproduces as a consistency check.

### 3.2 Two crossovers

Define \(i_\ast(n)\) = least \(i\ge1\) at which (W) is *not* refuted. Any
\(i\) with \(i<i_\ast(n)\) cannot carry a hit. Because
\(\min_{q\le i+B}\|q\theta\|\) is non-increasing in \(i\) while
\(\Delta(n,i)\) is strictly increasing, the predicate is monotone and
\(i_\ast\) is located by bisection, exactly.

> **W9-A (finite certificate).** For every odd \(7\le n\le501\) and each of
> the four targets above, \(i_\ast(n)>K_\downarrow(n)\). Hence the target is
> absent from the entire pre-descent \(a_n\)-orbit.

> **W9-B (proved here, from Rhin's theorem alone).** Put
> \(\theta=\log_23\). For every odd \(n\ge161\), every \(3\)-smooth \(s\),
> and every index \(i\le6n\), the window (W) is empty. Consequently, if
> \(K_\downarrow(n)\le6n\) then \(x^\star(n)\), \(M_{n+4}\) and \(y_n(s)\)
> are absent from the pre-descent \(a_n\)-orbit.

*Proof of W9-B.* For \(i\le6n\) and \(n\ge9\) one has
\(q=i+B\le7n+1\le8n\), hence \(2.085\,q\le16.68\,n\), so by (R)
\((\log2)\|q\theta\|\ge(16.68n)^{-13.3}\). On the other side, using
\(|\ln(1-u)|\le u/(1-u)\) and \(\ln(1+v)\le v\),
\[
(\log2)\,\Delta(n,i)\;\le\;\frac{2}{3^{n}}+\frac{10}{2^{n+4}}
+\frac{6n}{3(2^n-1)}\;\le\;\frac{3n}{2^{n}}
\qquad(n\ge9).
\]
So the window is empty at every \(i\le6n\) as soon as
\[
2^n>3n\,(16.68\,n)^{13.3}.
\tag{$*$}
\]
Writing \(h(n)=n-\log_2(3n)-13.3\log_2(16.68n)\), one has
\(h'(n)=1-14.3/(n\ln2)>0\) for \(n\ge21\), so \((*)\) is monotone; and
\(h(159)<0<h(161)\). \(\square\)

The verifier evaluates \(i_\ast(n)\) exactly (not through \((*)\)) and finds
the sharper crossover \(N_0=159\) for the theorem-only route, and \(N_0=15\)
for the continued-fraction route measured against the crude cap \(6n\).

Sample for the \(x^\star\) gate (the other three agree to within one unit):

| \(n\) | \(i_\ast(n)\) exact CF | \(K_\downarrow(n)\) | largest \(i\) proved empty by Rhin alone |
|---|---|---|---|
| 9 | 20 | 2 | — |
| 11 | 41 | 25 | — |
| 13 | 51 | 14 | — |
| 15 | \(>90\) | 17 | — |
| 151 | \(>906\) | 204 | 668 |
| 159 | \(>954\) | 263 | 1 039 |
| 201 | \(>1206\) | 420 | 8 879 |
| 471 | \(>2826\) | **732** | 4 250 317 670 |
| 501 | \(>3006\) | 652 | 18 133 726 369 |

The last column is the explicit form of the repo's
"\(i_\ast(n)\gg2^{n/\mu}\) for an effective \(\mu\)": the observed growth is
\(2^{n/14.33}\), matching \(\mu=14.3\) from (R) to two decimals.

### 3.3 What this changes in `avenue_a_comparison_dynamics.md`

Before: SD-L1-e2 / s4 / s-fixed were *doubly* conditional — on an unstated
Baker constant, and on \(K_\downarrow=n^{O(1)}\).

After: **the Baker conditionality is gone.** The surviving hypothesis is the
single concrete inequality \(K_\downarrow(n)\le6n\), which is exactly the
bound the repo already verifies on its certificate domain. The
"large-\(n\) tail" language should be replaced by the numeral \(161\), and
the window-gap scan for \(7\le n\le501\) is superseded by W9-A, which does
not trace orbits at all — it only reads the continued fraction of \(\theta\).

**Cross-check against the existing scan.** The repo records
\(i_\ast(5)=11\) and \(i_\ast^{(4)}(5)=12\) and \(K_\downarrow(5)=30\). This
note's \(i_\ast\) is a certified *lower* bound for the repo's (window
nonempty \(\Rightarrow\) (W) holds), and indeed gives \(4\) and \(5\) at
\(n=5\), and \(K_\downarrow(5)=30\) on the nose. \(n=5\) remains the sole
exception, discharged as before by direct orbit inspection
(Lemma SD-L1-e2-preimage-small).

### 3.4 What it does **not** change

Nothing here touches the open part of SD-L1: growing height \(s=s(n)\),
inbound \(e\ge4\), and the \(e=2\) valuation gate with \(|s|\ge3\). Those
are not Baker-gated; they are gated on bounding \(s\) and \(v\). W9 has no
purchase there, and no row of this note should be read as progress on them.

---

## 4. Row B1: BAKER1–3 needs no theorem in finite range

### 4.1 The exact closed form

> **W9-C (proved here).** Let \(\alpha\in\mathbb Z_2\) be the unique
> \(2\)-adic integer with \(3^\alpha=-7\). Then for every integer \(m\ge0\),
> \[
> v_2(3^m+7)=
> \begin{cases}
> 2+v_2(m-\alpha), & m\text{ even},\\
> 1, & m\text{ odd}.
> \end{cases}
> \]

*Proof.* \(3^m\bmod2^V\) depends only on \(m\bmod2^{V-2}\) for \(V\ge3\), so
\(m\mapsto3^m\) extends continuously to \(\mathbb Z_2\), with image the
closure of \(\langle3\rangle=\{x\equiv1,3\bmod8\}\). Since \(-7\equiv1\bmod8\),
there is a unique \(\alpha\) with \(3^\alpha=-7\), and \(\alpha\in2\mathbb Z_2\).
Then \(3^m+7=3^\alpha(3^{m-\alpha}-1)\), and the \(2\)-adic LTE identity
\(v_2(3^t-1)=2+v_2(t)\) for \(t\in2\mathbb Z_2\), \(=1\) for \(t\) odd,
extends by continuity from the integers. \(\square\)

Numerically \(\alpha\equiv6746143408631055534\pmod{2^{64}}\), and
\(\alpha\equiv1198\pmod{2^{16}}\).

**Consequence (restatement of BAKER1).** For odd \(n\ge3\), the repunit tail
of \(a_n\) begins with \((2,1^{K-1})\) **iff**
\[
n+1\equiv\alpha \pmod{2^{K+1}} .
\]
So the whole \(d=7\) branch is a single \(2\)-adic approximation question:
how well can \(\alpha\) be approximated by positive integers? BAKER2's
\(K\le C_7\log(n+1)\) is exactly the statement that \(\alpha\) is not a
\(2\)-adic Liouville number, which is where the (genuinely two-log,
\(2\)-adic) transcendence input belongs.

### 4.2 The exact envelope

Since the least \(m\ge0\) with \(v_2(3^m+7)\ge V\) is precisely
\(\alpha\bmod2^{V-2}\), the entire prefix envelope is a closed-form lookup —
**no theorem, no scan.** The record ladder (least \(n\) admitting each \(K\)):

| \(K\) | least \(n\) | \(\log_2(n{+}1)\) | \(K-\log_2(n{+}1)\) |
|---|---|---|---|
| 1 | 1 | 1.00 | +0.00 |
| 2 | 5 | 2.58 | −0.58 |
| 4 | 13 | 3.81 | +0.19 |
| 6 | 45 | 5.52 | +0.48 |
| 9 | 173 | 7.44 | +1.56 |
| **17** | **1 197** | 10.23 | **+6.77** |
| 18 | 263 341 | 18.01 | −0.01 |
| 21 | 787 629 | 19.59 | +1.41 |
| 23 | 4 981 933 | 22.25 | +0.75 |
| 24 | 21 759 149 | 24.38 | −0.38 |
| **35** | **55 313 581** | 25.72 | **+9.28** |
| 36 | 68 774 790 317 | 36.00 | −0.00 |

Hence, exactly:

| \(N\) | \(\max K\) over odd \(n\le N\) | repo envelope \(30\log_2(N{+}1)+10\) |
|---|---|---|
| 500 | 9 | 279 |
| 5 001 | 17 | 379 |
| 50 001 | 17 | 478 |
| 500 001 | 18 | 578 |
| 5 000 001 | 23 | 678 |

> **W9-D (finite certificate).** For every odd \(n\le1.8\times10^{19}\)
> (\(2\)-adic depth 64), a repunit tail beginning \((2,1^{K-1})\) satisfies
> \(K\le\log_2(n+1)+10\); through \(n\le50001\) the exact maximum is
> \(K=17\), attained only at \(n=1197\).

This supersedes the empirical envelope \(K\le30\log_2(n+1)+10\) of
`scripts/verify_repunit_baker_nonshadowing.py`, which is slack by a factor
of about \(30\) in the slope, and it replaces a modular-replay scan by a
closed form. The two visible "excess" events (\(K=17\) at \(n=1197\),
\(K=35\) at \(n=55\,313\,581\)) are exactly the places where \(\alpha\) has a
long run of coincident bits; they are the finite shadow of the Liouville
question and are the right test cases for any future explicit \(C_7\).

### 4.3 The theorem that should be cited instead of Yu

The linear form is \(v_2(m\log3-\log(-7))\) (with \(\log\) the \(2\)-adic
logarithm; note \(v_2(\log3)=2\), which is where the additive \(2\) in W9-C
comes from). **This has exactly two logarithms.** Yu's general \(p\)-adic
theorem, as cited in `repunit_baker_nonshadowing.md` §3, is a multi-log
theorem and carries constants many orders of magnitude worse than the
two-log \(p\)-adic estimates of Bugeaud–Laurent, which are the correct
input.

**Not done in this session, deliberately.** Instantiating Bugeaud–Laurent
to obtain a numeral for \(C_7\) requires the full parameter list of their
theorem, which was not available to verify in this session; quoting it from
memory would be exactly the kind of unchecked constant this note exists to
remove. Recorded as the open sub-row **W9-E**:

> **W9-E (open, bounded work).** Instantiate the Bugeaud–Laurent two-log
> \(2\)-adic estimate at \((\alpha_1,b_1,\alpha_2,b_2)=(3,m,-7,1)\), \(p=2\),
> to obtain a numeral for \(C_7\) in \(v_2(3^m+7)\le C_7\log m\). Success
> criterion: the resulting bound is *worse* than the exact ladder of §4.2 in
> the scanned range (it will be, by many orders of magnitude), so the value
> of the row is purely the unconditional tail \(n>1.8\times10^{19}\).

Note the honest ordering: for the finite range the exact ladder is already
strictly better than any transcendence theorem, so W9-E is a low-priority
completeness item, not a blocker.

---

## 5. The remaining rows

| Row | Sharpest applicable explicit theorem | Resulting \(N_0\) | Verdict |
|---|---|---|---|
| B5 EC1-large | Rhin (R) — the large-collision gap is a two-log \(\{\log2,\log3\}\) form | not computed | **deferred.** The gate is stated as a reduction, not as an inequality with named coefficients; it needs the coefficients written out before a numeral can be attached. One session. |
| B6 IEF10 continued-fraction growth | Rhin (R), replacing the Baker–Matveev citation | see below | **explicit, filable.** |
| B7 CYC5 cycle wall | Rhin (R) directly on \(|E_K\log2-K\log3|\) | explicit but subsumed | **file, do not promote.** |
| B8 \(\log_2\frac98\) | reduces to (R) with \(q\mapsto2q\) | immediate | **explicit, no new input needed.** |

### 5.1 B6 in detail

`integral_escape_frontier.md` needs \(|\beta-p/q|>q^{-C}\) for
\(\beta=\frac2{\log_2(3/2)}-3\), via the linear form
\(2q\log2-(3q+p)\log(3/2)=(5q+p)\log2-(3q+p)\log3\). For approximants with
\(|\beta-p/q|<1\) one has \(p<(\beta+1)q<1.42q\), so \(H=5q+p<6.42q\) and
(R) gives
\[
\left|\beta-\frac pq\right|
=\frac{|(5q+p)\log2-(3q+p)\log3|}{q\log(3/2)}
\;>\;\frac{(6.42\,q)^{-13.3}}{q\log(3/2)}
\;>\;4.4\times10^{-11}\,q^{-14.3}.
\]
Combined with \(|\beta-P_{k-1}/Q_{k-1}|<1/(Q_{k-1}Q_k)\) this turns IEF's
"\(Q_k<Q_{k-1}^{C-1}\) eventually" into the unconditional numeral
\[
Q_k<2.3\times10^{10}\,Q_{k-1}^{13.3}\qquad\text{for all }k .
\]
The word "eventually" and the unspecified \(C,Q_0\) can be deleted from that
section. (The constants above are hand-derived from (R) and confirmed only
by a floating-point evaluation; they are *not* in the verifier and must be
recomputed there in exact arithmetic before this row enters a proof chain.
Flagged.)

### 5.2 B7 in detail

\(|2^{E}-3^{K}|=3^K|e^{\Lambda}-1|\ge3^K|\Lambda|/e\) with
\(\Lambda=E\log2-K\log3\), so (R) gives
\(|2^{E_K}-3^{K}|\ge3^{K}E_K^{-13.3}/e\) — a fully explicit version of the
CYC5 wall. This is honest but has no independent value: Steiner (1977) and
Simons–de Weger (2005) already convert the same input into far stronger
cycle exclusions, and the note itself says so. Filed for completeness.

---

## 6. Barrier check

W9 is bookkeeping over proved inputs, so the four barriers of
`outside_box_avenue_triage.md` §14 are relevant only as things this note
must not accidentally claim to evade.

1. *Finite-state information.* Not used. §3 and §4 are Diophantine, not
   automaton-theoretic.
2. *Density / entropy.* Not used. Every statement is about an individual
   \(n\) and an individual orbit.
3. *Variable-height Diophantine bounds are tautological.* **This is the
   binding constraint and it is respected.** Every form treated here has
   *fixed* coefficients in \(\log2,\log3\) with height controlled by
   \(i+n\), which is exactly why the explicit theorems apply. The rows the
   audit could **not** close are precisely the variable-height ones: the
   generic reduced enemy \(d_K\) of
   `repunit_baker_applicability_census.md` (height \(\asymp E_K\)) is
   untouched, and §4 concerns only the fixed \(d=7\) branch. §3.4 states
   the same limitation for growing \(s(n)\).
4. *Virtual collisions.* Not applicable; all statements are about the
   actual \(a_n\)-orbit.

**Explicit non-claim.** Nothing in this note reduces the survivor set of
Avenue A, produces a descent, or bears on the storage-dominance lemma. It
removes conditionality from lemmas that were already proved modulo a
transcendence hypothesis. That is its entire content.

---

## 7. Falsifier

The W9 rows are falsified by any of:

- an arithmetic error in the certified brackets — re-run the verifier; every
  inequality is exact and every bracket is two-sided;
- a misquotation of Rhin's exponent. The number \(13.3\) is used here in the
  form "\(|u_0+u_1\log2+u_2\log3|\ge H^{-13.3}\), \(H=\max(|u_1|,|u_2|)\)",
  as restated in Simons (arXiv:2205.10582) Lemmas 10 and 12. Should the
  original hypothesis turn out to require \(H\ge H_0>2\), every crossover in
  §3 must be re-derived; the continued-fraction row (W9-A) is unaffected
  because it uses no theorem;
- for §4, any \(m\) with \(v_2(3^m+7)\ne2+v_2(m-\alpha)\) — checked for all
  even \(m<4000\) and structurally proved in W9-C.

**Kill rule inherited from W9's own statement:** kill an individual row when
the explicit \(N_0\) is beyond any feasible scan *and* the form is genuinely
multi-log. No row here meets that test; rows B1 (generic \(d_K\)) and B4
(non-\(3\)-smooth \(s\)) are excluded for the *height* reason instead, which
is barrier 3, not a constants problem.

---

## 8. Verification

```bash
python3 scripts/verify_baker_explicit_constants.py                 # 36 checks
python3 scripts/verify_baker_explicit_constants.py --nmax 501      # faster
python3 scripts/verify_baker_explicit_constants.py --cf-terms 13   # wider q
```

The script prints `BAKER-EXPLICIT: PASS`. Its stress row recomputes
\(K_\downarrow(471)=732\) from scratch and confirms all four gates are empty
through first descent at \(n=471\), by the continued fraction and by Rhin
separately.

---

## 9. Suggested ledger rows (not applied)

Per the session protocol, `CLAIM_LEDGER.md` is **not** edited by this note.
If Dr Bry accepts the rows, the natural entries are:

| ID | Statement | Status | Source |
|---|---|---|---|
| BAKEX1 | \(\|q\log_23\|\ge(2.085q)^{-13.3}/\log2\) for all \(q\ge1\) | Known theorem applied (Rhin 1987) | this note §2.1 |
| BAKEX2 | For odd \(n\ge161\) and \(3\)-smooth \(s\): if \(K_\downarrow(n)\le6n\) then \(x^\star(n),M_{n+4},y_n(s)\) are absent pre-descent — no Baker hypothesis | Proved here from a known theorem | §3.2 (W9-B) |
| BAKEX3 | \(v_2(3^m+7)=2+v_2(m-\alpha)\) for even \(m\), \(3^\alpha=-7\) in \(\mathbb Z_2\); prefix \((2,1^{K-1})\) iff \(n+1\equiv\alpha\bmod2^{K+1}\) | Proved here | §4.1 (W9-C) |
| BAKEX4 | Max \(K\) over odd \(n\le50001\) is exactly \(17\), at \(n=1197\); \(K\le\log_2(n+1)+10\) to \(2\)-adic depth 64 | Finite certificate | §4.2 (W9-D) |

BAKEX2 supersedes the Baker halves of the SD-L1-e2-preimage, SD-L1-s4 and
SD-L1-s-fixed rows of the Avenue A status table; BAKEX3/4 sharpen BAKER2/3
without contradicting them.
