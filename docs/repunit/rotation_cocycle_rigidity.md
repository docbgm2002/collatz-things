# Rotation-cocycle rigidity for the plateau problem  [W11]

**Task:** `OPUS5_WIDE_TASKS.md` W11, deliverables (i)–(iii) (session 3 of the
recommended order).
**Building on:** `payout_concentration_diffusion.md` §§15–17 (PCD13, PCD14,
PCD15), `integral_escape_frontier.md` §12 (IEF8 and the Sturmian
renormalization), `../../scripts/explore_balanced_q3_zero_cylinders.py`.
**Verifier:** `scripts/verify_rotation_cocycle_rigidity.py` (10 checks; exact
integer arithmetic, floats only in printing and in the continued fraction of
an irrational slope).
**Status:** **Avenue closed, with a transfer.** The proposed dictionary does
not exist, and the obstruction is exact. The session's positive output is a
bridge lemma for **W10**, obtained for free (§4).
**License:** CC-BY 4.0

---

## 0. Verdict

W11 proposed to write the PCD13 plateau condition \(t_m=\kappa_m\) as a
cocycle over the Sturmian rotation with values in the compact group
\(\mathbb Z_2\),

\[
(x,y)\ \longmapsto\ (x+\alpha,\ y+\varphi(x)),
\]

so that Furstenberg's criterion would give **unique ergodicity** — an
*every-orbit* statement — and thereby evade barrier 2, which kills
almost-every statements.

> **W11-KILL.** No such \(\varphi\) exists, and no finite tower of
> compact-group extensions over the rotation is conjugate to this system.
> The exact reason is already in the repo as PCD15, restated here as a
> dynamical invariant: **the fibre map multiplies \(2\)-adic distance by
> exactly \(2^{\delta_m}\) at block \(m\)**, so the system has strictly
> positive \(2\)-adic Lyapunov exponent
> \[
> \lim_{m\to\infty}\frac1m\sum_{j<m}\delta_j
> \;=\;5+\beta\;=\;2+\frac{2}{\log_2(3/2)}\;=\;5.4190225827\ldots
> \]
> (in units of \(\log2\) per block), whereas every compact-group extension is
> fibrewise an **isometry** and therefore has Lyapunov exponent \(0\) at every
> level of any finite tower. Furstenberg, Veech/Oren/Conze and
> Denjoy–Koksma are all inapplicable, not merely hard.

Both of W11's exits are therefore closed at once:

- the every-point exit (Furstenberg) is unavailable, because there is no
  compact-group extension to apply it to;
- the remaining exit is measure rigidity on a \(\times2\)/\(\times3\) joining
  (the Rudolph–Johnson branch the task's own Remark anticipates), which
  yields **almost-every** statements — forbidden by W11's own kill rule
  ("Kill any use of the theory that only yields almost-every statements").

Barrier 2 stands. Nothing in this note eliminates a cylinder.

---

## 1. Deliverable (i): the dictionary, and exactly where it breaks

### 1.1 What \(\varphi\) would have to be

The driver is genuine. Skipping the first appended block, the block-length
word is the characteristic Sturmian word of slope

\[
\beta=\frac{2}{\log_2(3/2)}-3=0.4190225827\ldots,
\]

with \(\delta_m=5\) for a \((1,1,3)\) block and \(\delta_m=6\) for a
\((1,1,1,3)\) block (IEF8; `BLOCK_DATA`). So the base
\(x\mapsto x+\beta\) on \(\mathbb T\) and the letter map
\(\delta(x)=5+\mathbb 1_{[1-\beta,1)}(x)\) are exactly a rotation and a
two-valued step function. That much of W11's picture is correct.

*Aside, since it pins the constant.* Balancedness forces
\(\overline{\delta}/\overline{\text{steps}}=\log_23\). With \(p\) the
frequency of the \(\delta=5\) block, \(\frac{6-p}{4-p}=\log_23\), whose
solution is \(p=1-\beta\); hence

\[
\overline{\text{steps}}=4-p=\frac{2}{\log_2(3/2)},
\qquad
\overline{\delta}=6-p=2+\frac{2}{\log_2(3/2)}=5+\beta .
\]

So the Lyapunov constant above is not fitted — it is forced by
balancedness, and \(\beta\) appears in it for the same reason it is the
Sturmian slope.

The fibre would have to carry the endpoint/lift state. PCD15 gives the exact
fibre map: with \(y\) the canonical endpoint and \(t\) the starting-cylinder
lift,

\[
F_{\mathbf v}(y,t)=\frac{3^{|\mathbf v|}\bigl(y+2t\,3^{K}\bigr)+c(\mathbf v)}
{2^{\delta}} .
\]

For a skew product we need \(F\) to be a **translation** of a compact group,
i.e. \(y\mapsto y+\varphi(x)\).

### 1.2 The obstruction, exactly

PCD15's displacement identity (re-verified here for both blocks, all tested
\(M,y,t\)) is

\[
F_{\mathbf v}(y+2^{M},t)-F_{\mathbf v}(y,t)=3^{|\mathbf v|}\,2^{\,M-\delta},
\]

that is

\[
\boxed{\ \bigl|F_{\mathbf v}(y_1,t)-F_{\mathbf v}(y_2,t)\bigr|_2
=2^{\delta}\,\bigl|y_1-y_2\bigr|_2\ }
\]

since \(3^{|\mathbf v|}\) is a \(2\)-adic unit. A translation of a compact
abelian group satisfies this with factor \(1\). So \(F\) is not a translation,
and it is not conjugate to one by any bi-Lipschitz change of fibre
coordinate.

> **W11-A (proved here).** Let \(\Lambda=\lim_m\frac1m\sum_{j<m}\delta_j\)
> be the \(2\)-adic Lyapunov exponent of the balanced endpoint recursion, in
> units of \(\log2\) per block. Then \(\Lambda=5+\beta>0\). Every extension
> of the rotation by a compact abelian group, and every finite tower of such
> extensions, has \(\Lambda=0\). Hence the balanced plateau system is not
> such an extension, and Furstenberg's criterion, the Veech/Oren/Conze
> coboundary criteria and Denjoy–Koksma do not apply to it.

Verified numerically: \(\frac1m\sum\delta_j\) equals
\(5.41900000\) at \(m=8000\) against \(5.41902258\).

This is the outcome W11 explicitly allowed for — "or to prove this is
impossible, which would itself sharpen PCD12's correlation warning into a
structural theorem". PCD15 said "no fixed-width endpoint state is closed";
W11-A says the same thing as a Lyapunov exponent, which is what makes it a
statement about the *class of methods* rather than about one encoding.

---

## 2. Deliverable (ii): the Furstenberg character test is vacuous

Furstenberg's criterion tests whether, for some nontrivial character \(\chi\)
of the fibre group, \(\chi\circ\varphi\) is a measurable coboundary over the
rotation. To pose it one needs \(\varphi\) to be a function **on the circle**
— equivalently, \(t_m\) must be determined by the rotation phase, hence by
the Sturmian word around position \(m\).

It is not, at any resolution. Over 8000 balanced blocks:

| window radius \(W\) | distinct factors | Sturmian \(p(2W{+}1)=2W{+}2\) | factors carrying \(>1\) lift value |
|---:|---:|---:|---:|
| 1 | 4 | 4 | 4 of 4 |
| 2 | 6 | 6 | 6 of 6 |
| 4 | 10 | 10 | 10 of 10 |
| 8 | 18 | 18 | 18 of 18 |
| 16 | 34 | 34 | 34 of 34 |
| 32 | 66 | 66 | 66 of 66 |
| 64 | 130 | 130 | 130 of 130 |
| 128 | 258 | 258 | 258 of 258 |

The middle column is a built-in consistency check: the observed factor count
is exactly \(L+1\), confirming the driver really is Sturmian. The right
column is the point: **every factor, at every tested length up to 257,
carries more than one lift value.** No coarse-graining of the phase
determines \(t_m\).

> **W11-B (finite certificate, and the computational face of PCD15).**
> Through 8000 balanced blocks, no factor of the block word of length
> \(\le257\) determines the starting-cylinder lift. Consequently \(\varphi\)
> is not a function on the circle at any finite resolution, there is no fibre
> character to test, and deliverable (ii) is vacuous rather than hard.

Note this is *stronger* than PCD12, which showed the lift alphabet is full.
PCD12 rules out excluding individual lift values; W11-B rules out
conditioning on any bounded amount of phase information.

---

## 3. Deliverable (iii): Denjoy–Koksma at the Ostrowski scales

The experiment is still worth running, because it **localises** the
obstruction: it separates the part of the system that *is* a bounded-variation
cocycle over the rotation from the part that is not.

**Positive control — the gap word.** \(\delta_m-\bar\delta\) is (an interval
indicator minus its mean), so \(\mathrm{Var}=2\) and Denjoy–Koksma predicts
\(\bigl|\sum_{m<Q}(\delta_m-\bar\delta)\bigr|\le2\) at every convergent
denominator \(Q\) of \(\beta\). Observed:

| \(Q_k\) | 2 | 5 | 7 | 12 | 31 | 74 | 105 | 284 | 389 | 4563 |
|---|---|---|---|---|---|---|---|---|---|---|
| cocycle sum | −0.838 | −0.095 | −0.933 | −0.028 | −0.990 | −0.008 | −0.997 | −0.002 | −1.000 | −0.000045 |

Textbook behaviour: the sums lie in \([-1,0]\), alternating between the
even- and odd-index convergents, with the even-index values collapsing to
\(0\). (The largest scale \(Q=4563\) is the same one IEF8's renormalization
diagnostic independently checks.)

**Negative test — the lift stream.** With
\(\hat t_m=t_m/2^{\delta_m}\in[0,1)\), the cocycle sums reach \(-3.10\) at
\(Q=105\) and \(-3.45\) at \(Q=4563\), exceeding the driver's variation.
These are *not* proofs of unboundedness on a range this short — but they do
not need to be, because §2 already shows there is no variation to bound them
with.

> **Correction (made in session 4, W10).** An earlier version of this section
> used \(t_m=0\) as the *plateau* indicator and compared its histogram with
> PCD12's. That was wrong. `analyse()` returns the **IEF starting-cylinder**
> lift digit \(z_H\) of \(u_H\) — IEF7's stream, whose vanishing means the
> *starting cylinder* stabilises. PCD's cylinder plateau is a vanishing
> **exponent** lift, \(n_{m+1}=n_m\), which by PCD13 is the condition
> \(t=\kappa\) and requires the exponent-side carry \(\kappa\), i.e. the
> digits of \(3^{n}\), which `analyse()` does not compute. The two streams
> are the digit streams of two different \(2\)-adic ghosts, related by the
> \(2\)-adic discrete logarithm (\(3^{\alpha}=2u_\infty+1\)); their zero
> counts differ (43 versus PCD12's 39 through \(m=1500\)). The verifier now
> reports the IEF stream under its own name and makes no comparison with
> PCD12. **W11-A, W11-B and W11-C are unaffected**: W11-A is about the fibre
> map, W11-B is about the starting-cylinder lift (which *is* PCD13's \(t\)),
> and W11-C is pure algebra from PCD13/PCD14.

**Reading.** The gap word is the bounded-variation, zero-entropy part of the
system; the carry is not. W11 hoped the plateau indicator would be the
former. It is the latter.

---

## 4. The transfer: W11's real output is W10's bridge lemma

The most useful thing the session produced is an identification, not a
refutation.

PCD13/PCD14 define the carry
\(C=\bigl(3^{n}-(2r+1)\bigr)/2^{E+2}\) with \(3^{n}\equiv2r+1\pmod{2^{E+2}}\)
and \(0\le2r+1<2^{E+2}\). Therefore, trivially but decisively,

\[
\boxed{\ C=\Bigl\lfloor \frac{3^{n}}{2^{E+2}} \Bigr\rfloor\ }
\]

— \(C\) is the **high part of the binary expansion of \(3^n\)**. And on a
plateau PCD14 reads \(C'=(C-t)/2^{\delta}\) with \(t\equiv C\ (2^{\delta})\),
i.e.

\[
C'=\bigl\lfloor C/2^{\delta}\bigr\rfloor
\quad\text{— the \(2\)-adic digit shift.}
\]

Combining with PCD14's concatenation law:

> **W11-C (proved here).** A plateau run over blocks
> \(\delta_1,\dots,\delta_\ell\) occurs **iff** the low
> \(\delta_1+\cdots+\delta_\ell\) binary digits of \(3^{n}\) equal the
> concatenated lift word \(t_1|t_2|\cdots|t_\ell\). Plateau runs are exactly
> agreements between the affine lift word and a window of the binary digits
> of \(3^{n}\); the plateau dynamics on the carry is the \(2\)-adic digit
> shift, driven at Sturmian rate \(\delta_m\).

Two consequences, pulling in opposite directions.

**(a) It explains the kill, and confirms it is not an accident of encoding.**
A rotation-driven digit shift is a \(\times2\)/\(\times3\) joining: a
zero-entropy rotation driving a positive-expansion \(2\)-adic shift whose
digits come from a power of three. That is precisely the structure the task's
own Remark predicted would appear if (i) failed, and it is precisely *not* a
compact-group extension. It also means W11 collapses into the portfolio's own
set-aside item — "**Normality or Fourier-type results on digits of \(3^n\).**
Open and hard independently of Collatz; enter only through W10's specific
bounded-height bridge, never as a standalone target."

**(b) It hands W10 its bridge lemma, on the friendliest branch, with height
one.** W10's deliverable (b) asks for "an exact identification of the reset
stream with digit windows of bounded-height \(3^{R}c\) integers, valid on a
named branch class", attempted first "on the eventual-plateau branch". W11-C
supplies exactly that for the plateau branch, with \(c=1\) — the best
possible height. W10's stated kill, "kill if the bridge provably requires
unbounded-height \(c\) on every branch class", therefore does *not* fire.

> **Outcome, recorded in session 4.** The bridge is real and the height is
> \(1\), but W10 is nonetheless killed — by the **exponent**, not the height.
> PCD10 forces \(\operatorname{bitlen}(n_m)\ge E_m-6\ell+1\), so the integer
> \(3^{n_m}\) whose digits the plateau reads has \(2^{\Theta(E_m)}\) binary
> digits while the plateau window has width only \(O(E_m)\). Stewart's bound
> is a global nonzero-digit *count* over that whole expansion and says
> nothing about a window of relative width \(2^{-\Theta(E_m)}\); worse, it
> weakens as the plateau lengthens. Details and numbers in
> `../no-go/digit_bridge_ceiling.md` §3.

**Honest caveat (which turned out to be the whole story).** Having the bridge
is not having the theorem. Stewart bounds the *count* of nonzero digits; a
plateau is an *agreement* between the digits of \(3^n\) and the lift word
\(t_1|\cdots|t_\ell\), which is a run condition at a prescribed position, not
a digit-count condition. Session 4 shows that gap is not a technicality but
the obstruction itself.

---

## 5. Barrier check

1. *Finite-state information.* §2 shows the lift is **not** finite-state over
   the rotation — that is the content, and it is a negative result, so
   barrier 1 is not being evaded, it is being confirmed in a new coordinate.
2. *Density / entropy.* The plateau statistics in §3 are reported as finite
   evidence and are explicitly **not** promoted. The observed plateau rate
   \(0.0256\) sits next to the naive independent heuristic
   \((1-\beta)2^{-5}+\beta2^{-6}=0.0247\), and the longest plateau through
   8000 blocks has length 3 (PCD convention). Barrier 2 says exactly that
   this census cannot finish, and W11 existed to escape it; the escape fails.
3. *Variable-height Diophantine.* §4 goes the other way: it produces a
   **height-zero** identification, which is why it is useful to W10 rather
   than barred by triage §11.
4. *Virtual collisions.* Not applicable; every statement is about the actual
   balanced word and its actual cylinders.

**Explicit non-claim.** Nothing here proves sublinear plateau growth, bounds
a reset gap, or eliminates any exponent. W11-A and W11-B are negative
structural results about a method; W11-C is a reformulation.

---

## 6. Falsifier

- **W11-A** is falsified by exhibiting a fibre coordinate in which the
  endpoint recursion is an isometry — equivalently, by contradicting PCD15's
  displacement identity \(F(y+2^M,t)-F(y,t)=3^{|\mathbf v|}2^{M-\delta}\),
  which the verifier checks exactly for both block types.
- **W11-B** is falsified by a window radius \(W\) at which some Sturmian
  factor determines \(t_m\) uniquely across all its occurrences. Checked to
  \(W=128\) (factor length 257) over 8000 blocks: none.
- **W11-C** is falsified by a plateau extension with
  \(t\not\equiv\lfloor3^n/2^{E+2}\rfloor\pmod{2^{\delta}}\).
- **The transfer to W10** is falsified if the plateau branch turns out to
  need the *general* carry \(C'\) rather than \(C\) itself — i.e. if the
  relevant stream after \(\ell\) plateau blocks is not still a digit window of
  \(3^{n}\). It is: by W11-C the shift only deletes low digits, so the height
  stays \(1\) forever along a plateau run. The height can only grow when
  \(z\ne0\), i.e. when the plateau ends. (The transfer is sound; what fails
  downstream is the *use* of it — see `../no-go/digit_bridge_ceiling.md`.)

## 7bis. Verification-hygiene note

Session 4 found and fixed a stream mislabelling in §3 of this note: the
stream `analyse()` computes is IEF's starting-cylinder lift, not PCD's
exponent lift, so it is not the cylinder-plateau indicator and its histogram
must not be compared with PCD12's. The structural results are unaffected;
see the boxed correction in §3. Anyone extending this note should check
which of the two \(2\)-adic ghosts — \(u_\infty\) (starting cylinder) or
\(\alpha_\infty\) with \(3^{\alpha_\infty}=2u_\infty+1\) (exponent) — a
given stream belongs to before comparing counts.

---

## 7. Verification

```bash
python3 scripts/verify_rotation_cocycle_rigidity.py                # 8000 blocks
python3 scripts/verify_rotation_cocycle_rigidity.py --blocks 12000
```

Prints `ROTATION-COCYCLE: PASS`. The run reproduces PCD12's plateau
statistics at four times the length (PCD convention
\(\{1{:}7597,\ 2{:}191,\ 3{:}7\}\) through \(m=8000\), against PCD12's
\(\{1{:}1423,\ 2{:}37,\ 3{:}1\}\) through \(m=1500\); the rates agree), which
is an independent check on the shared cylinder machinery.

---

## 8. Suggested ledger rows (not applied)

| ID | Statement | Status | Source |
|---|---|---|---|
| RCR1 | The balanced endpoint recursion multiplies \(2\)-adic distance by exactly \(2^{\delta_m}\); its Lyapunov exponent is \(5+\beta=2+2/\log_2(3/2)\). No compact-group extension of the rotation, and no finite tower of them, is conjugate to it | Proved here | §1 (W11-A) |
| RCR2 | Through 8000 blocks, no factor of the block word of length \(\le257\) determines the starting-cylinder lift | Finite certificate | §2 (W11-B) |
| RCR3 | \(C=\lfloor3^{n}/2^{E+2}\rfloor\); a plateau run is exactly an agreement between the concatenated lift word and the low binary digits of \(3^{n}\), and the plateau carry dynamics is the \(2\)-adic digit shift | Proved here | §4 (W11-C) |
| RCR4 | Denjoy–Koksma holds for the gap word at every Ostrowski scale through \(Q=4563\) (sums in \([-1,0]\), \(\mathrm{Var}=2\)); the IEF starting-cylinder lift stream exceeds that bound | Finite certificate | §3 |

RCR3 is the row that matters downstream: it is the W10 bridge lemma on the
plateau branch, at height \(c=1\). Session 4 (`../no-go/digit_bridge_ceiling.md`)
shows the bridge is sound but the digit theorems on the far side of it are
vacuous at the required scale, so RCR3 should be filed as a reformulation,
not as progress toward the plateau bound.
