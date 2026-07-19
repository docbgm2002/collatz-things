# Avenue A — Comparison Dynamics (Working Note)

**Status:** Active. Storage-dominance is the first lemma. Exact identities and
a finite certificate are recorded below. The universal first-descent
storage-dominance statement remains open. Not a claim-ledger promotion until
the human proof is complete.

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
odd \(3\le n\le511\) (checked in
`scripts/verify_repunit_storage_dominance.py`; the worst ratio is
\(K_\downarrow/T=30/31\) at \(n=5\)). Empirically \(K_\downarrow=O(n)\), so the
gate \(K_\downarrow\le T\) is extremely soft — but it remains unproved.

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

1. Prove \(K_\downarrow(n)\le T\) (or any \(K_\downarrow\le c\,T\) with
   \(c\) small enough for Lemma SD-T-budget). This single gate plus
   landing \(\ge3\) closes SD½ and SD1 via Theorem SD½-affine /
   Corollary SD1-affine.
2. Exclude descent to \(1\) after a prefix with \(P>0\) (pure-rail done;
   finite through \(4001\)). Landing on \(1\) is the only case in which the
   affine landing estimate with factor \(4/3\) fails.

## 13. Next lemmas on Avenue A

| ID | Statement | Status |
|---|---|---|
| SD-eq / SD-\(\phi\)-dyn / SD-rail / SD-Gamma / SD-T-rail | structure | proved here |
| SD-threshold / SD½-start / SD½-rail / SD½-factor | \(\phi<2\) toolkit | proved here |
| SD-deficit-dyn / SD-mass-deficit | \(\rho,d,P\) dictionary | proved here |
| SD-T-budget | \((1+1/(3T))^T(1+1/T)<2\) etc. | proved here |
| SD½-length / SD½-affine | length gates \(\Rightarrow\) SD½ | proved (conditional) |
| SD1-affine | \(K_\downarrow\le T\) and \(x'\ge3\) \(\Rightarrow\) SD1 | proved (conditional) |
| SD-conditional | \(\theta\le5/27\) and \(x'\ge3\) \(\Rightarrow\) SD1 | proved here |
| SD-no-1-at-seed / SD-no-1-pure-rail | no descent to \(1\) if \(P=0\) | proved here |
| \(K_\downarrow\le T\) | soft length gate | open; finite through \(511\) |
| SD½ / \(\theta\le5/27\) | stronger finite invariants | finite through \(4001\) / \(5001\) |
| no-descent-to-1 | \(x_{K_\downarrow}\ne1\) | open only for \(P>0\); finite OK |
| SD1 | first-descent storage-dominance | open; closes under the two gates above |
| ST1 | strict surplus-transfer sign law | conditional on SD1 |

## 14. Immediate next work

1. Prove \(K_\downarrow(n)\le2^n-1\) (softest remaining gate for SD1).
2. Exclude descent to \(1\) for \(P>0\) (pure-rail case done).
3. After SD1, promote ST1 and open SCH1.
