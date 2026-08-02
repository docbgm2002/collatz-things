# Notes

Research notes are grouped by topic:

- [`core/`](core/) - base map identities, residue rails, and parity-vector notes.
- [`no-go/`](no-go/) - potential-function no-go theorems, tower/spine synthesis,
  closed outside-box triage, and the outside-box avenue portfolio.
- [`density-cycles/`](density-cycles/) - survivor-density, stopping-time, and
  cycle-reduction notes.
- [`repunit/`](repunit/) - Mersenne-to-repunit structure, rail-5 analysis, tail
  merging, low-prefix obstructions, Baker diagnostics, and extremal ledgers.
- [`fuse/`](fuse/) - fuse-map and binary-fuel exploratory tracks.
- [`nested-anchor/`](nested-anchor/) - nested anchor escape and route diagnostics.
- [`diagnostics/`](diagnostics/) - broad exploratory diagnostics and probabilistic
  or entropy viewpoints.
- [`residual-atlas/`](residual-atlas/) - bounded side-project working notes for
  the residual-atlas checkpoint (`RESIDUAL_ATLAS.md`); not a claim chain.

The root [`README`](../README.md) and [`claim ledger`](../CLAIM_LEDGER.md)
remain the main entry points.

## Status hierarchy

- The claim ledger is authoritative for maintained mathematical claims.
- A note's status banner says whether it is proved, known/rederived, finite,
  conditional, open, or exploratory.
- Maintained ledger rows must already appear in the root ledger; note-local
  ledger tables are explanatory copies, not pending proposals.
- The roadmap is a chronological research record. Later checkpoints supersede
  earlier plans when they conflict.
- Files under `archive/` and root-level edit logs are provenance, not theorem
  dependencies.

## Current reading paths

The Opus 5 wide-attack portfolio (W1--W13) is complete; its synthesis is
[`../OPUS5_WIDE_RESULTS.md`](../OPUS5_WIDE_RESULTS.md), and the whole suite
runs with `python3 scripts/run_all_wide_attack.py`. The per-task notes are
listed below.

For the mature no-go results, read `no-go/shadow_certificate.md`,
`no-go/leading_digit_nogo.md`, `no-go/tower_theorem.md`, and
`no-go/spine_synthesis.md`.

For the exact density result, read `density-cycles/corridor_rate.md`.

For the digit-theoretic route to the plateau problem, read
`no-go/digit_bridge_ceiling.md` (task W10). It consolidates the elementary
\(2\)-adic ceiling into one ghost identity covering BAKER1--3, confirms the
bridge to digits of \(3^{n_m}\) at height \(c=1\), and then shows Stewart's
bound is vacuous there: PCD10 makes \(3^{n_m}\) have \(2^{\Theta(E_m)}\)
digits against a window of width \(O(E_m)\), and the guarantee weakens as the
plateau lengthens. Only a *local* digit theorem would reopen it.

For the ergodic-theory route to the plateau problem, read
`repunit/rotation_cocycle_rigidity.md` (task W11). It closes the avenue: the
balanced endpoint recursion multiplies \(2\)-adic distance by \(2^{\delta_m}\)
per block (PCD15 restated as a Lyapunov exponent \(5+\beta\)), so it is not a
compact-group extension of the Sturmian rotation and Furstenberg /
Veech–Oren–Conze / Denjoy–Koksma are inapplicable. Its useful output is
RCR3: \(C=\lfloor3^n/2^{E+2}\rfloor\), so a plateau run is exactly an
agreement between the affine lift word and a window of the binary digits of
\(3^n\) — W10's bridge lemma on the plateau branch, at height \(c=1\).

For the \(\mathbb F_2[x]\) analogue as a source of transfer, read
`no-go/carry_cocycle_polynomial_model.md` (task W3). The decomposition
\(3n+1=\Pi(n)+2\kappa(n)\) is exact, and \(v_2(\Pi(n))=\tau(n)\): the
polynomial model's valuation is the trailing-ones count, so its largest
divisions land exactly on the burn states where the integer model's are
smallest. The two dynamics are anti-correlated, not close, and any aggregate
of \(\kappa\) collapses to \(c_K\).

For the symbolic frontier, read `repunit/ief17_genericity.md` (task W7).
IEF17's coordinates split: 2--4 are generic in the critical ensemble (so
combinatorics-on-words is spent as an attack), while coordinate 5 --
IEF15 + FIN1, the only one carrying an arithmetic input -- fails generically
and discharges the random word by a factor \(1.7\times10^3\). The residual
is measure-zero, not generic, and raising FIN1's cutoff tightens it linearly.

For the Syracuse / Tao machinery, read
`repunit/syracuse_3adic_conditioning.md` (task W5). The repunit conditioning
is vacuous: \(a_n\to-1/2\) in \(\mathbb Z_3\), but mod \(3^k\) the affine
identity forgets the seed once \(K\ge k\), leaving a function of the valuation
word alone. The states do match the Syracuse stationary law (once the
reference measure is got right — it is neither uniform nor uniform on the
units), but that is an *ensemble* fact, whereas the reset-gap target is
single-orbit equidistribution. W5-D records the structural reason: \(f\)
contracts 3-adically and expands 2-adically, so Tao's method works on the
side where orbit information is destroyed.

For predecessor-density arguments, read
`density-cycles/kl_rail_restricted_tree.md` (task W4). The mod-8 rail
restriction is *free* — \(P_e(y)\equiv-3^{-1}\pmod{2^m}\) for \(e\ge m\), so
the residue is a bounded-suffix function of the \(e\)-word and the exponent is
unchanged — and no density theorem can serve Avenue A anyway: the repunit
family has counting function \(O(\log x)\) against a complement of \(\sim x\).
It also closes W2's hand-off.

For the *shape* of the extremal targets (navigation, not mathematics), read
`density-cycles/extremal_law_calibration.md` (task W13). Record deficits obey
a Cramér--Lundberg tail \(P(\max_K D_K>u)\asymp2^{-u}\) with the exact
exponent \(\gamma=\log2\) forced by PCD7's budget identity (measured slope
\(-1.0103\)), not a Bramson correction; plateau records obey
\(\ell_{\max}(m)\approx1+0.1845\log_2 m\). Barrier 2 applies in full — the
note eliminates nothing and proposes no ledger rows.

For automated potential synthesis, read
`no-go/machine_synthesis_surviving_class.md` (task W6). It corrects a stale
premise — the quantized-log class is already closed by SUFF1+CONN1, not open —
identifies the two-variable \(V(x,n)\) class as what actually survives (the
\(-5\) shadow reaches depth only \(\log_2(\#\text{states})\) inside a single
orbit), and proves a new finite no-go there from actual orbit states. It also
records MSY4: a SAT answer is meaningless unless its coordinate compression is
published alongside.

For the tower normal forms as a source of new exact lanes, read
`no-go/two_tower_interference.md` (task W8, re-scoped). Sums and differences
of tower members are all closed-form — the halved diagonal sum even lies in
the *same* tower cylinder as a single \(w_d\) — but every alignment resolves
onto a ghost the repo already carries (\(-1\), \(-1/3\), \(-3^{-k}\),
\(\Lambda_d\)), so the family produces no new structure. §4.1 records the
cross-cutting observation that this repo's exact lanes shadow *rational*
\(2\)-adic ghosts while its open objects shadow *irrational* ones.

For the additive "combine certificates for the parts" idea, read
`no-go/superposition_interaction_ledger.md` (task W1). It closes the avenue:
\(C^{(T)}\) is affine on each parity cylinder with slope \(6^{o}/2^T\), so the
superposition defect is a *slope* mismatch of trajectory size, not a carry
ledger; for odd \(n\) the parts have opposite parity so the closed-form regime
is empty, and the one exact regime uses a virtual part (barrier 4).

For the certificate-transport / "grow the verified basin" idea, read
`no-go/certificate_semigroup.md` (task W2). It closes the avenue: the
repo's proved transport rules split into forward-orbit rules (which enlarge
a finite certified set only finitely), one-parameter rules (whose orbit has
counting function \(\Theta((\log X)^2)\) and countable \(2\)-adic closure),
and the unrestricted predecessor selectors (whose orbit *is* the "reaches 1"
set, so characterizing it is the conjecture). Along the way it identifies
the Mersenne ancestry tower TWR1 as exactly the \(d\)-fold iterate of the
single \(e{=}2\) predecessor selector \(P_2(z)=(4z-1)/3\).

For the transcendence inputs, read `no-go/baker_explicit_constants_audit.md`
(task W9 of `OPUS5_WIDE_TASKS.md`). It audits every Baker / irrationality
invocation in the repo, finds that all of them are two-log forms, and
replaces the generic constants by numerals: the Avenue A \(L=1\) Baker
hypothesis is eliminated outright (crossover \(n\ge161\) by Rhin's explicit
proposition, inside the scanned range), and the fixed-\(d{=}7\) BAKER1--3
branch is given an exact closed form, \(v_2(3^m+7)=2+v_2(m-\alpha)\) with
\(3^\alpha=-7\) in \(\mathbb Z_2\), which needs no transcendence input at all
inside a finite range.

For the open repunit programme, start with
`repunit/repunit_extremal_principle.md`, then read the synchronized attack
status in `repunit/next_generation_attack_program.md` and the active PCD1--PCD17
development in `repunit/payout_concentration_diffusion.md`.
`repunit/primitive_ancestry_lemma.md` and
`repunit/general_payout_ancestry.md` supply the completed ancestry branches.
`repunit/coverage_portfolio.md` organizes these mechanisms as an ordered
residual cover and distinguishes genuine descent-or-merge rules from density
or classification results.
The root [`RESIDUAL_ATLAS.md`](../RESIDUAL_ATLAS.md) freezes IEF17 as the
live qualitative residual object and ranks the next coordinate-shrinking
lemmas. Bounded-phase working notes live in
[`residual-atlas/`](residual-atlas/).
`repunit/integral_escape_frontier.md` gives the terminal criterion: a
\(2\)-adic residual may remain nonempty if every surviving exponent acquires
nonzero high lift digits infinitely often and therefore is not a positive
integer. It also proves an exact bridge between the balanced starting-cylinder
lift and dual endpoint digit, reducing qualitative exclusion to showing that
one deterministic digit stream is not eventually zero. IEF10 completes that
step for the exact balanced itinerary using periodic Sturmian approximants and
a Baker growth bound. IEF11 extracts a general periodic-prefix discharge rule
and closes every fixed phase shift. IEF12 then uses the general repetition
theorem for Sturmian words to discharge every intercept at the critical
slope. IEF13 extends the rule to every bounded-critical-discrepancy language
with Diophantine exponent greater than \(1\), including every such language
of linear factor complexity. The remaining frontier is unbounded discrepancy
or superlinear complexity; IEF14 supplies an adaptive margin that also removes
some growing-discrepancy languages, while IEF15 finitely reduces sustained
negative-drift branches. IEF16 additionally forces every rational non-cyclic
survivor to have zero linear lower discrepancy. IEF17 records the exact
intersection left after all these rules, with cycles kept separate. IEF18
then sharpens the periodic-prefix coordinate using the directional drift that
actually contributes to rational height; IEF14 remains a coarser corollary.
IEF19 uses that estimate to discharge sublinear-drift words with repetition
exponent greater than one, leaving exponent one or positive linear excursions.
IEF20 additionally discharges fixed-surplus repetitions occurring in critical
drift windows, even when the global limsup is positive. IEF21 replaces the
full window envelope by exact terminal draw-up and endpoint-loss costs, so
internal peaks that return to a local valley are also covered.
The Collatz-free terminal dual-digit escape is ledger claims IEF22--IEF24
in `repunit/dio1_cocycle_problem.md` (Theorem G: no infinite path in the
residue graph; IEF24 excludes positive integers from infinite
\(\mathcal L_{3/4}\) itineraries via IEF7). Route A context is
`repunit/hecke_mahler_route_a.md`.
The separate
`repunit/repunit_equidistribution_reframing.md` is an empirical strategic
diagnosis for a shortcut-map stopping-time target, not a theorem and not a
replacement for the accelerated-map proof target.
