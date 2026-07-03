# No-Go for Fuel-Fraction Potentials (Certificate Proof)

**Building on:** `tower_theorem.md` (NLPD), `scripts/verify_nogo_certificate.py`
(certificate method), `recharge_nogo.md`
**Status:** Theorem D is proved here by an explicit finite certificate,
machine-verified in exact rational arithmetic (`scripts/verify_fuel_fraction.py`).
It resolves, negatively, the first open question of the manuscript's
boundary section. Not a proof of the Collatz conjecture.
**License:** CC-BY 4.0

---

## 1. Theorem D

Write $\mathrm{len}(x)$ for the bit length of $x$. Note that
$\bigl(\tau(x),\mathrm{len}(x)\bigr)$ determines the fuel fraction
$\tau/\log_2x$ to within the dyadic ambiguity of $\mathrm{len}$, so this
is the natural "mixed low/high-end" coordinate pair that the
frozen-family method of NLP1--NLPD cannot reach ($\mathrm{len}$ is never
frozen along a burn).

**Theorem D.** For every function
$g:\Z_{\ge1}\times\Z_{\ge1}\to\R$, the potential
$\Phi(x)=\log_2x+g\bigl(\tau(x),\mathrm{len}(x)\bigr)$ is not
nonincreasing along $f$ on odd $x>1$.

*Proof.* The eleven odd integers

$$
W=\{524543,\,524415,\,524351,\,524319,\,524303,\,524295,\,524291,\,
707241,\,526335,\,525311,\,524799\}
$$

have the property that the coordinate pairs
$\bigl(\tau,\mathrm{len}\bigr)$ of $x$ and $f(x)$, taken over $x\in W$ in
the listed order, form a single closed directed cycle:

$$
(8,20)\to(7,20)\to\cdots\to(2,20)\to(1,20)\to(11,20)\to(10,20)\to(9,20)\to(8,20),
$$

and the product of the value ratios is, exactly,

$$
\prod_{x\in W}\frac{f(x)}{x}
=\frac{13531448979384131435041387233644378449102725347401170844161191}
{312872567927064948647949831675046943888344341578974786509435}
\;>\;1
\qquad(=2^{\,5.4346\ldots}).
$$

If $\Phi$ were nonincreasing, summing
$g(\text{coords}(f(x)))-g(\text{coords}(x))\le-\log_2\!\frac{f(x)}{x}$
over the cycle would give $0\le-\log_2\prod_{x\in W}\frac{f(x)}{x}<0$.
$\;\blacksquare$

**Structure of the certificate.** Seven witnesses are of the exact form
$2^{19}+2^{t}-1$ ($t=8,\dots,2$): burn steps whose ratio exceeds
$\tfrac32$ while the value remains inside the dyadic window
$[2^{19},2^{20})$, so $\mathrm{len}$ is constant --- the coordinate
$\mathrm{len}$ resolves $\log_2x$ only to within $1$, and the entire
burn/recharge scissors fits inside a single dyadic interval. The eighth
witness $707241\mapsto530431$ is an in-window recharge ($\tau:1\to11$,
ratio $\to\tfrac34$), and three further burn edges close the loop. The
certificate was mined by Bellman--Ford over the coordinate graph of real
steps $x\le10^6$ and is verified exactly; but its origin is irrelevant to
the proof, which is the displayed finite computation.

**Corollary (triple window at $m=4$).** The two witnesses
$524315$ and $699065$ form a closed $2$-cycle in
$\bigl(\tau,\mathrm{len},\,x\bmod16\bigr)$-coordinates with ratio product
$2^{\,0.1699\ldots}>1$; hence no
$\log_2x+g\bigl(\tau,\mathrm{len},x\bmod16\bigr)$ is nonincreasing
either.

## 2. Scope, and the sharpened open question

Theorem D is unconditional and needs no uniformity device: unlike the
$(x\bmod2^m,\tau)$ classes --- where the window parameter $m$ forces the
burn/recharge \emph{families} of NLP1--NLPD --- the pair
$(\tau,\mathrm{len})$ is one fixed coordinate system, so a single finite
cycle refutes every $g$ at once.

What remains open is the fully combined class,
$g\bigl(x\bmod2^m,\ \tau,\ \mathrm{len}\bigr)$ \emph{for all $m$
simultaneously}: per-$m$ certificates are minable (the corollary is
$m=4$), but an all-$m$ theorem again needs designed families. A promising
route, recorded for future work: the fixed-length burn family
$x=2^{n}+2^{t}-1$ is residue-frozen at $-1\bmod2^m$ for
$m<t<t+1\le n-1$ (both endpoints), giving growth of
$g(-1,t,n{+}1)$ in $t$ at fixed length and fixed residue; what is missing
is an in-window recharge family with frozen source coordinates to cap it.
The mined witness $707241\mapsto530431$ shows such steps exist; a
parametric family has not yet been constructed.

## Appendix — Verification

`scripts/verify_fuel_fraction.py` re-derives every ingredient from scratch
(no imports from other notes): the coordinates of all $11+2$ witnesses
and their images, cycle closure, and both exact rational products.
It also confirms the structural claims: the seven burn witnesses equal
$2^{19}+2^t-1$, their steps stay in the dyadic window, and the
fixed-length burn family's residue freeze
($2^n+2^t-1\equiv-1\bmod2^m$ for $t\ge m$, image likewise for
$t-1\ge m$) over wide ranges.

## Proposed ledger row

| ID | Claim | Status | Source | Verification |
|---|---|---|---|---|
| FFN1 | No potential $\log_2x+g(\tau(x),\mathrm{len}(x))$ is nonincreasing (and the triple with $x\bmod16$ likewise) | Proved here (explicit finite certificate) | `fuel_fraction_nogo.md` | `scripts/verify_fuel_fraction.py` |
