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

## 2. The q=2 smallest-shell partner is sparse in the tested correction layers

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

### Exact correction matches (exhaustive, small \(u\))

Counting true \(A_i=C\) solutions exhaustively for \(8\le u\le18\):

- the number of correction matches stays \(O(1)\)–\(O(\text{tens})\) in each
  tested layer even as the pair count grows past \(10^7\); nonzero layer rates
  range from roughly \(10^{-3}\) at \(u=8\) down to the \(10^{-6}\)–\(10^{-7}\)
  scale at \(u=18\), without monotonicity across source lengths;
- matches are sparse but do **not** occur only at the shortest admissible
  length. At \(u=18\), for example, matches occur at \(i=9\) for \(j=2\),
  \(i=12\) for \(j=3\), and \(i=11\) for \(j=4\);
- the deepest tested layers are empty, but the threshold moves with \(u\).
  The finite data therefore does not support a fixed bounded source-depth or
  a universal “all longer lengths are empty” claim.

The correct structural conclusion comes from the interval bounds in
`../repunit/primitive_ancestry_lemma.md`, not from an apparent finite cutoff.
They force every exact match into a source-length window of critical-density
scale \(i\lesssim u/\log_2 3+O(j)\). Thus the remaining source words are not an
arbitrary long all-ones regime; they lie near the same valuation corridor as
the original descent problem.

**Caveats.** The mod-\(3^r\) test is necessary, not sufficient. The exact pass
enumerates abstract high words as well as source words and is exhaustive only
over \(8\le u\le18\). For a high word actually realised by an odd repunit
exponent, Section 9A of `../repunit/primitive_ancestry_lemma.md` now proves
that an exact correction match at an admissible positive source index is
already sufficient for reachability; there are no further source-prefix
congruences.

### Least representatives of nonmatching cylinders

The same exact pass computes the least positive odd exponent representative
(n_0\pmod{2^{u+2}}) for every realised high word and separates words with
and without any admissible correction match. Nonmembership alone does not
force a growing least representative:

| \(u\) | \(j\) | realised high words | matched | least \(n_0\) among nonmatches |
|---:|---:|---:|---:|---:|
| 8 | 4 | 20 | 1 | 1 |
| 12 | 3 | 45 | 2 | 9 |
| 14 | 4 | 220 | 18 | 9 |
| 18 | 4 | 560 | 50 | 777 |

Median nonmatching representatives grow rapidly in this finite census, but a
universal theorem must control the minimum. REPANC3 explains the obstruction:
nonmembership is constant across the already-fixed exponent cylinder and does
not create a narrower congruence. Consequently the open lower-bound lemma must
use its full extra hypotheses—primitivity, record deficit, and payout
dominance—or it is false as a statement about arbitrary realised high words.

Reproduce: `python scripts/explore_ancestry_reachability.py`.

### Full-hypothesis primitive filter

`explore_primitive_q2_correlation.py` repeats the least-representative test on
the finite merger census after retaining only strict record-deficit prefixes
on tails labelled primitive and only their largest historical payout when it
has valuation two. At \(D_K\ge2\), there are five distinct dominant payout
ancestors through exponent \(2001\):

| ancestor | \((j,u)\) | dangerous record times | admissible lengths | correction matches | payout-cylinder \(n_0\) |
|---:|---:|---:|---:|---:|---:|
| 17 | (1,2) | 11, 12 | none | none | 1 |
| 173 | (0,0) | 6, 7, 8, 9 | none | none | 1 |
| 221 | (5,9) | 12, 13 | 8 | none | 221 |
| 573 | (0,0) | 7, 8 | none | none | 1 |
| 1413 | (0,0) | 7 | none | none | 1 |

The four empty-window cases fail reachability for length/valuation/parity
reasons before correction membership is tested. The only genuine
nonmembership case is \(n=221\), so this filtered range is far too sparse to
suggest a quantitative correlation theorem. It does, however, show that the
open lemma must explicitly require a nonempty admissible window.

Reproduce:
`python scripts/explore_primitive_q2_correlation.py`.

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
