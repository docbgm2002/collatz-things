# AGENT_HANDOFF_NEXT — load this first in a new chat

Status (2026-11-03): **the manuscript is the deliverable; the spine
programme is closed.** Read `CLAIM_LEDGER.md` § "Manuscript Section 7
written; spine corrections logged (2026-11-03)" for the record.

---

## 0. One-line mission

Get `mersenne_obstructions.tex` to submission quality. Do not reopen the
Mersenne-spine / repunit-tail descent programme (§3 below says why).

---

## 1. Manuscript position

Theorems A–D as before. New on 2026-11-03:

- **Section 7, Theorem E (quantized logarithm).** For every precision
  \(j\), modulus \(N\) and detector depth \(d\), the coordinate
  \((\lfloor2^j\log_2x\rfloor,\tau,x\bmod N,\lambda_1..\lambda_d)\) admits a
  closed certificate; least length at \(2^j\) is a semiconvergent
  denominator of \(\log_23\). Proof: shadow the rational cycle of the word
  \((2,1)^p(3,1,1)^r\), one fresh witness per member. Corollaries: arbitrary
  modulus for Theorem B; multi-step (\(f^k\)) versions of B and E.
  Verifier: `scripts/verify_quantized_log_theorem.py` (`--quick` for a fast
  run).
- **Section 8, Theorem G (failure density).** The minimal failure density
  of a depth-\(m\) local potential is \(2^{-cm+O(\log m)}\),
  \(c=1-H(1/\log_23)=0.0500\ldots\). Lower bound: shadows of all expanding
  cyclic parity words of length \(m+1\). Upper bound: the lookahead
  potential. Fuel and detectors do not change the exponent (Proposition
  8.8). Verifier: `scripts/verify_failure_density.py`; note
  `docs/no-go/failure_density.md`.
- **Section 9** cites the rewritten miner `scripts/verify_nogo_certificate.py`.
- **Section 10, Theorem F** (was "Theorem E" in notes written before
  2026-11-03): the spine result, with a remark positioning it against
  Terras.
- **Section 11, boundary** rewritten: two open corners only —
  \(\mathrm{LD}_{j'}\) jointly with \(\lfloor2^j\log_2x\rfloor\), and
  orbit-dependent corrections.

Ledger rows: RATCYC1, QLG2, MODN1, MSTEP1, FD1–FD3 (general track table).

## 1b. Backward direction (2026-11-03, later)

`docs/density-cycles/predecessor_exponent.md`: the Krasikov–Lagarias
difference-inequality system reconstructed (their \(0.84\) at \(k=11\)
reproduced) and pushed to larger \(k\): certified \(\gamma=0.8530\) at
\(k=12\), \(0.8629\) at \(k=13\), \(0.8723\) at \(k=14\), \(0.8811\) at \(k=15\), \(0.8891\) at \(k=16\). Scripts `explore_predecessor_exponent.py` (float solver) and
`verify_predecessor_exponent.py` (exact certificate). Each level costs a
factor 3 in classes; \(k=16\) (\(28.7\)M classes) took 30 min for the
float solve and 3 GB; \(k=17\) (86M classes) would need about 10 GB and
2 h, at the edge of this container. The proof (PRED1) needs a human read: the
comparison principle and the subsolution inequality in §2.

## 2. DO NEXT (in this order)

1. **Human proof read** of Theorem G (Section 8): the counting Step 5 of
   the lower bound and the conditional-density step of the upper bound; of
   Theorem E (Section 7), especially Step 2 and Step 5; and of Theorem F(3),
   DISJ (§4) and the two-sided window bound (§5.3) in
   `avenue_a_mean_valuation_route.md`.
1b. **Sharpen Theorem G** if wanted: compute \(\delta_m\) exactly for small
   \(m\) (minimum-measure feedback set for the positive cycles of the
   coordinate graph), extend FD1 to Archimedean coordinates via the
   multi-witness cycles of Section 7, and write the \((a,b,c)\) transfer.
2. **Question 10.1**: \(\mathrm{LD}_{j'}\) jointly with the quantized
   logarithm. Expected route: the construction of Theorem E with the in-cell
   positions chosen along a rotation by \(\varphi\), so that each witness can
   be placed in the leading-digit window of its predecessor's image. This is
   the one open item where a short theorem is plausible.
3. **SHG1 decision**: fold `docs/no-go/general_shadow.md` (general
   \((ax+b)/c^{v}\) maps, ranking-function reading) into the paper as a
   section, or hold it for a separate note. The general \((a,b,c)\) form of
   Theorem E should follow from RATCYC1 verbatim with \(\log_ca\); not written.
4. Literature: manual pass over the two annotated bibliographies and
   Wirsching ch. 2–3 (recorded as not done in `BIBLIOGRAPHY_PASS.md`);
   check whether Theorem E's "no finite coordinate" principle has a prior
   statement.
5. Author line (`[author]`), then arXiv.

### Anti-patterns
- Do not restart the residue grind on \(n=64k+17\); Theorem F says it
  cannot cover all \(k\), and Correction SD-K-prefix says a cover would
  prove only a prefix inequality anyway.
- Do not budget sessions on Gap SD-K-nc-6: it implies Conjecture G
  (Proposition SD-K-nc6-barrier).
- Do not state a mod-\(2^j\) row for its whole class on one representative
  (`scripts/prove_block8_17_classes.py` is the exact prover if a class row
  is ever needed again).
- No ledger promotion of SD1/EC1/SD-L1 without a full human proof.

## 3. Why the spine programme is closed

- Every open gap in the Avenue A family (SD-K-nc-6, survivor-6, block-8,
  block-8-17) implies \(\sigma(a_n)<\infty\) on its domain and the strongest
  implies \(\operatorname{epoch}(2^n-1)\le7n\) for all odd \(n\).
- Theorem F: no finite set of certified residue classes of \(k\) covers all
  odd \(k\); the obstruction is the \(2\)-adic index \(k^*\) with
  \(3^{64k^*+20}=-367\), whose orbit enters \(-5\mapsto-7\).
- `obstruction_map.md`: five local routes closed, one counting route
  unsupported.

## 4. Key files

| Path | Role |
|---|---|
| `mersenne_obstructions.tex` / `.pdf` | the paper (20 pp.) |
| `scripts/verify_quantized_log_theorem.py` | Theorem E, cost law, corollaries |
| `scripts/verify_failure_density.py` | Theorem G (failure density) |
| `scripts/verify_nogo_certificate.py` | certificate miner (Section 8) |
| `scripts/verify_residue_certificate_nogo.py` | Theorem F |
| `scripts/prove_block8_17_classes.py` | exact class prover (spine rows) |
| `docs/no-go/avenue_a_comparison_dynamics.md` | spine notes, Correction SD-K-267-class |
| `docs/no-go/avenue_a_mean_valuation_route.md` | nc-6 barrier (§7), DISJ, window bound |
| `docs/no-go/general_shadow.md`, `general_cost_law.md`, `cost_law_proof.md` | SHG1, QLG-GEN, DICH1, COST1 |

Build the PDF with `pdflatex mersenne_obstructions.tex` twice
(`apt-get install -y texlive-latex-base texlive-latex-recommended texlive-latex-extra`
after `apt-get update` in a fresh container).
