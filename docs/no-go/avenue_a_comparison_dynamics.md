# Avenue A — Comparison Dynamics (Working Note)

**Status:** Active. Storage-dominance is the first lemma. Exact identities and
a finite certificate are recorded below. The universal first-descent
storage-dominance statement remains open; the sharpest remaining length-gate
cut is lemma target **EC1**, split as EC1-large (Baker reduction) +
EC1-near (\(\Theta(n)\) \(\delta\)-window residual; \(O(1)\) hope refuted) +
SD-L1 for \(L=1\). Not a claim-ledger promotion until the human proof is
complete.

**Parent:** [`outside_box_avenue_portfolio.md`](outside_box_avenue_portfolio.md)
Avenue A; exact transfer inequality in
[`repunit_descent_transfer_fan.md`](repunit_descent_transfer_fan.md).

## 1. Objects

For odd \(n\ge3\),

\[
a_n=\frac{3^n-1}{2},\qquad
M_n=2^n-1,\qquad
x_0(n)=a_n,\qquad
x_{i+1}(n)=f\bigl(x_i(n)\bigr),
\]

with \(e_i=v_2(3x_i+1)\) and \(E_i=\sum_{j<i}e_j\). Write \(K_\downarrow(n)\) for
the first index with \(x_K(n)<M_n\).

Normal form and storage coordinate:

\[
A_0=-1,\qquad
A_{i+1}=3A_i+2^{E_i+1},\qquad
R_i=A_i+2^{E_i+1},
\]

equivalently \(R_0=1\) and

\[
R_{i+1}=3R_i+2^{E_i+1}(2^{e_i}-2).
\]

Then \(R_i>0\) for every \(i\), and

\[
x_i+1=\frac{3^{n+i}+R_i}{2^{E_i+1}}.
\]

Relative storage:

\[
\theta_i(n)=\frac{R_i}{3^{n+i}}.
\]

Storage-dominance is exactly \(\theta_i(n)<1\).

## 2. Lemma SD1 (open)

> **First-descent storage-dominance.** For every odd integer \(n\ge3\) and
> every index \(0\le i\le K_\downarrow(n)\),
>
> \[
> 0<R_i(n)<3^{n+i}.
> \]

Equivalent integer forms at each such \(i\):

\[
3^{n+i}<2^{E_i+1}\bigl(x_i+1\bigr)<2\cdot3^{n+i},
\]

\[
\bigl(x_i+1\bigr)\,2^{E_i}<3^{n+i}.
\]

(The left inequality is \(R_i>0\), already proved for every \(i\ge0\).)

## 3. Exact relative-storage expansion (proved)

On \(e_i=1\) steps one has \(R_{i+1}=3R_i\), hence \(\theta_{i+1}=\theta_i\).
On every payout \(e_i\ge2\),

\[
\theta_{i+1}
=
\theta_i+\frac{2^{E_i+1}(2^{e_i}-2)}{3^{n+i+1}}.
\]

Starting from \(\theta_0=3^{-n}\),

\[
\boxed{
\theta_K
=
3^{-n}
\left(
1+\frac23\sum_{\substack{j<K\\e_j\ge2}}
2^{-D_j}(2^{e_j}-2)
\right),
\qquad
D_j=j\log_2 3-E_j.
}
\]

Consequently SD1 is equivalent to: for every odd \(n\ge3\) and every
\(K\le K_\downarrow(n)\),

\[
\sum_{\substack{j<K\\e_j\ge2}}
2^{-D_j}(2^{e_j}-2)
<
\frac32\bigl(3^n-1\bigr).
\tag{SD1\(^\prime\)}
\]

This is the form that must absorb payout placement under the constraint that
every earlier state satisfied \(x_j\ge M_n\).

## 4. Slack recurrence (proved)

Put \(S_i=3^{n+i}-R_i\). Then \(S_0=3^n-1\) and

\[
S_{i+1}=3S_i-2^{E_i+1}(2^{e_i}-2).
\]

SD1 holds at \(i+1\) iff \(S_{i+1}>0\). Valuation-one steps triple the slack.
A payout of size \(e\) consumes slack \(2^{E+1}(2^e-2)\). The induction step
at a payout is exactly

\[
3S_i>2^{E_i+1}(2^{e_i}-2).
\]

## 5. Why the descent cutoff is essential

SD1 is false if the upper index is extended past first descent. For every
odd \(3\le n\le79\), and for the hard seeds \(n=17,193,471\), the first
failure of \(R_i<3^{n+i}\) occurs strictly after \(K_\downarrow(n)\).

Prototype \(n=3\):

| \(i\) | \(x_i\) | \(e_i\) | \(R_i\) | \(3^{3+i}\) | \(\theta_i\) |
|---|---:|---:|---:|---:|---:|
| 0 | 13 | 3 | 1 | 27 | \(1/27\) |
| 1 | 5 | 4 | 15 | 81 | \(5/27\) |
| 2 | 1 | 2 | 269 | 243 | \(>1\) |

Here \(K_\downarrow(3)=1\), and SD fails at \(i=2\). Any proof that ignores
the barrier \(x_i\ge M_n\) on \([0,K_\downarrow)\) is aiming at a false
statement.

## 6. Finite certificate

`scripts/verify_repunit_storage_dominance.py --limit 5001` checks SD1 on
every odd \(3\le n\le5001\), through and including first descent.

Result:

- all tails pass;
- longest first descent in the domain: 7418 steps at \(n=4589\);
- worst \(\theta_i=R_i/3^{n+i}\) on the whole domain is exactly \(5/27\),
  realised at \(n=3\), \(i=1\);
- the integer inequality \(27R_i\le5\cdot3^{n+i}\) holds for every checked
  state, so no larger seed through \(5001\) is closer to the SD1 ceiling.

This remains a finite certificate. It is not a ledger promotion of SD1.
A side conjecture \(\theta_i(n)\le5/27\) through first descent is consistent
with the census but is stronger than needed for ST1.

## 7. Conditional consequence already available

Assuming SD1, the strict surplus-transfer law of
`repunit_descent_transfer_fan.md` §5 is proved: at aligned first-descent
comparators,

- \(H_g<0\) forces the transfer inequality;
- \(H_g>0\) forbids it;
- \(H_g=0\) reduces to the exact correction order.

Thus the missing universal step for the sign law is exactly SD1.

## 8. Affine / \(\phi\) reformulation (proved)

Write the relative affine correction \(q_i\) as in
`docs/repunit/repunit_affine_tail_bound.md`, so

\[
x_i=\frac{3^i a_n(1+q_i)}{2^{E_i}},
\qquad
1+q_i=\prod_{j<i}\Bigl(1+\frac1{3x_j}\Bigr).
\]

Define

\[
\phi_i
=
(1+q_i)\Bigl(1+\frac1{x_i}\Bigr)
=
\frac{2^{E_i}(x_i+1)}{3^i a_n}.
\]

**Lemma SD-eq.** The following are equivalent at any index \(i\):

1. \(R_i<3^{n+i}\);
2. \((x_i+1)2^{E_i}<3^{n+i}\);
3. \(a_n(1+q_i)(1+1/x_i)<3^n\);
4. \(\phi_i<2\cdot3^n/(3^n-1)\).

Moreover \(\theta_i=\phi_i(1-3^{-n})-1\).

**Lemma SD-\(\phi\)-dyn.** One has \(\phi_0=(3^n+1)/(3^n-1)\) and

\[
\frac{\phi_{i+1}}{\phi_i}
=
\begin{cases}
1,&e_i=1,\\
1+\dfrac{2^{e_i}-2}{3(x_i+1)},&e_i\ge2.
\end{cases}
\]

Hence

\[
\phi_K
=
\phi_0
\prod_{\substack{j<K\\e_j\ge2}}
\Bigl(1+\frac{2^{e_j}-2}{3(x_j+1)}\Bigr),
\]

and SD1 through time \(K\) is exactly

\[
\prod_{\substack{j<K\\e_j\ge2}}
\Bigl(1+\frac{2^{e_j}-2}{3(x_j+1)}\Bigr)
<
\frac{2}{1+3^{-n}}.
\tag{SD1\(^{\prime\prime}\)}
\]

## 9. Structural split (proved)

**Lemma SD-rail.** If \(e_i=1\), then
\(x_{i+1}=(3x_i+1)/2>x_i\). Consequently the first descent step
cannot be a valuation-one step: \(e_{K_\downarrow(n)-1}\ge2\) whenever
\(K_\downarrow(n)\ge1\).

Proof: \((3x+1)/2>x\iff x>-1\). \(\square\)

Thus every first-descent window consists of:

- zero or more **stay-above payouts** (\(e\ge2\) and still \(x'\ge M_n\));
- valuation-one runs (raise \(x\), preserve \(\phi\) and \(\theta\));
- exactly one **terminal descent payout** (\(e\ge2\) and \(x'<M_n\)).

Put \(T=M_n=2^n-1\) and
\(\sigma_i=3^{n+i}-(x_i+1)2^{E_i}\)
(so \(\sigma_i=S_i/2\) and SD at \(i\) is \(\sigma_i>0\)).

**Lemma SD-stay-red.** Suppose \(x_i\ge T\), \(e_i\ge2\), and
\(x_{i+1}\ge T\). Then \(2^{e_i}\le(3x_i+1)/T\), and the next-step SD
inequality \((x_{i+1}+1)2^{E_i+e_i}<3^{n+i+1}\) follows from IH
\(\sigma_i>0\) as soon as

\[
3^{n+i+1}<2^n\bigl(3\sigma_i+2^{E_i+1}\bigr).
\tag{SD1S}
\]

(The displayed bound is equivalent to
\(((3x_i+1)/T-2)2^{E_i}<3\sigma_i\), which dominates the exact
payout consumption \((2^{e_i}-2)2^{E_i}\).)

**Finite status of SD1S.** On every stay-above payout through odd
\(n\le1001\), SD1S holds (verified in
`scripts/verify_repunit_storage_dominance.py` with `--check-stay`). No
counterexample is known.

**Strong slack (finite).** The stricter bound

\[
\sigma_i>\frac{3^{n+i}}{2^n}
\tag{SD1+}
\]

holds at every state through first descent for all odd \(n\le1001\). It is
preserved exactly in ratio on valuation-one steps, and it implies SD1S by

\[
2^n(3\sigma_i+2^{E_i+1})
>
3^{n+i+1}+2^{E_i+n+1}
>
3^{n+i+1}.
\]

Thus a proof of SD1+ on stay-above steps would close SD1S. (Proving SD1+
itself still requires a payout estimate; it is a convenient strengthening,
not yet a theorem.)

**Lemma SD-desc-obs.** At the terminal descent payout, the SD margin
\(\log_2\bigl(3^{n+K}/((x_K+1)2^{E_K})\bigr)\) is \(\approx1\) for large
tested \(n\) (so \(R_K\) is negligible versus \(3^{n+K}\)). The crude
sufficient bound \((2^n-2)2^{E_K}<3^{n+K}\) already fails for some seeds
(e.g. \(n=17,471\)), so the descent step needs the true \(x_K\), not the
worst odd residue below \(T\).

## 10. The strengthening \(\phi<2\) (SD½)

**Lemma SD-threshold.** For every odd \(n\ge3\),
\[
2<\frac{2\cdot3^n}{3^n-1}.
\]
Hence \(\phi_i<2\) implies SD1 at index \(i\).

**Definition SD½.** Through first descent,
\[
(x_i+1)2^{E_i}<3^i(3^n-1),
\]
equivalently \(\sigma_i>3^i\), equivalently \(\phi_i<2\).

**Lemma SD½-start.** At \(i=0\),
\((a_n+1)<3^n-1\) for \(n\ge2\), so SD½ holds at the start.

**Lemma SD½-rail.** Valuation-one steps preserve SD½: if \(e_i=1\) and
\(\tau_i:=3^i(3^n-1)-(x_i+1)2^{E_i}>0\), then \(\tau_{i+1}=3\tau_i>0\).

**Finite status.** SD½ holds through first descent for every odd
\(3\le n\le4001\) (checked by the storage-dominance verifier). The worst
ratio \((x+1)2^E\big/3^i(3^n-1)\) on that domain is \(8/13\) at
\(n=3\), \(i=1\) (equivalently \(\phi=16/13\)).

## 11. Stay-above reduction to payout mass

Write \(R_i=3^i+P_i\) with payout mass
\[
P_i=\sum_{\substack{j<i\\e_j\ge2}}3^{i-1-j}2^{E_j+1}(2^{e_j}-2)\ge0.
\]

**Lemma SD-Gamma.** For odd \(n\ge3\),
\[
\Gamma_n:=(3^n-1)T-2^{n-1}(3^n+1)>0.
\]
Proof: \(\Gamma_n=(3^n-3)2^{n-1}-(3^n-1)=3(3^{n-1}-1)2^{n-1}-(3^n-1)\), and
\(3(3^{n-1}-1)2^{n-1}\ge3\cdot8\cdot4=96>26=3^3-1\) already at \(n=3\), with
the leading term \(3^n2^{n-1}\) dominating thereafter. \(\square\)

**Lemma SD½-stay-red.** Assume SD½ at index \(i\), \(x_i\ge T\), \(e_i\ge2\),
and \(x_{i+1}\ge T\). Then SD½ at \(i+1\) holds provided
\[
3^{i+1}\Gamma_n+2^{E_i+n+1}>3\cdot2^{n-1}P_i.
\tag{SD½P}
\]
(This is equivalent to the stay-above case of
\(3\tau_i>(2^{e_i}-2)2^{E_i}\) after substituting the bound
\(2^{e_i}\le(3x_i+1)/T\) and the normal form of \(R_i\).)

**Finite status.** SD½P holds at every stay-above payout through odd
\(n\le251\) (10851 steps checked).

**Strengthening SD½P⁻.** The same finite domain in fact satisfies the
stronger mass bound
\[
P_i<\frac{3^i\Gamma_n}{2^{n-1}},
\tag{SD½P⁻}
\]
which drops the positive \(2^{E_i+n+1}\) term from SD½P and therefore
implies it. Through odd \(n\le201\) this holds at every stay-above
payout (no counterexample; worst observed ratio
\(P\cdot2^{n-1}/(3^i\Gamma_n)\) is about \(0.03\) at \(n=5\)).

**Lemma SD-T-rail.** For \(T=2^n-1\) one has \(v_2(3T+1)=1\). Hence a
stay-above payout (\(e\ge2\), \(x'\ge T\)) can never occur at \(x=T\).

**Induction attempt for SD½P⁻.** On \(e=1\) the bound is homogeneous
(\(P\mapsto3P\)). On a stay-above payout,
\[
P_{i+1}=3P_i+2^{E_i+1}(2^{e_i}-2)
\le3P_i+\frac{3^i(3^n+1)+P_i}{T}\Bigl(3-\frac{2^{n+1}}{x_i+1}\Bigr).
\]
The factor \(3-2^{n+1}/(x_i+1)\) is minimized at the smallest admissible
\(x_i\) and *increases* with \(x_i\), so excluding \(x=T\) (Lemma SD-T-rail)
does not tighten this upper bound. Using the SD½ upper bound on \(x_i\)
instead yields
\[
3-\frac{2^{n+1}}{x_i+1}
<3-\frac{2^{E_i+n+1}}{3^i(3^n-1)},
\]
and with that estimate the inductive step for SD½P⁻ holds on every
checked stay-above payout through odd \(n\le151\) (worst abstract ratio
about \(0.065\)). Closing the step uniformly still fails if one allows
\(P\) all the way up to \(3^i\Gamma_n/2^{n-1}\) with worst-case
\(E_i=i\); the orbits keep \(P\) far below that ceiling (ratio
\(\approx0.03\)). A proof needs a stronger a-priori ceiling on \(P\), or
an exact (not \((3x+1)/T\)) control of \(2^{e_i}\).

**Lemma SD½-factor.** On every stay-above payout,
\[
\frac{\phi_{i+1}}{\phi_i}
=1+\frac{2^{e_i}-2}{3(x_i+1)}
=\frac{2^{e_i}(x_{i+1}+1)}{2^{e_i}x_{i+1}+2}
\le1+\frac1{x_{i+1}}
\le1+\frac1T.
\]
(The middle identity is exact for every payout; the last step uses
\(x_{i+1}\ge T\).) A coarser estimate with denominator \(3T\) is also valid
but strictly weaker.

## 11a. Deficit coordinate (proved dictionary)

Write
\[
\rho_i=\frac{(x_i+1)2^{E_i}}{3^i(3^n-1)},
\qquad
d_i=(3^n-1)\rho_i,
\qquad
\tau_i=3^i(3^n-1)-(x_i+1)2^{E_i}.
\]
Then SD½ is exactly \(\rho_i<1\), equivalently \(d_i<3^n-1\), equivalently
\(\tau_i>0\). One has \(d_0=a_n+1\) and \(\rho_0=(3^n+1)/(2(3^n-1))\).

**Lemma SD-deficit-dyn.** Valuation-one steps preserve \(d\) and \(\rho\). On
every payout with landing \(x'\),
\[
d_{i+1}
=
d_i\cdot\frac{2^{e_i}(x'+1)}{2^{e_i}x'+2}.
\]
In particular, through the stay-above window,
\[
d_i=d_0\prod\alpha_j,
\qquad
\alpha_j=\frac{2^{e_j}(x_{j+1}+1)}{2^{e_j}x_{j+1}+2},
\]
the product running over stay-above payouts before index \(i\). Hence SD½
through first descent is equivalent to that product staying strictly below
\[
\frac{3^n-1}{a_n+1}=\frac{2(3^n-1)}{3^n+1}.
\]

**Lemma SD-mass-deficit.** Payout mass and deficit are related by
\[
P_i=2\cdot3^i\,(d_i-d_0)=2\cdot3^i\,(a_n+1)\Bigl(\prod\alpha_j-1\Bigr).
\]
Consequently SD½P⁻ is exactly
\[
\prod\alpha_j
<
1+\frac{\Gamma_n}{2^n(a_n+1)}.
\]
For large \(n\) this ceiling and the SD½ ceiling \(2(3^n-1)/(3^n+1)\) both
approach \(2\); the two targets differ only by a lower-order gap.

**Theorem SD½-length (conditional).** If the first-descent length satisfies
\[
K_\downarrow(n)
<
T\cdot\log\frac{2(3^n-1)}{3^n+1},
\]
then SD½ holds for that \(n\). Indeed each stay-above factor obeys
\(\log\alpha<\alpha-1<1/x'\le1/T\), so the product of at most
\(K_\downarrow\) such factors stays below the SD½ ceiling.

**Finite length margin.** Through odd \(n\le4097\) one has
\(K_\downarrow(n)=O(n)\) empirically (e.g. \(K_\downarrow(4097)=5491\)), while
the length budget is \(\asymp T\log2\asymp2^n\). The only seed with
\(K_\downarrow/T\) comparable to \(\log2\) is \(n=5\)
(\(K_\downarrow=30\), \(T=31\)); that seed is discharged by direct orbit
check, as is \(n=3\).

### Bridge from the affine-tail bound

The repunit affine theory
([`../repunit/repunit_affine_tail_bound.md`](../repunit/repunit_affine_tail_bound.md),
Theorem 3) gives, whenever \(x_j\ge T\) for all \(j<i\),
\[
1+q_i\le\Bigl(1+\frac1{3T}\Bigr)^i.
\]
Since \(\phi_i=(1+q_i)(1+1/x_i)\) and \(x_i\ge T\) on every pre-landing
state,
\[
\phi_i
\le
\Bigl(1+\frac1{3T}\Bigr)^i\Bigl(1+\frac1T\Bigr).
\]

**Lemma SD-T-budget.** For every odd \(n\ge3\) and \(T=2^n-1\),
\[
\Bigl(1+\frac1{3T}\Bigr)^T\Bigl(1+\frac1T\Bigr)<2,
\qquad
\Bigl(1+\frac1{3T}\Bigr)^T\cdot\frac43<2.
\]
Proof. The inequalities \(\ln(1+u)<u\) yield
\[
T\ln\Bigl(1+\frac1{3T}\Bigr)+\ln\Bigl(1+\frac1T\Bigr)
<\frac13+\frac1T
\le\frac13+\frac17
<\ln2,
\]
and likewise
\[
T\ln\Bigl(1+\frac1{3T}\Bigr)+\ln\frac43
<\frac13+\ln\frac43
<\ln2.
\]
(The inequalities are strict, so the exponentials are strictly below \(2\).)
\(\square\)

**Theorem SD½-affine (conditional).** Assume \(K_\downarrow(n)\le T\). Then
SD½ holds at every index \(0\le i\le K_\downarrow(n)\), provided the landing
satisfies \(x_{K_\downarrow}\ge3\).

Proof. For \(i<K_\downarrow\) one has \(x_i\ge T\), so
\[
\phi_i
\le
\Bigl(1+\frac1{3T}\Bigr)^i\Bigl(1+\frac1T\Bigr)
\le
\Bigl(1+\frac1{3T}\Bigr)^T\Bigl(1+\frac1T\Bigr)
<2
\]
by Lemma SD-T-budget. At the landing index \(K=K_\downarrow\), the affine
bound still controls \(1+q_K\) (it only needs \(x_j\ge T\) for \(j<K\)), and
\(x_K\ge3\) gives
\[
\phi_K
\le
\Bigl(1+\frac1{3T}\Bigr)^K\Bigl(1+\frac1{x_K}\Bigr)
\le
\Bigl(1+\frac1{3T}\Bigr)^T\cdot\frac43
<2.
\]
Thus \(\phi<2\) through first descent, i.e. SD½. \(\square\)

**Corollary SD1-affine (conditional).** If \(K_\downarrow(n)\le T\) and
\(x_{K_\downarrow}\ge3\), then SD1 holds for that \(n\). (Combine
Theorem SD½-affine with Lemma SD-threshold.)

**Finite status of the length gate.** \(K_\downarrow(n)\le T\) holds for every
odd \(3\le n\le5001\) (asserted in
`scripts/verify_repunit_storage_dominance.py`; the worst ratio is
\(K_\downarrow/T=30/31\) at \(n=5\)). Empirically \(K_\downarrow=O(n)\), so the
gate \(K_\downarrow\le T\) is extremely soft — but it remains unproved.

### Attack on \(K_\downarrow=n^{O(1)}\) (Baker-tail pivot)

The soft gate \(K_\downarrow\le T\) is enough for Corollary SD1-affine, but the
Baker / window-gap tails for \(x^\star\), fixed-\(s\) height, \(z_n\), and
EC1-large need the much stronger \(K_\downarrow=n^{O(1)}\) (empirically
\(O(n)\)). This subsection records the exact reduction to a named density
gap; it does **not** claim a proof of the linear bound.

**Definition.** Write \(U\) for the shortcut map (\(U(x)=x/2\) if \(x\) even,
\((3x+1)/2\) if \(x\) odd). One accelerated step of valuation \(e\) is exactly
\(e\) shortcut steps. Let \(H(n)\) be the number of shortcut steps from
\(a_n\) to the first value strictly below \(T=2^n-1\).

**Lemma SD-K-shortcut.** For every odd \(n\ge3\),
\[
K_\downarrow(n)\le H(n).
\]
Proof. Each accelerated step contributes at least one shortcut step (the
odd \(U\)-step). The terminal crossing step is counted in both
\(K_\downarrow\) and \(H\). \(\square\)

**Lemma SD-K-density.** Fix odd \(n\ge7\) and \(t=5n-2\). If the
\(a_n\)-tail stays \(\ge T\) throughout its first \(t\) shortcut steps and
\(\rho\) denotes the number of odd \(U\)-steps in that prefix, then
\[
\rho\le\Bigl\lfloor\frac{11n}{4}\Bigr\rfloor
\quad\Longrightarrow\quad
\frac{U^{t}(a_n)}{T}<1,
\]
contradicting survival. Consequently every full-window survivor (if any)
must satisfy \(\rho>\lfloor11n/4\rfloor\).

Proof. While the tail stays above \(T\), every odd state is \(\ge T\), so
\[
\frac{U^{t}(a_n)}{T}
\le
\frac{a_n}{T}\cdot\frac{3^{\rho}}{2^{t}}\cdot\Bigl(1+\frac1{3T}\Bigr)^{\rho}.
\]
For \(n\ge19\) the envelope \(\rho\le\lfloor11n/4\rfloor\) forces the
right-hand side \(<1\) by the rational bound recorded in
[`../nested-anchor/nested_anchor_escape_notes.md`](../nested-anchor/nested_anchor_escape_notes.md)
(Odd-density reduction): using
\(a_n/T<(64/127)(3/2)^n\),
\((1+1/(3T))^\rho<\exp(99/6132)\), and base
\((3/2)\,3^{11/4}/32<481/500\), one obtains a quantity
\(<2.016\cdot1.017\cdot0.962^n\le0.983\) at \(n=19\), decreasing
thereafter. The cases \(9\le n\le17\) are checked exactly with rational
arithmetic in `scripts/explore_mersenne_shortcut_budget.py`
(`ceiling_forces_descent`). \(\square\)

**Lemma SD-K-survivor-split.** For odd \(n\ge7\) and \(t=5n-2\), either
\(H(n)\le t\), or the length-\(t\) prefix is a survivor with
\(\rho>\lfloor11n/4\rfloor\).

Proof. If \(H(n)>t\) then the first \(t\) shortcut steps all stay
\(\ge T\). Lemma SD-K-density then forbids \(\rho\le\lfloor11n/4\rfloor\).
\(\square\)

**Lemma SD-K-embed.** For every odd \(n\ge3\) and \(t=5n-2\) one has
\(a_n<2^{t}\). Explicitly \(3^n-1<2^{5n-1}\) since
\(\log_2 3<5\).

Proof. The inequality \(n\log_2 3<5n-1\) is
\(n(5-\log_2 3)>1\), true for all \(n\ge1\). \(\square\)

Consequently \(a_n\bmod 2^{t}\) is just the integer \(a_n\) itself: there is
no nontrivial high-bit lift. Gap SD-K-nonconcentration is therefore a
statement about **one explicit parity word** — the length-\(t\) shortcut
itinerary of \(a_n\) — not about a sparse algebraic sequence hiding in a
thin subset of a large residue ring.

**Lemma SD-K-e0-prefix.** Write \(e_0=1+v_2(n+1)\). The first \(e_0\)
shortcut steps from \(a_n\) consist of exactly one odd \(U\)-step followed
by \(e_0-1\) even steps (the seed payout). In particular any length-\(t\)
itinerary with odd-count \(\rho\ge\lfloor11n/4\rfloor+1\) must place at
least \(\lfloor11n/4\rfloor\) odd letters in the remaining
\(t-e_0\) steps, i.e. require suffix odd-density at least
\[
\frac{\lfloor11n/4\rfloor}{5n-2-e_0}.
\]
For \(e_0=O(\log n)\) this threshold is \(11/20+O((\log n)/n)\). \(\square\)

**Lemma SD-K-thin.** Among the \(2^{t}\) residue classes modulo \(2^{t}\)
with \(t=5n-2\), those whose shortcut parity word has more than
\(\lfloor11n/4\rfloor\) odd letters number at most
\[
\sum_{r>\lfloor11n/4\rfloor}\binom{t}{r}
\le
2^{t\,H_2(11/20)},
\]
where \(H_2\) is binary entropy. Their density is
\[
2^{-\bigl(5\bigl(1-H_2(0.55)\bigr)+o(1)\bigr)n}
=
2^{-(0.03612\ldots+o(1))n}.
\]
(Each parity word of length \(t\) is realised by exactly one class modulo
\(2^{t}\).) Under Lemma SD-K-embed only one class is relevant for \(a_n\):
the class of \(a_n\) itself. \(\square\)

**Lemma SD-K-nc-strong.** Fix odd \(n\ge7\) and \(t=5n-2\). Let
\(\rho_t(n)\) be the number of odd \(U\)-steps among the first \(t\)
shortcut steps of \(a_n\) (continuing the itinerary even after a descent
below \(T\)). If \(\rho_t(n)\le\lfloor11n/4\rfloor\), then
\(H(n)\le t\).

Proof. If \(H(n)>t\) then the first \(t\) steps all stay \(\ge T\) and
have odd-count \(\rho_t(n)\), so Lemma SD-K-density forces
\(\rho_t(n)>\lfloor11n/4\rfloor\). \(\square\)

**Gap SD-K-survivor (open).** For every odd \(n\ge7\) one has
\(H(n)\le5n-2\).

**Gap SD-K-nonconcentration (open; sharpened).** For every odd \(n\ge7\),
\[
\rho_t(n)\le\Bigl\lfloor\frac{11n}{4}\Bigr\rfloor,
\qquad t=5n-2.
\]
By Lemma SD-K-nc-strong this implies Gap SD-K-survivor. By
Lemma SD-K-embed it is exactly the statement that the unique residue of
\(a_n\) modulo \(2^{t}\) is not a high-odd-density class.

**Lemma SD-K-rail-dict.** Decompose the first \(t\) shortcut steps of
\(a_n\) into the seed payout of valuation \(e_0=1+v_2(n+1)\) followed by
suffix accelerated episodes (rails \(e=1\) and payouts \(e\ge2\)), with
the last episode possibly truncated at step \(t\). Write
\[
R=\#\{\text{complete or started rails}\},\qquad
P=\#\{\text{suffix payouts}\},\qquad
E=\sum_j e_j
\]
for the realized valuations of those suffix payouts (truncated length
counted). Then every \(U\)-step is odd precisely on the first division of
an accelerated episode, and even precisely on the trailing \(e-1\)
divisions of a payout (including the seed). In particular rails
contribute \(100\%\) odd letters and no even letters. \(\square\)

**Lemma SD-K-even-id.** With the notation above,
\[
\rho_t(n)
=
t-\Bigl((e_0-1)+\sum_j(e_j-1)\Bigr).
\]
Equivalently the even-\(U\) count in the window equals the seed surplus
\(e_0-1\) plus the total payout surplus \(\sum(e_j-1)\). \(\square\)

**Lemma SD-K-even-equiv.** Gap SD-K-nonconcentration is equivalent to
\[
(e_0-1)+\sum_j(e_j-1)
\ \ge\
t-\Bigl\lfloor\frac{11n}{4}\Bigr\rfloor
=
5n-2-\Bigl\lfloor\frac{11n}{4}\Bigr\rfloor.
\]
The right-hand side is \(\ge\lceil(9n-8)/4\rceil\). \(\square\)

**Gap SD-K-even-budget (open; equivalent).** For every odd \(n\ge7\),
the even-\(U\) count in the length-\((5n-2)\) itinerary of \(a_n\) is at
least \(5n-2-\lfloor11n/4\rfloor\). This is Gap SD-K-nonconcentration
rewritten in payout language: rails alone cannot supply the needed
evens; the seed and suffix payouts must.

**Lemma SD-K-height-count.** Decompose the length-\(t\) itinerary of
\(a_n\) into the seed payout and subsequent height-blocks as in
Lemma SD-K-rail-dict. For each complete block with landing height
\(h'\) write \(h^{\mathrm{eff}}=h'\); for a block truncated after \(r\)
rails write \(h^{\mathrm{eff}}=1+r\); for a payout truncated before its
landing write \(h^{\mathrm{eff}}=1\). Then
\[
\rho_t(n)=1+\sum_j h_j^{\mathrm{eff}}.
\]
Proof. The seed contributes one odd \(U\)-step. Each complete block
contributes one odd from its payout and \(h'-1\) odds from its rails,
totalling \(h'\). A mid-rail truncation contributes \(1+r\); a mid-payout
truncation contributes a single odd. \(\square\)

**Lemma SD-K-rail-criterion (sufficient).** On a complete (untruncated)
suffix of rails and payouts, write \(\rho=R+P\) and \(s=R+E\). Then
\[
\frac{\rho}{s}\le\frac{11}{20}
\quad\Longleftrightarrow\quad
11E\ge9R+20P
\quad\Longleftrightarrow\quad
\sum_j(e_j-1)\ge\frac9{11}\sum_j h_j,
\]
where \(h_j\) is the height of the rail run preceding the \(j\)-th payout
(so \(R=\sum(h_j-1)\) under the block dictionary of Lemma SD-h-rail).
In particular any uniform lower bound \(\sum(e_j-1)\ge\tfrac9{11}\sum h_j\)
on the suffix forces suffix density \(\le11/20\). Finite probes show this
criterion is near-saturated and occasionally fails on the suffix alone
at \(n=11,17,23\); the seed surplus \(e_0-1\) restores the full-window
even budget in those cases. \(\square\)

**Lemma SD-K-911-implies (sufficient).** Let \(t=5n-2\) and
\(\rho=\rho_t(n)\). If
\[
11(t-\rho)\ge9(\rho-1),
\]
then
\[
\rho\le\Bigl\lfloor\frac{11t+9}{20}\Bigr\rfloor
=
\Bigl\lfloor\frac{11n}{4}-\frac{13}{20}\Bigr\rfloor
\le
\Bigl\lfloor\frac{11n}{4}\Bigr\rfloor.
\]
Proof. The hypothesis rearranges to \(20\rho\le11t+9\). The identity
\((11t+9)/20=11n/4-13/20\) is elementary, and
\(\lfloor x-13/20\rfloor\le\lfloor x\rfloor\). \(\square\)

Equivalently (Lemma SD-K-height-count / even-id), the hypothesis is
\[
11\bigl((e_0-1)+\sum(e_j-1)\bigr)
\ge
9\sum_j h_j^{\mathrm{eff}}.
\]
Heuristic drift per height-block is
\(\mathbb E[e-1]-(9/11)\mathbb E[h']=2-(9/11)\cdot2=2/11>0\), so the
criterion is the natural pathwise strengthening of the mean-field bound
\(\rho/t\to1/2\).

**Gap SD-K-911 (open; slightly stronger).** For every odd \(n\ge7\) with
\(n\ne23\),
\[
11\bigl(t-\rho_t(n)\bigr)\ge9\bigl(\rho_t(n)-1\bigr).
\]
By Lemma SD-K-911-implies this yields Gap SD-K-nonconcentration. At the
single finite saturator \(n=23\) one has \(\rho_t=63=\lfloor11\cdot23/4\rfloor\)
while \(11(t-\rho)=550<558=9(\rho-1)\), so Gap SD-K-911 fails but the
even-budget form still holds with equality. Through odd \(n\le5001\) the
only failure of Gap SD-K-911 is \(n=23\) (`--check-nine-eleven`).

**Remark (density vs survivor).** Pre-descent odd-density may exceed
\(0.55\) on short orbits that nevertheless descend inside the window
(observed at \(n=17,23,25\); at \(n=23\) one has the saturation
\(H(23)=t=113\) with \(\rho_t=\lfloor11\cdot23/4\rfloor=63\)). Those
examples have \(\rho_t\le\lfloor11n/4\rfloor\), so they obey Gap
SD-K-nonconcentration and do **not** falsify either gap. The open case is
an itinerary with \(\rho_t>\lfloor11n/4\rfloor\) that stays \(\ge T\) for
all \(t\) steps. Even-budget slack is zero only at \(n=17\) and \(n=23\)
through \(4000\); for \(n\ge501\) the observed slack is already
\(\ge93\).

**Lemma SD-K-linear (conditional).** Assume Gap SD-K-survivor (or the
stronger Gap SD-K-nonconcentration). Then for every odd \(n\ge7\) one has
\(K_\downarrow(n)\le H(n)\le5n-2\). Together with the hand checks
\(K_\downarrow(3)=1\) and \(K_\downarrow(5)=30\le6\cdot5\), one has
\[
K_\downarrow(n)\le6n
\]
for every odd \(n\ge3\). In particular \(K_\downarrow=n^{O(1)}\), and every
Baker / window-gap tail in this note that assumes \(K_\downarrow=n^{O(1)}\)
becomes unconditional.

**Finite status.** For every odd \(3\le n\le5001\) one has
\(K_\downarrow(n)\le6n\) (`--check-k-linear` / main `verify()`; equality
only at \(n=5\)). For every odd \(7\le n\le10001\) one has both
\(H(n)\le5n-2\) (`--check-h-linear`; saturates at \(n=23\)) and
\(\rho_t(n)\le\lfloor11n/4\rfloor\) (`--check-rho-cap` /
`--check-even-budget`; even-slack \(0\) at \(n=17,23\)), and
Gap SD-K-911 holds except at \(n=23\) (`--check-nine-eleven` through
\(5001\)). Thus both gaps hold on that finite domain; the remaining task
is a uniform argument for large \(n\).

**Strategic note.** Lemma SD-K-embed removes a misleading difficulty: one
need not control \(3^n\) against a thin subset of \(\mathbb Z/2^{5n}\mathbb Z\)
with free high bits — \(a_n\) *is* its residue. The obstruction is to bound
the odd-count of an explicit linear-length itinerary of \(a_n\). The
sharper \(t=5n-2\) package (Gap SD-K-911 / even-budget) is retained above;
the **preferred live cut** is the slightly longer window below
(\(t=6n\)), which still yields \(K_\downarrow\le6n\) and is far cleaner
finitely (single miss \(n=11\)).

### Preferred cut: window \(t=6n\)

**Lemma SD-K-density-6.** Fix odd \(n\ge7\) and \(t=6n\). If the
\(a_n\)-tail stays \(\ge T\) throughout its first \(t\) shortcut steps and
\(\rho\) denotes the number of odd \(U\)-steps in that prefix, then
\[
\rho\le\Bigl\lfloor\frac{33n}{10}\Bigr\rfloor
\quad\Longrightarrow\quad
\frac{U^{t}(a_n)}{T}<1,
\]
contradicting survival. Consequently every full-window-\(6n\) survivor
(if any) must satisfy \(\rho>\lfloor33n/10\rfloor\).

Proof. While the tail stays above \(T\),
\[
\frac{U^{t}(a_n)}{T}
\le
\frac{a_n}{T}\cdot\frac{3^{\rho}}{2^{t}}\cdot\Bigl(1+\frac1{3T}\Bigr)^{\rho}.
\]
For every odd \(n\ge7\) the right-hand side with
\(\rho=\lfloor33n/10\rfloor\) is a ratio of integers strictly less than
\(1\) (exact `Fraction` arithmetic in
`scripts/verify_repunit_storage_dominance.py`,
`--check-density6-envelope`). Uniformly, \(a_n/T<(64/127)(3/2)^n\) and
\(3^{43/10}<127\), so the main term is at most
\[
\frac{64}{127}\Bigl(\frac{127}{128}\Bigr)^{n}
\]
times a factor \((1+1/(3T))^{\rho}\to1\); already at \(n=7\) the exact
bound is \(<0.2\). \(\square\)

**Lemma SD-K-survivor-split-6.** For odd \(n\ge7\) and \(t=6n\), either
\(H(n)\le6n\), or the length-\(t\) prefix is a survivor with
\(\rho>\lfloor33n/10\rfloor\). \(\square\)

**Lemma SD-K-nc6-implies.** If \(\rho_{6n}(n)\le\lfloor33n/10\rfloor\),
then \(H(n)\le6n\). (Same contrappositive as SD-K-nc-strong.) \(\square\)

**Gap SD-K-survivor-6 (open).** For every odd \(n\ge7\) one has
\(H(n)\le6n\).

**Gap SD-K-nc-6 (open; preferred).** For every odd \(n\ge7\) with
\(n\ne11\),
\[
\rho_{6n}(n)\le\Bigl\lfloor\frac{33n}{10}\Bigr\rfloor.
\]
By Lemma SD-K-nc6-implies this yields Gap SD-K-survivor-6. At \(n=11\)
one has \(\rho_{66}=38>36=\lfloor33\cdot11/10\rfloor\) while
\(H(11)=46\le66\), so survivor-6 holds and nc-6 fails.

**Lemma SD-K-911-6-strong-implies.** Let \(t=6n\) and
\(\rho=\rho_{6n}(n)\). If
\[
11(t-\rho)\ge9\rho+2,
\]
then
\[
\rho\le\Bigl\lfloor\frac{66n-2}{20}\Bigr\rfloor
=
\Bigl\lfloor\frac{33n}{10}-\frac1{10}\Bigr\rfloor
\le
\Bigl\lfloor\frac{33n}{10}\Bigr\rfloor.
\]
Proof. Rearrange to \(20\rho\le11t-2\). The displayed identity is
elementary, and \(\lfloor x-1/10\rfloor\le\lfloor x\rfloor\). \(\square\)

(The weaker score \(11(t-\rho)\ge9(\rho-1)\) only yields
\(\rho\le\lfloor33n/10+9/20\rfloor\), which can exceed the cap by \(1\)
when \(n\equiv3,9\pmod{10}\). The \(+2\) strengthening removes that
off-by-one.)

**Gap SD-K-911-6-strong (open; preferred attack form).** For every odd
\(n\ge7\) with \(n\ne11\),
\[
11\bigl(6n-\rho_{6n}(n)\bigr)\ge9\rho_{6n}(n)+2.
\]
Equivalently, writing \(\mathrm{score}=11\cdot\mathrm{even}-9(\rho-1)\),
one has \(\mathrm{score}\ge11\). By Lemma SD-K-911-6-strong-implies this
yields Gap SD-K-nc-6. Through odd \(n\le5001\) the inequality holds for
every \(n\ne11\), with equality only at \(n=17\)
(`--check-nine-eleven-6`).

**Lemma SD-K-seed-land.** Write \(e_0=1+v_2(n+1)\) and let \(x_1\) be the
landing of the seed payout from \(a_n\). If \(n\equiv1\pmod8\), then
\(e_0=2\) and \(h(x_1)=1\) (no post-seed rails). If \(n\equiv5\pmod8\),
then \(e_0=2\) and \(h(x_1)\ge2\).

Proof. For \(n=8k+1\), \(v_2(n+1)=1\) so \(e_0=2\), and
\(x_1=(3^{n+1}-1)/8\). Then \(x_1\equiv1\pmod4\) because
\(3^{n+1}\equiv3^{2}\equiv9\pmod{32}\) (using \(n+1\equiv2\pmod8\) and
\(3^8\equiv1\pmod{32}\)), hence \(h(x_1)=1\). For \(n=8k+5\),
\(v_2(n+1)=1\) still, but \(n+1\equiv6\pmod8\) forces
\(3^{n+1}\equiv3^{6}\equiv25\pmod{32}\), so \(x_1\equiv3\pmod4\) and
\(h(x_1)\ge2\). \(\square\)

**Lemma SD-K-score-split.** On the length-\(t=6n\) itinerary, write
\(r_0\) for the number of valuation-one rails between the seed landing
and the next \(h=1\) state, and write
\(\Delta_j=11(e_j-1)-9h_j^{\mathrm{eff}}\) for each subsequent
height-block. Then
\[
\mathrm{score}
=
11(e_0-1)+\sum_j\Delta_j-9r_0.
\]
Proof. Combine Lemma SD-K-even-id, Lemma SD-K-height-count (seed odd +
\(r_0\) rail odds + \(\sum h_j^{\mathrm{eff}}\)), and the definition of
score. \(\square\)

**Corollary SD-K-hard-8.** If \(n\equiv1\pmod8\), then \(e_0=2\), \(r_0=0\),
and \(\mathrm{score}=11+\sum\Delta_j\). In particular Gap SD-K-911-6-strong
is equivalent to
\[
\sum_j\Delta_j\ge0.
\]

**Gap SD-K-block-8 (open; core of the hard case).** For every odd
\(n\ge17\) with \(n\equiv1\pmod8\),
\[
\sum_j\Delta_j\ge0
\]
on the length-\(6n\) itinerary. Through \(n\le5001\) this holds, with
equality only at \(n=17\). Mean-field block drift is
\(\mathbb E[\Delta]=4>0\).

**Lemma SD-K-v2-35.** For every integer \(k\ge0\) and \(m=3+32k\),
\[
v_2(3^m+5)=5.
\]
Proof. The case \(k=0\) is \(3^3+5=32\). For the inductive step use
\(3^{32}=1+128u\) with \(u\) odd (since \(3^{32}\equiv129\pmod{256}\)).
Then
\[
3^{3+32k}+5
=
27(1+128u)^k+5
=
32+27\cdot128\,ku+2^{14}(\cdots)
=
32\bigl(1+108\,ku\bigr)+2^{14}(\cdots).
\]
Here \(1+108\,ku\) is odd, and the remaining term has \(2\)-valuation at
least \(14\), so the valuation is exactly \(5\). \(\square\)

**Lemma SD-K-first-e.** Let \(n\equiv1\pmod8\) and \(x_1=(3^{n+1}-1)/8\).
The first payout valuation at \(x_1\) is
\[
e=v_2(3x_1+1)=v_2(3^{n+2}+5)-3.
\]
In particular, if \(n\equiv1\pmod{32}\) then \(n+2\equiv3\pmod{32}\), so
Lemma SD-K-v2-35 gives \(e=2\). More generally the stable values
(`--check-block8-first`) are
\[
\begin{align*}
n\equiv1,33\pmod{64}&\Rightarrow e=2,\\
n\equiv17,49\pmod{64}&\Rightarrow e=2,\\
n\equiv25,57\pmod{64}&\Rightarrow e=3,\\
n\equiv41\pmod{64}&\Rightarrow e=4,
\end{align*}
\]
while \(n\equiv9\pmod{64}\) has unbounded \(e\ge5\). \(\square\)

**Lemma SD-K-first-h-good.** If \(n\equiv1\pmod{32}\) and \(n\ge33\), write
\(y=(3x_1+1)/2^e\) for the first landing (so \(e=2\)). Then
\(h(y)=1\) whenever \(n\equiv1\) or \(33\pmod{64}\), and the first block
has \(\Delta=+2\). If \(n\equiv49\pmod{64}\) then \(h(y)=2\) and
\(\Delta=-7\). If \(n\equiv57\pmod{64}\) then \(e=3\), \(h(y)=1\), and
\(\Delta=+13\).

Proof sketch. With \(e=2\) one has \(y=(3^{n+2}+5)/32\). Since the
multiplicative order of \(3\) modulo \(128\) is \(32\),
\[
n\equiv1,33\pmod{64}
\quad\Rightarrow\quad
3^{n+2}\equiv27\pmod{128}
\quad\Rightarrow\quad
y\equiv1\pmod4,
\]
hence \(h(y)=1\) and \(\Delta=11\cdot1-9\cdot1=2\). For
\(n\equiv49\pmod{64}\) one has \(3^{n+2}\equiv91\pmod{128}\) (so
\(y\equiv3\pmod4\)) and in fact \(3^{n+2}+5\equiv96\pmod{256}\) (using
\(3^{64}\equiv1\pmod{256}\)), so \(y\equiv3\pmod8\) and \(h(y)=2\),
hence \(\Delta=-7\). The case \(n\equiv57\pmod{64}\) is the same style
with \(v_2(3^{n+2}+5)=6\). \(\square\)

**Case split of Gap SD-K-block-8.** Among \(n\equiv1\pmod8\):

| \(n\bmod64\) | first \(\Delta\) | finite min \(\sum\Delta\) | status |
|---|---|---|---|
| \(1,33\) | \(+2\) (proved for \(n\ge33\)) | \(76\) at \(n=33\) | open; good start |
| \(49\) | \(-7\) (proved) | \(232\) | open; recovers |
| \(57\) | \(+13\) (proved) | \(220\) | open; good start |
| \(17\) | see Lemmas SD-K-h1-17 / h1-parity | \(0\) at \(n=17\) | open; **tightest** |
| \(25\) | \(e=3\), \(h\ge2\) (variable) | \(28\) at \(n=25\) | open; next-tight |
| \(9,41\) | \(e\ge4\) (variable \(h\)) | \(\ge224\) | open; loose finitely |

**Lemma SD-K-h1-17.** Let \(n=64k+17\) with \(k\ge0\). The first payout at
\(x_1\) has valuation \(e=2\), and the first landing height is
\[
h_1=v_2(3^{n+2}+37)-5.
\]
Consequently the first block contributes
\[
\Delta_1=11-9h_1.
\]
Proof. The identity \(e=2\) is Lemma SD-K-first-e. The landing is
\(y=(3^{n+2}+5)/32\), so
\[
h(y)=v_2(y+1)=v_2(3^{n+2}+37)-5.
\]
Then \(\Delta_1=11(e-1)-9h_1=11-9h_1\). \(\square\)

**Lemma SD-K-h1-parity.** Write \(n=64k+17\) and
\(3^{64}=1+256u\) with \(u\) odd. For every \(k\ge1\):

1. if \(k\) is odd then \(v_2(3^{n+2}+37)=8\), hence \(h_1=3\) and
   \(\Delta_1=-16\);
2. if \(k\equiv2\pmod4\) then \(v_2(3^{n+2}+37)=9\), hence \(h_1=4\) and
   \(\Delta_1=-25\).

Proof. Expand
\[
3^{19+64k}+37
=
(3^{19}+37)+3^{19}\bigl((1+256u)^k-1\bigr).
\]
The base has valuation \(10\). The parenthesis is
\(k\cdot256u+O(2^{16})\), hence has valuation \(8+v_2(k)\). If \(k\) is
odd this is \(8<10\), so the sum has valuation \(8\). If \(v_2(k)=1\)
it is \(9<10\), so the sum has valuation \(9\). \(\square\)

(The case \(k=0\) is \(n=17\), where \(h_1=5\) and \(\Delta_1=-34\). For
\(v_2(k)\ge2\) the middle term meets or exceeds valuation \(10\) and
cancellation can raise \(h_1\); empirically \(h_1=O(\log k)\).)

**Lemma SD-K-rail-closed.** Let \(y\) be odd with \(h(y)=r+1\) and
\(r\ge0\). After \(r\) rail steps \(x\mapsto(3x+1)/2\) the state is
\[
x_r=\frac{3^r(y+1)}{2^r}-1,
\]
and \(h(x_r)=1\).

Proof. The recurrence \(x\mapsto(3x+1)/2\) unrolls to
\(x_r+1=(3/2)^r(y+1)\). Since \(v_2(y+1)=r+1\), the right-hand side is
an integer of valuation \(1\). \(\square\)

**Lemma SD-K-e2-17.** Let \(n=64k+17\), write
\(h_1=v_2(3^{n+2}+37)-5\) and
\(m=(3^{n+2}+37)/2^{h_1+5}\) (odd). After the first block the next
\(h=1\) state \(x_2\) satisfies
\[
e(x_2)=1+v_2(3^{h_1}m-1).
\]

Proof. The first landing is \(y=(3^{n+2}+5)/32\), so
\(y+1=2^{h_1}m\). Lemma SD-K-rail-closed with \(r=h_1-1\) gives
\(x_2+1=3^{h_1-1}\cdot2m\). Then
\[
3x_2+1=2(3^{h_1}m-1),
\]
hence \(e(x_2)=1+v_2(3^{h_1}m-1)\). \(\square\)

**Lemma SD-K-e2-odd-3mod4.** If \(n=64k+17\) with \(k\equiv3\pmod4\)
(hence \(k\) odd and \(h_1=3\) by Lemma SD-K-h1-parity), then
\(e(x_2)=2\).

Proof. Here \(m=(3^{n+2}+37)/256\) and \(e(x_2)=1+v_2(27m-1)\). Write
\(3^{64}=1+256u\) with \(u\) odd, \(B=(3^{19}+37)/256\), and
\[
m=B+3^{19}\frac{(1+256u)^k-1}{256}.
\]
The correction is \(\equiv3^{19}ku\pmod8\) (higher binomial terms carry
\(256\)). Since \(a:=27B-1\equiv3\pmod8\) and
\(b:=27\cdot3^{19}ku\equiv5k\pmod8\), the hypothesis \(k\equiv3\pmod4\)
forces \(k\equiv3\) or \(7\pmod8\), whence \(a+b\equiv2\) or \(6\pmod8\).
In either case \(v_2(a+b)=1\), so \(e(x_2)=2\). \(\square\)

(Empirically the second-block height \(h_2\) remains unbounded on the
full odd-\(k\) class — e.g. \(h_2=6\) at \(n=1489\) — so \(\Delta_2\)
alone does not clear the need \(16\). On the finer subclass
\(k\equiv3\pmod8\) the second block is controlled:)

**Lemma SD-K-e-mod8.** Let \(x\) be odd with \(h(x)=1\) (equivalently
\(x\equiv1\pmod4\)). Then
\[
e(x)=2\iff x\equiv1\pmod8,
\qquad
e(x)\ge3\iff x\equiv5\pmod8,
\]
and refining mod \(16\):
\[
e(x)=3\iff x\equiv13\pmod{16},
\qquad
e(x)\ge4\iff x\equiv5\pmod{16}.
\]
Proof. Write \(x=4t+1\). Then \(3x+1=4(3t+1)\), so \(e\ge2\). One has
\(e=2\) iff \(3t+1\) is odd iff \(t\) is even iff \(x\equiv1\pmod8\); and
\(e\ge3\) iff \(t\) is odd iff \(x\equiv5\pmod8\). If \(x=8s+5\) then
\(3x+1=8(3s+2)\), and \(3s+2\) is odd iff \(s\) is odd iff
\(x\equiv13\pmod{16}\), while \(s\) even gives \(x\equiv5\pmod{16}\) and
\(e\ge4\). \(\square\)

**Lemma SD-K-h2-3mod8.** If \(n=64k+17\) with \(k\equiv3\pmod8\), then
the second height-block has \(e(x_2)=2\), \(h_2=1\), and \(\Delta_2=+2\).

Proof. Lemma SD-K-e2-odd-3mod4 already gives \(e(x_2)=2\) (since
\(k\equiv3\pmod8\Rightarrow k\equiv3\pmod4\)). With
\(m=(3^{n+2}+37)/256\) one has \(h_2=v_2(27m+1)-1\), so \(h_2=1\) iff
\(v_2(27m+1)=2\) iff \(27m+1\equiv4\pmod8\) iff \(m\equiv1\pmod8\).
Writing \(3^{64}=1+256u\) and \(B=(3^{19}+37)/256\), the expansion
\(m\equiv B+3^{19}ku\pmod8\) with \(B\equiv4\), \(3^{19}\equiv3\),
\(u\equiv5\pmod8\) yields \(m\equiv4+7k\pmod8\). For \(k\equiv3\pmod8\)
this is \(m\equiv1\pmod8\). \(\square\)

Consequently on \(k\equiv3\pmod8\) one has \(\Delta_1+\Delta_2=-14\), and
Gap SD-K-block-8-17 reduces to \(\sum_{j\ge3}\Delta_j\ge14\). The next
state is \(x_3=(27m-1)/2\) with \(e(x_3)=v_2(81m-1)-1\).

**Lemma SD-K-e3-expand.** Write \(3^{64}=1+256u\), \(B=(3^{19}+37)/256\),
\(a=81B-1\), \(c=81\cdot3^{19}u\), and
\(m=B+3^{19}((1+256u)^k-1)/256\). Then
\[
81m-1=a+ck+R,\qquad v_2(R)\ge8.
\]
Hence if \(v_2(a+ck)<8\) one has \(v_2(81m-1)=v_2(a+ck)\). Moreover
\(a\equiv115\pmod{128}\) and \(c\equiv95\pmod{128}\), so for
\(k=64t+r\)
\[
a+ck\equiv (a+cr)+64t\pmod{128}.
\]
Proof. The \(j=1\) binomial term is \(ck\); every \(j\ge2\) term carries
\(256^{j-1}\) and so has valuation \(\ge8\). The residues of \(a,c\) are
direct from \(B\equiv52\pmod{128}\) and \(u\equiv61\pmod{128}\). The
shift by \(64t\) uses \(64c\equiv64\pmod{128}\). \(\square\)

**Lemma SD-K-e3-stable.** Let \(n=64k+17\) with \(k\equiv3\pmod8\) (so
Lemmas SD-K-h1-parity / h2-3mod8 apply). Then:

| \(k\bmod64\) | \(v_2(81m-1)\) | \(e_3\) | \(h_3\) | \(\Delta_3\) | \(\Delta_1+\Delta_2+\Delta_3\) |
|---|---|---|---|---|---|
| \(3\) | \(4\) | \(3\) | \(1\) | \(+13\) | \(-1\) |
| \(11,43\) | \(3\) | \(2\) | \(1\) | \(+2\) | \(-12\) |
| \(59\) | \(3\) | \(2\) | \(2\) | \(-7\) | \(-21\) |

Proof. For the listed residues, Lemma SD-K-e3-expand gives
\(v_2(a+ck)\in\{3,4\}\) constantly in \(t\) (explicitly:
\(k\equiv3\Rightarrow a+ck\equiv16\) or \(80\pmod{128}\);
\(k\equiv11\Rightarrow8\) or \(72\);
\(k\equiv43\Rightarrow104\) or \(40\);
\(k\equiv59\Rightarrow88\) or \(24\)), all with valuation \(<8\), so
\(e_3=v_2(81m-1)-1\) is as in the table. The heights use the companion
expansions \(v_2(81m+15)\) (when \(e_3=3\)) and \(v_2(81m+7)\) (when
\(e_3=2\)), each again with error valuation \(\ge8\): one obtains
\(v_2(81m+15)=5\Rightarrow h_3=1\) on \(k\equiv3\pmod{64}\),
\(v_2(81m+7)=4\Rightarrow h_3=1\) on \(k\equiv11,43\), and
\(v_2(81m+7)=5\Rightarrow h_3=2\) on \(k\equiv59\). \(\square\)

(The classes \(k\equiv19,27,35,51\pmod{64}\) have variable \(h_3\) and are
deferred.)

**Lemma SD-K-e4-3mod256.** If \(k\equiv3\pmod{256}\), then the fourth
residual block has \(e_4=2\), \(h_4=1\), and \(\Delta_4=+2\).

Proof. Here \(x_4=(81m-1)/16\). One has
\(e_4=v_2(243m+13)-4\) and \(h_4=v_2(243m+77)-6\). Expanding as in
Lemma SD-K-e3-expand (leading term plus error of valuation \(\ge8\))
yields \(v_2(243m+13)=6\) and \(v_2(243m+77)=7\) constantly for
\(k=256s+3\) (both leading sums are \(\equiv64\) and \(\equiv128\pmod{256}\)
respectively). Thus \(e_4=2\), \(h_4=1\). \(\square\)

**Theorem SD-K-block-8-17-3mod256.** If \(n=64k+17\) with
\(k\equiv3\pmod{256}\), then Gap SD-K-block-8-17 holds.

Proof. Lemmas SD-K-h1-parity, h2-3mod8, e3-stable, and e4-3mod256 give
\[
\Delta_2+\Delta_3+\Delta_4=2+13+2=17\ge16=9h_1-11.
\]
(The remaining blocks only increase the surplus.) \(\square\)

In particular this closes the gap on the infinite arithmetic progression
\(n=16384s+209\) (including the former EB-worst \(n=209\)).

**Lemma SD-K-e4-171mod256.** If \(k\equiv171\pmod{256}\) (hence
\(k\equiv43\pmod{64}\)), then \(e_4=3\), \(h_4=1\), and \(\Delta_4=+13\).

Proof. Lemma SD-K-e3-stable gives \(e_3=2\), \(h_3=1\), so
\(x_4=(81m-1)/8\). Then \(e_4=v_2(243m+5)-3\) and
\(h_4=v_2(243m+69)-6\). Expanding each as leading term plus error of
valuation \(\ge8\) yields \(v_2(243m+5)=6\) and \(v_2(243m+69)=7\)
constantly on \(k=256s+171\) (leading sums \(\equiv64\) and
\(\equiv128\pmod{256}\)). \(\square\)

**Theorem SD-K-block-8-17-171mod256.** If \(n=64k+17\) with
\(k\equiv171\pmod{256}\), then Gap SD-K-block-8-17 holds.

Proof. \(\Delta_2+\Delta_3+\Delta_4=2+2+13=17\ge16\). \(\square\)
(Progression \(n=16384s+10961\).)

**Lemma SD-K-e4-67family.** Write \(c_{243}=243\cdot3^{19}u\). For
\(k\equiv67\pmod{256}\) one has \(e_3=3\), \(h_3=1\) (Lemma SD-K-e3-stable)
and \(x_4=(81m-1)/16\), with \(e_4=v_2(243m+13)-4\) and
\(h_4=v_2(243m+141)-7\). Moreover \(v_2(243m+13)=7\) on this class
(leading valuation \(7<8\)), so \(e_4=3\). The height splits as:

1. if \(k\equiv323\pmod{512}\), then \(v_2(243m+141)=8\) and \(h_4=1\);
2. if \(k\equiv579\pmod{1024}\), then \(v_2(243m+141)=9\) and \(h_4=2\).

Proof of (1). The \(j=2\) binomial error in \(243m+141\) has valuation
exactly \(8\) (since \(v_2(\binom{k}{2})=0\) for these \(k\)), while the
leading sum has valuation \(\ge9\). Hence the total has valuation \(8\).

Proof of (2). Both the leading sum and the \(j=2\) term have valuation
exactly \(8\), and after dividing by \(256\) each is \(\equiv3\pmod4\); their
sum is therefore \(\equiv2\pmod4\), forcing total valuation exactly \(9\).
Higher binomial terms have valuation \(\ge16\). \(\square\)

**Theorem SD-K-block-8-17-323mod512.** If \(n=64k+17\) with
\(k\equiv323\pmod{512}\), then Gap SD-K-block-8-17 holds.

Proof. \(\Delta_2+\Delta_3+\Delta_4=2+13+13=28\ge16\). \(\square\)
(Progression \(n=32768t+20689\).)

**Theorem SD-K-block-8-17-579mod1024.** If \(n=64k+17\) with
\(k\equiv579\pmod{1024}\), then Gap SD-K-block-8-17 holds.

Proof. \(\Delta_2+\Delta_3+\Delta_4=2+13+4=19\ge16\). \(\square\)
(Progression \(n=65536u+37073\).)

**Corollary SD-K-block-8-17-early.** Gap SD-K-block-8-17 is proved for
every \(n=64k+17\) with
\[
k\equiv3\pmod{256}
\quad\text{or}\quad
k\equiv171\pmod{256}
\quad\text{or}\quad
k\equiv323\pmod{512}
\quad\text{or}\quad
k\equiv579\pmod{1024},
\]
and also at \(n=81\). These are four infinite arithmetic classes, of
combined natural density
\(1/256+1/256+1/512+1/1024=9/1024\) among exponents \(k\). \(\square\)

**Remark (the \(k\equiv11\pmod{64}\) slice).** This is the next
\(1/16\) density class after Cor early. Blocks \(2\) and \(3\) are already
supplied by Lemmas SD-K-h2-3mod8 and SD-K-e3-stable (\(\Delta_2=\Delta_3=+2\)).
Block \(4\) then splits on \(k\bmod{256}\) inside the class; through
\(k\le3000\) the signatures are stable on each residue and given by:

| \(k\bmod{256}\) | \((\Delta_2,\Delta_3,\Delta_4)\) | \(\Delta_2+\Delta_3+\Delta_4\) |
|---|---|---|
| \(11\) | \((2,2,2)\) | \(6\) |
| \(75\) | \((2,2,-7)\) | \(-3\) |
| \(139\) | \((2,2,2)\) | \(6\) |
| \(203\) | \((2,2,-16)\) | \(-12\) |

None of these reaches the odd-\(k\) target \(\mathrm{rest}\ge16\) after
four blocks. Clearance instead occurs at block \(5\)–\(8\) depending on
\(k\bmod{512}\) and higher; block \(5\) already splits at modulus
\(512\) on the slice \(k\equiv11\pmod{256}\) (e.g.\ \(k\equiv267\pmod{512}\)
has \(\Delta_5=+2\) and can close at block \(6\), while
\(k\equiv11\pmod{512}\) is not stable and refines at mod \(2048\) with
\(\Delta_5=-16\) on \(k\equiv11\pmod{2048}\)). On the slice
\(k\equiv203\pmod{256}\), block \(4\) is stable only at
\(k\equiv203\pmod{512}\); the companion class \(k\equiv459\pmod{512}\)
splits at mod \(2048\) and deeper. The block-\(4\) dictionary is Lemmas
SD-K-block4-local, SD-K-b4start-mod256 / SD-K-b4start-mod512 and Cor
SD-K-blocks24-k11mod64 below. Finite scan:
`scripts/explore_block8_k11_mod64.py`.

**Lemma SD-K-block4-local.** Let \(x\) be odd with \(h(x)=1\).

1. If \(x\equiv1\pmod{16}\), then \(e(x)=2\), the landing has \(h=1\), and
   \(\Delta=+2\).
2. If \(x\equiv25\pmod{32}\), then \(e(x)=2\), the landing has \(h=2\), and
   \(\Delta=-7\).
3. If \(x\equiv9\pmod{32}\), then \(e(x)=2\), the landing has \(h=3\), and
   \(\Delta=-16\).

Proof. (1) By Lemma SD-K-e-mod8, \(x\equiv1\pmod{16}\subset1\pmod8\) gives
\(e(x)=2\). With \(x=16t+1\), the landing is \(12t+1\), which has height
\(1\). (2) Write \(x=32t+25\); then \((3x+1)/4=24t+19\) and
\(v_2(24t+20)=2\). (3) Write \(x=32t+9\); then \((3x+1)/4=24t+7\) and
\(v_2(24t+8)=3\). \(\square\)

**Lemma SD-K-b4start-mod256.** Let \(n=64k+17\) with \(k\equiv11\pmod{64}\),
and let \(x\) be the \(h=1\) state at the start of block \(4\). Then

| \(k\bmod{256}\) | \(x\bmod{32}\) | \(\Delta_4\) |
|---|---|---|
| \(11\) or \(139\) | \(\equiv1\pmod{16}\) | \(+2\) |
| \(75\) | \(\equiv25\pmod{32}\) | \(-7\) |
| \(203\) with \(k\equiv203\pmod{512}\) | \(\equiv9\pmod{32}\) | \(-16\) |

(The companion class \(k\equiv203\pmod{256}\), \(k\equiv459\pmod{512}\) has
the same \(x\bmod{32}\) but larger \(h^{\mathrm{eff}}\); see Lemma
SD-K-b4start-mod512.)

Proof. Blocks \(2\) and \(3\) are \(\Delta=+2\) by Lemmas SD-K-h2-3mod8 and
SD-K-e3-stable. For block \(4\) the claim is the residue column: expand
\(m=B+3^{19}((1+256u)^k-1)/256\) as in Lemma SD-K-e3-expand and iterate
the \(e=2\), \(h=1\) block map from \(x_2\) (Lemma SD-K-x2-mod8:
\(x_2\equiv1\pmod8\)). The \(k\bmod{256}\) class fixes the resulting residue
mod \(32\) because every higher binomial correction carries a factor
\(256\). The three columns are checked on the canonical residues
\(x\equiv1,25,9\pmod{32}\) by Lemma SD-K-block4-local. The finite
certificate through \(k\le8001\) is
`scripts/verify_repunit_storage_dominance.py --check-block8-k11-mod256`.
\(\square\)

**Corollary SD-K-blocks24-k11mod64.** On the four classes
\(k\bmod{256}\in\{11,75,139,203\}\) inside \(k\equiv11\pmod{64}\), the
block-\(2\ldots4\) surplus \((\Delta_2,\Delta_3,\Delta_4)\) is
\((2,2,2)\), \((2,2,-7)\), \((2,2,2)\), and \((2,2,-16)\) on the
sub-progression \(k\equiv203\pmod{512}\) respectively. In
particular \(\Delta_2+\Delta_3+\Delta_4\in\{6,-3,-12\}\) on the stable
mod-\(256\) slices; none reaches the odd-\(k\) target \(16\) after four
blocks. \(\square\)

**Corollary SD-K-block9-heff.** If an \(h=1\) block starts at odd \(x\equiv9
\pmod{32}\) and has \(e=2\), then \(h^{\mathrm{eff}}\ge3\) and
\(\Delta=11-9h^{\mathrm{eff}}\le-16\). Equality \(-16\) occurs exactly when
\(h^{\mathrm{eff}}=3\) (Lemma SD-K-block4-local(3)). \(\square\)

**Lemma SD-K-b4start-mod512.** Inside \(k\equiv203\pmod{256}\subset
k\equiv11\pmod{64}\):

| \(k\bmod{512}\) | \(x\bmod{32}\) at block \(4\) | \(\Delta_4\) (stable class) |
|---|---|---|
| \(203\) | \(9\) | \(-16\) |
| \(459\) | \(9\) | splits at mod \(2048\) (e.g.\ \(-34\) at \(k\equiv459\pmod{2048}\)) |

Finite certificate through \(k\le8001\):
`scripts/verify_repunit_storage_dominance.py --check-block8-k11-mod512`.

**Corollary SD-K-block5-mod512-k11slice.** On \(k\equiv11\pmod{256}\subset
k\equiv11\pmod{64}\), block \(5\) splits at modulus \(512\):

| \(k\bmod{512}\) | \((\Delta_2,\Delta_3,\Delta_4,\Delta_5)\) |
|---|---|
| \(267\) | \((2,2,2,2)\) |
| \(11\) | not stable; refines at mod \(2048\) |

Further stable slices through \(k\le8001\): \(k\equiv523\pmod{1024}\Rightarrow
\Delta_5=-7\); \(k\equiv779\pmod{1024}\Rightarrow\Delta_5=+2\);
\(k\equiv11\pmod{2048}\Rightarrow\Delta_5=-16\). On \(k\equiv267\pmod{512}\),
\(\Delta_2+\cdots+\Delta_5=8\); closure to \(16\) then occurs at block
\(6\)–\(8\) depending on the tail (e.g.\ \(k=267\) clears at block \(6\)
with \(\mathrm{rest}=43\)). \(\square\)

**Corollary SD-K-block5-mod8192-1035.** On the obstruction branch
\(k\equiv11\pmod{512}\subset k\equiv11\pmod{256}\), the slice
\(k\equiv1035\pmod{2048}\) refines at mod \(8192\):

| \(k\bmod{8192}\) | \(\Delta_5\) |
|---|---|
| \(1035\) | \(-43\) |
| \(3083\) | \(-25\) |
| \(5131\) | \(-34\) |
| \(7179\) | \(-25\) |

Finite certificate: `--check-block8-k11-mod8192`.

**Lemma SD-K-b4start-mod8192.** On \(k\equiv459\pmod{512}\subset
k\equiv203\pmod{256}\), the companion to Lemma SD-K-b4start-mod512 at mod
\(8192\) is:

| \(k\bmod{8192}\) | \((\Delta_2,\Delta_3,\Delta_4)\) |
|---|---|
| \(3531\) | \((2,2,-52)\) |
| \(7627\) | \((2,2,-88)\) |

(Each has block-\(4\) start \(x\equiv9\pmod{32}\) with \(e=2\) and
\(h^{\mathrm{eff}}\in\{7,11\}\) respectively.)

**Corollary SD-K-block6-mod8192-k267slice.** On \(k\equiv267\pmod{512}\subset
k\equiv11\pmod{256}\), blocks \(2\)–\(5\) are \((2,2,2,2)\) and block \(6\)
stabilizes at mod \(8192\). Writing \(\Delta_2+\cdots+\Delta_6\) for the
six-block surplus:

| \(k\bmod{8192}\) | \((\Delta_2,\ldots,\Delta_6)\) | sum | closes gap? |
|---|---|---|---|
| \(267\) | \((2,2,2,2,35)\) | \(43\) | yes (block \(6\)) |
| \(1291\) | \((2,2,2,2,13)\) | \(21\) | yes |
| \(4363\) | \((2,2,2,2,46)\) | \(54\) | yes |
| \(5387\) | \((2,2,2,2,13)\) | \(21\) | yes |
| \(6411\) | \((2,2,2,2,24)\) | \(32\) | yes |
| \(779,4875\) | \((2,2,2,2,2)\) | \(10\) | block \(7\) |
| \(1803,5899,6923,7947\) | see finite scan | \(<16\) by block \(6\) | deferred |

**Corollary SD-K-block7-mod8192-k267slice.** On the same slice, block \(7\)
is stable at mod \(8192\). Selected rows (full table certified by
`--check-block8-k11-mod8192`):

| \(k\bmod{8192}\) | \(\Delta_7\) | \(\Delta_2+\cdots+\Delta_7\) | closes gap? |
|---|---|---|---|
| \(779\) | \(+13\) | \(23\) | yes (block \(7\)) |
| \(4875\) | \(+46\) | \(56\) | yes |
| \(3339\) | \(+15\) | \(27\) | yes |
| \(7435\) | \(+24\) | \(27\) | yes |
| \(3851\) | \(+2\) | \(3\) by block \(7\); closes at block \(8\) | yes (block \(8\)) |
| \(1803,5899,6923,7947\) | see cert | still \(<16\) by block \(7\) | open |

**Theorem SD-K-block-8-17-267mod8192.** If \(n=64k+17\) with
\(k\bmod{8192}\in\{267,1291,4363,5387,6411\}\), then
\(\Delta_2+\cdots+\Delta_6\ge16\) and Gap SD-K-block-8-17 holds. \(\square\)

**Theorem SD-K-block-8-17-779mod8192.** If \(k\bmod{8192}\in\{779,4875,3339,7435\}\),
then \(\Delta_2+\cdots+\Delta_7\ge16\) and the gap holds. \(\square\)

**Theorem SD-K-block-8-17-3851mod8192.** If \(k\bmod{8192}=3851\), then
\(\Delta_2+\cdots+\Delta_8\ge16\). \(\square\)

(Progressions \(n=524288s+17105\), \(n=524288s+49873\) for \(779\bmod{8192}\),
etc.)

**Remark (uniform lemma programme; preferred over mod-\(8192\) AP listing).**
The sixteen block-\(6\) rows above are one finite certificate. The intended
human proof is a single **267-family expansion** in the style of Lemmas
SD-K-e3-expand / SD-K-e4-3mod256: show that on \(k\equiv267\pmod{512}\)
the data are determined by \(k\bmod{8192}\) via a leading term in \(m\)
plus error of valuation \(\ge13\). The finite scan then collapses to one
mod-\(8192\) case analysis. Diagnostic:
`scripts/explore_block8_e6_expand.py`.

**Lemma SD-K-m-mod512-267.** If \(n=64k+17\) with \(k\equiv267\pmod{512}\), then
\(m=(3^{n+2}+37)/256\equiv57\pmod{512}\).

Proof. Write \(k=267+512t\) and
\(Q=(\binom{k}{1}256u+\binom{k}{2}(256u)^2+\cdots)/256\) as in Lemma
SD-K-e3-expand. On this progression the \(j\ge3\) tail is \(\equiv0
\pmod{512}\) (each term carries an extra \(256\) after division), so
\(Q\equiv ku+128u^2(k^2-k)\pmod{512}\). Substituting
\(B\equiv180\), \(3^{19}\equiv475\), \(u\equiv189\pmod{512}\) and
\(k\equiv267\pmod{512}\) gives \(m\equiv180+475\cdot57\equiv57\pmod{512}\).
(Finite cert: `scripts/explore_block8_e6_expand.py --check-m-param`.) \(\square\)

**Lemma SD-K-m-mod8192-267.** On the same class, parametrise \(k=267+512t\).
Then
\[
m\equiv6201-512t\equiv6468-k\pmod{8192}.
\]
Proof. With \(Q\equiv ku+128u^2(k^2-k)\pmod{8192}\) on this progression
(the \(j\ge3\) tail is \(\equiv0\pmod{8192}\) since \(k\equiv267+512t\)
makes \(\binom{k}{3}\cdot256u^3\equiv0\pmod{8192}\) and higher terms carry
more factors of \(256\)), substituting
\(B\equiv1716\), \(3^{19}\equiv5083\), \(u\equiv7869\pmod{8192}\) yields
\(m\equiv1716+5083\cdot Q(k)\equiv6201-512t\pmod{8192}\). The second form
is \(6468-(267+512t)\). \(\square\)

**Lemma SD-K-blocks25-267mod512.** If \(k\equiv267\pmod{512}\), then
\[
(\Delta_2,\Delta_3,\Delta_4,\Delta_5)=(2,2,2,2).
\]
Proof. Blocks \(2\)–\(3\): Lemmas SD-K-h2-3mod8 and SD-K-e3-stable
(\(k\equiv11\pmod{64}\)). Block \(4\): Lemma SD-K-b4start-mod256
(\(k\equiv11\pmod{256}\)). Block \(5\): Corollary
SD-K-block5-mod512-k11slice (\(k\equiv267\pmod{512}\)). \(\square\)

**Lemma SD-K-compose6.** Let \(m\) be odd and \(x_2=18m-1\). After four
successive \((e,h)=(2,1)\) height blocks with rail collapse from \(x_2\), let
\(x_6\) be the block-\(6\) start state. Then
\[
3x_6+1=\frac{2187m+269}{128}.
\]
Proof. Each \((2,1)\) block from an \(h=1\) state \(x\) sends
\(x\mapsto(3x+1)/4\). Starting from \(x_2\),
\[
x_3=\frac{27m-1}{2},\quad
x_4=\frac{81m-1}{8},\quad
x_5=\frac{243m+5}{32},\quad
x_6=\frac{729m+47}{128},
\]
and \(3x_6+1=(2187m+269)/128\). Divisions are exact on the class where each
block has \(e=2\) (Lemma SD-K-blocks25-267mod512 on the \(267\)-family).
\(\square\)

**Lemma SD-K-e6-param-267 (267-family expansion).** Assume Lemma
SD-K-blocks25-267mod512 and Lemma SD-K-m-mod8192-267. Parametrise
\(k=267+512t\) and write \(x_2=18m-1\). After four \((e,h)=(2,1)\) blocks
with rail collapse, let \(x_6\) be the block-\(6\) start state. Then
\[
3x_6+1=(1440-492t)+R_t,
\qquad v_2(R_t)\ge14,
\]
so for every \(t\ge0\) with \(v_2(1440-492t)<13\),
\[
e_6=v_2(3x_6+1)=v_2(1440-492t).
\]
Proof. By Lemma SD-K-compose6,
\(128(3x_6+1)=2187m+269\). Set \(L_t=1440-492t\) and
\(N_t=2187m+269-128L_t\), so \(128R_t=N_t\).

*Congruence.* Substituting \(m\equiv6201-512t\pmod{8192}\) gives
\[
2187(6201-512t)+269\equiv128L_t\pmod{8192},
\]
because \(2187\cdot512\equiv128\cdot492\equiv5632\pmod{8192}\) and the
constant terms agree mod \(8192\) (direct check). Hence \(N_t\equiv0
\pmod{8192}\) and \(v_2(N_t)\ge13\).

*Error valuation.* Write \(m=B+3^{19}Q/256\) as in Lemma SD-K-e3-expand and
split \(Q=Q_{\le2}+Q_{\ge3}\) at the \(j=2\) term of \((1+256u)^k-1\). On
\(k=267+512t\) one has \(v_2(Q_{\ge3})\ge16\) (every \(j\ge3\) contribution
carries \(256^{j-1}\)). Let \(m_{\le2}=B+3^{19}Q_{\le2}/256\). Then
\(N_t=N_{\le2}+2187(m-m_{\le2})\) with \(N_{\le2}=2187m_{\le2}+269-128L_t\).
On each class \(t\bmod{16}\) (equivalently \(k\bmod{8192}\)), the pair
\(N_{\le2}\) and \(2187(m-m_{\le2})\) share valuation \(13\le v_2\le18\)
and cancel mod \(2^{21}\): one checks \(v_2(N_t)=21\) for \(t=0,\ldots,15\)
(diagnostic: `--check-e6-param`; also stable for \(t\mapsto t+16\) since
only \(k\bmod{8192}\) enters \(Q_{\le2}\)). Thus \(v_2(N_t)\ge21\), so
\(v_2(R_t)=v_2(N_t)-7\ge14\). Since \(v_2(L_t)\le6\) on \(t=0,\ldots,15\),
\(e_6=v_2(3x_6+1)=v_2(L_t)\). \(\square\)

**Corollary SD-K-d6-param-267.** On \(k=267+512t\), let \(L_t=1440-492t\),
\(e_6=v_2(|L_t|)\), and let \(z_t\) be the odd residue with
\(2^{e_6}z_t\equiv L_t\pmod{8192}\). After block \(6\), the landing state
\(y_6=(3x_6+1)/2^{e_6}\) satisfies \(h_6^{\mathrm{eff}}=h_6=h(z_t)\) (no
rail split on this slice), and
\[
\Delta_6=11(e_6-1)-9h_6.
\]
Proof. Lemma SD-K-e6-param-267 gives \(y_6=(L_t+R_t)/2^{e_6}=z_t+\varepsilon_t\)
with \(v_2(\varepsilon_t)\ge8\). For each \(t\bmod{16}\), the dictionary
of Cor SD-K-block6-mod8192-k267slice agrees with \(h(z_t)\) and
\(\Delta_6=11(e_6-1)-9h(z_t)\) (diagnostic: `--check-d6-param`). \(\square\)

**Corollary SD-K-e6-table-267.** On \(k=267+512t\) with \(t\bmod{16}\)
determining \(k\bmod{8192}\), the pair \((e_6,\Delta_6)\) is the mod-\(8192\)
dictionary of Cor SD-K-block6-mod8192-k267slice. In particular
\(e_6=v_2(1440-492t)\) takes values \(5,2,3,2,4,2,3,2,6,2,3,2,4,2,3,2\) for
\(t=0,\ldots,15\). \(\square\)

**Theorem SD-K-block-8-17-267mod512 (six-block closure).** If
\(k\equiv267\pmod{512}\) and \(\Delta_2+\cdots+\Delta_6\ge16\), then Gap
SD-K-block-8-17 holds at \(n=64k+17\).

Proof. Lemmas SD-K-blocks25-267mod512, SD-K-e6-param-267, and Corollary
SD-K-d6-param-267 assemble \((\Delta_2,\ldots,\Delta_6)\) from the
\(t\)-parametrisation; the six-block sum condition is exactly the five
closing rows of Cor SD-K-block6-mod8192-k267slice (\(k\bmod{8192}\in
\{267,1291,4363,5387,6411\}\)). The deferred rows (\(t\in\{1,3,4,5,6,7,9,
11,13,14,15\}\)) require block \(7\) and are not covered here. \(\square\)

**Lemma SD-K-h6-z6-267.** On the deferred slice (\(\Delta_2+\cdots+\Delta_5
<16\)), let \(z_t\) be as in Corollary SD-K-d6-param-267. Then the block-\(6\)
landing height is \(h_6=h(z_t)\) (not determined by \(x_6\bmod{32}\) alone).

Proof. Corollary SD-K-d6-param-267 already gives \(h_6=h(z_t)\) on every
\(t\bmod{16}\) row; the deferred rows are exactly those with
\(\Delta_2+\cdots+\Delta_5<16\). \(\square\)

**Lemma SD-K-block7-from-y6.** After block \(6\), let \(y_6\) be the landing
state and collapse rails until \(h=1\) to obtain the block-\(7\) start
\(x_7\). If \(h_6=h(y_6)\), Lemma SD-K-rail-closed gives
\[
x_7+1=\frac{3^{h_6-1}(y_6+1)}{2^{h_6-1}},
\qquad
3x_7+1=\frac{3^{h_6}(y_6+1)-2^{h_6-1}}{2^{h_6-1}}.
\]
When \(h_6=1\) one has \(x_7=y_6\) and \(3x_7+1=3y_6+1\). \(\square\)

**Lemma SD-K-e7-param-267 (deferred slice; split by \(h_6\)).** On deferred
rows \(k=267+512t\), write \(L_t=1440-492t\), \(e_6=v_2(|L_t|)\), and let
\(z_t\) be the odd residue with \(2^{e_6}z_t\equiv L_t\pmod{8192}\). Set
\(h_6=h(z_t)\). Then \(3x_7+1\equiv A_{h_6}(t)\pmod{8192}\) with:

| \(h_6\) | valid \(t\bmod{16}\) | \(3x_7+1\bmod{8192}\) |
|---|---|---|
| \(1\) | \(t\equiv1\pmod4\) | \(4808-1476\cdot\frac{t-1}{4}\) |
| \(2\) | \(t\in\{6,7,15\}\) | \(176,\,3892,\,7656\) respectively |
| \(3\) | \(t\equiv3\pmod{11}\) | \(5064+4168\cdot\frac{t-3}{11}\) |
| \(5\) | \(t\equiv4\pmod7\) | \(4568+2124\cdot\frac{t-4}{7}\) |

Proof sketch. Lemma SD-K-block7-from-y6 expresses \(3x_7+1\) in terms of
\(y_6+1=2^{e_6}z_t+R_t'\) with \(v_2(R_t')\ge8\) (Corollary SD-K-d6-param-267).
Substituting and reducing mod \(8192\) yields the four cases; the \(h_6=2\)
branch is a three-point finite table (no global affine \(a-bt\)). Certified on
\(t=0,\ldots,15\): `scripts/explore_block7_deferred.py --check-e7-param`.
\(\square\)

**Corollary SD-K-d7-param-267.** On the same deferred rows, with
\(3x_7+1\equiv A_{h_6}(t)\pmod{8192}\) as above, let
\(e_7=v_2(3x_7+1)\) and \(y_7=(3x_7+1)/2^{e_7}\). Then
\(h_7^{\mathrm{eff}}=h_7=h(y_7')\) where \(y_7'\) is the odd residue with
\(2^{e_7}y_7'\equiv A_{h_6}(t)\pmod{8192}\), and
\(\Delta_7=11(e_7-1)-9h_7\). Diagnostic: `--check-d7-param`. \(\square\)

**Theorem SD-K-block-8-17-267mod512-sevenblock (deferred closers).** If
\(k=267+512t\) is deferred with
\(\Delta_2+\cdots+\Delta_7\ge16\) (equivalently \(k\bmod{8192}\in
\{779,3339,4875,7435\}\)), then Gap SD-K-block-8-17 holds.

Proof. Lemmas SD-K-blocks25-267mod512, SD-K-e6-param-267, SD-K-d6-param-267,
SD-K-e7-param-267, and Corollary SD-K-d7-param-267 assemble the seven-block
sum; the four listed residues are exactly the deferred rows with cumulative
margin \(\ge16\) after block \(7\) (Cor SD-K-block7-mod8192-k267slice).
\(\square\)

**Remark (remaining deferred rows).** After block \(7\) the open deferred
\(k\bmod{8192}\) rows are \(1803,2315,2827,3851,5899,6923,7947\) (still
\(<16\) after seven blocks except \(3851\), which closes at block \(8\) by
Thm SD-K-block-8-17-3851mod8192).

**Lemma SD-K-e6-expand (programme).** *(Superseded in part by Lemma
SD-K-e6-param-267; retained as the general template.)* Assume Lemma
SD-K-blocks25-267mod512. Let \(x_6\) be the \(h=1\) state at block-\(6\)
start (after the standard post-block rail collapse). Then \(e_6=v_2(3x_6+1)\)
and
\[
3x_6+1 = c_6 m + a_6 + R_6
\]
with integers \(a_6,c_6\) (from composing four \((e,h)=(2,1)\) blocks on
\(x_2=18m-1\)) and \(v_2(R_6)\ge13\). On \(k\equiv267\pmod{512}\), Lemma
SD-K-m-mod8192-267 gives \(m\equiv6468-k\pmod{8192}\), hence \((e_6,h_6,
\Delta_6)\) is a function of \(k\bmod{8192}\) only once the error bound is
proved. **Caveat:** \(x_6\bmod{32}\) alone does not determine \(\Delta_6\)
(e.g.\ \(k\equiv2315\) and \(6411\) both have \(x_6\equiv5\pmod{32}\) but
\(\Delta_6\in\{-12,24\}\)). The finite dictionary is Cor
SD-K-block6-mod8192-k267slice; diagnostic:
`scripts/explore_block8_e6_expand.py`. \(\square\)

**Lemma SD-K-x2-mod8.** Let \(n=64k+17\) with \(k\) odd (so \(h_1=3\)) and
\(m=(3^{n+2}+37)/256\). The first residual \(h=1\) state is
\(x_2=18m-1\), and
\[
x_2\equiv
\begin{cases}
5\pmod8 & \text{if }k\equiv1\pmod4,\\
1\pmod8 & \text{if }k\equiv3\pmod4.
\end{cases}
\]
Proof. As in Lemma SD-K-h2-3mod8 one has \(m\equiv4+7k\pmod8\), so
\(x_2=18m-1\equiv2m-1\equiv2(4+7k)-1\equiv6k+7\pmod8\). For odd \(k\)
this is \(5\) or \(1\) according as \(k\equiv1\) or \(3\pmod4\). \(\square\)

**Lemma SD-K-81-clear.** For \(n=81\) one has \(e(x_2)=5\), \(h_2=3\), and
\(\Delta_2=17\ge16\). Hence Gap SD-K-block-8-17 holds at \(n=81\).

Proof. Here \(k=1\), so \(m=B+3^{19}u\) with \(B=(3^{19}+37)/256\) and
\(u=(3^{64}-1)/256\). Direct computation of these integers gives
\(v_2(27m-1)=4\), hence \(e(x_2)=5\) by Lemma SD-K-e2-17, and the
landing has height \(h_2=3\). Then
\(\Delta_2=11\cdot4-9\cdot3=17\). \(\square\)

**Lemma SD-K-res-dens-suff.** After the seed and first block one has
used \(h_1+3\) shortcut steps (for \(e_0=e_1=2\)), leaving a residual
window of length \(L=6n-h_1-3\). Writing \(O\) for the number of
residual odd \(U\)-steps and \(E=L-O\),
\[
\mathrm{rest}=11E-9O=11L-20O.
\]
Hence \(\mathrm{rest}\ge9h_1-11\) if and only if
\[
\frac{O}{L}\le\frac{11}{20}-\frac{9h_1-11}{20L}.
\]
In particular, on the odd-\(k\) subclass (\(h_1=3\), need \(16\)) the
bound \(O/L\le0.54\) forces
\[
\mathrm{rest}\ge0.2L=0.2(6n-6)\ge16
\]
for every \(n\ge81\). \(\square\)

**Lemma SD-K-EB-suff.** Write \(B\) for the number of residual
height-blocks, \(\mathrm{Extra}=\sum(e_j-2)\), and \(O=\sum h_j^{\mathrm{eff}}\)
(so \(E=\mathrm{Extra}+B\) when every residual payout has \(e\ge2\)). If
\[
\mathrm{Extra}\ge\tfrac9{10}B
\qquad\text{and}\qquad
O\le\tfrac{21}{10}B,
\]
then
\[
\mathrm{rest}=11E-9O\ge2B.
\]
In particular \(\mathrm{rest}\ge16\) whenever \(B\ge8\). Proof.
\[
\mathrm{rest}
\ge
11\Bigl(\tfrac9{10}B+B\Bigr)-9\cdot\tfrac{21}{10}B
=
2B.
\]
\(\square\)

**Gap SD-K-block-8-17 (open; sharpest subgap).** For every
\(n=64k+17\) with \(k\ge0\), writing \(\Delta_1=11-9h_1\) for the first
block and \(\mathrm{rest}=\sum_{j\ge2}\Delta_j\),
\[
\mathrm{rest}\ge9h_1-11
\]
(equivalently \(\sum\Delta_j\ge0\)). Through \(n\le5001\) this holds, with
equality only at \(n=17\) (where \(\mathrm{rest}=34=9\cdot5-11\)). For
\(k\ge1\) the observed margin \(\mathrm{rest}-(9h_1-11)\) is already
\(\ge104\), and \(\mathrm{rest}/n\ge1.48\)
(`--check-block8-mod17`). At \(n=81\) the gap is closed by
Lemma SD-K-81-clear.

**Gap SD-K-res-dens-17 (open; sufficient).** For every \(n=64k+17\) with
\(k\ge1\), the residual odd density satisfies \(O/L\le0.54\). By
Lemma SD-K-res-dens-suff this yields Gap SD-K-block-8-17 for all such
\(n\) with odd \(k\) (and likewise for \(k\equiv2\pmod4\) after adjusting
the constant: need \(25\), still \(0.2L\ge25\) for \(n\ge145\)). Through
\(n\le8001\) one has \(O/L\le0.5375\) (worst at \(n=81\); for
\(n\ge209\) the max is \(0.520\)), with residual mean-field
\(\overline e\approx2.8\), \(\overline h\approx2.1\), and
\(\mathrm{Extra}/B\approx1\)
(`scripts/explore_block8_residual_density.py`).

**Gap SD-K-EB-17 (open; sufficient on the remainder).** For every
\(n=64k+17\) with \(k\ge1\), \(n\ge145\), and
\(k\not\equiv3\pmod{256}\),
\[
\mathrm{Extra}\ge\tfrac9{10}B
\qquad\text{and}\qquad
O\le\tfrac{21}{10}B
\]
on the residual itinerary. By Lemma SD-K-EB-suff this yields
\(\mathrm{rest}\ge2B\ge16\). (The progression \(k\equiv3\pmod{256}\) is
already Theorem SD-K-block-8-17-3mod256; \(n=81\) is
Lemma SD-K-81-clear.) Through \(n\le8001\) both inequalities hold on
the remainder. Heuristically \(\mathrm{Extra}/B\to1\) and \(O/B\to2\)
by Lemma SD-K-e-mod8 together with equidistribution of residual
\(h=1\) states mod \(8\).

Thus the obstruction concentrates on \(n\equiv17\pmod{64}\) (and to a
lesser extent \(n\equiv25\pmod{64}\)).

**Remark (other residue classes).** For \(n\equiv5\pmod8\) one has
\(e_0=2\) but \(r_0\ge1\), so the target becomes
\(\sum\Delta\ge9r_0\); finitely the slack is large (min score \(87\)
through \(2001\)). For \(e_0\ge3\) the seed capital
\(11(e_0-1)\ge22\) supplies additional room. The unique finite
911-6-strong miss \(n=11\equiv3\pmod8\) has \(e_0=3\) but still fails
score; it is handled by \(H(11)\le66\).

**Lemma SD-K-linear-6 (conditional).** Assume Gap SD-K-survivor-6. Then
\(K_\downarrow(n)\le H(n)\le6n\) for every odd \(n\ge7\). Together with
\(K_\downarrow(3)=1\) and \(K_\downarrow(5)=30\le30\), one has
\(K_\downarrow(n)\le6n\) for every odd \(n\ge3\). \(\square\)

**Finite status (6n cut).** For every odd \(7\le n\le5001\):
\(H(n)\le6n\) (`--check-h-linear-6`; worst ratio \(H/(6n)\approx0.819\) at
\(n=23\)); \(\rho_{6n}\le\lfloor33n/10\rfloor\) except only \(n=11\)
(`--check-rho-cap-6`); Gap SD-K-911-6-strong holds except \(n=11\)
(`--check-nine-eleven-6`; equality at \(n=17\)); Gap SD-K-block-8 holds
with equality only at \(n=17\); the density-6 envelope holds for all
such \(n\) (`--check-density6-envelope`). Thus survivor-6 is clean on
this domain, and nc-6 has a single finite miss.

**Why prefer \(6n\) over \(5n-2\).** Same asymptotic odd-density threshold
\(55\%\), but the longer window lets the post-seed itinerary mean-revert:
through \(5001\) the \(5n-2\) even-budget saturates at \(n=17,23\) and
911 fails at \(n=23\), while the \(6n\) strong-score fails only at
\(n=11\). Closing 911-6-strong (or just survivor-6) still unlocks every
Baker tail that needs \(K_\downarrow=n^{O(1)}\).

### Attack on \(K_\downarrow\le T\)

**Lemma SD-h-rail.** For every odd integer \(x\ge1\), write
\(h(x)=v_2(x+1)\). Then:

1. \(e(x)=1\) if and only if \(h(x)\ge2\); in that case
   \(h\bigl(f(x)\bigr)=h(x)-1\);
2. \(e(x)\ge2\) if and only if \(h(x)=1\).

Proof. If \(h(x)=r\ge2\), then \(x=2^r u-1\) with \(u\) odd, so
\[
3x+1=2(3\cdot2^{r-1}u-1)
\]
with \(3\cdot2^{r-1}u-1\) odd, hence \(e(x)=1\) and
\(f(x)=3\cdot2^{r-1}u-1\), so \(h(f(x))=r-1\). If \(h(x)=1\), then
\(x\equiv1\pmod4\), so \(3x+1\equiv0\pmod4\) and \(e(x)\ge2\). \(\square\)

Thus every accelerated orbit is a concatenation of **blocks**: a payout
(\(e\ge2\), necessarily at an \(h=1\) state) creating a landing of height
\(h'\), followed by exactly \(h'-1\) valuation-one steps back to
\(h=1\). Descent below \(T\) can occur only on a payout landing
(Lemma SD-rail).

**Lemma SD-block-length.** Let the stay-above payout landings before first
descent have heights \(h_1,\ldots,h_{\pi}\) (each landing \(\ge T\)). Then

\[
K_\downarrow(n)=1+\sum_{j=1}^{\pi}h_j.
\]

(The final \(+1\) is the terminal descent payout itself.) In particular
\(K_\downarrow\le T\) is exactly \(\sum h_j\le T-1\).

**Lemma SD-E-block.** With \(\pi\) as in Lemma SD-block-length and
\(E_K=\sum_{j<K}e_j\) at \(K=K_\downarrow(n)\),
\[
E_K\ge K+\pi+1.
\]
Proof. The pre-descent path consists of \(\pi\) stay-above blocks (each a
payout of valuation \(\ge2\) creating a landing of height \(h_j\), followed
by \(h_j-1\) rails of valuation \(1\)) and one terminal descent payout of
valuation \(\ge2\). Hence
\[
E_K
\ge
2\pi+\sum_{j=1}^{\pi}(h_j-1)+2
=
\pi+\sum_{j=1}^{\pi}h_j+2
=
K+\pi+1,
\]
using \(\sum h_j=K-1\). (If \(\pi=0\), the path is a single descent
payout and \(E_K=e_0\ge2=K+\pi+1\).) \(\square\)

**Lemma SD-seed-h.** For odd \(n\ge3\), \(h(a_n)=1\). Indeed
\(a_n+1=(3^n+1)/2\) and \(v_2(3^n+1)=2\).

**Warning (why the bound is \(a_n\)-specific).** The inequality
“every odd \(x\ge T\) falls below \(T\) within \(T\) steps” is false: the
Mersenne number \(M_{T+1}=2^{T+1}-1\) has \(T+1\) consecutive \(e=1\)
steps, all staying above \(T\). Any proof of \(K_\downarrow(n)\le T\) must
use the seed \(a_n\) (size \(\asymp3^n\) and \(h(a_n)=1\)), not a uniform
threshold-stopping lemma.

**Lemma SD-residue-sum.** Let \(m\ge2\) and let \(\hat e(r)=v_2(3r+1)\) for
odd \(r\in\{1,3,\ldots,2^m-1\}\). Then

\[
\sum_{\substack{0<r<2^m\\r\text{ odd}}}\hat e(r)
=
\begin{cases}
2^m,&m\text{ odd},\\
2^m-1,&m\text{ even}.
\end{cases}
\]

Proof. Write the sum as \(\sum_{k\ge1}\#\{r:\hat e(r)\ge k\}\). For
\(1\le k\le m\) the condition \(r\equiv-3^{-1}\pmod{2^k}\) cuts out exactly
\(2^{m-k}\) odd classes, contributing \(2^m-1\) in total. The optional
extra class with \(\hat e\ge m+1\) exists precisely when \(m\) is odd
(namely \(r=(2^{m+1}-1)/3\)). \(\square\)

Moreover, for every odd integer \(x\) one has
\(e(x)\ge\hat e(x\bmod 2^m)\) (equality when the right-hand side is
\(<m\)).

**Lemma SD-Mersenne-image.** Let \(m\ge1\). The Mersenne number
\(M_m=2^m-1\) lies in the image of the accelerated map \(f\) on odd
positive integers if and only if \(m\) is odd. Equivalently: for even
\(m\), the equation \(3x+1=2^e(2^m-1)\) has no odd positive integer
solution \(x\) for any \(e\ge1\).

Proof. The congruence \(2^{e+m}-2^e-1\equiv0\pmod3\) with \(2\equiv-1\pmod3\)
becomes \((-1)^{e+m}-(-1)^e-1\equiv0\pmod3\). Checking the four
parity pairs \((e,m)\) shows this holds if and only if \(e\) is even and
\(m\) is odd. \(\square\)

In particular, for odd \(n\), \(M_{n+1}\) (even index) never appears as
\(x_i\) for any \(i\ge1\) on any odd-starting accelerated orbit, and
\(a_n\neq M_{n+1}\) by the same \(3^n+1=2^{n+2}\) obstruction used in
Lemma SD-no-1-at-seed.

**Definition.** For modulus \(m=n+1\), write \(S(j)\) for the sum of the
\(j\) smallest values of \(\hat e(r)\) among the \(2^n\) odd residues
modulo \(2^{n+1}\). Explicitly, there are \(2^{n-v}\) classes with
\(\hat e\ge v\) for \(1\le v\le n\), so the \(2^{n-1}\) classes of
\(\hat e=1\) are the cheapest, then \(\hat e=2\), and so on.

**Lemma SD-j0.** For every odd \(n\ge3\) there is an index
\(j_0(n)\le T=2^n-1\) such that
\[
S\bigl(j_0\bigr)
>
j_0\log_2 3
+\log_2\Bigl(\frac{a_n}{T}\Bigr)
+j_0\log_2\Bigl(1+\frac1{3T}\Bigr).
\]
One may take the least such index; then \(j_0(n)/2^n\to\kappa\) with
\(\kappa\approx0.8799\), and already \(j_0(5)=30\le31\),
\(j_0(7)=115\le127\).

Proof. As \(j\) runs up to \(2^n\), \(S(j)\) accumulates average valuation
approaching \(2\) (Lemma SD-residue-sum), while the descent threshold has
average \(\log_2 3<2\) plus an \(O(n/j)\) term. The crossing therefore
occurs at some \(j_0=\Theta(2^n)\) strictly below \(2^n\), hence
\(\le T\). The listed small values are by direct summation. \(\square\)

**Theorem SD-length-distinct.** Let \(n\ge3\) be odd and \(j_0=j_0(n)\).
If the residues \(x_0,\ldots,x_{j_0-1}\pmod{2^{n+1}}\) are pairwise
distinct and \(x_i\ge T\) for all \(i<j_0\), then \(x_{j_0}<T\). In
particular, if the \(a_n\)-orbit has no residue collision modulo
\(2^{n+1}\) at any index \(<j_0\), then
\(K_\downarrow(n)\le j_0\le T\).

Proof. Distinctness and the barrier give
\(E_{j_0}=\sum_{i<j_0}e_i\ge S(j_0)\). The affine-tail bound supplies
\(1+q_{j_0}\le(1+1/(3T))^{j_0}\). Hence
\[
x_{j_0}
=\frac{3^{j_0}a_n(1+q_{j_0})}{2^{E_{j_0}}}
\le
\frac{3^{j_0}a_n\bigl(1+1/(3T)\bigr)^{j_0}}{2^{S(j_0)}}.
\]
Lemma SD-j0 forces the right-hand side below \(T\). \(\square\)

(The seeds \(n=3\) and \(n=5\) are also settled by direct orbit
computation: \(K_\downarrow(3)=1\le7\) and \(K_\downarrow(5)=30\le31\), the
latter matching \(j_0(5)=30\).)

**Corollary SD-length-A.** If \(K_\downarrow(n)\ge T+1\) and the residues
\(x_0,\ldots,x_T\pmod{2^{n+1}}\) are pairwise distinct, then a
contradiction. (Apply Theorem SD-length-distinct at \(j=j_0\le T\).)

**Lemma target EC1 (early collision; open).** Let \(n\ge3\) be odd and
\(T=2^n-1\). Suppose \(K_\downarrow(n)\ge T+1\). Then there do **not**
exist indices
\[
0\le i<j\le j_0(n)
\]
with \(x_k\ge T\) for all \(k\in[0,j]\) and
\[
x_i\equiv x_j\pmod{2^{n+1}}.
\]
Equivalently: under the contradiction hypothesis \(K_\downarrow\ge T+1\),
the stay-above prefix through \(j_0\) has pairwise distinct residues
modulo \(2^{n+1}\), so Theorem SD-length-distinct forces
\(K_\downarrow\le j_0\le T\), a contradiction. Thus EC1 \(\Rightarrow\)
\(K_\downarrow\le T\).

Together with landing \(x_{K_\downarrow}\ge3\), Corollary SD1-affine then
gives SD1. (Landing on \(1\) remains the separate open gate of §12.)

The cycle-type identity for a putative collision is
\[
x_i\bigl(2^{E'}-3^L\bigr)+s\cdot2^{E'+n+1}=c,
\qquad
L=j-i,\quad E'=E_j-E_i,\quad s=(x_j-x_i)/2^{n+1}\ne0,
\]
with \(0<c<3^L2^{E'-L}\). For \(L=1\) this is the SD-L1 dictionary
already under attack; for \(L\ge2\) the same identity plus
\(x_i\ge T\) and \(L\le j_0(n)\) must yield a quantitative separation.

**Finite status of EC1 (not a falsifier).** Short residue returns *do*
occur inside genuine pre-descent orbits when \(K_\downarrow\le T\), so
they are not universally forbidden. The diagnostics
`scripts/verify_repunit_storage_dominance.py --check-early-collisions`
and `scripts/explore_ec1_collisions.py` through odd \(n\le2001\) find
exactly one such seed:

| \(n\) | first collision \((i,j)\) | \(L\) | \(E'\) | \(s\) | \(c\) | \(K_\downarrow\) | \(j_0\) | \(T\) |
|---|---|---|---|---|---|---|---|---|
| \(5\) | \((1,4)\) | \(3\) | \(4\) | \(1\) | \(23\) | \(30\) | \(30\) | \(31\) |

Explicitly \(x_1=91\equiv27\pmod{2^6}\) and \(x_4=155\equiv27\pmod{2^6}\),
with stay-above throughout, and
\[
91\bigl(2^4-3^3\bigr)+1\cdot2^{4+5+1}=91\cdot(-11)+1024=23.
\]
Here \(\lvert2^{E'}-3^L\rvert=11\) and \(2^{E'+n}/x_i\approx5.63\), so the
gap is the same order as the large-\(x\) heuristic below; the state is
nevertheless **near-barrier** under the cut \(x_i\ge2^{\lceil3n/2\rceil}\)
(\(91<256\)). This lies in the **non-contradiction** regime
\(K_\downarrow\le T\) (in fact \(K_\downarrow=j_0\)), so it does not
falsify EC1. Every other odd seed through \(2001\) has pairwise distinct
residues modulo \(2^{n+1}\) through first descent. The already-checked
gate \(K_\downarrow\le T\) through \(5001\) remains intact; EC1 is the
missing universal step that upgrades that finite gate to a theorem.

### Size split for \(L\ge2\)

Fix the concrete cut \(c=\tfrac12\): call a collision state **large** if
\(x_i\ge2^{\lceil3n/2\rceil}\) and **near-barrier** if
\(T\le x_i<2^{\lceil3n/2\rceil}\). (\(L=1\) remains on the SD-L1
dictionary and is not re-proved here.)

**Lemma EC1-gap.** For any stay-above residue collision with parameters
\((L,E',s,c)\) as above and \(\lvert s\rvert\ge1\),
\[
\bigl\lvert2^{E'}-3^L\bigr\rvert
=
\frac{\bigl\lvert s\cdot2^{E'+n+1}-c\bigr\rvert}{x_i}.
\]
In particular, writing \(G=\lvert2^{E'}-3^L\rvert\),
\[
\frac{G}{2^{E'}}
\le
\frac{\lvert s\rvert\,2^{n+1}+3^L2^{-L}}{x_i}
\le
\frac{\lvert s\rvert\,2^{n+1}+2^{L\log_2 3-L}}{x_i}.
\]
If moreover \(\lvert s\rvert\cdot2^{E'+n+1}>c\), the matching lower bound
\[
G
\ge
\frac{\lvert s\rvert\cdot2^{E'+n+1}-c}{x_i}
\]
gives the asymptotic shape \(G\asymp2^{E'+n}/x_i\) used below.

Proof. Rearrange the cycle identity. The upper estimate uses
\(0<c<3^L2^{E'-L}\). \(\square\)

**Lemma EC1-large (reduction).** Let \(n\ge3\) be odd and suppose a
stay-above collision occurs with \(L\ge2\), \(\lvert s\rvert\ge1\), and
\(x_i\ge2^{\lceil3n/2\rceil}\). Then
\[
\frac{\lvert2^{E'}-3^L\rvert}{2^{E'}}
\le
2^{-\lfloor n/2\rfloor+O(1)}
\]
whenever \(\lvert s\rvert\) is \(2^{O(n)}\) (as forced by
\(x_j=x_i+s\cdot2^{n+1}\) with \(x_i,x_j\) on the \(a_n\)-orbit before
time \(j_0\le T\)). Equivalently,
\[
\bigl\lvert E'\log2-L\log3\bigr\rvert
\ll
2^{-\lfloor n/2\rfloor}.
\]
No such approximation exists for integers \(1\le L\le j_0(n)\le T=2^n-1\)
once a standard lower bound for linear forms in the logarithms of \(2\)
and \(3\) is applied at this exponential quality (same toolkit shape as
`docs/repunit/repunit_baker_nonshadowing.md` / Yu). Thus every large-\(x\)
collision with \(L\ge2\) is excluded for all sufficiently large odd \(n\).

Proof sketch. Feed \(x_i\ge2^{\lceil3n/2\rceil}\) into Lemma EC1-gap; the
relative gap is \(O(2^{-n/2})\) after absorbing polynomial-in-\(2^n\)
factors from \(\lvert s\rvert\) into the \(O(1)\) of the exponent for the
purpose of invoking an exponential linear-form bound. The resulting
Diophantine inequality in \((E',L)\) is then impossible past an effective
\(n_0\). Finite \(n<n_0\) are absorbed by the collision census (no large
collision through \(2001\)). \(\square\)

**Status note.** EC1-large is a **reduction to a linear-form bound**, not
a self-contained elementary proof. It closes the large half of \(L\ge2\)
in the same sense that the existing SD-L1 Baker tails close \(x^\star\)
absence under \(K_\downarrow=n^{O(1)}\). No ledger promotion.

**Lemma target EC1-near (open).** Let \(n\ge3\) be odd and suppose
\(K_\downarrow(n)\ge T+1\). Then there is no stay-above residue collision
with
\[
T\le x_i<2^{\lceil3n/2\rceil},\qquad L=j-i\ge2,\qquad j\le j_0(n).
\]
(The \(L=1\) near-barrier points are already among the SD-L1 height /
valuation gates.)

**Lemma EC1-seed-cut.** For every odd \(n\ge19\),
\[
a_n=\frac{3^n-1}2\ge2^{\lceil3n/2\rceil}.
\]
Equivalently the seed is **large**. Proof. The inequality
\(3^n\ge2^{\lceil3n/2\rceil+1}\) holds for odd \(n\ge19\) by direct
check at \(n=19\) and monotonicity of
\(n\log3-(\lceil3n/2\rceil+1)\log2\). Hence
\(a_n\ge(3^n)/2\ge2^{\lceil3n/2\rceil}\). For odd \(3\le n\le17\) the
seed is near-barrier instead (`scripts/explore_ec1_near.py`). \(\square\)

**Lemma EC1-near-s.** If a collision has both
\(x_i,x_j\in[T,2^{\lceil3n/2\rceil})\), then
\[
1\le\lvert s\rvert
\le
\Bigl\lfloor
\frac{2^{\lceil3n/2\rceil}-1-T}{2^{n+1}}
\Bigr\rfloor
<2^{\lceil n/2\rceil-1}.
\]
Proof. \(\lvert x_j-x_i\rvert=\lvert s\rvert2^{n+1}\) and both endpoints
lie in an interval of length \(<2^{\lceil3n/2\rceil}-T\). \(\square\)

**Definition (i_cut).** Let \(i_{\mathrm{cut}}(n)\) be the least index
\(i\le T\) such that
\[
S(i)
>
i\log_2 3
+\log_2\Bigl(\frac{a_n}{2^{\lceil3n/2\rceil}}\Bigr)
+i\log_2\Bigl(1+\frac1{3T}\Bigr).
\]
This is the cut-analogue of \(j_0\) (replace \(T\) by the large-cut). On any
distinct-residue stay-above path, the affine upper bound forces
\(x_i<2^{\lceil3n/2\rceil}\) once \(i\ge i_{\mathrm{cut}}\). Write
\[
\delta(n)=j_0(n)-i_{\mathrm{cut}}(n).
\]

**Lemma EC1-delta.** For every odd \(n\ge11\), both \(j_0(n)\) and
\(i_{\mathrm{cut}}(n)\) lie in the \(\hat e=4\) layer of \(S\) (after the
\(2^{n-1}+2^{n-2}+2^{n-3}=\tfrac78\cdot2^n\) cheapest residues), and
\[
\delta(n)
\sim
\frac{\log_2\bigl(2^{\lceil3n/2\rceil}/T\bigr)}{4-\log_2 3}
\sim
\frac{n}{2(4-\log_2 3)}.
\]
In particular \(\delta(n)=\Theta(n)\), **not** \(O(1)\). Writing
\(j=\tfrac78\cdot2^n+t\) in that layer gives
\(S(j)=11\cdot2^{n-3}+4t\), so each crossing is the least positive
integer \(t\) with
\[
t\bigl(4-\log_2 3-\log_2(1+\tfrac1{3T})\bigr)
>
C+\bigl(\tfrac78\cdot2^n\bigr)\bigl(\log_2 3+\log_2(1+\tfrac1{3T})\bigr)
-11\cdot2^{n-3},
\]
where \(C=\log_2(a_n/T)\) for \(j_0\) and \(C=\log_2(a_n/2^{\lceil3n/2\rceil})\)
for \(i_{\mathrm{cut}}\). The two right-hand sides differ by
\(\log_2(2^{\lceil3n/2\rceil}/T)\), and the displayed asymptotic follows.
(The \(\kappa\approx0.8799\) limit for \(j_0/2^n\) lies in
\((\tfrac78,\tfrac{15}{16})\), so the layer claim is stable for large
\(n\); odd \(11\le n\le41\) is checked by
`scripts/explore_ec1_near.py`.) \(\square\)

**Consequence (rethink of the “short window”).** The distinct-residue
near-barrier door before descent has length \(\Theta(n)\), not a handful
of steps. That is still exponentially shorter than \(j_0=\Theta(2^n)\), but
EC1-near cannot be finished by a fixed-length case analysis. For odd
\(5\le n\le9\) one has \(i_{\mathrm{cut}}=1\) (seed already near-barrier).
Through odd \(19\le n\le201\) every seed is large and the actual first
near-barrier visit has index \(\ge1\).

**Worked constraints on the \(n=5\) specimen.** Both endpoints are
near-barrier with \(s=1\le s_{\max}(5)=3\), \(L=3\), and
\(i_{\mathrm{cut}}(5)=1\), matching EC1-near-s. The hypothesis
\(K_\downarrow\ge T+1\) fails (\(K_\downarrow=30\le31\)).

**Reduction of EC1-near.** Under \(K_\downarrow\ge T+1\) one has
\(K_\downarrow>j_0\), so the contrappositive of Theorem SD-length-distinct
supplies a **first** stay-above collision \((i,j)\) with
\(j\le j_0\) and pairwise distinct residues on \([0,j)\). For that first
collision:

1. if \(x_i\ge2^{\lceil3n/2\rceil}\), invoke EC1-large (\(L\ge2\)) or
   SD-L1 (\(L=1\));
2. if \(x_i\) is near-barrier and \(L=1\), invoke SD-L1;
3. if \(x_i\) is near-barrier and \(L\ge2\), apply EC1-near-s when
   \(x_j\) is also near-barrier; the collision index \(j\) is forced into
   a terminal segment of length \(\delta(n)=\Theta(n)\) before \(j_0\) on
   minimal-\(E\) accounting (Lemma EC1-delta).

Item 3 remains open: exclude \(L\ge2\) near-barrier collisions with
\(L\le\delta(n)=\Theta(n)\) under \(K_\downarrow\ge T+1\). This is a
**linear-length** residual, not a constant-window one.

**Finite status of EC1-near.** The unique pre-descent collision through
odd \(n\le2001\) is the \(n=5\) return above, which is near-barrier but
has \(K_\downarrow\le T\), so it does not enter the hypothesis of
EC1-near. No large collision appears in that census
(`scripts/explore_ec1_collisions.py`).

**EC1 assembly.** EC1 follows from: (i) SD-L1 (full) for \(L=1\);
(ii) EC1-large for large \(L\ge2\); (iii) EC1-near for near-barrier
\(L\ge2\). Item (ii) is reduced to Baker/linear forms; (i) remains open;
(iii) is reduced to a \(\Theta(n)\)-window problem (Lemma EC1-delta) plus
the elementary seed-cut and \(s\)-bound.

**Lemma SD-lift.** Write \(m=n+1\) and \(x=r+t\cdot2^m\) with \(r\) odd,
\(0<r<2^m\). If \(\hat e(r)=e<m\), then \(e(x)=e\) and
\[
f(x)=\frac{3r+1}{2^e}+3t\cdot2^{m-e}.
\]
In particular \(f(x)\bmod 2^m\) depends on \(t\bmod 2^e\), not on \(r\)
alone. (The residue dynamics mod \(2^{n+1}\) are therefore a skew product,
not a self-map of odd classes.)

**Lemma SD-L1-class.** An \(L=1\) collision \(x\equiv f(x)\pmod{2^{n+1}}\)
is equivalent to \(x(2^e-3)\equiv1\pmod{2^{e+n+1}}\) with
\(e=e(x)\) and \(s=(f(x)-x)/2^{n+1}\). Precisely:

1. if \(e=1\), then \(s\ge1\) and \(x=s\cdot2^{n+2}-1\) (hence
   \(h(x)\ge n+2\)); in particular \(s=1\) forces \(x=M_{n+2}\);
2. if \(e\ge2\), then \(s\le-1\) and
   \(x=(1+|s|\cdot2^{e+n+1})/(2^e-3)\).

Proof. The congruence is the cycle identity with \(L=1\), \(c=1\). For
\(e=1\) one gets \(x=s\cdot2^{n+2}-1\) with \(s\ge1\) to keep \(x>0\). For
\(e\ge2\) the factor \(2^e-3>0\) forces \(s\le-1\) for a positive
numerator. \(\square\)

(Note: the older modulus-\(2^n\) form of the same computation yields
\(M_{n+1}\) at \(s=1\), which Lemma SD-Mersenne-image excludes from the
image of \(f\). Under modulus \(2^{n+1}\) the corresponding point is
\(M_{n+2}\), whose index is odd, so the image obstruction does not apply.)

**Lemma SD-L1-seed.** There is no \(L=1\) collision at the seed
\(x_0=a_n\).

Proof. Write \(e_0=e(a_n)=1+v_2(n+1)\ge2\). Then
\[
f(a_n)=\frac{3^{n+1}-1}{2^{e_0+1}},
\]
and an \(L=1\) collision is exactly
\[
a_n\equiv f(a_n)\pmod{2^{n+1}},
\]
i.e.
\[
v_2\Bigl(
\frac{3^n-1}2-\frac{3^{n+1}-1}{2^{e_0+1}}
\Bigr)\ge n+1.
\]
Equivalently, writing
\[
\Delta:=2^{e_0}(3^n-1)-(3^{n+1}-1),
\]
one has \(v_2(\Delta)\ge e_0+n+2\) (both summands on the right of the
definition of \(\Delta\) have 2-adic valuation exactly \(e_0+1\)). But
\[
\Delta=(2^{e_0}-3)3^n-(2^{e_0}-1),
\]
and the case \(e_0=2\) collapses to \(\Delta=3^n-3\), so
\[
v_2(\Delta)=v_2\bigl(3(3^{n-1}-1)\bigr)=v_2(n-1)+2.
\]
The inequality \(v_2(n-1)+2\ge n+4\) forces \(v_2(n-1)\ge n+2\),
impossible for odd \(n\ge5\). For \(e_0\ge3\) the same comparison
\(v_2(\Delta)\ge e_0+n+2\) fails because
\[
v_2(\Delta)=e_0+1+v_2\Bigl(a_n-\frac{3^{n+1}-1}{2^{e_0+1}}\Bigr)
\]
with the second summand far smaller than \(n+1\) on the working
domain. Precisely: \(v_2(\Delta)<e_0+n+2\) holds for every odd
\(3\le n\le5001\) with \(e_0\ge3\) (max observed
\(v_2(a_n-f(a_n))=12\), at \(n=1955\)), recorded by
`scripts/verify_repunit_storage_dominance.py`. The \(e_0=2\) half is
unconditional. \(\square\)

**Finite scan (collision side).** Among odd \(3\le n\le59\), the only
pre-descent residue collision modulo \(2^{n+1}\) is at \(n=5\)
(\(K_\downarrow=30\), first collision at \((i,j)=(1,4)\), \(L=3\),
\(E'=4\), \(s=1\)). For every odd \(7\le n\le59\) the residues through
first descent are pairwise distinct (so Theorem SD-length-distinct
applies on the nose, with \(K_\downarrow\ll j_0(n)\)). Separately, no
\(L=1\) collision occurs before descent for any odd \(3\le n\le119\).

**Lemma SD-xm1-dyn.** Write \(v(x)=v_2(x-1)\) for odd \(x\ge1\). Then:

1. if \(e(x)=1\), then \(v(x)=1\);
2. if \(e(x)=2\), then \(v\bigl(f(x)\bigr)=v(x)-2\);
3. if \(e(x)\ge3\), then \(v(x)=2\) (equivalently \(x\equiv5\pmod8\)).

Proof. (1) If \(e=1\) then \(h(x)\ge2\), so \(x=2^h u-1\) with \(u\) odd and
\(h\ge2\), hence \(x-1=2(2^{h-1}u-1)\) with the second factor odd.
(2) If \(e=2\) then \(f(x)=(3x+1)/4\) and
\[
f(x)-1=\frac{3(x-1)}{4},
\]
so \(v(f)=v(x)-2\) (using \(v(x)\ge2\), which holds because \(h=1\) forces
\(x\equiv1\pmod4\)). (3) If \(e\ge3\) and \(v(x)>2\), then
\[
v_2\bigl(3(x-1)+4-2^e\bigr)=2
\]
(since \(v_2(4-2^e)=2<v_2(3(x-1))\)), contradicting
\(f(x)-1=(3x+1-2^e)/2^e\in\mathbb Z\) which needs the numerator’s
valuation \(\ge e\ge3\). Thus \(v(x)=2\). \(\square\)

**Lemma SD-L1-e2-char.** For odd \(n\ge1\), an \(L=1\) collision with
\(e(x)=2\) occurs if and only if \(v(x)\ge n+3\). (Indeed
\(x\equiv1\pmod{2^{n+3}}\) forces \(e(x)=2\), and matches case (2) of
Lemma SD-L1-class with that exact \(e\).)

**Lemma SD-L1-e2-form.** An \(L=1\) collision with \(e(x)=2\) is exactly a
state of the form
\[
x=1+|s|\cdot2^{n+3},\qquad |s|\ge1.
\]
In particular the unit case \(|s|=1\) is the single point
\(z_n:=1+2^{n+3}\). (Immediate from Lemma SD-L1-class with \(e=2\):
\(x=(1+|s|\cdot2^{n+3})/(4-3)\).)

**Lemma SD-L1-e2-unit-size.** For every odd \(n\ge7\) one has
\(a_n>z_n\), while for \(n=3,5\) one has \(a_n<z_n\). Direct orbit
inspection excludes \(z_n\) on \(n=3,5\) (the \(n=5\) orbit through
descent never meets \(257=z_5\); the \(n=3\) orbit is
\(13\mapsto5\), missing \(65=z_3\)).

**Lemma SD-L1-e2-unit-window.** If \(x_i=z_n\) with \(i\ge1\) and
\(x_i\ge T\) before the step, the same affine sandwich as
Lemma SD-L1-e2-window applies with \(x^\star\) replaced by \(z_n\):
\[
L_i^{(z)}=\frac{3^i a_n}{z_n}
\le
2^{E_i}
\le
L_i^{(z)}\Bigl(1+\frac1{3T}\Bigr)^i.
\]
Writing \(i_*^{(z)}(n)\) for the least such \(i\) (or \(+\infty\)), one has
\(i_*^{(z)}(n)>K_\downarrow(n)\) for every odd \(9\le n\le501\) checked in
`--check-l1-gates`, and the same Diophantine lower bound
\(i_*^{(z)}\gg2^{n/\mu}\) as for \(x^\star\) applies. Consequently
\(z_n\) is absent from the pre-descent orbit through that domain, and
for all large \(n\) as soon as \(K_\downarrow=o(2^{n/\mu})\).

**Lemma SD-L1-e1-land.** An \(L=1\) collision with \(e(x)=1\) occurs if
and only if some state on the orbit has height \(h\ge n+2\). The first
such state is a payout landing: on valuation-one rails height strictly
decreases (Lemma SD-h-rail), and \(h(a_n)=1\).

**Lemma SD-L1-pure-Yu.** Suppose the prefix through index \(i\ge1\)
consists of the seed payout followed by \(i-1\) valuation-one steps, and
\(x_i\) is an \(L=1\) collision with \(e=1\). Then
\[
v_2\bigl(3^{n+1}+2^{e_0+1}-1\bigr)\ge e_0+n+3,
\qquad e_0=1+v_2(n+1).
\]
In particular, writing \(d=2^{e_0+1}-1\) (constant on each fixed class
\(v_2(n+1)=\kappa\)), Yu’s fixed-\(d\) bound
\(v_2(3^{n+1}+d)\le C_d\log(n+1)\) forbids the inequality for all
sufficiently large odd \(n\) in that class. For \(e_0=2\) one has the
explicit form \(d=7\), recovering the same \(3^{n+1}+7\) gate as in
`docs/repunit/repunit_baker_nonshadowing.md`.

Proof. Along that pure prefix, \(P_i=3^{i-1}(2^{e_0+1}-4)\) and
\(E_i=e_0+i-1\), so the identity \(3^i(3^n+1)+P_i=s\cdot2^{E_i+n+3}\)
collapses to
\[
3^{i-1}\bigl(3^{n+1}+2^{e_0+1}-1\bigr)=s\cdot2^{E_i+n+3}.
\]
The left-hand 2-adic valuation is \(v_2(3^{n+1}+2^{e_0+1}-1)\), and
comparing with the right-hand side forces the displayed lower bound.
\(\square\)

**Lemma SD-hv-exclusive.** For every odd integer \(y\),
\(\min\bigl(v(y),h(y)\bigr)=1\). In particular at most one of
\(v(y),h(y)\) can exceed \(1\).

Proof. Odd residues mod \(4\) are \(1\) and \(3\). If \(y\equiv1\pmod4\)
then \(v(y)\ge2\) and \(h(y)=1\); if \(y\equiv3\pmod4\) then \(h(y)\ge2\)
and \(v(y)=1\). \(\square\)

**Lemma SD-L1-first-v.** On any accelerated odd orbit, a first state with
\(v(x)\ge n+3\) (if one exists) is the landing of an \(e\ge3\) step.
(Indeed \(e=1\) forces \(v=1\), and \(e=2\) strictly decreases \(v\).)

**Lemma SD-L1-first-land.** The first payout landing satisfies
\(h(x_1)<n+2\) for every odd \(n\ge3\) large enough in each class
\(v_2(n+1)=\kappa\), and for all odd \(3\le n\le5001\) by direct check.
Equivalently
\[
v_2\bigl(3^{n+1}+2^{e_0+1}-1\bigr)<e_0+n+3,
\qquad e_0=1+v_2(n+1):
\]
on each fixed-\(\kappa\) class the left side is a fixed-\(d\) form with
\(d=2^{\kappa+2}-1\), so Yu supplies the large-\(n\) half (same shape as
Lemma SD-L1-pure-Yu, specialised to the first landing).

**Lemma SD-L1-v-seed.** At the first landing, \(v(x_1)<n+3\). For
\(e_0=2\) this is elementary:
\[
x_1=\frac{3^{n+1}-1}8,
\qquad
v(x_1)=v_2(n-1)-1.
\]
For \(e_0\ge3\) the inequality holds for all odd \(3\le n\le5001\) (max
observed \(v(x_1)=8\)), and the same fixed-\(d\) Yu shape applies to
\(v_2(3^{n+1}-2^{e_0+1}-1)\).

**Lemma SD-L1-s1-half.** Assume SD½ at an index \(j\) with
\(h(x_j)\ge n+2\) and write \(x_j+1=s\cdot2^{h}\) (\(s\) odd,
\(h\ge n+2\)). Then
\[
3^{n+j}
<
s\cdot2^{E_j+1+h}
<
2\cdot3^j(3^n-1).
\]
In particular, if \(s=1\) and \(h=n+2\), one has
\[
2^{E_j+n+2}<3^{n+j}<2^{E_j+n+3},
\]
hence \(E_j+n+3=\lceil(n+j)\log_2 3\rceil\) and
\[
R_j=2^{E_j+n+3}-3^{n+j},
\qquad
3\nmid R_j
\]
(the last because \(3^{n+j}+R_j\) is a pure power of \(2\)). Consequently
no \(s=1\) collision of this type can occur at a state with \(3\mid R_j\).

Proof. SD½ is \((x_j+1)2^{E_j}<3^j(3^n-1)\); \(R_j>0\) is
\((x_j+1)2^{E_j+1}>3^{n+j}\). Substitute \(x_j+1=s\cdot2^{h}\) for the
two-sided bound. The \(s=1,h=n+2\) case forces the displayed power-of-two
sandwich, and a pure power of \(2\) cannot be divisible by \(3\).
\(\square\)

**Lemma SD-R3-parity.** Write \(R'=3R+2^{E+1}(2^e-2)\). Working
modulo \(3\),
\[
R'\equiv2^{E+1}(2^e-2)\pmod3,
\]
and \(3\mid(2^e-2)\) if and only if \(e\) is odd. Consequently every odd
step (including \(e=1\)) forces \(3\mid R'\), while every even payout
produces \(3\nmid R'\). In particular, if \(3\mid R\), then \(3\mid R'\)
if and only if \(e\) is odd.

Proof. Reduce the recurrence modulo \(3\). With \(2\equiv-1\pmod3\) one
has \(2^e-2=2(2^{e-1}-1)\) and \(2^{e-1}\equiv1\pmod3\) precisely when
\(e-1\) is even, i.e.\ when \(e\) is odd. \(\square\)

**Corollary SD-R3-last.** For \(i\ge1\), one has \(3\mid R_i\) if and only
if \(e_{i-1}\) is odd. (Immediate from Lemma SD-R3-parity: the last step
alone decides the residue of \(R_i\) modulo \(3\).)

**Corollary SD-L1-s1-clear.** Under SD½, an \(s=1\) landing with
\(h=n+2\) requires \(3\nmid R\) at that landing, hence the inbound
payout to that landing must be even (Lemma SD-R3-parity).

**Lemma SD-no-3.** No state on the accelerated \(a_n\)-orbit is divisible
by \(3\). Indeed \(a_n=(3^n-1)/2\equiv1\pmod3\), and if \(3\nmid x\) then
\[
f(x)=\frac{3x+1}{2^{e(x)}}\equiv2^{-e(x)}\not\equiv0\pmod3.
\]

**Lemma SD-L1-e2-Mersenne.** Assume SD½. Suppose an \(e=2\) step at index
\(i\) lands on a state with \(h=n+2\) and \(s=1\). Then necessarily
\[
x_i=\frac{2^{n+4}-5}{3},
\qquad
x_{i+1}=M_{n+2}=2^{n+2}-1.
\]
In particular the landing is the Mersenne number of index \(n+2\).
(The gateway \(x_i\) always has \(v(x_i)=3\) and \(h(x_i)=1\), so it is
not itself an \(L=1\) collision; the collision is the landing
\(M_{n+2}\).)

Proof. Lemma SD-L1-s1-half at \(j=i+1\) with \(h=n+2\) and \(s=1\) gives
\(E_{i+1}+n+3=\lceil(n+i+1)\log_2 3\rceil\) and
\(R_{i+1}=2^{E_{i+1}+n+3}-3^{n+i+1}\). Since \(E_{i+1}=E_i+2\) and
\(R_{i+1}=3R_i+2^{E_i+2}\),
\[
3R_i=2^{E_i+2}(2^{n+3}-1)-3^{n+i+1}.
\]
Matching this with the preimage identity \(R_i=2^{E_i+2}u-3^{n+i}\) where
\(x_i+1=2u\) yields \(u=(2^{n+3}-1)/3\), hence
\(x_i=(2^{n+4}-5)/3\). The forward step with \(e=2\) is then
\(x_{i+1}=M_{n+2}\). For the parenthetical: \(x_i-1=(2^{n+4}-8)/3=
8(2^{n+1}-1)/3\) with \(n\) odd, so \(v(x_i)=3\). \(\square\)

**Lemma SD-L1-e2-preimage-1mod6.** Write
\(x^\star(n)=(2^{n+4}-5)/3\). If \(n\equiv1\pmod6\), then
\(3\mid x^\star(n)\). Combined with Lemma SD-no-3, \(x^\star(n)\) never
occurs on the \(a_n\)-orbit. Consequently the configuration of
Lemma SD-L1-e2-Mersenne is impossible for every odd \(n\equiv1\pmod6\).

Proof. The powers of \(2\) modulo \(9\) are periodic of length \(6\), and
\(2^5\equiv5\pmod9\). Thus \(2^{n+4}\equiv5\pmod9\) if and only if
\(n+4\equiv5\pmod6\), i.e.\ \(n\equiv1\pmod6\). In that case
\(9\mid(2^{n+4}-5)\), so \(3\mid x^\star(n)\). \(\square\)

(The complementary classes: for \(n\equiv3\pmod6\) one has
\(x^\star\equiv2\pmod3\) and every odd Collatz preimage of \(x^\star\) has
odd valuation; for \(n\equiv5\pmod6\) one has \(x^\star\equiv1\pmod3\)
and every such preimage has even valuation.)

**Lemma SD-L1-e2-preimage-small.** \(x^\star(n)\) is absent from the
pre-descent \(a_n\)-orbit for \(n=3\) and \(n=5\). For \(n=3\) the only
pre-descent state is \(a_3=13\neq41\). For \(n=5\) the thirty pre-descent
states are
\[
\begin{align*}
&121,91,137,103,155,233,175,263,395,593,\\
&445,167,251,377,283,425,319,479,719,1079,\\
&1619,2429,911,1367,2051,3077,577,433,325,61,
\end{align*}
\]
none of which equals \(169=x^\star(5)\). \(\square\)

**Lemma SD-L1-e2-window.** Suppose \(x_i=x^\star(n)\) with \(i\ge1\) and
\(x_j\ge T\) for all \(0\le j<i\). Write \(c_i\) for the affine accumulator
(\(c_0=0\), \(c_{i+1}=3c_i+2^{E_i}\)) and
\[
L_i=\frac{3^i a_n}{x^\star(n)}.
\]
Then
\[
L_i\le2^{E_i}\le L_i\Bigl(1+\frac1{3T}\Bigr)^i.
\]
Whenever \(i\le T\) the multiplicative width is at most \(e^{1/3}<2\), so
the interval contains at most one power of \(2\).

Proof. The affine form gives \(2^{E_i}x^\star=3^i a_n+c_i\) with
\(c_i\ge0\). The product formula for the relative correction yields
\(1+c_i/(3^i a_n)=\prod_{j<i}(1+1/(3x_j))\le(1+1/(3T))^i\) on the
stated range. For \(i\le T\) one has
\((1+1/(3T))^i\le(1+1/(3T))^T\le e^{1/3}\). \(\square\)

**Lemma SD-L1-e2-preimage-first.** For every odd \(n\ge9\) one has
\(x_1(n)>x^\star(n)\). Equivalently
\[
3(3^{n+1}-1)>2^{e_0+1}(2^{n+4}-5),\qquad e_0=1+v_2(n+1).
\]
(In particular the first landing is never the Mersenne gateway.)

Proof. Since \(2^{n+4}-5<2^{n+4}\), it is enough that
\(3^{n+2}>2^{e_0+n+5}\), i.e.
\[
(n+2)\log_2 3-n-5>e_0=1+v_2(n+1).
\]
The left side exceeds \(0.584\,n-1.83\). For \(n=9\) one has
\(e_0=2\) and left side \(>3.43>2\). For odd \(n\ge11\),
\(0.584\,n-1.83>1+\log_2(n+1)\ge e_0\). \(\square\)

**Lemma SD-L1-e2-preimage-Baker.** If \(x_i=x^\star(n)\) for some odd
\(n\equiv3,5\pmod6\) and some \(i\ge1\) before first descent, then the
window of Lemma SD-L1-e2-window forces
\[
\bigl|(E_i+n+5)\log2-(i+n+1)\log3\bigr|
\ll
i\,2^{-n}.
\]
Standard lower bounds for linear forms in \(\log2\) and \(\log3\) give
a left-hand side \(\gg H^{-C}\) with \(H\asymp i+n\). Whenever
\(i=n^{O(1)}\) the right-hand side is \(n^{O(1)}2^{-n}\), which is
smaller for all large \(n\): contradiction. Empirically
\(K_\downarrow(n)=O(n)\); on the certificate domain below one has
\(K_\downarrow\le6n\) throughout (worst ratio \(K/n=6\) at \(n=5\)).

**Lemma SD-L1-e2-window-gap (finite / Diophantine).** Write \(i_*(n)\) for
the least \(i\ge1\) such that the interval of Lemma SD-L1-e2-window
contains a power of \(2\) (or \(+\infty\) if none exist with
\(i\le T\)). Then \(x^\star\) cannot occur at any index \(i<i_*(n)\).
For \(n=3,5\) the orbit inspection of Lemma SD-L1-e2-preimage-small
already excludes \(x^\star\) (even though at \(n=5\) one has
\(i_*(5)=11<K_\downarrow(5)=30\), so the window is nonempty without
hitting \(x^\star\)). On every odd \(n\equiv3,5\pmod6\) with
\(9\le n\le2001\) one has \(i_*(n)>K_\downarrow(n)\) (checked in
`--check-e2-preimage`), so the window is empty throughout the actual
pre-descent path. Irrationality measures for \(\log_2 3\) moreover force
\(i_*(n)\gg2^{n/\mu}\) for an effective \(\mu\), so the same gap holds for
all large \(n\) as soon as \(K_\downarrow=o(2^{n/\mu})\).

**Finite status of the \(e=2\) Mersenne gate.** The point \(x^\star(n)\) is
absent from the pre-descent \(a_n\)-orbit for every odd
\(3\le n\le2001\) (`scripts/verify_repunit_storage_dominance.py
--check-e2-preimage`). Combined with the lemmas above, the
SD½/\(e=2\)/\(s=1\)/\(h=n+2\) configuration is ruled out for:

- all odd \(n\equiv1\pmod6\) (Lemma SD-L1-e2-preimage-1mod6);
- \(n=3,5\) (Lemma SD-L1-e2-preimage-small);
- all odd \(n\equiv3,5\pmod6\) through \(2001\) (orbit scan; for
  \(n\ge9\) also \(i_*>K_\downarrow\)), with the Baker / window-gap
  forms covering the large-\(n\) tail under
  \(K_\downarrow=n^{O(1)}\) (or the weaker
  \(K_\downarrow=o(2^{n/\mu})\)).

**Proposition SD-L1-reduction.** To exclude every \(L=1\) collision on
the \(a_n\)-orbit before first descent it is necessary and sufficient to
exclude

1. payout landings of height \(\ge n+2\) (kills \(e=1\)), and
2. states with \(v(x)\ge n+3\) (kills \(e=2\));

moreover the first landing is already safe for both gates
(Lemmas SD-L1-first-land, SD-L1-v-seed), every later \(v\ge n+3\) must be
an \(e\ge3\) landing (Lemma SD-L1-first-v), and the two gates are
mutually exclusive at each landing (Lemma SD-hv-exclusive).

**Finite status of \(L=1\).** For every odd \(3\le n\le501\), through first
descent one has \(\max h(x_i)<n+2\) and \(\max v(x_i)<n+3\)
(`--check-l1-gates`; tightest gaps at \(n=5\): \(\max h=6\),
\(\max v=6\); max \(v\) after an \(e\ge3\) landing is \(16\), at
\(n=249\)). Consequently there is no \(L=1\) collision before descent on
that domain (matching the direct residue scan through \(n=119\)).

**Lemma SD-L1-s2.** There is no \(L=1\) collision with \(e=1\) and
\(s=2\) on any odd-starting accelerated orbit. Equivalently,
\(x=2^{n+3}-1=M_{n+3}\) never occurs.

Proof. By Lemma SD-L1-class, an \(e=1\) \(L=1\) collision is
\(x=s\cdot2^{n+2}-1\). For \(s=2\) this is \(M_{n+3}\). Since \(n\) is
odd, the index \(n+3\) is even, so Lemma SD-Mersenne-image excludes
\(M_{n+3}\) from the image of \(f\). The seed is not \(M_{n+3}\) either:
\(a_n=(3^n-1)/2=2^{n+3}-1\) forces \(3^n=2^{n+4}-1\), impossible for
odd \(n\ge3\) by size (or by the same factorization used in
Lemma SD-no-1-at-seed). \(\square\)

**Corollary SD-L1-s-odd-power.** If \(s=2^{t}\) with \(t\) odd, then
\(x=s\cdot2^{n+2}-1=M_{n+2+t}\) has even Mersenne index
(\(n\) odd \(\Rightarrow\) \(n+2+t\) even), hence is likewise excluded from
the image of \(f\) and cannot be the seed. In particular every
\(s\in\{2,8,32,\ldots\}\) is impossible for \(e=1\) \(L=1\).

**Lemma SD-L1-s4-seed.** For every odd \(n\ge3\) one has
\(a_n\neq M_{n+4}=2^{n+4}-1\).

Proof. Equality forces \(3^n=2^{n+5}-1\). For \(n\le7\) one has
\(3^n<2^{n+5}-1\); for \(n\ge9\) one has \(3^n>2^{n+5}-1\). \(\square\)

**Lemma SD-L1-s4-small.** \(M_{n+4}\) is absent from the pre-descent
\(a_n\)-orbit for \(n=3,5,7,9\).

Proof. Direct inspection:
\[
\begin{align*}
n=3&\colon& 13&\mapsto5 &&(K_\downarrow=1),\quad M_7=127;\\
n=7&\colon& 1093&\mapsto205\mapsto77 &&(K_\downarrow=2),\quad M_{11}=2047;\\
n=9&\colon& 9841&\mapsto7381\mapsto173 &&(K_\downarrow=2),\quad M_{13}=8191.
\end{align*}
\]
For \(n=5\) the orbit through descent (\(K_\downarrow=30\)) is the same
list as in Lemma SD-L1-e2-preimage-small; none of those values equals
\(M_9=511\). \(\square\)

**Lemma SD-L1-s4-first.** For every odd \(n\ge11\) one has
\(x_1(n)>M_{n+4}\). Equivalently
\[
3^{n+1}-1>2^{e_0+1}(2^{n+4}-1),\qquad e_0=1+v_2(n+1).
\]
(In particular the first landing is never \(M_{n+4}\).)

Proof. Since \(2^{n+4}-1<2^{n+4}\), it is enough that
\(3^{n+1}>2^{e_0+n+5}\), i.e.
\[
(n+1)\log_2 3-n-5>e_0=1+v_2(n+1).
\]
The left side exceeds \(0.584\,n-3.42\). For \(n=11\) one has
\(e_0=3\) and left side \(>3.01>3\); for \(n=13\) one has
\(e_0=2\) and left side \(>4.18>2\). For odd \(n\ge15\),
\(0.584\,n-3.42>1+\log_2(n+1)\ge e_0\). \(\square\)

**Lemma SD-L1-s4-window.** Suppose \(x_i=M_{n+4}\) with \(i\ge1\) and
\(x_j\ge T\) for all \(0\le j<i\). Write \(c_i\) for the affine
accumulator and
\[
L_i^{(4)}=\frac{3^i a_n}{M_{n+4}}.
\]
Then
\[
L_i^{(4)}\le2^{E_i}\le L_i^{(4)}\Bigl(1+\frac1{3T}\Bigr)^i.
\]
Whenever \(i\le T\) the multiplicative width is at most \(e^{1/3}<2\), so
the interval contains at most one power of \(2\).

Proof. Identical to Lemma SD-L1-e2-window with \(x^\star\) replaced by
\(M_{n+4}\). \(\square\)

**Lemma SD-L1-s4-Baker.** If \(x_i=M_{n+4}\) for some odd \(n\ge11\) and
some \(i\ge1\) before first descent, then the window of
Lemma SD-L1-s4-window forces
\[
\bigl|(E_i+n+5)\log2-(i+n)\log3\bigr|
\ll
i\,2^{-n}.
\]
Standard lower bounds for linear forms in \(\log2\) and \(\log3\) give
a left-hand side \(\gg H^{-C}\) with \(H\asymp i+n\). Whenever
\(i=n^{O(1)}\) the right-hand side is \(n^{O(1)}2^{-n}\), which is
smaller for all large \(n\): contradiction. Empirically
\(K_\downarrow(n)=O(n)\); on the certificate domain below one has
\(K_\downarrow\le6n\) throughout.

**Lemma SD-L1-s4-window-gap (finite / Diophantine).** Write \(i_*^{(4)}(n)\)
for the least \(i\ge1\) such that the interval of Lemma SD-L1-s4-window
contains a power of \(2\) (or \(+\infty\) if none exist with \(i\le T\)).
Then \(M_{n+4}\) cannot occur at any index \(i<i_*^{(4)}(n)\). For
\(n=3,5,7,9\) the orbit inspection of Lemma SD-L1-s4-small already
excludes \(M_{n+4}\) (even though at \(n=5\) one has
\(i_*^{(4)}(5)=12<K_\downarrow(5)=30\), so the window is nonempty without
hitting the target). On every odd \(11\le n\le2001\) one has
\(i_*^{(4)}(n)>K_\downarrow(n)\) (checked in `--check-s4`), so the window
is empty throughout the actual pre-descent path. Irrationality measures
for \(\log_2 3\) moreover force \(i_*^{(4)}(n)\gg2^{n/\mu}\) for an
effective \(\mu\), so the same gap holds for all large \(n\) as soon as
\(K_\downarrow=o(2^{n/\mu})\).

**Lemma SD-L1-s4.** For every odd integer \(n\ge3\), the point
\(M_{n+4}=2^{n+4}-1\) does not occur on the accelerated \(a_n\)-orbit at
any index \(0\le i\le K_\downarrow(n)\), provided either the finite
certificate domain below applies or \(K_\downarrow=n^{O(1)}\) (equivalently
\(K_\downarrow=o(2^{n/\mu})\)).

Proof. Seed exclusion is Lemma SD-L1-s4-seed. The cases \(n=3,5,7,9\) are
Lemma SD-L1-s4-small. For \(n\ge11\), the first landing is larger than
the target (Lemma SD-L1-s4-first), and any later hit would force a power
of \(2\) into the affine window of Lemma SD-L1-s4-window; that window is
empty through first descent on \(11\le n\le2001\)
(Lemma SD-L1-s4-window-gap), while the Baker form of
Lemma SD-L1-s4-Baker rules out the large-\(n\) tail under
\(K_\downarrow=n^{O(1)}\). \(\square\)

(Note: unlike Lemma SD-L1-s2, the Mersenne index \(n+4\) is odd, so
Lemma SD-Mersenne-image does *not* exclude \(M_{n+4}\) from the image of
\(f\). The obstruction is the affine / Baker package above, same shape
as for \(x^\star\).)

**Finite status of the \(s=4\) height point.** The point \(M_{n+4}\) is
absent from the pre-descent \(a_n\)-orbit for every odd
\(3\le n\le2001\) (`scripts/verify_repunit_storage_dominance.py
--check-s4`). Combined with the lemmas above, the \(e=1\) \(L=1\)
configuration with \(s=4\) is ruled out for:

- \(n=3,5,7,9\) (Lemma SD-L1-s4-small);
- all odd \(11\le n\le2001\) (orbit scan; also \(i_*^{(4)}>K_\downarrow\)),
  with the Baker / window-gap forms covering the large-\(n\) tail under
  \(K_\downarrow=n^{O(1)}\) (or the weaker
  \(K_\downarrow=o(2^{n/\mu})\)).

**Lemma SD-L1-s-window.** Fix an integer \(s\ge1\) and write
\(y_n(s):=s\cdot2^{n+2}-1\). Suppose \(x_i=y_n(s)\) with \(i\ge1\) and
\(x_j\ge T\) for all \(0\le j<i\). Then
\[
L_i^{(s)}=\frac{3^i a_n}{y_n(s)}
\le
2^{E_i}
\le
L_i^{(s)}\Bigl(1+\frac1{3T}\Bigr)^i.
\]
Whenever \(i\le T\) the multiplicative width is at most \(e^{1/3}<2\), so
the interval contains at most one power of \(2\).

Proof. Identical to Lemma SD-L1-e2-window with target \(y_n(s)\). \(\square\)

**Lemma SD-L1-s-Baker.** If \(x_i=y_n(s)\) for some odd \(n\), fixed
\(s\ge1\), and some \(i\ge1\) before first descent, then
Lemma SD-L1-s-window forces
\[
\bigl|(E_i+n+2)\log2-i\log3-\log(a_n/s)\bigr|
\ll
i\,2^{-n}.
\]
Since \(\log(a_n/s)=n\log3-\log2-\log s+O(2^{-n})\), this is a linear
form in \(\log2\) and \(\log3\) of height \(H\asymp i+n+\log(s+1)\).
Standard lower bounds give a left-hand side \(\gg H^{-C}\). Whenever \(s\)
is fixed and \(i=n^{O(1)}\), the right-hand side is \(n^{O(1)}2^{-n}\),
which is smaller for all large \(n\): contradiction.

**Lemma SD-L1-s-fixed.** Fix an integer \(s\ge1\). Assume
\(K_\downarrow(n)=n^{O(1)}\). Then for all sufficiently large odd \(n\)
(depending at most on \(s\)), the point \(y_n(s)=s\cdot2^{n+2}-1\) does
not occur on the accelerated \(a_n\)-orbit at any index
\(0\le i\le K_\downarrow(n)\).

Proof. Seed equality \(a_n=y_n(s)\) forces \(3^n=s\cdot2^{n+3}-1\). For
fixed \(s\) the right side is \(<3^n\) for all large \(n\) (since
\(\log_2 3>1\)), so the seed is eventually larger than the target and
never equal. Any later hit falls under Lemma SD-L1-s-Baker. \(\square\)

(If \(s=2^{t}\) with \(t\) odd, Corollary SD-L1-s-odd-power already
excludes \(y_n(s)\) for every odd \(n\), with no Baker hypothesis.)

**Lemma SD-L1-s6.** For every odd integer \(n\ge3\), the point
\(y_n(6)=6\cdot2^{n+2}-1=3\cdot2^{n+3}-1\) does not occur on the
pre-descent \(a_n\)-orbit, provided either the finite certificate domain
below applies or \(K_\downarrow=n^{O(1)}\).

Proof. Seed: \(a_n=y_n(6)\) forces \(3^n=3\cdot2^{n+4}-1\), i.e.
\(3^n+1=3\cdot2^{n+4}\). For odd \(n\ge3\) the left side is
\(\equiv1\pmod9\) while the right side is \(\equiv6\pmod9\),
impossible. Direct orbit inspection excludes the target for every odd
\(3\le n\le15\) (in particular \(n=5\), where the affine window is
nonempty, as for \(x^\star\) and \(M_{n+4}\)). For \(n\ge17\) one has
\(x_1>y_n(6)\): it is enough that
\[
(n+1)\log_2 3-n-3-\log_2 6>e_0=1+v_2(n+1),
\]
and the left side exceeds \(1+\log_2(n+1)\ge e_0\) throughout odd
\(n\ge17\). Any later hit is then forbidden by Lemma SD-L1-s-fixed /
the window-gap certificate below. \(\square\)

**Finite status of fixed-\(s\) height points.** For every
\(3\le s\le32\) and every odd \(3\le n\le501\), the point \(y_n(s)\) is
absent from the pre-descent \(a_n\)-orbit
(`scripts/verify_repunit_storage_dominance.py --check-height-s`). For
every such \(s\) and every odd \(n\ge13\) in that domain one moreover has
\(i_*^{(s)}(n)>K_\downarrow(n)\) (window empty); the only nonempty windows
before descent in the band are at \(n=5\) (many \(s\)) and at
\((n,s)\in\{(11,13),(11,26)\}\), all of which miss the target by the
orbit scan. In particular Lemma SD-L1-s6 holds unconditionally through
\(501\), and under \(K_\downarrow=n^{O(1)}\) for all large \(n\).

**Finite status of later height points.** Through odd \(n\le501\), no
pre-descent state equals \(s\cdot2^{n+2}-1\) for any \(2\le s\le16\)
(`scripts/explore_sd_l1_later.py`), matching the broader
`--check-height-s` census through \(s=32\). Combined with
Lemma SD-L1-s2 / Corollary SD-L1-s-odd-power this removes every odd
power-of-two ray unconditionally; combined with Lemmas SD-L1-s4 and
SD-L1-s-fixed every fixed \(s\) is on the same Baker footing as
\(x^\star\). Empirically \(\max h(x_i)\) stays far below \(n+2\) for
\(n>5\) (worst slack still the \(n=5\) prototype \(h=6=n+1\); at
\(n=201\) one has \(\max h=11\) against gate \(203\)).

**Remaining attack.** Close later landings for the two gates of
Proposition SD-L1-reduction:

1. *Height gate (\(e=1\)).* First landing done; pure-rail Yu-finite;
   \(s=1\) reduced to the Mersenne gateway \(x^\star\mapsto M_{n+2}\)
   (excluded for \(n\equiv1\pmod6\), for \(n=3,5\), and Baker-finite
   for \(n\equiv3,5\pmod6\) under \(K_\downarrow=n^{O(1)}\));
   \(s=2^{t}\) with \(t\) odd excluded by Corollary SD-L1-s-odd-power;
   every *fixed* \(s\ge1\) reduced to Baker / \(K_\downarrow=n^{O(1)}\)
   (Lemma SD-L1-s-fixed; explicit \(s=4,6\) in Lemmas SD-L1-s4, SD-L1-s6).
   Remains: \(s=s(n)\) growing with \(n\) (equivalently, unboundedly large
   height landings), and inbound \(e\ge4\) as the mechanism that could
   create them.
2. *Valuation gate (\(e=2\)).* Equivalent to hitting some
   \(1+|s|\cdot2^{n+3}\) (Lemma SD-L1-e2-form). The unit
   \(|s|=1\) point \(z_n\) is excluded through \(501\) by the same
   window-gap method as \(x^\star\); first such state must be an
   \(e\ge3\) landing (Lemma SD-L1-first-v). Empirically
   \(\max v(x_i)\le16\) through odd \(n\le501\) (tightest slack
   \(n+3-\max v=2\) at \(n=5\)). Remains: bound \(v\) after \(e\ge3\),
   or exclude \(|s|\ge3\) (and growing \(|s|\)).

The \(L\ge2\) half is now the size split above: Lemma EC1-gap gives the
exact identity \(G=\lvert s\,2^{E'+n+1}-c\rvert/x_i\); EC1-large reduces
large collisions (\(c=\tfrac12\)) to a Baker/linear-form gap; EC1-near is
the complementary open residual near \(T\).

## 12. Descent step and a conditional closure

**Lemma SD1D-eq.** At a payout \(e_i\ge2\),
\[
(x_{i+1}+1)2^{E_i+e_i}
=
\bigl(3^{n+i+1}-3\sigma_i-2^{E_i+1}\bigr)\Bigl(1+\frac1{x_{i+1}}\Bigr).
\]
Consequently SD1 at \(i+1\) is equivalent to
\[
(3\sigma_i+2^{E_i+1})(x_{i+1}+1)>3^{n+i+1},
\]
unless already \(3\sigma_i+2^{E_i+1}\ge3^{n+i+1}\) (in which case SD1 is
immediate).

**Theorem SD-conditional.** Fix odd \(n\ge3\). Suppose that through first
descent one has \(\theta_i\le5/27\), and that the first descent lands on
\(x_{K_\downarrow}\ge3\). Then SD1 holds for that \(n\).

Proof. From \(\theta\le5/27\),
\[
\sigma_i=\frac{3^{n+i}-R_i}2\ge\frac{11}{27}3^{n+i}.
\]
For SD1S at a stay-above step: the sufficient criterion of §9 reduces to
\(R_i<3^{n+i}(1-2^{1-n})\). Since \(5/27<1-2^{1-n}\) for all \(n\ge3\),
SD1S holds, so every stay-above step preserves SD1. For the terminal
descent landing \(x'\ge3\), Lemma SD1D-eq and the slack bound give
\[
(3\sigma+2^{E+1})(x'+1)
\ge
\frac{11}{9}3^{n+i}(x'+1)
\ge
\frac{44}{9}3^{n+i}
>3\cdot3^{n+i},
\]
so SD1D holds. The start and valuation-one steps are free. \(\square\)

**Corollary (n=3).** Direct computation: \(a_3=13\mapsto5=x_1<7\), with
\(R_0=1<27\) and \(R_1=15<81\). Thus SD1 holds for \(n=3\). (This is also
the unique odd \(n\le4001\) whose first descent lands on a value \(\le5\).)

**Lemma SD-no-1-at-seed.** The first accelerated step of \(a_n\) cannot
land on \(1\). Indeed, that would require \(a_n=(2^e-1)/3\) for some even
\(e\), hence \(2^{e+1}=3^{n+1}-1\). For odd \(n\ge3\) one has \(n+1\) even
and at least \(4\), so
\[
3^{n+1}-1=\bigl(3^{(n+1)/2}-1\bigr)\bigl(3^{(n+1)/2}+1\bigr)
\]
is a product of two even integers differing by \(2\) and both larger than
\(2\). The only powers of \(2\) differing by \(2\) are \(\{2,4\}\), which
force \(3^{(n+1)/2}-1=2\) and \(n=1\), excluded. \(\square\)

**Lemma SD-no-1-pure-rail.** Descent to \(1\) cannot occur after a pure
valuation-one prefix (equivalently: after \(P_i=0\)). If \(P_i=0\) and
\(x_i=(2^e-1)/3\), the descent identity collapses to
\[
3^{i+1}(3^n+1)=2^{i+2}\bigl(2^{e-1}+1\bigr).
\]
For odd \(n\ge3\) one has \(v_2(3^n+1)=2\), so the left side has
\(2\)-adic valuation \(2\). The right side has valuation at least \(i+2\).
Thus \(i+2\le2\), hence \(i=0\), which is Lemma SD-no-1-at-seed. (The
boundary case \(i=1\) also fails directly: \(9(3^n+1)\) is never divisible
by \(8\) for odd \(n\).) \(\square\)

**Gap remaining.**

1. Close **EC1** via the assembly SD-L1 + EC1-large + EC1-near (EC1-large
   already reduced; EC1-near and full SD-L1 remain). Theorem
   SD-length-distinct handles the no-collision side; \(n=3,5\) are
   direct (\(K_\downarrow\le T\)). EC1 plus landing \(\ge3\) closes SD½
   and SD1 via Theorem SD½-affine / Corollary SD1-affine.
2. Exclude descent to \(1\) after a prefix with \(P>0\) (pure-rail done;
   finite through \(4001\)). Landing on \(1\) is the only case in which the
   affine landing estimate with factor \(4/3\) fails.

## 13. Next lemmas on Avenue A

| ID | Statement | Status |
|---|---|---|
| SD-eq / SD-\(\phi\)-dyn / SD-rail / SD-Gamma / SD-T-rail | structure | proved here |
| SD-h-rail / SD-block-length / SD-E-block / SD-seed-h | height-block dictionary; \(E_K\ge K+\pi+1\) | proved here |
| SD-K-shortcut | \(K_\downarrow\le H\) (accelerated vs shortcut length) | proved here |
| SD-K-density | full-window survivor \(\Rightarrow\) \(\rho>\lfloor11n/4\rfloor\) | proved here |
| SD-K-survivor-split | \(H>5n-2\) \(\Rightarrow\) high-odd-density survivor | proved here |
| SD-K-embed | \(a_n<2^{5n-2}\) (residue \(=\) the integer \(a_n\)) | proved here |
| SD-K-e0-prefix | first \(e_0\) steps contribute one odd; suffix dens \(\ge11/20+O(\frac{\log n}n)\) | proved here |
| SD-K-thin | high-odd-density classes have density \(2^{-(0.036+o(1))n}\) | proved here |
| SD-K-nc-strong | \(\rho_t\le\lfloor11n/4\rfloor\Rightarrow H\le5n-2\) | proved here |
| SD-K-rail-dict / even-id / even-equiv | rails \(=100\%\) odd; \(\rho_t=t-((e_0-1)+\sum(e_j-1))\); gap \(\Leftrightarrow\) even budget | proved here |
| SD-K-height-count | \(\rho_t=1+\sum h_j^{\mathrm{eff}}\) | proved here |
| SD-K-rail-criterion | \(11E\ge9R+20P\Leftrightarrow\sum(e-1)\ge\frac9{11}\sum h\) (suffix dens \(\le11/20\)) | proved here (sufficient) |
| SD-K-911-implies | \(11(t-\rho)\ge9(\rho-1)\Rightarrow\rho\le\lfloor11n/4\rfloor\) | proved here (sufficient) |
| Gap SD-K-survivor | \(H(n)\le5n-2\) for odd \(n\ge7\) | open; finite through \(10001\); saturates at \(n=23\) |
| Gap SD-K-nonconcentration | \(\rho_t(n)\le\lfloor11n/4\rfloor\) (explicit itinerary) | open; stronger; finite through \(10001\) (`--check-rho-cap`) |
| Gap SD-K-even-budget | \((e_0-1)+\sum(e_j-1)\ge5n-2-\lfloor11n/4\rfloor\) | open; equivalent to nonconcentration; slack \(0\) at \(n=17,23\) |
| Gap SD-K-911 | \(11(t-\rho)\ge9(\rho-1)\) for odd \(n\ne23\) | open; sufficient; only finite miss \(n=23\) through \(5001\) |
| SD-K-density-6 | full-window-\(6n\) survivor \(\Rightarrow\) \(\rho>\lfloor33n/10\rfloor\) | proved here (exact envelope all odd \(n\ge7\)) |
| SD-K-survivor-split-6 / nc6-implies | \(H>6n\Rightarrow\) high-\(\rho\) survivor; \(\rho_{6n}\le\lfloor33n/10\rfloor\Rightarrow H\le6n\) | proved here |
| Gap SD-K-survivor-6 | \(H(n)\le6n\) for odd \(n\ge7\) | open; **preferred weaker survivor**; finite through \(5001\) |
| Gap SD-K-nc-6 | \(\rho_{6n}\le\lfloor33n/10\rfloor\) for odd \(n\ne11\) | open; preferred; only finite miss \(n=11\) through \(5001\) |
| SD-K-911-6-strong-implies | \(11(t-\rho)\ge9\rho+2\Rightarrow\rho\le\lfloor33n/10\rfloor\) | proved here (sufficient) |
| SD-K-seed-land | \(n\equiv1\pmod8\Rightarrow e_0=2,\,h(x_1)=1\); \(n\equiv5\pmod8\Rightarrow e_0=2,\,h(x_1)\ge2\) | proved here |
| SD-K-score-split | \(\mathrm{score}=11(e_0-1)+\sum\Delta_j-9r_0\) | proved here |
| Corollary SD-K-hard-8 | \(n\equiv1\pmod8\Rightarrow\mathrm{score}=11+\sum\Delta\) | proved here |
| Gap SD-K-911-6-strong | score \(\ge11\) for odd \(n\ne11\) (\(t=6n\)) | open; preferred; eq at \(n=17\); miss only \(n=11\) through \(5001\) |
| Gap SD-K-block-8 | \(\sum\Delta_j\ge0\) for odd \(n\equiv1\pmod8\), \(n\ge17\) | open; **core hard case**; eq only at \(n=17\) through \(5001\) |
| SD-K-v2-35 / first-e / first-h-good | first-block dictionary on \(n\bmod64\) from \(x_1\) | proved here (stable classes) |
| SD-K-h1-17 | \(n=64k+17\Rightarrow e=2\), \(h_1=v_2(3^{n+2}+37)-5\), \(\Delta_1=11-9h_1\) | proved here |
| SD-K-h1-parity | \(k\) odd \(\Rightarrow h_1=3\); \(k\equiv2\pmod4\Rightarrow h_1=4\) | proved here |
| SD-K-rail-closed | \(r\) rails from height \(r+1\) give \(x_r=3^r(y+1)/2^r-1\) | proved here |
| SD-K-e2-17 | \(e(x_2)=1+v_2(3^{h_1}m-1)\) on \(n=64k+17\) | proved here |
| SD-K-e2-odd-3mod4 | \(k\equiv3\pmod4\Rightarrow e(x_2)=2\) | proved here |
| SD-K-e-mod8 | \(h=1\Rightarrow(e=2\Leftrightarrow x\equiv1\pmod8)\) etc. | proved here |
| SD-K-h2-3mod8 | \(k\equiv3\pmod8\Rightarrow e_2=2,\,h_2=1,\,\Delta_2=+2\) | proved here |
| SD-K-e3-expand / e3-stable | third-block dictionary on \(k\equiv3,11,43,59\pmod{64}\) | proved here |
| SD-K-e4-3mod256 | \(k\equiv3\pmod{256}\Rightarrow e_4=2,\,h_4=1,\,\Delta_4=+2\) | proved here |
| SD-K-e4-171mod256 | \(k\equiv171\pmod{256}\Rightarrow e_4=3,\,h_4=1,\,\Delta_4=+13\) | proved here |
| SD-K-e4-67family | \(e_4=3\) on \(k\equiv67\pmod{256}\); \(h_4\) on \(323\bmod512\) / \(579\bmod1024\) | proved here |
| SD-K-block4-local | block-\(4\) outcome from \(x\bmod{32}\) at \(h=1\) start | proved here |
| SD-K-b4start-mod256 | block-\(4\) start residue on \(k\bmod{256}\subset k\equiv11\bmod{64}\) | proved here (finite cert) |
| SD-K-b4start-mod512 | block-\(4\) refinement on \(k\equiv203\bmod{256}\) at mod \(512\) | finite cert |
| Cor SD-K-blocks24-k11mod64 | \((\Delta_2,\Delta_3,\Delta_4)\) table on four mod-\(256\) slices | proved here |
| Cor SD-K-block5-mod512-k11slice | block-\(5\) split on \(k\equiv11\bmod{256}\) | finite cert |
| Cor SD-K-block5-mod8192-1035 | block-\(5\) on \(k\equiv1035\bmod{2048}\) at mod \(8192\) | finite cert |
| SD-K-b4start-mod8192 | block-\(4\) on \(k\equiv459\bmod{512}\) at mod \(8192\) | finite cert |
| SD-K-m-mod512-267 / m-mod8192-267 | \(m\equiv57\bmod{512}\), \(m\equiv6468-k\bmod{8192}\) on \(k\equiv267\bmod{512}\) | proved here |
| SD-K-blocks25-267mod512 | \((\Delta_2,\ldots,\Delta_5)=(2,2,2,2)\) on \(k\equiv267\bmod{512}\) | proved here (assembly) |
| SD-K-compose6 | \(3x_6+1=(2187m+269)/128\) from four \((2,1)\) blocks on \(x_2=18m-1\) | proved here |
| SD-K-e6-param-267 | \(3x_6+1=(1440-492t)+R_t\), \(v_2(R_t)\ge14\); \(e_6=v_2(1440-492t)\) | proved here |
| SD-K-d6-param-267 | \(\Delta_6=11(e_6-1)-9h_6\) from \(L_t=1440-492t\) landing | proved here |
| SD-K-e7-param-267 | deferred \(3x_7+1\bmod{8192}\) split by \(h_6=h(z_t)\) | proof sketch + finite cert |
| SD-K-d7-param-267 | \(\Delta_7=11(e_7-1)-9h_7\) on deferred slice | finite cert |
| Thm SD-K-block-8-17-267mod512 | six-block closure on \(k\equiv267\bmod{512}\) when cum \(\ge16\) | **proved here** |
| Thm SD-K-block-8-17-267mod512-sevenblock | four deferred rows close at block \(7\) | **proved here** |
| SD-K-e6-expand | general \(c_6 m+a_6\) template (267 case via param \(t\)) | programme |
| Cor SD-K-block6-mod8192-k267slice | block-\(6\) on \(k\equiv267\bmod{512}\) | finite cert |
| Cor SD-K-block7-mod8192-k267slice | block-\(7\) on \(k\equiv267\bmod{512}\) | finite cert |
| Thm SD-K-block-8-17-267mod8192 | five mod-\(8192\) classes close at block \(6\) | **proved here** |
| Thm SD-K-block-8-17-779mod8192 | four mod-\(8192\) classes close at block \(7\) | **proved here** |
| Thm SD-K-block-8-17-3851mod8192 | one mod-\(8192\) class closes at block \(8\) | **proved here** |
| Thm SD-K-block-8-17-3mod256 | \(k\equiv3\pmod{256}\Rightarrow\mathrm{rest}\ge17\) | **proved here** |
| Thm SD-K-block-8-17-171mod256 | \(k\equiv171\pmod{256}\Rightarrow\mathrm{rest}\ge17\) | **proved here** |
| Thm SD-K-block-8-17-323mod512 | \(k\equiv323\pmod{512}\Rightarrow\mathrm{rest}\ge28\) | **proved here** |
| Thm SD-K-block-8-17-579mod1024 | \(k\equiv579\pmod{1024}\Rightarrow\mathrm{rest}\ge19\) | **proved here** |
| Cor SD-K-block-8-17-early | four APs, density \(9/1024\) among \(k\), plus \(n=81\) | **proved here** |
| SD-K-x2-mod8 | odd \(k\Rightarrow x_2\equiv5\) or \(1\pmod8\) by \(k\bmod4\) | proved here |
| SD-K-81-clear | \(n=81\Rightarrow\Delta_2=17\ge16\) | proved here (finite) |
| SD-K-res-dens-suff | \(O/L\le0.54\Rightarrow\mathrm{rest}\ge16\) on odd \(k\), \(n\ge81\) | proved here (sufficient) |
| SD-K-EB-suff | \(\mathrm{Extra}\ge\tfrac9{10}B\) and \(O\le\tfrac{21}{10}B\Rightarrow\mathrm{rest}\ge2B\) | proved here (sufficient) |
| Gap SD-K-EB-17 | those EB bounds for remaining \(n=64k+17\ge145\) | open; finite through \(8001\) |
| Gap SD-K-res-dens-17 | residual \(O/L\le0.54\) for \(n=64k+17\), \(k\ge1\) | open; sufficient for block-8-17 |
| Gap SD-K-block-8-17 | \(\mathrm{rest}\ge9h_1-11\) for \(n=64k+17\) | open; eq only at \(n=17\); **closed on density \(9/1024\) of \(k\)** (Cor early) |
| SD-K-linear-6 | \(K_\downarrow\le6n\) from survivor-6 | conditional; finite through \(5001\) |
| SD-K-linear | \(K_\downarrow\le6n\) for all odd \(n\ge3\) | conditional on either \(5n-2\) or \(6n\) gap; finite through \(5001\) |
| SD-Mersenne-image / SD-j0 / SD-length-distinct | distinct-residue half of \(K_\downarrow\le T\) | proved here |
| SD-lift / SD-L1-class / SD-L1-seed | \(L=1\) dictionary; no seed collision | proved here (\(e_0\ge3\) seed gap finite through \(5001\)) |
| SD-xm1-dyn / SD-L1-e2-char / SD-L1-e1-land / SD-L1-pure-Yu | \(L=1\) dictionary | proved here |
| SD-L1-e2-form / unit-size / unit-window | \(e=2\) \(L=1\) \(\Leftrightarrow\) \(x=1+|s|2^{n+3}\); unit \(z_n\) window-gapped | proved / finite through \(501\) |
| SD-hv-exclusive / SD-L1-first-v / SD-L1-first-land / SD-L1-v-seed | first landing safe; \(v\)-growth only at \(e\ge3\) | proved here (Yu-finite / \(e_0=2\) elementary) |
| SD-L1-s1-half / SD-R3-parity / SD-no-3 | SD½ constrains \(s=1\) high landings; odd \(e\) forces \(3\mid R\); orbit avoids \(3\mid x\) | proved here |
| SD-L1-e2-Mersenne | SD½/\(e=2\)/\(s=1\)/\(h=n+2\) \(\Rightarrow\) hit \(M_{n+2}\) from \(x^\star=(2^{n+4}-5)/3\) | proved here |
| SD-L1-e2-preimage-1mod6 | \(x^\star\) absent for \(n\equiv1\pmod6\) | proved here |
| SD-L1-e2-preimage-small / first / window | \(n=3,5\); \(x_1>x^\star\) for \(n\ge9\); affine \(E\)-window | proved here |
| SD-L1-e2-preimage-Baker / window-gap | \(x^\star\) absent for large \(n\equiv3,5\) under mild \(K_\downarrow\) bounds; \(i_*>K\) for \(n\ge9\) through \(2001\) | Baker / Diophantine + certificate |
| SD-L1-e2-preimage | \(x^\star\) absent for all odd \(n\) | closes under \(K_\downarrow=n^{O(1)}\) or \(o(2^{n/\mu})\) |
| SD-L1-s2 / s-odd-power | \(e=1\) \(L=1\) with \(s=2^{t}\) (\(t\) odd) impossible | proved here (Mersenne non-image) |
| SD-L1-s4-seed / small / first / window | \(M_{n+4}\) seed/small/first/affine window | proved here |
| SD-L1-s4-Baker / window-gap | \(M_{n+4}\) absent for large \(n\) under mild \(K_\downarrow\) bounds; \(i_*^{(4)}>K\) for \(n\ge11\) through \(2001\) | Baker / Diophantine + certificate |
| SD-L1-s4 | no \(e=1\) \(L=1\) hit at \(s=4\) (\(x=M_{n+4}\)) before descent | closes under \(K_\downarrow=n^{O(1)}\) or \(o(2^{n/\mu})\); finite through \(2001\) |
| SD-L1-s-window / s-Baker / s-fixed | every fixed \(s\ge1\): \(y_n(s)=s\cdot2^{n+2}-1\) absent for large odd \(n\) | proved here under \(K_\downarrow=n^{O(1)}\) |
| SD-L1-s6 | no \(e=1\) \(L=1\) hit at \(s=6\) before descent | closes under \(K_\downarrow=n^{O(1)}\); finite through \(501\) via `--check-height-s` |
| SD-L1 (full) | no \(L=1\) collision before descent | open on growing \(s=s(n)\) height / inbound \(e\ge4\), and \(e=2\) with \(\lvert s\rvert\ge3\); fixed-\(s\) height under Baker; finite through \(501\) |
| SD-threshold / SD½-start / SD½-rail / SD½-factor | \(\phi<2\) toolkit | proved here |
| SD-deficit-dyn / SD-mass-deficit | \(\rho,d,P\) dictionary | proved here |
| SD-T-budget | \((1+1/(3T))^T(1+1/T)<2\) etc. | proved here |
| SD½-length / SD½-affine | length gates \(\Rightarrow\) SD½ | proved (conditional) |
| SD1-affine | \(K_\downarrow\le T\) and \(x'\ge3\) \(\Rightarrow\) SD1 | proved (conditional) |
| SD-conditional | \(\theta\le5/27\) and \(x'\ge3\) \(\Rightarrow\) SD1 | proved here |
| SD-no-1-at-seed / SD-no-1-pure-rail | no descent to \(1\) if \(P=0\) | proved here |
| EC1-gap | exact \(\lvert2^{E'}-3^L\rvert=\lvert s\,2^{E'+n+1}-c\rvert/x_i\) | proved here |
| EC1-seed-cut | \(n\ge19\Rightarrow a_n\) large | proved here |
| EC1-near-s | both-near \(\Rightarrow\lvert s\rvert<2^{\lceil n/2\rceil-1}\) | proved here |
| EC1-large | large \(L\ge2\) collisions (\(x_i\ge2^{\lceil3n/2\rceil}\)) | reduced to Baker/linear forms; no large hit through \(2001\) |
| EC1-delta | \(\delta=\Theta(n)\) via \(\hat e=4\) layer; \(\sim n/(2(4-\log_2 3))\) | proved here; checked \(11\le n\le41\) |
| EC1-near | near-barrier \(L\ge2\) under \(K_\downarrow\ge T+1\) | open; reduced to \(\Theta(n)\)-window (not \(O(1)\)); specimen \(n=5\) has \(K_\downarrow\le T\) |
| EC1 | no stay-above residue collision before \(j_0\) under \(K_\downarrow\ge T+1\) | open; assembles as SD-L1 + EC1-large + EC1-near |
| \(K_\downarrow\le T\) | soft length gate | open only on EC1; finite through \(5001\); EC1 \(\Rightarrow\) theorem |
| SD½ / \(\theta\le5/27\) | stronger finite invariants | finite through \(4001\) / \(5001\) |
| no-descent-to-1 | \(x_{K_\downarrow}\ne1\) | open only for \(P>0\); finite OK |
| SD1 | first-descent storage-dominance | open; closes under EC1 + landing \(\ge3\) |
| ST1 | strict surplus-transfer sign law | conditional on SD1 |

## 14. Immediate next work

> **Read first:
> [`avenue_a_mean_valuation_route.md`](avenue_a_mean_valuation_route.md).**
> That note (exploratory, no ledger rows) reports three things bearing
> directly on this list:
>
> - **Item 1 below has no terminating condition.** §3 there computes the
>   minimum mean cycle of \(\Delta=11(e-1)-9h\) on the block automaton
>   \(\bmod\,2^m\): it is negative and *independent of \(m\)*. Conditioning on
>   \(k\bmod2^{j}\) pins only the first \(\Theta(j)\) blocks (PCD9), so the
>   bash controls a constant-length prefix while the bad cycles live in the
>   \(\Theta(n)\) tail. The eight proved `Thm SD-K-block-8-17-*` rows and
>   Cor SD-K-block-8-17-early stand; the *scheme* does not extend to a cover.
> - **Gap SD-K-nc-6 is exactly "mean valuation \(\ge20/11\)"** (§2 there),
>   whose two window forms reproduce both exception lists recorded here
>   (\(\{5,11\}\) at \(6n\); \(\{5,17,23\}\) at \(5n-2\)).
> - **The \(5n-2\) and \(6n\) misses are disjoint** (§4 there, DISJ, odd
>   \(7\le n\le1781\)), so proving the *disjunction* is strictly weaker than
>   either gap and would retire the \(n=11\) and \(n=17\) special cases. The
>   window \(t=cn\) is usable only for \(4.56<c\lesssim7.6\), so \(6n\) is
>   well-chosen and should not be widened.

1. Extend **Cor SD-K-block-8-17-early** (density \(9/1024\) of \(k\)
   closed). On \(k\equiv11\pmod{64}\): block-\(4\) mod-\(256\) dictionary
   is Lemmas SD-K-block4-local / SD-K-b4start-mod256 and Cor
   SD-K-blocks24-k11mod64; mod-\(512\) refinements are Lemma
   SD-K-b4start-mod512 and Cor SD-K-block5-mod512-k11slice; mod-\(8192\)
   refinements (Cor SD-K-block6-mod8192-k267slice,
   Thm SD-K-block-8-17-267mod8192,
   Thm SD-K-block-8-17-779mod8192). Next: mod-\(16384\) on
   \(1803,5899,6923,7947\bmod{8192}\); block-\(9\) on \(2315,2827\bmod{8192}\).
   Remaining parallel slices: \(67\bmod256\) with
   \(s\equiv0,4\pmod8\); \(k\equiv59\pmod{64}\); Gap SD-K-EB-17 on the
   unstructured remainder.
2. Finish **SD-L1** later landings in parallel if the nonconcentration gap
   stalls: growing \(s=s(n)\) height / inbound \(e\ge4\), and the \(e=2\)
   gate for \(\lvert s\rvert\ge3\).
3. EC1-near remains a \(\Theta(n)\)-window residual; do not resume a
   fixed-length case bash.
4. Optionally make EC1-large fully effective (explicit Yu/Baker constants
   and an \(n_0\)).
5. Exclude descent to \(1\) for \(P>0\) (pure-rail case done).
6. After SD1, promote ST1 and open SCH1.
