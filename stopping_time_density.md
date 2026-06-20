# An Explicit Stopping-Time Density for the $3x+1$ Map

**Building on:** `Mod8_Rail_Descent.md`, `recharge_nogo.md`, `mersenne_repunit_reduction.md`, `verify_descent_tree.py`
**Status:** Exact. An elementary, fully machine-checked re-derivation of the Terras (1976) / Everett (1977) density theorem, with an **explicit geometric rate**. It does **not** prove the Collatz conjecture.
**License:** CC-BY 4.0

---

## Abstract

We give a self-contained, elementary proof that *almost every* odd integer descends below itself in a bounded number of odd-steps, with an explicit rate. Define the stopping time $\sigma(x)=\min\{t\ge1: f^{(t)}(x)<x\}$ and the density $D(K)=\operatorname{dens}\{x\text{ odd}:\sigma(x)\le K\}$. Then

$$
\boxed{\;D(K)\;\ge\;1-\rho^{\,K},\qquad \rho=e^{-I(\log_2 3)}=0.94650\ldots\;}
$$

where $I$ is the Cramér (large-deviation) rate of the per-step $2$-adic valuation. The proof has three exact ingredients: an **affine accumulation** with a clean tail bound (§1), a **descent criterion** "$enough$ division $\Rightarrow$ descent" (§2), and the **exact equidistribution** of valuation patterns (§3). Every step is verified in `verify_stopping_density.py`. This is Terras's theorem made explicit and machine-checked; the residual hard core of density $\le\rho^K$ — dominated by the near-Mersenne spine of the companion notes — is exactly what remains, and remains open.

---

## 0. Setup

For odd $x$, $f(x)=(3x+1)/2^{\,v_2(3x+1)}$. Write the orbit $x_0=x$, $x_{i+1}=f(x_i)$, with per-step valuations $e_i=v_2(3x_i+1)\ge1$ and partial sums $E_0=0$, $E_i=e_0+\cdots+e_{i-1}$, $E_K=\sum_{i<K}e_i$. Let $\theta=\log_2 3=1.58496\ldots$ (note $\theta<2$, the mean valuation).

---

## 1. Affine accumulation

**Lemma 1.** For odd $x$ and $K\ge1$,

$$
x_K=\frac{3^K x + c_K}{2^{E_K}},\qquad c_K=\sum_{i=0}^{K-1}3^{\,K-1-i}\,2^{E_i},
\qquad \frac{c_K}{2^{E_K}}<\Big(\tfrac32\Big)^{\!K}.
$$

*Proof.* Induction: $3x_i+1=\dfrac{3^{i+1}x+3c_i+2^{E_i}}{2^{E_i}}$, so dividing by $2^{e_i}$ gives $c_{i+1}=3c_i+2^{E_i}$ with $c_0=0$, hence $c_K=\sum_{i<K}3^{K-1-i}2^{E_i}$. For the bound, with $m=K-1-i$,

$$
\frac{c_K}{2^{E_K}}=\sum_{m=0}^{K-1}\frac{3^{m}}{2^{\,e_{K-1-m}+\cdots+e_{K-1}}}
\le\sum_{m=0}^{K-1}\frac{3^{m}}{2^{\,m+1}}
=\tfrac12\sum_{m=0}^{K-1}\big(\tfrac32\big)^m=\big(\tfrac32\big)^{K}-1,
$$

using that each suffix sum of $m+1$ valuations is $\ge m+1$. $\;\blacksquare$

---

## 2. The descent criterion

**Lemma 2.** If $E_K(x)\ge K\log_2 3 + 1$ (i.e. $2^{E_K}\ge 2\cdot 3^K$) and $x\ge 2(3/2)^K$, then $f^{(K)}(x)<x$; in particular $\sigma(x)\le K$.

*Proof.* By Lemma 1, $x_K=\dfrac{3^Kx}{2^{E_K}}+\dfrac{c_K}{2^{E_K}}\le \dfrac{3^Kx}{2^{E_K}}+\big(\tfrac32\big)^K-1$. With $2^{E_K}\ge2\cdot3^K$ the first term is $\le x/2$; with $x\ge2(3/2)^K$ we have $(3/2)^K\le x/2$, so $x_K\le \tfrac{x}{2}+\tfrac{x}{2}-1=x-1<x$. $\;\blacksquare$

The size condition $x\ge 2(3/2)^K$ excludes only finitely many $x$ for each $K$, so it is invisible to natural density. This criterion is the clean closed form of what the branching prover in `verify_descent_tree.py` was approximating residue-by-residue.

---

## 3. Exact equidistribution of valuations

**Lemma 3.** Fix $K$. Among the $2^{N-1}$ odd residues modulo $2^N$, every $K$-step valuation pattern $(e_0,\dots,e_{K-1})$ of total weight $E\le N-1$ is realized by **exactly** $2^{\,N-1-E}$ residues. Equivalently the per-step valuations are i.i.d. with $\Pr[e_i=j]=2^{-j}$, and $\operatorname{dens}\{x:E_K(x)=E\}=\Pr[\,\textstyle\sum_{i<K}e_i=E\,]$.

*Proof sketch.* For odd $x$, $e_0=v_2(3x+1)=j$ iff $x\equiv 3^{-1}(2^j-1)\pmod{2^{j+1}}$ — one odd class of density $2^{-j}$. On that class $x\mapsto f(x)$ is a bijection onto the odd residues of a lower modulus, so the next valuation is independent with the same law; iterating gives the product measure and the exact count $2^{N-1-E}$ for $E\le N-1$. This is the classical Terras/Everett equidistribution; `verify_stopping_density.py` confirms the exact counts (e.g. mod $2^{16}$, all $3003$ patterns for $K=5$). $\;\blacksquare$

---

## 4. The density theorem with explicit rate

**Theorem.** $D(K)\ge 1-\rho^{K}$ with $\rho=e^{-I(\theta)}$, $\theta=\log_2 3$, where

$$
I(\theta)=\max_{0<u<1}\big[(\theta-1)\ln u+\ln(2-u)\big]
=(\theta-1)\ln u^\star+\ln(2-u^\star),\quad u^\star=\frac{2(\theta-1)}{\theta},
$$

numerically $I(\log_2 3)=0.05498\ldots$ and $\rho=0.94650\ldots$. Hence $D(K)\to1$.

*Proof.* By Lemma 2, $G_K=\{x:E_K(x)\ge K\theta+1\}$ (minus finitely many small $x$) satisfies $G_K\subseteq\{\sigma\le K\}$, so $D(K)\ge\operatorname{dens}(G_K)=1-\operatorname{dens}\{E_K\le\lfloor K\theta\rfloor\}$. By Lemma 3 this density equals $\Pr[E_K\le\lfloor K\theta\rfloor]$ for $E_K=\sum_{i<K}e_i$, a sum of i.i.d. Geometric$(\tfrac12)$ variables of mean $2$. Since $\theta<2$, the Cramér bound for the lower tail gives, with MGF $M(s)=\mathbb E[e^{se}]=\dfrac{e^s/2}{1-e^s/2}$ $(e^s<2)$,

$$
\Pr[E_K\le \theta K]\le \inf_{s\le0}e^{-s\theta K}M(s)^{K}=e^{-K I(\theta)}=\rho^{K},
$$

and the Legendre maximisation (substitute $u=e^s$) yields the stated $I(\theta)$, $u^\star$. As $\lfloor K\theta\rfloor\le K\theta$, $\operatorname{dens}\{E_K\le\lfloor K\theta\rfloor\}\le\rho^K$, so $D(K)\ge1-\rho^K$. $\;\blacksquare$

**Numerically** (verified): the true measured density already runs *above* the bound, e.g. $D(12)\approx0.948\ (\ge1-\rho^{12}=0.483)$, $D(24)\approx0.987\ (\ge0.733)$ — the empirical tail decays like $\approx0.926^K$, faster than the rigorous $\rho=0.9465$, as Cramér is an upper bound.

---

## 5. What is and is not proved

**Proved exactly:** the accumulation and tail bound (L1), the descent criterion (L2), the exact valuation equidistribution (L3, with machine-confirmed counts), and the density lower bound $D(K)\ge1-\rho^K$ with explicit $\rho=0.9465\ldots$ (Theorem).

**Honest attribution:** the qualitative statement $D(K)\to1$ ("almost all integers have finite stopping time") is **Terras 1976 / Everett 1977**. The contribution here is the explicit elementary criterion, the explicit Cramér rate, and end-to-end machine verification — not a new theorem.

**Not proved (the gap to Collatz):** density $1$ is not *all*. The residual $\{\sigma>K\}$ has density $\le\rho^K$ but is **never empty**; that shrinking hard core is dominated by the high-fuel / near-Mersenne numbers that `recharge_nogo.md` and `mersenne_repunit_reduction.md` localise (the spine has $E_K$ deep in the lower tail — it is the worst large-deviation case). Removing the "$K$" — proving $\sigma(x)<\infty$ for *every* $x$ — is exactly the conjecture, and nothing here closes it. The rate is also genuinely slow ($\rho\approx0.95$), so this controls *almost all*, not a uniform bound.

**Supersedes:** the density goal of `verify_descent_tree.py`, whose branching certificate gave a non-monotone proven fraction (dropping to $5/8$ at mod $16$). The present bound $1-\rho^K$ is monotone with an explicit rate.

---

## Appendix — Verification

`verify_stopping_density.py` checks, with exact integer / rational arithmetic:

* **L1:** $x_K=(3^Kx+c_K)/2^{E_K}$, $c_K=\sum 3^{K-1-i}2^{E_i}$, and $c_K/2^{E_K}<(3/2)^K$, for $K\le12$.
* **L2:** $0$ violations of the descent criterion over $8.7\times10^5$ cases.
* **L3:** exact pattern counts $2^{N-1-E}$ for $N\in\{12,14,16\}$.
* **Theorem:** $\Pr[\text{non-good}]\le\rho^K$ (Cramér) and measured $D(K)\ge1-\rho^K$, for $K\le24$.

```bash
python3 verify_stopping_density.py   # prints PASS for every claim above
```
