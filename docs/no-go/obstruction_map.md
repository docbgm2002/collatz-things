# Obstruction Map for the Repunit-Tail Programme

**Status:** Consolidation. This note proves nothing new. Every closure below
is stated and proved in the note cited beside it; this file exists so that the
combined force of the closures is visible in one place, which it currently is
not.
**License:** CC-BY 4.0

---

## 1. The target

The residual after the proved reduction (MER1, MER2, SPN1) is:

> **T.** For \(a_n=(3^n-1)/2\) with \(n\) odd, the orbit of \(a_n\) falls
> below \(2^n-1\) within \(\sigma(a_n)\le Cn\) odd-steps.

`RESEARCH_ROADMAP.md` sets \(C=3\) as Priority 1. Nothing below refutes **T**.
What follows records five closed *routes to* **T** and one unsupported
counting route, with their precise limitations.

---

## 2. Five closures and one unsupported route

| # | Route | Obstruction / status | Where |
|---|---|---|---|
| 1 | Fixed local block floor (256-Block Floor) | Explicit exponent class with 256-block weight 257, no prior descent, no equal-diagonal collision | `docs/repunit/repunit_low_prefix_obstruction.md` §§3-4, 9 |
| 2 | Variable-window recovery depending only on the observed finite deficit | Corollary 5: the low run extends past any prescribed finite horizon | `docs/repunit/repunit_low_prefix_obstruction.md` §7 |
| 3 | Kolmogorov / description-complexity argument | A residue mod an enormous power of two can have a very short description ("the discrete-log residue associated with \((2,1^{K-1})\)") | `docs/repunit/repunit_low_prefix_obstruction.md` §10 |
| 4 | Generic Baker / \(p\)-adic logarithmic forms | The height gate: the fixed-\(d=7\) cancellation is special; generic \(d_K\) has bit-length comparable to \(E_K\), so a variable-\(d\) bound feeds the unknown valuation mass back into its own upper bound | `docs/repunit/repunit_baker_nonshadowing.md` §6 |
| 5 | Any argument local to a valuation-one run | EXR1: the storage/accumulation exchange rate is exactly one, so \(D_K-\log_2Z_K\) is conserved | `docs/no-go/storage_exchange_rate.md` |
| 6 | The proposed escape-set counting route | Unsupported: FUEL1 puts a full positive-integer residue class in \(E_a\), but LUN2 bounds only homogeneous multiplier products and supplies no global density bound for \(E_a\) | `docs/no-go/macro_step_lundberg.md` §6 |

Closures 1-3 all descend from a single object: the nested exponent classes
converging \(2\)-adically to the ghost solution of \(3^{\alpha+1}=-7\).
Closure 5 explains *why* that object is so hard to charge against — it
generates long valuation-one runs, and by EXR1 nothing local can be charged
against them.

Item 6 involves the same residue-freezing that drives closures 1-3 and
`no_local_potential.md` §1. Sufficient trailing-one fuel forces escape, and
fuel is a low-bit congruence. Thus \(E_a\) contains every positive odd integer
in the class \(x\equiv-1\pmod{2^{t_a}}\), where
\(t_a=\lceil a/\alpha\rceil+1\) and \(\alpha=\log_2(3/2)\). This gives a
finite-domain Walsh lower bound in terms of the observed escape fraction. An asymptotic
white-noise obstruction follows only if those fractions stay bounded away
from one. The cylinder inclusion alone does not establish the formerly
claimed \(2^a\) overrepresentation or refute all counting routes.

> **Correction history.** `macro_step_lundberg.md` first reported finite
> computational evidence for DISC1/WALSH1, then declared both refuted using
> the purported true-orbit escape bound \(\mu(E_a)\le2^{-a}\). That bound
> does not follow from LUN2: the multiplier product omits the positive affine
> corrections. The finite computations remain observations, while the
> all-modulus refutation and WALSH1's claimed \(C=1\) consequence are
> withdrawn. See `CLAIM_LEDGER.md` for the corrected statuses.

---

## 3. The one thing that did close

The ghost branch itself is dead, and this is the programme's real result.

**BAKER1-3.** A tail has prefix \((2,1^{K-1})\) **iff**
\(v_2(3^{n+1}+7)\ge K+3\). By the fixed-\(d\) consequence of Yu's \(p\)-adic
logarithmic-form estimates, \(K+3\le C_7\log(n+1)\), so \(K=O(\log n)\).
Hence the explicit enemy branch cannot shadow for a window linear in \(n\),
and **does not threaten T**.

The tension is worth stating explicitly, because it is easy to misread the
two results as contradictory:

> The \((2,1^{*})\) branch **defeats any fixed local block floor** (closure 1)
> while **posing no threat to the \(3n\) window** (BAKER3). The exponents that
> realise a deep prefix exist, but Yu forces them to be astronomically large —
> beyond any computational reach, and beyond the window in which they would
> need to persist.

A consequence that should not be overlooked: **the falsity of the 256-Block
Floor is not computationally certifiable.** Any counterexample lives at height
\(\ge\exp(259/C_7)\). Finite verification of the floor (REP256-2, 1.7M blocks,
minimum exactly 425) is therefore not weak evidence — it is evidence from a
range where the obstruction provably cannot appear.

---

## 4. What remains open

Ruled out above: local block floors, finite-horizon recovery, complexity
arguments, generic Baker, local valuation-one arguments. What survives:

1. **Off-diagonal merger.** A merger theorem beyond equality of full diagonal
   states. All 4783 observed mergers through \(n\le10001\) have equal full
   diagonal states (REPMRG3), so this would be a genuinely new mechanism, not
   an extension of the observed one.
2. **Global non-shadowing.** A theorem that a positive integer exponent cannot
   follow *any* low-valuation \(2\)-adic branch for a window linear in the
   exponent. BAKER1-3 is the \(d=7\) instance; the general case needs the
   low-height family classification of BAKER-GEN.
3. **Primitive ancestry-amortization.** The target at the end of
   `docs/repunit/repunit_extremal_principle.md` §9. EXR1 shows this historical
   framing is not merely convenient but forced.

Routes 2 and 3 are the same problem seen from two sides: both need to charge
present deficit against something the local data does not contain.

### 4.3 An untested input to route 3

`macro_step_lundberg.md` §5 (ANC1 and its corollary) gives a capacity bound on
the reverse tree: for odd \(z\) with \(3\nmid z\), consecutive odd preimages
differ by a factor \(>4\), so at most \(\lceil n/2\rceil\) of them have
bit-length \(\le n\).

This is the right *type* of object for route 3 — a non-local resource
constraint, capping how much ancestry can be spent per bit of height, which is
exactly what EXR1 says local data cannot supply. Whether the cap is tight
enough to charge against the repunit deficit has **not been tested**, and the
bound's novelty is doubtful (the preimage family and reverse-tree growth rates
are standard; see Applegate–Lagarias). Recorded here because it is the only
identified bridge between the macro-step programme and a live open item, not
because it is expected to work.

---

## 5. Assessment

The programme has produced one theorem (BAKER1-3), five closures, an
unsupported counting route, and no unconditional progress on **T**. The
closures are the more valuable output:
they are permanent, they are cheap to state, and they redirect effort. But
they also mean the repunit-tail route is not a short path to **T**, and the
no-go / manuscript track should not be held for it.

The honest summary for a reader: *the natural local mechanisms have been
enumerated and eliminated; what remains requires either a new merger theorem
or a Diophantine input strictly stronger than the fixed-\(d\) case of Yu.*

---

## 6. Dependencies

No new claims. Cites REPLOW1-4, BAKER1-3, REPMRG1-3, REP256-1-2, REPEXT1-5,
EXR1, GAPMRG1, FUEL1, ANC1, ANC1-CAP. All statuses as recorded in
`CLAIM_LEDGER.md`.
