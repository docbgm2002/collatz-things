# Opus 5 wide-attack task portfolio

**Status:** Exploratory / proof targets. Nothing here is promoted to
`CLAIM_LEDGER.md` until it produces an exact lemma with a falsifier and a
verifier. Notation follows `NOTATION.md`.

**ALL TWELVE TASKS ARE DONE.** Outcomes are recorded inline below, and the
synthesis — what changed, the three structural filters, the consolidated
proposed ledger rows, the mid-flight corrections, and what to do next — is in
[`OPUS5_WIDE_RESULTS.md`](OPUS5_WIDE_RESULTS.md). Run the whole suite with
`python3 scripts/run_all_wide_attack.py`.

**Purpose.** The maintained programme has narrowed to Avenue A
(storage-dominance / comparison dynamics) plus the IEF symbolic frontier.
This file is a deliberately *wide* set of alternative architectures for an
Opus 5 session to attack one at a time. Each task states the exact first
deliverable, the falsifier, and the kill criterion, and is pre-checked
against the four closed barriers of
`docs/no-go/outside_box_avenue_triage.md` §14:

1. finite-state information cannot control the least exponent representative;
2. density/entropy cannot eliminate an individual exceptional cylinder;
3. variable-height / variable-dimension Diophantine bounds are tautological;
4. virtual collisions mixing congruence data from different words are void.

**Cold-start reading order (fresh session, no prior context).** Read, in
order: `NOTATION.md`; `docs/no-go/outside_box_avenue_triage.md` §§10–15
(the four barriers and the restart condition — the immune system of this
repo); `docs/no-go/outside_box_avenue_portfolio.md` (Avenues A–K, so
nothing here is re-derived); the Avenue A progress block in that file;
then this file. Consult `CLAIM_LEDGER.md` before asserting anything is
open or closed. For W10/W11 specifically, read
`docs/repunit/payout_concentration_diffusion.md` §15 (PCD13, the exact
plateau cocycle) and `docs/repunit/integral_escape_frontier.md`
(IEF1, IEF5, IEF8) first — those sections define the objects the tasks
attack.

**Pre-verified identities.** The claims in W1/W2/W8 below were
machine-checked before handoff (exact integer arithmetic): the linear
form \(2^{E_K}x_K=3^Kx_0+c_K\) (2000 random cases), \(f(4n+1)=f(n)\) for
odd \(n<20000\), the cylinder splitting identity with the \(+1\) margin
noted in W1, and the TWR1 tower lane (\(d\le4\), all \(e=2\), exact
Mersenne endpoint).

**Session protocol for Opus 5.** One task per session. Deliverable is a
note in `docs/` using the claim-status vocabulary, plus (where computation
occurs) a `scripts/explore_*` or `scripts/verify_*` program in exact
integer arithmetic. Stress every candidate rule on \(n=471\) (732 odd
steps, the known hard primitive) before believing it. Do not update
`CLAIM_LEDGER.md` from a finite run.

---

## W1 — Additive superposition and the interaction ledger

> **DONE (session 5) — AVENUE CLOSED.** Deliverable:
> `docs/no-go/superposition_interaction_ledger.md`, verifier
> `scripts/verify_superposition_ledger.py` (9 checks). All three
> deliverables complete; the kill fires on both clauses. **(ii) the exact
> expansion:** \(C^{(T)}\) is affine on each cylinder with slope
> \(\lambda_w=6^{o_w}/2^T\), so
> \(I_T=(\lambda_u-\lambda_w)a+(\lambda_u-\lambda_v)b+(\rho_u-\rho_w-\rho_v)\).
> The defect is a **slope** mismatch, not carry bookkeeping: \(o_u\ne o_w\)
> forces \(|\lambda_u-\lambda_w|\ge\frac56\max(\lambda_u,\lambda_w)\), so
> \(I_T\) is of trajectory size. This corrects the task's own guess that the
> obstruction is "binary carry propagation". **(i) W1.a, as a pincer:** for
> odd \(n=a+b\) the parts have opposite parity, so the three words differ at
> step 1 and the closed-form regime is empty; where it is nonempty (even
> \(n\)) it is vacuous — all 6581 agreeing triples with \(a,b<200\),
> \(T\le8\) have the all-zeros word, hence \(I_T=0\) trivially. The one
> exact regime, \(n=a+2^Nt\), is the cylinder/affine identity and its part
> \(2^Nt\) is **virtual** (barrier 4, and this file's own global kill rule).
> **(iii) census:** over every odd \(n\le501\) and every two-part
> decomposition, \(\min_a\max_T|I_T|/\rho_T\ge11.8\), with the interaction
> still \(\ge0.775\) of the trajectory. \(n=471\) testbed:
> \(|I|/\rho\approx10^{225}\). Proposed rows SIL1--SIL4 in §9.

### Motivating question (Dr Bry)

Take the initial number and split it as \(n=b_1+\cdots+b_r\) where each
\(b_i\) is already known to reach 1. Can the certificates for the parts be
combined into a certificate for \(n\)?

### Honest framing first

Existence of such a decomposition is free (\(n=1+1+\cdots+1\)), so the
entire content lives in the **interaction term**: \(C\) and \(f\) are not
additive, and the failure of additivity is exactly binary carry
propagation between the parts. Any viable version of this idea is a
theorem about controlling that interaction, not about choosing summands.

There is one regime where superposition is *exact* and it collapses to
known machinery. From the linear form of the accelerated map,

\[
2^{E_K}x_K \;=\; 3^K x_0 + c_K,
\qquad
c_K=\sum_{t=0}^{K-1}3^{K-1-t}2^{E_t},
\]

the map is affine in \(x_0\) *conditional on the valuation word*. Hence if
\(n=a+2^{N}t\) with \(a\equiv n\bmod 2^{N}\) and \(N\ge E_K(a)+1\), the
itineraries agree for \(K\) steps and (verified 2000 random cases; at
\(N=E_K\) exactly, agreement fails in roughly half of sampled cases, so
the \(+1\) is required in the uniform statement)

\[
x_K(n)=x_K(a)+3^K\,2^{N-E_K}\,t .
\]

This is the standard cylinder/affine identity already carried by the repo
(`docs/repunit/repunit_affine_tail_bound.md` and the transfer-defect
algebra). **W1.a (expected easy lemma, prove and file it):** every
decomposition whose parts share the leading itinerary of \(n\) reproduces
the affine identity and adds nothing. This closes the naive version
cleanly and should be written down so it is not rediscovered.

### The live object

The non-collapsing version: parts whose itineraries *differ*. For ordinary
\(C\) with common time \(T\),

\[
C^{(T)}(x)=\frac{3^{o(T,x)}}{2^{T-o(T,x)}}\,x+\rho(T,x),
\]

where \(o\) counts odd steps and \(\rho\) depends only on the parity word.
For \(n=a+b\), define the interaction ledger

\[
I_T(a,b)\;=\;C^{(T)}(a+b)-C^{(T)}(a)-C^{(T)}(b),
\]

which has an exact expansion in the three parity words and their
mismatch positions. Target statement shape:

> **Superposition transfer (proof target).** There is an explicit
> predicate \(Q(a,b,T)\) on the pair of *actual* trajectories such that
> \(Q\) plus descent of both parts forces either descent of \(a+b\) below
> a stated threshold or a merge with an actual smaller trajectory.

### Why this is not yet closed by triage

Triage §12 closes *virtual* congruence mixing; here both parts carry
actual trajectories, satisfying the §15 restart condition in additive
rather than gap coordinates. Avenue A is the special case
\(b=n-(n-g)\)-type subtractive comparison on one diagonal; W1 asks whether
the two-sided (both parts free) version buys anything the one-sided
version does not.

### Concrete testbed

Use decompositions into states with *known closed binary normal forms*, so
carries are computable in closed form: tower members \(w_d(M)\) have exact
carry-free periodic binary expansions of period \(2\cdot3^{d-1}\) (TWR1),
and \(3(2^L-1)\) has the protected-window form of the Block Fracture
Lemma. First experiment: decompose repunit states \(x_s(n)\) as
(tower/Mersenne part) + (remainder) and compute \(I_T\) exactly.

### First deliverable

(i) W1.a proved. (ii) The exact expansion of \(I_T(a,b)\) in the three
parity words. (iii) A finite census: for every odd \(n\le 5001\), the
minimum over decompositions \(n=a+b\) (both odd parts \(\le n/2\)… state
the exact family) of the first time \(Q\)-style control fails, versus
\(\sigma(n)\).

### Falsifier / kill

Kill if every decomposition family tested has interaction ledger growth at
the same rate as the raw correction ledger (i.e. \(I_T\) is just \(c_K\)
bookkeeping re-partitioned — the analogue of the scalar-flux collapse in
triage §3), or if control of \(I_T\) is shown to require the itineraries
to agree (which is W1.a again). The \(n=471\) test: if no decomposition of
\(a_{471}\)'s pre-descent states admits sub-ledger interaction growth,
close the avenue.

---

## W2 — The certificate semigroup (the version of W1 that can work)

> **DONE (session 2) — AVENUE CLOSED.** Deliverable:
> `docs/no-go/certificate_semigroup.md`, verifier
> `scripts/verify_certificate_semigroup.py` (25 checks, exact arithmetic).
> All four sub-deliverables complete. The kill fires, but *not* by the
> predicted barrier-1 route: the proved transport rules split into
> **forward-orbit rules** (burn, all four mod-8 rails — void: they enlarge a
> finite certified set only finitely), **one-parameter rules**
> (\(\sigma=4n+1\), the \(e{=}2\) predecessor selector \(P_2\)) whose orbit
> has counting function \(\sim\frac{|B'|}4(\log_2X)^2\) with countable
> \(2\)-adic closure, and the **unrestricted predecessor selectors**
> \(P_e\), whose orbit is literally \(\{n:n\text{ reaches }1\}\). The
> nominated escape hatch fails: the burn is a forward-orbit rule.
> Incidental find: **TWR1 = \(P_2^{\,d}\)** exactly, with the domain
> condition \(M\equiv1\ (2\cdot3^{d-1})\) recovered as the integrality
> condition \(3^d\mid z-1\). W2's only live descendant is W4.
> Proposed rows CSG1--CSG5 in §9 of the note; `CLAIM_LEDGER.md` untouched.

### Idea

Addition does not commute with \(f\), but an algebra of *affine maps*
partially does, and closure statements of this type are provably within
reach: Applegate–Lagarias settled the wild-semigroup conjecture, a
closure statement about a Collatz-related semigroup, without touching the
conjecture itself. So: replace "sum of certified numbers" by "orbit of
certified numbers under certificate-preserving maps."

Known exact generators already in or near the repo:

- \(f(4n+1)=f(n)\) for odd \(n\): one-step merge, so \(P\)-certificates
  transport across \(n\mapsto 4n+1\);
- \(n\mapsto 2n\) (trivial for \(C\));
- the Mersenne burn \(2^tu-1\to 3^tu-1\) (Andaloro; `recharge_nogo.md`);
- the tower lifts \(w_d\) (TWR1), transporting the entire \(e{=}2\) lane;
- rail-3 fixed-division bridge and rail-7 escape formulas
  (`Mod8_Rail_Descent.md`, `collatz_rail7_new_results.md`).

### Target

> **Certificate-orbit problem.** Let \(S\) be the semigroup generated by
> all maps \(g\) with a proved transport rule
> "descent certificate for \(n\) yields one for \(g(n)\)". Let
> \(B=\{x \text{ odd}: x\le 10^6\}\) (FIN1). Characterize the orbit
> \(S\cdot B\): its density, its 2-adic closure, and its intersection with
> the repunit family.

Even a negative structural answer is valuable: if \(S\cdot B\) is
contained in a proper 2-adic congruence class union, that is an exact
no-go for all certificate-transport proofs of this shape (a sibling of
SH1), worth filing.

### First deliverable

(i) A formal definition of "transport rule" tight enough to exclude
trivialities. (ii) The generator inventory above, each with its proved
transport lemma. (iii) An exact computation of the orbit density of
\(\langle 4n+1,\,2n\rangle\cdot B\) (this sub-case is elementary 2-adic
bookkeeping and should be closed completely). (iv) Search the repo's exact
identities for one *new* generator; the shell-fusion identities of PCD and
the \(L=1\) dictionary of Avenue A are the first places to look.

### Falsifier / kill

Kill if every proved transport rule is parity-word-preserving on a
bounded window — then the orbit is a bounded-depth modular language and
barrier 1 applies. The task must show at least one generator that moves
between itinerary cylinders (the burn does; verify this survives the
formal definition).

### Priority

High. Cheap first deliverable, provable sub-results, and it is the
mathematically sound cousin of the additive idea.

---

## W3 — Carry cocycle over the solved polynomial model

> **DONE (session 12) — COLLAPSES ON ITS OWN CRITERION; ONE IDENTITY KEPT.**
> Deliverable: `docs/no-go/carry_cocycle_polynomial_model.md`, script
> `scripts/explore_carry_cocycle.py`. The decomposition
> \(3n+1=\Pi(n)+2\kappa(n)\) with \(\Pi(n)=(2n\oplus n)\oplus1\) is exact
> and easy. **The finding is \(v_2(\Pi(n))=\tau(n)=v_2(n+1)\):** the
> polynomial model's valuation is the trailing-ones count. Combined with the
> burn lemma (\(\tau\ge2\Rightarrow e=1\)) and
> \(\tau=1\Rightarrow e\ge2\), the two valuations are **exactly
> anti-correlated** — \(\min(e,v)=1\) always, \(e\ne v\) for 100.0% of odd
> \(n<200001\). So "integer = polynomial + carries" is true as an identity
> and false as an approximation: the carry **replaces** the itinerary rather
> than perturbing it, and the polynomial model's biggest divisions land
> exactly on the burn states where the integer model's are smallest. That is
> why the \(\mathbb F_2[x]\) theorem is easy and why it cannot be borrowed.
> **Kill fires:** \(\kappa\) is a function of the state, so any Birkhoff sum
> is determined by \((x_0,e\text{-word})\) and reproduces \(c_K\) — the
> triage §3 scalar-flux collapse verbatim. TWR1 sanity check passes
> (\(\kappa\bmod2^{12}\) marches \(4095,2047,1023,\ldots\) down the burn)
> but on a lane already known in closed form. No ledger rows proposed.

### Idea

The Collatz analogue over \(\mathbb F_2[x]\) (no carries) is a settled
theorem: divisions and the \((x+1)\)-multiplication commute cleanly and
every polynomial terminates. Integer Collatz = polynomial Collatz +
carry propagation. Formalize this as an extension: write the integer step
as the \(\mathbb F_2[x]\) step composed with a carry cocycle \(\kappa\),
and ask which repo quantities are cocycle-cohomological.

> **Target.** Express the storage variable \(R_i(n)\) (Avenue A) or the
> correction \(c_K\) as a cocycle sum over \(\kappa\), and reformulate
> storage-dominance \(0<R_i(n)<3^{n+i}\) as a boundedness/coboundary
> statement. If SD1 becomes "\(\kappa\) is a coboundary on the repunit
> family," cohomological tools (rigidity of transfer cocycles, Livšic-type
> arguments over the 2-adic odometer) become applicable in principle.

### Barrier check

Triage §§1,3 closed CQCA *scalar flux* arguments: summed conservation laws
collapse to affine bookkeeping. W3 is only alive if it uses the
two-dimensional spacetime structure (where in the word the carries occur),
not row sums. The kill criterion is inherited verbatim: any formulation
whose content survives summation over a row is dead on arrival.

### First deliverable

The exact algebraic decomposition (integer step = polynomial step ∘ carry
correction) with the cocycle identity verified by script on the tower lane
(where TWR1 says the carry stream is exactly periodic — the cocycle should
be visibly a coboundary there, a sanity check with a known answer).

### Priority

Medium. High conceptual upside, high collapse risk; the TWR1 sanity check
decides quickly.

---

## W4 — Krasikov–Lagarias difference inequalities on the repunit-aligned tree

> **DONE (session 9) — DELIVERABLE ANSWERED, AVENUE CLOSED.** Deliverable:
> `docs/density-cycles/kl_rail_restricted_tree.md`, script
> `scripts/explore_kl_rail_restricted_tree.py`. **The comparison returns
> EQUALITY.** \(P_e(y)=(2^ey-1)/3\equiv-3^{-1}\pmod{2^m}\) for every
> \(e\ge m\), so a node's residue mod \(2^m\) is fixed by a bounded
> *suffix* of its \(e\)-word: the rail restriction selects a constant
> fraction of words (shares stabilise at 0.189/0.189/0.563/0.056) and leaves
> the exponent untouched. The dominant rail \(5\bmod8\) is exactly
> \(-3^{-1}\bmod8\), the W2 \(\sigma\)-ghost residue. **The kill is the
> gap, not the exponent:** the repunit family has counting function
> \(O(\log x)\) (1292 below \(2^{4096}\)) while the complement of an
> \(x^{0.84}\) set is \(\sim x\) — a shortfall of \(x/\log x\) that no
> exponent improvement closes. The *supporting* role fails too: Avenue A's
> survivors are \(O(\log^2x)\)-many \((n,i)\) pairs, not a positive-density
> set, so there is nothing for a density theorem to shrink. And the repunit
> states spread uniformly over the four rails (0.245/0.245/0.250/0.259) while
> the tree's words concentrate on rail 5 — the restriction points the wrong
> way. **W2's hand-off is closed by the same gap.** 0.84 is *not* re-derived;
> only the comparison question is answered. No ledger rows proposed.

### Idea

The strongest known unconditional coverage results (predecessor counts
\(\gg x^{0.84}\)) come from Krasikov–Lagarias systems of difference
inequalities on the backward tree, solved by nonlinear programming. The
repo's Avenue C stalls on a termination lemma. Instead of termination,
import the K–L machinery *restricted to the repunit/Mersenne-aligned
subtree*: count predecessors of the FIN1 basin inside the arithmetic
progressions that the repunit pre-descent states actually occupy
(rails mod 8, the \(8y+1\) tower rail, the mod-\(2^{n+1}\)
distinct-residue structure from Avenue A).

### Target

A positive-proportion (within the named progression family) discharge
theorem feeding Avenue A: fewer surviving comparison states, and an
explicit density floor replacing the current census-only evidence.

### Barrier check

Barrier 2 says density cannot finish the job. Framing is therefore
explicitly *supporting*: shrink the survivor set that Avenue A schedules
must handle; never present density as descent. This is the same division
of labour as COR1–COR3.

### First deliverable

The K–L inequality system written for the mod-8 rail-restricted tree, with
its LP/NLP solved exactly (rational arithmetic) at small depth; compare
the exponent obtained against the unrestricted 0.84.

### Priority

Medium-high. Known-sound technique, never yet specialized to this
repo's structures; bounded downside.

---

## W5 — Syracuse 3-adic distribution conditioned on the repunit family

> **DONE (session 10) — DELIVERABLE COMPLETE; CONDITIONING VACUOUS.**
> Deliverable: `docs/repunit/syracuse_3adic_conditioning.md`, script
> `scripts/explore_syracuse_3adic_conditioning.py`. **The conditioning has no
> content.** \(a_n\to-1/2\) in \(\mathbb Z_3\) (a Dirac mass), but the affine
> identity kills the \(3^Kx_0\) term mod \(3^k\) once \(K\ge k\), leaving
> \(x_K\equiv c_K2^{-E_K}\) — a function of the **valuation word alone**.
> Verified on 3916 seed pairs. **The distribution matches**, once the
> reference is right: *not* uniform on \(\mathbb Z/3^k\) (states are never
> divisible by 3) and *not* uniform on the units (mod 3 the law is
> \(1/3,2/3\), since \(x=2^{-e}\) and \(P(e\text{ odd})=2/3\)) — both wrong
> references show a large stable spurious bias. Against the correctly
> modelled Syracuse law every \(E\)-scale bucket sits at fair-sample noise,
> **except** the \(E\)-scale-0 bucket, which is exactly the pre-forgetting
> regime — an internal consistency check. **The target does not follow:**
> Tao's decrement is an *ensemble* statement over random words; the
> decrement lemma is *single-orbit* equidistribution — the same object W11
> and W10 hit from the ergodic and arithmetic sides. **No 3-adic character
> carries the plateau obstruction**, which lives 2-adically in \(n_m\).
> **W5-D, the useful output:** \(f\) contracts 3-adically at \(\log3=1.099\)
> (destroying seed information) and expands 2-adically at
> \(\mathbb E[e]\log2=1.397\) (creating it; measured mean \(e=2.0152\)).
> Tao's method works on the destroying side. No ledger rows proposed.

### Idea

Tao's almost-boundedness proof runs on Syracuse random variables: the
3-adic distribution of \(2^{-E_K}\)-weighted states and a Fourier
decrement ("entropy gain") as valuations accumulate. The repunit family
has measure zero, so the theorem does not apply — but the *mechanism*
(characters of \(\mathbb Z_3\), decrement per valuation block) is exactly
the missing quantitative control in the plateau / least-representative
problem (PCD16–17, IEF frontier): plateaus are precisely windows where the
2-adic lift matches a power-of-three carry, i.e. where a specific
character sum fails to decrement.

### Target

> **Deterministic decrement lemma (proof target).** Along any balanced
> \(q=3\) blocked phase of an actual repunit orbit, the relevant
> \(3^{R_L}\)-character sums decay at an explicit rate unless the dual
> digit stream is eventually zero — reconnecting to IEF10's qualitative
> exclusion with a quantitative reset-gap bound (the bound IEF left open).

### Barrier check

Barrier 2 again: distributional statements alone cannot kill a cylinder.
The task is honest only as an attack on the *quantitative reset-gap*
inside the already-qualitative IEF framework, where the repo has an exact
affine recursion for the dual residue to hang estimates on.

### First deliverable

Compute the empirical 3-adic distribution of repunit orbit states at
matched \(E\)-scales against the Syracuse stationary measure
(script; \(n\le 2001\)); identify which characters carry the plateau
obstruction; state the decrement lemma precisely.

### Priority

Medium. The one task on this list aimed directly at the current deepest
open coordinate (reset gaps), using the only known mechanism that has
produced a strong Collatz theorem in the last decade.

---

## W6 — Machine synthesis inside the surviving potential class

> **DONE (session 7) — PREMISE CORRECTED, NEW FINITE NO-GO.** Deliverable:
> `docs/no-go/machine_synthesis_surviving_class.md`, verifier
> `scripts/verify_machine_synthesis.py` (9 checks; z3 + exact cycle search,
> cross-checked). **Premise correction:** the quantized-log class is *not*
> unsearched — **SUFF1 + CONN1** already close it for every \(j\) and every
> \(m\ge3\); certificates were rediscovered independently here. W6's
> literal first deliverable is already a ledger theorem. **The surviving
> branch is the two-variable one**, \(V(x,n)\): the SH1 shadow cancels an
> \(n\)-dependence only inside a single \(a_n\) orbit, and the realised
> shadow depth on orbits is only \(N^*=12\) over 3464 states (10 on
> \(n=471\)) — logarithmic, so SH1 gives only a finite no-go there.
> **New result:** on the two-variable coordinate
> \((x\bmod2^m,\tau,\lfloor Q\log_2x\rfloor-\lfloor Q\log_2a_n\rfloor)\),
> certificates exist from *actual orbit states* at \((m,j)=(4,1),(6,1),(8,2)\)
> over \(n\le101\) — a finite no-go extending SH1 into \(V(x,n)\).
> **Methodological caution (MSY4):** at finer coordinates the search returns
> SAT, but the coordinate is then essentially injective (compression
> \(\approx0\)) and the SAT is **vacuous** — it reports an empty problem,
> not a candidate. Any future run must publish compression with its verdict.
> Next step is a *bigger window*, not a bigger solver. Rows MSY1--MSY4 in §10.

### Idea

SH1/SH2/BND1 killed every one-step potential below the quantized full
logarithm \(\lfloor 2^j\log_2 x\rfloor\); the manuscript marks that
boundary as where the no-go programme *terminates* — meaning the
surviving class has never been searched. Termination-prover technology
(matrix interpretations, SAT/SMT-synthesized ranking functions) is
precisely automated search over ranking-function classes. Point it at the
surviving class only, and at the two-variable setting SH1 does not cover:
potentials \(V(x,n)\) on (state, repunit exponent) pairs, decreasing only
on *residual* steps (Avenue F's rank idea, now with automated synthesis
instead of hand-guessing).

### Constraints (hard, from the ledger)

No claim of one-step decrease for all odd \(x\) (SH1). No bounded
correction to \(\log_2x\) (BND1). The synthesized object must read either
quantized-log bits or genuine second-variable data. Any candidate the
solver returns must be verified symbolically, then stress-tested on the
\(n=471\) blocked-diffuse phase and on the SH1 shadow family
\(1275\mapsto1913\mapsto1435\) (it must *not* claim decrease there unless
its domain excludes it).

### First deliverable

An SMT encoding of "V decreases on residual steps through first descent,
for all states in the finite window", solved for increasing windows;
either a candidate \(V\) surviving \(n\le 5001\) (then attempt proof) or
an UNSAT certificate at small quantization depth \(j\) — which would be a
*new finite no-go extending SH1 into the surviving class*, publishable in
the ledger as a bounded certificate either way.

### Priority

Medium-high. Both outcomes are filable, which is rare.

---

## W7 — Finish shrinking the IEF17 survivor profile with combinatorics-on-words

> **DONE (session 11) — FRONTIER SHARPENED; THE SPLIT IS THE RESULT.**
> Deliverable: `docs/repunit/ief17_genericity.md`, script
> `scripts/explore_ief17_genericity.py`. Under the critical Bernoulli
> ensemble (\(P(r{=}4)=\beta=0.419023\), the unique zero-drift frequency —
> the same \(\beta\) as W11's Sturmian slope), IEF17's coordinates split.
> **Coordinates 2, 3, 4 are GENERIC:** \(\liminf S_L/L=0\) by SLLN;
> \(\operatorname{dio}(w)=1\) because excess repetition is \(O(\log L)\)
> (measured \(g=17\)--\(23\) vs \(\log_2L\approx16.6\)); no prefix margin
> diverges by the same bound. So the symbolic portfolio IEF13--IEF21
> discharges essentially nothing — **W7 outcome 2 holds for the symbolic
> coordinates**, and further combinatorics-on-words mining is spent.
> **Coordinate 5 FAILS generically and discharges the generic word:** \(Z_L\)
> at a record low is \(O(1)\) (a fresh record has accumulated no time at or
> below its own level — the minimum sits at the *edge* of the range, not the
> bulk). Measured: **0 of 910 record lows** reached \(B_X\); largest
> \(Z=583\) against \(B_X=984{,}615\), a factor \(1.7\times10^3\).
> **Sharpened frontier:** the IEF17 residual is *not* generic — it is
> measure-zero, and coordinate 5, the only one carrying an arithmetic input
> (\(B_X\) from FIN1), is the single binding condition. Actionable
> consequence: \(B_X\) scales linearly with FIN1's cutoff \(X\), so
> extending the exhaustive descent certificate genuinely tightens a frontier
> coordinate. No ledger rows proposed.

### Idea

The residual symbolic object is tightly profiled: non-Sturmian, with
(unbounded discrepancy or superlinear factor complexity), repetition
exponent one or positive linear-drift excursions (IEF13–IEF21). This is
now a pure combinatorics-on-words class. The literature
(Bugeaud–Kim repetition exponents, Berthé–Delecroix bounded remainder
sets, Adamczewski–Bugeaud complexity bounds, Ostrowski numeration carry
automata) has classification theorems for exactly such profiles that the
repo has not yet mined past Bugeaud–Kim.

### Two acceptable outcomes

1. A new discharged coordinate: some literature theorem shows the profile
   class is empty or forces a property IEF18–IEF21 already discharges.
2. A *certified example word* realizing the full IEF17 profile — proving
   the symbolic route cannot close alone and that arithmetic input
   (W5's decrement, or Avenue A coupling) is necessary. This converts a
   vague "frontier" into a theorem-shaped boundary.

### Barrier check

Triage §13 warns: word-complexity facts without an exact
descent-or-merger consequence do not promote. Outcome 2 is exempt because
it is a negative structural result about the method, not a descent claim.

### First deliverable

A literature-mining note mapping each IEF17 coordinate to the sharpest
known theorem, with the gap stated exactly; then pursue whichever outcome
the mapping favours.

### Priority

Medium. Bounded effort, guaranteed to sharpen the frontier statement
even on failure.

---

## W8 — Interference of exact normal forms (two-tower arithmetic)

> **DONE (session 6) — RE-SCOPED, CRITERION MET, FAMILY FORECLOSED.**
> Deliverable: `docs/no-go/two_tower_interference.md`, verifier
> `scripts/verify_two_tower_interference.py` (14 checks).
> **Re-scoping:** the "laboratory for W1's ledger" motivation died with W1
> in session 5; the intrinsic exact-lane question was pursued instead.
> **Ghost algebra:** with \(\Xi_{d,d'}=1-(4/3)^d-(4/3)^{d'}\), one has
> \(\Lambda_d=\Xi_{d,d}\) exactly, \(3\Xi_{d,d'}+1=4\Xi_{d-1,d'-1}\) (so
> \(\Xi=P_2^{\min}\) of \(-(4/3)^{|d-d'|}\)), and
> \(f^{\min}(\Xi_{d,d'})=-3^{-|d-d'|}\). **New exact lane:** the halved
> diagonal sum \((w_d(M)+w_d(M'))/2\) lies in the *same tower cylinder* as
> \(w_d\) and has \(e\)-word prefix \(2^d1^{V-1}\),
> \(V=\min(M,M')-2d-1\); verified to 758 bits. Differences, off-diagonal
> sums and \(w_d\pm2^j\) are all closed-form too. **But foreclosed:** every
> alignment resolves onto a ghost already in the repo — \(-1\) (Mersenne
> burn), \(-1/3\) (the W2 \(\sigma\)-ghost), \(-3^{-k}\) (block
> constants), \(\Lambda_d\) (TWR1). No new structure; the tower normal forms
> should not be revisited as a source of lanes. Structural moral recorded in
> §4.1: **this repo's exact lanes shadow *rational* 2-adic ghosts; the hard
> open objects shadow *irrational* ones.** Rows TTI1--TTI4 in §8.

### Idea

A narrower, fully concrete slice of W1 worth its own line: TWR1 gives an
infinite family of states with *exactly known* periodic binary expansions
and frozen 2-adic tails separating at bit \(2\min(d,d')+1\). Sums and
differences of two tower members therefore have carry patterns computable
in closed form — the only known infinite family where the interaction
ledger of W1 is exactly solvable. Classify the trajectories of
\(w_d(M)\pm w_{d'}(M')\) (and \(w_d(M)\pm 2^k\)) for small windows: if any
sub-family has closed-form itineraries, it is a new exact lane like SPN1,
and a direct laboratory for superposition-transfer statements.

### First deliverable

Exact first-odd-step and \(e\)-word computation for \(w_d(M)+w_{d'}(M')\)
as a function of \((d,d',M,M')\) via the LTE normal forms; script plus
note. Success criterion: any closed-form sub-lane. Kill if carries
destroy periodicity immediately outside the frozen-tail overlap for all
alignments.

### Priority

Medium-low as a bet; very cheap; natural first Opus warm-up task because
everything needed is already proved in TWR1.

---

## W9 — Explicit-constants upgrade of every Baker-gated threshold

> **DONE (session 1).** Deliverable:
> `docs/no-go/baker_explicit_constants_audit.md`, verifier
> `scripts/verify_baker_explicit_constants.py` (37 checks, exact
> arithmetic). Outcome: all eight invocations are two-log forms; the
> Avenue A \(L=1\) Baker hypothesis is **eliminated** (explicit crossover
> \(n\ge161\) from Rhin's proposition, inside the scanned range, leaving
> only \(K_\downarrow(n)\le6n\)); BAKER1--3 gains the exact closed form
> \(v_2(3^m+7)=2+v_2(m-\alpha)\), so its finite-range envelope needs no
> theorem at all (true max \(K=17\) at \(n=1197\) through \(n\le50001\),
> against the repo's empirical \(30\log_2(n+1)+10\)). Two rows deferred:
> a numeral for \(C_7\) via Bugeaud--Laurent (W9-E), and writing out
> EC1-large's coefficients. Nothing promoted to `CLAIM_LEDGER.md`;
> proposed rows BAKEX1--4 are listed in §9 of the note.

### Idea

The repo invokes transcendence inputs generically: Yu's \(p\)-adic theorem
(multi-log, enormous constants) in the Baker-nonshadowing notes, and
"Baker / irrationality of \(\log_2 3\)" for the Avenue A large-\(n\) tails
(\(x^\star\), \(z_n\), the \(K_\downarrow\) crossover). Two families of
much sharper *fully explicit* results exist and have never been
substituted in:

- real two-log bounds (Laurent–Mignotte–Nesterenko lineage) and the
  sharpest published effective irrationality measure of \(\log 3/\log 2\);
- \(2\)-adic **two-log** bounds (Bugeaud–Laurent), which are dramatically
  stronger than Yu's general theorem whenever the linear form has only two
  logarithms — and the repo's applicability census
  (`repunit_baker_applicability_census.md`) already identifies which forms
  are two-term.

### Target

For each gate currently closed only asymptotically, compute an explicit
crossover \(N_0\) such that the gate is closed for all \(n\ge N_0\), then
close \(n<N_0\) by the existing scan scripts (several already run to
\(501\)–\(5001\)). Any gate whose \(N_0\) lands inside scanned range
becomes a **finished unconditional lemma** — the cheapest route on this
list to promoting something into the ledger.

### First deliverable

An audit table: every Baker/irrationality invocation in the repo × the
sharpest applicable explicit theorem × the resulting \(N_0\) × the
existing scan range. Then execute the best gap-closures.

### Falsifier / kill

None needed — this is bounded bookkeeping with proved inputs. Kill
individual rows only when the explicit \(N_0\) is astronomically beyond
any feasible scan *and* the form is genuinely multi-log.

### Priority

**Highest of the new tasks.** Low risk, uses only proved mathematics, and
can convert conditional Avenue A gates into unconditional ones.

---

## W10 — Digit arithmetic of powers of three (the reset-count bridge)

> **DONE (session 4) — AVENUE CLOSED.** Deliverable:
> `docs/no-go/digit_bridge_ceiling.md`, verifier
> `scripts/verify_digit_bridge_ceiling.py` (6 checks). **(a) consolidated:**
> for odd \(A\equiv1,3\ (8)\) there is a unique ghost \(\alpha_A\in\mathbb Z_2\)
> with \(3^{\alpha_A}=A\) and \(v_2(3^n-A)=2+v_2(n-\alpha_A)\) (or 1 on a
> parity mismatch); the least \(n\) matching to depth \(W\) is exactly
> \(\alpha_A\bmod2^{W-2}\). This is BAKER1--3 for general \(A\), so the
> ceiling and the W9 enemy branch are one statement. **(b) the bridge
> exists at the best possible height \(c=1\)** (W11-C), so W10's stated kill
> ("unbounded height \(c\)") does **not** fire. **(c) Stewart applies and is
> vacuous.** PCD10 forces \(\operatorname{bitlen}(n_m)\ge E_m-6\ell+1\), so
> \(3^{n_m}\) has \(2^{\Theta(E_m)}\) digits while the plateau window has
> width \(O(E_m)\): the guaranteed nonzero digits expected in the window are
> \(<10^{-10}\) in every live regime. Worse, Stewart's guarantee is
> **non-increasing in the plateau length** — the input is anti-correlated
> with the event it must exclude, and becomes non-vacuous only when the
> plateau is already linear in \(m\). Recorded failure mode: not the height
> but the **exponent**, so no sharpening of \(c\) can help; only a *local*
> digit theorem for \(3^R\) would reopen it, and the bridge is in place to
> receive one. Proposed rows DBC1--DBC3 in §8.
>
> *Session 4 also corrected a stream mislabelling in the W11 note* — see
> `docs/repunit/rotation_cocycle_rigidity.md` §3 and §7bis.

### Idea

IEF needs the lift/dual digit stream to be *not eventually zero*
(qualitative) with controlled reset gaps (quantitative). The exact
integral bridge identifies the dual digit with the starting-cylinder lift
digit. If, along a concrete branch family, that stream can be identified
with (a window of) the binary digits of explicit integers of the shape
\(3^{R}c\) with \(c\) of bounded height, then off-the-shelf effective
theorems apply:

- Stewart's effective lower bound on the number of nonzero binary digits
  of \(3^R\) (\(\gg \log R/\log\log R\)) — nonzero digits are exactly
  resets, so this is a quantitative infinitely-many-resets statement;
- Stewart/Senge–Straus two-base sparseness: integers simultaneously
  digit-sparse in base 2 and base 3 are effectively bounded — relevant
  wherever a gate demands a state be simultaneously structured in both
  bases (the Mersenne/repunit spine is exactly such a demand).

### Honest framing

The elementary ceiling — matching \(3^{R}\) against a fixed 2-adic target
to depth \(v\) forces \(R\) into a progression mod \(2^{v-2}\)
(ord/LTE) — is likely already implicit in the PCD nested-cylinder jump
statement; consolidating it is part (a), not a discovery. The real
content is the **bridge lemma** (b): an exact identification of the reset
stream with digit windows of bounded-height \(3^Rc\) integers, valid on a
named branch class. The carry shifting block-by-block across a plateau is
the known obstacle; the bridge must either absorb the shift or restrict
to a sub-branch where \(c\) stabilizes.

### First deliverable

(a) The consolidation note. (b) The bridge lemma attempted on the
eventual-plateau branch (where IEF says the high carry is *eventually
exhausted* and the exponent is fixed — the friendliest case, and the case
IEF1 makes decisive). (c) If (b) succeeds there: apply Stewart, file the
result; this would be a quantitative strengthening of IEF10's qualitative
exclusion.

### Falsifier / kill

Kill if the bridge provably requires unbounded-height \(c\) on every
branch class (then the digit theorems are tautological — barrier 3 — and
the failure note should say exactly where the height enters, which feeds
W11).

### Priority

Medium-high. Aimed point-blank at the stated live target ("sublinear
plateau growth"), with proved effective inputs waiting on the far side of
one bridge lemma.

---

## W11 — Rotation-cocycle rigidity: the barrier-2 breaker

> **DONE (session 3) — AVENUE CLOSED, WITH A TRANSFER.** Deliverable:
> `docs/repunit/rotation_cocycle_rigidity.md`, verifier
> `scripts/verify_rotation_cocycle_rigidity.py` (10 checks). (i)–(iii) all
> complete. **(i) kills it:** PCD15's displacement identity says the fibre
> map multiplies \(2\)-adic distance by exactly \(2^{\delta_m}\), so the
> system has Lyapunov exponent \(5+\beta=2+2/\log_2(3/2)=5.41902\ldots>0\),
> while every compact-group extension — and every finite tower — is
> fibrewise isometric. Furstenberg, Veech/Oren/Conze and Denjoy--Koksma are
> **inapplicable**, not merely hard. **(ii) is vacuous:** through 8000
> blocks, every Sturmian factor of length \(\le257\) carries more than one
> lift value, so there is no \(\varphi\) on the circle to test. **(iii) run
> anyway and it localises the obstruction:** DK holds textbook-perfectly for
> the gap word at all Ostrowski scales through \(Q=4563\) (sums in
> \([-1,0]\), Var \(=2\)) and fails for the lift/plateau streams. The
> positive-entropy branch of the Remark is where the system actually lives,
> and it yields only almost-every statements, which W11's own kill rule
> forbids. **Transfer (the session's real output):**
> \(C=\lfloor3^n/2^{E+2}\rfloor\), so a plateau run is exactly an agreement
> between the affine lift word and a window of the binary digits of
> \(3^n\) — this is **W10's bridge lemma (b) on the plateau branch, at
> height \(c=1\)**, so W10's stated main risk is removed before it starts.
> Proposed rows RCR1--RCR4 in §8; `CLAIM_LEDGER.md` untouched.

### Idea

PCD13–PCD14 already say it: the plateau condition \(t_m=\kappa_m\) is a
word-matching **cocycle driven by the Sturmian coding of a rotation**.
That object — a cocycle over an irrational rotation with values in a
compact abelian group (\(\mathbb Z_2=\varprojlim \mathbb Z/2^\delta\)) —
has a developed rigidity theory the repo has not touched:

- **Furstenberg's criterion:** a compact-group skew product over a
  uniquely ergodic rotation is itself uniquely ergodic iff no nontrivial
  fiber character makes the cocycle a measurable coboundary.
- **Veech / Oren / Conze coboundary criteria** for step-function cocycles
  over rotations, decided by the continued fraction of the slope — and
  IEF8 has already built the exact continued-fraction renormalization of
  this very slope.
- **Denjoy–Koksma:** for bounded-variation drivers, cocycle sums at the
  Ostrowski scales \(q_k\) are bounded by the variation — exact control
  at precisely the Sturmian scales where IEF8 renormalizes.

### Why this can evade barrier 2

Density/entropy statements fail because they cannot see one exceptional
cylinder. **Unique ergodicity is an every-point statement**: if the
plateau skew product is uniquely ergodic, then along *every* orbit —
including the one actual balanced word — the fiber digits equidistribute,
so nonzero lifts (resets) have positive density. That is strictly
stronger than the requested \(o(m)\) plateau bound. This is the only
mechanism on either portfolio that upgrades a measure statement to an
individual-orbit statement by theorem rather than by census.

### The hard step (state it before believing anything)

The rotation drives the *gap word*; the carry \(\kappa_m\) is arithmetic
(powers of three mod powers of two), not given as a function on the
circle. The work is to exhibit the plateau indicator as (BV or
step-function observable on the rotation) composed with an explicit
arithmetic re-coordinatization — or to prove this is impossible, which
would itself sharpen PCD12's correlation warning into a structural
theorem. PCD15's "fixed-width endpoint machine must replenish from the
carry" is the same obstacle seen from the transducer side; W11 asks
whether the replenishment is exactly a compact-group extension.

### First deliverable

(i) A precise dictionary: PCD13 lift recursion \(\to\) candidate skew
product \((x,y)\mapsto(x+\alpha,\,y+\varphi(x))\), stating exactly what
\(\varphi\) must be and where the arithmetic carry breaks the picture.
(ii) The Furstenberg character test computed formally: which character
sums must be non-coboundaries, in terms of quantities the repo already
computes. (iii) A Denjoy–Koksma experiment at the IEF8 scales
(script exists: `explore_balanced_q3_sturmian_renormalization.py`) —
measure cocycle-sum growth at \(q_k\) against the BV prediction.

### Falsifier / kill

Kill if (i) proves the carry term is *not* expressible over any finite
tower of rotation extensions (then record the obstruction — it likely
means the system is a genuinely 2-and-3-adic joining, see the
Rudolph–Johnson remark below). Kill any use of the theory that only
yields almost-every statements — the whole point is the every-point
conclusion.

### Remark (positive-entropy branch)

IEF13 splits survivors into (unbounded discrepancy) vs (superlinear
complexity). The superlinear-complexity branch has positive entropy
flavour; measure rigidity for \(\times2\times3\)-type joint structure
(Rudolph–Johnson lineage) is the natural pincer partner there, with W7
covering the low-complexity side. Speculative — one session maximum, and
only after (i)–(iii).

### Priority

**High.** It targets the repo's own declared quantitative frontier with
the one tool class built for individual-orbit conclusions.

---

## W12 — S-unit gcd machinery: the missing back-end for Avenue D

### Idea

Triage §11 killed variable-height Diophantine routes; Avenue D proposed
fixed-rank compression but has no theorem to feed the compressed form
into. The missing back-end may be the Corvaja–Zannier subspace-theorem
gcd machinery: bounds of the shape
\(\gcd(2^a-1,3^b-1)\le\exp(\varepsilon\max(a,b))\)
(Bugeaud–Corvaja–Zannier), extended by Levin and others to gcds of
polynomial S-unit expressions with a *fixed* number of terms. These are
ineffective, but IEF-style qualitative exclusions already accept
ineffective inputs (IEF10 used Baker qualitatively).

### Target

Audit which open gates reduce, after a proved fixed-rank compression on a
named branch class, to statements of the form "large
\(v_2\)/\(v_3\)-proximity between two bounded-rank S-unit expressions
happens only finitely often". Candidates: the enemy-constant valuation
identity \(\tau(x_K)=v_2(3^{m_K}+d_K)-E_K-1\) on phases where \(d_K\)
compresses (valuation-one runs have the two-term closed form recorded in
Avenue D); merger/shell coincidence equalities on mechanical blocks.

### Order of operations

This task is *conditional on* an Avenue D compression lemma and should be
attempted only when a branch class with bounded-rank corrections is
actually proved. Its first deliverable is the audit only: a table of
gates × required gcd statement × whether current literature covers that
shape. No census.

### Falsifier / kill

Inherited from triage §11: kill any row where faithful encoding needs
unboundedly many terms or heights feeding back into the bound.

### Priority

Low-medium now; rises sharply if Avenue D lands a compression identity.

---

## W13 — Branching-walk calibration of the extremal law

> **DONE (session 8) — CALIBRATED; THE SUGGESTED LAW FAMILY WAS WRONG.**
> Deliverable: `docs/density-cycles/extremal_law_calibration.md`, script
> `scripts/explore_extremal_law_calibration.py`. **Record deficit:** not a
> branching-walk leftmost particle at all — \(\max_K D_K\) is the excursion
> height of one orbit above its own start, maximised over independent
> exponents, so the family is **Cramér--Lundberg, not Bramson**, with no
> logarithmic correction. The Lundberg equation \(z^{1-\log_23}=2-z\) has
> the **exact** root \(z=1/2\), so \(\gamma=\log2\) and
> \(P(\max D>u)\asymp2^{-u}\) — and that is forced by PCD7's budget
> identity, not fitted. Measured tail slope over 1000 orbits:
> \(-1.0103\). Record \(9.28\) vs \(\log_2 1000=9.97\). **Plateaus:**
> \(\ell_{\max}(m)\approx1+\log_2(m)/\bar\delta\) with
> \(\bar\delta=5+\beta=5.419\); reproduces every certified census point
> (\(m\le300\to2\); \(m\le1500\to3\); \(m\le8000\to3\)).
> **Answer to the stated question:** \(\Theta(\log m)\), constant
> \(0.1845\), **no** \(\log\log\) factor — and PCD10's \(o(m)\) target
> leaves an enormous margin, so \(O(\log m)\) is the right thing to attempt.
> Forward predictions: first length-4 plateau near \(m\approx7.8\times10^4\),
> none below \(2\times10^4\). \(n=471\)'s peak deficit \(4.23\) is
> typical, not anomalous — its six diffuse records are one deep excursion.
> **No ledger rows proposed:** exploratory by construction.

### Idea

COR1–COR3 computed the exact branching factor of the survivor tree. The
record-deficit extremes (\(D_K\) records, plateau records) are the
*leftmost-particle* statistics of an (inhomogeneous) branching random
walk, for which precise second-order laws exist (Biggins; Bramson's
logarithmic correction). Fit the prediction to the census data
(\(n\le5001\) records, the \(m=1200\) plateau failure, \(n=471\)): if the
Bramson-corrected law matches, it tells us the *true expected shape* of
the extremal growth that any exact rank function (Avenue F) or plateau
bound (W10/W11) must accommodate — e.g. whether the honest target is
\(O(\log m)\) or \(O(\log m\cdot\log\log m)\) plateaus.

### Honest framing

Pure prediction engine. Barrier 2 applies in full: nothing here
eliminates a cylinder. Its value is stopping Opus from attempting exact
lemmas with the wrong target exponent — a cheap way to avoid another
\(L=2\)-style refutation at \(m=1200\).

### First deliverable

One script + note: fitted extremal law vs census, with the implied
correct conjecture shapes for plateau growth and record-deficit growth.

### Priority

Low as mathematics, high as navigation; half a session.

---

## Considered and set aside (so Opus does not re-derive the triage)

- **Berg–Meinardus functional equations.** Analytic repackaging; no
  repunit-specific boundary datum identified that would constrain the
  solution space beyond the known equivalence. Revisit only with a
  concrete boundary condition in hand.
- **Wirsching predecessor density functions.** Genuine, but on this
  repo's structures it is the same move as W4 with weaker quantitative
  output; folded into W4.
- **2-adic conjugacy (parity-vector) recoordinatization.** The repo's
  cylinder/least-representative machinery already *is* the conjugacy in
  explicit coordinates; a re-derivation adds notation, not information.
- **Cyclotomic / Zsygmondy structure of \(3^n-1\).** Closed by triage §2;
  primitive-divisor data does not survive reduction to the affine
  identity.
- **Normality or Fourier-type results on digits of \(3^n\).** Open and
  hard independently of Collatz; enter only through W10's specific
  bounded-height bridge, never as a standalone target.
- **Undecidability of generalized Collatz (Conway).** Scope warning only:
  it says nothing about this specific map, and justifies no pessimism
  about structured subfamilies.

---

## Recommended order for Opus 5 sessions

| Session | Task | Reason |
|---|---|---|
| 1 | ~~W9~~ **done** | Proved inputs only; finished the Avenue A \(L=1\) Baker gates outright |
| 2 | ~~W2 (i)–(iv)~~ **done, closed** | Provable sub-results; the avenue is thin — absorbed into W4 |
| 3 | ~~W11 (i)–(iii)~~ **done, closed** | Not a compact-group extension; but it built W10's bridge |
| 4 | ~~W10~~ **done, closed** | Bridge built at \(c=1\); Stewart vacuous by \(2^{\Theta(E)}\) and anti-correlated |
| 5 | ~~W1.a + interaction ledger~~ **done, closed** | Closed the naive question exactly; the "real one" is a slope defect, not a ledger |
| 6 | ~~W8~~ **done, re-scoped, foreclosed** | Closed-form lanes for every alignment, but all onto known ghosts |
| 7 | ~~W6~~ **done** | Premise corrected; new finite no-go in the two-variable class |
| 8 | ~~W13~~ **done** | Lundberg not Bramson; plateau target is \(\Theta(\log m)\), constant \(0.1845\) |
| 9 | ~~W4~~ **done, closed** | Rail restriction is free; density can't reach an \(O(\log x)\) family at any exponent |
| 10 | ~~W5~~ **done** | Conditioning vacuous; wrong prime — \(f\) destroys 3-adically, creates 2-adically |
| 11 | ~~W7~~ **done** | Symbolic coordinates generic; IEF15+FIN1 is the binding one |
| 12 | ~~W3~~ **done, collapsed** | \(v_2(\Pi(n))=\tau(n)\): the two models are anti-correlated, not close |
| — | W12 | Dormant until Avenue D lands a compression identity |

Avenue A remains the maintained main line and is not displaced by this
portfolio; W4, W5, and W9 feed it directly. If forced to bet on where
"real progress" is most likely: W9 for a guaranteed finished lemma, and
W11 for the breakthrough-shaped outcome, because it is the only route on
either portfolio whose success mode is an individual-orbit theorem
rather than a density statement or a census.

## Global kill rules

Inherited unchanged from `outside_box_avenue_portfolio.md`: kill on
abstract-word-only applicability, virtual sources, bounded-depth modular
language, SH1/SH2/BND1-excluded potential shapes, or classification
presented as descent. Additionally for this file: any W1/W8 statement
whose "parts" do not each carry an actual computed trajectory is void
(barrier 4), and any W4/W5 density statement presented as eliminating an
individual cylinder is void (barrier 2).
