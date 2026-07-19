# L5: Terminal-language classification target

**Status:** Theorem target for the bounded atlas phase. Not proved.
Checklist below is **frozen** from PCD definitions and the finite
blocked-diffuse diagnostic (`scripts/explore_atlas_l5_language.py`).
Emptying \(\mathcal R\) without this lemma does **not** establish qualitative
repunit descent.

**Logical role:** cover / classification. Required before the atlas can be
presented as a route to spine descent.

**Dependencies (intended):** PCD1, PCD8--PCD9, IEF11--IEF21,
`docs/repunit/coverage_portfolio.md`.

## 1. Why L5 is the bottleneck

IEF17 and \(\mathcal R\) are defined for itineraries in the **\(3/4\)-block
terminal language** \(\mathcal L_{3/4}\). That language is the mechanical PCD8
construction, not the PCD1 ledger label “blocked-diffuse.”

A proof that \(\mathcal R=\emptyset\) therefore yields:

> no positive-integer survivor **inside \(\mathcal L_{3/4}\)**.

It does **not** yield:

> no positive-integer survivor among **all** infinite blocked-diffuse
> primitive residuals,

unless every such residual eventually enters \(\mathcal L_{3/4}\), is already
discharged by IEF11--IEF21, or is named as an exotic class.

**Finite stress test (2026-07-14).** The only blocked-diffuse primitive
records through odd \(n\le5001\) lie on \(n=471\). Its valuation word through
80 steps has payout alphabet \(\{2,3,4,6,7\}\) and is **not** a mechanical
\(3/4\) suffix for any preperiod \(\le40\). See F-01 in
`falsification_log.md`. So \(\mathcal E\) is already forced nonempty at the
level of finite seeds, unless “blocked-diffuse” is redefined away from PCD1.

## 2. Frozen definitions

### 2.1 Blocked-diffuse (ledger state, not an itinerary language)

At a strict record-deficit prefix, following PCD1 with the diagnostic
thresholds of `scripts/explore_payout_concentration.py`:

- eligible mass \(R\): payouts with \(q\not\equiv 3,4\pmod6\);
- blocked mass \(B\): payouts with \(q\equiv 3,4\pmod6\);
- **blocked-diffuse** means: after failing the one-third eligible and
  initial tests, one has \(2B_{\max}<B\) (equivalently blocked effective
  count \(>2\) in the half-share form of PCD1).

This is a **property of a finite ledger at a record time**. An
**infinite blocked-diffuse branch** means: a nested cylinder / primitive
tail that visits blocked-diffuse record prefixes for infinitely many
depths (or, for the \(2\)-adic limit, whose every large enough finite
record prefix on the branch is blocked-diffuse). Until a theorem exists,
finite visits (as on \(n=471\)) are only **seeds** for candidate exotic
languages.

### 2.2 The language \(\mathcal L_{3/4}\) (with preperiod)

Fix \(c=\log_2(3/2)\). A valuation word \(e_0e_1e_2\ldots\) lies in
\(\mathcal L_{3/4}\) **after preperiod \(P\)** if the suffix
\(e_P e_{P+1}\ldots\) satisfies:

1. every payout (letter \(>1\)) equals \(3\);
2. every non-payout letter equals \(1\);
3. the step gaps between consecutive \(q=3\) payouts all lie in \(\{3,4\}\).

Equivalently, the suffix is a PCD8 mechanical block word: payouts of size
\(3\) separated by gaps \(r_j\in\{3,4\}\), filled with valuation one.

**Convention (frozen):** \(\mathcal L_{3/4}\) **allows a finite preperiod**
outside this pattern. IEF statements about the infinite balanced /
Sturmian / critical itinerary apply to the **suffix**. Phase shifts and
critical-slope intercepts that stay inside the \(\{3,4\}\) gap alphabet are
inside \(\mathcal L_{3/4}\); they are discharged for positive integers by
IEF11--IEF12 when the corresponding hypotheses hold, not by leaving the
language.

### 2.3 Phase shifts and intercepts

- Fixed phase shifts of the deterministic balanced word: still in
  \(\mathcal L_{3/4}\); discharged by IEF11.
- Sturmian intercepts at the critical slope: still in \(\mathcal L_{3/4}\);
  discharged by IEF12.
- Words that leave the gap alphabet \(\{3,4\}\) or introduce payouts
  \(q\neq3\) infinitely often: **not** in \(\mathcal L_{3/4}\).

### 2.4 Exotic remainder \(\mathcal E\)

A family of infinite itineraries outside \(\mathcal L_{3/4}\) that still
arise from blocked-diffuse branches (or their cylinder limits), equipped
with exact normal form, membership test, and a separate shrink programme.

**Provisional named seed (not yet a normal form):**

> **\(\mathcal E_{\mathrm{mix}}\)** — mixed-payout diffuse seeds: valuation
> words whose payout alphabet is not eventually \(\{3\}\) with gaps in
> \(\{3,4\}\), while some infinite subsequence of record prefixes is
> blocked-diffuse in the PCD1 sense. Finite prototype: \(n=471\).

Until \(\mathcal E_{\mathrm{mix}}\) has a generating rule, L5 is **not**
satisfied; the exotic slot is occupied only by a seed.

### 2.5 Demotion trigger

If an unnamed residual outside \(\mathcal L_{3/4}\) is found and not named
with an exact normal form within the bounded phase, apply **demote outcome
1** in `RESIDUAL_ATLAS.md` §7. The present \(\mathcal E_{\mathrm{mix}}\) seed
starts that clock: naming without a normal form is insufficient for
promote.

## 3. Universe \(\mathcal B\)

Work after portfolio reductions that are sound as *mechanisms*:

1. odd exponent \(n>1\);
2. not yet descended below \(M_n\);
3. not merged into a strictly smaller exponent (**primitive**);
4. visits blocked-diffuse record prefixes unboundedly often (or the
   corresponding \(2\)-adic branch).

\(\mathcal B\) is the set of infinite forward valuation itineraries
realizable by such branches. Finite certificates diagnose seeds; they do
not define \(\mathcal B\).

## 4. Precise theorem target

> **L5 (target).** Every itinerary \(w\in\mathcal B\) satisfies exactly one
> of:
>
> 1. **Discharged:** \(w\) meets a hypothesis of IEF11--IEF21 (or another
>    already-proved positive-integer discharge rule);
> 2. **Inside \(\mathcal R\):** after a finite preperiod, \(w\) lies in
>    \(\mathcal L_{3/4}\) and satisfies the IEF17 coordinates A--E;
> 3. **Exotic:** \(w\) belongs to a named class \(\mathcal E\) with an exact
>    normal form recorded in this folder (candidate slot:
>    \(\mathcal E_{\mathrm{mix}}\)).
>
> In particular, there is no unnamed blocked-diffuse primitive residual
> itinerary outside \(\mathcal L_{3/4}\cup\mathcal E\).

**Corollaries if proved.**

- Qualitative emptying of \(\mathcal R\cup\mathcal E\) empties \(\mathcal B\)
  for positive integers (up to already-discharged cases).
- The atlas becomes eligible for **promote** under
  `RESIDUAL_ATLAS.md` §7, subject to L2--L4 coupling.

**Non-goals.**

- L5 does not prove \(\mathcal R=\emptyset\).
- L5 does not prove a linear stopping bound.
- L5 does not classify blocked-concentrated, eligible, or merge branches.

## 5. Acceptable proof shapes

1. **Eventual entry:** every blocked-diffuse primitive residual eventually
   produces only gaps in \(\{3,4\}\) with payouts \(q=3\).
2. **Dichotomy:** every such residual is IEF-discharged, enters
   \(\mathcal L_{3/4}\), or matches one named exotic generator.
3. **Cylinder exhaustion:** leaving \(\mathcal L_{3/4}\) forces merge,
   descent, or exit from the blocked-diffuse branch.

Given F-01, shape (1) is already false for the finite prototype unless
\(n=471\) eventually enters \(\mathcal L_{3/4}\) after step 80. Checking
longer windows is allowed but does not remove the need for
\(\mathcal E_{\mathrm{mix}}\) until entry is proved.

## 6. Falsifiers

| Falsifier | Status |
|---|---|
| Blocked-diffuse seed outside \(\mathcal L_{3/4}\) for all tested preperiods | **Observed:** \(n=471\) (F-01) |
| Two incompatible exotic patterns with no common normal form | Open |
| Definition mismatch ledger-diffuse vs \(\mathcal L_{3/4}\) | **Confirmed:** PCD1 ≠ PCD8 language |

## 7. Formalization checklist

- [x] exact definition of blocked-diffuse (ledger vs branch)
- [x] \(\mathcal L_{3/4}\) allows finite preperiod; suffix must be mechanical
- [x] phase shifts / intercepts stay in \(\mathcal L_{3/4}\); handled by IEF11--IEF12
- [x] exotic template: \(\mathcal E_{\mathrm{mix}}\) seed named; normal form missing
- [x] demotion trigger: unnamed residual / seed without normal form

## 8. Relation to demotion

| Outcome | Atlas status |
|---|---|
| L5 proved with \(\mathcal E=\emptyset\) | Unlikely after F-01 unless \(n=471\) enters \(\mathcal L_{3/4}\) |
| L5 proved with named \(\mathcal E\) including a normal form for \(\mathcal E_{\mathrm{mix}}\) | Cover OK on enlarged universe |
| Seed only, no normal form | **Not promote-ready**; treat as leaning demote-1 until named |
| Unnamed residual beyond \(\mathcal E_{\mathrm{mix}}\) | Demote outcome 1 |

## 9. Next action

1. Decide whether to pursue a normal form for \(\mathcal E_{\mathrm{mix}}\) or
   demote the atlas as a descent route and keep IEF as local to
   \(\mathcal L_{3/4}\).
2. In parallel, falsify L2--L4 **inside** \(\mathcal L_{3/4}\) only (does not
   repair the cover gap).
3. Optional: extend `explore_atlas_l5_language.py` on \(n=471\) past first
   descent to test late entry into \(\mathcal L_{3/4}\).
