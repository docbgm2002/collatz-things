# No-Go for Local-Coordinate Potentials

**Building on:** `recharge_nogo.md` (Lemmas 1–3), `../../NOTATION.md`
**Status:** Proved here, subject to a final external literature check
(surveys state the absence of a known monotone invariant as folklore; no
published theorem excluding this class was found in the search of
2026-07-01). Strictly generalizes RNG1. Not a proof of the Collatz
conjecture.
**License:** CC-BY 4.0

---

## Abstract

`recharge_nogo.md` (RNG1) proved that no potential $\log_2 x + g(\tau(x))$
is nonincreasing along the odd-step map $f$. Here the same burn/recharge
scissors closes on a strictly larger class: **no potential of the form**

$$
P(x)=\log_2 x + g\big(x\bmod 2^m,\ \tau(x)\big)
$$

**is nonincreasing along $f$ over all odd $x>1$, for any modulus $2^m$ and
any function $g$ whatsoever.** The mechanism is that both the Mersenne burn
family and the recharge family are *residue-frozen*: every member of either
family sits in a single residue class mod $2^m$ once its parameters clear
$m$, so fixed-modulus information cannot distinguish a burning number from a
freshly recharged one. Since the pair $(x\bmod 2^m,\ \tau(x))$ determines
the entire low-bit window of $x$ of width $\max(m,\tau+1)$, the corollary
is: **a monotone potential correcting $\log_2 x$ must use unbounded-window
information about $x$.** The $m=0$ case is exactly RNG1.

---

## 0. Setup

Notation as in `../../NOTATION.md`: $f(x)=(3x+1)/2^{v_2(3x+1)}$ for odd $x$,
$\tau(x)=v_2(x+1)$. Fix $m\ge0$ and an arbitrary
$g:(\mathbb Z/2^m\mathbb Z)^\times\times\mathbb Z_{\ge1}\to\mathbb R$
(for $m=0$ read $g$ as a function of $\tau$ alone). Suppose toward a
contradiction that

$$
P(f(x))\le P(x)\qquad\text{for every odd }x>1. \tag{$\ast$}
$$

Both families below are drawn from `recharge_nogo.md`; only the residue
bookkeeping is new.

---

## 1. The burn family is residue-frozen

**Lemma 1.** Let $t\ge\max(m+1,2)$ and $j\ge0$, and set
$x=3^{\,j}2^{\,t}-1$. Then

$$
\tau(x)=t,\qquad x\equiv-1\ (\mathrm{mod}\ 2^m),\qquad
f(x)=3^{\,j+1}2^{\,t-1}-1,\qquad \tau(f(x))=t-1,
$$

$$
f(x)\equiv-1\ (\mathrm{mod}\ 2^m),\qquad \frac{f(x)}{x}=\frac32+\frac1{2x}>\frac32 .
$$

*Proof.* $x+1=3^{\,j}2^{\,t}$ with $3^{\,j}$ odd gives $\tau(x)=t$, and
$2^m\mid x+1$ since $t\ge m$, so $x\equiv-1$. By `recharge_nogo.md`
Lemma 1 (applicable since $\tau(x)=t\ge2$), $v_2(3x+1)=1$ and
$f(x)=(3x+1)/2=3^{\,j+1}2^{\,t-1}-1$ with $\tau(f(x))=t-1$ and the stated
ratio. Finally $f(x)+1=3^{\,j+1}2^{\,t-1}$ and $t-1\ge m$, so
$f(x)\equiv-1$. $\;\blacksquare$

**Consequence.** Applying $(\ast)$ to the step $x\to f(x)$ of Lemma 1:

$$
g(-1,\,t)-g(-1,\,t-1)\;\ge\;\log_2\!\Big(\tfrac32+\tfrac1{2x}\Big)
\;>\;\log_2\tfrac32
\qquad\text{for every }t\ge\max(m+1,2),
$$

(taking $j\to\infty$ if one wants the clean constant; the strict form above
already suffices). Summing from $t_0:=\max(m+1,2)$ to $M$:

$$
g(-1,\,M)\;\ge\;g(-1,\,t_0)\;+\;(M-t_0)\,\log_2\tfrac32
\qquad(M>t_0). \tag{1}
$$

The right side tends to $+\infty$ with $M$.

---

## 2. The recharge family is residue-frozen

**Lemma 2.** Let $M$ be odd, $M\ge\max(m,3)$, and set
$x'_M=(2^{\,M+2}-5)/3$ (an integer since $M$ is odd). Then

$$
f(x'_M)=2^{\,M}-1,\qquad \tau(x'_M)=1,\qquad \tau(f(x'_M))=M,
$$

$$
x'_M\equiv r^\star:=-5\cdot3^{-1}\ (\mathrm{mod}\ 2^m)
\quad\text{— independent of }M,\qquad
f(x'_M)\equiv-1\ (\mathrm{mod}\ 2^m),
$$

$$
\frac{x'_M}{2^{\,M}-1}\;<\;\frac43 .
$$

*Proof.* $f(x'_M)=2^M-1$ and $\tau(f(x'_M))=M$ are `recharge_nogo.md`
Lemma 2. For $\tau(x'_M)$: $x'_M+1=(2^{\,M+2}-2)/3=2\cdot(2^{\,M+1}-1)/3$,
and $2^{\,M+1}-1\equiv3\ (\mathrm{mod}\ 4)$ (as $M+1\ge4$), so
$(2^{\,M+1}-1)/3$ is odd; hence $\tau(x'_M)=1$. For the residue:
$3x'_M=2^{\,M+2}-5\equiv-5\ (\mathrm{mod}\ 2^m)$ since $M+2\ge m$, and $3$
is invertible mod $2^m$, so $x'_M\equiv-5\cdot3^{-1}$, a single residue for
all admissible $M$. $f(x'_M)+1=2^M$ with $M\ge m$ gives
$f(x'_M)\equiv-1$. Finally
$x'_M=(2^{\,M+2}-5)/3<(2^{\,M+2}-4)/3=\tfrac43(2^{\,M}-1)$. $\;\blacksquare$

**Consequence.** Applying $(\ast)$ to the step $x'_M\to 2^M-1$:

$$
g(-1,\,M)\;\le\;g(r^\star,\,1)\;+\;\log_2\frac{x'_M}{2^M-1}
\;<\;g(r^\star,\,1)+\log_2\tfrac43
\qquad\text{for every odd }M\ge\max(m,3). \tag{2}
$$

The right side is a constant independent of $M$.

---

## 3. The theorem

**Theorem (no local-coordinate potential).** For every $m\ge0$ and every
function $g$, the potential $P(x)=\log_2x+g(x\bmod2^m,\ \tau(x))$ fails
$(\ast)$: there exists an odd $x>1$ with $P(f(x))>P(x)$.

*Proof.* If $(\ast)$ held, the single real sequence
$M\mapsto g(-1,M)$ would satisfy both (1) — growth at least
$\log_2\frac32$ per unit $M$ — and (2) — a uniform upper bound. For odd
$M>t_0+\big(g(r^\star,1)+\log_2\frac43-g(-1,t_0)\big)/\log_2\frac32$ the
two are inconsistent. $\;\blacksquare$

**Remark (relation to RNG1).** At $m=0$ this is RNG1 verbatim. Unlike
RNG1, whose contradiction closes in the finite window $\tau\in[3,7]$, the
generalized proof needs $M\to\infty$: the burn constraints only bind on the
residue $-1$ for $t>m$, and the two unknown constants $g(-1,t_0)$,
$g(r^\star,1)$ cannot be compared except through the recharge itself. The
contradiction is nonetheless fully explicit once those two values are
named.

---

## 4. Reading

The pair $(x\bmod2^m,\tau(x))$ determines the bottom
$\max(m,\tau(x)+1)$ bits of $x$: the trailing-one run, the terminating $0$,
and the fixed window above it. So the theorem says:

> No correction to $\log_2x$ computed from any fixed-width low-bit window
> of $x$ together with the (unbounded) trailing-one count can be monotone
> along $f$.

The obstruction is the residue-frozen pair of families: burn members
$3^{\,j}2^{\,t}-1$ and recharge images $2^M-1$ all inhabit residue $-1$,
and recharge sources inhabit the single residue $r^\star$, however large
the numbers grow. Local coordinates cannot see whether trailing-one fuel is
*hot* (mid-burn, value rising at ratio $\frac32$) or *cold* (freshly
recharged at cost $\to\log_2\frac43$). Any working potential must
distinguish these using unbounded-window information — for example the
position of the fuel block relative to the full binary length, which is
exactly the quantity the per-rail $\Delta z$ program tracks.

**Not covered (open):** corrections using high-end information (leading
bits / fractional part of $\log_2x$), mixed low–high windows, or
multi-step (path-dependent) potentials. The theorem constrains one-step
scalar potentials with low-end local coordinates only.

---

## Appendix — Verification

`scripts/verify_no_local_potential.py` checks, with exact integer arithmetic:

* **Lemma 1:** for $m\le12$, $t\le40$, $j\le25$: $\tau$, both residues
  $\equiv-1\bmod2^m$, the exact image $3^{\,j+1}2^{\,t-1}-1$, and the exact
  ratio $\frac32+\frac1{2x}$.
* **Lemma 2:** for $m\le12$ and odd $M\le99$: $f(x'_M)=2^M-1$ exactly,
  $\tau(x'_M)=1$, $x'_M\bmod2^m=r^\star$ constant across $M$, and
  $x'_M<\frac43(2^M-1)$.
* **Theorem:** for sample $m$, the explicit inconsistency of (1) and (2)
  as a linear-feasibility check over the finitely many constrained values
  $g(-1,t_0..M)$, $g(r^\star,1)$.

```bash
python3 scripts/verify_no_local_potential.py   # prints PASS for every claim above
```
