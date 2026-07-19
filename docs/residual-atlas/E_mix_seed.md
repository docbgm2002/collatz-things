# E_mix seed — normal-form attempt (closed)

**Status:** Closed without a normal form. Supports **demote outcome 1**.

**Prototype:** odd repunit exponent \(n=471\), the unique blocked-diffuse
primitive in the PCD2 census through \(n\le5001\).

**Script:** `scripts/explore_atlas_emix_probe.py`.

## Probe result (full pre-descent tail)

| Quantity | Value |
|---|---|
| Steps to descent below \(M_{471}\) | 732 |
| Payout alphabet on whole tail | \(\{2,3,4,5,6,7,8\}\) |
| Earliest mechanical \(3/4\) suffix | **None** |
| Sliding 40-step payout alphabets | Always contain \(2\) and usually \(\ge3\) distinct payout sizes |
| Best terminal payout period | trivial (\(1\) with \(2\) reps) |
| Gap alphabet between payouts | \(\{1,\ldots,9\}\), not \(\{3,4\}\) |

Conclusion: through the entire finite descent, \(n=471\) never enters
\(\mathcal L_{3/4}\). There is no obvious ultimately periodic payout or gap
law to promote to a generating rule for \(\mathcal E_{\mathrm{mix}}\).

## What would have counted as a normal form

Any of:

1. eventual entry into mechanical \(\{3,4\}\)-gap \(q=3\) language;
2. a finite automaton / substitution rule generating the payout-gap word;
3. an exact inverse-branch IFS (as for rail-5 survivors) whose attractor
   contains the seed and has a clean membership test.

None appeared in the probe. Keeping \(\mathcal E_{\mathrm{mix}}\) as an
unnamed residual class would violate the L5 promote criterion
(“named class with exact normal form”).

## Decision consequence

Treat \(\mathcal E_{\mathrm{mix}}\) as a **diagnostic label for one finite
seed**, not as an atlas exotic class. Harden demote-1: emptying
\(\mathcal R\subset\mathcal L_{3/4}\) is not a blocked-diffuse cover and is
not a qualitative spine-descent route.
