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
python scripts/verify_shadow.py
python scripts/explore_repunit_sync_tree.py --through-step 7 --max-total 24 --common-depth 24
```
