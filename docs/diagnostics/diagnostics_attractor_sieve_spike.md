# Diagnostics: motif attractor, ancestry reachability, spike recovery

**Building on:** `../fuse/binary_fuel_bad_block_notes.md`,
`../repunit/primitive_ancestry_lemma.md`, `../nested-anchor/near_threshold_episode_notes.md`

**Status:** exploratory diagnostics. Three finite/numeric experiments. None
proves a new universal claim. Each one sharpens, or redirects, an existing
proof target. Scripts:
`scripts/explore_fuel_motif_attractor.py`, `scripts/explore_ancestry_reachability.py`,
`scripts/explore_spike_recovery.py`.

---

## 1. The {A,B,C} motif attractor is negative but only weakly contracting

The cheap near-threshold motifs of `../fuse/binary_fuel_bad_block_notes.md` Section 3,

\[
A=(2,1,2),\qquad B=(2,1,3)(3,1,2),\qquad C=(2,1,4)(4,1,2),
\]

have inverse maps with contraction ratios and fixed points

| motif | inverse slope | inverse fixed point |
|---|---:|---:|
| \(A^{-1}\) | \(8/9\approx0.8889\) | \(-1.000000\) |
| \(B^{-1}\) | \(128/243\approx0.5267\) | \(-0.373913\) |
| \(C^{-1}\) | \(256/729\approx0.3512\) | \(-0.238901\) |

A Monte-Carlo sweep over depth-80 backward words boxes the attractor at

\[
[-0.793133,\ -0.238901]\subset(-\infty,0),
\qquad
\operatorname{dist}(\text{attractor},0)\approx0.2389.
\]

So the negative-ghost picture for the reduced alphabet is robust: the whole
attractor sits a fixed distance below zero.

**Caveat that this exposes.** The largest contraction ratio is \(8/9\), from
the nearly neutral motif \(A\) (block surplus only \(-\log_2(3/2)+1\approx
-0.17\) bits). Hence \( \text{maxslope}^{N}\) decays slowly
(\(\approx8\times10^{-5}\) only at \(N=80\)). The real-topology contraction
therefore gives an exponential but *very weak* lower bound on the terminal
tail of a positive \(N\)-block shadow. It cannot by itself bound shadow
length, which is consistent with the beam search finding long \(A\)-dominated
examples. The usable size pressure must come from the 2-adic gate (the
Baker/Yu route already used in `../repunit/repunit_baker_nonshadowing.md`), not from the
Archimedean contraction.

Reproduce: `python scripts/explore_fuel_motif_attractor.py`.

---

## 2. The q=2 smallest-shell partner is generically unreachable at long source length

For the smallest-shell (\(q=2\)) reachability condition of
`../repunit/primitive_ancestry_lemma.md`, write a source valuation word of length \(i\)
and total \(u\), and a high prefix of length \(j\) and total \(u\). The
necessary congruence is \(A_i\equiv C\pmod{3^r}\) with
\(C=3A_j+2^{u+2}\).

### Sieve density (necessary condition)

Monte-Carlo over \(u=24,\ j=4,\ i=9\), \(3\times10^5\) samples:

| \(r\) | survivor fraction | ratio vs. previous level |
|---:|---:|---:|
| 1 | 0.602650 | 0.6027 |
| 2 | 0.180910 | 0.3002 |
| 3 | 0.060270 | 0.3331 |
| 4 | 0.020180 | 0.3348 |
| 5 | 0.006717 | 0.3328 |
| 6 | 0.002270 | 0.3380 |
| 7 | 0.000777 | 0.3421 |
| 8 | 0.000270 | 0.3476 |

The first level keeps \(0.60\) (the \(\ell\)-odd bias of Section 11); every
later lift prunes by a near-uniform factor \(\approx1/3\). The sieve keeps
shrinking geometrically and does **not** plateau, but \(3^{-r}\) does not
outrun the growth in candidate source words, so the congruence sieve alone
cannot decide reachability.

### Exact reachability (exhaustive, small \(u\))

Counting true \(A_i=C\) solutions exhaustively for \(8\le u\le18\):

- the number of reachable pairs stays \(O(1)\)–\(O(\text{tens})\) even as the
  total pair count grows past \(10^7\); the reach rate falls from
  \(\sim4\times10^{-3}\) at \(u=8\) to \(\sim3\times10^{-7}\) at \(u=18\);
- reachable solutions concentrate at the **shortest** admissible source
  length \(i=j+2\);
- every longer source length tested (the low-valuation-tail regime, i.e. the
  deep primitive-deficit regime) yields **zero** reachable partners.

This is the structurally useful outcome. At a deep record deficit the source
word that could realise the smallest-shell partner would have to be long with
a low-valuation tail, and in that regime the partner is essentially never
reachable. Non-reachability at long \(i\) is therefore the lever for
Sublemma A: it forces the argument into the long-low-valuation-source branch,
which is exactly where an ordinary positive-integer size bound can act.

**Caveats.** The mod-\(3^r\) test is necessary, not sufficient; the exact
pass omits the exponent-prefix congruences for \(m=d-i\); it is exhaustive
only over \(8\le u\le18\).

Reproduce: `python scripts/explore_ancestry_reachability.py`.

---

## 3. The Mersenne-spike recovery coincidence survives to R = 999

For \(R\equiv5\pmod6\), the spike start
\(x_0=4(2^{R+1}-1)/9-1\) recharges to \(x_1=2^R-1\). Testing on exact
integer orbits whether first descent below \(x_0\) coincides with the first
nonnegative cumulative fuel-block surplus:

- range \(5\le R\le999\), 166 values;
- **0 mismatches**;
- worst recovery length 696 blocks.

This extends the original \(R\le299\) check by roughly threefold with no
exception. The proof target is now sharp:

> In the exact Mersenne-spike family, once the cumulative block surplus
> \(\sum\Delta\) first reaches \(0\), the finite-size correction \(\sum
> \varepsilon\) can no longer keep the orbit above \(x_0\); hence first
> nonnegative surplus implies descent.

The note `../fuse/binary_fuel_bad_block_notes.md` already bounds
\(\varepsilon(x)\le 4/((x+1)\ln2)\), and the spike starts have
\(x_0\asymp2^R\), so the correction is exponentially small from the first
block. Turning the empirical coincidence into a lemma is a matter of showing
the surplus increment at the crossing block exceeds that tiny correction
budget.

**Caveat.** Finite certificate to \(R=999\); floats used only for the
surplus diagnostic, orbits are exact integers.

Reproduce: `python scripts/explore_spike_recovery.py`.
