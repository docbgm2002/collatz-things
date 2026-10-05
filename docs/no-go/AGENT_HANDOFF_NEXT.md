# AGENT_HANDOFF_NEXT — load this first in a new chat

Status: **267-family grind stopped (2026-10-05).** The mod-\(8192\) closure
theorems on this family were refuted as class-level statements; see
Correction SD-K-267-class in `avenue_a_comparison_dynamics.md`.
Do not reopen residual-atlas L5 / E_mix unless user explicitly asks.
Do not ledger-promote SD1/EC1/SD-L1 until a full human proof closes the gate.
The macro-step counting route has no established escape-density bridge (see §6).

---

## 0. One-line mission

Gap SD-K-block-8-17 is **not** to be closed by further residue-class
refinement. `avenue_a_mean_valuation_route.md` §3 (method no-go) already said
so; the 267-family correction is a concrete instance of it.

---

## 1. Programme position

- Master: `docs/no-go/avenue_a_comparison_dynamics.md`
- Open core: Gap SD-K-nc-6, a single-orbit lower-deviation bound on the mean
  valuation. It implies Conjecture G (Proposition SD-K-nc6-barrier).
- Class-stability falsifier: `scripts/verify_block8_17_class_stability.py`
  (run it on any new mod-\(2^j\) row before stating it for the class).

---

## 2. What changed (this stamp)

- Checking \(1024\) members of each class refutes Thm SD-K-block-8-17-267mod8192
  (rows \(267\), \(4363\)), all of Thm SD-K-block-8-17-779mod8192, Thm
  SD-K-block-8-17-3851mod8192, the \(7627\) row of Lemma SD-K-b4start-mod8192,
  and the \(1035\) row of Cor SD-K-block5-mod8192-1035. The block-\(6\)/\(7\)
  "uniform expansion" (Cor SD-K-d6-param-267, Lemma SD-K-e7-param-267, the
  seven-block theorem) depended on treating \(h_6\) as a function of
  \(t\bmod16\), which is false.
- **Kept and now proved for all \(t\):** Lemma SD-K-e6-affine-267,
  \(3x_6+1=L_t+R_t\) with \(v_2(R_t)\ge14\) (Mahler-expansion proof).
- The four early theorems (\(3,171\bmod256\), \(323\bmod512\),
  \(579\bmod1024\)) prove only prefix inequalities. Their conclusion "Gap
  SD-K-block-8-17 holds" is withdrawn (Correction SD-K-prefix): later blocks
  can be negative, so no residue class of \(k\) is proved to satisfy the gap.

---

## 3. DO NEXT

1. Human proof read of DISJ (§4) and the two-sided window bound (§5.3) in
   `avenue_a_mean_valuation_route.md`. These are the items there that
   satisfy the admission rule's form.
2. ~~Re-audit the one-representative rows.~~ **Done (2026-10-05):**
   `scripts/prove_block8_17_classes.py` decides each class row exactly
   (Lemma SD-K-class-determinacy): \(43\) proved, \(29\) refuted, \(0\)
   undecided. New class rows must go through this prover.
3. ~~Attack the open core (Gap SD-K-nc-6).~~ **Assessed (2026-10-05):**
   Proposition SD-K-nc6-barrier (`avenue_a_mean_valuation_route.md` §7)
   shows it implies \(\operatorname{epoch}(2^n-1)\le7n\) for every odd
   \(n\), i.e. Conjecture G, which `mersenne_repunit_reduction.md`
   identifies as the general Collatz difficulty. Treat it as an open
   conjecture, not a next step.

### Anti-patterns
- Do not state a mod-\(2^j\) row for its whole class on the strength of one
  representative. A lemma of the form "data depend only on \(k\bmod2^j\)"
  needs an error-valuation bound that covers every bit the conclusion reads.
- Do not resume the deferred-row grind (\(1803,2315,\ldots\)).
- No ledger promotion; no git commit unless asked.

---

## 4. Success criteria

- [x] Block \(6\) affine identity for every \(t\) (Lemma SD-K-e6-affine-267);
- [ ] ~~Seven remaining deferred rows~~ (withdrawn: the scheme does not close);
- [ ] Gap SD-K-block-8-17 for all \(n=64k+17\): needs a non-residue input.

---

## 5. Key files

| Path | Role |
|---|---|
| `docs/no-go/avenue_a_comparison_dynamics.md` | e6/e7 params, seven-block thm |
| `scripts/explore_block8_e6_expand.py` | block \(6\) cert |
| `scripts/explore_block7_deferred.py` | block \(7\) deferred cert (built on refuted periodicity) |
| `scripts/verify_block8_17_class_stability.py` | class-stability falsifier (sampling) |
| `scripts/prove_block8_17_classes.py` | exact class prover (Lemma SD-K-class-determinacy) |
| `scripts/verify_repunit_storage_dominance.py` | regression |

---

## 6. Side branch corrected — macro-step Lundberg programme

`docs/no-go/macro_step_lundberg.md` is **not** part of the live spine and does
not feed the 267-family grind. Its former closure claim relied on identifying
a homogeneous multiplier with the true affine orbit ratio; that inference is
withdrawn.

- **Proved and kept:** MAC1–MAC3 (fuel partition, Haar renewal law, and exact
  affine macro-step), LUN1A (mean homogeneous multiplier equals one), LUN1
  (homogeneous log-multiplier exponent \(\theta^*=\ln2\)), LUN2 (a maximal
  bound for products of those multipliers, with a Haar start in Class B),
  ANC1 + capacity corollary, and FUEL1 (sufficient initial fuel forces escape
  for positive odd integers).
- **Not established:** a Haar or integer-density bound for true orbit
  escape, the earlier all-modulus refutation of DISC1, and WALSH1's claimed
  \(C=1\) bound. FUEL1 yields a finite-domain Walsh lower bound; its
  asymptotic white-noise obstruction requires densities bounded away from
  one. Escape-frequency computations are finite integer-domain evidence.
- **Recorded as unsupported route 6** in `docs/no-go/obstruction_map.md` §2.

**Possible follow-ups if the spine stalls:**

1. Literature check on LUN1A's homogeneous-multiplier identity.
   `BIBLIOGRAPHY_PASS.md` does not cover it; this is not a value-martingale
   identity for the true orbit.
2. Test ANC1-CAP against ancestry-amortization (`obstruction_map.md` §4.3).
   Modest odds; the only identified bridge from this note to a live open item.

### Anti-patterns (this branch)

- Do not use LUN2 as a bound on \(E_a\), or promote finite escape experiments
  to an infinite-domain density theorem.
- Do not treat FUEL1 alone as a refutation of every counting or spectral
  route. Any such proposal needs its own precise density and counting
  arguments; the present note does not supply them.
