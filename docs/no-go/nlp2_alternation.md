# No-Go for Potentials with a Latent-Fuel Detector (NLP2)

**Building on:** `no_local_potential.md` (NLP1), `latent_fuel_notes.md`
(Lemmas L1–L2), `recharge_nogo.md` (Lemmas 1–2)
**Status:** Theorem 1 (NLP2) is proved here, depending only on the already
proved L1–L2 and the NLP1 lemmas; machine-checked in `scripts/verify_nlp2.py`.
Theorem 2 (NLP-$d$) is **conditional** on the hierarchy conjecture of
`latent_fuel_notes.md` and is labelled as such. Not a proof of the Collatz
conjecture.
**License:** CC-BY 4.0

---

## Abstract

NLP1 showed no potential $\log_2x+g(x\bmod2^m,\tau(x))$ is nonincreasing:
fixed-modulus residues plus the trailing-one count cannot distinguish hot
fuel from cold. The natural repair is a detector for *latent* fuel — the
alternating suffix $(\texttt{10})^\ell\texttt{1001}$ that converts to
trailing ones in one step (Lemma L1). Define

$$
\lambda(x)=\max\{\ell\ge0:\ x\equiv x'_{2\ell+3}\ (\mathrm{mod}\ 2^{2\ell+4})\},
\qquad x'_M=\tfrac{2^{M+2}-5}{3},
$$

with $\lambda(x)=\bot$ when no $\ell$ matches. This detector is unbounded
and genuinely informative: $\lambda(x'_M)=\tfrac{M-3}{2}$, so it *sees the
recharge coming* and breaks the NLP1 contradiction. **Theorem 1:** it does
not help — no potential $\log_2x+g(x\bmod2^m,\tau(x),\lambda(x))$ is
nonincreasing either. The level-2 family $y_k=(\texttt{111000})^k\texttt{01}$
of Lemma L2 is invisible to $\lambda$ (its residue mod $16$ is $1$, not
the required $9$), so it feeds the recharge one step earlier at a cost of
only one more $\log_2\frac43$, and the scissors reclose one link deeper.
Each detector level costs the adversary a bounded constant while the burn
liability stays unbounded — the mechanism telescopes.

---

## 0. Setup and the coordinate facts

Notation as in `../../NOTATION.md`. Fix $m\ge0$ and arbitrary
$g:(\mathbb Z/2^m)^\times\times\mathbb Z_{\ge1}\times(\mathbb
Z_{\ge0}\cup\{\bot\})\to\mathbb R$; suppose toward a contradiction that
$P(x)=\log_2x+g(x\bmod2^m,\tau(x),\lambda(x))$ satisfies
$P(f(x))\le P(x)$ for all odd $x>1$.

**Lemma 0 (coordinate facts; machine-checked).**
1. $x\equiv x'_3=9\ (\mathrm{mod}\ 16)$ is necessary for $\lambda(x)\ne\bot$
   (the $\ell=0$ template).
2. Burn members $3^{\,j}2^{\,t}-1$ with $t\ge4$, and all-ones $2^M-1$ with
   $M\ge4$, are $\equiv15\ (\mathrm{mod}\ 16)$; hence $\lambda=\bot$ on
   both.
3. $\lambda(x'_M)=\tfrac{M-3}{2}$ for odd $M\ge5$ (match at
   $\ell=\tfrac{M-3}{2}$ is equality of $(M{+}1)$-bit numbers; larger
   $\ell$ would force equality of distinct numbers below $2^{2\ell+4}$).
4. $y_k=(2^{6k+5}-23)/9\equiv1\ (\mathrm{mod}\ 16)$, hence
   $\lambda(y_k)=\bot$; also $\tau(y_k)=1$ and
   $y_k\equiv r^{\star\star}:=-23\cdot9^{-1}\ (\mathrm{mod}\ 2^m)$ for all
   $k$ with $6k+2\ge m$ — a frozen residue.
5. Both chain steps drop value by less than $\log_2\frac43$:
   $3y_k<4\,x'_{6k+1}$ and $3\,x'_{M}<4\,(2^{M}-1)$, exactly.

*Proof.* (1)–(2), (4)–(5) are direct congruence/inequality computations
(`scripts/verify_nlp2.py`, exact arithmetic, wide ranges); (3) as sketched:
$x'_M$ has $M+1$ bits, so the modulus-$2^{M+1}$ congruence at
$\ell=\frac{M-3}{2}$ is equality with the template, while for larger
$\ell$ both sides are distinct integers below the modulus. $\;\blacksquare$

---

## 1. Theorem 1 (NLP2)

**Theorem 1.** For every $m\ge0$ and every $g$, the potential
$P(x)=\log_2x+g(x\bmod2^m,\ \tau(x),\ \lambda(x))$ is not nonincreasing
along $f$ over odd $x>1$.

*Proof.* Write $t_0=\max(m+1,5)$.

**(i) Burn.** For $t\ge t_0$ and any $j\ge0$, the step
$x=3^{\,j}2^{\,t}-1\mapsto f(x)=3^{\,j+1}2^{\,t-1}-1$ (NLP1 Lemma 1) has
both endpoints with residue $-1\bmod2^m$, trailing-one counts $t,t-1$, and
$\lambda=\bot$ on both (Lemma 0.2, using $t-1\ge4$). Monotonicity forces
$g(-1,t,\bot)-g(-1,t-1,\bot)>\log_2\tfrac32$, hence

$$
g(-1,M,\bot)\;\ge\;g(-1,t_0,\bot)+(M-t_0)\log_2\tfrac32
\qquad(M>t_0). \tag{1}
$$

**(ii) Recharge, level 1.** For odd $M\ge\max(m,5)$, the step
$x'_M\mapsto2^M-1$ (Lemma L1) has coordinates
$(r^\star,\,1,\,\tfrac{M-3}{2})\mapsto(-1,\,M,\,\bot)$ (Lemma 0.2–0.3;
$r^\star=-5\cdot3^{-1}\bmod2^m$ frozen as in NLP1). Monotonicity and
Lemma 0.5 give

$$
g(-1,M,\bot)\;\le\;g\big(r^\star,1,\tfrac{M-3}{2}\big)+\log_2\tfrac43. \tag{2}
$$

Unlike NLP1, the right side is **not** a constant: $\lambda$ grows with
$M$. This is exactly the repair the detector was meant to provide.

**(iii) Recharge, level 2.** Take $M=6k+1$ with $k$ large enough that
$6k+2\ge m$. The step $y_k\mapsto x'_{6k+1}$ (Lemma L2) has coordinates
$(r^{\star\star},\,1,\,\bot)\mapsto(r^\star,\,1,\,3k-1)$ (Lemma 0.4,
0.3; note $\tfrac{M-3}{2}=3k-1$). Monotonicity and Lemma 0.5 give

$$
g\big(r^\star,1,3k-1\big)\;\le\;g\big(r^{\star\star},1,\bot\big)
+\log_2\tfrac43. \tag{3}
$$

**(iv) Close.** Chain (1)→(2)→(3) at $M=6k+1$:

$$
g(-1,t_0,\bot)+(6k+1-t_0)\log_2\tfrac32
\;\le\;g\big(r^{\star\star},1,\bot\big)+2\log_2\tfrac43 .
$$

The right side is a constant; the left side is unbounded in $k$.
Contradiction. $\;\blacksquare$

---

## 2. Theorem 2 (NLP-$d$, conditional)

**Theorem 2 (conditional on the hierarchy conjecture of
`latent_fuel_notes.md`).** Suppose for each depth $i\le d+1$ there is an
exact family $w_i^{(k)}$ of eventually-periodic-suffix words with
$f(w_{i}^{(k)})=w_{i-1}^{(k')}$ (value ratio $<\tfrac43$ per step,
$w_0=$ all-ones), each family frozen in every coordinate of levels
$<i$ (residue mod $2^m$, $\tau$, and the level-$1..i{-}1$ detectors
$\lambda_1,\dots,\lambda_{i-1}$), while the level-$i$ detector reads an
unbounded run on $w_i^{(k)}$. Then no potential
$\log_2x+g(x\bmod2^m,\tau,\lambda_1,\dots,\lambda_d)$ is nonincreasing:
chaining the $d{+}1$ recharge steps caps $g$ at the burn coordinate by a
constant plus $(d{+}1)\log_2\tfrac43$, against the unbounded burn
liability (1).

*Status.* The hypothesis is proved for $i\le2$ (L1, L2 — this is
Theorem 1) and is supported at $i=3$ by the period-18 evidence in
`scripts/explore_latent_fuel.py`. Theorem 2 is a one-paragraph induction **given**
the families; the mathematical content of the conjecture is their
existence with the freezing property. If the hierarchy conjecture holds
for all $d$, the conclusion is: *no finite tower of suffix-periodicity
detectors, of any depths, added to any fixed-modulus window and the
trailing-one count, admits a monotone one-step potential.*

---

## 3. Reading

NLP1 said local coordinates fail. NLP2 says the *obvious first non-local
repair* — detect the pattern that recharges fuel — fails too, and fails
for a structural reason with a price list: each level of detection buys
the adversary one more $\log_2\frac43$ of cap, a bounded cost, while the
liability $\log_2\frac32\cdot M$ is unbounded. A monotone potential must
either read unboundedly deep pattern structure all at once (whole-word
objects: the repunit normal forms, per-rail $\Delta z$ distributions), or
abandon the one-step scalar form (paired/multi-step accounting, as
proposed in `../../archive/potential_attack_notes.md` §5). The hierarchy prices the
first option: any finite depth is insufficient, conditionally for all
$d$, unconditionally for $d\le1$ beyond NLP1's $d=0$.

---

## Appendix — Verification

`scripts/verify_nlp2.py` checks with exact integer arithmetic, over wide ranges:
Lemma 0.1–0.5 (the $\lambda$ values and $\bot$-freezing on all three
families, frozen residues $r^\star$, $r^{\star\star}$, both exact ratio
bounds), the burn-step coordinate freeze at level $\lambda=\bot$, and the
chain arithmetic $(6k+1-t_0)\log_2\frac32>C+2\log_2\frac43$ for every
sampled constant $C$.

```bash
python3 scripts/verify_nlp2.py   # prints PASS for every claim above
```

## Ledger status

| ID | Claim | Status | Source | Verification |
|---|---|---|---|---|
| NLP2 | No potential $\log_2x+g(x\bmod2^m,\tau(x),\lambda(x))$ is nonincreasing, any $m$, any $g$ | Proved here; subsumed by SH1 | `nlp2_alternation.md` | `scripts/verify_nlp2.py`; depends on NLP1 lemmas and L1–L2 |

The conditional NLPD formulation developed in this note was subsequently
proved unconditionally in `tower_theorem.md` and then subsumed, as an
impossibility statement, by SH1. The current NLP2 and NLPD rows are recorded in
`../../CLAIM_LEDGER.md`.
