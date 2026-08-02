# Avenue A — the mean-valuation reformulation, and why the mod-\(2^m\) bash cannot close

**Status:** Working note. Nothing here is a claim-ledger promotion. Contains
one **proved reformulation** (§2), one **mechanical no-go for the current
method** (§3), and one **proposed route** (§5) with an explicit falsifier.

**Parent:** [`avenue_a_comparison_dynamics.md`](avenue_a_comparison_dynamics.md)
§13 Gap SD-K-block-8-17 / Gap SD-K-res-dens-17 / Gap SD-K-911-6-strong.

**Reproducer:** `python3 scripts/explore_mean_valuation_gap.py`

---

## 1. Applicability predicate

Odd \(n\ge3\); \(a_n=(3^n-1)/2\); \(x_{i+1}=f(x_i)\); \(e_i=v_2(3x_i+1)\);
\(K=K_\downarrow(n)\) the first index with \(x_K<M_n=2^n-1\);
\(E_K=\sum_{i<K}e_i\). All statements are about the pre-descent window only.

**Logical role.** §2 is a restatement (no new content, sharper coordinates).
§3 is a **method no-go**: it deletes an approach, not a residual. §5 is a
tool request with a named dependency.

---

## 2. The gap is exactly a mean-valuation statement (proved)

Avenue A's score is \(\mathrm{rest}=11E-9O\) on the shortcut window, with
\(O=\rho\) the odd-step count and \(E=\sum(e_i-1)\) the *surplus* halvings.
Substituting \(E=E_K-K\), \(O=K\), \(L=E+O=E_K\):

\[
\mathrm{rest}\ge0
\iff
11(E_K-K)\ge9K
\iff
\boxed{\ \frac{E_K}{K_\downarrow}\ \ge\ \frac{20}{11}=1.8181\ldots\ }
\]

> **Reformulation (proved).** Gap SD-K-block-8-17 — equivalently
> Gap SD-K-res-dens-17 (\(O/L\le11/20\)), equivalently Gap SD-K-911-6-strong
> up to the seed bookkeeping — is precisely the statement that the **mean
> valuation of the \(a_n\) orbit before first descent is at least \(20/11\)**.

This is worth having because \(20/11\) is a threshold on a quantity whose
unconditional expectation is \(2\) (geometric \(e\), \(P(e=k)=2^{-k}\)). The
gap therefore asks for a **constant-size lower deviation** — \(0.18\) below
the mean, sustained over \(K\asymp1.5n\) steps — to be impossible for one
deterministic orbit.

**Consistency check (exact, \(n\le2001\)).** The complete list of odd \(n\)
with \(E_K/K<20/11\) is

\[
n\in\{5,\,17,\,23\},
\]

which is exactly the repository's known exceptional set: \(n=17\) is the
equality case of Gap SD-K-block-8-17, \(n=23\) is the \(5n-2\) even-budget
saturation and the unique 911 miss, \(n=5\) is the one seed handled directly.
The 911-6-strong miss \(n=11\) sits at \(1.8400\), just above. Nothing else in
range comes close. This agreement across four independently-derived
exceptional cases is the evidence that \(E_K/K\) is the right invariant.

**Window minima (measured, \(n\le6001\)).**

| \(n\) window | \(\min E_K/K\) | argmin | margin over \(20/11\) |
|---|---|---|---|
| \([16,32)\) | 1.804348 | 17 | \(-0.0138\) |
| \([32,64)\) | 1.870588 | 43 | \(+0.0524\) |
| \([128,256)\) | 1.838710 | 131 | \(+0.0205\) |
| \([512,1024)\) | 1.933808 | 837 | \(+0.1156\) |
| \([1024,2048)\) | 1.943882 | 1335 | \(+0.1257\) |
| \([2048,4096)\) | 1.926726 | 2349 | \(+0.1085\) |
| \([4096,6001)\) | 1.937329 | 4401 | \(+0.1191\) |

The window minimum **increases** and settles near \(1.93\). This is the
signature of concentration: the deviation needed is a constant \(0.18\) while
the fluctuation scale is \(O(\sqrt{\log n/n})\). The gap is not marginal
asymptotically; it is marginal only at \(n\le23\), which is why the finite
certificates saturate exactly there.

---

## 3. Method no-go: no modulus closes the case bash (mechanical)

`avenue_a_comparison_dynamics.md` §14 item 1 proposes continuing the
refinement \(k \bmod 2^{13}\to2^{14}\to\cdots\) on \(n=64k+17\). The
following says that programme has no terminating condition.

Model the pre-descent orbit as a walk on the **block automaton**: states are
odd residues \(x\bmod2^m\) with \(h(x)=v_2(x+1)=1\); one edge per block
(payout \(e\ge2\), landing of height \(h\), then \(h-1\) rails, using
Lemma SD-K-rail-closed); edge weight \(\Delta=11(e-1)-9h\). Every real
itinerary is a walk in this graph, so

\[
\liminf_{\text{orbit}}\ \overline{\Delta}
\ \ge\
\min_{\text{cycles }C}\ \frac{\Delta(C)}{|C|}.
\]

A **positive** minimum mean cycle would give \(\mathrm{rest}\ge-O(1)\)
uniformly in \(n\) and close the gap at a single stroke — this is the
max-plus dual of the Bellman–Ford negative-cycle machinery already used for
QLG1/WITN1, run for a lower bound instead of a certificate. It has never been
computed here. It is:

| \(m\) | states | edges | min mean cycle of \(\Delta\) |
|---|---|---|---|
| 6 | 16 | 176 | \(-106\) |
| 8 | 64 | 1408 | \(-106\) |
| 10 | 256 | 9472 | \(-106\) |
| 12 | 1024 | 57344 | \(-106\) |

The value is \(-106=11-9\cdot13\), i.e. a single self-loop at the deepest
landing the enumeration allows (\(h=13\)); it therefore diverges to
\(-\infty\) as the lift depth grows, and it is **independent of \(m\)**.
Restricting landings to \(h\le h_{\max}\) gives \(-7,-16,-25,-34,-43,-61\)
for \(h_{\max}=2,3,4,5,6,8\) — again identical at \(m=8\) and \(m=10\).

> **Method no-go (mechanical).** For every \(m\) the block automaton
> \(\bmod\,2^m\) contains cycles of arbitrarily negative mean \(\Delta\).
> Hence **no argument whose only input is "the block outcome is determined by
> \(x\bmod2^m\)" can prove \(\mathrm{rest}\ge0\)**, at any \(m\). Refining the
> modulus enlarges the state space but never removes the bad cycles.

**Where the bad cycle lives.** The \(h_{\max}=2\) value \(-7=11-18\) is
attained on a cycle whose \(2\)-adic fixed point solves
\(x+1=3\bigl((3x+1)/4+1\bigr)/2\), i.e. \(x=-7\). That is the repository's own
ghost — REPLOW3's \(\alpha\) with \(3^{\alpha+1}=-7\). Excising the ball
\(v_2(x+7)\ge D\) does **not** repair the min mean cycle (it moves to
\(-68\), then \(-88\)): the \(-7\) ghost is one bad cycle among many, and
deep-landing self-loops are dense in the state space.

**Consequence for §14.** Item 1 (mod-\(16384\) on
\(1803,5899,6923,7947\bmod8192\); block-9 on \(2315,2827\bmod8192\)) closes
individual classes but cannot close the class *scheme*. The eight
already-proved `Thm SD-K-block-8-17-*` rows are genuine, and the
density-\(9/1024\) corollary is genuine; they are simply not extendable to a
cover by more of the same. This is consistent with, and is the Avenue A
instance of, SH1: \(\Delta\) is a potential in local coordinates, and SH1 says
no such potential is nonincreasing.

---

## 4. What the reformulation says the obstruction actually is

Combining §2 and §3: the gap is a **single-orbit lower-deviation bound** for
\(E_K/K\), and the enemy set is exactly SD-K-thin's high-odd-density class, of
density \(2^{-(0.036+o(1))n}\). Worst-case tooling cannot see a thin set; that
is the whole content of §3.

This identifies Gap SD-K-block-8-17 with `OPUS5_WIDE_RESULTS.md` §4's frontier
object (single-orbit equidistribution of a deterministic sequence built from
powers of \(3\)) — **but at a far weaker exponent**. The frontier object as
stated there wants a sharp local digit theorem. Here any bound that keeps the
mean above \(20/11\) suffices, and the truth sits at \(2\). The needed input
is lossy by a factor \(\approx1.1\), not sharp.

---

## 5. Proposed route: realizability instead of equidistribution

The repository owns an arithmetic substitute for the missing equidistribution.

1. **RUNLEN1/RUNLEN2.** Only valuation-one runs depress \(E_K/K\), and a
   maximal run from step \(K_0\) has length **exactly**
   \(v_2(3^{m_{K_0}}+d_{K_0})-E_{K_0}-2\).
2. **DBC1** (W10 §1, proposed row). \(v_2(3^m-A)=2+v_2(m-\alpha_A)\). So run
   lengths are exactly \(2\)-adic distances from \(m_K\) to ghosts
   \(\alpha_{d}\) — no transcendence input, and W9 §4.2 gives the true finite
   envelope (max \(17\), at \(n=1197\), through \(n\le50001\)) where the
   Baker bound gave \(30\log_2(n+1)+10\).
3. **BAKERC1.** The enemy coordinate \((m_K,d_K)\) is invariant across a run,
   hence distinct runs carry distinct coordinates.
4. **PCD9 + PCD10.** A valuation word of total valuation \(E\) is realized by
   exactly one odd class \(\bmod\,2^E\); and along a nested cylinder tower
   every change of least representative costs \(n_{m+1}\ge2^{E_m}\).

**Target lemma (GVB, ghost-visit budget).** Depressing \(E_K/K\) to \(20/11\)
over \(K\asymp1.5n\) steps requires total valuation-one-run length
\(\ge\tfrac2{11}K+O(1)\), i.e. \(\Theta(n)\) accumulated ghost-approach depth.
By (2) each single approach contributes \(O(\log n)\), so \(\Theta(n/\log n)\)
**independent** approaches are needed, with distinct enemy coordinates by (3).
By (4) the resulting nested cylinder pins \(n\) as the least representative of
a class \(\bmod\,2^{\Theta(n)}\) through \(\Theta(n)\) extensions — i.e. it
forces a cylinder plateau of length \(\Theta(n)\), against W13's calibrated
law \(\ell_{\max}(m)\approx1+0.1845\log_2m\).

**Why this is the right shape.** It never asks for equidistribution. It asks
for an *upper bound on plateau length*, and any bound of the form
\(\ell_{\max}=o(n)\) suffices — the calibrated truth is \(\Theta(\log n)\), so
the route has a full exponential of slack. This is also the softest possible
form of W10 §2's bridge, which is already built to receive exactly such a
bound.

**Falsifiers, in the order they should be checked.**

- **F1 (cheapest, decisive).** Measure plateau lengths for the *actual*
  \(a_n\) cylinder towers, not only the balanced \(q=3\) family PCD10 is
  stated for. If plateaus on real towers are not \(O(\log)\), the route dies
  immediately.
- **F2.** PCD10's own candidate universal bound \(L=2\) already fails at
  \(m=1198,1199,1200\). GVB needs only \(o(n)\), so that failure is survivable
  — but the generalization from balanced cylinders to arbitrary itinerary
  cylinders is unproved and is the real work item. Do not assume it.
- **F3.** Exhibit an odd \(n>23\) with \(E_K/K<20/11\). None exists through
  \(n\le6001\) and the window minima are rising; such an \(n\) would refute
  Gap SD-K-block-8-17 outright and retire the whole sub-programme.
- **F4.** W13's forward prediction — no PCD-length-4 plateau below
  \(m\approx2\times10^4\) — is cheap and, if violated, invalidates the
  calibration the route leans on.

---

## 6. Residual after this note

Unchanged mathematically. What changes is the **task list**:

- \(-\) Remove: further mod-\(2^m\) refinement as a route to a *cover*
  (§3). Individual classes remain fair game; the scheme does not close.
- \(+\) Add: F1, the plateau measurement on real \(a_n\) towers.
- \(+\) Add: GVB as a stated target with dependencies PCD9, PCD10, RUNLEN2,
  DBC1, BAKERC1, W13.
- \(=\) Unchanged: EC1-near, SD-L1 later landings, descent-to-\(1\) for
  \(P>0\). These are independent of the score route.

If GVB closes, the chain is
GVB \(\Rightarrow\) Gap SD-K-block-8-17 \(\Rightarrow\) 911-6-strong
\(\Rightarrow\) survivor-6 \(\Rightarrow\) \(K_\downarrow\le6n\)
\(\Rightarrow\) (BAKEX2, W9 §3.2) the Avenue A \(L=1\) gates unconditionally
\(\Rightarrow\) (with EC1 and landing \(\ge3\)) SD1, then ST1.
