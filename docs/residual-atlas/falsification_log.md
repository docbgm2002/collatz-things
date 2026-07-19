# Falsification log (L2--L4)

**Status:** Adversarial working log. Entries are evidence against proposed
implications, not theorems.

Rule: attempt to **construct** an itinerary in \(\mathcal R\),
\(\mathcal R_1\), or \(\mathcal R_+\) that violates the hoped-for tax before
writing a proof sketch. If construction is easy, demote the implication.
If construction repeatedly hits an arithmetic wall (cylinder, carry,
ancestry), record that wall as a candidate lemma.

Universe warning: until L5 is settled, constructions outside
\(\mathcal L_{3/4}\) refute the cover (L5), not L2--L4 inside
\(\mathcal R\).

Script: `scripts/explore_atlas_l5_language.py`,
`scripts/explore_balanced_q3_residual_axes.py`.

---

## Template

```text
### F-XX — <short title>
- Date:
- Target implication: L2 / L3 / L4 / L5
- Proposed claim being tested:
- Construction:
- Result: survives / hits arithmetic wall / inconclusive
- Arithmetic wall (if any):
- Consequence for atlas:
```

---

## Open proposed implications (to attack)

### P-L2 — Recurrence forces margin or exotic

Proposed: every \(w\in\mathcal R_1\) admits either a divergent IEF18/IEF21
approximant family, a return to a discharged language, or a named exotic
normal form.

**Falsifier shape.** An aperiodic word with \(\operatorname{dio}(w)=1\),
\(\overline s(w)=0\), replenished negative valleys, and bounded directional
margins on every natural periodic-prefix family, with no exotic algebra.

### P-L3 — Positive limsup forces localized cheap approximants or rigidity

Proposed: every \(w\in\mathcal R_+\) has a fixed-surplus approximant family
with \(H_k,L_k=o(n_k)\), or an exact structural obstruction.

**Falsifier shape.** Positive limsup achieved only by rare spikes that keep
linear IEF21 draw-up/loss on every fixed-surplus approximant, with no other
obstruction.

### P-L4 — Valley replenishment couples to directional margin

Proposed: maintaining \(Z_{L_k}>B_X\) on deep negative excursions forces a
divergent IEF18/IEF21 margin or return to a discharged class.

**Falsifier shape.** Partition mass replenishes while every useful
approximant keeps bounded directional margin and the word stays in
\(\mathcal R\).

---

## Entries

### F-00 — Log initialized

- Date: 2026-07-14
- Target implication: setup
- Result: inconclusive
- Consequence for atlas: begin after L1 freeze and L5 target freeze.

### F-01 — Blocked-diffuse seed outside \(\mathcal L_{3/4}\)

- Date: 2026-07-14
- Target implication: **L5 cover**
- Proposed claim being tested: every blocked-diffuse primitive residual
  eventually enters \(\mathcal L_{3/4}\) (eventual-entry shape).
- Construction: valuation word of the unique blocked-diffuse primitive
  tail in the PCD2 census, \(n=471\), via
  `scripts/explore_atlas_l5_language.py`.
- Evidence:
  - Through 80 and 200 steps, payout alphabet is
    \(\{2,3,4,5,6,7\}\), not eventually \(\{3\}\).
  - No preperiod \(\le100\) yields a mechanical \(3/4\) suffix
    (payouts \(q=3\), gaps in \(\{3,4\}\), ones in between).
  - Ledger at diffuse records mixes eligible \(q=2\) with blocked
    \(q\in\{3,4\}\) (PCD2 profile).
- Result: **survives as a cover falsifier** for eventual-entry L5 with
  \(\mathcal E=\emptyset\).
- Arithmetic wall: none for language membership; the wall is definitional
  (PCD1 ledger ≠ PCD8 mechanical language).
- Consequence for atlas:
  - Freeze \(\mathcal E_{\mathrm{mix}}\) as a provisional exotic **seed**
    (`L5_terminal_language_target.md` §2.4).
  - Atlas is **not promote-ready** as a descent route until
    \(\mathcal E_{\mathrm{mix}}\) has an exact normal form, or \(n=471\) is
    proved to enter \(\mathcal L_{3/4}\) later (not seen by step 200).
  - Leans **demote outcome 1** if the phase ends with seed only.

### F-02 — Stock \(\mathcal L_{3/4}\) families fail to enter \(\mathcal R\)

- Date: 2026-07-14
- Target implication: L2 / L3 / L4 (prerequisite: can we even sample
  \(\mathcal R\)?)
- Proposed claim being tested: the residual-axis families contain easy
  points of \(\mathcal R\) usable as L2--L4 falsifiers.
- Construction: `explore_balanced_q3_residual_axes.py --blocks 500` on
  `mechanical`, `square-flips`, `xorshift`, `negative-bias`.
- Evidence (finite proxies only):
  - `mechanical`: directional margins \(\to+\infty\) with footprint
    (consistent with IEF10 discharge; not in \(\mathcal R\)).
  - `square-flips` / `xorshift`: positive and growing directional margins
    at caps 32/64/128; not yet a bounded-margin survivor.
  - `negative-bias`: \(S/L<0\) and \(Z\approx65.7\ll B_X\approx9.85\cdot10^5\);
    IEF15-shaped, not coordinate-E survivor.
- Result: **inconclusive for P-L2--P-L4**; stock families do not furnish
  itineraries in \(\mathcal R\).
- Arithmetic wall: none yet; sampling \(\mathcal R\) itself is the
  obstacle.
- Consequence for atlas: L2--L4 falsification needs **hand-built** words
  aimed at bounded margins + large \(Z\) on deep valleys. Easy falsifiers
  are not sitting in the existing diagnostic families.

### F-03 — Attempted L4 falsifier shape (not constructed)

- Date: 2026-07-14
- Target implication: L4
- Proposed claim being tested: P-L4 (valley replenishment ⇒ margin
  divergence).
- Construction attempted: seek a \(\{3,4\}\)-block word with
  \(S_{L_k}\to-\infty\), \(Z_{L_k}>B_X\), and bounded IEF18/IEF21 margins
  on natural periodic approximants.
- Result: **not yet constructed**. Large \(Z\) under deep negative drift
  appears to require earlier high peaks (large draw-ups), which inflate
  \(H\) / directional budgets on the same scales—suggestive of a wall,
  not a proof.
- Arithmetic wall (candidate): partition replenishment may force linear
  IEF21 draw-up on the peak-to-valley scale.
- Consequence for atlas: L4 remains the most interesting coupling
  mechanism, but only **inside** \(\mathcal L_{3/4}\); it does not repair
  F-01.

### F-04 — Hand-built peak/crash/sojourn families (refined)

- Date: 2026-07-14
- Target implication: L4 (local to \(\mathcal L_{3/4}\) after demote-1)
- Proposed claim being tested: P-L4 falsifier shape (large deep-late \(Z\)
  with non-discharging directional margins).
- Construction: `scripts/explore_atlas_l4_peak_crash.py` families
  `peak_crash_*`, `long_neg_sojourn_*`, `irregular_neg_sojourn`,
  `spike_train`, plus mechanical control (`--sojourn 8000`).
- Evidence:
  - Deepest crash bottoms have tiny \(Z\sim O(1)\)–\(O(10)\) (IEF15-shaped).
  - Large \(Z>B_X\) occurs on deep-late sojourns (critical density), but
    every such family has \(\min\) directional margin \(\gg 20\) on the
    tested caps (discharged-like / IEF18-positive), typically from a long
    pure-\(3\) prefix approximant.
  - Irregular xorshift sojourns reduce margins somewhat
    (\(\min\approx36\)) but then fail the deep-late \(Z>B_X\) test in the
    run above.
  - Corrected verdict for all tested families: **no_falsifier**.
- Result: **P-L4 still unfalsified.** Suggestive wall: replenishing
  \(Z\) at sustained negative \(S\) while keeping IEF18 margins from
  diverging was not achieved with these hand-built words.
- Consequence: after demote-1, L4 remains a plausible *local* coupling
  lemma inside \(\mathcal L_{3/4}\), not a promote path for the atlas.

### F-05 — \(\mathcal E_{\mathrm{mix}}\) normal-form failure

- Date: 2026-07-14
- Target implication: L5 / promote
- Construction: `scripts/explore_atlas_emix_probe.py --n 471`
- Evidence: full descent in 732 steps; payout alphabet
  \(\{2,3,4,5,6,7,8\}\); no mechanical \(3/4\) suffix; no nontrivial
  terminal payout/gap period (`E_mix_seed.md`).
- Result: **no normal form**
- Consequence: **demote outcome 1 hardened** in `PHASE_CHECKPOINT.md`.

---

## Next falsification tasks

1. (Optional, local only.) Seek an aperiodic \(\{3,4\}\) word with
   deep-late \(Z>B_X\) and \(\mathrm{dir\_margin}=O(1)\) or \(o(\mathrm{agr})\).
2. Do **not** reopen atlas promotion without a new cover lemma.
3. Primary programme returns to PCD/ancestry/surplus outside this folder.