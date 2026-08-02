# Machine synthesis inside the surviving potential class  [W6]

**Task:** `OPUS5_WIDE_TASKS.md` W6 (session 7 of the recommended order).
**Building on:** `shadow_certificate.md` (SH1), `leading_digit_nogo.md`
(SH2), `spine_synthesis.md` (BND1), `quantized_log_witnesses.md` (WITN1),
`suff1.md` (SUFF1), `connectivity.md` (CONN1), `cost_law_proof.md` (COST1).
**Verifier:** `scripts/verify_machine_synthesis.py` (9 checks; exact integer
arithmetic for every promoted claim, floats only to guide the cycle search,
z3 as an independent decision procedure).
**Status:** **Premise corrected; new finite no-go proved; the surviving
question is re-stated.** W6's one-variable branch was already closed by the
ledger. Its two-variable branch is genuinely open, and this session extends
the no-go into it on the compressing coordinates.
**License:** CC-BY 4.0

---

## 0. Verdict

W6's stated premise was: "SH1/SH2/BND1 killed every one-step potential
*below* the quantized full logarithm \(\lfloor2^{j}\log_2x\rfloor\); the
manuscript marks that boundary as where the no-go programme terminates —
meaning the surviving class has never been searched."

> **W6-KILL-A (premise correction).** That is out of date. **SUFF1**, made
> unconditional by **CONN1**, already proves that for every \(j\), every
> admissible \(K\) and every \(m\ge3\) there is a closed certificate against
> \[
> \Phi(x)=\log_2x+g\bigl(\lfloor Q\log_2x\rfloor,\ \tau(x),\ x\bmod2^{m}\bigr),
> \qquad Q=2^{j}.
> \]
> The quantized full logarithm is therefore **not** the surviving class; it
> is closed at every finite precision. This session rediscovers such
> certificates independently (§2), so the correction does not rest on
> re-reading the ledger.

What genuinely survives is the *other* half of W6's own proposal, which the
task states but does not emphasise: **two-variable potentials \(V(x,n)\) on
(state, repunit exponent) pairs.** SH1 and SUFF1 both concern functions of
\(x\) alone; neither says anything about a potential that may also read
\(n\).

> **W6-B (the reason the two-variable class survives).** The SH1 shadow
> cancels an \(n\)-dependence only if the shadow cycle lies **inside one
> \(a_n\) orbit**, since \(n\) is constant along an orbit and then \(g\)'s
> \(n\)-part telescopes away. Measured on actual repunit orbits, the shadow
> depth \(N^\ast(n)=\max_i v_2(x_i(n)+5)\) grows only like
> \(\log_2(\#\text{states})\) — it reached \(12\) over \(3464\) states
> (heuristic \(11.8\)), and only \(10\) on the whole \(n=471\) orbit. So SH1
> gives a **finite** no-go on repunit orbits (\(m\lesssim N^\ast-3\)), not
> its usual universal one. That gap is exactly where \(V(x,n)\) lives.

> **W6-C (new finite no-go).** On the two-variable coordinate
> \[
> C(x,n)=\bigl(x\bmod2^{m},\ \tau(x),\
> \lfloor Q\log_2 x\rfloor-\lfloor Q\log_2 a_n\rfloor\bigr)
> \]
> — the quantized log taken *relative to the orbit's own seed*, a genuine
> second-variable reading — certificates exist on actual repunit orbits for
> \((m,j)\in\{(4,1),(6,1),(8,2)\}\) over \(n\le101\). Both the exact
> negative-cycle search and z3 agree (UNSAT). This is a new finite no-go
> extending SH1 into the two-variable class, and its witnesses are actual
> orbit states, not constructed shadows.

The complementary answer is honest but negative: at finer coordinates
(\(m\ge12\)) the search returns SAT, and **that SAT is vacuous** — the
coordinate is essentially injective on the window, so \(g\) is unconstrained.
See §4.

---

## 1. The encoding

W6 asked for "an SMT encoding of *V decreases on residual steps through
first descent, for all states in the finite window*". The clean encoding is
multiplicative. Substituting \(h_c=2^{g_c}>0\), the requirement that
\(\Phi(x)=\log_2x+g(C(x))\) be nonincreasing along \(f\) becomes, for every
observed transition \(x\mapsto y=f(x)\),

\[
\boxed{\;y\,h_{C(y)}\;\le\;x\,h_{C(x)},\qquad h_c>0.\;}
\]

This is **linear with integer coefficients**, so z3 decides it exactly over
the rationals — no logarithm is ever evaluated. And by LP duality it is
infeasible exactly when the coordinate digraph carries a cycle with
\(\prod y_i>\prod x_i\), i.e. a certificate in the sense of SH1/WITN1. So
the synthesis question and the certificate question are literally the same
question; the verifier answers both and cross-checks them against each other
on every coordinate tested.

Following WITN1's discipline, floats guide the Bellman–Ford negative-cycle
search and **every** promoted certificate is re-checked as an exact integer
comparison \(\prod y_i>\prod x_i\).

---

## 2. The premise check

Rediscovering certificates against the one-variable quantized-log
coordinate, by exact search over odd \(x\) in a range:

| \(j\) | \(m\) | odd \(x<\) | coords | certificate | \(\prod y/\prod x\) |
|---:|---:|---:|---:|---|---|
| 1 | 8 | 4000 | 1172 | yes, length 2 | \(8812067/7831075\) |
| 2 | 8 | 4000 | 1787 | yes, length 21 | \(6687037/5425981\) |
| 3 | 16 | 20000 | 11667 | none in range | — |

z3 independently reports UNSAT on the \(j=1,m=8\) system. The \(j=3,m=16\)
row finding nothing in range is expected rather than contrary: SUFF1's own
bound requires witnesses of bit-length at least
\(\Theta=m+K+j+\log_2(1/\min(\varphi_Q,1-\varphi_Q))+K/4+O(1)\), which
exceeds this search range. The row is reported rather than suppressed.

**Conclusion.** The one-variable class — including the quantized full
logarithm at any precision — is closed. W6's first deliverable as literally
written ("an UNSAT certificate at small quantization depth \(j\), which would
be a new finite no-go extending SH1") is already a ledger theorem.

---

## 3. The shadow on actual orbits

| \(n\) | orbit length | \(N^\ast(n)\) | running max |
|---:|---:|---:|---:|
| 11 | 26 | 6 | 8 |
| 51 | 37 | 10 | 11 |
| 101 | 128 | 9 | 12 |

Over \(3464\) states scanned, the best realised shadow depth is
\(N^\ast=12\), attained at \(n=63\), against the "random states" heuristic
\(\log_2 3464=11.8\). On the whole \(n=471\) orbit (733 pre-descent states)
the deepest is \(10\).

So the \(-5\) shadow behaves on repunit orbits exactly as a coincidence
should: the depth is logarithmic in the number of states, not unbounded. The
SH1 certificate is a statement about *arbitrary* integers; it is not
available at arbitrary depth inside a single orbit, and the SH1 shadow triple
\(1275\mapsto1913\mapsto1435\) does not occur on any tested repunit orbit at
all. This is what makes \(V(x,n)\) a genuinely different question rather than
a notational variant.

---

## 4. The two-variable search, and the vacuity diagnostic

| \(m\) | \(j\) | \((x,n)\) pairs | coords | compression | certificate | z3 | verdict |
|---:|---:|---:|---:|---:|---|---|---|
| 4 | 1 | 3464 | 994 | 0.713 | yes | unsat | **no-go** |
| 6 | 1 | 3464 | 2079 | 0.400 | yes | unsat | **no-go** |
| 8 | 2 | 3464 | 3211 | 0.073 | yes | unsat | **no-go** |
| 12 | 2 | 3464 | 3447 | 0.005 | no | sat | vacuous |
| 16 | 3 | 3464 | 3463 | 0.0003 | no | sat | vacuous |
| 24 | 3 | 3464 | 3464 | 0.000 | no | sat | vacuous |
| 32 | 4 | 3464 | 3464 | 0.000 | no | sat | vacuous |

*Compression* is \(1-\#\text{coords}/\#(x,n)\text{ pairs}\). The denominator
counts **pairs**, not integers: the same integer occurs in several orbits
with different coordinates, because the third component is relative to that
orbit's seed.

**The vacuity diagnostic is the methodological point of this session.** A
SAT answer means "some \(g\) works on this window". When compression is
\(\approx0\) the coordinate is injective on the window, every \(g\) is free,
and SAT reports the *absence of constraints* rather than a candidate
potential. Any synthesis run in this class must publish its compression
alongside its SAT/UNSAT verdict, or it will mistake an empty problem for a
solved one. **No SAT answer in the table above is claimed as a candidate
\(V\).**

The consequence for future work is specific: at fine coordinates the window
must be enlarged (more orbits, hence more coordinate returns), not the
solver. A bigger SMT solver on \(n\le101\) will keep returning the same
uninformative SAT.

The smallest certificate found, exactly:

\[
x_1=5182891940559758051838133792379\ \mapsto\ y_1=7774337910839637077757200688569,
\]
\[
x_2=7774337910839637077757200688569\ \mapsto\ y_2=5830753433129727808317900516427,
\]

a length-2 coordinate cycle at \((m,j)=(4,1)\) with

\[
\frac{y_1y_2}{x_1x_2}
=\frac{5830753433129727808317900516427}{5182891940559758051838133792379}>1 .
\]

Both witnesses are genuine pre-descent states of repunit orbits.

---

## 5. Constraints from the ledger, checked

W6 imposes hard constraints. Each is respected:

- *No claim of one-step decrease for all odd \(x\)* (SH1) — nothing here
  claims a decreasing potential at all; the positive results are all no-gos.
- *No bounded correction to \(\log_2x\)* (BND1) — the coordinate alphabets
  used are finite but the correction is not asserted bounded; and no
  candidate is promoted.
- *Must read quantized-log bits or genuine second-variable data* — §4's
  coordinate reads both.
- *Stress on the SH1 shadow family* — reproduced exactly
  (\(8\cdot1435=9\cdot1275+5\), gain \(287/255\)), and shown **not** to occur
  on any tested repunit orbit, so it cannot by itself refute a two-variable
  \(V\).
- *Stress on the \(n=471\) blocked-diffuse phase* — 733 pre-descent states,
  deepest shadow \(10\), consistent with §3.

---

## 6. Barrier check

1. *Finite-state information.* The certificates of §4 are finite-state
   objects, used **negatively** (to refute potentials). Barrier 1 forbids
   using finite-state information to control the least representative; it
   does not forbid using it to kill a proposed potential, which is what SH1
   itself does.
2. *Density / entropy.* Not invoked.
3. *Variable-height Diophantine.* Not invoked.
4. *Virtual sources.* **Respected, and it is the substance of §3.** SH1's
   witnesses are constructed integers; §4's are actual repunit-orbit states.
   The distinction is exactly why the two-variable class is not already
   closed.

**Explicit non-claims.** No candidate potential is proposed. W6-C is a finite
certificate over \(n\le101\) at three coordinate resolutions, not a theorem
about all \(n\) or all \(m\). Nothing here bears on descent.

---

## 7. Falsifier

- **W6-KILL-A** is falsified by showing SUFF1 does not in fact cover some
  \((j,m)\); the independent rediscovery in §2 is the check.
- **W6-B** is falsified by a repunit orbit with \(v_2(x_i+5)\) far above
  \(\log_2(\#\text{states})\) — which would restore the universal shadow on
  orbits and close the two-variable class immediately.
- **W6-C** is falsified by any of its cycles failing the exact integer
  comparison \(\prod y>\prod x\), or by z3 returning SAT where the cycle
  search returns a certificate. The verifier checks the two procedures agree
  on every row.
- **The vacuity diagnostic** is falsified by a SAT answer at compression
  bounded away from \(0\) — that *would* be a real candidate \(V\), and is
  the outcome a larger window should be run to look for.

---

## 8. What a next session should do

Not a better solver. A bigger window. Concretely: run §4's search over
\(n\le1001\) or beyond with the compression column monitored, and look for
the first \((m,j)\) at which SAT occurs while compression is still, say,
\(>0.1\). That would be a genuine candidate \(V(x,n)\), at which point the
symbolic-verification and \(n=471\) stress steps of W6's protocol apply. The
z3 solve is the bottleneck (\(n\le201\) already takes about a minute); the
Bellman–Ford side scales much better and can run alone, with z3 reserved for
confirming the boundary rows.

---

## 9. Verification

```bash
python3 scripts/verify_machine_synthesis.py              # n <= 101, ~9 s
python3 scripts/verify_machine_synthesis.py --nmax 201   # ~1 min
```

Prints `MACHINE-SYNTHESIS: PASS`. Requires `z3-solver` for the SMT
cross-checks; without it the script still runs and reports the exact
certificate search alone.

---

## 10. Suggested ledger rows (not applied)

| ID | Statement | Status | Source |
|---|---|---|---|
| MSY1 | The one-variable quantized-log class is closed at every precision (SUFF1+CONN1); independently rediscovered certificates at \((j,m)=(1,8),(2,8)\) | Finite certificate (re-derivation) | §2 |
| MSY2 | On repunit orbits the realised \(-5\) shadow depth is \(N^\ast=12\) over 3464 states (\(10\) on \(n=471\)), i.e. logarithmic in the state count; SH1 gives only a finite no-go there | Finite certificate | §3 |
| MSY3 | Certificates exist on the two-variable coordinate \((x\bmod2^m,\tau,\lfloor Q\log_2x\rfloor-\lfloor Q\log_2a_n\rfloor)\) for \((m,j)=(4,1),(6,1),(8,2)\) over \(n\le101\), with witnesses actual orbit states | Finite certificate | §4 (W6-C) |
| MSY4 | A SAT answer in this class is meaningful only alongside its compression \(1-\#\text{coords}/\#(x,n)\); at compression \(\approx0\) SAT reports an empty problem | Proved here (methodological) | §4 |

MSY4 is the row worth keeping even if the others are not promoted: it is the
methodological precondition for any future synthesis run in this class.
