# Is the IEF17 survivor profile generic?  [W7]

**Task:** `OPUS5_WIDE_TASKS.md` W7 (session 11 of the recommended order).
**Building on:** `integral_escape_frontier.md` §§20–21 (IEF15, IEF16, IEF17)
and §§22–25 (IEF18–IEF21), `dio1_cocycle_problem.md` (the exact definitions
of \(\operatorname{dio}\), \(\operatorname{rep}\), drift),
`rotation_cocycle_rigidity.md` (W11, for \(\beta\)),
`syracuse_3adic_conditioning.md` (W5, which removed one of the arithmetic
inputs W7 nominates).
**Script:** `scripts/explore_ief17_genericity.py`.
**Status:** **Frontier sharpened; the split is the result.** The symbolic
coordinates are generic (W7 outcome 2 holds for them); the one arithmetic
coordinate is not, and it discharges the generic word outright.
**License:** CC-BY 4.0

---

## 0. Verdict

W7 offers two acceptable outcomes: (1) a literature theorem empties the
IEF17 class, or (2) a certified example word realising the full profile,
proving the symbolic route cannot close alone.

The answer splits along the five IEF17 coordinates, and the split is the
finding.

> **W7-A (the symbolic coordinates are free).** Under the natural critical
> ensemble — Bernoulli block words with \(P(r{=}4)=\beta=0.419022\ldots\),
> the unique frequency giving zero drift — coordinates 2, 3 and 4 hold
> **almost surely**:
> - \(\liminf S_L/L=0\) by the law of large numbers;
> - \(\operatorname{dio}(w)=1\), because the excess repetition is
>   \(O(\log L)\) (measured \(g=17\)–\(23\) against \(\log_2L\approx16\));
> - no periodic-prefix margin diverges, by the same \(O(\log L)\) bound
>   against a growing \(2\log_2N_k\).
>
> So the symbolic portfolio IEF13–IEF21 discharges essentially nothing in the
> critical ensemble. **W7 outcome 2 holds for the symbolic coordinates.**

> **W7-B (the arithmetic coordinate is the binding one, and it fires).**
> Coordinate 5 **fails** generically. \(Z_L\) at a record low of \(S\) is
> \(O(1)\): a fresh record has, by definition, accumulated no time at or
> below its own level, so the suffix partition stays tiny. Measured over
> 910 record lows in three trials of \(10^5\) blocks: **not one** exceeded
> \(B_X\), and the largest \(Z\) seen was \(583.3\) against
> \(B_X=984\,615\) — a factor of \(1.7\times10^3\). By IEF15 + FIN1 the
> generic critical word is therefore **discharged**.

> **W7-C (the sharpened frontier).** The IEF17 residual is **not** generic;
> it has measure zero in the critical ensemble, and coordinate 5 is the
> single binding condition. A survivor must accumulate \(Z>10^{6}\) worth of
> suffix mass before all but finitely many of its record lows — a structural
> demand that coordinates 2–4 do not imply and that a random word never
> meets.

And the observation worth carrying: **coordinate 5 is the only coordinate
carrying an arithmetic input** (\(B_X=64X/65\) comes from FIN1). The purely
symbolic coordinates are free; all the content sits in the arithmetic one.

---

## 1. The mapping (W7's first deliverable)

| # | IEF17 coordinate | condition | character | sharpest relevant input | generic? |
|---|---|---|---|---|---|
| 1 | starting size | \(x_0>10^{6}\) | arithmetic | FIN1 | n/a — not a word condition |
| 2 | density drift | \(\liminf S_L/L=0\) | symbolic | López–Stoll, via IEF16 | **yes** (SLLN) |
| 3 | symbolic/drift axis | \(\operatorname{dio}(w)=1\) or \(\limsup S_L/L>0\) | symbolic | Bugeaud–Kim repetition exponents (IEF12, IEF19) | **yes** (repeats are \(O(\log L)\)) |
| 4 | periodic-prefix margin | no divergent \(G_k-J(A_k)-J(B_k)-2\log_2N_k\) | symbolic | IEF18/IEF21 contrapositives; Adamczewski–Bugeaud complexity is the ambient literature | **yes** (same \(O(\log L)\) bound) |
| 5 | negative excursions | \(Z_{L_k}>B_X\) whenever \(S_{L_k}\to-\infty\) | **arithmetic** | IEF15 + FIN1 | **no** |

**Where the literature W7 nominates would enter, and why it does not help.**
Berthé–Delecroix bounded remainder sets, Ostrowski carry automata and the
Adamczewski–Bugeaud complexity bounds all speak to coordinates 3 and 4.
Those coordinates are already generic — there is nothing left for a sharper
theorem to discharge. Mining that literature further would refine conditions
that a random word satisfies anyway. That is the concrete answer to "map each
coordinate to the sharpest known theorem, with the gap stated exactly": for
coordinates 2–4 the gap is **zero and uninteresting**, because the conditions
are satisfied by almost every word; the whole gap is at coordinate 5, where
the literature in question says nothing.

---

## 2. The set-up, exactly

With \(c=\log_2(3/2)\) the block drift is \(\Delta(r)=cr-2\) (IEF16 §20), so

\[
\Delta(3)=-0.245112\ldots,\qquad \Delta(4)=+0.339850\ldots,
\qquad S_L=\sum_{j\le L}\Delta(r_j).
\]

Zero drift requires \(P(r{=}4)=\beta=2/c-3=0.419022\ldots\) — the same
\(\beta\) that is the Sturmian slope in W11, for the same reason. The
verifier confirms the drift of the critical measure is \(0\) to
\(5.6\times10^{-17}\).

\(Z_L=\sum_{j\le L}2^{S_L-S_j}\) obeys the one-line recursion
\(Z_L=2^{\Delta_L}Z_{L-1}+1\), which is what makes the measurement cheap.

**How coordinate 3 is measured.** By the Bugeaud–Kim definition
(`dio1_cocycle_problem.md`), \(\operatorname{dio}(w)\ge\rho\) needs
arbitrarily long prefixes \(UV^{t}\) with \(|UV^{t}|/|UV|\ge\rho\). Writing
\(g(n)\) for the largest \(\ell-p\) over periods \(p\) and \(p\)-periodic
suffixes of length \(\ell\) of the prefix of length \(n\),

\[
\operatorname{dio}(w)=\limsup_n\frac{n}{n-g(n)} ,
\]

so \(g=O(\log n)\) forces \(\operatorname{dio}(w)=1\). The same \(g\) bounds
the agreement excess \(G_k\) of a periodic prefix approximant, which is why
one measurement settles both coordinates 3 and 4. This is robust to the
normalisation convention: \(\operatorname{dio}>1\) needs repetitions of length
*linear* in the position, and a Bernoulli word has none.

---

## 3. Measured

Three trials, \(10^{5}\) blocks each, seed 20260801.

**Coordinates 2–4.** \(|S_L/L|\le0.005\) at every checkpoint; excess
repetition \(g\in\{17,21,23\}\) against \(\log_2L\approx16.6\), giving
\(\operatorname{dio}(w)\le1.0004\).

**Coordinate 5.**

| | trial 1 | trial 2 | trial 3 (all pooled) |
|---|---:|---:|---:|
| record lows | 630 | 58 | 910 total |
| max \(Z\) at a record low | 583.3 | 193.1 | **583.3** |
| median \(Z\) | 52.5 | 81.5 | — |
| records with \(Z>B_X\) | 0 | 0 | **0 of 910** |

\(Z\) at record lows does not grow with \(L\) (means over the first and
second halves of the records agree to within a factor two), and sits three
orders of magnitude below \(B_X=984\,615\).

**Why, structurally.** \(Z_L\approx\#\{j\le L: S_j\le S_L+O(1)\}\), the time
spent at or below the current level. At a *fresh record low* that set is by
definition only the current excursion — the running minimum sits at the edge
of the walk's range, where local time is \(O(1)\), not in the bulk, where it
would be \(\Theta(\sqrt L)\). Since new record lows recur forever and each
resets \(Z\) to \(O(1)\), coordinate 5's "all but finitely many" requirement
fails almost surely.

*(This corrects an expectation I formed before measuring: I had assumed
\(Z\) at minima would inherit the \(\Theta(\sqrt L)\) local time of a
recurrent walk and hence eventually clear \(B_X\). It does not, because the
minimum is at the edge of the range. The measurement is what caught it.)*

---

## 4. What this means for the programme

1. **Stop mining combinatorics-on-words for this frontier.** Coordinates 2–4
   are satisfied by almost every critical word. A sharper Berthé–Delecroix or
   Adamczewski–Bugeaud theorem would discharge a subset of a measure-zero
   set. W7's "outcome 1" is unreachable *through the symbolic coordinates*.
2. **IEF15 is doing more work than the frontier table suggests.** It is the
   only coordinate that bites on a random word, and it bites hard (factor
   \(1.7\times10^{3}\)). The residual profile is thin precisely because of
   it.
3. **The next quantitative question is about \(Z\), not about words.** What
   structure forces a word's suffix partition above \(10^{6}\) at every deep
   excursion? That is a question about the interaction between the drift path
   and FIN1's numerical cutoff, and it is where a sharper lemma would pay.
4. **Raising FIN1's cutoff has direct leverage here**, and this is the one
   cheap actionable consequence: \(B_X\) scales linearly with \(X\), so
   extending the exhaustive descent certificate raises the bar a survivor
   must clear at every record low. Unusually for this repository, more
   computation would genuinely tighten a frontier coordinate rather than
   just extend a census.

---

## 5. Barrier check

1. *Finite-state.* Not invoked.
2. *Density / entropy.* The measure-theoretic statements here are used
   **negatively** — to show a proposed *method* (symbolic classification)
   cannot bite — never to eliminate a cylinder or to claim descent. Triage
   §13's warning ("word-complexity facts without an exact descent-or-merger
   consequence do not promote") is respected: nothing is promoted, and W7's
   own exemption for outcome-2-style results covers §0.
3. *Variable-height Diophantine.* Not invoked.
4. *Virtual sources.* Not invoked. Note the honest limit: these are
   statements about **words**, and a generic word is not a realised integer.
   Realisation is exactly the arithmetic condition IEF7/IEF10 impose. Nothing
   here asserts a survivor exists.

**Explicit non-claims.** IEF17 is not shown empty, no coordinate is
discharged, and no new theorem about realised integers is obtained. The
result is about which coordinates carry content.

---

## 6. Falsifier

- **W7-A** is falsified by a critical-ensemble coordinate among 2–4 that
  fails with positive probability — e.g. excess repetition growing faster
  than \(O(\log L)\), which would raise \(\operatorname{dio}\) above 1.
- **W7-B** is falsified by a record low with \(Z>B_X\) appearing at
  reachable \(L\), or by \(Z\) at record lows showing genuine growth in \(L\).
  Both are directly measured; a longer run (`--blocks 400000`) is the check.
- **W7-C** is falsified if coordinate 5 turns out to be implied by
  coordinates 2–4 for some structured subclass — which would collapse the
  split this note reports.
- The whole framing assumes the critical Bernoulli measure is the right
  ensemble. A different natural measure on the \(3/4\)-block language (for
  instance one conditioned on realisability) could change which coordinates
  are generic. That is the main modelling risk and it is not tested here.

---

## 7. Reproduction

```bash
python3 scripts/explore_ief17_genericity.py
python3 scripts/explore_ief17_genericity.py --blocks 400000 --trials 5
```

Prints `IEF17-GENERICITY: symbolic coordinates generic; coordinate 5
binding`. The drift arithmetic is exact; the word ensemble is sampled, and
every conclusion drawn from it is stated as a measure-theoretic or empirical
claim, never as a theorem about a particular integer.

---

## 8. Ledger

**No rows proposed.** This is a scoping result about where the content of
IEF17 sits, not a new claim about survivors. The two things worth carrying
into planning notes:

- coordinates 2–4 of IEF17 are generic, so combinatorics-on-words is spent
  as an attack on this frontier;
- coordinate 5 (IEF15 + FIN1) is the binding one, and raising FIN1's cutoff
  \(X\) tightens it linearly.
