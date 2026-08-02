# Opus 5 wide attack — results and handoff

Companion to `OPUS5_WIDE_TASKS.md`. All twelve tasks in that file's
recommended order were run, one per session. This file is the synthesis: what
changed, what closed, what to do next, and what went wrong along the way.

**Suite:** `python3 scripts/run_all_wide_attack.py` (all sessions plus the
repository's own gatekeepers; `--quick` skips the one row needing `z3`).
**`CLAIM_LEDGER.md` was not edited.** Proposed rows are consolidated in §5.

---

## 1. The one real gain

Everything else on this list is a closure or a scoping result. One task moved
the maintained programme forward:

> **W9 eliminated the Baker hypothesis from Avenue A's \(L=1\) gates.**
> Lemmas SD-L1-e2-preimage-Baker, SD-L1-s4-Baker and SD-L1-s-Baker (for
> \(3\)-smooth \(s\)) previously read "standard lower bounds … give … for all
> large \(n\), whenever \(K_\downarrow=n^{O(1)}\)". They now read: *for every
> odd \(n\ge161\), by Rhin's explicit proposition, under the concrete
> hypothesis \(K_\downarrow(n)\le6n\)*. Since \(161\) sits inside the existing
> scan range, nothing is left over. Two conditional inputs became one, and
> the survivor is an arithmetic hypothesis rather than a transcendence one.

The enabling observation was that **every** Baker/irrationality invocation in
the repository is a linear form in exactly two logarithms, and in six of the
eight cases the two logarithms are \(\log2\) and \(\log3\) — for which a fully
explicit published bound exists and had never been substituted in.

---

## 2. Outcome table

| # | task | verdict | the finding |
|---|---|---|---|
| W9 | explicit Baker constants | **advanced** | all invocations are two-log; crossover \(n\ge161\); BAKER1–3 gains the exact closed form \(v_2(3^m+7)=2+v_2(m-\alpha)\), so its finite-range envelope needs no theorem (true max \(K=17\) at \(n=1197\) vs the empirical \(30\log_2(n+1)+10\)) |
| W2 | certificate semigroup | closed | transport rules are forward-orbit (void), one-parameter (\(\Theta((\log X)^2)\), countable \(2\)-adic closure), or unrestricted predecessors (= the conjecture). Incidental: **TWR1 \(=P_2^{\,d}\)** |
| W11 | rotation-cocycle rigidity | closed | fibre map expands \(2\)-adically by \(2^{\delta_m}\), Lyapunov exponent \(5+\beta\); not a compact-group extension, so Furstenberg/Veech/Denjoy–Koksma are inapplicable. Output: \(C=\lfloor3^n/2^{E+2}\rfloor\) |
| W10 | digit arithmetic / Stewart | closed | bridge exists at the best height \(c=1\), but PCD10 makes \(3^{n_m}\) have \(2^{\Theta(E_m)}\) digits against an \(O(E_m)\) window; Stewart is vacuous **and anti-correlated** with plateau length |
| W1 | additive superposition | closed | defect is a **slope** mismatch of trajectory size, not carry bookkeeping; pincer between empty agreement regime and a virtual part |
| W8 | two-tower interference | closed | closed-form lanes for every alignment, but all resolve onto ghosts already held (\(-1\), \(-1/3\), \(-3^{-k}\), \(\Lambda_d\)) |
| W6 | machine synthesis | **premise corrected**; new finite no-go | quantized-log class already closed by SUFF1+CONN1; the two-variable \(V(x,n)\) class survives, and certificates exist there from actual orbit states |
| W13 | extremal calibration | calibrated | Cramér–Lundberg, **not** Bramson; \(\gamma=\log2\) exactly (measured slope \(-1.0103\)); plateaus are \(\Theta(\log m)\), constant \(0.1845\) |
| W4 | Krasikov–Lagarias rails | closed | rail restriction is free (bounded-suffix condition); density cannot reach an \(O(\log x)\) family at any exponent |
| W5 | Syracuse 3-adic | closed | conditioning vacuous (seed forgotten mod \(3^k\) once \(K\ge k\)); ensemble ≠ single orbit |
| W7 | IEF17 / words | **frontier sharpened** | coordinates 2–4 generic (combinatorics-on-words spent); coordinate 5 (IEF15+FIN1) binding and it discharges the generic word by \(1.7\times10^3\) |
| W3 | carry cocycle | collapsed | \(v_2(\Pi(n))=\tau(n)\); the two models are **anti-correlated**, not close |

---

## 3. Three filters, and what they are for

The same distinction kept reappearing from different directions. Each is
cheap to check and would have saved a session had it been available first.

1. **Rational vs irrational \(2\)-adic ghosts** (W8 §4.1). Every exact lane
   this repository owns shadows a *rational* \(2\)-adic point — \(-1\)
   (Mersenne burn), \(-1/3\) (the \(\sigma\)/recharge limit),
   \(\Lambda_d=1-2(4/3)^d\) (TWR1), \(-3^{-k}\) (block constants),
   \(\Xi_{d,d'}\) (two-tower). Every open object shadows an *irrational* one:
   \(\alpha\) with \(3^\alpha=-7\), \(\alpha_A\) in general, the balanced
   ghosts \(u_\infty\) and \(\alpha_\infty\). Rational ghosts are solvable
   because \(f\) and \(P_2\) act affinely with small denominators.

2. **Which prime carries the information** (W5-D). \(f(x)=(3x+1)/2^e\)
   contracts \(3\)-adically at \(\log3=1.099\) — destroying seed information —
   and expands \(2\)-adically at \(\mathbb E[e]\log2=1.397\) — creating it.
   Methods that manufacture equidistribution (Tao's Syracuse machinery) work
   on the destroying side and therefore cannot see an individual orbit.

3. **The polynomial analogue is anti-correlated** (W3). \(v_2(\Pi(n))=\tau(n)\):
   the \(\mathbb F_2[x]\) model's valuation is the trailing-ones count, so its
   largest divisions land exactly on the burn states where the integer model's
   are smallest. \(\min(e,v)=1\) always. The solved model is not an
   approximation to this one.

**Use:** before spending a session importing an outside method, check it
against these three. A method that only sees rational ghosts, or lives on the
\(3\)-adic side, or borrows from \(\mathbb F_2[x]\), will not reach the open
objects.

---

## 4. What the frontier looks like now

Three sessions converged, from three different directions, on **one object**:

> **Single-orbit equidistribution of a deterministic sequence built from
> powers of 3.**

- **W11** reached it from the ergodic side: the plateau system is not a
  compact-group extension, so no every-point theorem is available.
- **W10** reached it from the arithmetic side: Stewart bounds a *global*
  nonzero-digit count, while the plateau needs a *local* run bound at a
  prescribed position.
- **W5** reached it from the distributional side: Tao's decrement is an
  *ensemble* statement, and there is no ensemble along one orbit.

Nothing in the current literature supplies it. The concrete thing to watch
for is a **local** digit theorem for \(3^R\) — a bound on runs of prescribed
digits in a window at a prescribed position, with an effective constant.
W10 §2 has the bridge already in place to receive one.

Separately, **W7 relocated the IEF17 frontier**: its symbolic coordinates are
generic, and the content sits entirely in coordinate 5 (IEF15 + FIN1).

---

## 5. Proposed ledger rows, consolidated

Twenty-five rows were proposed across the notes. **None applied.** Grouped by
what they would be worth:

**Worth promoting (exact, with verifier and falsifier):**

| ID | note | statement |
|---|---|---|
| DBC1 | W10 §1 | the general ghost identity \(v_2(3^n-A)=2+v_2(n-\alpha_A)\) — **supersedes BAKEX3**, which is the \(A=-7\) case; file as one row |
| BAKEX1 | W9 §2.1 | \(\|q\log_23\|\ge(2.085q)^{-13.3}/\log2\) (Rhin, applied) |
| BAKEX2 | W9 §3.2 | the Avenue A gates for \(n\ge161\) under \(K_\downarrow\le6n\), no Baker hypothesis |
| CSG1 | W2 §3 | TWR1 \(=P_2^{\,d}\), with the domain condition recovered |
| RCR3 | W11 §4 | \(C=\lfloor3^n/2^{E+2}\rfloor\) and the plateau-as-digit-agreement reformulation |
| SIL1, SIL3 | W1 §1 | the \(I_T\) expansion and the \(\frac56\) slope-defect bound |
| TTI1 | W8 §1 | the two-tower ghost algebra |
| W3 | §0 | \(v_2(\Pi(n))=\tau(n)\) — no ID assigned; small but the cleanest statement of why the analogue is easy |

**Finite certificates (file, do not promote):** BAKEX4, CSG2, CSG3, RCR2,
RCR4, SIL2, SIL4, TTI2, TTI3, MSY1, MSY2, MSY3.

**Methodological (worth keeping even if nothing else is):** CSG4, CSG5
(forward-orbit rules are void), DBC3, TTI4 (foreclosures), **MSY4** — a SAT
answer in the potential-synthesis class is meaningless unless its coordinate
compression is published alongside.

**No rows proposed** by W13, W4, W5 or W7: those are navigation and scoping.

---

## 6. Corrections made mid-flight

Four substantive errors were caught and fixed. Recording them because each is
a trap a future session could fall into again.

| session | the error | how it surfaced | fix |
|---|---|---|---|
| W11 | used `analyse()`'s lift digit as the *plateau* indicator; it is the IEF **starting-cylinder** lift, a different \(2\)-adic ghost | zero counts (43) disagreed with PCD12's (39) | boxed correction in W11 §3 + §7bis; W11-A/B/C unaffected |
| W6 | accepted the task's premise that the quantized-log class was unsearched | checked it against SUFF1+CONN1 before building | premise correction is now the headline of the note |
| W13 | followed the task's suggestion of a Bramson correction | the object is an excursion height over independent seeds, not a common-depth branching walk | Cramér–Lundberg instead; \(\gamma=\log2\) comes out exactly |
| W5 | compared 3-adic residues to uniform, then to uniform-on-units | a stable TV of 0.28–0.35 that would not shrink with sample size | modelled the true Syracuse law; the residual bias vanished |

Two near-misses worth the same treatment: in **W7** I expected \(Z_L\) at
record lows to inherit \(\Theta(\sqrt L)\) local time and was wrong (the
minimum sits at the *edge* of the range, not the bulk) — the measurement
caught it and inverted the conclusion; in **W4** my first enumeration
measured a depth truncation rather than the tree, because the realised
integer set is conjecturally everything and carries no exponent information.

**The pattern:** in five of the six cases the error was a *wrong reference
object* — wrong stream, wrong law family, wrong measure, wrong set. The
generic fix was to compute the correct reference from first principles rather
than reach for the nearest standard one.

---

## 7. What to do next

**Cheap and concrete.**

1. **Extend FIN1's cutoff.** \(B_X=64X/65\) scales linearly with \(X\), and
   W7 shows coordinate 5 is the single binding IEF17 coordinate. Raising
   \(X\) from \(10^6\) strictly strengthens the IEF15 discharge. Unusually for
   this repository, more computation buys ground rather than another census.
   The efficient route is a residue-class sieve mod \(2^k\), not an
   integer-by-integer scan.
2. **Decide the ledger rows** in §5. The DBC1/BAKEX3 duplication should be
   resolved before either is promoted.
3. **Check W13's forward predictions** if the PCD census is ever extended:
   first PCD-length-4 plateau near \(m\approx7.8\times10^4\), and **none
   below \(m\approx2\times10^4\)**. The second is cheap and would falsify the
   calibration outright.

**Bounded and worthwhile.**

4. **W6 at a bigger window.** The two-variable synthesis returns vacuous SAT
   at fine coordinates because the window (\(n\le101\)) has no coordinate
   returns. It needs more orbits, not a better solver — the Bellman–Ford side
   scales fine and z3 is the bottleneck. Watch for the first \((m,j)\) with
   SAT at compression \(>0.1\).
5. **W10-E**: instantiate Bugeaud–Laurent to get a numeral for \(C_7\). Low
   priority — the exact ladder already beats it in every finite range — but
   it would complete the audit's unconditional tail.

**Not worth a session** (recorded so it is not re-attempted): further
combinatorics-on-words on IEF17 (W7); density restrictions on the mod-8 rails
(W4); tower normal forms as a lane source (W8); importing the
\(\mathbb F_2[x]\) theorem (W3); certificate-transport semigroups (W2);
additive superposition (W1).

---

## 8. Scope and honesty

Nothing in these twelve sessions proves the Collatz conjecture, produces a
descent, or eliminates a cylinder. The single advance is W9's removal of one
conditional input from three Avenue A lemmas. Everything else either closes a
proposed route, corrects a stale premise, or relocates a frontier.

All claims are backed by exact integer or rational arithmetic where they are
asserted as claims; floats appear only in measurements explicitly labelled as
such. Every note carries its own falsifier section. `CLAIM_LEDGER.md` is
unchanged and its validator still passes at 134 rows.
