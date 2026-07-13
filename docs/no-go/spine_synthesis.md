# Spine Synthesis: the Complete Exact Lane

**Building on:** `tower_theorem.md` (TWR1), `recharge_nogo.md` (MER1),
`../repunit/mersenne_repunit_reduction.md` (MER2, R0), `../core/Mod8_Rail_Descent.md`,
`../repunit/repunit_tail_attack.md`, `Exponential_Decay_Potential.md`,
`../../archive/potential_attack_notes.md`
**Status:** Theorem S1 is a composition of already-proved results plus two
small exact additions (rail location; exact repunit payout on tower-fed
Mersennes), machine-checked in `scripts/verify_spine_synthesis.py`. Theorem S2
(bounded corrections) is new but one paragraph. Nothing here bears on the
open residual $\sigma(a_n)$; Observation R4's genericity verdict stands.
**License:** CC-BY 4.0

---

## 1. Theorem S1 (the complete exact lane)

Let $d\ge1$, $\mathrm{ord}_d=2\cdot3^{d-1}$, $s\ge1$, $M=1+\mathrm{ord}_d\,s$
(automatically odd). Then the orbit of $w_d(M)$ is exactly known for its
first $d+M+1$ odd steps:

$$
w_d(M)\ \xrightarrow{\ d\ \text{steps},\ e=2,\ \times(\tfrac34)^{+}\ }\
2^M-1\ \xrightarrow{\ M-1\ \text{steps},\ e=1,\ \times(\tfrac32)^{+}\ }\
2\cdot3^{M-1}-1\ \xrightarrow{\ 1\ \text{step}\ }\ a_M
\ \xrightarrow{\ 1\ \text{step}\ }\ \frac{a_{M+1}}{2^{\,e^\star}},
$$

where $a_m=(3^m-1)/2$ is the base-3 repunit and the repunit's first payout
is exactly

$$
e^\star \;=\; 1+v_2(M+1)\;=\;2+v_2\!\bigl(1+3^{\,d-1}s\bigr)
\qquad\bigl(=2\ \text{iff}\ s\ \text{is even}\bigr).
$$

Moreover **every tower member $w_d(M)$, $d\ge1$, lies on rail
$8y+1$**: the entire uniform-$e{=}2$ ancestry of the Mersenne spine — the
worst members of the hard rail $8y+7$ — lives on the rail where
`../core/Mod8_Rail_Descent.md` proves immediate descent.

*Proof.* The three segments are TWR1 (tower descent), MER1 (burn closed
form), and MER2 with $M$ odd (repunit landing). The payout: by
`../repunit/repunit_tail_attack.md` §2 (LTE), $v_2(3a_M+1)=1+v_2(M+1)$; here
$M+1=2\,(1+3^{\,d-1}s)$ with $3^{\,d-1}s$ odd iff $s$ odd, giving the
formula and the parity criterion. The rail: $w_d(M)\equiv9\ (d{=}1)$ or
$\equiv1\ (d{\ge}2)$ modulo $16$ (tower theorem, Lemma D.2 calculus),
hence $\equiv1\pmod 8$ in both cases. $\;\blacksquare$

**Reading.** Three programs meet in one picture:

* **Rails.** Rail 7's hardest inhabitants (near-Mersenne, high fuel) are
  fed, along the slowest exact lanes, entirely from rail 1 — the tamest
  rail. The rail decomposition is not just a case split; it is a
  routing diagram: tame rail $\to$ frozen 2-adic lane $\to$ maximal fuel
  $\to$ burn $\to$ repunit.
* **Repunits.** The lane terminates on the repunit ladder ($3a_m+1=a_{m+1}$,
  R0) with a payout $e^\star$ controlled by the tower parameters through
  LTE — the same lemma that generates the tower's periodic blocks
  $B_d=(2^{\mathrm{ord}_d}-1)/3^d$. On the even-$s$ half of every tower
  progression the lane extends one more exact step with $e^\star=2$.
* **Where exactness ends.** After $f(a_M)$ the orbit is generic
  (Observation R4); the lane adds $d+M+1$ exact steps to the front, not
  one step to the back. The open residual is unchanged: $\sigma(a_n)$.

---

## 2. Theorem S2 (no bounded correction)

**Theorem.** Let $G:2\Z+1\to\R$ be **any bounded** function. Then
$\Phi(x)=\log_2x+G(x)$ is not nonincreasing along $f$ on odd $x>1$.

*Proof.* Let $\Omega=\sup G-\inf G<\infty$. If $\Phi$ were nonincreasing,
then telescoping over the burn of $2^M-1$ (MER1: $M-1$ steps, each with
value ratio $>\tfrac32$) gives
$0\ge\Phi(2\cdot3^{M-1}-1)-\Phi(2^M-1)>(M-1)\log_2\tfrac32-\Omega$,
false for $M>1+\Omega/\log_2\tfrac32$. $\;\blacksquare$

**Consequences.**
* This closes, as a theorem, the axis that
  `Exponential_Decay_Potential.md` explored and honestly conceded in its
  §4: the decayed-bit potential $\log_2x+c\,g_r(x)$ has
  $\Omega\le 2c/(1-r)$, so it fails globally for *every* parameter choice
  — as do all bounded corrections, of arbitrary dependence on $x$
  (whole-word, high-bit, anything). POT1 (recharge-family descent) and
  POT2 (epoch certificate) are untouched; the note's "not a global
  Lyapunov function" upgrades from admission to consequence of S2.
* Combined with the NLP theorems, the potential landscape is now:
  bounded corrections fail (S2, burn alone); unbounded corrections
  through any finite tower of low-end coordinates fail (NLP-$d$, burn +
  recharge scissors). What survives is unbounded + genuinely global —
  e.g. functions of $(\tau,\mathrm{len})$ — where, as the manuscript's
  boundary section records, the class borders on arbitrary corrections
  and the question changes character.
* For the paired-macro program of `../../archive/potential_attack_notes.md` §5: S1
  supplies the exact macro inventory. A recharge$\to$burn$\to$escape pair
  fed through a depth-$d$ lane has exact multiplicative drift
  $\bigl(\tfrac34\bigr)^{d+O(1)}\bigl(\tfrac32\bigr)^{M-1}
  \cdot2^{-e^\star}\cdots$ up to the repunit; the pair's *net* drift
  question is then exactly $\sigma(a_M)$ again. The macro program cannot
  shortcut the residual either — worth recording so it is not re-attempted.

---

## Appendix — Verification

`scripts/verify_spine_synthesis.py` checks with exact integer arithmetic, for
$d\le5$, $s\le5$ (and rails to $d\le6$, $s\le7$): the full
$d+M+1$-step lane including both closed forms and the repunit landing;
the payout formula $e^\star=2+v_2(1+3^{d-1}s)$ and its parity criterion;
rail $8y+1$ for every tower member; and the S2 arithmetic (exact burn
ratio exceeding $(3/2)^{M-1}$).

Note (correction history): a draft of S1 claimed $M\equiv1\pmod4$
uniformly, hence $e^\star=2$ always; the verifier refuted this at
$(d,s)=(1,1)$, and the statement was corrected to the parity-split
formula before promotion. Logged per repository practice.

## Ledger entries

| ID | Claim | Status | Source | Verification |
|---|---|---|---|---|
| SPN1 | Complete exact lane of length $d+M+1$: tower $\to$ Mersenne $\to$ burn $\to$ repunit, with exact payout $e^\star$ and rail-$1$ location of all tower members | Proved here (composition + two exact additions) | `spine_synthesis.md` | `scripts/verify_spine_synthesis.py` |
| BND1 | No potential $\log_2x+G(x)$ with bounded $G$ is nonincreasing | Proved here | `spine_synthesis.md` | one-paragraph proof from MER1; arithmetic in verifier |

These rows are recorded in `../../CLAIM_LEDGER.md`.
