# AGENT_HANDOFF_NEXT — load this first in a new chat

Status: **live spine cut = Gap SD-K-block-8-17 remainder**
(267-family block \(6\)–\(7\) uniform expansion; seven open deferred rows).
Date stamp: 2026-07-21 (SD-K-e7-param-267).
Do not reopen residual-atlas L5 / E_mix unless user explicitly asks.
Do not ledger-promote SD1/EC1/SD-L1 until a full human proof closes the gate.
Do not reopen the macro-step counting route (see §6 below).

---

## 0. One-line mission

Close the **267-family** by \(k=267+512t\). **Proved:** block \(6\) (Lemmas
SD-K-compose6, SD-K-e6-param-267, Cor SD-K-d6-param-267; six-block Thm) and
**four block-\(7\) closers** (Lemma SD-K-e7-param-267 split by \(h_6=h(z_t)\);
Thm SD-K-block-8-17-267mod512-sevenblock on \(779,3339,4875,7435\bmod{8192}\)).
**Next:** block \(7\)–\(8\) on the seven remaining deferred rows
(\(1803,2315,2827,3851,5899,6923,7947\)).

---

## 1. Programme position

- Master: `docs/no-go/avenue_a_comparison_dynamics.md`
- Block \(6\) cert: `scripts/explore_block8_e6_expand.py --check-m-param
  --check-e6-param --check-d6-param`
- Block \(7\) cert: `scripts/explore_block7_deferred.py --check-e7-param
  --check-d7-param`
- Regression: `--check-block8-k11-mod8192`

---

## 2. What changed (this stamp)

- **Block \(7\)** is not one global affine \(a-bt\bmod{8192}\); it splits by
  \(h_6=h(z_t)\) from block-\(6\) landing:
  - \(h_6=1\): \(4808-1476s\), \(s=(t-1)/4\)
  - \(h_6=3\): \(5064+4168s\), \(s=(t-3)/11\)
  - \(h_6=5\): \(4568+2124s\), \(s=(t-4)/7\)
  - \(h_6=2\): finite table \(t\in\{6,7,15\}\)
- **Thm SD-K-block-8-17-267mod512-sevenblock:** four deferred rows close at
  block \(7\) (subsumes prior Thm SD-K-block-8-17-779mod8192 on those four).

---

## 3. DO NEXT

1. **Block \(8\)** for \(3851\bmod{8192}\) (already has finite Thm; seek
   uniform expansion from block-\(7\) start).
2. **Blocks \(7\)–\(9\)** on \(1803,5899,6923,7947\) (still \(<16\) after
   block \(7\)) and block \(7\) margin on \(2315,2827\).
3. Parallel slices: \(67\bmod{256}\), \(59\bmod{64}\), EB-17 remainder.

### Anti-patterns
- No mod-\(16384\) AP theorems without a \(t\)- or \(m\)-expansion lemma.
- No ledger promotion; no git commit unless asked.

---

## 4. Success criteria

- [x] Block \(6\) uniform expansion (SD-K-e6/d6-param-267);
- [x] Four block-\(7\) deferred closers (SD-K-e7-param-267);
- [ ] Seven remaining deferred rows;
- [ ] Gap SD-K-block-8-17 for all \(n=64k+17\).

---

## 5. Key files

| Path | Role |
|---|---|
| `docs/no-go/avenue_a_comparison_dynamics.md` | e6/e7 params, seven-block thm |
| `scripts/explore_block8_e6_expand.py` | block \(6\) cert |
| `scripts/explore_block7_deferred.py` | block \(7\) deferred cert |
| `scripts/verify_repunit_storage_dominance.py` | regression |

---

## 6. Side branch closed (2026-08-03) — macro-step Lundberg programme

`docs/no-go/macro_step_lundberg.md` is **not** part of the live spine and does
not feed the 267-family grind. It is recorded here only so the closure is not
re-attempted.

- **Proved and kept:** MAC1–MAC3 (exact renewal structure), LUN1A
  (\(\mathbb E[x_{\text{out}}/x_{\text{in}}]=1\) exactly — the map is a
  martingale in value), LUN1 (\(\theta^*=\ln2\)), LUN2 (\(\mu(E_a)\le2^{-a}\),
  an "almost all" theorem), ANC1 + capacity corollary.
- **Refuted:** DISC1 (equidistribution of \(E_a\)) and the white-noise reading
  of WALSH1, both by FUEL1: \(\tau(x)\ge\lceil a/\alpha\rceil+1\Rightarrow
  x\in E_a\), so \(E_a\) contains a full residue class. WALSH1 *as literally
  written* was vacuous — implied by LUN2 with \(C=1\).
- **Now closure 6** in `docs/no-go/obstruction_map.md` §2.

**Do next only if the spine stalls,** in this order:

1. Literature check on LUN1A — cheap, settles whether the note has anything
   citable. `BIBLIOGRAPHY_PASS.md` does not cover it.
2. Test ANC1-CAP against ancestry-amortization (`obstruction_map.md` §4.3).
   Modest odds; the only bridge from this note to a live open item.

### Anti-patterns (this branch)

- No counting, equidistribution, or spectral argument over \(E_a\). The
  property those need is false, not unproven.
- No fuel-level decomposition of \(E_a\); considered and rejected, reasons in
  `macro_step_lundberg.md` §8.
