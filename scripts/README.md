# Scripts

Python verification and exploration programs live here.

- `verify_*.py` scripts check maintained identities, finite certificates, and
  claim-ledger entries.
- `explore_*.py` scripts are research probes and diagnostics; their output is
  bounded evidence, not a proof of a universal claim. A ledger row may cite
  one as the generator of an explicitly finite certificate or as a
  cross-check on a human proof.
- `scripts/capstone_data.py` is a small data-generation helper for the repunit
  equidistribution notes.

Run scripts from the repository root, for example:

```bash
python scripts/verify_claim_ledger.py
python scripts/verify_repunit_storage_dominance.py --limit 5001
python scripts/verify_repunit_storage_dominance.py --limit 2001 --check-e2-preimage
python scripts/verify_repunit_storage_dominance.py --limit 2001 --check-s4
python scripts/verify_repunit_storage_dominance.py --limit 501 --check-height-s --s-max 32
python scripts/verify_repunit_storage_dominance.py --limit 2001 --check-k-linear
python scripts/verify_repunit_storage_dominance.py --limit 2001 --check-h-linear
python scripts/verify_repunit_storage_dominance.py --limit 2001 --check-rho-cap
python scripts/verify_repunit_storage_dominance.py --limit 2001 --check-even-budget
python scripts/verify_repunit_storage_dominance.py --limit 2001 --check-nine-eleven
python scripts/verify_repunit_storage_dominance.py --limit 2001 --check-density6-envelope
python scripts/verify_repunit_storage_dominance.py --limit 2001 --check-rho-cap-6
python scripts/verify_repunit_storage_dominance.py --limit 2001 --check-nine-eleven-6
python scripts/verify_repunit_storage_dominance.py --limit 2001 --check-h-linear-6
python scripts/explore_even_budget_surplus.py --limit 2001
python scripts/explore_911_descent_split.py --limit 2001
python scripts/explore_nc6_split_bound.py --limit 2001
python scripts/explore_9116_e0_two.py --limit 2001
python scripts/explore_block8_x1.py --limit 2001
python scripts/verify_repunit_storage_dominance.py --limit 2001 --check-block8-first
python scripts/verify_repunit_storage_dominance.py --limit 2001 --check-block8-mod17
python scripts/explore_block8_mod17.py --limit 2001
python scripts/explore_block8_residual_density.py --limit 4001
python scripts/explore_block8_mod8_drift.py --limit 4001
python scripts/verify_repunit_storage_dominance.py --limit 2001 --check-early-collisions
# Note: the main verify() pass already asserts K_down <= 6n (and K_down <= T).
# For deep H/rho censuses alone, prefer explore_mersenne_shortcut_budget.py
# or a lightweight loop (avoids heavy SD1 R-tracking in verify).
python scripts/explore_ec1_collisions.py --limit 2001
python scripts/explore_ec1_near.py --limit 201
python scripts/explore_sd_l1_later.py --limit 501
python scripts/verify_shadow.py
python scripts/explore_repunit_sync_tree.py --through-step 7 --max-total 24 --common-depth 24
python scripts/explore_cocycle_factor_complexity.py --blocks 1000
python scripts/verify_zero_digit_orbits.py
python scripts/explore_zero_digit_orbits.py --max-period 12 --bit-bound 20
```
