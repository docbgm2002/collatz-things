# Recharge No-Go and the Tight Mersenne Burn Ledger

**Building on:** `Mod8_Rail_Descent.md`, `Block_Fracture_Lemma.md`, archived exploratory note `archive/potential_attack_notes.md`
**Status:** Part I is an exact *negative* result; Part II is an exact closed-form ledger. Neither is a proof of the Collatz conjecture — Part II ends at the open residual it cannot close.
**License:** CC-BY 4.0

---

## Abstract

The archived `archive/potential_attack_notes.md` observed that the single-term potential $\log_2 x + c\,\tau(x)$, with $\tau(x)=v_2(x+1)$ the trailing-one count, fails because of *recharge*. Here we sharpen that observation in two directions.

**Part I (No-Go).** *No* potential of the form $P(x)=\log_2 x + g(\tau(x))$, with $g$ **any** function, can be a global Collatz supermartingale. The burn side (rail-7 / Mersenne erosion) forces $g$ to climb with slope $\ge \log_2\frac32$ per unit of fuel; the recharge side (landing on a Mersenne number $2^m-1$) permits $g$ to climb with slope $\to 0$. The two are inconsistent already over $\tau\in[3,7]$.

**Part II (Tight ledger).** For the Mersenne spine $M_n=2^n-1$ the burn phase has the exact closed form $x_j=3^j2^{\,n-j}-1$, and the *critical* potential $\Phi(x)=\log_2 x+\log_2\!\frac32\cdot\tau(x)$ rises by a total of at most $\log_2\frac{10}{9}$ over the entire (arbitrarily long) burn. So the burn's fuel price is **exactly** $\log_2\frac32$, approached from above — the spine pins the lower bound that Part I's recharge contradicts.

All identities are checked with exact integer / rational arithmetic in `verify_recharge_nogo.py`.

---

## 0. Setup

For odd $x$, the odd-step map is $f(x)=(3x+1)/2^{v_2(3x+1)}$, and the **trailing-one fuel** is

$$
\tau(x)=v_2(x+1)=\#\{\text{trailing 1-bits of }x\}.
$$

We study scalar potentials $P(x)=\log_2 x + g(\tau(x))$ and ask whether any choice of $g$ makes $P$ nonincreasing along $f$ (a supermartingale); such a $P$, bounded below with $g$ bounded, would force descent.

---

## Part I — The Recharge No-Go

### Lemma 1 (Burn slope)

Let $x$ be odd with $\tau(x)=t\ge 2$; write $x=2^t m-1$ with $m$ odd. Then $v_2(3x+1)=1$ and

$$
f(x)=\frac{3x+1}{2}=3\cdot2^{\,t-1}m-1,\qquad \tau(f(x))=t-1,\qquad
\frac{f(x)}{x}=\frac32+\frac1{2x}>\frac32 .
$$

*Proof.* $3x+1=3(2^t m-1)+1=3\cdot2^t m-2=2\,(3\cdot2^{\,t-1}m-1)$, and $3\cdot2^{\,t-1}m-1$ is odd because $t\ge 2$; so $v_2=1$ and $f(x)=3\cdot2^{\,t-1}m-1=2^{\,t-1}(3m)-1$ with $3m$ odd, giving $\tau(f(x))=t-1$. Finally
$\tfrac{f(x)}{x}-\tfrac32=\tfrac{2(3\cdot2^{t-1}m-1)-3(2^t m-1)}{2x}=\tfrac{1}{2x}$. $\;\blacksquare$

**Consequence.** If $P(f(x))\le P(x)$ on this step then $\log_2\!\frac{f(x)}{x}\le g(t)-g(t-1)$, so

$$
g(t)-g(t-1)\;\ge\;\log_2\!\Big(\tfrac32+\tfrac1{2x}\Big)\;>\;\log_2\tfrac32\qquad(\forall t\ge 2).
$$

Taking $x\to\infty$ at each level, $g(t)-g(t-1)\ge\log_2\frac32$ is **necessary**. In particular $g$ must be strictly increasing.

### Lemma 2 (Recharge family — slope $\to 0$)

For odd $m\ge 3$ let $x_m=\dfrac{2^{\,m+2}-5}{3}$ (an integer iff $m$ is odd). Then

$$
3x_m+1=2^{\,m+2}-4=4\,(2^m-1),\qquad f(x_m)=2^m-1,\qquad \tau(f(x_m))=m,
$$

and $\dfrac{f(x_m)}{x_m}=\dfrac{3(2^m-1)}{2^{\,m+2}-5}\to\dfrac34$. The recharge jumps $\tau$ to $m$ while the value falls by only $\to\log_2\frac43$, so the **allowed** per-unit climb $(-\Delta\log_2)/\Delta\tau\to 0$.

*Proof.* Direct: $3x_m+1=2^{m+2}-4=4(2^m-1)$ with $2^m-1$ odd gives $v_2=2$ and $f(x_m)=2^m-1$. The ratio limit is immediate. $\;\blacksquare$

Concretely $m=7$ gives $x_7=169\xrightarrow{f}127=2^7-1$: $\tau$ jumps $1\to 7$ while the value drops by only $\log_2\frac{169}{127}\approx 0.412$.

### Theorem 1 (No-Go for any $g$)

There is no function $g$ for which $P(x)=\log_2 x+g(\tau(x))$ satisfies $P(f(x))\le P(x)$ for all odd $x>1$.

*Proof.* Suppose such a $g$ exists. By Lemma 1 it is increasing with $g(t)-g(t-1)\ge\log_2\frac32$ for every $t\ge 2$, so

$$
g(7)-g(3)=\sum_{t=4}^{7}\big(g(t)-g(t-1)\big)\;\ge\;4\log_2\tfrac32\;\approx\;2.340 .
$$

But the single step $169\to127=2^7-1$ (Lemma 2, $m=7$, with $\tau(169)=1$) forces $g(7)-g(1)\le\log_2\frac{169}{127}\approx0.412$; and since $g$ is increasing, $g(3)\ge g(1)$, hence

$$
g(7)-g(3)\;\le\;g(7)-g(1)\;\le\;0.412 .
$$

$2.340>0.412$ is a contradiction. $\;\blacksquare$

The gap is not an accident of $\tau\in[3,7]$: Lemma 2 makes the recharge bound $\to 0$ for large $m$, while Lemma 1 keeps the burn requirement at $\log_2\frac32$, so the inconsistency widens without bound. **A working potential must see more than the trailing-one count** — it must distinguish freshly-recharged ("cold") fuel from fuel positioned for an imminent burn.

---

## Part II — The Tight Mersenne Burn Ledger

The burn of Lemma 1, iterated, is the worst case for the No-Go. On the Mersenne spine it has an exact closed form, which lets us price it precisely.

### Lemma 3 (Burn closed form)

For $M_n=2^n-1$ $(n\ge2)$ and $j=0,1,\dots,n-1$,

$$
x_j=3^{\,j}\,2^{\,n-j}-1,\qquad \tau(x_j)=n-j,
$$

and for $0\le j\le n-2$ the odd-step is the affine map

$$
x_{j+1}=f(x_j)=\frac{3x_j+1}{2}=\frac32x_j+\frac12,\qquad
\frac{x_{j+1}}{x_j}=\frac32+\frac1{2x_j}.
$$

*Proof.* Induction with $x_0=2^n-1$. At step $j$, $x_j=2^{\,n-j}(3^{\,j})-1$ has $\tau=n-j$ (as $3^j$ is odd); since $n-j\ge2$ while $j\le n-2$, Lemma 1 applies and $f(x_j)=3\cdot2^{\,n-j-1}3^{\,j}-1=3^{\,j+1}2^{\,n-(j+1)}-1=x_{j+1}$. $\;\blacksquare$

The burn ends at $x_{n-1}=2\cdot3^{\,n-1}-1$ with $\tau=1$. (For $n=2d+3$ this is the rail-7 escape value $18\cdot9^{d}-1$ of `Mod8_Rail_Descent.md`, so the two analyses agree.)

### Theorem 2 (Critical potential / tight ledger)

Let $\Phi(x)=\log_2 x+\log_2\!\frac32\cdot\tau(x)$. Along the burn,

$$
\Phi(x_{j+1})-\Phi(x_j)
=\log_2\frac{x_{j+1}}{x_j}-\log_2\tfrac32
=\log_2\!\Big(1+\frac1{3x_j}\Big)\;>\;0,
$$

so $\Phi$ is strictly increasing, but its **total** rise over the entire burn is bounded:

$$
\Phi(x_{n-1})-\Phi(x_0)=S_n:=\sum_{j=0}^{n-2}\log_2\!\Big(1+\frac1{3x_j}\Big),
\qquad 0<S_n<\frac{2^{\,1-n}}{\ln 2},
$$

and the exact supremum $\sup_n S_n=S_2=\log_2\frac{10}{9}\approx0.152$. Equivalently

$$
\log_2\frac{x_{n-1}}{x_0}=(n-1)\log_2\tfrac32+S_n,\qquad
c^\star(n):=\frac{\log_2(x_{n-1}/x_0)}{\,n-1\,}\;\downarrow\;\log_2\tfrac32 .
$$

*Proof.* The increment formula is Lemma 3 plus $\log_2(\tfrac32+\tfrac1{2x})-\log_2\tfrac32=\log_2(1+\tfrac1{3x})$; the sum telescopes. Each term is positive. For the bound, $\log_2(1+u)\le u/\ln2$ and $x_j=3^{\,j}2^{\,n-j}-1\ge 3^{\,j}2^{\,n-j-1}$ give

$$
S_n\le\frac1{\ln2}\sum_{j=0}^{n-2}\frac1{3x_j}
\le\frac1{3\ln2}\sum_{j\ge0}\frac{2}{3^{\,j}2^{\,n-j}}
=\frac{2^{\,1-n}}{3\ln2}\sum_{j\ge0}\Big(\tfrac23\Big)^{\!j}\!\cdot\!\frac{3}{2}
=\frac{2^{\,1-n}}{\ln 2}.
$$

So $S_n\to0$ geometrically; the precise supremum $S_2=\log_2\frac{10}{9}$ (single term, $x_0=3$) is a finite check. $\;\blacksquare$

**Reading.** At the critical price $c=\log_2\frac32$ the burn neither gains nor loses $\Phi$ beyond a *uniformly bounded* total $S_n<\log_2\frac{10}{9}$, however long the burn runs: $\Phi$ is an **almost-invariant** of the Mersenne spine. This is exactly the lower edge Part I straddles — the spine pins the burn requirement at $\log_2\frac32$, and recharge (Lemma 2) demands strictly less, which is why no scalar $g$ can hold.

### Lemma 4 (Escape step, exact)

From the peak $x_{n-1}=2\cdot3^{\,n-1}-1$,

$$
3x_{n-1}+1=2\,(3^{\,n}-1),\qquad
f(x_{n-1})=\frac{3^{\,n}-1}{2^{\,v_2(3^{\,n}-1)}}.
$$

By Lifting-the-Exponent, $v_2(3^n-1)=1$ for odd $n$ and $=2+v_2(n)$ for even $n$. Thus the **even rail-7 spine** ($k=n-3$ even, i.e. $n$ odd) escapes to $f(x_{n-1})=\dfrac{3^{\,n}-1}{2}$ with $\tau=1$ and step ratio $\to\frac34$. $\;\blacksquare$

### The open residual (stated, not closed)

From Theorem 2, $x_{n-1}=x_0\cdot(3/2)^{\,n-1}\,2^{S_n}$, so

$$
\frac{x_{n-1}}{x_0}=\Big(\tfrac32\Big)^{\!n-1}2^{S_n}\longrightarrow\infty .
$$

The Mersenne number **grows** by $(3/2)^{n-1}$ over its burn; the closed-form phase does not return it below $x_0$. After escape it sits near $3^n/2$ with $\tau=1$, and whether the subsequent (non-closed-form) trajectory falls below $x_0$ is precisely the open question — equivalent to Collatz on this orbit. We claim none of it.

What the ledger *does* deliver: the spine's burn is exactly priced ($\log_2\frac32$ per unit fuel, tight to a bounded total), so any future descent proof for the spine must extract its margin **after** escape, from the $\to\frac34$ steps Lemma 4 begins — not from a value/fuel trade during the burn, which is provably margin-free.

---

## What this rules out, and what it suggests

* **Ruled out (Theorem 1):** every potential $\log_2 x+g(\tau)$, for *any* $g$ — not merely the linear one tried in `archive/potential_attack_notes.md`.
* **Suggested:** a potential needs a second coordinate beyond $\tau$ — a "phase" distinguishing cold fuel (just recharged, as in Lemma 2) from hot fuel (about to burn, as in Lemma 3). Equivalently, the paired-macro program of `archive/potential_attack_notes.md §5`: charge each recharge against the burst it later feeds, and ask whether the pair has net drift below $1$.
* **Where the margin lives:** Theorem 2 says it is *not* in the burn (margin-free at $c=\log_2\frac32$). For the spine it can only come from the post-escape $\frac34$-steps of Lemma 4 — a concrete target for the next note.

---

## Appendix — Verification

`verify_recharge_nogo.py` checks, with exact integer / rational arithmetic:

* **Lemma 1:** $\tau(x)=t\ge2\Rightarrow v_2(3x+1)=1$, $\tau(f(x))=t-1$, ratio $=\frac32+\frac1{2x}$ (exact `Fraction`).
* **Lemma 2:** $x_m=(2^{m+2}-5)/3\xrightarrow{f}2^m-1$ for odd $m\le 99$; allowed slope strictly decreasing to $0$.
* **Theorem 1:** the explicit $[3,7]$ contradiction $4\log_2\frac32 > \log_2\frac{169}{127}$.
* **Lemma 3:** $x_j=3^j2^{\,n-j}-1$, $\tau=n-j$, exact per-step ratio, for $n=2..200$.
* **Theorem 2:** $S_n\in(0,\log_2\frac{10}{9}]$ and $c^\star(n)\downarrow\log_2\frac32$ (summed with `log1p` for accuracy past float resolution).
* **Lemma 4:** $f(\text{peak})=(3^n-1)/2^{v_2(3^n-1)}$ exact; $\tau=1$ for odd $n$; peak/$x_0\gg1$ (residual open).

Run:

```bash
python3 verify_recharge_nogo.py     # prints PASS for every claim above
```
