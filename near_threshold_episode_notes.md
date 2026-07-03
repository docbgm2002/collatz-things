# Near-Threshold Repunit Episodes

**Building on:** `explore_repunit_tight_margins.py`,
`explore_near_threshold_episodes.py`

**Status:** finite diagnostic on selected tight-margin cases. This note is
not a certificate beyond the named exponents.

---

## 1. Question

The tight-margin scan through odd \(n\le20001\) found that the smallest exact
first-descent margins occur at large exponents, even though the largest
observed stopping ratio remains the small exponent \(n=23\).

The diagnostic question is:

> When a repunit tail comes within a few bits of the Mersenne target before
> first descent, is the final crossing caused by one exceptional payout, or
> by a short near-threshold episode with several modest repairs?

For each selected exponent, `explore_near_threshold_episodes.py` records the
segment from the first time

\[
-10<\log_2((2^n-1)/x_K)<0
\]

until first descent.

---

## 2. Selected cases

The selected tight-margin cases were:

| \(n\) | \(\sigma_n\) | \(\sigma_n/n\) | final exact margin | final valuation |
|---:|---:|---:|---:|---:|
| 6035 | 8236 | 1.364706 | 0.000152 | 4 |
| 18707 | 26766 | 1.430801 | 0.000205 | 4 |
| 18921 | 25887 | 1.368162 | 0.000268 | 3 |
| 3871 | 5745 | 1.484113 | 0.000593 | 4 |
| 10397 | 14820 | 1.425411 | 0.000619 | 2 |
| 23 | 63 | 2.739130 | 1.693224 | 7 |

The last row is included as the stopping-ratio record control, not as a
tight-margin case.

---

## 3. What the tight cases show

The five large tight-margin cases enter the near-threshold zone very late:

| \(n\) | first near-threshold \(K\) | episode length | actual hits in \((-10,0)\) |
|---:|---:|---:|---:|
| 6035 | 8224 | 13 | 8 |
| 18707 | 26742 | 25 | 22 |
| 18921 | 25877 | 11 | 10 |
| 3871 | 5723 | 23 | 21 |
| 10397 | 14794 | 27 | 23 |

The entry episode is not a monotone glide to descent. Several cases dip back
below the \(-10\)-bit band after first entry. The orbit is better described
as a near-threshold oscillation: valuation-one runs push the margin downward,
while modest payouts repeatedly pull it back toward zero.

The final crossing is usually modest:

- \(n=6035\), \(18707\), and \(3871\) cross on valuation \(4\);
- \(n=18921\) crosses on valuation \(3\);
- \(n=10397\) crosses on valuation \(2\), after a valuation \(8\) at the
  preceding step brings the margin to about \(-0.4144\) bits.

Thus the tightest finite margins are not explained by a single enormous late
payout. They are short balanced episodes where the final crossing happens
after the orbit has already been brought within a few bits of the target.

---

## 4. Contrast with the ratio-record case

The exponent \(n=23\) behaves differently:

- it enters the \((-10,0)\) band at \(K=6\);
- it remains in the near-threshold regime for most of its tail;
- it has long valuation-one runs, including a final run of length \(7\)
  before the terminal repair;
- it crosses with valuation \(7\) and a comparatively large final margin
  \(1.693224\).

So the stopping-ratio record and the tight-margin records are different
phenomena. The small record exponent spends a long time near the threshold;
the large tight cases arrive near the threshold late and then cross after a
short repair episode.

---

## 5. Theory implication

The near-threshold cases support the payout-ancestry viewpoint more than a
single-terminal-payout viewpoint.

A useful next theorem should not say:

> once the orbit enters a fixed band, it must cross within a uniformly bounded
> number of steps.

The observed entry episodes are short in this sample, but the earlier
enemy-episode work already warns against local recovery bounds.

A better target is:

> In a near-threshold episode, every valuation-one drift must be paid for by
> a nearby collection of modest payouts. Either those payouts contain a
> reachable shell ancestor, or their balanced spacing gives an amortized
> upper bound on how long the orbit can remain near threshold without
> descent.

This links the near-threshold diagnostic back to the concentrated/diffuse
ancestry split in `primitive_ancestry_lemma.md`.

---

## 6. Reproduction

Run:

```bash
python explore_near_threshold_episodes.py --tail 8
```

The script uses exact integer orbits and floating logarithms only for
diagnostic margins.
