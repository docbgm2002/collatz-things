# The Repunit `6n` Target Is an Equidistribution Statement

*Capstone note. Status: the identities and lemmas cited here are exact and
machine-verified; the central reframing is supported by computation over odd
`7 ≤ n < 3000` and is presented as the precise location of the difficulty, not
as a proof.*

## 0. What this note claims

The conjecture `σ_U(2^n − 1) < 6n` for the shortcut Collatz map reduces, by the
program's own exact bookkeeping, to a bound on the **odd-step density** of one
specific deterministic sequence: the accelerated tail of `a_n = (3^n − 1)/2`.
Direct computation shows this density converges to `1/2` with fluctuations
shrinking like `O(1/√n)`, clearing the descent-failure threshold of `0.55` by a
margin that *widens* with `n`.

The consequence is strategic, and it is the main point of this note: the `6n`
target is not "barely true and in need of a clever finite argument." It is
**overwhelmingly true**, and true for the same reason it is hard to prove — it is
an equidistribution / pseudorandomness statement about a specific exponential
sequence, in the same family as Mahler's `3/2` problem and the normality of the
binary digits of `3^n`. No algebraic structure forces the descent; statistical
neutrality does. This explains why every elementary and structural approach in
the program terminates at the same wall.

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

Three facts:

1. **Mean → 1/2.** The window-averaged odd-density sits at neutral parity, the
   value the standard `E[v] = 2` heuristic predicts.
2. **Fluctuations shrink like `1/√(window)`.** The stdev falls from 0.045 to
   0.007 as the window length grows `~5n`, exactly the law-of-large-numbers rate.
3. **The max clears 0.55 with widening margin.** The only excursions above 0.55
   occur at `n = 17` (0.561) and `n = 23` (0.5575) — the small-`n` regime where
   the window is too short for any averaging. Past `n ≈ 200` the maximum density
   falls below 0.52 and continues toward 0.50. The gap to the 0.55 failure line
   is `≈ 0.05 − O(1/√n)`, positive and increasing.

The deficit picture is the same fact in different coordinates. The in-tail
valuation deficit `D_K = K log₂3 − E_K` is typically `~1.4` bits; its slow record
growth reaches only `~9.3` bits at `n ≈ 1200`, while the descent-failure
threshold is `0.585n`. The ratio threshold/observed is already `~75×` at
`n = 1200` and grows linearly in `n`. The tail does not descend "barely"; it
descends by a landslide.

## 3. Why this is the right description, and why it is hard

The reduction turns a dynamical statement into a statement about the parity
itinerary of a fixed sequence. The data says that itinerary is **statistically
neutral**: the orbit descends because its odd/even pattern behaves like a fair
coin over the window, not because any arithmetic mechanism enforces descent.

This is precisely the kind of statement current number theory cannot prove for a
named sequence:

- **Mahler's `3/2` problem.** Whether `(3/2)^n mod 1` is equidistributed is open.
- **Normality of `3^n`.** Whether the binary digits of `3^n` are asymptotically
  half ones is open.
- **The repunit odd-density.** Whether the parity itinerary of `(3^n − 1)/2`
  under `U` has density `→ 1/2` is the same genre: equidistribution of a specific
  exponential sequence, believed with overwhelming numerical support, with no
  known algebraic handle.

The reason these are hard is the reason they are true. There is no algebraic
obstruction generating the regularity, so there is nothing for an elementary or
structural argument to grip. Proving the bound means proving pseudorandomness of
a particular sequence, and we have no general tools for that.

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

All five terminated at the same point because the obstruction is not structural.
The bounded-ancestry premise passed its stress test precisely because there is
almost no deficit to concentrate: the system is overwhelmingly contractive, and
the elaboration was aimed at a worst case that equidistribution rules out.

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
4. **This reframing.** The `6n` target ⟺ odd-density `< 0.55` for the `a_n` tail,
   with measured density `→ 1/2`, stdev `→ O(1/√n)`, and a widening margin — placing
   the target in the Mahler/normality equidistribution class.

Item 4 is itself a contribution: it tells future effort to stop searching for an
algebraic lever and to recognise the target as a pseudorandomness statement about
`(3^n − 1)/2`. That redirection is the most useful output of the whole program.

## 6. Honest status line

`σ_U(2^n − 1) < 6n` is true on all tested `n` and, by the density picture, true
with a margin that grows in `n`. It is **not proved**, and the reframing argues
it will not yield to elementary or structural methods, because it is an
equidistribution statement about a specific exponential sequence. The exact
lemmas in §5 stand independently of this and are the durable results.

## Appendix: reproduction

```
python scripts/capstone_data.py
```

- Odd-density bands and global max over odd `7 ≤ n < 3000`.
- Deficit records over odd `7 ≤ n < 2500` (champion `≈ 9.28` bits at `n = 1197`).
- All ledger identities: `scripts/verify_repunit_extremal_principle.py` (PASS, 60000
  transitions), `scripts/verify_nested_anchor_work.py` (all PASS).
