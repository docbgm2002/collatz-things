# Digit arithmetic of powers of three: the reset-count bridge  [W10]

**Task:** `OPUS5_WIDE_TASKS.md` W10, deliverables (a)–(c) (session 4 of the
recommended order).
**Building on:** `../repunit/rotation_cocycle_rigidity.md` (W11-C, the
bridge), `../repunit/payout_concentration_diffusion.md` §§12–16 (PCD10,
PCD11, PCD13, PCD14), `baker_explicit_constants_audit.md` §4 (the \(A=-7\)
ghost).
**Verifier:** `scripts/verify_digit_bridge_ceiling.py` (6 checks; exact
integer arithmetic, floats only where the quantities compared differ by
factors of \(2^{\Theta(E)}\)).
**Status:** **Avenue closed.** (a) is proved and generalises the W9 identity;
(b) is proved and the bridge is at the *best possible* height; (c) fails, and
the failure is not where W10 expected it.
**License:** CC-BY 4.0

---

## 0. Verdict

W10's plan was: identify the reset/plateau stream with digit windows of
integers of the shape \(3^{R}c\) with \(c\) of bounded height, then apply
Stewart's effective lower bound on the number of nonzero binary digits of
\(3^{R}\). Its stated kill was "kill if the bridge provably requires
unbounded-height \(c\) on every branch class".

> **W10-KILL.** The bridge exists on the plateau branch and its height is
> \(c=1\) — the best possible case, so W10's own kill criterion does **not**
> fire. The avenue dies one step later, at the **exponent**. PCD10 forces
> \(\operatorname{bitlen}(n_m)\ge E_m-6\ell+1\), so the integer whose digits
> the plateau reads, \(3^{n_m}\), has \(2^{\Theta(E_m)}\) binary digits while
> the plateau window has width only \(O(E_m)\). Stewart bounds a **global**
> nonzero-digit count over that whole expansion; in a window of relative
> width \(2^{-\Theta(E_m)}\) it says nothing. Worse, the bound is
> **anti-correlated** with the event it must exclude: a longer plateau makes
> \(n_m\) smaller, which makes Stewart's guarantee weaker.

So the recorded failure mode is *not* "the height is unbounded" but "the
exponent is doubly exponential in the window position". That distinction
matters, because it means no improvement in \(c\), and no sharpening of the
bridge, can rescue the route. Any repair must come from a **local** digit
theorem — a bound on runs of prescribed digits at a prescribed position in
\(3^{R}\) — which is the normality question the portfolio already sets aside.

---

## 1. Deliverable (a): the elementary ceiling, consolidated

W10 called this "part (a), not a discovery". It is nonetheless worth writing
down exactly, because the exact form is the same object that governs
BAKER1–3, and having one statement covering both is the consolidation.

> **W10-A (proved here).** The closure of \(\langle3\rangle\) in
> \(\mathbb Z_2^{\times}\) is exactly \(\{x:x\equiv1,3\ (\mathrm{mod}\ 8)\}\),
> of index \(2\). For any odd \(A\) in that set there is a unique **ghost**
> \(\alpha_A\in\mathbb Z_2\) with \(3^{\alpha_A}=A\), and for every integer
> \(n\ge0\)
> \[
> v_2\bigl(3^{n}-A\bigr)=
> \begin{cases}
> 1,& n\not\equiv\alpha_A\ (\mathrm{mod}\ 2),\\[2pt]
> 2+v_2(n-\alpha_A),& n\equiv\alpha_A\ (\mathrm{mod}\ 2).
> \end{cases}
> \]
> Consequently the least \(n\) matching \(A\) to \(2\)-adic depth \(W\) is
> **exactly** \(\alpha_A\bmod2^{W-2}\), and matching to depth \(W\) forces
> \(n\) into the progression \(\alpha_A\ (\mathrm{mod}\ 2^{W-2})\).

*Proof.* \(3^m\bmod2^W\) depends only on \(m\bmod2^{W-2}\) for \(W\ge3\), so
\(m\mapsto3^m\) extends continuously to \(\mathbb Z_2\); its image is the
closure of \(\langle3\rangle\), which is \(\{x\equiv1,3\ (8)\}\) since
\(3^m\equiv1\ (8)\) for even \(m\) and \(\equiv3\ (8)\) for odd \(m\).
Uniqueness of \(\alpha_A\) follows from \(\operatorname{ord}_{2^W}(3)=2^{W-2}\).
Then \(3^n-A=3^{\alpha_A}\bigl(3^{\,n-\alpha_A}-1\bigr)\), and the \(2\)-adic
LTE identity \(v_2(3^t-1)=2+v_2(t)\) for \(t\in2\mathbb Z_2\), \(=1\) for
\(t\) odd, extends by continuity. \(\square\)

**Relation to W9.** Taking \(A=-7\) recovers BAKER1–3 verbatim: the verifier
checks that the general construction returns \(\alpha_{-7}\equiv1198\)
\((\mathrm{mod}\ 2^{16})\), the same ghost as
`baker_explicit_constants_audit.md` §4.1. So the "elementary ceiling" and the
Baker-gated \(d=7\) enemy branch are one statement, and the ceiling
\(W\le2+\log_2 n\) holds *unless the ghost has an anomalously long run of
zero digits* — which is precisely where transcendence input is needed, and
precisely what W9 showed is exactly computable in any finite range.

This is the consolidation W10(a) asked for. It is not new mathematics; it is
the removal of a duplicated idea.

---

## 2. Deliverable (b): the bridge, at height \(c=1\)

From PCD13, the exponent carry is
\(C=\bigl(3^{n}-(2r+1)\bigr)/2^{E+2}\) with \(3^{n}\equiv2r+1\pmod{2^{E+2}}\)
and \(0\le2r+1<2^{E+2}\). Hence, exactly,

\[
C=\Bigl\lfloor\frac{3^{n}}{2^{E+2}}\Bigr\rfloor .
\]

Combining with PCD14 (a plateau removes the matched low \(\delta\) bits from
\(C\), i.e. \(C'=\lfloor C/2^{\delta}\rfloor\)), the plateau stream is a
window of the binary digits of \(3^{n}\) — see W11-C for the statement and
its proof.

> **W10-B.** The reset/plateau stream on the eventual-plateau branch is a
> digit window of \(3^{R}c\) with \(R=n_m\) and \(c=1\). The height is
> \(0\); W10's kill criterion does not fire.

The bridge is therefore not the obstacle. This is worth stating plainly
because W10 named the bridge as its main risk ("The carry shifting
block-by-block across a plateau is the known obstacle; the bridge must either
absorb the shift or restrict to a sub-branch where \(c\) stabilizes"). The
shift is absorbed for free — by PCD14 it only deletes low digits, so \(c\)
stays \(1\) for the whole plateau run and can change only when the plateau
ends.

---

## 3. Deliverable (c): Stewart applies, and is vacuous

### 3.1 The theorem

> **Known theorem (Stewart 1980).** For multiplicatively independent bases
> \(a,b\) and \(n>25\),
> \[
> s_a(n)+s_b(n)>\frac{\log\log n}{\log\log\log n+C(a,b)}-1,
> \]
> with \(C(a,b)\) effectively computable.

Reference: C. L. Stewart, *On the representation of an integer in two
different bases*, J. reine angew. Math. **319** (1980), 63–72; this is the
effective form of the Senge–Straus theorem, obtained from Baker's method.
With \(n=3^{R}\) and \(s_3(3^{R})=1\),

\[
s_2\bigl(3^{R}\bigr)>\frac{\log R}{\log\log R+C}-2 .
\]

The verifier takes \(C=0\), i.e. it **overstates** the guarantee, so the
vacuity conclusion below is conservative.

### 3.2 The size gap

PCD10 gives \(\operatorname{bitlen}(n_m)\ge E_m-6\ell+1\) where \(\ell\) is
the length of the plateau ending at \(m\). So \(n_m\gtrsim2^{E_m-6\ell}\) and
\(3^{n_m}\) has \(\approx1.585\cdot2^{E_m-6\ell}\) binary digits, while the
plateau window has width \(\sum\delta_j\le6\ell\).

| \(E_m\) | plateau \(\ell\) | \(\operatorname{bitlen}(n_m)\ge\) | digits of \(3^{n_m}\) | Stewart \(\ge\) | expected in window |
|---:|---:|---:|---:|---:|---:|
| 100 | 3 | 83 | \(2^{82.7}\) | 12.1 | \(10^{-23}\) |
| 100 | 10 | 41 | \(2^{40.7}\) | 6.3 | \(10^{-10}\) |
| 500 | 3 | 483 | \(2^{482.7}\) | 55.5 | \(10^{-142}\) |
| 1000 | 3 | 983 | \(2^{982.7}\) | 102.3 | \(10^{-293}\) |
| 5000 | 3 | 4983 | \(2^{4982.7}\) | 421.9 | \(10^{-1496}\) |

The last column is the number of Stewart-guaranteed nonzero digits one would
expect to find inside the plateau window if they were spread uniformly. It is
below \(10^{-10}\) in every live regime and falls off like
\(2^{-\Theta(E_m)}\).

### 3.3 The bound runs the wrong way

At \(E_m=1000\):

| plateau \(\ell\) | \(\operatorname{bitlen}(n_m)\ge E_m-6\ell+1\) | Stewart \(\ge\) |
|---:|---:|---:|
| 1 | 995 | 103.4 |
| 3 | 983 | 102.3 |
| 10 | 941 | 98.6 |
| 30 | 821 | 87.6 |
| 100 | 401 | 47.3 |
| 160 | 41 | 6.3 |

> **W10-C (the kill).** Stewart's guaranteed nonzero-digit count for
> \(3^{n_m}\) is non-increasing in the plateau length \(\ell\), because a
> longer plateau forces a *smaller* least exponent representative (PCD10).
> The digit-theoretic input therefore weakens exactly in the regime where it
> would have to be strong. It becomes non-vacuous only when
> \(6\ell\asymp E_m\), i.e. only when the plateau is already linear in \(m\)
> — precisely the case that the target "plateau \(=o(m)\)" assumes away.

This is a cleaner refutation than a mere order-of-magnitude mismatch: the
method is not just too weak, it is pointed the wrong way.

---

## 4. Why the mismatch is structural, not fixable

The gap is between two different kinds of statement:

- **Stewart gives a global count.** "\(3^{R}\) has at least \(N\) nonzero
  binary digits somewhere among its \(\Theta(R)\) digits."
- **The plateau needs a local run bound.** "The digits of \(3^{R}\) in
  positions \(E,\dots,E+V\) do not equal a prescribed word."

A global count cannot bound a local run from above: \(3^{R}\) having
\(\gg\log R/\log\log R\) nonzero digits is entirely compatible with a run of
\(\Theta(R/\log R)\) zeros. The only theorems that would close the gap are
local — equidistribution or normality of the digits of \(3^{R}\) in a moving
window — and the portfolio already fences those off:

> "**Normality or Fourier-type results on digits of \(3^n\).** Open and hard
> independently of Collatz; enter only through W10's specific bounded-height
> bridge, never as a standalone target."

W10 existed to be that specific bounded-height entrance. The bridge is built
(§2) and the height is \(1\); the entrance leads to the same open problem
anyway, because the *bounded height* was never the binding constraint. This
should be recorded in the set-aside list so the item is not reopened by the
same route a third time.

**Feeds back to W11.** W10's kill rule says the failure note "should say
exactly where the height enters, which feeds W11". The answer: the height
does not enter at all. What enters is PCD10's exponent-growth inequality,
which is the same quantity W11's Lyapunov computation measures from the other
side — \(E_m\) grows linearly in \(m\) at rate \(5+\beta\), and
\(\operatorname{bitlen}(n_m)\) tracks it, so \(n_m\) is doubly exponential in
the block index. The two sessions are measuring one phenomenon: the balanced
system consumes \(5+\beta\) previously unseen high bits per block, and every
method that needs to see those bits in advance fails for that reason.

---

## 5. Barrier check

1. *Finite-state information.* Not invoked.
2. *Density / entropy.* Not invoked; §3 is a comparison of two proved
   bounds, not a census.
3. *Variable-height Diophantine bounds are tautological.* **This is the
   relevant barrier and the finding refines it.** Triage §11 says such bounds
   "feed the unknown valuation scale back into their own upper bound". Here
   the height is fixed at \(c=1\), so the usual form of the tautology does
   not apply — and yet the route still fails, because the *exponent*, not the
   height, carries the unknown scale. Barrier 3 should be read as covering
   both: variable height **or** variable exponent.
4. *Virtual collisions.* Not applicable.

**Explicit non-claims.** Nothing here proves sublinear plateau growth, bounds
a reset gap, strengthens IEF10, or eliminates any exponent. W10-A is a
consolidation; W10-B is a reformulation; W10-C is a negative result about a
proposed method.

---

## 6. Falsifier

- **W10-A** is falsified by any \((A,n)\) with \(A\equiv1,3\ (8)\) and
  \(v_2(3^n-A)\) not given by the displayed formula, or by a depth \(W\) at
  which some \(m<\alpha_A\bmod2^{W-2}\) already matches \(A\). Checked for
  a spread of targets, all \(n<600\), and all \(W\le21\).
- **W10-B** is falsified by a plateau extension whose relevant carry is not
  \(\lfloor3^{n}/2^{E+2}\rfloor\).
- **W10-C** is falsified by a *local* digit theorem for \(3^{R}\) — a bound
  on runs of prescribed digits in a window at a prescribed position — with an
  effective constant. Such a theorem would reopen the avenue immediately, and
  the bridge of §2 is already in place to receive it. That is the one
  concrete thing to watch for in the literature.

---

## 7. Verification

```bash
python3 scripts/verify_digit_bridge_ceiling.py
```

Prints `DIGIT-BRIDGE: PASS`.

---

## 8. Suggested ledger rows (not applied)

| ID | Statement | Status | Source |
|---|---|---|---|
| DBC1 | For odd \(A\equiv1,3\ (8)\) there is a unique \(\alpha_A\in\mathbb Z_2\) with \(3^{\alpha_A}=A\), \(v_2(3^n-A)=1\) or \(2+v_2(n-\alpha_A)\) by parity, and the least \(n\) matching \(A\) to depth \(W\) is \(\alpha_A\bmod2^{W-2}\) | Proved here | §1 (W10-A) |
| DBC2 | The plateau stream is a digit window of \(3^{n_m}\) with height \(c=1\) | Proved here | §2 (W10-B) |
| DBC3 | Stewart's guaranteed nonzero-digit count for \(3^{n_m}\) is non-increasing in the plateau length and is vacuous in the plateau window by a factor \(2^{\Theta(E_m)}\) | Proved here | §3 (W10-C) |

DBC1 supersedes the \(A=-7\) special case stated separately in
`baker_explicit_constants_audit.md` §4.1 (BAKEX3); the two should be filed as
one row if either is promoted.
