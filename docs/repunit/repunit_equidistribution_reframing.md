# The Repunit `6n` Target as an Empirical Equidistribution Problem

**Status:** capstone diagnostic. The cited identities and conditional
reductions are exact and machine-verified. The parity-neutrality interpretation
is supported by computation over odd `7 ≤ n < 3000`; it is a conjectural
strategic diagnosis, not a proof of convergence or equidistribution.

**Map convention:** this note uses the shortcut map \(U\), not the accelerated
odd map \(f\) used by most of the repository. One \(f\)-step with valuation
\(e_i\) corresponds to \(e_i\) shortcut steps: one odd \(U\)-step followed by
\(e_i-1\) even \(U\)-steps. Thus the `6n` target here and the roadmap's `3n`
odd-step target are related, but neither stated bound currently implies the
other without additional valuation control.

## 0. What this note claims

The conjecture `σ_U(2^n − 1) < 6n` for the shortcut Collatz map reduces, by the
program's own exact bookkeeping, to a bound on the **odd-step density** of one
specific deterministic sequence: the accelerated tail of `a_n = (3^n − 1)/2`.
Direct computation finds density close to `1/2`, with fluctuations consistent
with `O(1/√n)` scaling over the tested range. Beyond the small-index cases, the
measurements clear the descent-failure threshold of `0.55` by a substantial
observed margin.

The consequence is strategic: the tested cases do not look close to the
failure threshold. Their behaviour suggests an equidistribution or
pseudorandomness problem for a specific exponential sequence, reminiscent of
Mahler's `3/2` problem and questions about the binary digits of `3^n`. No formal
reduction to either classical problem is claimed. This viewpoint helps explain
why the exact structural approaches developed in the programme have not yet
forced the required uniform bound.

## 1. The exact reduction (recap, all verified)

For the shortcut map `U(n) = n/2` (n even), `(3n+1)/2` (n odd):

- **Burn (exact, closed form).** `M_n = 2^n − 1` has trailing-ones run `n`. The
  decrement lemma — *`t` trailing ones with `t ≥ 2` gives `v₂(3x+1) = 1` and a
  new run of `t − 1`* — forces a deterministic countdown, so after exactly
  `n − 1` odd steps the trajectory reaches the closed form `2·3^(n−1) − 1`, and
  reaches `a_n = (3^n − 1)/2` at shortcut step `n + 1`.
- **Split.** `σ_U(M_n) = (n + 1) + H(n)`, where `H(n)` is the shortcut-step
  count from `a_n` to the first value below `2^n − 1`.
- **Sufficient density condition (verified as a conditional).** If the tail has
  not descended within `t = 5n − 2` shortcut steps, and `ρ` is the number of odd
  steps in that window, then the exact affine product gives `U^t(a_n)/T < 1`
  whenever `ρ ≤ ⌊11n/4⌋`. Equivalently: descent fails only if the odd-density
  over the window exceeds `(11/4)/5 = 0.55`.

So `σ_U(2^n − 1) < 6n` follows if the repunit tail's odd-density stays below
`0.55`.

## 2. The measured density

Odd-density of the `a_n` tail over its pre-descent window, odd `7 ≤ n < 3000`:

| n range | mean density | max | stdev |
|---------|--------------|-----|-------|
| [7, 200) | 0.4872 | 0.5610 | 0.0455 |
| [200, 800) | 0.4979 | 0.5364 | 0.0121 |
| [800, 1600) | 0.4994 | 0.5173 | 0.0076 |
| [1600, 3000) | 0.4986 | 0.5191 | 0.0072 |

Three finite observations:

1. **Mean near 1/2.** The window-averaged odd-density sits near neutral parity,
   the value the standard `E[v] = 2` heuristic predicts.
2. **Fluctuations are consistent with `1/√(window)`.** The stdev falls from
   0.045 to 0.007 as the window length grows `~5n`, matching the qualitative
   scale predicted by a law-of-large-numbers heuristic.
3. **The observed max clears 0.55 after the small-index range.** The only
   excursions above 0.55 occur at `n = 17` (0.561) and `n = 23` (0.5575) — the
   small-`n` regime where the window is too short for any averaging. Past
   `n ≈ 200` the maximum density is below 0.52 in the reported bands. The data
   is consistent with a gap of size `≈ 0.05 − O(1/√n)` from the failure line;
   this formula is not proved.

The deficit picture is the same fact in different coordinates. The in-tail
valuation deficit `D_K = K log₂3 − E_K` is typically `~1.4` bits; its slow record
growth reaches only `~9.3` bits at `n ≈ 1200`, while the descent-failure
threshold is `0.585n`. The ratio threshold/observed is already `~75×` at
`n = 1200`. Within this finite range, descent is not close to the
sufficient-condition boundary.

## 3. Why this is the right description, and why it is hard

The reduction turns a dynamical statement into a statement about the parity
itinerary of a fixed sequence. The data is consistent with a statistically
neutral itinerary over the tested windows. It does not show that no arithmetic
mechanism enforces descent.

This resembles several notoriously difficult distribution questions for named
sequences:

- **Mahler's `3/2` problem.** Whether `(3/2)^n mod 1` is equidistributed is open.
- **Normality of `3^n`.** Whether the binary digits of `3^n` are asymptotically
  half ones is open.
- **The repunit odd-density.** Whether the parity itinerary of `(3^n − 1)/2`
  under `U` has density `→ 1/2` appears to be in the same broad genre. The
  present computation supplies finite evidence, not a theorem or a formal
  equivalence to either problem above.

The comparison is diagnostic rather than definitive. A proof of the `6n` bound
might establish only the one-sided density estimate needed here, which is weaker
than full equidistribution. The current structural lemmas do not supply even
that one-sided uniform estimate.

## 4. Why this explains the program's history

Each prior layer of the program sought *structure* that forces descent:

- a Boolean/De Morgan gate reformulation (cosmetic; same arithmetic);
- a worst-case `k`-window bound (invalid denominator; withdrawn);
- a burn-budget split `5n − 2` (the `n + 1` burn miscount; corrected to the exact
  `n − 1` burn and `2·3^(n−1) − 1` landing);
- a surplus/deficit "amortization" argument (self-contradictory under `D = −S`);
- an extremal-deficit / shell-ancestry apparatus (exact identities, but its
  bounded-ancestry premise — verified to hold, ≤ 5 ancestors carry 50% of `B_K`
  even at the deepest deficits — controls a deep-deficit adversary the dynamics
  never produce).

All five terminated without a uniform theorem. The finite data suggests that
deep deficits are atypical, but it does not rule them out. The bounded-ancestry
premise passed its finite stress test in a regime where little deficit was
observed to concentrate; turning that observation into a uniform statement is
the unresolved step.

## 5. What is actually finished (and worth keeping)

These are exact and do **not** depend on the equidistribution wall:

1. **Trailing-ones decrement lemma + Mersenne burn closed form.**
   `t ≥ 2` trailing ones ⟹ `v₂(3x+1) = 1`, new run `t − 1`; hence
   `M_n → 2·3^(n−1) − 1` in exactly `n − 1` odd steps. (Algebraic proof,
   verified 2·10⁵ cases.)
2. **Extremal-storage ledger identities.** The normal form
   `x_K + 1 = 3^(n+K)/2^(E_K+1) + Z_K`, the recurrence
   `Z_{K+1} = 1 + (3Z_K − 2)/2^{e_K}`, the `v=1` conservation
   `Z_{K+1} = (3/2)Z_K`, the payout ledger `B_K`, the integer expansion of `R_K`,
   and the virtual-collision-partner identity `f(Y) = f(X)`. (All verified
   exactly with rational arithmetic.)
3. **The single-run no-go.** During a `v=1` run, `ΔD = Δlog₂Z = log₂(3/2)`: the
   exchange rate between storing and accumulating deficit is exactly one, so no
   argument confined to one valuation-one run can prove unsustainability.
4. **This reframing.** The sufficient condition for the `6n` target is
   odd-density `< 0.55` for the stated `a_n`-tail window. The measured density
   is near `1/2`, with variance consistent with `O(1/√n)` scaling. This motivates
   an equidistribution-style viewpoint without proving convergence or reducing
   the target to Mahler/normality questions.

Item 4 is a research diagnosis: future work should test whether it can prove the
specific one-sided density bound, while remaining open to an arithmetic
mechanism not visible in the present experiments.

## 6. Honest status line

`σ_U(2^n − 1) < 6n` holds for all tested `n`. The tested density bands show a
substantial margin after the small-index range. The universal inequality,
convergence to density `1/2`, and any `O(1/√n)` fluctuation law are **not
proved**. The exact lemmas in §5 stand independently of this empirical
interpretation.

## Appendix: reproduction

```
python scripts/capstone_data.py
```

- Odd-density bands and global max over odd `7 ≤ n < 3000`.
- Deficit records over odd `7 ≤ n < 2500` (champion `≈ 9.28` bits at `n = 1197`).
- All ledger identities: `scripts/verify_repunit_extremal_principle.py` (PASS, 60000
  transitions), `scripts/verify_nested_anchor_work.py` (all PASS).
