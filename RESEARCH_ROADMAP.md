# Research Roadmap

This document organises the remaining research options into a systematic
programme. It contains proof targets and experimental plans, not established
claims. The authoritative status of proved statements remains
`CLAIM_LEDGER.md`.

The current exact reduction is:

1. an odd-exponent Mersenne number \(M_n=2^n-1\) follows a closed-form burn;
2. after exactly \(n\) odd-steps it reaches the base-\(3\) repunit
   \[
   a_n=\frac{3^n-1}{2};
   \]
3. the unresolved task is to prove that the trajectory from \(a_n\) eventually
   falls below the original Mersenne level \(2^n-1\).

The main programme below attacks this residual directly.

### Proved foundations (do not re-prove)

These are already in the maintained claim chain; the roadmap builds on them:

- closed-form Mersenne burn and epoch split
  `epoch(2^n-1)=n+\sigma(a_n)` — `recharge_nogo.md`, `mersenne_repunit_reduction.md`;
- almost-everywhere finite stopping time with explicit rate — `stopping_time_density.md`;
- repunit rail-5 hitting density and geometric avoider law — `repunit_rail5_density.md`;
- no global potential \(\log_2 x+g(\tau(x))\) — `recharge_nogo.md`;
- bounded exponential bit-weight potential fixes recharge only, not per-step descent —
  `Exponential_Decay_Potential.md`.

### Strategic context

Two density results already control **size**, not **membership**:

- Terras/Everett: almost every odd integer has finite stopping time.
- REP5-7/8: almost every odd repunit index eventually hits rail 5.

Priority 1 targets something strictly stronger: a **universal** bound
\(\sigma(a_n)\le 3n\) for the explicit sparse sequence \(a_n=(3^n-1)/2\).
This is the non-concentration problem isolated in `repunit_tail_attack.md` §5:
\(a_n\) could, in principle, lie in nested low-valuation classes forever even
though those classes have density \(\le\rho^K\).

`mersenne_repunit_reduction.md` Observation R4 warns that post-\(a_n\) statistics
look generic after the forced first payout. Treat that as a **pivot trigger**:
if the diagonal survivor explorer (Priority 1A) shows no reusable exponent
structure through the \(3n\) window, downgrade the universal-spine target and
record that density-level control may be the practical ceiling.

### Distinct stopping problems (do not conflate)

| quantity | meaning | primary programme |
|---|---|---|
| \(\sigma(a_n)\) | first \(K\) with \(f^K(a_n)<2^n-1\) | Priority 1 |
| \(T(n)\) | first rail-5 hit time for repunit \(a_n\) | Priority 3 |
| \(\operatorname{epoch}(2^n-1)\) | \(n+\sigma(a_n)\) for odd \(n\) | Priority 1 |

Rail-5 hitting gives strict one-step descent once reached, but
\(T(n)<\infty\) for all \(n\) would not by itself prove \(\sigma(a_n)<\infty\).
Priority 3 is secondary unless its 2-adic survivor machinery feeds the surplus
programme.

### Ruled-out directions (for orientation)

- Potentials depending only on \(\tau(x)=v_2(x+1)\) — Theorem RNG1,
  `recharge_nogo.md`.
- Independent enumeration of bad valuation patterns without tracking the
  repunit correction \(A_i\) — `repunit_bad_automaton_notes.md`.
- Global longest-run contraction from block fracture — `Block_Fracture_Lemma.md` §5.

---

## Priority 1 — Repunit-tail surplus

Let

\[
x_0=a_n,\qquad x_{i+1}=f(x_i),\qquad
e_i=v_2(3x_i+1),\qquad E_K=\sum_{i<K}e_i.
\]

The affine accumulation formula is

\[
x_K=\frac{3^K a_n+c_K}{2^{E_K}},
\qquad c_K>0.
\]

The principal quantity is the valuation surplus

\[
S_K(n)=E_K-K\log_2 3.
\]

Ignoring the positive affine correction for orientation, descent below the
Mersenne start requires approximately

\[
S_K(n)>
\log_2\!\left(\frac{a_n}{2^n-1}\right)
=n\log_2(3/2)-1+o(1).
\]

### Provisional theorem target

Prove that for every odd \(n\ge7\), there is some \(K\le3n\) such that

\[
f^{(K)}(a_n)<2^n-1.
\]

This is the empirical Repunit Tail Lemma already isolated in
`repunit_tail_attack.md`.

The constant \(3\) is provisional. It must not be built into a candidate proof
until the empirical constant search below has been extended substantially and
its record-setting structure has been examined.

### Surplus-form target

A proof-oriented sufficient target is to establish, for some \(K\le3n\),

\[
E_K\ge
K\log_2 3+
\log_2\!\left(\frac{a_n}{2^n-1}\right)
+\delta_K(n),
\]

where \(\delta_K(n)\) is an explicit allowance large enough to dominate the
positive affine term \(c_K/2^{E_K}\).

The affine allowance must remain explicit. A proof using only the raw surplus
without controlling \(c_K\) would be incomplete.

---

## Priority 1A — Empirical constant search

Define

\[
C(N)=\max_{\substack{7\le n\le N\\n\ {\rm odd}}}\frac{\sigma_n}{n},
\qquad
\sigma_n=\min\{K\ge1:f^K(a_n)<2^n-1\}.
\]

The present baseline is \(C(10001)=63/23\approx2.73913\). Before fixing a
linear-window constant, extend this search and record:

- every new record for \(\sigma_n/n\);
- the record-setting exponents and valuation prefixes;
- the smallest exact first-descent margin;
- the affine correction penalty at first descent;
- failures or near-failures for candidate constants such as
  \(2.75,2.8,2.9,3.0\);
- how \(C(N)\) changes as \(N\) grows.

### Decision rule for the constant

- If new records remain below \(2.75\) over a substantially extended range and
  the record structure stabilises, use \(3\) as a conservative working
  constant while continuing to label it empirical.
- If records drift upward, revise the working constant before constructing a
  block theorem.
- If the record sequence reveals a parametrised family, analyse that family
  directly rather than extrapolating from the numerical maximum.

This stage protects against promoting a finite-window constant into a theorem
target prematurely.

---

## Priority 1B — Diagonal survivor tree

The first implementation should study exponents \(n\), not arbitrary Collatz
starting values.

For each odd \(n\), follow the repunit tail for up to \(3n\) odd-steps. Call
\(n\) a diagonal survivor at depth \(K\) if the exact orbit has not yet fallen
below \(2^n-1\).

The computation should track:

- the exact valuation prefix \((e_0,\ldots,e_{K-1})\);
- cumulative valuation \(E_K\);
- raw surplus \(S_K(n)\);
- exact descent margin
  \[
  D_K(n)=\log_2\!\left(\frac{2^n-1}{x_K}\right);
  \]
- the correction term \(A_K\) from the normal form below;
- the surviving residue class of \(n\) modulo the required power of two.

### Questions for the survivor computation

1. Do long-surviving exponents form nested residue classes modulo powers of
   two?
2. How many new bits of \(n\) are fixed by each additional bad valuation?
3. Does the number of surviving exponent classes shrink geometrically?
4. Do the same valuation or correction-term blocks recur?
5. Does a long bad block force a later compensating valuation?
6. Are the worst finite examples isolated branches or members of a stable
   family?

### Deliverable

Create an exploratory program, tentatively
`explore_repunit_diagonal_survivors.py`, that emits:

- survivor counts by \(n\)-range and scaled time \(K/n\);
- worst surplus and exact margins;
- nested exponent residue classes;
- repeated valuation blocks;
- candidate block inequalities.

The first stage is diagnostic. Its output is evidence, not a certificate.

**Existing baseline.** `explore_repunit_tail.py` already verifies the forced
first payout, prints valuation ledgers, and checks the empirical \(3n\) window
for odd \(n\le 2001\) (worst ratio \(\sigma_{23}/23=63/23\), smallest margin
\(\approx 0.00122\) bits at \(n=1345\)). The diagonal explorer should extend
this by tracking exponent residue classes and repeated blocks, not duplicate
the basic tail sweep.

---

## Priority 1C — Repunit-tail normal form

The existing exact normal form is

\[
x_i=\frac{3^{n+i}+A_i}{2^{E_i+1}},
\qquad
A_0=-1,
\qquad
A_{i+1}=3A_i+2^{E_i+1}.
\]

The next valuation is

\[
e_i=
v_2\!\left(3^{n+i+1}+A_{i+1}\right)-(E_i+1).
\]

This separates the moving exponential \(3^n\) from the correction term
\(A_i\).

### Theorem-shaped target

Prove that the recurrence for \(A_i\) cannot maintain insufficient valuation
surplus for \(3n\) consecutive steps.

A useful block lemma would have the form:

> For every admissible \(L\)-step repunit-tail block, either the block earns
> at least its required valuation surplus, or the exponent \(n\) is forced
> into one of finitely many deeper residue classes modulo \(2^q\).

The objective would then be to show that exceptional blocks cannot concatenate
indefinitely, or that each concatenation consumes more independent low bits of
\(n\) than a \(3n\)-step survivor can support.

### Warning

`repunit_bad_automaton_notes.md` already shows that independently counting
bad valuation patterns is too weak: many individual patterns intersect the
repunit curve. The recurrence of \(A_i\) and the nesting of the exponent
classes must be retained.

---

## Priority 1B′ — Exact affine-tail control

Before attempting a block-surplus theorem, isolate the contribution of
\(c_K\) in

\[
x_K=\frac{3^K a_n+c_K}{2^{E_K}},
\qquad
c_K=\sum_{i=0}^{K-1}3^{K-1-i}2^{E_i}.
\]

The raw and exact margins differ by the affine penalty

\[
P_K(n)
=\log_2\!\left(1+\frac{c_K}{3^K a_n}\right),
\]

because

\[
\log_2\!\left(\frac{2^n-1}{x_K}\right)
=S_K(n)-P_K(n).
\]

### Required deliverables

1. Measure \(P_K(n)\) along diagonal survivors and at first descent.
2. Derive the strongest uniform bound available from the valuation prefix.
3. Seek a blockwise recurrence for
   \[
   q_K=\frac{c_K}{3^K a_n},
   \qquad
   q_{K+1}=q_K+\frac{2^{E_K}}{3^{K+1}a_n}.
   \]
4. Determine whether \(P_K\) is uniformly negligible, merely bounded, or
   structurally correlated with bad surplus blocks.
5. State the exact surplus threshold including \(P_K\) before proposing any
   block lemma.

### Success criterion

Produce a proved bound \(P_K(n)\le B_K\) or a prefix-dependent bound strong
enough that a surplus inequality implies actual descent.

### Failure criterion

If \(P_K\) can be comparable to the available surplus margin on the survivor
branches, raw-surplus arguments must be abandoned or reformulated using the
exact affine state.

This stage protects against silently discarding the positive affine term, the
second recurring failure mode in earlier approaches.

### Result

This stage is now closed by `repunit_affine_tail_bound.md`. It proves

\[
\log_2(1+q_K)
\le K\log_2\left(1+\frac1{3(2^n-1)}\right)
<\frac{K}{3(2^n-1)\ln2}
\]

before first descent. Thus the affine allowance is exponentially small in
every linear window, and the remaining substantive target is the valuation
surplus itself.

---

## Priority 1D — Exact exponent-residue automaton

For a fixed valuation prefix, the normal form gives congruences of the type

\[
3^{n+i+1}\equiv -A_{i+1}
\pmod{2^{E_i+1+e_i}}.
\]

Because powers of \(3\) have explicit cyclic structure modulo powers of two,
each valuation extension can be translated into restrictions on \(n\).

### Construction target

Build a nested automaton whose states contain:

- the current valuation ledger;
- the correction term \(A_i\) modulo the required power of two;
- surviving classes of \(n\);
- the exact accumulated value/descent inequality.

Unlike the retired bad-pattern enumeration, this automaton must refine the
same exponent classes step by step instead of treating each valuation word
independently.

### Success criterion

The automaton becomes mathematically useful if it reveals a finite collection
of block types with a provable contraction or surplus inequality.

### Retirement criterion

If the state count grows without reusable structure and each finite bad path
continues to define a nonempty exponent class, record that finite modular
exclusion alone is insufficient and move to a cumulative analytic argument.

### Programme-level retirement

Retire the universal-spine target (Priority 1) and document the outcome if **all**
of the following hold:

1. Priority 1D retirement criterion triggers (no reusable block types);
2. Priority 1B shows survivor exponent classes shrink geometrically but never
   exhaust at any tested depth;
3. post-\(a_n\) statistics remain indistinguishable from generic orbits (R4).

In that case the honest ceiling is the proved density chain
(`stopping_time_density.md`, `repunit_rail5_density.md`), not a spine-specific
epoch bound.

---

## Priority 1E — Diagonal merge-or-descend induction

`repunit_tail_merge_reduction.md` introduces the diagonal state

\[
\mathcal D_i(n)=(n+i,E_i,A_i).
\]

Equality of diagonal states forces exact merging, and a tail that merges into
a smaller exponent's pre-descent tail inherits its descent.

The finite computation through \(n\le10001\) classifies \(95.70\%\) of the
exponents by merger, leaving only \(215\) primitive tails.

### Theorem target

Prove that every sufficiently large repunit tail either:

1. descends directly; or
2. coalesces on a diagonal with a tail from a smaller exponent.

### Near-term programme

- classify primitive exponents and diagonal states;
- derive local conditions forcing the common small-gap mergers;
- run deficit-block analysis only on primitive tails;
- seek a density or finiteness theorem for primitive starts.

This programme complements the surplus route: surplus need only be controlled
on primitive tails if all other tails inherit descent by merging.

### Current focal target

`repunit_256_block_target.md` shows that the following statement would close
the repunit-tail problem:

> Every active 256-step valuation block, before descent or merger, has total
> valuation at least \(425\).

The statement is verified over \(1{,}712{,}672\) active blocks for odd
\(n\le10001\). If proved, it yields descent-or-merge by
\(256\lceil n/32\rceil\le8n+248\).

The preferred proof form is: any putative active block of weight at most
\(424\) must force a diagonal collision with a smaller tail.

### Adversarial update

`repunit_low_prefix_obstruction.md` proves that the word
\((2,1^{255})\) occurs on an explicit infinite exponent class, cannot descend
during the block, and cannot collide through equality of full diagonal states.
Hence the fixed 256-floor can only survive through a different universal merger
mechanism for that class.

The nested classes extend the low run past any prescribed finite recovery
horizon, so a recovery theorem based only on the observed block or its deficit
is also ruled out.

`repunit_baker_nonshadowing.md` closes the positive-integer side of the
primary ghost branch: if the tail begins with \((2,1^{K-1})\), then
\(K=O(\log n)\) by Yu's \(p\)-adic Baker theorem applied to
\(v_2(3^{n+1}+7)\).

The roadmap therefore returns to a genuinely global non-shadowing programme,
with a height gate before Baker theory is invoked:

1. normalize each primitive deficit prefix to
   \(v_2(3^m+d)\ge t\) after removing powers of \(3\) from the exact enemy
   constant;
2. classify low-height families, where \(\log|d|\) is bounded or small
   relative to \(t\), and apply \(p\)-adic logarithmic-form estimates there;
3. prove variable-window recovery or off-diagonal merger for the remaining
   high-height moving-deficit patterns, together with merge inheritance on
   non-primitive tails.

`explore_baker_enemy_height.py` supplies the first diagnostic for this gate.
On the current primitive sample, generic reduced enemy constants have
bit-length comparable to their cumulative valuation. Thus the fixed-\(7\)
argument is a real theorem for an exceptional structured branch, not yet a
universal template.

`repunit_baker_applicability_census.md` sharpens the gate on active states.
It defines the enemy coordinate

\[
(m_K,d_K)=(n+K-r_K,d_K),
\qquad
A_K+2^{E_K+1}=3^{r_K}d_K,
\]

and proves that this coordinate is invariant through every valuation-one
run. Through odd \(n\le5001\), only \(46\) of roughly \(341{,}551\) active
states with \(K\ge8\) have reduced-height ratio at most \(0.75\). The longest
observed one-run has length \(17\), but its enemy constant has generic height.

The next theorem target is an enemy-coordinate dichotomy: low-height
coordinates are eliminated by Baker non-shadowing; high-height coordinates
must force surplus recovery or an arithmetic collision usable by the merger
programme.

### Enemy-episode test and strategic revision

`repunit_enemy_episode_analysis.md` tests the most local version of that
dichotomy by compressing a valuation-one run and its terminal payout into one
episode. Through odd \(n\le10001\), terminal repair or a prior-coordinate exit
covers only \(41.94\%\) of Case B episodes. Recovery can require \(129\)
steps even after a one-step run, so a recovery bound depending only on the
run length is not credible.

Moreover, recovery by first descent is automatic once first descent is
assumed, and therefore cannot be used to bound that descent time.

The episode decomposition is retained as a diagnostic, but the primary
programme is revised to:

1. prove local conditions for the frequent small-gap diagonal mergers;
2. remove nonprimitive tails by merge inheritance;
3. apply Baker only to controlled-height enemy families;
4. seek cumulative, adaptive surplus blocks on the residual primitive tails,
   with windows bounded independently of \(\sigma_n\).

The immediate next target is the algebra of gap-\(2\), gap-\(4\), and
gap-\(6\) mergers through the scalar collision condition
\(3A+2^{E+1}=3B+2^{F+1}\).

The overarching target remains:

> A positive integer exponent \(n\) cannot shadow any low-valuation 2-adic
> branch for a number of steps proportional to \(n\), unless it first merges
> into a smaller controlled tail.

The 256-floor remains a valid conditional reduction and finite phenomenon, but
is no longer a plausible standalone local theorem target.

### Model non-shadowing lemma

For the explicit enemy branch \((2,1^{K-1})\), ordinary size gives

\[
K<\log_2(3)(n+1)-2.
\]

Thus this branch cannot shadow through \(3n\) steps. The next target is to
extend this Archimedean-versus-2-adic argument from one closed-form branch to
general low-surplus valuation words.

---

## Priority 2 — Fuse-map cumulative payout

The fuse map compresses a complete trailing-one burn:

\[
x=2^Lm-1
\longmapsto
\Phi(x)=\operatorname{oddpart}(3^Lm-1).
\]

Writing

\[
s=v_2(3^Lm-1),
\]

the approximate logarithmic change is

\[
\log_2\frac{\Phi(x)}x
\approx L\log_2(3/2)-s.
\]

### Theorem target

Prove a cumulative payout inequality

\[
\sum_{i<N}s_i
>
\log_2(3/2)\sum_{i<N}L_i-O(1)
\]

for a suitable variable-length block, unless the orbit has already descended
or merged below its starting value.

### Role in the programme

This route is more general than the repunit-tail programme and may reveal a
global mechanism. It is also harder. It should be pursued after the diagonal
repunit computation identifies concrete recurring burn/recharge blocks.

It is the natural episode-level version of the post-burn margin location
identified in `recharge_nogo.md`: the burn is margin-free at
\(c=\log_2\frac32\), so cumulative payout must come from recharge/escape
episodes, not from trailing-one fuel consumption alone.

### Useful retained files

- `fuse_map_theory.md`
- `fuse_burn_attack.md`
- `explore_fuse_burn.py`
- `explore_mersenne_spine.py`
- `explore_mersenne_formulas.py`

---

## Priority 3 — The 2-adic rail-5 survivor set

`repunit_rail5_density.md` proves

\[
\operatorname{dens}\{n\text{ odd}:T(n)>K\}
=\frac12\left(\frac34\right)^K.
\]

Thus the finite rail-avoiding sets form a nested, geometrically shrinking
family of exponent classes.

### Possible targets

1. Describe the inverse-limit survivor set in \(\mathbb Z_2\).
2. Determine its Hausdorff dimension under the natural 2-adic metric.
3. Describe its symbolic dynamics or construct an explicit finite-state
   presentation if one exists.
4. Determine whether any positive odd integer exponent belongs to the infinite
   survivor intersection.

### Expected value

The first three targets may produce clean mathematics. The fourth would prove
universal rail-5 hitting and is substantially harder.

### Limitation

Rail-5 hitting is not itself Mersenne descent. This branch is secondary unless
its survivor structure supplies tools for the surplus programme.

---

## Priority 4 — Descent-tree survivor geometry

The descent-tree survivor note identifies the Mersenne residue as the
minimal-valuation spine and observes geometric shrinkage over finite depths.

### Possible target

Repair the mismatch between:

- modulus depth in the residue tree; and
- odd-step count in the Terras/Everett large-deviation estimate.

A valid theorem would relate the number of low bits consumed by a valuation
prefix to the time required to cross the descent boundary.

### Limitation

The existing density theorem already gives almost-everywhere descent.
This route matters only if it provides a uniform structural statement about
the exceptional spine, rather than another density estimate.

Repairing Conjecture TREE2 (`descent_tree_survivors.md`) — the mismatch between
modulus depth \(K\) in the residue tree and odd-step count in the Cramér
estimate — would unify this programme with Priority 1A/1C if a valid containment
between discharge level \(L(r)\) and accumulated valuation \(E_K\) can be proved.

---

## Working protocol

Each research branch should pass through the following stages.

### Stage 1 — Exact definitions

- State the map, indexing, domain, and stopping condition.
- Separate odd-step count, modulus depth, and accumulated valuation.
- Write the exact affine correction; do not silently replace it by an
  asymptotic approximation.

### Stage 2 — Diagnostic computation

- Use exact integer arithmetic.
- Print bounds and finite domains explicitly.
- Record counterexamples to candidate lemmas.
- Prefer residue classes and symbolic ledgers over large undifferentiated
  sweeps.

### Stage 3 — Candidate lemma

- Extract one statement with explicit quantifiers.
- Identify every dependency.
- State whether it is universal, conditional, or finite.

### Stage 4 — Adversarial verification

- Test edge cases and smallest parameters.
- Search deliberately for minimal counterexamples.
- Compare prose and verifier domains.
- Distinguish proof ingredients from finite confirmation.

### Stage 5 — Promotion or retirement

- Promote proved statements to `CLAIM_LEDGER.md`.
- Keep finite certificates explicitly bounded.
- Move superseded or misleading approaches to `archive/`.
- Record failed approaches when they rule out a tempting line of attack.

---

## Recommended execution order

Completed diagnostics have:

- extended the empirical constant search through \(n=10001\);
- isolated the affine correction and proved it exponentially negligible;
- implemented diagonal merger and primitive-tail classification;
- tested the fixed 256-block target and found its 2-adic low-prefix
  obstruction;
- separated low-height Baker families from generic high-height Case B;
- tested and retired terminal-payout enemy episodes as a standalone proof.

The revised execution order is:

1. Derive exact local criteria for gap-\(2\), gap-\(4\), and gap-\(6\)
   diagonal mergers.
2. Express those criteria as restrictions on adjacent exponent starts or
   normal-form states.
3. Determine whether the common merger gaps cover all but a structurally
   describable primitive residue tree.
4. Apply Baker non-shadowing only to low-height branches within that tree.
5. On the remaining primitive branches, construct adaptive cumulative
   surplus blocks whose endpoints are defined without reference to the
   unknown first-descent time.
6. Attempt a merge-or-surplus induction and build a verifier for every finite
   ingredient.

### Gap-merger result

This task is completed in `repunit_gap_merger_analysis.md`.

Every first same-diagonal merger lies on an exact collision shell. If the
predecessor cumulative valuations differ by \(2h\), their correction terms
differ by

\[
2^{u+1}\frac{2^{2h}-1}{3},
\]

and their outgoing valuations differ by \(2h\). The smallest shell
\(|E-F|=2\) accounts for \(4527\) of all \(4783\) observed mergers through
\(n\le10001\).

Two infinite synchronization families are proved:

\[
n\equiv31\pmod{64}
\quad\Longrightarrow\quad
x_2(n)=x_4(n-2),
\]

\[
n\equiv2047\pmod{4096}
\quad\Longrightarrow\quad
x_2(n)=x_6(n-4).
\]

The next gap-\(2\) layer is also exact:

\[
n\equiv79\pmod{128},\quad
n\equiv199\pmod{256},\quad
n\equiv323\pmod{512},\quad
n\equiv1289\pmod{4096}
\quad\Longrightarrow\quad
x_3(n)=x_5(n-2).
\]

The fourth family is hidden in the first-merger table because those tails
also meet the \((n-4)\)-tail at the same diagonal.

For gap \(6\), the same local shell law dominates, but no comparably shallow
broad residue family has yet emerged.

`repunit_gap2_sync_tree.md` completes the next symbolic stage. It identifies
17 exact level-\(4\) first-hit cylinders, all on the smallest shell. At
modulus \(2^{24}\), the resolved first-hit masses at levels \(2\) through
\(7\) decline from \(3.125\%\) to \(1.090\%\), with cumulative coverage
\(12.0651\%\).

The decline is compatible with geometric level mass but does not imply
exhaustion; it may leave a positive gap-\(2\) survivor set. The strategy must
therefore combine merger gaps.

### Multi-gap synchronization result

`repunit_multigap_sync_union.md` completes the bounded comparison at common
depth \(20\), levels \(2\) through \(7\), and cumulative valuation cutoff
\(20\).

The gap-\(2\) tree covers \(12.023926\%\) of the odd classes. Adding gap
\(4\) and gap \(6\) raises the union only to \(12.672615\%\). Additional
gaps \(8,10,12\) contribute essentially no shallow mass at this cutoff.

This does not conflict with the \(95.70\%\) eventual merger rate: it shows
that the observed mergers are predominantly a long-time phenomenon rather
than a finite collection of shallow residue families.

### Collision-defect recurrence result

`repunit_collision_defect_dynamics.md` derives the exact normalized relative
recurrence. It also gives an explicit repunit-tail counterexample showing
that even \((d,E,F,\delta,z)\) does not determine the outgoing valuation
pair. Hence the defect recurrence does not close without restoring an
absolute correction coordinate.

The two attempted theorem routes for shell hitting now have clear limits:

1. synchronization-cylinder enumeration grows rapidly and is strongly
   depth-truncated;
2. relative collision-defect compression is not deterministic.

The merger framework remains a valuable induction reduction, but the
immediate proof focus should return to cumulative surplus on primitive tails.
Synchronization families and Baker non-shadowing remain auxiliary mechanisms
that remove structured nonprimitive or low-height cases.

The immediate next task is:

> Reanalyse primitive-tail surplus using adaptive record blocks whose
> endpoints are defined by surplus minima and new maxima, rather than fixed
> lengths or valuation-one episodes.
