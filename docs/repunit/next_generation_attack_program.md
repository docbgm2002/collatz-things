# Next-Generation Repunit Attack Programme

**Status:** research programme. This document records proposed attacks,
falsification criteria, and the order in which they should be attempted. It
does not assert a proof of repunit-tail descent or of the Collatz conjecture.
The programme is synchronized through PCD17.

## 1. Why a new programme is justified

The existing work has isolated a genuinely arithmetic obstruction involving
valuation words, affine corrections, exponent cylinders on the repunit curve,
historical payout storage, and collision ancestry from smaller repunit tails.
Standard stopping-time, density, local-potential, fixed-block, and shallow
collision arguments each see only part of this structure.

Progress need not mean closing universal descent. A successful attack may
instead produce an exact structural lemma, a sharply formulated conjecture,
or a no-go theorem that removes an entire class of arguments.

## 2. Operating rules

For every attack:

- derive the exact symbolic object before enlarging a census;
- distinguish universal statements from finite diagnostics;
- minimize counterexamples to each proposed lemma;
- record negative results as reusable constraints;
- stop broad computation unless it tests a named arithmetic statement;
- maintain the ordered residual cover in `coverage_portfolio.md`: measure a
  rule only on cases not discharged by earlier sound descent-or-merge rules,
  and require an exact proof that the final residual set is empty;
- promote claims only through CLAIM_LEDGER.md and a matching verifier when
  appropriate.

## 3. Attack order

| Attack | Current state | Handoff |
|---|---|---|
| 1. General-payout shell ancestry | Completed as GPA1--GPA2 | Blocked \(q=3,4\pmod6\) classes moved to Attack 3 |
| 2. Correction-set geometry | Parked, still available | Re-enter for GPA2-eligible or Attack 4 rigid families |
| 3. Payout concentration/diffusion | Active, sharply narrowed | Prove carry/endpoint non-shadowing for the balanced \(q=3\) family |
| 4. Correction/cylinder transversality | Active companion | Add least-representative, primitivity, or prior-descent information |
| 5. Ancestry capacity/expansion | Queued | Use only after a deterministic exceptional family is isolated |
| 6. Induced record map | Queued with constraints | State must pass PCD15 and normalize the PCD17 linear scale |
| 7. Conditioned transfer operators | Queued | Must retain exceptional-cylinder arithmetic |
| 8. Computer-assisted discovery | Supporting | Optimize exact cylinder lifting before enlarging the certificate |

### Attack 1: general-payout shell ancestry

**Question.** Does automatic realisation of the canonical shell partner extend
from \(q=2\) to arbitrary payouts, especially \(q=3\)?

For a payout \(q\ge2\), use

\[
h=\lfloor q/2\rfloor,\qquad
u=E_j+q-2h,\qquad
C=A_{j+1}+S(u,2h).
\]

Test equality of \(C\) with source corrections \(A_i(\mathbf f)\) at aligned
admissible lengths.

**Deliverables.** An exact general-\(q\) criterion, residue obstructions by
payout class, and a census separated by \(q\bmod6\).

**Stopping rule.** If a payout class is identically excluded by a local
congruence, move it to Attack 3 rather than collecting more zeros.

**Result.** GPA1 proves automatic realisation for every \(q\ge2\). GPA2 proves
that the canonical partner is identically unreachable when
\(q\equiv3,4\pmod6\). In particular, the dominant \(q=3\) branch cannot be
solved by the one-partner mechanism. Its immediate handoff is Attack 3;
Attack 2 remains the symbolic route for payout classes not excluded by GPA2.

### Attack 2: correction-set geometry

**Question.** What recursive geometry is hidden in
\(\mathcal A(i,u)\)?

**Candidate tools.** Affine recursions, normalized interval bounds, residue
trees modulo \(3^r\), generating functions, additive energy, and transfer
matrices.

**Target theorem.** A record-extremal correction cannot avoid every
admissible reachable layer unless its valuation word lies in a quantitatively
small rigid family.

**Stopping rule.** Abandon any statistic that fails to distinguish realised
record words from arbitrary compositions after exact small-layer testing.

### Attack 3: payout concentration versus diffusion

**Question.** Can a large record deficit retain its payout mass without
creating reachable ancestry?

Use the normalized payout shares and effective count

\[
N_{\mathrm{eff}}
=\frac{(\sum_jw_j)^2}{\sum_jw_j^2}.
\]

**Target dichotomy.** Either a bounded collection of ancestors carries a
fixed ledger share, or many comparable ancestors occur in controlled
historical-deficit layers. The first branch feeds shell ancestry; the second
feeds a spacing, additive-energy, or amortized charge theorem.

**Stopping rule.** A concentration statistic is useful only if its branches
imply different exact arithmetic constraints. A histogram alone is not
progress.

**Current result.** PCD1 gives an exact initial/eligible/blocked trichotomy
and a blocked concentration-effective-count alternative. PCD2 finds that the
\(110\) dangerous primitive records through \(n=5001\) split \(88/0/16/6\)
across the eligible, initial, blocked-concentrated, and blocked-diffuse
branches. All six diffuse records occur on \(n=471\). The live symbolic test
is now a two-ancestor correction calculation for the blocked branches. PCD4
identifies six universal short mixed shell-fusion identities, but the complete
paired target correction still has to be derived before GPA1 can be applied.
PCD5 rules out the naive transport of that correction for every short fusion
block. PCD6 then supplies the correct affine-aware transport universally: the
canonical shell is annihilated into the high correction after one step. Thus
canonical shells cannot persist as independent states for later pairing, and
the live Attack 3 branch is amortized payout charging and historical spacing.
PCD7 starts that branch: \(2N_B\le Q_B\le Q_K\), so
\(D_K+2N_B\le K\log_2(3/2)\). The next task is to amplify this additive
effective-count charge. PCD8 shows that near-balanced historical blocks and
spacing alone cannot do so: an explicit mechanical word supports arbitrarily
many comparable \(q=3\) ancestors and arbitrarily large later records. The
next task must intersect that balanced language with repunit-cylinder
realization, primitivity, or correction-set geometry. PCD9 resolves the first
of these: every finite word beginning with valuation at least two has exactly
one odd repunit exponent cylinder, so the phase-shifted balanced language is
fully realised at every finite depth. The remaining discriminator must be
prior descent, merger/primitivity, or least-representative growth.
PCD10 reduces the last option to a concrete non-shadowing statement: a bound
on the length of a plateau on which one exponent continues to realise
successive balanced payout blocks. A plateau bound \(L\) forces
\(\operatorname{bitlen}(n_m)\ge E_m-6L+1\). The proposed universal value
\(L=2\) fails at \(m=1200\); the live target is sublinear plateau growth.
PCD11 gives an exact local extension recursion, reducing every balanced block
to a linear congruence and a discrete logarithm of order at most \(64\).
PCD12 finds the full local lift alphabet through \(m=1500\), so no individual
residue is forbidden. The live formulation is a zero-run bound for the 2-adic
lift cocycle driven by the Sturmian mechanical gap word; correlations, rather
than one-step residue exclusions, must do the work.
PCD13 linearizes the cocycle: with starting lift \(t_m\) and exponent carry
\(\kappa_m\), the exponent lift is
\((t_m-\kappa_m)[h_E(2r+1)]^{-1}\), and a plateau is exactly the coincidence
\(t_m=\kappa_m\). The next target is a deterministic bound on consecutive
coincidences of these coupled streams.
PCD14 shows that consecutive coincidences are one contiguous word match:
during a plateau the exponent is fixed and the full carry obeys
\(C'=(C-t)/2^\delta\). The next target is a deterministic non-shadowing bound
between this fixed carry and the concatenated affine-lift word.
PCD15 rules out an endpoint-only fixed-state implementation: each balanced
block consumes five or six unseen high bits, so equal endpoint residues can
have different successor residues. Any transducer must replenish its window
from the carry or use growing state.
PCD16 also rules out a purely real contraction argument: every consecutive
balanced block interval has homogeneous multiplier in \((2/3,3/2)\),
independently of length. The next mechanism must therefore be arithmetic
non-shadowing between the replenished endpoint window and the carry stream.
PCD17 applies that distortion theorem to the exact ledger storage:
\(L/2+7/8<Z_L<9L/8+33/32\) after \(L\) appended blocks. Thus the raw ledger
coordinate is necessarily unbounded; an induced record state must normalize
it without erasing its coupling to the carry.

**Current handoff.** Attack 3 no longer seeks another concentration statistic,
local residue exclusion, endpoint-only transducer, or real contraction. Its
remaining target is a closed carry-replenished transition and a deterministic
non-shadowing bound for \(t_m=\kappa_m\). Attack 4 should be developed in
parallel as the source of least-representative, primitivity, and prior-descent
constraints. Larger cylinder censuses are deferred until the exact lifting
engine avoids repeated full-modulus exponentiation.

The integral-escape reformulation in `integral_escape_frontier.md` separates
the qualitative and quantitative goals. Universal eventual descent needs only
the exclusion of an infinite terminal plateau on every residual branch, or
equivalently infinitely many nonzero exponent lifts. The stronger sublinear
plateau target is retained only when pursuing an explicit bound such as
\(\sigma(a_n)\le3n\).

IEF3 adds a dual arithmetic route for the balanced terminal branch. If
\(q_L\equiv B_L2^{-E_L}\pmod{3^{R_L}}\) is the least nonnegative endpoint
residue, then any bound \(q_L/L\to\infty\) excludes a fixed positive starting
state from the infinite word. The exact diagnostic currently finds
\(q_L\ge2^{5L-1}\) through \(L=10000\). Proving any superlinear lower bound is
now a named symbolic target; the finite exponential floor is not presumed.
IEF5 shows that a nonzero dual digit resets \(q\) to modulus scale and proves
\(q_L>3^{R_{s(L)}}/672\), where \(s(L)\) is the last reset. It is therefore
enough to establish the very weak gap condition \(27^{s(L)}/L\to\infty\);
positive digit density and short zero runs are unnecessary.

IEF7 identifies the dual digit with the lift digit of the canonical relaxed
starting cylinder modulo \(2^{E_L}\). This sharpens the qualitative route
again: proving that the common digit is nonzero infinitely often directly
excludes every fixed positive starting state, without any reset-gap rate.
The converse only constructs integral affine block endpoints and may include
extra powers of two, so it is not an exact Collatz realization. The next
symbolic experiment groups the mechanical word at the continued-fraction
denominators of \(2/\log_2(3/2)-3\), seeking a standard-word recursion that
forces a nonzero lift at infinitely many such scales.

IEF8 now supplies that recursion. After the first appended block, the
characteristic Sturmian prefixes satisfy
\(S_k=S_{k-1}^{a_k}S_{k-2}\), and their bridge pairs compose without carrying
the full affine correction. The top standard lift is nonzero whenever

\[
v_2\!\left(q_{S_{k-1}^{a_k}}-u_{S_{k-2}}\right)<E_{k-2}.
\]

This valuation inequality infinitely often is the current qualitative
handoff. The diagnostic finds a maximum valuation of \(4\) through
\(Q_k=111457\), against a tail depth of \(125743\). No bounded-valuation claim
is made. Derive a recurrence for the cross-difference or a low-bit invariant
that survives standard-word composition; enlarging the convergent census is
secondary.

Because every tail standard prefix begins with the \(r=3\) block,
\(u_{S_{k-2}}\equiv23\pmod{32}\). It is therefore sufficient to prove
\(q_{S_{k-1}^{a_k}}\not\equiv23\pmod{32}\) infinitely often. This is the
smallest current target, but PCD15 still forbids treating the endpoint residue
alone as a closed five-bit state.

IEF9 supplies a separate analytic formulation of the same infinite residual.
The complete balanced parity vector has odd positions
\(d_i=i+2\lceil\gamma i\rceil\), where
\(\gamma=\log_2(3/2)/2\), and inverse-conjugacy value

\[
\xi=-\frac13-\frac43\sum_{i\ge1}
(2/3)^i4^{\lfloor\gamma i\rfloor}.
\]

This series converges in \(\mathbb Q_2\) but lies on the exact Archimedean
Hecke--Mahler boundary \((2/3)4^\gamma=1\). Proving
\(\xi\notin\mathbb Q\) eliminates the balanced itinerary. Existing complex
transcendence theorems require strict interior convergence, so the acceptable
next step is a genuinely \(2\)-adic irrationality argument, preferably using
the IEF8 standard-word repetitions and their rational periodic approximants.

IEF10 completes the weaker positive-integer exclusion. Repeating a standard
parity prefix gives a rational \(2\)-adic approximant of height
\(O(E_k2^{E_k})\), while the characteristic word shares
\(E_k+E_{k-1}\) bits with it. If a fixed integer realized the tail, an
ordinary nonzero integer of size \(O_x(E_k2^{E_k})\) would be divisible by
\(2^{E_k+E_{k-1}}\). Baker's finite irrationality measure for the logarithmic
slope makes \(E_k\) at most polynomial in \(E_{k-1}\), giving a contradiction.
The deterministic infinite balanced branch is therefore discharged
qualitatively. IEF11 extracts the actual reusable rule: agreement for
\(E_k+G_k\) bits with a period-\(E_k\) rational inverse of height
\(H(E_k)2^{E_k}\) is enough whenever
\(G_k-\log_2H(E_k)\to\infty\). Fixed phase shifts lose only a fixed number of
agreement bits and are therefore covered. Attack 3 now hands back to the
residual portfolio: classify whether other terminal languages meet this
periodic-prefix criterion or need separate rules.

IEF12 closes the apparent intercept loophole. Bugeaud and Kim prove that
every Sturmian word has infinitely many prefix-plus-period completions with a
uniform agreement exponent exceeding \(2.5\). Critical factor discrepancy
controls the nonuniform balanced code length up to an additive constant,
leaving linear parity-bit excess, while the
eventually periodic Collatz inverse has height \(O(N^2 2^N)\). Thus every
critical-slope Sturmian intercept is discharged. The residual classification
must now detect the first genuinely non-Sturmian behaviour rather than search
for another phase of the same mechanical word.

IEF13 removes much of that non-Sturmian region as well. If every finite block
factor has bounded critical discrepancy and the block word has Diophantine
exponent greater than \(1\), bounded discrepancy makes the nonuniform code
length asymptotically constant per block, so every positive repetition
surplus remains linear after the parity morphism. Bounded
discrepancy keeps rational inverse height at \(O_D(N^2 2^N)\), so IEF11
applies. The new attack split is exact: force unbounded critical discrepancy,
force superlinear factor complexity, or obtain descent before either limit
language forms.

IEF14 replaces the coarse bounded/unbounded discrepancy split by an adaptive
one. At a prefix/period approximant, let \(K\) be the largest critical
discrepancy of a factor in its footprint and \(G\) its parity-bit agreement
surplus. The rational inverse has height \(O(N^2 2^{N+2K})\), so
\(G-2K-2\log_2N\to\infty\) is enough. Experimental ledgers should report this
margin directly.

IEF15 attacks negative discrepancy without symbolic approximation. With
\(S_L\) the cumulative log multiplier and
\(Z_L=\sum_{j\le L}2^{S_L-S_j}\), the exact affine composition gives
\(x_L\le2^{S_L}x_0+(65/64)Z_L\). If \(S_L\to-\infty\) along endpoints where
\(Z_L\le B\), a minimal counterexample is at most \(65B/64\), reducing the
branch to a finite verification.

IEF16 should be applied before both adaptive rules. The known necessary
lower-parity-density equality for a rational non-cyclic orbit is exactly
\(\liminf S_L/L=0\) in block coordinates. Hence neither positive nor negative
linear lower drift is a live terminal language; only sublinear discrepancy
and critical-envelope oscillation remain.

IEF17 consolidates the result into one survivor profile: above the FIN1
window, density-critical, outside the IEF13 low-complexity discharge, with no
divergent periodic-prefix margin, and with \(Z>64\cdot10^6/65\) eventually along every
arbitrarily deep negative excursion. Attack work should now target this
intersection only; cycles remain separate.

IEF18 tightens the periodic-prefix coordinate. For a preperiod/period pair
\((A,B)\), it charges only the total and suffix-positive parity drift
\(J(A)+J(B)\), rather than the symmetric IEF14 budget \(2K\). Future searches
should rank candidates by this directional margin and retain the exact
rational-height margin as a finite diagnostic.

IEF19 removes unbounded sublinear discrepancy from the residual by itself.
If \(S_L=o(L)\), any word with \(\operatorname{dio}(w)>1\) is discharged.
Together with IEF16, the terminal symbolic attack therefore splits into
\(\operatorname{dio}(w)=1\) and \(\limsup S_L/L>0\), subject to the other
IEF17 coordinates.

IEF20 localizes the same argument. A fixed-surplus periodic-prefix family is
discharged whenever its complete preceding drift envelope is sublinear at the
footprint scale. Thus the positive-limsup attack should test whether recurrence
returns at much larger critical scales after each excursion. On the other
side, exponent one forces \(p(n,w)/n\to\infty\); proving that terminal cylinder
ancestry forbids this strong return scarcity remains open.

IEF21 makes the oscillation test directional and exact. For a full block word,
\(J(\chi(W))\) is its endpoint drift minus its past minimum. A useful
preperiod/period approximation is therefore discharged when the two terminal
draw-ups and the footprint-to-agreement drift loss are sublinear. Searches
should report these three quantities; a large internal peak that is shed
before a cut is not a surviving obstruction.

### Attack 4: correction/cylinder transversality

Study the two encodings

\[
\mathbf e\longmapsto A(\mathbf e),\qquad
\mathbf e\longmapsto n_0(\mathbf e).
\]

**Target theorem.** A word with an exceptional correction, small least
exponent representative, and long record deficit belongs to an explicit
rigid family.

**Stopping rule.** Reject independence claims that do not control the minimum
representative or omit record and primitive hypotheses.

**Current entry point.** PCD9 shows that finite cylinder compatibility is
automatic for the balanced family, while PCD10--PCD14 identify the least
representative and carry data that finite compatibility omits. Study the joint
encoding

\[
\mathbf e\longmapsto
\bigl(A(\mathbf e),n_0(\mathbf e),C(\mathbf e),t(\mathbf e)\bigr)
\]

at cylinder changes and plateau endpoints. The first acceptable lemma must
distinguish the balanced word from arbitrary realised cylinders using
primitivity, earlier merger, or a quantitative minimum-representative bound.

### Attack 5: ancestry capacity and expansion

Replace pointwise reachability by a weighted incidence graph between high
prefixes and smaller repunit-tail states. Study expansion, collision
multiplicity, and Hall-type capacity.

**Target theorem.** Too many primitive record prefixes cannot remain
simultaneously unmatched because the ancestry graph has insufficient
exceptional capacity.

**Stopping rule.** The graph must yield a deterministic statement about every
surviving prefix, not merely a density-zero exceptional set.

### Attack 6: the induced record map

Define a transition between strict deficit records, retaining

\[
(D_K,A_K,\text{payout profile},\text{cylinder residue}).
\]

Search for monotonicity, compact normalized regimes, or finitely many
asymptotic transition types unavailable at individual odd steps.

**Stopping rule.** Any state compression must pass an adversarial continuation
test: equal compressed states may not permit incompatible future behaviour.

**Inherited constraints.** PCD15 refutes fixed-width endpoint residue plus
Sturmian phase as a closed state, and PCD17 makes raw \(Z_K\) unbounded even
inside the balanced deficit band. A viable record map must replenish endpoint
bits from the carry and normalize ledger scale without identifying states
that admit incompatible continuations.

### Attack 7: conditioned transfer operators

Construct an operator for repunit exponent cylinders surviving a deficit
barrier. Seek spectral contraction conditioned on the repunit curve, followed
by classification of any low-dimensional exceptional subshift.

**Stopping rule.** Almost-everywhere estimates are insufficient; the operator
must retain enough arithmetic data to address exceptional repunit cylinders.

### Attack 8: computer-assisted lemma discovery

Generate exact primitive record prefixes, extract symbolic features, search
for short inequalities or dichotomies, minimize counterexamples, and return
surviving statements to human proof.

SAT/SMT and exact dynamic programming may operate on valuation words and
corrections, but numerical descent prediction without a symbolic statement is
not a deliverable.

**Immediate engineering task.** The current balanced-cylinder implementation
repeats full-modulus power computations as precision grows and does not scale
cleanly from \(1500\) to \(10000\) prefixes. Before extending PCD12, replace
that update with a streaming, checkpointed, or otherwise incrementally lifted
power residue. The output must still certify the exact PCD13 carry identity at
every transition.

## 4. Review protocol

After each attack, record:

1. the exact statement tested;
2. what was proved;
3. what was refuted;
4. the smallest counterexample or obstruction;
5. whether the route continues, branches, or stops;
6. which later attacks inherit the result.

This turns failed attacks into cumulative mathematical information rather
than disconnected experiments.
