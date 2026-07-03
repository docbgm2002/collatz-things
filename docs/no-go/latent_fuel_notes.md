# Latent Fuel: Periodic Normal Forms Above the Mersenne Spine

**Building on:** `recharge_nogo.md` (Lemma 2), `no_local_potential.md`,
`../repunit/repunit_normal_form_notes.md`
**Status:** Exploratory, EXCEPT Lemmas L1–L2 which are exact and
machine-verified. The hierarchy conjecture and the NLP-hierarchy conjecture
are open and clearly labelled. Not part of the proved-results track.
**License:** CC-BY 4.0

---

## 1. Two exact identities

The recharge source of `recharge_nogo.md` Lemma 2 has an exact binary
normal form, and so does its natural preimage family.

**Lemma L1 (level-1 fuel is alternation).** For $k\ge1$ and $M=2k+3$,

$$
x'_M=\frac{2^{M+2}-5}{3}=\big(\texttt{10}\big)^{k}\,\texttt{1001}
\;\text{ in binary},\qquad f(x'_M)=2^M-1 .
$$

*Proof.* The word $(\texttt{10})^k$ has value $2(4^k-1)/3$, so the full
word has value $2^4\cdot\tfrac{2(4^k-1)}{3}+9=\tfrac{32\cdot4^k-5}{3}
=\tfrac{2^{2k+5}-5}{3}=x'_{2k+3}$. The image is
`recharge_nogo.md` Lemma 2. $\;\blacksquare$

**Lemma L2 (level-2 fuel is period-6).** For $k\ge1$ and $M=6k+1$,

$$
y_k=\frac{2^{6k+5}-23}{9}=\big(\texttt{111000}\big)^{k}\,\texttt{01}
\;\text{ in binary},\qquad
f(y_k)=x'_{M},\qquad f^{2}(y_k)=2^{M}-1 .
$$

*Proof.* $(\texttt{111000})^k$ has value $56\cdot\tfrac{64^k-1}{63}
=\tfrac{8(64^k-1)}{9}$, so the full word is
$4\cdot\tfrac{8(64^k-1)}{9}+1=\tfrac{32\cdot64^k-23}{9}=y_k$. Then
$3y_k+1=\tfrac{2^{6k+5}-23+3\cdot... }{3}$ — directly:
$3y_k+1=\tfrac{32\cdot64^k-23}{3}+1=\tfrac{32\cdot64^k-20}{3}
=4\cdot\tfrac{8\cdot64^k-5}{3}=4\cdot\tfrac{2^{6k+3}-5}{3}=4\,x'_{6k+1}$,
with $x'_{6k+1}$ odd, so $v_2=2$ and $f(y_k)=x'_{6k+1}$; Lemma L1 gives
$f^2(y_k)=2^{6k+1}-1$. $\;\blacksquare$

So the two-step ancestry of the Mersenne spine (for $M\equiv1\bmod 6$) is a
chain of **exact periodic binary words**:

$$
(\texttt{111000})^{k}\texttt{01}
\;\xrightarrow{\;f,\;\times\frac34\;}\;
(\texttt{10})^{3k+1}\texttt{1001}
\;\xrightarrow{\;f,\;\times\frac34\;}\;
\texttt{1}^{\,6k+1}
\;\xrightarrow{\;\text{burn},\;\times(\frac32)^{6k}\;}\;\cdots
$$

Fuel that looks absent to $\tau$ (both ancestors have $\tau\le2$) is stored
as periodicity: period 2 one step out, period 6 two steps out. Note the
obstruction to continuing naively: $x'_M\equiv0\pmod 3$ for
$M\equiv3\pmod 6$ (no preimage at all), so the hierarchy selects residues —
the ancestry filters $M$ through arithmetic progressions.

## 2. Conjectures (open)

**Hierarchy conjecture.** For each depth $d\ge1$ there is a period
$\pi_d$ and an exact family of words $w_d^{(k)}$ of the form
(period-$\pi_d$ block)$^k\cdot$(bounded suffix) with
$f^{d}(w_d^{(k)})=2^{M(d,k)}-1$, $M(d,k)\to\infty$, and per-step value
ratio $\to\tfrac34$. (L1, L2 are $d=1,2$; candidate mechanism: the
period multiplies by the multiplicative order structure of $2$ modulo
$3^d$, suggesting $\pi_d = 2\cdot3^{d-1}$.)

**NLP-hierarchy conjecture.** For any finite $d$, augmenting the
coordinates of `no_local_potential.md` with the run-lengths of the level
$1..d$ periodic suffixes still admits no nonincreasing potential
$\log_2x+g(\cdot)$: the depth-$(d{+}1)$ family is frozen in all coordinates
up to level $d$ (its own periodicity is invisible to shallower run-length
detectors), and the scissors reclose with the burn liability propagated
through $d{+}1$ steps of $\tfrac34$-cost. If true for all $d$, the moral of
NLP1 sharpens: *no finite tower of suffix-periodicity detectors suffices;
a monotone potential must read unboundedly deep structure* — consistent
with the whole-word objects ($\Delta z$ per rail, repunit normal forms)
being the right coordinates.

## 3. Immediate checkable steps

1. Compute the $d=3$ family: solve $f(z)=y_k$ over $z$ odd and test for a
   periodic normal form of period $18$ (`scripts/explore_latent_fuel.py` scaffolds
   this).
2. If $d=3$ is periodic, attempt the general lemma by the same telescoping
   geometric-series calculation as L1/L2 (the proofs are one-line once the
   word is guessed).
3. Attempt NLP-hierarchy at $d=1$: add the alternation run-length
   $\lambda(x)$ to the NLP1 coordinates and check whether the frozen-family
   argument closes. This is the first genuinely new no-go beyond NLP1.

## Appendix — Verification

`scripts/explore_latent_fuel.py` verifies L1 and L2 exactly for $k\le60$
(word value, image chain, $\tau$ values, value ratios), reports the
mod-3 filtering of $x'_M$, and searches for the $d=3$ family.
Exploratory output beyond L1/L2 is evidence, not proof.
