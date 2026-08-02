# Carry cocycle over the solved polynomial model  [W3]

**Task:** `OPUS5_WIDE_TASKS.md` W3 (session 12, the last of the recommended
order).
**Building on:** `recharge_nogo.md` (Lemma 1, the burn), `tower_theorem.md`
(TWR1), `outside_box_avenue_triage.md` §§1, 3 (the CQCA scalar-flux
closures), `../repunit/repunit_affine_tail_bound.md` (the affine identity).
**Script:** `scripts/explore_carry_cocycle.py`.
**Status:** **Collapses on its own kill criterion — but produces one exact
identity worth keeping**, which says precisely why the solved model is solved
and why that cannot be borrowed.
**License:** CC-BY 4.0

---

## 0. Verdict

W3 proposes writing the integer step as the \(\mathbb F_2[x]\) step composed
with a carry cocycle, then asking which repo quantities are
cocycle-cohomological. The decomposition is exact and easy. What it reveals
is that the two models are not perturbations of one another.

> **W3-A (proved here).** Encode polynomials by coefficient bits, so that
> \((x+1)P+1\) is the carry-free \(\Pi(n)=(2n\oplus n)\oplus1\). Then
> \[
> 3n+1=\Pi(n)+2\,\kappa(n)
> \]
> defines the carry defect \(\kappa\) exactly, and
> \[
> \boxed{\;v_2\bigl(\Pi(n)\bigr)=\tau(n)=v_2(n+1).\;}
> \]
> The polynomial model's valuation is exactly the **trailing-ones count**.

> **W3-B (the substantive finding).** The two valuations are **exactly
> anti-correlated**. By the burn lemma \(\tau\ge2\Rightarrow e=1\), and
> \(\tau=1\Rightarrow n\equiv1\ (4)\Rightarrow e\ge2\). Hence
> \[
> \min\bigl(e,\ v\bigr)=1\ \text{always, and }e,v\text{ are never both}>1 .
> \]
> Measured: \(e\ne v\) for **100.0%** of odd \(n<200\,001\).
>
> So "integer Collatz = polynomial Collatz + carries" is true as an identity
> and false as an approximation. The carry does not perturb the polynomial
> itinerary — it **replaces** it. The polynomial model takes its largest
> divisions \(2^{\tau}\) on exactly the states where the integer model takes
> its smallest, \(2^{1}\): the burn states. That is why the
> \(\mathbb F_2[x]\) problem is easy and this one is not, and it is why the
> settled theorem's mechanism has no transfer.

> **W3-C (the kill fires).** W3's inherited criterion: *any formulation whose
> content survives summation over a row is dead on arrival.* \(\kappa\) is a
> function of the state \(x\), and \(x\) is determined by \((x_0,\ e\text{-word})\).
> So any Birkhoff sum of \(\kappa\) carries no information beyond what the
> affine identity \(2^{E_K}x_K=3^Kx_0+c_K\) already packages into \(c_K\)
> (verified exactly, \(K=12\), all odd \(n<4001\)). Every row-summed
> formulation reproduces \(c_K\) bookkeeping — the scalar-flux collapse of
> triage §3, verbatim.
>
> What does *not* collapse is the valuation reading, since \(e\) is a local
> low-bit function of the carry rather than a row sum. But by W3-B that
> reading is anti-correlated with the polynomial model's own, so it is not a
> correction to a solved dynamics; it is a different dynamics. And it is
> exactly the \(e\)-word, which the repository already studies directly.

---

## 1. The decomposition

With \(P\) odd (\(P(0)=1\)) the \(\mathbb F_2[x]\) step is
\(P\mapsto((x+1)P+1)/x^{v}\), and every polynomial reaches 1
(Hicks–Mullen–Yucas–Zavislak 2008). In coefficient-bit encoding
\((x+1)P=xP\oplus P\) is \(2n\oplus n\), so the carry-free numerator is
\(\Pi(n)=(2n\oplus n)\oplus1\), and \(\kappa(n)=\bigl(3n+1-\Pi(n)\bigr)/2\).

| \(n\) | \(3n+1\) | \(\Pi(n)\) | \(\kappa(n)\) | \(\tau(n)\) |
|---:|---:|---:|---:|---:|
| 1 | 4 | 2 | 1 | 1 |
| 3 | 10 | 4 | 3 | 2 |
| 7 | 22 | 8 | 7 | 3 |
| 13 | 40 | 22 | 9 | 1 |
| 15 | 46 | 16 | 15 | 4 |
| 27 | 82 | 44 | 19 | 2 |

\(\kappa\) is a genuine carry functional, not a function of \(\tau\): the
tempting guess \(\kappa=2^{\tau}-1\) holds for \(n<13\) and then fails
(\(n=13,25,27,29,\dots\)). Verified exact for all odd \(n<200\,000\).

---

## 2. Why the solved model is solved

The identity \(v_2(\Pi(n))=\tau(n)\) is the whole explanation, and it is
elementary once seen: \((x+1)P\) cancels precisely along \(P\)'s trailing
run of ones, and the \(+1\) extends the cancellation by one place.

So the polynomial step divides by \(2^{\tau(n)}\). A state with a long
trailing-ones block — a Mersenne-form number, the repository's hardest lane —
is the *easiest* state for the polynomial model, collapsing by a factor
\(2^{\tau}\) in one step. For the integer model that same state is the burn:
\(e=1\), the slowest possible division, and value growth of \(3/2\) per step
sustained for the whole block (`recharge_nogo.md` Lemma 1, Theorem 2).

The polynomial orbits are correspondingly trivial: every odd \(n<20\,000\)
reaches 1, longest run 28 steps (at \(n=17\,969\)).

**The two models are not close.** They agree on no step at all in the tested
range, and the disagreement is systematic rather than occasional.

---

## 3. The TWR1 sanity check

W3's first deliverable asks for the cocycle identity verified on the tower
lane, "where TWR1 says the carry stream is exactly periodic — the cocycle
should be visibly a coboundary there, a sanity check with a known answer".

It is. On the Mersenne-form lane \(x=2^{t}u-1\),
\(3x+1=2\bigl(3\cdot2^{t-1}u-1\bigr)\) exactly (verified for \(2\le t<30\),
\(u\in\{1,3,5,7\}\)), so the carry runs the whole trailing-ones block and the
stream is periodic; \(\kappa\) is a coboundary there. Running \(w_d(M)\) for
\((d,M)=(2,13)\) and \((3,37)\) shows the \(e=2\) tower prefix followed by the
\(e=1\) burn, with \(\kappa\bmod 2^{12}\) marching through
\(4095,4095,2047,1023,511,255,\dots\) — the trailing-ones block shortening by
one bit per step, exactly as TWR1 predicts.

The check passes. But it is a lane where the answer was already known in
closed form, so it confirms the bookkeeping and nothing more — which is what
W3 said it would do, and why it was billed as deciding quickly.

---

## 4. Barrier check

1. *Finite-state.* Not invoked.
2. *Density / entropy.* Not invoked.
3. *Variable-height Diophantine.* Not invoked.
4. *Virtual sources.* Not invoked; every statement is an identity on actual
   integers.

**The binding constraint is triage §§1,3**, which W3 inherited explicitly:
CQCA scalar-flux arguments collapse to affine bookkeeping. §0's W3-C shows
the carry cocycle is exactly such an argument as soon as it is aggregated.
The escape clause W3 reserved — "only alive if it uses the two-dimensional
spacetime structure, not row sums" — is available in principle (the valuation
is a local reading), but W3-B shows that reading points away from the solved
model rather than toward it.

**Explicit non-claims.** No descent, no bound, no reformulation of SD1 as a
coboundary statement. The target "express \(R_i(n)\) or \(c_K\) as a cocycle
sum over \(\kappa\)" is achievable and empty: \(c_K\) *is* the cocycle sum,
which is the affine identity written twice.

---

## 5. Falsifier

- **W3-A** is falsified by an odd \(n\) with \(v_2(\Pi(n))\ne v_2(n+1)\), or
  with \(3n+1\ne\Pi(n)+2\kappa(n)\). Checked to \(n<200\,000\) and
  \(n<40\,000\) respectively.
- **W3-B** is falsified by an odd \(n\) with \(\min(e,\tau)>1\). Checked to
  \(n<40\,000\); it also follows from the burn lemma plus
  \(n\equiv1\ (4)\Rightarrow4\mid3n+1\), so it is a proof, not a census.
- **W3-C** is falsified by a formulation whose content survives row
  summation — i.e. an aggregate of \(\kappa\) not determined by
  \((x_0, e\text{-word})\). Since \(\kappa\) is a function of the state, this
  requires leaving the Birkhoff-sum framework entirely.

---

## 6. Reproduction

```bash
python3 scripts/explore_carry_cocycle.py
```

Prints `CARRY-COCYCLE: consistent`. Exact integer arithmetic throughout; no
floats appear.

---

## 7. Ledger

**No rows proposed.** W3-A is a small exact identity about the polynomial
analogue rather than about Collatz, and W3-B/C are scoping results.

The one thing worth carrying forward, and it belongs with the two earlier
structural morals:

> **\(v_2(\Pi(n))=\tau(n)\).** The \(\mathbb F_2[x]\) analogue is easy
> because its valuation is the trailing-ones count, which is largest exactly
> where the integer map's valuation is smallest. Any proposal to import the
> polynomial theorem should be checked against this first: the two dynamics
> are anti-correlated, not close.

This sits alongside W8 §4.1 (exact lanes shadow *rational* \(2\)-adic ghosts;
open objects shadow irrational ones) and W5-D (\(f\) destroys information
\(3\)-adically and creates it \(2\)-adically). All three are cheap filters
for deciding whether an outside method can reach this problem before a
session is spent on it.
