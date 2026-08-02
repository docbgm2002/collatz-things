# Avenue A — the mean-valuation reformulation, the modulus no-go, and a disjunctive cut

**Status:** Working note. Nothing here is a claim-ledger promotion.

Contents, by what each part is worth:

| § | Content | Class |
|---|---|---|
| 2 | Gap SD-K-911-6-strong \(\iff\) mean valuation \(\ge20/11\) | **proved reformulation** |
| 3 | No modulus closes the mod-\(2^m\) case bash | **method no-go** (mechanical) |
| 4 | The two window cuts have **disjoint** finite misses | **finite certificate**, \(n\le1781\) |
| 4.1 | Extremal calibration: risk confined to \(n\lesssim341\), safety \(\sim\sqrt n\) | **calibration** (measurement), with falsifier |
| 5 | The window \(t=cn\) is a **two-sidedly** bounded parameter: \(4.5605<c<12.3565\) | **proved bounds**; corrects a wrong recommendation made earlier in this note |
| 5.1 | BAKEX2 tolerates any \(c\) (crossover \(161+14.3\log_2(c/6)\)) | **proved** (rerun of W9-B; \(c=6\) reproduces \(161\)) |
| 5.2 | Lemma SD-K-density-15, uniform exact envelope | **proved**, certified by \(3^{37}<2^{64}\); **correct but not useful** — see §5.3 |
| 5.3 | \(c=15\) is outside the honest range; **WIDE-15 retracted** | retracted; the reason is the useful part |
| 6 | A PCD9/PCD10 route — **proposed, then refuted by its own falsifier** | retracted; recorded |

**Net effect.** Two things survive: the reformulation (§2) with the modulus
no-go (§3), and DISJ (§4). The window relaxation does **not** survive: §5.3
shows the parameter \(c\) is bounded above as well as below, and that the
repository's \(c=6\) already sits in the right band. Both retractions in this
note came from the same mistake — *treating a larger numerical margin as
progress without asking what the margin was borrowed against.*

**Parent:** [`avenue_a_comparison_dynamics.md`](avenue_a_comparison_dynamics.md)
§13–§14.
**Reproducer:** `python3 scripts/explore_mean_valuation_gap.py --mmc`

---

## 1. Applicability predicate

Odd \(n\ge3\); \(a_n=(3^n-1)/2\). Two bookkeepings are used and must not be
mixed:

- **Shortcut window.** \(T(x)=(3x+1)/2\) on odd, \(x/2\) on even; run \(t\)
  steps from \(a_n\) and let \(\rho_t(n)\) be the number of odd steps. Total
  halvings over the window are exactly \(t\).
- **Accelerated first descent.** \(x_{i+1}=f(x_i)\), \(e_i=v_2(3x_i+1)\),
  \(K=K_\downarrow(n)\) the first index with \(x_K<M_n=2^n-1\),
  \(E_K=\sum_{i<K}e_i\).

**Logical role.** §2 is a restatement. §3 deletes a method, not a residual.
§4 is a finite certificate with a stated domain. §5 is retracted.

---

## 2. The gap is exactly a mean-valuation statement (proved)

Avenue A's score on a window of length \(t\) is \(\mathrm{rest}=11E-9O\) with
\(O=\rho_t\) and \(E=t-\rho_t\). Hence

\[
\mathrm{rest}\ge0
\iff
\rho_t\le\tfrac{11}{20}t
\iff
\boxed{\ \frac{t}{\rho_t}\ \ge\ \frac{20}{11}=1.8181\ldots\ }
\]

and \(t/\rho_t\) is exactly the **mean valuation** of the accelerated orbit
over the window (\(t\) halvings spread over \(\rho_t\) accelerated steps).

> **Reformulation (proved).** Gap SD-K-nc-6 is *exactly* the statement that
> the mean valuation of the \(a_n\) orbit over the window \(t=6n\) is at least
> \(20/11\).

**Exact scope, since the neighbouring gaps are not literally identical.**

- **Gap SD-K-nc-6** (\(\rho_{6n}\le\lfloor33n/10\rfloor\)) is the reformulation
  on the nose: \(\lfloor\tfrac{11}{20}\cdot6n\rfloor=\lfloor33n/10\rfloor\).
- **Gap SD-K-911-6-strong** carries the \(+2\) strengthening
  (\(11(t-\rho)\ge9\rho+2\)) that removes an off-by-one at
  \(n\equiv3,9\pmod{10}\). It is the reformulation with the threshold nudged
  to \(t/\rho\ge20/11+2/(20\rho)\) — the same statement asymptotically, one
  unit stronger at finite \(n\).
- **Gap SD-K-res-dens-17 / Gap SD-K-block-8-17** are the same inequality
  *restricted to \(n\equiv17\pmod{64}\)* and rebased on the residual window
  after the seed and first block. They are instances, not equivalents.

Everything below uses the nc-6 form.

This is worth having because the unconditional expectation of \(e\) is \(2\)
(geometric, \(P(e=k)=2^{-k}\)). The gap therefore asks that a **constant-size
lower deviation** — \(0.18\) below the mean, sustained over \(\rho\asymp3n\)
steps — be impossible for one deterministic orbit.

**Validation: the reformulation recovers both documented exception lists.**

| window | odd \(n\) with mean valuation \(<20/11\) | repository's documented exceptions |
|---|---|---|
| \(t=6n\) | \(\{5,\,11\}\) (checked \(n\le401\)) | \(n=11\) is the unique 911-6-strong miss; \(n=5\) handled direct; \(n=17\) is the equality case (margin \(+0.0032\)) |
| first descent, \(E_K/K_\downarrow\) | \(\{5,\,17,\,23\}\) (checked \(n\le6001\)) | \(n=17,23\) are exactly the \(5n-2\) even-budget saturations; \(n=23\) the unique 911 miss |

Two different windows, two different exception sets, each reproducing
independently-derived lists from the note. That agreement is the evidence
that \(t/\rho_t\) is the right invariant rather than a coincidence of weights.

**Window minima of \(E_K/K_\downarrow\) (measured, \(n\le6001\)).**

| \(n\) window | min | argmin | margin over \(20/11\) |
|---|---|---|---|
| \([16,32)\) | 1.804348 | 17 | \(-0.0138\) |
| \([128,256)\) | 1.838710 | 131 | \(+0.0205\) |
| \([512,1024)\) | 1.933808 | 837 | \(+0.1156\) |
| \([1024,2048)\) | 1.943882 | 1335 | \(+0.1257\) |
| \([4096,6001)\) | 1.937329 | 4401 | \(+0.1191\) |

The window minimum **rises** and settles near \(1.93\): the deviation needed
is a constant \(0.18\) while the fluctuation scale is \(O(\sqrt{\log n/n})\).
The gap is marginal only at \(n\le23\), which is exactly where the finite
certificates saturate.

---

## 3. Method no-go: no modulus closes the case bash (mechanical)

§14 item 1 proposes continuing \(k\bmod2^{13}\to2^{14}\to\cdots\) on
\(n=64k+17\). That programme has no terminating condition.

Model the pre-descent orbit as a walk on the **block automaton**: states are
odd residues \(x\bmod2^m\) with \(h(x)=v_2(x+1)=1\); one edge per block
(payout \(e\ge2\), landing of height \(h\), then \(h-1\) rails via
Lemma SD-K-rail-closed); weight \(\Delta=11(e-1)-9h\). Every real itinerary is
a walk in this graph, so its average \(\Delta\) is at least the minimum mean
cycle. A **positive** minimum mean cycle would give \(\mathrm{rest}\ge-O(1)\)
uniformly in \(n\) and close the gap outright — this is the max-plus dual of
the Bellman–Ford negative-cycle machinery already used for QLG1/WITN1, run
for a lower bound instead of a certificate. It had not been computed. It is:

| \(m\) | states | edges | min mean cycle of \(\Delta\) |
|---|---|---|---|
| 6 | 16 | 176 | \(-106\) |
| 8 | 64 | 1408 | \(-106\) |
| 10 | 256 | 9472 | \(-106\) |
| 12 | 1024 | 57344 | \(-106\) |

\(-106=11-9\cdot13\) is a single self-loop at the deepest landing the
enumeration allows, so the value diverges to \(-\infty\) with lift depth, and
it is **independent of \(m\)**. Capping landings at \(h\le h_{\max}\) gives
\(-7,-16,-25,-34,-43,-61\) for \(h_{\max}=2,3,4,5,6,8\), again identical at
\(m=8\) and \(m=10\).

> **Method no-go (mechanical).** For every \(m\) the block automaton
> \(\bmod\,2^m\) contains cycles of arbitrarily negative mean \(\Delta\).
> No argument whose only input is "the block outcome is determined by
> \(x\bmod2^m\)" can prove \(\mathrm{rest}\ge0\), at any \(m\).

**Why this bites on the actual case bash — the prefix/tail split.** The
`Thm SD-K-block-8-17-*` results condition on \(k\bmod2^{j}\), which is more
than mod-\(2^m\) state information: by PCD9 a residue class mod \(2^{E}\)
pins the valuation word of total valuation \(E\) **exactly**. Since \(E\)
grows by about \(2\) per block, fixing \(k\bmod2^{j}\) determines roughly the
first \(j/2\) blocks and *nothing after them*. So a case bash at modulus
\(2^{j}\) controls a prefix of \(\Theta(j)\) blocks and must bound the
remaining \(\Theta(n)-\Theta(j)\) blocks by other means. The bad cycles above
live in that uncontrolled tail, where the only available information is the
mod-\(2^m\) state. Raising \(j\) lengthens the controlled prefix but never
reaches the tail, because the tail has length \(\Theta(n)\) while \(j\) is a
constant. That is the precise sense in which the scheme has no terminating
condition.

**What the no-go does *not* say.** It does not say a bad cycle is realized by
an actual \(a_n\) orbit — that is the realizability question, and §6 records
what happens when one forgets to ask it. The claim is about what the
abstraction can *prove*: a method that cannot distinguish \(a_n\)'s tail from
any other walk in the graph cannot prove a statement false for some walks.

**Where the bad cycle lives.** The \(h_{\max}=2\) value \(-7=11-18\) sits on
the cycle whose \(2\)-adic fixed point solves \(x+1=3((3x+1)/4+1)/2\), i.e.
\(x=-7\) — REPLOW3's own ghost. Excising the ball \(v_2(x+7)\ge D\) does
**not** repair it (the minimum moves to \(-68\), then \(-88\)): deep-landing
self-loops are dense in the state space, and \(-7\) is one bad cycle of many.

**Consequence.** The eight proved `Thm SD-K-block-8-17-*` rows and the
density-\(9/1024\) corollary are genuine; the *scheme* does not extend to a
cover. This is the Avenue A instance of SH1: \(\Delta\) is a potential in
local coordinates, and SH1 says no such potential is nonincreasing.

**Second, independent reason the score cannot close alone.** The score
threshold is \(\rho/t\le11/20=0.55\). The stay-above size constraint
(SD-K-density-6) only forces \(\rho/t\ge(t+1-0.585n)/(1.585\,t)\), which at
\(t=6n\) is \(\approx0.55\) — the two thresholds coincide by construction, so
tuning the window \(t\) cannot make them cross. Any closure needs an
arithmetic input bounding \(\rho/t\) away from \(1\); no size or
window-tuning escape exists.

---

## 4. Disjunctive cut: the two finite misses are complementary (finite certificate)

The note treats \(t=5n-2\) and \(t=6n\) as competing cuts and prefers \(6n\)
because it has one finite miss instead of two. They are better used as a
**disjunction**, because their misses are disjoint:

| \(n\) | margin at \(t=6n\) | margin at \(t=5n-2\) | max |
|---|---|---|---|
| 11 | \(-0.081340\) | \(+0.009404\) | \(+0.009404\) |
| 17 | \(+0.003247\) | \(-0.013834\) | \(+0.003247\) |
| 23 | \(+0.021818\) | \(-0.024531\) | \(+0.021818\) |
| 25 | \(+0.033670\) | \(+0.017639\) | \(+0.033670\) |
| 131 | \(+0.035592\) | \(+0.016088\) | \(+0.035592\) |

> **Finite certificate (DISJ, \(7\le n\le1781\) odd).** For every odd
> \(7\le n\le1781\), at least one of \(t=5n-2\), \(t=6n\) satisfies
> \(t/\rho_t\ge20/11\). No \(n\ge7\) in range fails both. \(n=5\) fails both
> and is already handled directly (\(K_\downarrow(5)=30\)).

Extended past the original \(601\): through \(1781\) **neither single cut fails
anywhere above \(n=601\)**, and the tightest disjunctive margin in
\(603\le n\le1781\) is \(+0.1250\) at \(n=1335\) — a factor \(39\) looser than
the binding case \(n=17\). All exceptional behaviour is confined to
\(n\le23\).

**Cross-check against the parent note (independent of this note's code).**
Since DISJ is a pure finite certificate, its only failure mode is a bug in
\(\rho_t\). Three values stated in `avenue_a_comparison_dynamics.md` are
reproduced exactly:

| stated in parent note | recomputed here | |
|---|---|---|
| "\(\rho_{66}=38>36=\lfloor33\cdot11/10\rfloor\)" at \(n=11\) | \(\rho=38\), cap \(36\) | match |
| "equality only at \(n=17\)" for the \(6n\) cut | \(\rho=56=\) cap \(56\) | match |
| the \(5n-2\) even budget "saturates at \(n=17,23\)" | both exceed cap by exactly \(1\) | match |

Since Lemma SD-K-linear-6 and its \(5n-2\) analogue both conclude
\(K_\downarrow\le6n\), proving the **disjunction** suffices and is strictly
weaker than either gap. This retires the \(n=11\) special case (currently
carried by \(H(11)\le66\)) and the \(n=17\) equality case at once — both were
artifacts of committing to a single window.

The two tightest cases in range are \(n=17\) and \(n=11\), each rescued by the
other cut. Extending DISJ beyond \(601\) is cheap and is the first thing to do
with this note.

---

### 4.1 Extremal calibration: where a violation could still hide

DISJ and Gap SD-K-nc-6 are checked, not proved, so the useful question is not
"does the check extend" but **"where would a violation have to live?"** In
W13's idiom (`extremal_law_calibration.md`), calibrate the margin

\[
M(n)=\frac{6n}{\rho_{6n}(n)}-\frac{20}{11},
\qquad
M(n)>0\iff\text{the }6n\text{ cut holds at }n.
\]

**Measured, odd \(5\le n\le1781\).**

| \(n\) window | count | mean \(M\) | sd \(M\) | min \(M\) | argmin | \((\mu-\min)/\mathrm{sd}\) | \(\sqrt{2\ln N}\) |
|---|---|---|---|---|---|---|---|
| \([64,128)\) | 32 | \(+0.15422\) | 0.07763 | \(+0.02957\) | 89 | 1.61 | 2.63 |
| \([128,256)\) | 64 | \(+0.19140\) | 0.07084 | \(+0.03559\) | 131 | 2.20 | 2.88 |
| \([256,512)\) | 128 | \(+0.18643\) | 0.04392 | \(+0.10428\) | 281 | 1.87 | 3.12 |
| \([512,1024)\) | 256 | \(+0.18752\) | 0.02395 | \(+0.11942\) | 621 | 2.84 | 3.33 |
| \([1024,1782)\) | 379 | \(+0.18038\) | 0.02274 | \(+0.12505\) | 1335 | 2.43 | 3.45 |

Three things read off cleanly:

1. \(\mathbb E[M]\to0.1804\), against the exact asymptote
   \(2-\tfrac{20}{11}=0.18182\) (which is where \(\rho_t/t\to1/2\) puts it).
2. \(\mathrm{sd}(M)\approx C/\sqrt n\), with \(C\) measured at
   \(0.98,0.86,0.66,0.85\) on successive windows; take the **conservative**
   \(C=0.982\).
3. The realised extremal deviation \((\mu-\min)/\mathrm{sd}\) is \(1.6\)–\(2.8\),
   i.e. *inside* the Gaussian extremal scale \(\sqrt{2\ln N}=2.6\)–\(3.4\). The
   minimum is not anomalous.

> **Calibration (measurement, not a theorem).** The lower envelope
> \[
> M(n)\ \ge\ 0.18182-C\sqrt{2\ln n}\,/\sqrt n,
> \qquad C=0.982,
> \]
> holds in every dyadic window tested, conservatively (observed minima sit
> \(0.05\)–\(0.37\) above it). The envelope **crosses zero at \(n\approx341\)**.

**Prediction.** No violation of the \(6n\) cut for odd \(n>341$; the only
observed violations are \(n=5,11\), both far inside. Safety grows like
\(\sqrt n\), so the cut becomes *more* secure with \(n\), and the entire risk
is concentrated in \(n\lesssim341\) — a range already exhaustively checked.

**Falsifier.** Any odd \(n>341\) violating the \(6n\) cut refutes this
calibration outright; any odd \(n>23\) violating it would already be a
surprise. Both are cheap to search for and neither has been found through
\(1781\).

**What this does and does not buy.** It converts "checked to \(1781\)" into a
statement with a stated envelope and a place to look. It is *not* a proof:
the underlying single-orbit concentration is exactly the object §3 says
worst-case tooling cannot reach. Its value is triage — it says extending the
census further is not where the risk is.

---

## 5. The window parameter \(c\): a wrong recommendation and the bound that kills it

**Read §5.3 first if short on time.** §5–§5.2 develop a proposal to re-base
the Avenue A cut from \(t=6n\) to \(t=15n\); §5.3 refutes it and extracts the
part worth keeping. The intermediate results are correct as stated and are
retained because the refutation depends on them.

Both cuts in §4 are instances of a one-parameter family. Write \(t=cn\).

**Validity of the cut.** A survivor through the window has
\(a_n3^{\rho_t}2^{-t}\gtrsim2^n\), i.e.

\[
\rho_t\ \ge\ \frac{t+1-(\log_23-1)n}{\log_23}.
\]

The score caps \(\rho_t\le\tfrac{11}{20}t\). The two are contradictory — so
"\(\rho_t\le\tfrac{11}{20}t\)" implies \(K_\downarrow\le H\le t\) — exactly when

\[
\frac{c-0.58496}{1.58496}>\frac{11}{20}c
\iff
\boxed{\ c>4.5605\ }.
\]

So **every** \(c>4.5605\) is a valid cut. The note uses \(c=5\) and \(c=6\):
the two smallest usable values, i.e. the tightest end of the family, where the
conclusion is strongest and the margin is smallest. That is precisely where
finite misses appear.

**Measured minimum margin \(t/\rho_t-20/11\), odd \(5\le n\le401\).**

| \(c\) | min margin | argmin | min over \(n\ge25\) | exceptions |
|---|---|---|---|---|
| 6 | \(-0.454545\) | 5 | \(+0.0032\) (\(n=17\)) | 5, 11 |
| 10 | \(-0.151515\) | 5 | \(+0.052566\) | 5 |
| 13 | \(-0.012626\) | 5 | \(+0.071353\) | 5 |
| **15** | \(+0.011086\) | 5 | \(+0.085371\) | **none** |
| 18 | \(+0.018553\) | 5 | \(+0.104895\) | none |
| 20 | \(+0.033670\) | 5 | \(+0.112320\) | none |

> **Finite certificate (WIDE-15, \(5\le n\le601\) odd).** For every odd
> \(5\le n\le601\), the window \(t=15n\) satisfies \(t/\rho_t\ge20/11\) with
> strictly positive margin. **No exceptions at all** — including \(n=5,11,17,23\).
> Tightest: \(n=5\) at \(+0.011086\). Median margin \(+0.181020\).

**This certificate is true and useless. §5.3 explains why.** It is retained
because the reason is the substantive finding of this section.

### 5.1 BAKEX2 transfers: the constant is essentially free (checked)

BAKEX2 (W9 §3.2) is the one consumer that cites \(6n\) specifically: the
Avenue A \(L=1\) gates hold "for every odd \(n\ge161\) under
\(K_\downarrow(n)\le6n\)". Rerunning W9-B's own argument with \(c\) in place
of \(6\) — \(q=i+B\le(c+2)n\), so \((\log2)\|q\theta\|\ge(2.085(c+2)n)^{-13.3}\)
by (R), against \((\log2)\Delta\le A(c)\,n/2^{-n}\) with
\(A(c)=\lceil c/3+O(1)\rceil\) — gives the crossover \(N_0(c)\) as the least
\(n\) with \(2^n>A(c)\,n\,(2.085(c+2)n)^{13.3}\):

| \(c\) | \(A(c)\) | \(2.085(c+2)\) | \(N_0(c)\) | inside W9-A's certified \(n\le501\)? |
|---|---|---|---|---|
| **6** | **3** | **16.680** | **161** | yes — *reproduces W9 exactly* |
| 10 | 4 | 25.020 | 170 | yes |
| **15** | **6** | **35.445** | **178** | **yes** |
| 20 | 7 | 45.870 | 184 | yes |
| 30 | 11 | 66.720 | 193 | yes |
| 50 | 17 | 108.420 | 204 | yes |

The \(c=6\) row returns \(A=3\), \(k=16.68\) and \(N_0=161\) — W9's published
numbers — which is the check that the reparametrization is faithful.

> **Answer.** BAKEX2 holds under \(K_\downarrow\le15n\) with crossover
> \(n\ge178\) instead of \(n\ge161\). The seventeen values \(161\le n\le177\)
> are already covered by W9-A's finite certificate (odd \(7\le n\le501\)), so
> **nothing is left over** — exactly the situation W9 engineered for \(6n\).

The crossover grows only logarithmically:

\[
N_0(c)\ \approx\ 161+14.3\log_2(c/6)
\]

(\(14.3=1+13.3\), the Rhin exponent plus one), which predicts \(204.8\) at
\(c=50\) against the computed \(204\). **The choice of \(6n\) was never forced
by the Baker side.** Any \(c\) up to at least \(50\) leaves the crossover deep
inside the certified range. Taking \(c=15\) costs nothing and buys the margin
in the table above.

### 5.2 The exact envelope at \(c=15\) (proved, uniform)

\(c>4.5605\) was a leading-order computation; SD-K-density-6 is stated in the
parent note as an *exact envelope* including affine corrections. Here is the
\(c=15\) analogue, uniform in \(n\) and certified by one integer inequality.

> **Lemma SD-K-density-15.** Fix odd \(n\ge7\) and \(t=15n\). If the
> \(a_n\)-tail stays \(\ge T=2^n-1\) throughout its first \(t\) shortcut steps
> and \(\rho\) is the number of odd \(U\)-steps in that prefix, then
> \[
> \rho\le\Bigl\lfloor\frac{33n}{4}\Bigr\rfloor
> \quad\Longrightarrow\quad
> \frac{U^{t}(a_n)}{T}<1,
> \]
> contradicting survival. Hence every full-window-\(15n\) survivor satisfies
> \(\rho>\lfloor33n/4\rfloor\).

(The cap is the score cap: \(\lfloor\tfrac{11}{20}\cdot15n\rfloor=\lfloor33n/4\rfloor\).)

*Proof.* While the tail stays above \(T\),
\[
\frac{U^{t}(a_n)}{T}
\le
\frac{a_n}{T}\cdot\frac{3^{\rho}}{2^{t}}\cdot\Bigl(1+\frac1{3T}\Bigr)^{\rho}.
\]

- \(2^n-1\ge\tfrac{127}{128}2^n\) for \(n\ge7\), so \(a_n/T<\tfrac{64}{127}(3/2)^n\).
- \(\rho\le33n/4\), so \(3^{\rho}/2^{t}\le3^{33n/4}/2^{15n}\).
- \((1+x)^{\rho}\le e^{\rho x}\le1/(1-\rho x)\) for \(0\le\rho x<1\), with
  \(x=1/(3T)\). Now \(\rho/(3T)\le\tfrac{33n}{4}/(3(2^n-1))\) is decreasing in
  \(n\) for \(n\ge7\) and equals \(57/381\) there, so the correction is at most
  \(381/324\).
- Since \(381=3\cdot127\), one has \(\tfrac{64}{127}\cdot\tfrac{381}{324}=\tfrac{16}{27}\) **exactly**.

Therefore
\[
\frac{U^{t}(a_n)}{T}
\ <\
\frac{16}{27}\,\lambda^{n},
\qquad
\lambda=\frac{3^{1+33/4}}{2^{16}}=\frac{3^{37/4}}{2^{16}}.
\]
The single integer inequality
\[
3^{37}=450\,283\,905\,890\,997\,363
\;<\;
18\,446\,744\,073\,709\,551\,616=2^{64}
\]
(a factor \(40.97\) of room) gives \(\lambda<0.396<1\). The bound is therefore
decreasing in \(n\), and at \(n=7\) it is already \(8.94\times10^{-4}<1\). \(\square\)

This is the exact analogue of the parent note's "\(3^{43/10}<127\)" step at
\(c=6\), and it has vastly more room: the \(c=6\) envelope's worst value is
\(0.196\) at \(n=7\), the \(c=15\) envelope's is \(3.92\times10^{-4}\).

**Corollaries.** *SD-K-nc15-implies:* if \(\rho_{15n}(n)\le\lfloor33n/4\rfloor\)
then \(H(n)\le15n\). *Gap SD-K-nc-15:* for every odd \(n\ge5\),
\(\rho_{15n}(n)\le\lfloor33n/4\rfloor\).

Everything above is correct. §5.3 shows the last line is the wrong thing to
want.

---

### 5.3 The window is bounded **above** too — WIDE-15 retracted

The cap \(\rho_t\le\tfrac{11}{20}t\) is not a free numerical constraint: it
*asserts a descent depth*. The correct direction is a contrapositive, so state
it that way.

Along any shortcut prefix, \(x_t\ge x_03^{\rho}2^{-t}\) unconditionally (the
\(+1\) in \(3x+1\) only adds), and \(x_t\le x_03^{\rho}2^{-t}(1+1/(3B))^{\rho}\)
whenever the prefix stays above a level \(B\). Suppose the orbit stays in the
multiplicative regime — say above \(B=2^{\sqrt n}\), so the correction is
\(1+o(1)\) — throughout the window. Then with \(x_0=a_n\) and \(t=cn\),

\[
\rho_t\le\tfrac{11}{20}t
\quad\Longrightarrow\quad
\log_2x_t\ \le\ n\bigl(\log_23-(1-\tfrac{11}{20}\log_23)\,c\bigr)+o(n),
\qquad
1-\tfrac{11}{20}\log_23=0.12827.
\]

If the right-hand side is negative, this contradicts \(x_t\ge1\). **Hence for
such \(c\) the cap can hold only if the orbit leaves the multiplicative regime
inside the window** — i.e. only if \(a_n\) descends to \(O(1)\). No claim is
made about the correction factor after descent; none is needed, because the
argument is a contrapositive against the orbit *staying* large.

So the cap at window \(cn\) demands descent to \(2^{(1.58496-0.12827c)n}\):

| \(c\) | required \(\log_2x_t\) | what the cap actually asserts |
|---|---|---|
| 4.5605 | \(+1.000\,n\) | exactly "below \(M_n\)" — the validity threshold |
| 5 | \(+0.944\,n\) | below \(M_n\), slightly |
| **6** | \(+0.815\,n\) | below \(M_n\) with room |
| 7 | \(+0.687\,n\) | deeper |
| 10 | \(+0.302\,n\) | much deeper |
| **12.3565** | \(0\) | **descent to \(O(1)\) — Collatz for \(a_n\)** |
| 15 | \(-0.339\,n\) | impossible multiplicatively |

> **Two-sided bound (proved).** The window \(t=cn\) is a usable cut only for
> \(4.5605<c<12.3565\). Below, the cap is weaker than descent below \(M_n\)
> and the contradiction fails. **Above, the cap asserts descent to the
> affine-dominated regime — i.e. the Collatz conjecture for \(a_n\)** — so
> proving it is harder than the conclusion it buys.

At \(c=15\) the model requires \(x_t<1\), which is impossible; the inequality
is nonetheless *true* for the measured orbits, purely because they have
already reached the \(1\to2\to1\) cycle, where density is exactly \(1/2\) and
the multiplicative model no longer applies.

**The measurement confirms it.** With \(\sigma_1(n)\) the shortcut steps for
\(a_n\) to reach \(1\):

| \(n\) | \(6n\) | \(15n\) | \(\sigma_1\) | \(\sigma_1<6n\)? | \(\sigma_1<15n\)? | \(\operatorname{bitlen}x_t\) at \(15n\) |
|---|---|---|---|---|---|---|
| 23 | 138 | 345 | 275 | no | yes | 1 |
| 101 | 606 | 1515 | 836 | no | yes | 2 |
| 201 | 1206 | 3015 | 1703 | no | yes | 1 |
| 301 | 1806 | 4515 | 2811 | no | yes | 1 |

In every case the \(15n\) window has swallowed the entire descent to \(1\) and
is sitting in the trivial cycle, while the \(6n\) window has not.
Empirically \(\sigma_1(n)\approx7.64\,n\) (the Terras constant
\(2/\log(4/3)\) times \(\ln a_n\)), so **for \(c\gtrsim7.6\) the measured
margin is borrowed from the trivial-cycle tail**, not from descent structure.
A proof strategy that only knows "the orbit eventually falls below \(M_n\)"
cannot use that margin.

**And the margin is not even monotone in \(c\).** Sampling only
\(c\in\{6,10,13,15,18,20\}\) produced the misleading impression that it grows.
Filling in the honest range:

| \(c\) | exceptions (odd \(5\le n\le301\)) | min margin over \(n\ge25\) |
|---|---|---|
| 5 | \(\{5,17,23\}\) | \(+0.003852\) |
| **6** | \(\{5,11\}\) | \(+0.029569\) |
| 7 | \(\{5,23\}\) | \(+0.004969\) |
| 8 | \(\{5,23,81\}\) | \(\mathbf{-0.008126}\) |
| 9 | \(\{5,25\}\) | \(\mathbf{-0.018182}\) |
| 10 | \(\{5,23\}\) | \(+0.020053\) |

\(c=8\) and \(c=9\) are strictly **worse** than \(c=6\), with new exceptions at
\(n=81\) and \(n=25\).

> **Conclusion. \(c=6\) is well-chosen, not arbitrary.** The usable band is
> \(4.56<c\lesssim7.6\); within it \(c=6\) has the best margin of any integer
> value. The earlier recommendation to re-base at \(c=15\) is **withdrawn**.
> §4's DISJ — a disjunction over the two *honest* windows \(5n-2\) and \(6n\) —
> is the surviving improvement, and it is already optimal: \(n=5\) lies in
> every exception set, so "no odd \(n\ge7\) fails both" cannot be bettered.

**What §5.1 is still worth.** It shows the Baker side tolerates any \(c\) up
to at least \(50\) at negligible cost. So the binding constraint on the window
is the **descent-depth** bound of this subsection, not the transcendence
input — which is the opposite of what one would guess, and is worth recording
so the question is not reopened.

---

## 6. Retracted: the PCD9/PCD10 route (refuted by its own falsifier F1)

**What was proposed.** RUNLEN2 makes valuation-one runs exactly \(2\)-adic
ghost distances; DBC1 makes those exact without transcendence input; PCD9
assigns each valuation word a unique odd exponent class \(\bmod\,2^{E}\);
PCD10 says a nested cylinder's least representative jumps by \(2^{E_m}\)
unless it plateaus. The hope: a mean-depressing itinerary of length
\(\Theta(n)\) forces a cylinder plateau of length \(\Theta(n)\), against
W13's calibrated \(\ell_{\max}(m)\approx1+0.1845\log_2m\).

**F1 (run, decisive).** Plateau lengths on the **actual** \(a_n\) towers,
where \(n_m=n\bmod2^{E_m}\) by PCD9:

| \(n\) | \(K_\downarrow\) | \(E_K\) | first \(m\) with \(n_m=n\) | longest plateau |
|---|---|---|---|---|
| 131 | 310 | 570 | 3 | 308 |
| 471 | 732 | 1436 | 6 | 727 |
| 1197 | 1635 | 3291 | 10 | 1626 |
| 2349 | 4026 | 7757 | 8 | 4019 |
| 4401 | 7308 | 14158 | 6 | 7303 |

The tower reaches \(n\) after \(O(\log n)\) extensions and is then constant for
the entire rest of the orbit: the plateau is \(K_\downarrow-O(\log n)\), i.e.
\(\Theta(n)\), not \(\Theta(\log n)\).

**Why the proposal was wrong.** PCD10's plateau bound constrains *which
exponents realize an adversarially prescribed word*. It says nothing about the
word an exponent actually produces: once \(2^{E_m}>n\), \(n\) is trivially the
least representative of its own class forever. Applying PCD10 to an orbit's
own itinerary is vacuous. This is `OPUS5_WIDE_RESULTS.md` §6's recurring
failure mode — **wrong reference object** — and the falsifier caught it in one
run, which is the point of writing falsifiers first.

**What this leaves.** Combining §2 and §3: the gap is a single-orbit
lower-deviation bound for the mean valuation, the enemy set is SD-K-thin's
high-odd-density class of density \(2^{-(0.036+o(1))n}\), and worst-case
tooling cannot see a thin set. The bad classes are cut out by the binary
digits of \(3^n\) in a window of length \(\Theta(n)\) — i.e. W11's
\(C=\lfloor3^n/2^{E+2}\rfloor\) and W10 §2's bridge. So Gap SD-K-block-8-17 is
**not an independent route**: it is `OPUS5_WIDE_RESULTS.md` §4's frontier
object in disguise, at a weaker exponent (a lossy factor \(\approx1.1\)
suffices, where the frontier statement is sharp).

---

## 7. Residual after this note

The open core is mathematically unchanged: Gap SD-K-nc-6 at *any* window is
still a single-orbit lower-deviation bound on the mean valuation, and §3 says
worst-case tooling cannot supply it. What changes is **which** instance to
attack and how much margin it carries.

**Task list.**

1. ~~Check BAKEX2's constant.~~ **Done (§5.1): it transfers, crossover
   \(178\), nothing left over.**
2. ~~Redo SD-K-density-6's exact envelope at general \(c\).~~ **Done (§5.2):
   Lemma SD-K-density-15, uniform for odd \(n\ge7\), certified by
   \(3^{37}<2^{64}\).**
3. ~~Adopt \(c=15\).~~ **Withdrawn (§5.3): the window is bounded above at
   \(c<12.3565\), and margin above \(c\approx7.6\) is borrowed from the
   trivial-cycle tail.** \(c=6\) stands.
4. ~~Extend DISJ past \(n=1501\).~~ **Done: holds through \(n=1781\),
   cross-checked against three values stated in the parent note.** Do *not*
   extend WIDE-15; it is retracted. **And do not extend the census further:**
   §4.1 calibrates the risk as confined to \(n\lesssim341\), with safety
   growing like \(\sqrt n\). More census is the cheapest thing to do here and
   the least informative.
5. **Human proof read of §4 (DISJ) and §5.3's two-sided bound**, the two
   items here that meet the admission rule's form. Neither has had a proof
   read, which the rule requires. §5.3's derivation is the one to read
   carefully — it is a contrapositive and the direction of the affine
   correction matters.
4. **Restate the Avenue A gap list at \(c=15\).** Gap SD-K-survivor-6,
   Gap SD-K-nc-6, Gap SD-K-911-6-strong, Gap SD-K-block-8, Gap SD-K-block-8-17
   and its sub-gaps are all the \(c=6\) instances of a family. At \(c=15\) the
   \(n\equiv17\pmod{64}\) concentration that motivated the whole
   `Thm SD-K-block-8-17-*` tower has margin \(+0.085\) rather than \(+0.003\),
   so the tower is no longer needed to reach a linear bound.
5. \(-\) **Remove.** Further mod-\(2^m\) refinement as a route to a *cover*
   (§3). Individual classes remain fair game; the scheme does not close.
6. \(-\) **Remove.** Any plateau/least-representative argument applied to an
   orbit's own itinerary (§6, F1).
7. \(=\) **Unchanged.** EC1-near, SD-L1 later landings, descent-to-\(1\) for
   \(P>0\) — independent of the score route.

**Record.** Gap SD-K-block-8-17 is the W10/W11 frontier object at a weaker
exponent, not an independent lane. Do not budget further sessions on it as if
it were separable. What §5 buys is not a proof of the gap but a much larger
safety margin in the instance one has to prove.

**Falsifiers still live.**

- **F3.** Exhibit odd \(n>23\) with mean valuation \(<20/11\) at \(t=5n-2\) or
  \(t=6n\). None through the ranges checked; window minima are rising.
- **F5.** Exhibit odd \(n\ge7\) failing **both** \(5n-2\) and \(6n\). None
  through \(n\le1501\). Refutes DISJ.
- **F6 (retired).** WIDE-15 is withdrawn (§5.3); its falsifier is moot. The
  replacement question is whether any \(c\) in the honest band
  \((4.56,\,7.6)\) beats \(c=6\). Through \(n\le301\) none does: \(c=7\) has
  min margin \(+0.0050\) and \(c=8,9\) go negative.
- **F7 (resolved, §5.1).** BAKEX2 survives \(K_\downarrow\le15n\) at crossover
  \(178\). The falsifier would be a misreading of W9-B's \(q\)-bound or of
  \(A(c)\); the \(c=6\) row reproducing \(161\) exactly is the guard against
  both. A genuine refutation would need Rhin's exponent \(13.3\) to be
  misquoted — which W9 §7 already flags as its own falsifier.
