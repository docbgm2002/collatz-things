# Shadow Certificates: the Master No-Go Theorem

**Building on:** `fuel_fraction_nogo.md` (certificate method),
`tower_theorem.md` (detector definitions), `../density-cycles/cycle_reduction.md` (CYC1),
`recharge_nogo.md`
**Status:** Theorem SH1 is proved here; it strictly subsumes, with a
half-page proof, the impossibility statements NLP1, NLP2, NLPD, FFN1, and
resolves the all-$m$ triple question of `fuel_fraction_nogo.md` §2. The
earlier notes retain their structural content (the tower, the exact burn
ledger, the price mechanism) but are dominated as no-go statements.
Machine-checked in `scripts/verify_shadow.py`. Not a proof of the Collatz
conjecture.
**License:** CC-BY 4.0

---

## 1. The mechanism

The $3x{+}1$ map has the rational (negative-integer) cycle
$-5\mapsto-7\mapsto-5$: $f(-5)=(3\cdot(-5)+1)/2=-7$,
$f(-7)=(3\cdot(-7)+1)/4=-5$. Its multiplier is $3^2/2^3=\tfrac98>1$ —
an **expanding** cycle, which is exactly why it lives at negative
integers (CYC1: $x=c_K/(2^{E_K}-3^K)$ with $2^{E_K}<3^K$). Shadowing it
at positive integers congruent to $-5$ modulo a high power of $2$
reproduces its coordinate itinerary while the value *gains* a factor
$\to\tfrac98$ per period. Every coordinate system that is $2$-adically
local near $-5$ and $-7$ closes the shadow into a cycle — and a closed
coordinate cycle with value gain refutes every correction $g$ at once.

## 2. Theorem SH1

For $N\ge8$ and $k\ge3$ let $w=2^{k-1}+1$ and

$$
x_{N,k}=2^{N}w-5 .
$$

**Lemma S (exact shadow).** With $x=x_{N,k}$:
$v_2(3x+1)=1$ and $f(x)=3\cdot2^{N-1}w-7$;
$v_2(3f(x)+1)=2$ and $f^2(x)=9\cdot2^{N-3}w-5$, so that

$$
8\,f^2(x)=9x+5,\qquad \frac{f^2(x)}{x}=\frac98+\frac{5}{8x}>\frac98 .
$$

Moreover: $\tau(x)=\tau(f^2(x))=2$, $\tau(f(x))=1$;
$x\equiv f^2(x)\equiv-5$ and $f(x)\equiv-7\pmod{2^{\,N-3}}$;
$\mathrm{len}(x)=\mathrm{len}(f^2(x))=N+k$; and every tower detector
$\lambda_d$ (of `tower_theorem.md`) reads $\bot$ on $x$, $f(x)$, and
$f^2(x)$ — since $x\equiv27$, $f(x)\equiv25\pmod{32}$ while every
template is $\equiv9$ ($d{=}1$) or $\equiv1$ ($d{\ge}2$) modulo $32$.

*Proof.* Direct computation:
$3x+1=2(3\cdot2^{N-1}w-7)$ with odd bracket;
$3f(x)+1=4(9\cdot2^{N-3}w-5)$ with odd bracket ($N\ge5$);
$8f^2(x)=9\cdot2^{N}w-40=9x+5$. Fuel:
$x+1=4(2^{N-2}w-1)$, $f(x)+1=6(2^{N-1}w... )$ — explicitly
$f(x)+1=3\cdot2^{N-1}w-6=2\cdot3(2^{N-2}w-1)$ with odd second factor;
$f^2(x)+1=4(9\cdot2^{N-5}w-1)$ ($N\ge8$). Residues are immediate from
the closed forms. Length: $w=2^{k-1}+1$ places $x$ and
$f^2(x)=\tfrac98x+\tfrac58$ in the same dyadic window
$[2^{N+k-1},2^{N+k})$ since $9(2^k+2)<2^{k+4}$. Detectors: templates
$T$ with $\mathrm{bitlen}(T)\ge5$ satisfy $T\equiv\Lambda_d\pmod{32}$
with $\Lambda_1\equiv9$, $\Lambda_{d\ge2}\equiv1$; the smaller
templates ($9$, $225$) are checked directly; $27,25\notin\{9,1\}$
modulo $32$, and matching any template forces the mod-$32$ congruence.
$\;\blacksquare$

**Theorem SH1.** Let $m\ge0$, $d\ge0$, and let
$g$ be *any* real-valued function of
$\bigl(x\bmod2^m,\ \tau(x),\ \mathrm{len}(x),\
\lambda_1(x),\dots,\lambda_d(x)\bigr)$. Then
$\Phi(x)=\log_2x+g(\cdots)$ is not nonincreasing along $f$ on odd
$x>1$.

*Proof.* Take $N\ge\max(m+3,8)$ and any $k\ge3$; write $x=x_{N,k}$. By
Lemma S the coordinate vectors satisfy
$\mathrm{coords}(f^2(x))=\mathrm{coords}(x)$, so the two monotonicity
constraints at $x$ and $f(x)$ sum to
$0\le-\log_2\dfrac{f^2(x)}{x}<-\log_2\dfrac98<0$. $\;\blacksquare$

The smallest member: $x_{8,3}=1275\mapsto1913\mapsto1435$, with
$8\cdot1435=9\cdot1275+5$ and product $\tfrac{287}{255}>1$.

## 3. Consequences and general principle

**Subsumption.** SH1 contains NLP1 ($d=0$, drop len), NLP2 and NLPD
(any $d$), FFN1/Theorem D ($m=0$), and answers the all-$m$ triple
question of `fuel_fraction_nogo.md` §2 affirmatively-negatively — the
"missing in-window recharge family" is unnecessary; the $-5$ shadow
bypasses the entire burn/recharge architecture. The earlier results
retain value as structure (the tower TWR1, the exact ledger of
`recharge_nogo.md` Part II, the price mechanism, the corridor rate),
not as impossibility statements.

**General principle.** Nothing is special about $-5$: *every* expanding
rational cycle of the map — every solution of the cycle equation with
$2^{E}<3^{K}$, e.g. the $K{=}7$ cycle at $-17$ — shadows at positive
integers $\equiv$ (cycle member) mod $2^{N}$ into a closed coordinate
$K$-cycle of value gain $3^{K}/2^{E}>1$, refuting every correction that
is $2$-adically local along the cycle. Expanding negative cycles are
certificate factories against local potentials. (Historical note: the
forward identities Andaloro attaches to $-1$, $-5$, $-17$ — see
`../../BIBLIOGRAPHY_PASS.md` — are the same shadows viewed as orbits.)

**What genuinely survives.** A coordinate defeats the shadow only by
separating $x$ from $f^2(x)=\tfrac98x+\tfrac58$ at arbitrarily high
shadow depth $N$: since they agree on the bottom $N-3$ bits, share
$\tau$, len, and all suffix detectors, the separating information must
come from the *top* of the number — leading digits / the fractional
part of $\log_2x$ (the ratio $\tfrac98$ shifts leading digits). The
sharp boundary of the one-step no-go program is therefore: corrections
using leading-digit information, and multi-step potentials. Both are
open; both now have a precise reason for being the boundary.

## Appendix — Verification

`scripts/verify_shadow.py`: Lemma S in full (orbit identities, $8f^2=9x+5$,
fuel, residues, length closure, detector $\bot$ at levels $1..4$) for
$N\le19$, $k\le6$, exact arithmetic; the explicit smallest certificate;
and the $-17$-cycle shadow spot-check for the general principle.

## Proposed ledger rows

| ID | Claim | Status | Source | Verification |
|---|---|---|---|---|
| SH1 | No potential $\log_2x+g(x\bmod2^m,\tau,\mathrm{len},\lambda_1..\lambda_d)$ is nonincreasing, any $m,d$ | Proved here; subsumes NLP1/NLP2/NLPD/FFN1 as impossibility statements | `shadow_certificate.md` | `scripts/verify_shadow.py` |

**Ledger status changes:** NLP1, NLP2, NLPD, FFN1 → "Proved here;
subsumed by SH1 (retained for structural content / historical proof
path)".
