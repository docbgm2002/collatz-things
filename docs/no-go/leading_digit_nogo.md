# Leading Digits Do Not Survive: the Iterated Shadow

**Building on:** `shadow_certificate.md` (SH1, Lemma S),
`tower_theorem.md` (detectors)
**Status:** Theorem F is proved here; machine-checked in
`scripts/verify_leading_digit.py` (exact arithmetic for all identities and a
concrete instance of the Dirichlet step). It moves the boundary of the
one-step no-go program from "leading digits" to "the quantized full
logarithm". Not a proof of the Collatz conjecture.
**License:** CC-BY 4.0

---

## 1. Statement

For odd $y$ let $\mathrm{LD}_j(y)=\lfloor y/2^{\,\mathrm{len}(y)-j}\rfloor$
(the top $j$ bits). `shadow_certificate.md` observed that a coordinate
survives the $-5$ shadow only by separating $x$ from
$f^2(x)=\tfrac98x+\tfrac58$, and that $\mathrm{LD}_j$ does separate them
(the ratio $\tfrac98$ shifts leading digits). Iterating the shadow
removes this last refuge:

**Theorem F.** For every $m,j,d\ge0$ and every $g$,

$$
\Phi(x)=\log_2x+g\bigl(x\bmod2^m,\ \tau(x),\ \mathrm{LD}_j(x),\
\lambda_1(x),\dots,\lambda_d(x)\bigr)
$$

is not nonincreasing along $f$ on odd $x>1$.

## 2. Proof

**Iterated shadow (exact).** For $x\equiv-5\pmod{2^{3a+c}}$ with $c\ge5$,
Lemma S applies $a$ times (each period consumes three bits of shadow
depth), the itinerary alternating $-5,-7$ residues with $\tau$-pattern
$2,1$ and every detector $\bot$ throughout, giving the exact closed form

$$
f^{2a}(x)\;=\;\frac{9^{\,a}x+5\,(9^{\,a}-8^{\,a})}{8^{\,a}}
\;=\;\Bigl(\tfrac98\Bigr)^{\!a}x\,(1+\delta),\qquad 0<\delta<\tfrac5x .
$$

**Dirichlet step.** $\beta=\log_2\tfrac98$ is irrational
($2^{\,p+3q}=3^{\,2q}$ is impossible), so for every $\varepsilon>0$
there is $a\ge1$ with $\|a\beta\|<\varepsilon$ (distance to the nearest
integer $P$); note $a\beta>0$ regardless of the side of the
approximation.

**Assembly.** Fix $m,j,d$; choose $a$ with
$\|a\beta\|<2^{-j-3}$ and set $N=3a+\max(m,5)+j+8$. Since
$\log_2(2^Nw-5)\approx N+\log_2w$ and $w$ is a free positive integer,
choose $w$ so that the fractional part of $\log_2x$, $x=2^Nw-5$, lies at
distance $>2^{-j-2}$ from every breakpoint of $\mathrm{LD}_j$ (the
points $\log_2(D/2^{\,j-1})$, $D=2^{\,j-1},\dots,2^{\,j}-1$), and $N$
large enough that $\delta<2^{-j-4}/x^0$ — concretely $x>2^{\,j+7}$
suffices for $\log_2(1+\delta)<2^{-j-3}$. Then

$$
\log_2 f^{2a}(x)=\log_2x+P\pm\|a\beta\|+\log_2(1+\delta),
$$

so the fractional part of $\log_2f^{2a}(x)$ stays inside the same
$\mathrm{LD}_j$-cell: $\mathrm{LD}_j(f^{2a}(x))=\mathrm{LD}_j(x)$. All
other coordinates close by the iterated shadow ($x\equiv f^{2a}(x)
\equiv-5\pmod{2^m}$, $\tau=2$ on both, detectors $\bot$). Telescoping
monotonicity over the $2a$-step walk:

$$
0\;\ge\;\Phi\bigl(f^{2a}(x)\bigr)-\Phi(x)
\;=\;\log_2\frac{f^{2a}(x)}{x}\;=\;a\beta+\log_2(1+\delta)\;>\;0 .
\qquad\blacksquare
$$

A concrete instance ($j=4$): $a=53$ gives $53\beta=9.00603\ldots$,
fractional part $0.0060<2^{-7}$; the verifier realizes the full
$106$-step walk in exact integers with top-$4$ bits $1011\to1011$ and
value gain $2^{9.006}$.

## 3. The boundary, again

What survives Theorem F must separate $x$ from $f^{2a}(x)$ for *every*
good approximation $a$ — i.e. it must see $\log_2x$ to a precision
finer than every $\|a\beta\|$, integer and fractional parts jointly.
The remaining one-step class is therefore

$$
\Phi(x)=\log_2x+g\bigl(\lfloor2^{\,j}\log_2x\rfloor,\ \tau(x),\
x\bmod2^m,\dots\bigr),
$$

the **quantized full logarithm**. Here a closed coordinate walk needs
total gain in $(0,2^{-j})$; each shadow period gains $\beta>2^{-j}$ for
$j\ge3$, so pure shadows cannot close it, and any certificate must mix
gain and loss segments — a connectivity question in the coordinate
graph, minable per $(m,j)$ but with no all-$(m,j)$ construction known.
Note the class is enormous: as $j\to\infty$ it approaches arbitrary
corrections, for which nonincreasing potentials exist iff the
conjecture-level dynamics permit them; so the program has, plausibly,
reached the point where further no-go progress and the conjecture
itself begin to interact.

## Appendix — Verification

`scripts/verify_leading_digit.py`: the iterated closed form
$8^af^{2a}(x)=9^ax+5(9^a-8^a)$ with full itinerary (residues, $\tau$,
detector $\bot$ at levels $1..3$ on all $2a{+}1$ nodes) for the
concrete instance $(m,j,a)=(6,4,53)$ at shadow depth $N=179$;
$\mathrm{LD}_4$ closure; strict value gain; and the irrationality
argument's arithmetic ($2^{p+3q}=3^{2q}$ has no solutions, checked as
$v_3$ of both sides for a range and stated in general).

## Proposed ledger row

| ID | Claim | Status | Source | Verification |
|---|---|---|---|---|
| SH2 | No potential $\log_2x+g(x\bmod2^m,\tau,\mathrm{LD}_j,\lambda_1..\lambda_d)$ is nonincreasing, any $m,j,d$ | Proved here (iterated shadow + Dirichlet) | `leading_digit_nogo.md` | `scripts/verify_leading_digit.py` |
