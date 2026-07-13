# Next-Generation Repunit Attack Programme

**Status:** research programme. This document records proposed attacks,
falsification criteria, and the order in which they should be attempted. It
does not assert a proof of repunit-tail descent or of the Collatz conjecture.

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
- promote claims only through CLAIM_LEDGER.md and a matching verifier when
  appropriate.

## 3. Attack order

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
