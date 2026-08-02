# Syracuse 3-adic distribution on the repunit family  [W5]

**Task:** `OPUS5_WIDE_TASKS.md` W5 (session 10 of the recommended order).
**Building on:** `integral_escape_frontier.md` (IEF10 and the reset-gap
frontier), `payout_concentration_diffusion.md` (PCD16–17),
`rotation_cocycle_rigidity.md` (W11), `../no-go/digit_bridge_ceiling.md`
(W10), `../density-cycles/kl_rail_restricted_tree.md` (W4).
**Script:** `scripts/explore_syracuse_3adic_conditioning.py`.
**Status:** **First deliverable complete; the conditioning is vacuous and the
target is not a corollary of Tao's mechanism.** The distributional facts are
reproduced and match the model; the reset-gap bound does not follow.
**License:** CC-BY 4.0

---

## 0. Verdict

W5 proposes conditioning Tao's Syracuse machinery on the repunit family to
get a quantitative reset-gap bound. Three findings, in order of importance.

> **W5-A (the conditioning is vacuous).** \(a_n=(3^n-1)/2\to-\tfrac12\) in
> \(\mathbb Z_3\), so every repunit seed shares one 3-adic ghost: 3-adically
> the family is a **Dirac mass**, maximally concentrated. But the affine
> identity \(x_K=(3^Kx_0+c_K)/2^{E_K}\) erases it — modulo \(3^k\) the term
> \(3^Kx_0\) vanishes as soon as \(K\ge k\), leaving
> \[
> x_K\equiv c_K2^{-E_K}\pmod{3^k},
> \]
> a function of the **valuation word alone**. So "conditioning on the repunit
> family" has no 3-adic content past step \(k\). Any two starting values
> sharing a \(K\)-step valuation word have identical residues mod \(3^k\)
> (verified on 3916 seed pairs at \(k=4\)).

> **W5-B (the distributional facts hold, and are ensemble facts).** Pooled at
> matched \(E\)-scales, the repunit states match the modelled Syracuse
> stationary law to within a small multiple of fair-sample noise. So Tao's
> stationary behaviour is reproduced here — as a statement whose average runs
> over exponents \(n\).

> **W5-C (the target is strictly harder).** The "deterministic decrement
> lemma" asks for decay along **one actual orbit**, where the average runs
> over \(K\) and there is no ensemble. That is a single-orbit equidistribution
> claim — the same object W11 showed is not reachable by rotation/cocycle
> methods and W10 showed is not reachable by digit theorems. It does not
> follow from Tao's decrement; it is what Tao's decrement is a substitute for.

And the structural reason, which is the session's most useful output:

> **W5-D (wrong prime).** \(f(x)=(3x+1)/2^{e}\) acts oppositely on the two
> primes. 3-adically it multiplies by 3, contracting at rate \(\log3=1.0986\)
> — **destroying** seed information. 2-adically it divides by \(2^{e}\),
> expanding at rate \(\mathbb E[e]\log2=1.3968\) (measured mean \(e=2.0152\)
> over 31 152 repunit steps) — **creating** it. Tao's method lives on the
> contracting side, where equidistribution is manufactured; equidistribution
> is precisely the destruction of the individual-orbit information this
> repository needs. Every structure the repo actually uses — TWR1, the burn,
> the ghosts, PCD15's "previously unseen high bits" — lives on the expanding
> side.

---

## 1. Deliverable: the empirical distribution against the Syracuse law

W5's first deliverable is the empirical 3-adic distribution "against the
Syracuse stationary measure". Getting the reference measure right is the
whole exercise, and there are two traps.

**Trap 1 — uniform on \(\mathbb Z/3^k\).** Syracuse states are never
divisible by 3: if \(3\nmid x\) then \(f(x)\equiv2^{-e}\not\equiv0\). Comparing
against uniform on \(\mathbb Z/3^k\) therefore reports a spurious bias of
order \(\tfrac12\) for *every* sequence.

**Trap 2 — uniform on the units.** The true law is not uniform on
\((\mathbb Z/3^k)^\times\) either. Already mod 3, \(x\equiv2^{-e}\), and
\(P(e\text{ odd})=\tfrac12+\tfrac18+\cdots=\tfrac23\), so

\[
P(x\equiv2\ \mathrm{mod}\ 3)=\tfrac23,\qquad
P(x\equiv1\ \mathrm{mod}\ 3)=\tfrac13 .
\]

Comparing against uniform-on-units reports a stable total variation of
\(\approx0.28\) (mod 9) and \(\approx0.35\) (mod 27) — a bias that does not
shrink with sample size and is *entirely an artefact of the wrong reference*.

**The correct reference.** Under \(P(e=j)=2^{-j}\), the pair
\((c\bmod3^k,\ E\bmod\varphi(3^k))\) is a finite Markov chain with
\(c\mapsto3c+2^{E}\), \(E\mapsto E+e\); only \(e\) mod
\(\varphi(3^k)=2\cdot3^{k-1}\) matters, and
\(P(e\equiv r)=2^{-r}/(1-2^{-\varphi})\). Its stationary law, pushed to
\(x=c\,2^{-E}\), is the Syracuse measure. Mod 3 it returns exactly
\((\tfrac13,\tfrac23)\).

### 1.1 Measured

296 orbits, 126 262 post-seed states, pooled by \(E\)-scale:

| \(k\) | \(E\)-scale | samples | TV to Syracuse law | fair-sample TV | ratio |
|---:|---:|---:|---:|---:|---:|
| 2 | 0 | 2087 | 0.0758 | 0.0195 | 3.88 |
| 2 | 16 | 2392 | 0.0115 | 0.0182 | 0.63 |
| 2 | 32 | 2370 | 0.0155 | 0.0183 | 0.85 |
| 2 | 48 | 2347 | 0.0260 | 0.0184 | 1.41 |
| 3 | 16 | 2392 | 0.0199 | 0.0336 | 0.59 |
| 3 | 32 | 2370 | 0.0316 | 0.0338 | 0.93 |
| 3 | 64 | 2302 | 0.0340 | 0.0343 | 0.99 |

Every bucket sits at ratio \(\approx1\) — indistinguishable from a fair
sample — **except the \(E\)-scale-0 bucket, at ratio 3.9.** That outlier is
an internal consistency check rather than a defect: it pools the first few
steps, which is exactly the regime where W5-A says the seed has not yet been
forgotten. The bias disappears precisely once \(K\ge k\), as predicted.

### 1.2 Single orbits

| \(n\) | states | \(k\) | TV to Syracuse law | fair-sample TV | ratio |
|---:|---:|---:|---:|---:|---:|
| 471 | 732 | 2 | 0.0238 | 0.0330 | 0.72 |
| 471 | 732 | 3 | 0.0417 | 0.0608 | 0.69 |
| 1197 | 1635 | 2 | 0.0242 | 0.0221 | 1.10 |
| 2001 | 2776 | 2 | 0.0079 | 0.0169 | 0.47 |
| 2001 | 2776 | 3 | 0.0174 | 0.0312 | 0.56 |

A single orbit — including \(n=471\) — matches the Syracuse law as well as a
fair sample of its own size would.

---

## 2. Which characters carry the plateau obstruction?

W5 asks to "identify which characters carry the plateau obstruction". The
answer follows from W5-A and is negative in a specific way.

Since \(x_K\equiv c_K2^{-E_K}\pmod{3^k}\) depends only on the valuation word,
the 3-adic characters see **exactly the valuation word and nothing else**.
The plateau obstruction, by PCD13/PCD14 and W11-C, is a matching between the
affine lift word and a window of the binary digits of \(3^{n_m}\) — a
condition on the **2-adic** side, involving the exponent representative
\(n_m\), which the 3-adic residues have forgotten.

So no 3-adic character carries the plateau obstruction. They carry the
valuation word, which is the *input* to the plateau condition, not the
coincidence itself.

---

## 3. Why the decrement lemma does not follow

Tao's decrement is a statement about the distribution of
\(\mathbf{Syrac}(\mathbb Z/3^n)\) — an average over valuation words drawn
from a measure. The repunit family supplies **one** word per exponent, and
the target statement quantifies over the actual word of an actual orbit.

Formally the difference is the usual one between

\[
\Bigl|\ \mathbb E_{\text{words}}\bigl[e_{3^k}(\xi\,x)\bigr]\Bigr|\ \text{small}
\qquad\text{versus}\qquad
\Bigl|\ \tfrac1L\textstyle\sum_{K<L}e_{3^k}(\xi\,x_K)\Bigr|\ \text{small},
\]

and no amount of the first gives the second for a prescribed sequence. §1.2
shows the second *holds numerically*, which is worth recording as evidence
and worthless as a proof — it is precisely the kind of observation barrier 2
exists to discount.

This is the third consecutive session to land on the same object. W11 reached
it from the ergodic side (no compact-group extension, so no every-point
theorem); W10 reached it from the arithmetic side (Stewart bounds a global
count, not a local run); W5 reaches it from the distributional side. The
object is single-orbit equidistribution of a deterministic sequence built
from powers of 3, and nothing in the current literature supplies it.

---

## 4. Barrier check

1. *Finite-state.* Not invoked.
2. *Density / entropy.* **Binding.** W5's own framing conceded that
   distributional statements cannot kill a cylinder and reserved the task as
   an attack on the quantitative reset gap. §3 shows the reserved attack does
   not go through either, because the ensemble/single-orbit gap is exactly
   where the reset gap lives. W4 (session 9) sharpens the general point;
   this note is its distributional instance.
3. *Variable-height Diophantine.* Not invoked.
4. *Virtual sources.* Not invoked; §1.2 uses actual orbits.

**Explicit non-claims.** No reset-gap bound is obtained. No improvement to
IEF10 is claimed. The Syracuse-law agreement in §1 is finite evidence about a
model fit, not a theorem about repunit orbits, and the single-orbit agreement
in §1.2 is an observation about three sequences.

---

## 5. Falsifier

- **W5-A** is falsified by a \(K\ge k\) and two seeds with the same
  \(K\)-step valuation word but different residues mod \(3^k\). The identity
  \(x_K\equiv c_K2^{-E_K}\) is checked directly for \(k\le4\), \(K\le11\).
- **W5-B** is falsified by an \(E\)-scale bucket whose TV to the modelled law
  stays a large multiple of fair-sample noise as the sample grows. The
  \(E\)-scale-0 bucket does exceed it, for the reason §1.1 gives; if that
  excess persisted at large \(E\) the model would be wrong.
- **W5-D** is falsified by a mean valuation far from 2 on repunit orbits,
  which would change the balance of the two rates. Measured: 2.0152.

---

## 6. Reproduction

```bash
python3 scripts/explore_syracuse_3adic_conditioning.py               # n <= 601
python3 scripts/explore_syracuse_3adic_conditioning.py --nmax 1001
```

Prints `SYRACUSE-3ADIC: consistent`. All structural claims are exact integer
arithmetic; floats appear in the modelled stationary law (computed by power
iteration) and in the total-variation figures, which are averages.

---

## 7. Ledger

**No rows proposed.** W5-A is a one-line consequence of the affine identity
and belongs in this note rather than the ledger; W5-B is a model fit; W5-C
and W5-D are scoping results.

The one thing worth carrying forward is **W5-D**, as a planning heuristic
alongside W8 §4.1's rational/irrational-ghost observation:

> The Collatz map destroys information 3-adically and creates it 2-adically.
> Methods that manufacture equidistribution work on the 3-adic side and
> therefore cannot see an individual orbit; every exact structure this
> repository owns lives on the 2-adic side. A proposed import from the
> probabilistic literature should be checked against this before a session is
> spent on it.
