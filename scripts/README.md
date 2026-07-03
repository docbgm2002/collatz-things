# Scripts

Python verification and exploration programs live here.

- `verify_*.py` scripts check maintained identities, finite certificates, and
  claim-ledger entries.
- `explore_*.py` scripts are research probes and diagnostics; their output is
  evidence, not a proof unless a note says otherwise.
- `scripts/capstone_data.py` is a small data-generation helper for the repunit
  equidistribution notes.

Run scripts from the repository root, for example:

```bash
python scripts/verify_shadow.py
python scripts/explore_repunit_sync_tree.py --through-step 7 --max-total 24 --common-depth 24
```
