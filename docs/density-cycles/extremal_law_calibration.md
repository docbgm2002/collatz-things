# Calibration of the extremal laws  [W13]

**Task:** `OPUS5_WIDE_TASKS.md` W13 (session 8; scoped as half a session,
"low as mathematics, high as navigation").
**Building on:** `corridor_rate.md` (COR1–COR3),
`../repunit/payout_concentration_diffusion.md` (PCD2, PCD7, PCD10),
`../repunit/rotation_cocycle_rigidity.md` (W11, for \(\bar\delta\)).
**Script:** `scripts/explore_extremal_law_calibration.py`.
**Status:** **Exploratory — navigation only.** Nothing here eliminates a
cylinder, bounds anything, or is eligible for the ledger as mathematics.
Barrier 2 applies in full. Its purpose is to stop exact lemmas being
attempted with the wrong target exponent.
**License:** CC-BY 4.0

---

## 0. Summary

Two extremal statistics are calibrated, and W13's own suggested law family
turns out to be the wrong one for the first of them.

| statistic | correct law | constant | W13's guess |
|---|---|---|---|
| record deficit \(\max_K D_K\) | Cramér–Lundberg tail \(P(>u)\propto2^{-u}\) | \(\gamma=\log2\) **exactly** | Bramson \(-\tfrac{3}{2\theta}\log K\) — wrong family |
| plateau records | \(\ell_{\max}(m)\approx1+\log_2(m)/\bar\delta\) | \(1/\bar\delta=0.1845\) | "\(O(\log m)\) or \(O(\log m\log\log m)\)?" — it is \(\Theta(\log m)\) |

Both constants are *forced*, not fitted: \(\gamma=\log2\) is the exact root
of the Lundberg equation and is equivalent to the repo's own budget identity;
\(\bar\delta=5+\beta\) comes from W11's balancedness computation.

---

## 1. Why Bramson is the wrong family

W13 proposes that the record-deficit extremes are "the leftmost-particle
statistics of an (inhomogeneous) branching random walk", to be fitted with
Biggins' speed and Bramson's \(-\tfrac{3}{2\theta^\ast}\log K\) correction.

That describes the extreme of \(b^{K}\) particles **at a common depth \(K\)**
of one branching tree. The record deficit is a different object: it is

\[
\max_K D_K,\qquad D_K=K\log_23-E_K,
\]

the **excursion height** of a single orbit above its own starting value
(\(x_K\ge x_0\,2^{D_K}\)), maximised over *independent starting exponents*
\(n\). There is no common depth and no branching: the sample is one walk per
\(n\). The correct family is therefore Cramér–Lundberg (ruin theory), whose
answer is a pure exponential tail with no logarithmic correction at all.

---

## 2. The record deficit: \(\gamma=\log2\), exactly

Under the standard valuation model \(P(e=k)=2^{-k}\) \((k\ge1)\) the
increment is \(X=\log_23-e\) with \(\mathbb E[X]=\log_2 3-2<0\). The
Lundberg exponent solves \(\mathbb E[e^{\gamma X}]=1\); writing
\(z=e^{-\gamma}\),

\[
\mathbb E[e^{\gamma X}]=z^{-\log_23}\cdot\frac{z/2}{1-z/2}
=\frac{z^{\,1-\log_23}}{2-z}=1
\quad\Longleftrightarrow\quad
z^{\,1-\log_23}=2-z .
\]

Besides the trivial root \(z=1\), this has the exact root \(z=\tfrac12\):
\((\tfrac12)^{-0.58496\ldots}=2^{0.58496\ldots}=\tfrac32=2-\tfrac12\). Hence

\[
\boxed{\;\gamma=\log2,\qquad P\bigl(\max_K D_K>u\bigr)\;\asymp\;2^{-u}.\;}
\]

**This is not a coincidence of the model.** The set of valuation words with
\(D_K\ge u\) has density \(2^{-u}\), directly from PCD7's budget identity
\(D_K+Q_K=K\log_2(3/2)\) with \(Q_K\ge0\). The Lundberg tail *is* the
density of the corresponding cylinder. The exponent is forced by the ledger.

### 2.1 Measured

Peak deficits over all odd \(n\le2001\) (1000 orbits, computed to first
descent with exact integer comparisons \(3^{K}2^{E_J}>3^{J}2^{E_K}\)):

| \(u\) | \(\#\{\max D>u\}\) | \(\log_2\) fraction | step slope |
|---:|---:|---:|---:|
| 0 | 428 | −1.224 | |
| 1 | 207 | −2.272 | −1.048 |
| 2 | 104 | −3.265 | −0.993 |
| 3 | 52 | −4.265 | −1.000 |
| 4 | 26 | −5.265 | −1.000 |
| 5 | 10 | −6.644 | thin |
| 6 | 5 | −7.644 | thin |

Slope over the populated range (\(u=0\ldots4\), counts \(\ge20\)):
\(-1.0103\). The survival counts halve, exactly as \(2^{-u}\) requires.

The record is \(9.284\) at \(n=1197\), against \(\log_2 1000=9.966\) — inside
one bit, as an exponential tail predicts. (The single record is a noisy
order statistic and is *not* what confirms the exponent; the tail slope is.)

### 2.2 What this tells a rank function

Avenue F, or any exact rank, must tolerate a deficit that grows like
\(\log_2\) of the **number of exponents considered** — about 11 bits at
\(n\le5001\), about 21 bits at \(n\le10^{6}\). So:

- a rank designed for a **constant** deficit bound is under-specified and
  will fail on the first record beyond its range;
- a rank designed for a bound **linear in \(K\)** is over-engineered by an
  exponential factor and will be far harder to prove than necessary.

The honest target is \(O(\log(\text{sample size}))\), i.e. \(O(\log n)\) if
one ranges over exponents up to \(n\).

---

## 3. Plateau records: \(\Theta(\log m)\), constant \(0.1845\)

A PCD-length-\(\ell\) plateau is \(\ell-1\) consecutive zero exponent lifts,
which by PCD14 demands that \(\sum_{j<\ell}\delta_j\) prescribed bits match.
W11 fixes the cost per block:

\[
\bar\delta=5+\beta=2+\frac{2}{\log_2(3/2)}=5.419023\ldots
\]

Under a uniform heuristic the first occurrence of length \(\ell\) is near
\(m_\ell=2^{\bar\delta(\ell-1)}\) and the running maximum through \(m\) is

\[
\boxed{\;\ell_{\max}(m)\;\approx\;1+\frac{\log_2 m}{\bar\delta}
\;=\;1+0.1845\,\log_2 m .\;}
\]

Against the repository's certified census points:

| census point | observed | predicted \(\ell_{\max}\) |
|---|---:|---:|
| PCD10, \(m\le300\) | 2 | 2.52 |
| PCD10, \(m\le1500\) | 3 | 2.95 |
| W11 run, \(m\le8000\) | 3 | 3.39 |

and the first length-3 plateau is predicted near \(m=1831\) against the
observed \(m=1198\) — a factor \(1.5\).

### 3.1 Answer to W13's stated question

W13 asks "whether the honest target is \(O(\log m)\) or
\(O(\log m\cdot\log\log m)\) plateaus". **It is \(\Theta(\log m)\)**, with the
explicit constant \(1/\bar\delta=0.1845\). There is no \(\log\log\) factor:
the matching cost per block is constant, so the extreme-value calculation is
a plain geometric one.

The practical consequence is a warning in the other direction from the one
W13 anticipated. PCD10 asks for plateau lengths \(o(m)\). The truth is
\(\approx0.18\log_2 m\) — so **\(o(m)\) leaves an enormous margin**, and a
lemma proving merely \(o(m)\) is aiming far below the phenomenon, while a
lemma proving \(O(\log m)\) would be essentially optimal and is the right
thing to attempt.

### 3.2 Falsifiable forward predictions

For whoever extends the PCD census:

- first PCD-length-4 plateau near \(m\approx7.8\times10^{4}\);
- first PCD-length-5 plateau near \(m\approx3.4\times10^{6}\);
- **no length-4 plateau below \(m\approx2\times10^{4}\)** (a factor-4 safety
  margin below the prediction).

The last is the one to check first: it is cheap and it would falsify the
calibration outright if it failed. Note that PCD10 already refuted the
tempting extrapolation "\(L=2\) universally" at \(m=1200\); the calibration
above predicts exactly that refutation (\(\ell_{\max}(1200)=2.89\)) and is the
tool for not repeating the mistake at \(\ell=3\).

---

## 4. The \(n=471\) anchor

\(n=471\) has peak deficit \(D_K=4.229\) at \(K=38\), \(E_K=56\). Against a
predicted record of \(9.97\) over 1000 samples, it is a comfortably typical
large excursion, not an outlier.

PCD2 places all six blocked-diffuse records on this single tail at
\(K=31,33,34,35,37,38\) — consecutive positions inside one excursion whose
peak is at \(K=38\). The calibration says this is **one deep excursion**
sitting where the law expects a record to sit, not a distinct mechanism
requiring its own theory. That is worth stating plainly, because \(n=471\)
is used throughout the repo as *the* hard primitive and it would be easy to
over-read its diffuse records as structural.

---

## 5. Barrier check and scope

**Barrier 2 applies in full and is the whole point.** Every statement here is
distributional. Nothing eliminates a cylinder, nothing is promoted, and no
conclusion may be cited as evidence for or against any exact lemma. The
calibration's only legitimate uses are:

1. choosing the exponent to aim an exact lemma at;
2. recognising when a census result is exactly what chance predicts (§4) and
   therefore not evidence of structure;
3. generating cheap falsifiable predictions (§3.2).

The other three barriers are not engaged: no finite-state, Diophantine, or
virtual-source reasoning appears.

**Explicitly not claimed.** The valuation model \(P(e=k)=2^{-k}\) is a
heuristic; the orbits are neither independent nor identically distributed;
the repunit family is measure zero. The agreement in §2.1 is evidence that
the heuristic is *adequate for calibration*, not that it is true.

---

## 6. Falsifier

- **§2** is falsified by a measured tail slope differing from \(-1\) by more
  than a few percent over a well-populated range, or by the record deficit
  outgrowing \(\log_2 N\).
- **§3** is falsified by a length-4 plateau appearing below
  \(m\approx2\times10^{4}\), or by no length-4 plateau by
  \(m\approx3\times10^{5}\).
- **§1** (the claim that Bramson is the wrong family) is falsified by
  exhibiting a genuine common-depth branching structure whose leftmost
  particle is the record deficit — which would require the records to be
  taken across the survivor tree at fixed \(K\) rather than across exponents.

---

## 7. Reproduction

```bash
python3 scripts/explore_extremal_law_calibration.py              # n <= 2001
python3 scripts/explore_extremal_law_calibration.py --nmax 5001  # slower
```

Prints `EXTREMAL-CALIBRATION: consistent`. The peak-deficit comparisons are
exact integer inequalities; floats appear only in reporting the fitted slopes
and in the heuristic predictions, which are heuristics anyway.

---

## 8. Ledger

**No rows proposed.** This note is exploratory by construction and its
content is a prediction engine, not mathematics. It should be cited in
planning notes (the choice of target exponent for Avenue F, W10 and W11) and
nowhere in a proof chain.
