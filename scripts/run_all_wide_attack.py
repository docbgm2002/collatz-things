#!/usr/bin/env python3
"""Run the whole Opus 5 wide-attack suite (W1-W13) plus the ledger validator.

One command, one verdict.  Each session produced either a `verify_*` script
(exact claims, must PASS) or an `explore_*` script (measurement/calibration,
must run clean and report `consistent`).

    python3 scripts/run_all_wide_attack.py
    python3 scripts/run_all_wide_attack.py --quick     # skip the slow rows
"""

from __future__ import annotations

import argparse
import pathlib
import subprocess
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent

# (script, task, kind, approx seconds, slow?)
SUITE = [
    ("verify_baker_explicit_constants.py", "W9", "verify", 1, False),
    ("verify_certificate_semigroup.py", "W2", "verify", 1, False),
    ("verify_rotation_cocycle_rigidity.py", "W11", "verify", 3, False),
    ("verify_digit_bridge_ceiling.py", "W10", "verify", 1, False),
    ("verify_superposition_ledger.py", "W1", "verify", 6, False),
    ("verify_two_tower_interference.py", "W8", "verify", 1, False),
    ("verify_machine_synthesis.py", "W6", "verify", 9, True),
    ("explore_extremal_law_calibration.py", "W13", "explore", 3, False),
    ("explore_kl_rail_restricted_tree.py", "W4", "explore", 1, False),
    ("explore_syracuse_3adic_conditioning.py", "W5", "explore", 1, False),
    ("explore_ief17_genericity.py", "W7", "explore", 2, False),
    ("explore_carry_cocycle.py", "W3", "explore", 1, False),
    # the repository's own gatekeepers, re-run to confirm nothing regressed
    ("verify_claim_ledger.py", "--", "ledger", 1, False),
    ("verify_shadow.py", "--", "prior", 1, False),
    ("verify_tower.py", "--", "prior", 1, False),
    ("verify_suff1_composition.py", "--", "prior", 2, False),
]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--quick", action="store_true",
                    help="skip rows marked slow (W6 needs z3)")
    ap.add_argument("--timeout", type=int, default=300)
    args = ap.parse_args()

    print("== Opus 5 wide-attack suite ==\n")
    print(f"  {'script':<42s} {'task':<5s} {'kind':<8s} {'time':>7s}  verdict")
    print("  " + "-" * 78)
    failures: list[str] = []
    skipped: list[str] = []
    t_all = time.time()

    for script, task, kind, _approx, slow in SUITE:
        path = HERE / script
        if not path.exists():
            failures.append(f"{script}: MISSING")
            print(f"  {script:<42s} {task:<5s} {kind:<8s} {'-':>7s}  MISSING")
            continue
        if slow and args.quick:
            skipped.append(script)
            print(f"  {script:<42s} {task:<5s} {kind:<8s} {'-':>7s}  skipped")
            continue
        t0 = time.time()
        try:
            r = subprocess.run([sys.executable, str(path)],
                               capture_output=True, text=True,
                               timeout=args.timeout)
            dt = time.time() - t0
            last = [ln for ln in r.stdout.strip().splitlines() if ln.strip()]
            tail = last[-1][:34] if last else ""
            if r.returncode == 0:
                verdict = f"ok    {tail}"
            else:
                verdict = f"FAIL  {tail}"
                failures.append(f"{script}: exit {r.returncode}")
        except subprocess.TimeoutExpired:
            dt = time.time() - t0
            verdict = "TIMEOUT"
            failures.append(f"{script}: timeout")
        print(f"  {script:<42s} {task:<5s} {kind:<8s} {dt:6.1f}s  {verdict}")

    print("  " + "-" * 78)
    print(f"  total {time.time() - t_all:.1f}s")
    if skipped:
        print(f"  skipped: {', '.join(skipped)}")
    print()
    if failures:
        print(f"WIDE-ATTACK SUITE: {len(failures)} FAILURE(S)")
        for f in failures:
            print(f"  - {f}")
        raise SystemExit(1)
    print("WIDE-ATTACK SUITE: ALL PASS")


if __name__ == "__main__":
    main()
