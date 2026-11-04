# Session report, 3–4 November 2026

**What this is.** One place that records everything of value produced in the
long working session that followed the Mersenne-spine corrections, with an
honest status for each item. The authoritative statuses are in
[`CLAIM_LEDGER.md`](../CLAIM_LEDGER.md); this report explains how the pieces
fit and what a reader should check first.

**Provenance warning.** All of it was produced in a single assistant session.
Every numbered claim has an exact-arithmetic verifier, but a passing verifier
is not a proof read, and nothing below has had one. The verifiers caught
errors during the session (listed in §6), which is evidence they work and also
evidence that errors were being produced at a rate that matters. The
Krasikov–Lagarias and Applegate–Lagarias papers could not be fetched (the
session's network blocked the hosts); the predecessor-count system was
reconstructed from their published description.

---

## 1. Summary table

| Result | Statement | Status | Where | Verifier |
|---|---|---|---|---|
| **Theorem E** (QLG2) | The quantized logarithm \(\lfloor2^j\log_2x\rfloor\), jointly with \(\tau\), \(x\bmod N\) for any \(N\), and all suffix detectors, admits a closed certificate at every precision \(j\); least length is a semiconvergent denominator of \(\log_23\) | Proved here | manuscript §7; ledger RATCYC1, QLG2, MODN1, MSTEP1 | `scripts/verify_quantized_log_theorem.py` |
| **Theorem F** | No finite set of certified residue classes of \(k\) covers the spine family \(n=64k+17\) | Proved here (part 3 needs a human read) | manuscript §10 | `scripts/verify_residue_certificate_nogo.py`, `prove_block8_17_classes.py` |
| **Theorem G** (FD1–FD3) | Minimal failure density of a depth-\(m\) local potential is \(2^{-cm+O(\log m)}\), \(c=1-H(1/\log_23)=0.0500\) | Proved here | manuscript §8; `docs/no-go/failure_density.md` | `scripts/verify_failure_density.py` |
| **PRED1** | A positive solution of the Krasikov-type system on classes mod \(3^k\) gives \(\pi_a(X)\ge c\,v_a(X/a)^\gamma-1\) | Proved here (one page) | `docs/density-cycles/predecessor_exponent.md` §2 | BFS cross-check |
| **PRED2** | Certified exponents \(\gamma=0.8417,0.8530,0.8629,0.8723,0.8811,0.8891,0.8964\) for \(k=11,\dots,17\); published record \(0.84\) | Finite certificate (exact integer check, up to 86 million inequalities) | same, §4 | `scripts/verify_predecessor_exponent.py` |
| **PRED3** | If any integer fails to reach 1 then at least \(c\,X^{\gamma}\) integers below \(X\) fail; so Collatz is a power-saving statement for the exceptional set | Proved here (corollary; a restatement, not progress) | same, §6.1 | immediate |
| **PRED4** | The averaged Krasikov system is critical at \(\gamma=1\) for every \(k\) (Haar mass preservation), so \(\gamma_k\le1\) | Proved here (lemma) + numerics | same, §6.2 | loss tables from the explorer |
| **EPOCH1** | \(\Phi(x)=T^{\ell(x)}(x)\) is determined by the parity word of \(x\) up to one bit via \(c(w)2^{-\ell}\bmod3^k\) | Proved here | `docs/no-go/epoch_transform.md` | `scripts/explore_epoch_bias.py` |
| **EPOCH2** | Bias propagation is memoryless given length through four epochs at 32 and 40 bits; no structured multi-epoch survivor family found | Finite diagnostic | same, §3, §5 | `explore_epoch_bias.py`, `explore_epoch_survivors.py` |
| Certificate miner | The independent miner cited by the paper, absent from the repo, rewritten | Tool | `scripts/verify_nogo_certificate.py` | self-checking (exact confirmation of every cycle) |

Manuscript state: 20 pages (`mersenne_obstructions.tex`, `.pdf`), Theorems A–G,
boundary section rewritten to two open corners.

## 2. The no-go programme, completed in three directions

The paper previously excluded corrections built from residues, fuel, suffix
detectors, length and leading digits (Theorems A–D). This session added:

1. **Size read to any fixed precision (Theorem E).** One shadow period gains
   \(\log_2\frac98>2^{-j}\), so a single chain cannot close the quantized
   logarithm for \(j\ge3\). The remedy is a cycle of \(K\) independent
   witnesses, one per member of the rational cycle of a chosen valuation word
   \((2,1)^p(3,1,1)^r\), with the number of carries in the cell chosen so the
   total displacement is exactly zero. Existence needs only that every
   valuation word is the exact word of a rational 2-adic cycle (RATCYC1), and
   that \(K\) is *admissible*: \(\lfloor K\beta\rfloor/K\ge\lfloor Q\beta\rfloor/Q\).
   Minimal admissible \(K\) at \(Q=2^j\): 1, 2, 2, 2, 7, 7, 12, 12, 12, 53, 665,
   a one-sided best-approximation (semiconvergent) sequence for \(\log_23\).
   This repaired a false claim in the old boundary section and answered the
   paper's own open Question. Corollaries: arbitrary modulus for Theorem B;
   potentials monotone only along \(f^k\).
2. **How often a local potential must fail (Theorem G).** Lower bound: one
   shadow class per expanding cyclic parity word of length \(m+1\), pairwise
   disjoint, counted by an entropy bound. Upper bound: the lookahead potential,
   which satisfies the exact identity
   \(\Psi(Tx)-\Psi(x)=(k\log_23-m)/m+[x\text{ odd}]\log_2(1+\tfrac1{3x})\).
   The exponent \(c\) is the large-deviation rate of "the orbit has not
   descended within \(m\) parity steps", so a local correction can do no better
   than wait for descent, and fuel and detectors do not change the exponent
   (they are local away from one 2-adic point each).
3. **The spine method closed.** Theorem F plus the earlier corrections: no
   finite set of residue-class certificates on \(n=64k+17\) can work, because
   the 2-adic index \(k^*\) with \(3^{64k^*+20}=-367\) enters the cycle
   \(-5\mapsto-7\). Every open gap of the Avenue A family implies Conjecture G.

## 3. The backward direction

The predecessor-counting system of Krasikov, Applegate–Lagarias and
Krasikov–Lagarias was reconstructed (their \(0.81\) at \(k=9\) and \(0.84\) at
\(k=11\) are reproduced to the printed precision, which is the evidence the
reconstruction is theirs) and solved at larger \(k\) by nonlinear power
iteration with bisection on \(\gamma\), each level certified by an exact
integer check with the two irrational coefficients rounded down:

| \(k\) | classes | certified \(\gamma\) | cost |
|---|---|---|---|
| 11 | 118 098 | 0.8417 | seconds |
| 12 | 354 294 | 0.8530 | 1 min |
| 13 | 1.06 M | 0.8629 | 3 min |
| 14 | 3.19 M | 0.8723 | 6 min |
| 15 | 9.57 M | 0.8811 | 18 min |
| 16 | 28.7 M | 0.8891 | 30 min |
| 17 | 86.1 M | 0.8964 | 1 h 52 min, 5.3 GB |

Gains per level shrink slowly (0.0112 to 0.0075). \(k=18\) needs about 16 GB
and 6 hours and was not attempted. Two structural facts: PRED3 (a restatement
of the problem as a power saving for the exceptional set) and PRED4 (the
averaged system is exactly critical at \(\gamma=1\), so the method can only
approach 1; the minimum over the three child subclasses is its only loss, and
numerically that loss decays like \(0.91^k\)). Krasikov's conjecture
\(\gamma_k\to1\) is therefore supported by data and by a mechanism but not
proved. A proof along these lines needs equicontinuity of the Perron
eigenfunctions of a 3-adic transfer operator whose branches are an isometry
and an expansion.

**Caveat.** A bound \(X^{\gamma}\), \(\gamma<1\), says nothing about density;
`docs/density-cycles/kl_rail_restricted_tree.md` already records why no
exponent below 1 can serve the repunit family.

## 4. The epoch transform

\(\Phi(x)=T^{\ell(x)}(x)\), applying \(T\) exactly as many times as \(x\) has
bits. Identity (EPOCH1): the next epoch's integer is the binary expansion of a
3-adic residue computed from the current epoch's parity word. Dynamics is the
alternation *binary word → residue mod \(3^k\) → binary word*. Descent happens
in an epoch iff \(k/\ell<1/\log_23\).

- **Memorylessness hypothesis.** The binary digits of this residue carry no
  memory of the bias of the word that produced it, except along the bounded
  shadows of rational cycles. It would imply Collatz and is not provable with
  current tools (it contains base-2 normality of base-3-defined numbers).
- **Evidence.** Chains from uniform samples of the non-descending set
  (6 million samples at 32 and 40 bits, 4–8 million at 26): ratios to the
  length-matched independent prediction \(0.999,1.008,0.986\) at 32 bits and
  \(0.985,0.991,1.021\) at 40 bits. At 26 bits there is a real finite-size
  excess of about 4.5 percent and 18 percent at stages 2 and 3, not explained
  by the image's dyadic position or residue mod 9 and absent from 32 bits up.
  Its mechanism is not identified.
- **Structured families.** None survives beyond chance: all 157 expanding
  primitive periodic words of length up to 9 (shadows up to 64 bits), the
  epoch-fixed points below \(2^{20}\), Sturmian words, and the census champions
  below \(2^{26}\). A bit-budget argument shows a rational-cycle shadow cannot
  last more than one epoch.

## 5. Avenues proposed, with honest status

These came out of discussion, not from verified work. Items are marked
**sketch** (a plausible argument not written), **unchecked** (rests on recall
of the literature), or **retracted**.

| Avenue | Status |
|---|---|
| Prove Krasikov's conjecture \(\gamma_k\to1\) via equicontinuity of Perron eigenfunctions of the 3-adic transfer operator | Target with a mechanism (PRED4) and data; **no proof**. Recommended next |
| Power saving for the exceptional set (PRED3), or positive lower density for the basin of 1 | The actual frontier. An earlier remark that upper density 1 is known from Tao plus Barina is **retracted**: it was not checked and should not be relied on |
| Litmus test: a method that cannot exclude one integer whose orbit is 90 percent odd forever is not going to prove Collatz | A criterion, not a result |
| Bounded-memory corrections (history of fixed length) also fail, since the shadow extends backward along inverse branches | **Sketch**, unwritten. Would close the boundary section's orbit-history corner for bounded memory |
| Corrections reading digit statistics (Hamming weight, run counts) | **Sketch**. The claim that the burn kills weight-only corrections was stated loosely and is unchecked; a witness-editing argument was only outlined |
| Which window the shadow certificates actually touch (they alter only the top bits), giving the sharp reach of the method in terms of continued fractions of \(\log_23\) | **Sketch**. The statement that \(K_{\min}(Q)\) grows like \(\sqrt Q\) is unchecked and should be tested before use |
| Termination-analysis audience (automated proofs by matrix interpretations; Yolcu, Aaronson, Heule) and the Stein–Thompson group view of the general map | **Unchecked** (recalled from the literature) |
| Cobham's theorem as a mechanism (the map is both 2- and 3-definable) | Framework only, no candidate property |
| Both sides of the continued fraction of \(\log_23\): certificates live at approximations from below, positive cycles at approximations from above; reproduce the Simons–de Weger run-count induction with modern bounds | Remark plus a possible computation; not done |
| Rigidity of closed invariant sets in \(\mathbb Z_2\times\mathbb Z_3\) | **Retracted** on a sketched argument that every basin is dense in every completion, so closure-based rigidity cannot separate a divergent basin from that of 1 |

## 6. Errors the verifiers caught this session

Recorded because they are the best evidence of how much the unchecked claims
above should be trusted.

- The first quantized-log verifier timed out on a quadratic loop and then
  failed on the 3-adic residues (cycle members are 3-adic integers, not
  \(2^{-E}\)) and on a partner search that assumed a fixed step.
- The epoch census looped forever on the trivial cycle (\(x=2\) is an
  epoch-fixed point).
- The first predecessor certificate failed on a too-tight sanity tolerance.
- A first estimate of the exponent constant in manuscript Theorem G was
  stated as \(0.049\); the exact value is \(0.0500\).
- The first census comparison against the independent model used a
  predicted chain length rather than the actual one, and counted members of
  one orbit family as separate coins. Using actual lengths and collapsing
  families moved the fifth-stage ratio from 1.41 to about 1.22 (on 121 events,
  so not significant); the later 26-bit importance runs, which are better
  powered, then isolated the real few-percent excess at stages 2 and 3.
- Two simultaneous importance-sampled runs exhausted memory; the sampler was
  made chunked.

## 7. Reading order for a human reviewer

1. Manuscript Theorem G, Step 5 (the counting step) and the conditional
   density step of the upper bound.
2. Manuscript Theorem E, Step 2 (the residues excluded by the chosen word)
   and Step 5 (height bookkeeping).
3. PRED1 (the one-page comparison principle) in
   `docs/density-cycles/predecessor_exponent.md` §2.
4. Theorem F(3), DISJ and the two-sided window bound (carried over from the
   previous handoff).
5. Check the reconstruction of the Krasikov system against the original papers
   (not accessible in the session).

## 8. Reproduction

```bash
python3 scripts/verify_failure_density.py                       # Theorem G, ~25 s
python3 scripts/verify_quantized_log_theorem.py --quick         # Theorem E; full grid ~2 h
python3 scripts/verify_residue_certificate_nogo.py --measure    # Theorem F
python3 scripts/verify_nogo_certificate.py --limit 200000       # miner, ~15 s
python3 scripts/verify_predecessor_exponent.py --k 12 --gamma 0.8530 --count-check
python3 scripts/explore_predecessor_exponent.py --kmin 2 --kmax 13   # exponents
python3 scripts/explore_epoch_bias.py --importance --l 32 --n 6000000 --J 6
python3 scripts/explore_epoch_survivors.py --lmax 24 --parts 1234
python3 scripts/verify_claim_ledger.py && python3 -m unittest discover -s tests
```

Final status at the time of writing: all maintained verifiers pass; the claim
ledger validates with 173 rows; the PDF is rebuilt.
