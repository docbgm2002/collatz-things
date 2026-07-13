# Repository edits, part 2 — sessions of 2026-07-01/02

> **Historical provenance only.** This is a session edit plan, not an
> authoritative status document. Many listed edits have since been applied or
> superseded. Use `CLAIM_LEDGER.md` for current claims and `README.md` for the
> current reading path.

Supplements `REPO_EDITS.md` (which covers PAR1 reclassification, TREE2
refutation, cycle-reduction literature note, and NLP1). This file
consolidates everything since. New files to add to the repository, all in
this session's outputs, each with a passing exact-arithmetic verifier:

    docs/density-cycles/corridor_rate.md            scripts/verify_corridor_rate.py
    docs/no-go/nlp2_alternation.md         scripts/verify_nlp2.py
    docs/no-go/tower_theorem.md            scripts/verify_tower.py
    docs/no-go/spine_synthesis.md          scripts/verify_spine_synthesis.py
    docs/no-go/latent_fuel_notes.md        scripts/explore_latent_fuel.py
    scripts/verify_survivor_density_rate.py        (TREE2 refutation, from part 1)
    mersenne_obstructions.tex/.pdf         (manuscript)
    BIBLIOGRAPHY_PASS.md                   (literature check log)

## New CLAIM_LEDGER.md rows

| ID | Claim | Status | Source | Verification |
|---|---|---|---|---|
| COR1 | dens(S~_K) <= 31 * rho^(K/theta) for all K >= 1 | Proved here | `docs/density-cycles/corridor_rate.md` | `scripts/verify_corridor_rate.py` |
| COR2 | lim dens(S~_K)^(1/K) = rho^(1/theta) = 0.965907... | Proved here | `docs/density-cycles/corridor_rate.md` | rate convergence checked to K=1800 (finite evidence; proof is human) |
| COR3 | Undischarged-class count for K-bit forced-descent certificates grows with branching factor exactly 2 rho^(1/theta) = 1.9318... | Proved here | `docs/density-cycles/corridor_rate.md` | sandwich checked by enumeration K=8..14 (upper bound attained exactly) |
| NLP1 | No potential log2 x + g(x mod 2^m, tau(x)) is nonincreasing | Proved here | `docs/no-go/no_local_potential.md` | `scripts/verify_no_local_potential.py` |
| NLP2 | No potential log2 x + g(x mod 2^m, tau(x), lambda(x)) is nonincreasing | Proved here (subsumed by NLPD; kept for its explicit level-2 computation) | `docs/no-go/nlp2_alternation.md` | `scripts/verify_nlp2.py` |
| TWR1 | Exact ancestry tower w_d(M) = (2^(M+2d) - 2^(2d+1) + 3^d)/3^d, f^d(w_d(M)) = 2^M - 1 on M = 1 mod 2*3^(d-1); carry-free period-2*3^(d-1) normal form; 2-adic freeze with cross-level separation at bit 2min(d,d')+1 | Proved here | `docs/no-go/tower_theorem.md` | `scripts/verify_tower.py` |
| NLPD | No potential log2 x + g(x mod 2^m, tau, (lambda_i)_{i in S}) is nonincreasing, for any finite set S of tower detectors | Proved here (unconditional; supersedes the conditional version) | `docs/no-go/tower_theorem.md` | `scripts/verify_tower.py` |
| SPN1 | Complete exact lane of length d+M+1: tower -> Mersenne -> burn -> repunit, with payout e* = 2 + v2(1+3^(d-1)s) and rail 8y+1 for all tower members | Proved here (composition of TWR1+MER1+MER2 plus two exact additions) | `docs/no-go/spine_synthesis.md` | `scripts/verify_spine_synthesis.py` |
| BND1 | No potential log2 x + G(x) with bounded G is nonincreasing | Proved here | `docs/no-go/spine_synthesis.md` | arithmetic in `scripts/verify_spine_synthesis.py` |

## Status changes to existing rows

- **TREE2**: original rho^K bound REFUTED (exact walk computation; holds
  K <= 194, fails from K = 195, ratio unbounded after). Corrected
  conjecture superseded by COR1/COR2, which prove both directions of the
  corrected rate. Add `scripts/verify_survivor_density_rate.py` to its row and a
  history note; see REPO_EDITS.md item 2 for the docs/density-cycles/descent_tree_survivors.md
  text.
- **PAR1**: reclassify to "Known theorem rederived" (Terras 1976 /
  Everett 1977); see REPO_EDITS.md item 1.
- **POT1/POT2** (`docs/no-go/Exponential_Decay_Potential.md`): unchanged as stated,
  but append a note: BND1 now proves the note's §4 admission — no bounded
  correction, including c*g_r for every (c, r), is a global Lyapunov
  function. The recharge-family and epoch statements stand.
- **MER1 / burn lemma** (`docs/no-go/recharge_nogo.md`): add attribution — the
  iterated fuse identity 2^t u - 1 -> 3^t u - 1 is recorded by Andaloro,
  Fibonacci Quart. 38 (2000) 73-78 (per Lagarias's annotated
  bibliography II). The frozen-coordinate use is this repository's.
  Same note in `docs/no-go/no_local_potential.md` when next edited.

## README.md additions

Under "Mersenne structure and potential limitations":
- `docs/no-go/no_local_potential.md` — no potential log2 x + g(x mod 2^m, tau) (NLP1).
- `docs/no-go/tower_theorem.md` — the exact Mersenne ancestry tower and the
  unconditional finite-detector no-go (TWR1, NLPD).
- `docs/no-go/spine_synthesis.md` — the complete exact lane and the bounded-correction
  no-go (SPN1, BND1).

Under "Density and cycles":
- `docs/density-cycles/corridor_rate.md` — the exact survivor-density rate rho^(1/theta) and the
  tree-prover branching exponent (COR1-COR3); supersedes the refuted
  TREE2 conjecture.

Exploratory list: add `docs/no-go/latent_fuel_notes.md` with a banner note that its
hierarchy conjecture is RESOLVED by `docs/no-go/tower_theorem.md` (e=2-uniform form);
the note is retained for the discovery path and the L1/L2 word forms.

New top-level entry for the manuscript: `mersenne_obstructions.tex` —
consolidated paper (Theorems A/B/C = NLP1, TWR1, NLPD + BND1 corollary);
pre-submission checklist: manual read of the annotated bibliographies and
Wirsching chs. 2-3 (see `BIBLIOGRAPHY_PASS.md`), adversarial proof read,
author block.

## Notes for the active programs

- **Repunit tail** (`docs/repunit/repunit_tail_attack.md`): SPN1's payout formula
  refines §2 — on tower-fed Mersennes, e* = 2 + v2(1 + 3^(d-1)s), so the
  even-s half of every tower progression has forced e* = 2. The residual
  sigma(a_n) is untouched (Observation R4 stands).
- **Paired-macro program** (`archive/potential_attack_notes.md` §5): SPN1 supplies
  the exact macro inventory, and the note records that the pair's net-drift
  question reduces to sigma(a_M) again — logged so the shortcut is not
  re-attempted.
- **Correction history**: docs/no-go/spine_synthesis.md includes a logged draft
  correction (M = 1 mod 4 overclaim caught by verifier at (d,s)=(1,1),
  corrected to the parity-split payout before promotion).

## Addendum (self-review session)

- New file: scripts/verify_nogo_certificate.py — logically independent
  infeasibility certificates for local potentials, mined from real orbits
  (Bellman-Ford + exact Fraction confirmation). NLP1 window: two-step
  certificate (57, 27), a complete proof of NLP1 for m <= 4; NLP2 window:
  five-step certificate routing through the recharge step 41 -> 31.
  Referenced in the manuscript (Remark after Theorem A).
- New file: SELF_REVIEW.md — adversarial pass over T1(d), T2, and
  Corridor 1b: all sound; two minor presentational items logged for the
  journal version.

- New files: docs/no-go/fuel_fraction_nogo.md / scripts/verify_fuel_fraction.py — Theorem D
  (FFN1): no potential log2 x + g(tau, len) is nonincreasing, proved by an
  explicit 11-witness cycle certificate; triple with mod 16 falls to a
  2-witness certificate. Manuscript Question 1 replaced by Theorem D; the
  boundary question is now the all-m triple class, with the fixed-length
  residue-frozen burn family recorded as the growth half of a route.

- New files: docs/no-go/shadow_certificate.md / scripts/verify_shadow.py — Master Theorem SH1:
  shadowing the expanding cycle -5 -> -7 refutes ALL potentials
  log2 x + g(x mod 2^m, tau, len, lambda_1..lambda_d) in half a page;
  smallest certificate 1275 -> 1913 -> 1435. Subsumes NLP1/NLP2/NLPD/FFN1
  as impossibility statements (ledger status change; structural content
  retained). General principle: every expanding rational cycle (2^E < 3^K)
  is a certificate factory. Manuscript restructured accordingly; a fuller
  editorial reorganization is flagged for the human pass.

- New files: multistep shadow / scripts/verify_multistep.py — SH2: no k-step
  potential over (mod 2^m, tau, detectors) for ANY k, m, d, via the exact
  shadow closed form x_2j = 9^j 2^(N-3j) w - 5; len-inclusive for even
  k<=10 / odd k<=5 with placement constraints. Scope correction logged
  (draft claimed k<=11; verifier refuted at k=5; window arithmetic redone).
  Manuscript boundary section updated: residuals are now leading-digit
  corrections and the contracting-edge connectivity question.

- New files: docs/no-go/leading_digit_nogo.md / scripts/verify_leading_digit.py — Theorem F
  (SH2): iterated -5 shadow + Dirichlet approximation of log2(9/8) excludes
  potentials using any fixed number of leading digits (with residues, tau,
  and detectors), any m, j, d. Concrete instance (m,j,a)=(6,4,53) realized
  in exact integers at depth N=177. Boundary moves to the quantized full
  logarithm; manuscript updated (abstract + shadow section + boundary).

## Manuscript restructure (final)

The manuscript was rewritten top-down (old version preserved in session
as old_manuscript.tex.bak; superseded). New architecture:
  Title: "No-Go Theorems for One-Step Lyapunov Potentials for the 3x+1 Map"
  Theorem A = master shadow no-go (residues, tau, len, all detectors)
  Theorem B = leading digits (iterated shadow + Dirichlet)
  Theorem C = bounded corrections (Mersenne burn)
  Theorem D = the ancestry tower (structural companion; gives the
              detectors their meaning)
  + certificate-mining section with provenance note (the shadow was
    discovered via mined witnesses); family method compressed to the
    price-list remark, full proofs retained in repository notes;
  + boundary section: quantized full logarithm + multi-step, with the
    honest statement that further no-go progress is conjecture-adjacent.
Detector definition moved to preliminaries with a self-contained mod-32
lemma, removing the forward dependency on the tower section.
8 pages, clean compile, all statements match verified facts.
