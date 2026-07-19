# Outside-the-Box Avenue Portfolio

**Status:** Research backlog. Not a claim chain. None of these routes is
promoted to `CLAIM_LEDGER.md` until it produces an exact lemma with a
falsifier and a verifier.

**Purpose.** Existing maintained routes have either closed, demoted, or
narrowed to one live restart (the unrestricted actual-source transfer fan
and its storage-dominance lemma). This note records *different* proof
architectures worth attempting later, one at a time. It deliberately avoids
reopening routes already falsified in
`outside_box_avenue_triage.md`, the residual-atlas demotion, NSF demotion,
or the transversality audit, unless a restart condition is stated.

**Operating rules.**

1. One avenue at a time; finish its first exact test before opening another.
2. Every avenue must end in **descent below \(M_n\)** or **strictly smaller
   exponent merge / inductive transfer**. Classification alone is not a win.
3. Finite censuses are allowed only to falsify or to certify a named finite
   domain. They do not promote a universal claim.
4. Do not invent a new language cover of blocked-diffuse seeds unless the
   cover lemma is proved first (atlas demote-1).
5. Virtual or approximate collisions are forbidden; comparisons must involve
   an *actual* smaller-odd-repunit trajectory or an actual discharged basin.

## Relation to live work

| Already live / queued | Do not duplicate as “new” |
|---|---|
| Full actual-source transfer fan + storage-dominance | Avenue A below *extends* this, not replaces it |
| PCD amortized charging / carry–endpoint non-shadowing | Keep in `next_generation_attack_program.md` |
| IEF theorems inside \(\mathcal L_{3/4}\) | Classification only after demote-1 |
| Cycle ledger CYC1–CYC4 | Separate track |

---

## Avenue A — Comparison dynamics as the primary object

### Idea

Stop treating mergers and transfers as rare accidents discovered after a
valuation word is built. Make the *comparison process* between \(a_n\) and
actual smaller \(a_m\) the fundamental dynamical system. Descent of \(a_n\)
is then a statement about when the comparison process hits a transfer
inequality or a state equality.

### Exact objects

For even gaps \(g\ge2\) and times \(s\ge g\), define the same-diagonal pair

\[
\bigl(x_{s-g}(n),\; x_s(n-g)\bigr)
\]

and the transfer defect

\[
\Delta_g(n,s)
=
2^g x_s(n-g)+(2^g-1)-x_{s-g}(n).
\]

Descent transfers when \(\Delta_g(n,s)\ge0\) at a time when
\(x_s(n-g)<M_{n-g}\). Merger occurs when the states are equal.

Also keep the already-observed storage-surplus difference

\[
H_g=(E_s(n-g)-s)-(E_{s-g}(n)-(s-g))
\]

from the full-fan restart note.

### Target lemmas (in order)

1. **Storage-dominance.** Through first descent of every odd \(n\), every
   compared same-diagonal state satisfies \(0<R_i(n)<3^{n+i}\). (This is the
   live restart target; prove or falsify first.)
2. **Sign law.** Storage-dominance \(\Rightarrow\) \(\operatorname{sign} H_g\)
   agrees with \(\operatorname{sign}\Delta_g\) except on an explicitly
   classified affine-correction equality set.
3. **Schedule lemma.** Every primitive \(n\) admits an actual schedule
   \((g_k,s_k)\) of comparisons whose defects are monotone in a
   well-founded rank until a transfer or merge occurs.
4. **Hard-seed discharge.** The schedule discharges \(n=471\) by an
   explicit finite certificate that generalizes.

### Why this is outside the prior boxes

Earlier work mined mergers or tested a *bounded* gap fan. This avenue treats
the infinite family of actual comparisons as the system to be proved
contractive, rather than as a post-hoc certificate search.

### First falsifier

A primitive \(n\) whose every same-diagonal comparison with every smaller odd
\(m<n\) stays strictly negative until after \(n\) itself has already
descended, *and* for which no independent merge exists. If such an \(n\)
appears inside a computationally closed initial segment, the schedule idea
fails as a cover.

### Cost / tools

Exact diagonal algebra already in REPMRG/GAPMRG; full-fan explorer
`scripts/explore_repunit_full_descent_transfer_fan.py`; new proof work on
storage dominance.

### Priority

**Highest.** It is the only avenue that already meets the triage restart
condition.

### Progress (2026-07-19)

Working note: [`avenue_a_comparison_dynamics.md`](avenue_a_comparison_dynamics.md).

- SD1 stated; \(\theta\)/\(\phi\)/affine equivalences proved.
- Descent cannot occur on \(e=1\); \(\phi<2\) (SD½) implies SD1.
- Conditional theorem: \(\theta\le5/27\) and descent landing \(\ge3\)
  \(\Rightarrow\) SD1. The case \(n=3\) is settled by hand.
- Deficit dictionary: \(d=(3^n-1)\rho\), \(P=2\cdot3^i(d-d_0)\).
- Affine bridge: \(K_\downarrow\le T\) and landing \(\ge3\) \(\Rightarrow\) SD½
  \(\Rightarrow\) SD1 (uses the proved affine-tail bound + SD-T-budget).
- Descent to \(1\) impossible after a pure \(e=1\) prefix (\(P=0\)).
- Finite: SD1 through \(5001\); \(K_\downarrow\le T\) through \(511\);
  SD½ / no descent-to-\(1\) through \(4001\); empirical \(K_\downarrow=O(n)\).
- Open gates: prove \(K_\downarrow\le T\); exclude descent-to-\(1\) for \(P>0\).

---

## Avenue B — Heterogeneous portfolio with an explicit exotic class

### Idea

The atlas failed because it assumed eventual entry into \(\mathcal L_{3/4}\).
Keep the portfolio lemma, but *name* a complementary class \(\mathcal E\) of
mixed-alphabet primitive seeds (prototype \(n=471\)) and demand a separate
discharge rule for \(\mathcal E\), not a language cover of \(\mathcal B\).

### Exact objects

Partition odd exponents into:

- \(\mathcal M\): merge before first descent (inductive);
- \(\mathcal D\): direct descent with no prior merge;
- \(\mathcal P_{\mathrm{bal}}\): primitive with a long balanced \(q=3\)
  blocked phase (atlas classification may apply *inside* this class only);
- \(\mathcal E\): primitive residuals whose payout alphabet is not eventually
  mechanical \(3/4\).

The cover claim is

\[
\{\text{odd }n>1\}=\mathcal M\cup\mathcal D\cup\mathcal P_{\mathrm{bal}}\cup\mathcal E,
\]

with each class carrying its own discharge implication. No claim that
\(\mathcal E=\emptyset\) a priori.

### Target lemmas

1. **Partition theorem.** Every odd \(n\) falls into exactly one of the four
   classes under an explicit, checkable definition (not a soft “looks
   balanced” predicate).
2. **Exotic normal form.** Every seed in \(\mathcal E\) admits a finite list
   of payout motifs / storage phases with exact transition rules (the
   earlier \(\mathcal E_{\mathrm{mix}}\) attempt failed; any new form must
   survive the full 732-step \(n=471\) descent).
3. **Exotic discharge.** A rule that sends every \(\mathcal E\) seed to
   either \(M_n\)-descent or a smaller merge/transfer, possibly by Avenue A.

### Why not a reopened atlas

Atlas demote-1 forbids presenting emptiness of \(\mathcal R\subset
\mathcal L_{3/4}\) as descent. This avenue *accepts* that failure and makes
the exotic class a first-class inductive case.

### First falsifier

An infinite constructive family of primitives that escape every proposed
exotic normal form while remaining outside \(\mathcal M\cup\mathcal D\).

### Priority

**High**, but only after Avenue A’s storage-dominance lemma is settled:
\(\mathcal E\) may simply be “seeds for which the comparison schedule is
long.”

---

## Avenue C — Basin certificates from the FIN1 range

### Idea

Work backward from the finite discharged set \(\{x\text{ odd}:x\le10^6\}\)
(FIN1), not forward from repunit ancestry. A dangerous repunit prefix is
discharged when an explicit finite backward tree from that prefix is forced
to hit the FIN1 basin (or a previously discharged repunit tail).

### Exact objects

Accelerated inverse branches of \(f\): for each odd \(y\) and each
\(e\ge1\) with \(2^e y\equiv1\pmod3\),

\[
x=\frac{2^e y-1}{3}
\]

is an odd preimage. A *basin certificate* for \(a_n\) is a finite labeled
tree of such branches ending in nodes already known to descend below their
own Mersenne thresholds or below \(10^6\).

### Target lemmas

1. **Certificate soundness.** Any such tree implies \(P(n)\).
2. **Uniform depth bound or rank.** Certificate depth is controlled by
   bit-length or by record deficit, so the search is not an unbounded
   open-ended crawl.
3. **Primitive completeness.** Every primitive residual admits a
   certificate; merged cases inherit by induction.

### Why this differs from NSF / GPA ancestry

Shell-fan ancestry seeks a *smaller repunit* source with equal correction.
Basin certificates allow arbitrary odd preimages that are already
discharged, not only aligned repunit diagonals. The classical predecessor
tree is used as a *certificate language*, with FIN1 as the leaf set.

### Hard constraints from triage

Applegate–Lagarias / Wirsching / Kontorovich–Lagarias already describe these
trees. The repository-specific content must be a *repunit-aligned or
storage-aligned pruning* that terminates. Without a termination lemma, this
is the classical open Collatz tree in new clothing.

### First falsifier

A primitive prefix whose every pruned backward search either (i) exceeds the
proposed depth bound without hitting a discharged leaf, or (ii) only hits
leaves that are not yet discharged without circularity.

### Priority

**Medium.** Powerful if a termination lemma appears; otherwise a known open
problem restated.

---

## Avenue D — Fixed-dimension Diophantine packaging

### Idea

Standard Baker / \(S\)-unit / dynamical Mordell–Lang tools failed because
the number of summands or the height grew with the counterexample. Repackage
the correction identity so that the number of free multiplicative variables
is bounded independently of \(n\).

### Exact objects

The correction

\[
A_K=\sum_{t<K}3^{K-1-t}2^{E_t+1}-3^K
\]

has \(K\) summands. Seek an equivalent form with a fixed number of
\(S\)-units, for example by grouping into mechanical blocks, generating
functions, or closed forms along valuation-one runs:

\[
A_{K+L}=3^L A_K+\text{(explicit two-term run contribution)}.
\]

A candidate equation might involve only \((3^{m},2^{E},d_{\mathrm{enemy}},R)\)
with bounded arity.

### Target lemmas

1. **Compression identity.** On every record-extremal or exotic phase, the
   correction equals an expression in at most \(r_0\) multiplicative
   variables for a universal \(r_0\).
2. **Effective non-shadowing.** Apply a fixed-rank \(S\)-unit or linear-form
   bound to force a merge, transfer, or surplus violation.

### Why triage does not already kill this

The triage killed *generic* variable-dimension encodings. It did not kill a
proved compression that is valid on the residual class actually remaining
after Avenue A/B filters.

### First falsifier

A residual family on which any faithful correction encoding still requires
unboundedly many independent summands (or heights \(\asymp E_K\) feeding
back into the same bound).

### Priority

**Medium.** Attempt only after the residual class is named and thin.

---

## Avenue E — Shadow-factory forcing (positive use of expanding cycles)

### Idea

SH1 uses the expanding cycle \(-5\leftrightarrow-7\) as a *no-go factory*
for potentials. Use the same expanding rational cycles as a *forcing
factory*: every sufficiently dangerous positive integer near a shadow
residue is forced into a known descending or merging corridor.

### Exact objects

For an expanding cycle of odd length \(K\) with \(2^E<3^K\), the shadow
residues \(x\equiv c\pmod{2^N}\) have controlled local itineraries. Define
a *forcing window* in which either:

- the trajectory enters the FIN1 range, or
- it meets an actual smaller repunit / discharged seed, or
- it violates primitivity by hitting a shell equality.

### Target lemmas

1. **Local forcing.** Inside each shadow cylinder of depth \(N\ge N_0\),
   one of the three outcomes occurs within \(K\) odd steps.
2. **Coverage of residuals.** Every residual primitive (Avenue B) eventually
   enters some forcing cylinder, or is discharged by another rule.

### Why this is not a resurrected local potential

No global Lyapunov function is claimed. The output is a finite case split
inside arithmetic progressions, in the spirit of residue corridors but using
expanding-cycle geometry rather than surplus-budget trees alone.

### First falsifier

A primitive residue class that shadows an expanding cycle for arbitrarily
large \(N\) without entering a discharged basin (compatible with SH1’s
existence of shadows, so the lemma must use *extra* repunit or storage
structure).

### Priority

**Medium–low** until a residual class is known to prefer shadow residues.

---

## Avenue F — Rank by primitive record height, not by \(n\)

### Idea

Change the induction parameter. Instead of inducting on the odd exponent
\(n\), induct on a well-founded rank derived from the primitive record
ledger \((D_K,N_B,Z_K,\ldots)\). Prove there is no infinite ascending chain
of primitive record states; every chain either descends below its Mersenne
target or merges to a lower rank.

### Exact objects

A candidate rank on pre-descent states of primitive tails, for example

\[
\rho=\bigl(\lceil D_K\rceil,\; N_B,\; \operatorname{bitlen}(n)-E_K\bigr)
\]

in lexicographic order, or a single integer combining storage and deficit.
The key is that every residual step either decreases \(\rho\) or triggers a
known discharge rule.

### Target lemmas

1. **Rank drop on residual steps.** On any step that is not already a
   descent or merge, \(\rho\) falls.
2. **No infinite residual chain.** Immediate from well-foundedness.
3. **Translation to \(P(n)\).** Finite residual chains imply eventual
   descent or merge for every odd \(n\).

### Hard constraint

PCD8 / balanced mechanical words produce arbitrarily large record deficits
abstractly. Any viable rank must use *repunit-cylinder* or *least
representative* information so that abstract words do not lift to infinite
ascending chains of actual seeds. Without that, this is another language
argument.

### First falsifier

An explicit infinite sequence of actual odd exponents whose primitive record
ranks are nondecreasing before descent.

### Priority

**Medium.** Attractive as architecture; dangerous as a restatement of the
open plateau / least-representative problem.

---

## Avenue G — Pairwise meeting for repunits (relative Collatz)

### Idea

Weaken the goal from “\(a_n\) falls below \(M_n\)” to “for every odd
\(n>m\ge m_0\), the trajectories of \(a_n\) and \(a_m\) meet or satisfy a
transfer inequality on a controlled schedule.” Strong induction plus FIN1
then upgrades relative meeting to absolute descent.

### Exact objects

Meeting time \(\tau(n,m)=\min\{i:x_i(n)=x_{i-(n-m)}(m)\}\) when defined on
a common diagonal, or transfer time for \(\Delta_{n-m}\).

### Target lemmas

1. **Eventual meeting or transfer** for all odd pairs with \(n-m\) in a
   fixed arithmetic progression (start with gap 2, then all even gaps).
2. **Uniform lag bound** in terms of \(\max(n,D_K)\).
3. **Upgrade lemma:** relative control + FIN1 \(\Rightarrow\) every
   \(P(n)\).

### Relation to Avenue A

This is Avenue A specialized to a *universal pairwise* statement rather than
an existential schedule. It may be harder, but the theorem statement is
cleaner.

### First falsifier

A pair of odd exponents that remain unequal and transfer-negative on the
entire pre-descent window of the larger exponent.

### Priority

**High as a theorem shape; execute as a specialization of Avenue A.**

---

## Avenue H — Automatic / morphic residual words

### Idea

Almost-all and corridor-rate theorems leave a thin exceptional set. Assume
the valuation words of primitive residuals are automatic, morphic, or
otherwise finitely generated, then classify them by existing automata
methods and discharge each class.

### Exact objects

A conjecture of the form: the payout word of every primitive residual is
generated by a morphism of rank \(\le r\) (or a finite transducer from a
Sturmian or Toeplitz base). Then apply IEF-style periodic-prefix discharge
or Avenue A schedules class by class.

### Target lemmas

1. **Structure theorem** for residual words (the hard step).
2. **Class discharge** for each generator.
3. **No other residuals.**

### Why triage is hostile

Entropy / complexity without incidence was closed. This avenue is viable
only if the structure theorem is *forced* by primitivity + storage
identities, not assumed from finite data.

### First falsifier

A primitive residual whose payout word has factor complexity incompatible
with the proposed automatic class (already plausible for \(n=471\)).

### Priority

**Low** until a forcing structure theorem exists. Useful as a
classification side project, not as a descent bet.

---

## Avenue I — Adelic / height packaging (speculative)

### Idea

Encode the pre-descent state by an adelic height that couples Archimedean
size, \(2\)-adic valuation storage, and \(3\)-adic correction residues. Seek
a height inequality that decreases on residual steps for actual repunit
seeds (not for abstract words).

### Exact objects

A height \(H(x;n)\) on pairs (state, exponent) such that:

- \(H\) is bounded below on pre-descent states;
- each residual odd step decreases \(H\) by a definite amount;
- descent or merge occurs when \(H\) crosses an explicit threshold.

### Hard constraints from SH1 / BND1 / NLP

Any height of the form \(\log_2 x+G\) with \(G\) bounded, or with \(G\)
depending on a finite local coordinate list, is already impossible as a
*global* one-step potential. The avenue must use the exponent \(n\) (or
cylinder data) as a genuine second variable, and must not claim one-step
decrease for all odd \(x\).

### First falsifier

A one-parameter family of actual seeds on which every proposed adelic height
increases through a residual record phase (e.g. the blocked-diffuse phase of
\(n=471\)).

### Priority

**Low.** Documented so it is not rediscovered naively; attempt only with a
precise height formula and an immediate \(n=471\) stress test.

---

## Avenue J — Derandomized certificate covering

### Idea

Finite data suggest that merge/transfer certificates are abundant. Formulate
a probabilistic method on exponent cylinders: a random smaller gap / time
hits a transfer inequality with positive density, then derandomize using
discrepancy or pigeonhole arguments to an explicit certificate.

### Exact objects

For each odd \(n\), a finite set of probes
\(\{(g,s)\}\) with a measure \(\mu_n\). Show

\[
\mu_n\{\Delta_g(n,s)\ge0\text{ and }x_s(n-g)<M_{n-g}\}>0,
\]

then extract an explicit successful probe.

### Hard constraints

Density-one statements do not eliminate exceptional cylinders (rail-5
survivor warning). Derandomization must produce a certificate for *every*
\(n\), including exotic seeds.

### First falsifier

A cylinder on which every probe in the proposed finite probe set fails,
while the seed remains primitive through the probe horizon.

### Priority

**Low–medium.** Best used as a discovery tool feeding Avenue A, not as a
standalone existence proof.

---

## Avenue K — Change the spine target

### Idea

The repository concentrates on the Mersenne–repunit spine because of the
tower/burn reductions. Temporarily change the primary open target to a
different complete residue system or complete induction scaffold—for
example, all odd \(x\equiv\pm1\pmod{2^m}\) for increasing \(m\), or all
rail-7 escapees—where comparison dynamics might be easier, then transfer
back to repunits.

### Exact objects

A family \(\{S_m\}\) of odd sets with:

- \(\bigcup_m S_m=\{\text{odd positives}\}\) or a set whose descent implies
  Collatz;
- each \(S_m\) closed under an inductive discharge rule;
- repunit seeds appear inside some \(S_m\) with controlled parameters.

### Risk

This can become a full Collatz rephrasing with no gain. Accept only if the
new scaffold has a *simpler comparison identity* than the repunit diagonal.

### First falsifier

No scaffold found whose comparison algebra is strictly simpler than
same-diagonal transfer on repunits after a bounded search of natural
candidates (rails, Mersenne, near-Mersenne, Andaloro companions).

### Priority

**Low** as a main bet; **useful** as a one-week exploratory spike with a
hard stop.

---

## Recommended working order

| Order | Avenue | First concrete deliverable |
|---|---|---|
| 1 | A | Prove or falsify first-descent storage-dominance |
| 2 | G | Specialize A to gap-2 / all-even-gap pairwise statements |
| 3 | B | Define a checkable partition including \(\mathcal E\) |
| 4 | C | One explicit basin-certificate schema with depth bound |
| 5 | D | Compression identity on the remaining residual class |
| 6 | F | Candidate rank function stress-tested on \(n=471\) |
| 7 | E, J, H, I, K | Only after 1–6 produce a named thin residual |

## Restart / kill criteria (global)

**Kill an avenue immediately if** its first exact lemma:

- applies only to abstract valuation words without forcing actual seeds; or
- uses virtual sources whose moduli belong to a different word; or
- reduces to a bounded-depth modular language (bounded-depth closure); or
- claims a global one-step potential already excluded by SH1/SH2/BND1; or
- presents emptiness of a subclass of \(\mathcal L_{3/4}\) as full descent.

**Keep an avenue if** it produces either:

- a new exact identity coupling two *actual* trajectories; or
- a well-founded rank that decreases on residual steps of actual seeds; or
- a finite explicit certificate schema that covers a named infinite class.

## Suggested first session when we “get to work”

Open Avenue A only:

1. Write the storage-dominance statement as a lemma with explicit quantifiers.
2. Check it against the full-fan explorer through the existing finite domain.
3. Attempt a human proof from the exact normal form
   \(R_K=A_K+2^{E_K+1}\); identify the first missing inequality.
4. If proved, move to the schedule lemma; if falsified, record the
   counterexample and skip to Avenue B’s exotic partition using that seed.
