# Residual Atlas

**Status:** Side-project research programme. **Demoted from descent route
(outcome 1: cover failure).** Retained as a classification framework for the
mechanical \(3/4\)-block language \(\mathcal L_{3/4}\) and the IEF17 residual
\(\mathcal R\) inside it. It does not prove repunit-tail descent or the
Collatz conjecture. Authoritative claim status remains `CLAIM_LEDGER.md`.

Decision record:
[`docs/residual-atlas/PHASE_CHECKPOINT.md`](docs/residual-atlas/PHASE_CHECKPOINT.md).

Working notes live in
[`docs/residual-atlas/`](docs/residual-atlas/README.md). Exact discharge
theorems live in `docs/repunit/integral_escape_frontier.md` (IEF1--IEF21).
Ordered covering mechanics live in `docs/repunit/coverage_portfolio.md`.
Chronological development remains in `RESEARCH_ROADMAP.md`.

## 1. Premise

There need not be one local mechanism that makes every odd integer descend.
A proof may be a **portfolio of sound rules** whose residual positive-integer
intersection is empty.

The atlas therefore rejects:

- a single global one-step potential (already impossible for large classes:
  SH1, SH2, BND1);
- a single finite-modulus forced-descent tree (COR3: undischarged frontier
  branching factor \(2\rho^{1/\theta}=1.9318\ldots\));
- treating density-one statements as universal covers;
- launching broad censuses that do not test a named residual predicate.

The atlas accepts:

- many complementary descent-or-merge rules;
- a nonempty \(2\)-adic Cantor residual, provided it contains no positive
  integer (IEF1--IEF2);
- tools invented only after a residual class is thin enough to name a
  Diophantine obstruction.

## 2. Targets (do not conflate)

| Target | Meaning | Terminal condition |
|---|---|---|
| **Qualitative repunit descent** | For every odd \(n>1\), some \(f\)-iterate of \(a_n=(3^n-1)/2\) falls below \(M_n=2^n-1\) | Residual atlas empties for positive integers (IEF2) |
| **Quantitative window** | \(\sigma(a_n)\le 3n\) (provisional constant) | Needs plateau / surplus control beyond IEF |
| **Full Collatz** | Every odd \(x\) eventually descends | Separate reduction; this atlas attacks the Mersenne--repunit spine residual |
| **Cycle exclusion** | No nontrivial positive cycle | Separate cycle ledger (CYC1--CYC4); not part of IEF17 |

This document's live object is the **qualitative** residual. Quantitative
plateau bounds must be labelled as such and must not be inferred from
IEF10--IEF21.

## 3. Proof architecture

```text
odd exponent n
    │
    ├─ direct descent below M_n          → discharge
    ├─ merge to strictly smaller exponent → inductive discharge
    └─ primitive residual
            │
            ├─ ancestry / low-height / concentrated PCD branches
            │       → existing or pending discharge rules
            └─ blocked-diffuse terminal language
                    │
                    └─ IEF17 survivor profile  ← live atlas object
                            │
                            └─ shrink coordinates until empty
```

A rule is a **discharge rule** only if it proves descent or a
strictly-smaller merge. Classification, density, and finite observation are
not discharges until they supply one of those implications
(`coverage_portfolio.md` §2).

**Cover warning.** Emptying \(\mathcal R\) proves absence of positive-integer
survivors only inside the language in which \(\mathcal R\) is defined. If
blocked-diffuse primitives need not enter that language, the atlas is a
classification framework, not a descent route. That is lemma **L5**.

## 4. The live survivor object (IEF17)

After FIN1 and IEF13--IEF21, any non-cyclic positive-integer survivor whose
terminal itinerary lies in the \(3/4\)-block language must satisfy **all** of
the following simultaneously:

| ID | Coordinate | Necessary survivor condition | Source |
|---|---|---|---|
| A | Starting size | \(x_0>10^6\) | FIN1 |
| B | Density drift | \(\liminf S_L/L=0\) | IEF16 |
| C | Symbolic / drift axis | \(\operatorname{dio}(w)=1\) **or** \(\limsup S_L/L>0\) | IEF16 + IEF19 |
| D | Periodic-prefix margin | No useful approximant sequence has divergent IEF18 margin; in particular every fixed-surplus sequence retains linear IEF21 terminal draw-up or endpoint loss | ¬IEF18, ¬IEF21 |
| E | Negative excursions | Along every \(L_k\) with \(S_{L_k}\to-\infty\), eventually \(Z_{L_k}>64\cdot10^6/65\) | IEF15 + FIN1 |

**Live residual.**

\[
\mathcal R
=
\{\text{itineraries satisfying A}\cap\text{B}\cap\text{C}\cap\text{D}\cap\text{E}\}.
\]

IEF17 proves that every non-cyclic positive-integer survivor in this terminal
language lies in \(\mathcal R\).

**Update (IEF22--IEF24).** The dual-digit escape Theorem G (`dio1_cocycle_problem.md`)
proves that no infinite \(\{3,4\}\)-block word has an eventually-zero IEF4
digit stream. With IEF7 this excludes every positive integer from realizing
an infinite itinerary in \(\mathcal L_{3/4}\) in the integrality sense
(IEF24). Thus \(\mathcal R\) contains no positive-integer survivor.
Cover lemma **L5** remains: this empties the residual *inside*
\(\mathcal L_{3/4}\), and does not by itself prove every blocked-diffuse
primitive enters that language.

Cyclic trajectories are excluded from \(\mathcal R\) by definition of the
ledger and remain on the cycle track.

## 5. Discharged layers (do not reopen)

These are already removed from the qualitative terminal residual. New work
must not re-prove them as the main programme:

| Layer | Status |
|---|---|
| Local one-step potentials of SH1/SH2/BND1 type | Impossible |
| Fixed 256-block floor as standalone theorem | Obstructed (REPLOW) |
| Shallow multi-gap sync trees as exhaustive cover | Insufficient mass |
| Compressed collision-defect state | Not closed (COLDEF2) |
| Canonical single-partner ancestry for \(q\equiv3,4\pmod6\) | Impossible (GPA2) |
| Deterministic balanced \(q=3\) itinerary | Discharged (IEF10) |
| Fixed phase shifts of the balanced word | Discharged (IEF11) |
| All critical-slope Sturmian intercepts | Discharged (IEF12) |
| Bounded critical discrepancy + \(\operatorname{dio}>1\) | Discharged (IEF13) |
| Adaptive discrepancy beaten by agreement surplus | Discharged when margin \(\to\infty\) (IEF14) |
| Sustained negative drift with bounded \(Z\) | Finite reduction (IEF15) |
| Nonzero linear lower drift either sign | Excluded (IEF16) |
| Sublinear prefix drift + \(\operatorname{dio}>1\) | Discharged (IEF19) |
| Fixed-surplus reps in critical windows / valley transitions | Discharged under IEF20/IEF21 hypotheses |

## 6. Operating protocol

Every proposed lemma must state:

1. **Applicability predicate** with explicit quantifiers.
2. **Logical role:** discharge (descent or smaller merge), residual shrink
   (deletes part of \(\mathcal R\)), classification only, or tool request.
3. **Coordinate hit:** which of A--E it shrinks, and whether the shrink is
   unconditional or conditional on an approximant family.
4. **Dependencies** already in the claim ledger.
5. **Residual after:** the exact intersection that remains.
6. **Falsifier:** the smallest counterexample shape the lemma must survive.

Promotion rules:

- Promote to `CLAIM_LEDGER.md` only under the usual admission rule.
- Recompute \(\mathcal R\) after every promoted shrink.
- Do not launch a broad census unless it tests a named predicate on
  \(\mathcal R\).
- Do not add percentages from different universes.
- Do not treat a positive finite diagnostic margin as a discharge.

## 7. Bounded-phase checkpoint

This atlas is a **side project** for a bounded research phase. It is not yet
the main programme bet.

### Phase goals

1. Establish **L1** (bookkeeping partition of coordinate C).
2. Formalize exactly what **L5** must prove (universe, predicates, exotic
   remainder).
3. Aggressively attempt to **falsify** the key implications proposed for
   **L2--L4**, using constructed symbolic itineraries before inventing proofs.
4. Decide promote / demote using the outcomes below.

### Promote (keep as a route to qualitative descent)

All of:

- L5 is either proved, or reduced to a named exotic class with an exact
  normal form that replaces the \(3/4\)-block universe;
- at least one of L2--L4 exhibits a forced **arithmetic** coupling between
  terminal words and fixed positive integers (cylinder lift, carry match,
  ancestry, or comparable exact constraint), not merely a combinatorial
  wish;
- the residual after those shrinks is either empty or a single precise
  Diophantine tool request (**L6**).

### Demote outcome 1 — cover failure

L5 fails or remains incomplete: \(\mathcal R\) is not known to contain every
primitive blocked-diffuse residual.

**Action.** Retain IEF1--IEF21 as local theorems about the \(3/4\)-block
language. Stop presenting the atlas as a route to spine descent. Return the
main programme to cover / ancestry / surplus work outside \(\mathcal R\).

### Demote outcome 2 — coupling failure

L5 holds (or exotic remainder is named), but L2--L4 produce no arithmetic
coupling: itineraries in \(\mathcal R\) are easy to construct that evade the
hoped-for taxes.

**Action.** Retain the atlas as a **rigorous residual-classification
framework** and record the open core as an L6-style Diophantine statement.
Do not claim a descent route from emptying \(\mathcal R\) until new tools
appear.

### Decision log

Record the phase decision in
[`docs/residual-atlas/PHASE_CHECKPOINT.md`](docs/residual-atlas/PHASE_CHECKPOINT.md).

**Provisional lean (2026-07-14):** ~~demote-1 on cover~~ → **hardened to
demote outcome 1**. Reason: \(n=471\) never enters \(\mathcal L_{3/4}\) on
its full 732-step descent, and \(\mathcal E_{\mathrm{mix}}\) acquired no
normal form (`docs/residual-atlas/E_mix_seed.md`,
`docs/residual-atlas/PHASE_CHECKPOINT.md`). The atlas is retained only as a
classification framework for \(\mathcal L_{3/4}\), not as a spine-descent
route.

**Postscript (2026-07-19).** IEF22--IEF24 empty the positive-integer
residual inside \(\mathcal L_{3/4}\) (L6 local discharge recorded in
`PHASE_CHECKPOINT.md`). Demote-1 is unchanged. Primary programme returns to
Avenue A / first-descent storage-dominance
(`docs/no-go/avenue_a_comparison_dynamics.md`) and the transfer fan.

## 8. Next lemmas (checkpoint order)

Each item is a candidate, not a claim. Order follows the bounded-phase plan,
not mathematical depth alone.

### L1 — Split coordinate C into named residual classes

**Role.** Bookkeeping. Do immediately; do not treat as mathematical progress.

**Goal.** Partition \(\mathcal R\) into

- \(\mathcal R_+\): \(\limsup S_L/L>0\) (with B still holding);
- \(\mathcal R_1\): \(\limsup S_L/L=0\) (hence \(\operatorname{dio}(w)=1\) by C).

**Working note.**
[`docs/residual-atlas/L1_coordinate_split.md`](docs/residual-atlas/L1_coordinate_split.md)

### L5 — Terminal-language classification (cover lemma)

**Role.** Most important step for the atlas as a descent route.

**Goal.** Prove that every infinite blocked-diffuse PCD residual is either:

- already covered by IEF11--IEF21, or
- eventually enters the \(3/4\)-block terminal language (hence lies under
  \(\mathcal R\)), or
- a member of one explicitly named exotic class with an exact normal form.

**Why.** Emptying \(\mathcal R\) without L5 does not establish qualitative
repunit descent.

**Working note.**
[`docs/residual-atlas/L5_terminal_language_target.md`](docs/residual-atlas/L5_terminal_language_target.md)

### L2 / L3 — Exploratory after falsification

Attempt to falsify before proving. Log attempts in
[`docs/residual-atlas/falsification_log.md`](docs/residual-atlas/falsification_log.md).

#### L2 — Recurrence tax on the \(\operatorname{dio}=1\) branch

**Goal.** Show that \(\operatorname{dio}(w)=1\) plus terminal PCD/cylinder
ancestry forces either a divergent IEF18/IEF21 margin family, return to a
discharged language, or a named exotic normal form.

#### L3 — Excursion localization on the positive-limsup branch

**Goal.** Show that every itinerary in \(\mathcal R_+\) admits a fixed-surplus
periodic-prefix family with sublinear IEF21 costs \(H_k,L_k\), or else an
exact structural obstruction dischargeable by another rule.

### L4 — Negative-valley replenishment tax

**Role.** Potentially the most promising *mechanism*, because it couples E
with D instead of treating survivor conditions independently.

**Goal.** On \(\mathcal R\), show that maintaining \(Z_{L_k}>B_X\) along every
deep negative excursion forces a divergent directional margin or a return to
a discharged discrepancy class.

**Caution.** Only attempt seriously after L5's universe is fixed; coupling
inside the wrong language is not a descent proof.

### L6 — Tool request (stopping rule)

When a residual class is reduced to a single Diophantine sentence, record it
as a tool request. Isolating a precise unsupported statement is valuable even
if it remains open. Example shape:

> No fixed positive integer realizes an aperiodic critical itinerary with
> \(\operatorname{dio}(w)=1\), density-critical lower drift, bounded IEF18
> margins on every useful periodic-prefix family, and partition
> replenishment above \(B_X\) on every deep negative valley.

## 9. Parallel avenues (atlas-compatible only)

Side tracks are welcome only when they invent a **new sound discharge rule**
or a **named residual predicate**. Otherwise they are diagnostics.

| Avenue | Atlas role | Admission test |
|---|---|---|
| Fuse / episode cumulative payout | Possible discharge for high-discrepancy excursions | Must reduce to descent or smaller merge on a stated class |
| Merge-inheritance + primitive-only surplus | Shrinks the universe before \(\mathcal R\) | Already partly in place; extend only with exact local criteria |
| Entropy / Kolmogorov notes | Predicate or no-go only | Must name a residual set it empties |
| Shortcut-map `6n` equidistribution | Separate empirical track | Not a substitute for accelerated-map \(\mathcal R\) |
| Cycle ledger | Parallel, mandatory for full Collatz | Keep separate from IEF17 |
| Computer-assisted discovery | Supporting | Tests a named L1--L6 predicate; no blind enlargement of certificates |

## 10. Immediate execution order

1. Establish **L1** in `docs/residual-atlas/L1_coordinate_split.md`.
2. Formalize **L5** as a precise theorem target in
   `docs/residual-atlas/L5_terminal_language_target.md`.
3. Aggressively falsify proposed **L2--L4** implications; log results.
4. Apply the §7 promote / demote checkpoint; write the decision in
   `docs/residual-atlas/PHASE_CHECKPOINT.md`.
5. Keep `docs/repunit/next_generation_attack_program.md` and the main
   roadmap as the primary programme until the atlas is promoted.

## 11. Guardrails (short)

- \(\mathcal R=\emptyset\) (IEF24) is a theorem only inside the language of
  \(\mathcal R\); L5 is required for a spine route and remains demoted.
- Nonempty \(2\)-adic ghosts are allowed.
- Finite diagnostics are not discharges.
- IEF10--IEF24 do not imply \(\sigma(a_n)\le3n\).
- Percentages are prioritization tools, not covers.
- Do not bet the whole programme on this atlas; live spine work is Avenue A
  / SD1 after demote-1.

## 12. Related files

- `docs/residual-atlas/` — side-project working notes
- `CLAIM_LEDGER.md` — claim status
- `docs/repunit/integral_escape_frontier.md` — IEF1--IEF21
- `docs/repunit/dio1_cocycle_problem.md` — IEF22--IEF24 (local dual-digit escape)
- `docs/no-go/avenue_a_comparison_dynamics.md` — live SD1 attack
- `docs/repunit/coverage_portfolio.md` — ordered cover mechanics
- `docs/repunit/payout_concentration_diffusion.md` — PCD residual language
- `docs/repunit/next_generation_attack_program.md` — attack tactics
- `RESEARCH_ROADMAP.md` — chronological programme
