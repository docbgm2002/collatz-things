# Interference of exact normal forms: two-tower arithmetic  [W8, re-scoped]

**Task:** `OPUS5_WIDE_TASKS.md` W8 (session 6 of the recommended order),
**re-scoped** — see §0.
**Building on:** `tower_theorem.md` (TWR1), `certificate_semigroup.md`
(W2-A: TWR1 \(=P_2^{\,d}\), and the \(\sigma\)-ghost \(-1/3\)),
`recharge_nogo.md` (the Andaloro burn), `superposition_interaction_ledger.md`
(W1, whose closure prompted the re-scoping).
**Verifier:** `scripts/verify_two_tower_interference.py` (14 checks; exact
integer and rational arithmetic).
**Status:** **Success criterion met, avenue foreclosed.** Closed-form
sub-lanes exist for *every* alignment — but they are not new lanes. Every
two-tower interference resolves onto a ghost the repo already carries.
**License:** CC-BY 4.0

---

## 0. The re-scoping

W8 was written as "a narrower, fully concrete slice of W1 … a direct
laboratory for superposition-transfer statements". Session 5 closed W1: the
superposition defect is a *slope* mismatch of trajectory size, not a carry
ledger, so no laboratory can rescue it. That motivation is dead and is not
pursued here.

What survives is W8's own question, which never depended on W1:

> Do sums and differences of tower members carry closed-form itineraries —
> is there a new exact lane like SPN1?

Its success criterion ("any closed-form sub-lane") and kill criterion ("kill
if carries destroy periodicity immediately outside the frozen-tail overlap
for all alignments") are both intrinsic. This note answers that question and
nothing else.

The re-scoping also gets a free simplification from session 2. W2-A showed

\[
w_d(M)=P_2^{\,d}\bigl(2^{M}-1\bigr)=1+\Bigl(\tfrac43\Bigr)^{d}\bigl(2^{M}-2\bigr),
\qquad P_2(z)=\tfrac{4z-1}{3},
\]

which is a much better handle than TWR1's original numerator form, and it is
what makes §1 a two-line computation.

---

## 1. The two-tower ghost algebra

TWR1(e) gives the frozen tail \(\Lambda_d=1-2(4/3)^{d}\), with
\(w_d(M)\equiv\Lambda_d\pmod{2^{M-1}}\). For a pair, define

\[
\Xi_{d,d'}\;:=\;1-\Bigl(\tfrac43\Bigr)^{d}-\Bigl(\tfrac43\Bigr)^{d'} .
\]

> **W8-A (proved here).** For \(d,d'\ge1\):
> 1. \(\Lambda_d=\Xi_{d,d}\) **exactly**;
> 2. \(3\,\Xi_{d,d'}+1=4\,\Xi_{d-1,d'-1}\), i.e.
>    \(\Xi_{d,d'}=P_2\bigl(\Xi_{d-1,d'-1}\bigr)\), hence
>    \(\Xi_{d,d'}=P_2^{\,m}\bigl(-(4/3)^{k}\bigr)\) with
>    \(m=\min(d,d')\), \(k=|d-d'|\);
> 3. \(f^{\,m}(\Xi_{d,d'})=-3^{-k}\) in \(\mathbb Q_2\).

*Proof of 2.* \(3(4/3)^{j}=4(4/3)^{j-1}\), so
\(3\Xi_{d,d'}+1=4-4(4/3)^{d-1}-4(4/3)^{d'-1}=4\Xi_{d-1,d'-1}\). \(\square\)
Item 1 is \(1-2(4/3)^d\) read twice; item 3 follows by iterating 2 and noting
that \(\Xi_{j,j'}\) is a \(2\)-adic unit for \(j,j'\ge1\) while
\(\Xi_{k,0}=-(4/3)^{k}\) has \(v_2=2k\), which the final step absorbs.

Sample (verifier output):

| \(d\) | \(d'\) | \(\Xi_{d,d'}\) | \(v_2(3\Xi+1)\) | \(f\)-image |
|---:|---:|---|---:|---|
| 1 | 1 | \(-5/3\) | 2 | \(-1\) |
| 2 | 2 | \(-23/9\) | 2 | \(-5/3\) |
| 3 | 3 | \(-101/27\) | 2 | \(-23/9\) |
| 1 | 2 | \(-19/9\) | 4 | \(-1/3\) |
| 1 | 3 | \(-73/27\) | 6 | \(-1/9\) |

**Item 1 is the surprise.** The frozen tail of a *diagonal two-tower sum* is
the frozen tail of a *single* tower member at the same level. The
interference is invisible at the level of the ghost.

---

## 2. The exact lane

> **W8-B (proved here; new exact lane).** Let \(d\ge1\) and
> \(M,M'\equiv1\pmod{2\cdot3^{d-1}}\). Put \(s=w_d(M)+w_d(M')\) and
> \(V=\min(M,M')-2d-1\). Then
> - \(v_2(s)=1\), so \(x_0=s/2\) is odd;
> - \(x_0\equiv\Lambda_d\pmod{2^{\min(M,M')-2}}\): \(x_0\) lies in the **same
>   tower cylinder** as \(w_d\) itself;
> - the accelerated itinerary of \(x_0\) begins with the exact word
>   \[
>   \boxed{\;2^{\,d}\,1^{\,V-1}\;}
>   \]
>   — \(d\) steps of \(e=2\) walking the tower down to a Mersenne-form number
>   \(2^{V}u-1\), followed by the Andaloro burn.

Verified for \(d\le4\) over all pairs from five admissible \(M\) each, and at
\(758\)-bit scale (\(d=3\), \(M=739\), predicted lane length 734 — matched
exactly).

**Sharpness.** The word \(2^d1^{V-1}\) is a *guaranteed prefix*, not the whole
lane: \(x_d\equiv-1\pmod{2^{V}}\) forces \(\tau(x_d)\ge V\), and the burn
actually runs \(\tau(x_d)-1\) steps. In the \(d=2,M=49,M'=55\) instance the
predicted 45 steps matched and the burn continued four steps further before
the first non-burn valuation (10). So \(V\) is a lower bound on the lane
length and the lane is a little longer than advertised.

---

## 3. The complete classification

Everything else in the family is closed-form too.

| family | \(v_2\) | odd part / frozen tail | initial \(e\)-word |
|---|---|---|---|
| diagonal sum \(w_d(M)+w_d(M')\) | \(1\) | \(\Lambda_d\) | \(2^d1^{V-1}\) |
| off-diagonal sum \(w_d(M)+w_{d'}(M')\) | \(1\) | \(\Xi_{d,d'}\), reaching \(-3^{-k}\) | \(2^{\,m-1}\,(2{+}2k)\) |
| diagonal difference \(w_d(M)-w_d(M')\) | \(2d+M'\) | exactly \((2^{M-M'}-1)/3^{d}\) | — |
| off-diagonal difference | \(2\min(d,d')+1\) | \(-3^{-d}\bigl(1-(4/3)^{k}\bigr)\) | — |
| \(w_d(M)\pm2^{j}\) | — | \(\Lambda_d\) perturbed at bit \(j\) | tower word while \(E_K<j\) |

with \(m=\min(d,d')\), \(k=|d-d'|\). All rows verified exactly.

The diagonal-difference row is worth isolating: the odd part is exactly
\((2^{L}-1)/3^{d}\) with \(L=M-M'\), which is TWR1's own block constant
\(B_d=(2^{\mathrm{ord}_d}-1)/3^{d}\) generalised to arbitrary admissible
\(L\). So a two-tower difference lands back inside the tower's own
normal-form family.

---

## 4. Verdict: the criterion is met, and the family is foreclosed

The success criterion asked for *any* closed-form sub-lane. There is one for
every alignment (§2, §3), so on its own terms W8 succeeds and the kill
criterion — "carries destroy periodicity immediately outside the frozen-tail
overlap **for all alignments**" — does not fire: they do not destroy it
immediately, and the lane runs the full frozen depth.

But the honest reading is negative, and it is the finding worth filing.

> **W8-C (the foreclosure).** Every two-tower interference resolves onto a
> ghost the repository already carries:
> \[
> \Xi_{d,d}=\Lambda_d\ \ (\text{TWR1}),\qquad
> f^{m}(\Xi_{d,d'})=-3^{-k},
> \]
> and \(-3^{0}=-1\) is the Mersenne ghost (the burn), \(-3^{-1}=-1/3\) is the
> \(\sigma\)-ghost of W2 (the \(4n+1\) recharge limit), and \(-3^{-k}\) for
> \(k\ge2\) is the ghost of the tower block-constant family
> \((2^{L}-1)/3^{k}\). No new lane is produced: the diagonal sum *is* TWR1's
> lane reached from a different starting point, and the off-diagonal cases
> fall onto objects already in the ledger.

So the family is a closed system. Two-tower arithmetic cannot manufacture a
state outside the Mersenne / tower / \(\sigma\) ghost set, and therefore
cannot supply a new exact lane for the descent programme to exploit.

### 4.1 The structural moral

Across sessions 1–6 the same distinction keeps appearing, and it is worth
recording explicitly as an observation (not a theorem):

> **The exact lanes of this repository are precisely the orbits that shadow
> *rational* \(2\)-adic ghosts; the hard open objects shadow *irrational*
> ones.**

- Rational ghosts, all with closed-form lanes: \(-1\) (Mersenne burn),
  \(-1/3\) (the \(\sigma\)/recharge limit, W2 §4.3), \(\Lambda_d=1-2(4/3)^d\)
  (TWR1), \(-3^{-k}\) (block constants), and now \(\Xi_{d,d'}\) (this note).
- Irrational ghosts, all open: \(\alpha\) with \(3^{\alpha}=-7\) (BAKER1–3,
  W9 §4), \(\alpha_A\) for general \(A\) (W10-A), the balanced
  starting-cylinder ghost \(u_\infty\) and the exponent ghost
  \(\alpha_\infty\) with \(3^{\alpha_\infty}=2u_\infty+1\) (W11 §7bis).

The rational ones are closed-form precisely because \(P_2\) and \(f\) act on
\(\mathbb Q\cap\mathbb Z_2\) by affine maps with small denominators, so
orbits are eventually periodic. The irrational ones are exactly where the
transcendence and digit questions live. W8 confirms the two-tower family sits
entirely on the rational side, which is why it is both fully solvable and
strategically inert.

---

## 5. Barrier check

1. *Finite-state information.* Not invoked; §2 is an exact identity, not an
   automaton.
2. *Density / entropy.* Not invoked.
3. *Variable-height Diophantine.* Not invoked — the ghosts here are rational
   with fixed denominators \(3^{d}\), which is precisely why no Diophantine
   input is needed.
4. *Virtual sources.* **Respected, and worth noting.** Every statement here
   is about actual integers \(w_d(M)\pm w_{d'}(M')\) with actual computed
   trajectories; the frozen tails are used only to *predict* those
   trajectories, and every prediction is checked against the real orbit. This
   is the discipline W1 §2.2 failed to meet.

**Explicit non-claims.** Nothing here produces a descent, a merger, or a
bound on any open quantity. W8-B is a new exact family with a closed-form
itinerary prefix; W8-C says that family is not new *structure*.

---

## 6. Falsifier

- **W8-A** is falsified by a pair \((d,d')\) with
  \(3\Xi_{d,d'}+1\ne4\Xi_{d-1,d'-1}\), or with
  \(f^{\min(d,d')}(\Xi_{d,d'})\ne-3^{-|d-d'|}\). Checked for all
  \(1\le d,d'\le8\).
- **W8-B** is falsified by an admissible \((d,M,M')\) whose halved diagonal
  sum does not have \(e\)-word \(2^{d}1^{V-1}\). Checked for \(d\le4\) over
  all pairs from five admissible \(M\), and at \(d=3\), \(M=739\).
- **W8-C** is falsified by an alignment whose orbit leaves
  \(\{-3^{-k}\}\cup\{\Lambda_d\}\) — i.e. a two-tower combination landing on a
  ghost outside the known set. That is the one thing that would reopen the
  avenue, and §1 item 2 shows why it cannot happen for sums: the \(P_2\)
  recursion drives every \(\Xi_{d,d'}\) down the same chain.
- The classification is stated only for **two** towers. Three or more
  (\(\sum_j w_{d_j}(M_j)\)) has ghost
  \(1-\sum_j(4/3)^{d_j}\) plus a parity correction; the same \(P_2\)
  recursion applies whenever all \(d_j\ge1\), so the same foreclosure is
  expected, but it is **not verified here**.

---

## 7. Verification

```bash
python3 scripts/verify_two_tower_interference.py
```

Prints `TWO-TOWER: PASS` (14 checks, under a second).

---

## 8. Suggested ledger rows (not applied)

| ID | Statement | Status | Source |
|---|---|---|---|
| TTI1 | \(\Lambda_d=\Xi_{d,d}\); \(3\Xi_{d,d'}+1=4\Xi_{d-1,d'-1}\); \(f^{\min}(\Xi_{d,d'})=-3^{-\lvert d-d'\rvert}\) | Proved here | §1 (W8-A) |
| TTI2 | For \(M,M'\equiv1\ (2\cdot3^{d-1})\), \((w_d(M)+w_d(M'))/2\) lies in the tower cylinder of \(w_d\) and has \(e\)-word prefix \(2^{d}1^{V-1}\), \(V=\min(M,M')-2d-1\) | Proved here | §2 (W8-B) |
| TTI3 | \(w_d(M)-w_d(M')\) has \(v_2=2d+M'\) and odd part exactly \((2^{M-M'}-1)/3^{d}\) | Proved here | §3 |
| TTI4 | Every two-tower sum/difference resolves onto \(\Lambda_d\) or \(-3^{-k}\); no new exact lane is produced | Proved here | §4 (W8-C) |

TTI4 is the row that matters: it forecloses the family, so the tower normal
forms should not be revisited as a source of new lanes.
