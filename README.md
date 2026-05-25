# Some notes on The Collatz Conjecture

**Some ideas**
First published: 28 November 2025 · Revised 2026
Author: Some Bloke Down the Pub (who happens to know docbgm, but is better than him at maths)

---

A structured, modern re-examination of the **3n+1 problem** using algebraic structure, parity dynamics, density analysis, and high-resolution computational experiments.

This repository contains a sequence of technical notes that build a coherent picture of *why* the Collatz map is so strongly biased toward collapse, and *why* non-trivial cycles and divergent trajectories appear to be structurally impossible — even though no complete proof yet exists.

All documents are designed to be:

- **mathematically clean**,
- **GitHub-renderable**,
- **modular**, and
- **non-overclaiming** (each states exactly what it proves).

> **2026 revision note.** Two things changed in this pass. First, the original "Algebraic Fracture" claim that a block of 1-bits is *annihilated* under $3n$ was **wrong**; it has been replaced by the exact **Block-Fracture Identity** ($3(2^L-1) = \texttt{10}\,1^{L-2}\,\texttt{01}$: the run contracts by two, it is not destroyed), with a full carry proof and a verifier. Second, a new exact note on **mod-8 rail descent** has been added. Every exact claim in the two new notes ships with a reproducible Python script and has been checked with zero exceptions.

---

# 📚 Document Overview

The notes split into two groups: **exact results** (theorems with proofs and verifiers) and **heuristic/structural arguments** (compelling but not proven). The 2026 revision sharpens this split.

## ⭐ Exact results (proved + machine-verified)

### A. Block-Fracture Identity  *(NEW / corrects the old Algebraic Fracture Lemma)*
📄 `Block_Fracture_Lemma.md` · 📄 `Block_Fracture_Lemma.pdf` · 🧪 `verify_block_fracture.py`

An exact, elementary description of what $\times 3$ does to a run of 1-bits:
- $3(2^L-1) = \texttt{10}\,1^{L-2}\,\texttt{01}$ — an isolated block of $L$ ones becomes a run of $L-2$ ones (it is **not** annihilated; weight is preserved at the multiply).
- A full **carry proof** (Lemma 2) shows the interior contraction is independent of surrounding bits.
- **Mersenne erosion:** one odd-step sends $2^L-1 \to \texttt{10}\,1^{L-1}$, so the leading run drops by exactly one.
- Stated limit: the *global* longest run is **not** bounded under $3x+1$ — the result is about isolated blocks only.

> Replaces the earlier `algebraic_fracture_proof.md`, whose "annihilation" claim was false.

### B. Mod-8 Rail Descent  *(NEW)*
📄 `Mod8_Rail_Descent.md` · 📄 `Mod8_Rail_Descent.pdf` · 🧪 `verify_mod8_rails.py`

Exact descent behaviour by residue class mod 8:
- $f(8y+1) = 6y+1$ (exact image; strict descent for $y \ge 1$).
- $f(8y+5) \le 3y+2 < 8y+5$ (immediate descent).
- $8y+3 \to 9y+4$ via an exact two-step affine bridge (holds for all integers).
- $8y+7$: a finite-escape recursion with cap $\lfloor v_2(y+1)/2 \rfloor$; the all-ones numbers $2^k-1$ are the unique uncapped class (handed off to the Block-Fracture note).
- **Machine-verified:** every odd $x \le 10^6$ descends within $\le 111$ odd-steps.
- Stated limit: the window-free (global) version is left open and is, in effect, equivalent to the conjecture.

> **Update: exact `8y+7` rail closed form**
> 
> The rail `8y+7` has an exact two-odd-step image:
> $$
> f_2(8y+7) = 18y+17.
> $$
> While it remains on rail 7, the index evolves by:
> $$
> y \mapsto \frac{9y+5}{4},
> $$
> so the exact number of consecutive rail-7 stays is:
> $$
> \left\lfloor \frac{v_2(y+1)}{2}\right\rfloor.
> $$
> A previous shorthand that rail 7 exits only to `8z+1` or `8z+5` should be read with care: the exact exit rails are `8z+1`, `8z+3`, and `8z+5`. In particular, for `y = 2^k - 1`, even $k$ exits to `8z+1`, while odd $k$ exits to `8z+3`.

### B2. Recharge No-Go & Tight Mersenne Burn Ledger  *(NEW)*
📄 `recharge_nogo.md` · 🧪 `verify_recharge_nogo.py`

Sharpens the failed potential of `potential_attack_notes.md` into two exact results:
- **No-Go (negative):** *no* potential $\log_2 x + g(v_2(x+1))$, for **any** $g$, can be a Collatz supermartingale — the burn forces $g$-slope $\ge\log_2\tfrac32$ while recharge onto $2^m-1$ allows slope $\to 0$; they collide already on $\tau\in[3,7]$.
- **Tight ledger:** the Mersenne burn $M_n=2^n-1$ has closed form $x_j=3^j2^{\,n-j}-1$, and the critical potential $\Phi=\log_2 x+\log_2\tfrac32\cdot\tau$ rises by $<\log_2\tfrac{10}{9}$ over the *entire* burn — so the fuel price is exactly $\log_2\tfrac32$.
- Stated limit: the post-escape descent below $x_0$ is the open residual and is **not** claimed.

### B2.5. Exponentially Decayed Bit Potential *(NEW / candidate)*
📄 `Exponential_Decay_Potential.md` · 🧪 `verify_exponential_potential.py`

A state-sensitive, uniformly bounded potential that makes the *recharge step* safe (which the $\tau$-only potential could not):
- **Exact:** the exponentially decayed bit weight $g_r(x) = \sum r^i b_i(x)$ is bounded by $1/(1-r)$ for all $x$, so on the recharge family $x_m\to2^m-1$ the potential strictly decreases (Theorem 1).
- **Empirical:** 0 epoch-descent failures over odd $x\le10^7$ (extended), worst margin $\approx-0.0085$.
- **Caveat (not a Lyapunov solution):** epoch descent here is driven by the bare $\log_2 x$ term — $x_{\text{end}}<x_0$ holds *by definition* of an epoch, and smaller $c$ only makes the margin more negative, so $g_r$ erodes rather than powers it. This does **not** bypass the global/per-step obstruction (a burn step raises $\log_2x$ by $0.585$, far above the $\le0.25$ the bounded fuel term can move). Global descent remains open.


### B3. Mersenne–Repunit Reduction  *(NEW)*
📄 `mersenne_repunit_reduction.md` · 🧪 `verify_repunit_reduction.py`

Solves the first $n$ steps of the worst case and reduces the rest to one question:
- **Exact:** for odd $n$, $f^{(n)}(2^n-1)=\frac{3^n-1}{2}=a_n$, the **base-3 repunit**, reached in exactly $n$ steps (even $n$ divides further to $a_n/2^{1+v_2(n)}$); the repunits ladder via $3a_m+1=a_{m+1}$.
- **Exact reduction:** $\operatorname{epoch}(2^n-1)=n+\sigma(a_n)$ — all remaining difficulty is the first passage of $a_n$ below $2^n-1$.
- **Empirical (not proved):** that residual descent is statistically *generic* ($v_2$ law $\approx2^{-k}$, mean $\approx2$, orbits routinely exceed the burn peak), so the spine offers no shortcut — Conjecture G is the general difficulty in disguise.

### B4. Explicit Stopping-Time Density  *(NEW)*
📄 `stopping_time_density.md` · 🧪 `verify_stopping_density.py`

An elementary, machine-checked re-derivation of Terras (1976) / Everett (1977), **with an explicit rate**:
- **Exact:** the density of odd $x$ with stopping time $\le K$ satisfies $D(K)\ge 1-\rho^K$, $\rho=e^{-I(\log_2 3)}=0.9465\ldots$ — so almost every integer descends below itself in boundedly many steps.
- Built from three exact pieces: affine accumulation $x_K=(3^Kx+c_K)/2^{E_K}$ with $c_K/2^{E_K}<(3/2)^K$; a descent criterion (*enough division $\Rightarrow$ descent*); and the exact equidistribution of $2$-adic valuations (each weight-$E$ pattern has density $2^{-E}$).
- Supersedes the density goal of `verify_descent_tree.py` (whose proven fraction was non-monotone) with a monotone bound.
- Stated limit: density $1$ is not *all*; the residual hard core (density $\le\rho^K$, dominated by the near-Mersenne spine) is exactly the conjecture and is **not** closed.
- **Unifying rate:** B4 proves almost everyone descends at rate $1-\rho^K$; B6 identifies the surviving $\rho^K$ hard core, anchored by the all-ones spine $2^K-1$.

### B5. Repunit Tail Attack  *(NEW / proof target)*
📄 `repunit_tail_attack.md` · 🧪 `explore_repunit_tail.py`

Turns the Mersenne reduction and stopping-density theorem into a narrow attack:
- **Exact:** the first post-repunit valuation is $v_2(3a_n+1)=1+v_2(n+1)$ for odd $n$.
- **Exact ledger:** the remaining question is whether the cumulative valuation sum along $a_n$ crosses the line $K\log_2 3+\log_2(a_n/(2^n-1))$ soon enough.
- **Normal-form lever:** $x_i=(3^{n+i}+A_i)/2^{E_i+1}$ with $A_{i+1}=3A_i+2^{E_i+1}$, so future payouts become explicit 2-adic congruences.
- **Target lemma:** prove $\sigma_n\le Cn$ for odd $n$, where $\sigma_n=\min\{K:f^K(a_n)<2^n-1\}$; empirically $C=3$ works for odd $n=7..2001$.
- Stated limit: this is a proposed lemma, not a proof; the missing ingredient is a non-concentration result for $a_n=(3^n-1)/2$ against the low-valuation residue classes.

Follow-up exploratory notes:
- 📄 `repunit_bad_automaton_notes.md` · 🧪 `explore_repunit_bad_automaton.py` — shows that naive bad residue classes still intersect the repunit curve, so a one-shot forbidden-residue proof is too weak.
- 📄 `repunit_normal_form_notes.md` · 🧪 `explore_repunit_normal_form.py` — gives the exact form $x_i=(3^{n+i}+A_i)/2^{E_i+1}$ with $A_{i+1}=3A_i+2^{E_i+1}$, turning future payouts into explicit 2-adic congruences.

### B6. Descent-Tree Survivors Are the Spine  *(NEW)*
📄 `descent_tree_survivors.md` · 🧪 `verify_tree_survivors.py`

Identifies *what survives* the residue-class descent tree, unifying three threads:
- **Exact:** the depth-$K$ survivors $S_K$ have density $\le\rho^K\to0$ (same Cramér rate as B4), and are the *valuation-deficient* (high-fuel / near-Mersenne) classes.
- **Anchor:** the all-ones $2^K-1$ survives at **every** depth — it is the unique minimal-valuation orbit ($E_j=j$), the extreme point of the lower tail.
- Explains why the nested bridge tree (mod $16/32/\dots$) can never close: at each depth a $\rho^K$-fraction survives, always including the spine.
- **Unifying rate:** B4 gives the complement, $D(K)\ge1-\rho^K$; B6 describes the same $\rho^K$ exceptional mass as the descent-tree survivor set.

### B7. Cycle Reduction  *(NEW)*
📄 `cycle_reduction.md` · 🧪 `verify_cycle_reduction.py`

Turns the affine accumulation into the cycle equation and reads off what is elementary:
- **Exact:** a $K$-odd-step cycle forces $x(2^{E_K}-3^K)=c_K$, so $x=c_K/(2^{E_K}-3^K)$ and $E_K\ge\lceil K\log_2 3\rceil$.
- **Verified:** only $x=1$ for $K\le8$ (exhaustive); no nontrivial cycle element $\le10^6$.
- **Corollary:** cycle minima have natural density $0$ (a cycle minimum has $\sigma=\infty$, inside the $\le\rho^K$ hard core).
- Stated limit: full cycle exclusion reduces to bounding the gap $|2^{E_K}-3^K|$ — the transcendence wall of Steiner (1977) / Simons–de Weger (2005), not reached here.

### C. Parity Fragility & Instability
📄 `Collatz_Parity_Fragility_Corrected.md`

A rigorous dynamical result: trajectories from $n$ and $n+\delta$ ($\delta \neq 0$) must diverge; any cycle is **repelling**. Establishes **Lock 3** below.

## 🧩 Structural summary

### D. Triple Lock (Cycle Impossibility Architecture)  *(revised, honestly labeled)*
📄 `Triple_Lock_Revised.md`

Three independent barriers to non-trivial cycles:
1. **Arithmetic Lock** — most U/D patterns have no integer solution *(evidential, not universal)*.
2. **Parity Lock** — integer solutions ("ghost loops") violate parity *(verified on all tested cases)*.
3. **Stability Lock** — any hypothetical cycle is dynamically repelling *(theorem; constrains stability, not existence)*.

The revision marks each lock as *evidential* or *proven*, plugs in the corrected Block-Fracture Identity as supporting structure, and notes that Lock 3 bounds a cycle's stability, not its existence. The $n=28$ ghost-loop worked example ($C=364$, $G=13$) is verified exactly.

Cycle Reduction (B7) makes the Arithmetic Lock precise: a cycle must solve
$x(2^{E_K}-3^K)=c_K$; excluding all such integer solutions is the remaining gap problem.

## 🌫️ Heuristic / structural arguments (compelling, not proven)

These describe the *macro picture* via density and probabilistic reasoning. They are evidential, not rigorous, and are labeled as such.

- 📄 `recharge_density_inverse_law.md` — only low-density states recharge; high density must burn down.
- 📄 `fusion_fracture_cycle.md` — the pulse–decay–reset rhythm of density.
- 📄 `refractory_period_barrier.md` — large fusion spikes can't reorganize before decay.

---

# 🔗 How the Documents Fit Together

- **Micro-scale (exact):** Block-Fracture Identity → high-density runs contract deterministically.
- **Residue-scale (exact):** Mod-8 Rail Descent → 3 of 4 rails descend or bridge exactly; the 4th escapes in finite time.
- **Potential boundary (exact negative):** Recharge No-Go → scalar trailing-one fuel potentials cannot prove global descent.
- **Potential candidate (recharge-safe, global open):** Exponential Decay Potential → bounded bit-weight fuel makes recharge steps safe (Theorem 1) and is empirically epoch-monotone to $10^7$; but epoch descent is carried by the bare $\log_2 x$ term, so it does not yet bypass the global obstruction.
- **Worst case (exact):** Mersenne–Repunit Reduction → $2^n-1$ solves to a base-3 repunit in $n$ steps; the rest is generic.
- **Average behaviour (exact):** Stopping-Time Density → almost every integer descends in boundedly many steps, $D(K)\ge1-\rho^K$.
- **Proof target:** Repunit Tail Attack → try to show the explicit repunit family cannot shadow the exceptional low-valuation tail for `3n` steps.
- **Tree structure (exact):** Descent-Tree Survivors → the undischarged classes are the spine, density $\le\rho^K$; finite-modulus refinement can't close.
- **Cycles (exact reduction):** Cycle Reduction → the cycle equation $x(2^{E_K}-3^K)=c_K$; cycle minima have density $0$; full exclusion needs the $|2^{E_K}-3^K|$ gap.
- **Medium/macro-scale (heuristic):** Recharge / Fusion–Fracture / Refractory → why density can't grow indefinitely.
- **Cycle architecture:** Triple Lock + Parity Fragility → cycles are arithmetically rare, parity-forbidden, and dynamically unstable.

---

# 🧭 Suggested Reading Order

1. **Block-Fracture Identity** (exact, micro-scale)
2. **Mod-8 Rail Descent** (exact, residue-scale)
3. **Recharge No-Go & Tight Mersenne Burn Ledger** (exact negative / potential boundary)
3.5. **Exponential Decay Potential** (recharge-safe candidate; global descent open)
4. **Mersenne–Repunit Reduction** (exact, worst-case structure)
5. **Explicit Stopping-Time Density** (exact, almost-all descent with rate)
6. **Repunit Tail Attack** (proof target after the exact reductions)
7. **Descent-Tree Survivors Are the Spine** (exact, ties the tree to the density rate)
8. **Cycle Reduction** (exact, the cycle equation and density-0 corollary)
9. **Parity Fragility (Corrected)** (exact, dynamical)
10. **Triple Lock (Revised)** (structural summary)
11. Recharge / Fusion–Fracture / Refractory (heuristic macro picture)

---

# 🧪 Reproducing the exact results

```bash
python3 verify_block_fracture.py   # Block-Fracture Identity + Mersenne erosion
python3 verify_mod8_rails.py       # Mod-8 rail lemmas + finite-window check to 1e6
python3 verify_recharge_nogo.py    # Recharge No-Go + tight Mersenne burn ledger
python3 verify_exponential_potential.py # Exponential decayed bit potential (0 failures to 1e6)
python3 verify_repunit_reduction.py # Mersenne -> base-3 repunit reduction (R0-R3 exact)
python3 verify_stopping_density.py  # Explicit stopping-time density D(K) >= 1 - rho^K
python3 verify_tree_survivors.py    # Descent-tree survivors = spine, density <= rho^K
python3 verify_cycle_reduction.py   # Cycle equation, no cycle <= 1e6, density-0 corollary
```

Both use exact integer arithmetic, need no dependencies, and print PASS for every claim (the mod-8 script's $10^6$ sweep takes a little longer).

For exploratory certificate work:

```bash
python3 explore_residue_certificates.py
python3 verify_descent_tree.py
python3 explore_potential.py
python3 explore_fuse_burn.py
python3 explore_mersenne_spine.py
python3 explore_mersenne_formulas.py
python3 explore_mersenne_epoch.py
python3 explore_repunit_tail.py
python3 explore_repunit_bad_automaton.py
python3 explore_repunit_index_automaton.py
python3 explore_repunit_normal_form.py
```

These scripts search for residue-class descent certificates. They are research tools, not proof artifacts: unresolved branches mean the current certificate strategy ran out of fixed low-bit information, not that a counterexample was found.

---

# 📌 About This Project

This project aims to separate *rigorous results* from *heuristic arguments*, create clean modular papers suitable for GitHub and peer review, avoid past overclaims, and unify algebraic, probabilistic, and computational insights.

It does **not** claim a proof of the Collatz conjecture. It presents a *structural explanation* of why the conjecture appears true, with the exact/heuristic boundary drawn explicitly.

---

# 🙌 Contact & Contributions

Issues, corrections, and improvements are welcome. Feel free to open a GitHub Issue or pull request.

---

The guy who wrote these can drink and supports Liverpool FC.
