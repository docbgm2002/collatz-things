#!/usr/bin/env python3
"""
Explore valuation-deficit blocks in repunit tails.

For each odd exponent n, follow the repunit tail until first descent below
2^n-1. For each block length L, inspect windows of valuations e_i and define

    block_surplus = sum(e_i) - L log2(3).

A negative block surplus is a local growth/deficit episode. The recovery time
is the least t >= L such that the cumulative surplus from the block start
through t steps becomes nonnegative.

This is a finite diagnostic tool, not a proof.
"""

import argparse
import math
import time
from collections import Counter

from explore_repunit_diagonal_survivors import trace_exponent
from explore_repunit_tail_merges import scan as scan_merges


THETA = math.log2(3)


def max_run_of_ones(values):
    best = current = 0
    for value in values:
        if value == 1:
            current += 1
            best = max(best, current)
        else:
            current = 0
    return best


def recovery_time(pattern, start, length, max_multiple):
    """Return first local time with nonnegative surplus, or None."""
    total = sum(pattern[start : start + length]) - THETA * length
    if total >= 0:
        return length

    upper = min(len(pattern) - start, max_multiple * length)
    for local_time in range(length + 1, upper + 1):
        total += pattern[start + local_time - 1] - THETA
        if total >= 0:
            return local_time
    return None


def scan(limit, block_lengths, max_multiple, primitive_only=False):
    stats = {}
    for length in block_lengths:
        stats[length] = {
            "windows": 0,
            "deficit_windows": 0,
            "total_e_counts": Counter(),
            "recovery_buckets": Counter(),
            "worst_mean": None,
            "worst_prefix": None,
            "longest_recovery": None,
            "top_deficits": [],
        }

    power3 = 3**7
    started = time.perf_counter()
    primitive_exponents = None
    if primitive_only:
        merge_result = scan_merges(limit=limit, factor=3)
        primitive_exponents = {row["n"] for row in merge_result["primitives"]}

    for n in range(7, limit + 1, 2):
        if primitive_exponents is not None and n not in primitive_exponents:
            power3 *= 9
            continue
        row = trace_exponent(n, factor=3, start=(power3 - 1) // 2)
        power3 *= 9
        pattern = row["pattern"]

        prefix = [0]
        for value in pattern:
            prefix.append(prefix[-1] + value)

        for length in block_lengths:
            state = stats[length]
            if len(pattern) < length:
                continue

            for start in range(0, len(pattern) - length + 1):
                total_e = prefix[start + length] - prefix[start]
                surplus = total_e - THETA * length
                block = pattern[start : start + length]

                local = 0.0
                minimum_prefix = math.inf
                minimum_at = 0
                for offset, value in enumerate(block, start=1):
                    local += value - THETA
                    if local < minimum_prefix:
                        minimum_prefix = local
                        minimum_at = offset

                record = {
                    "n": n,
                    "start": start,
                    "length": length,
                    "total_e": total_e,
                    "mean_e": total_e / length,
                    "surplus": surplus,
                    "minimum_prefix": minimum_prefix,
                    "minimum_at": minimum_at,
                    "max_ones": max_run_of_ones(block),
                    "block": block,
                }

                state["windows"] += 1
                state["total_e_counts"][total_e] += 1

                if (
                    state["worst_mean"] is None
                    or record["mean_e"] < state["worst_mean"]["mean_e"]
                ):
                    state["worst_mean"] = record

                if (
                    state["worst_prefix"] is None
                    or minimum_prefix < state["worst_prefix"]["minimum_prefix"]
                ):
                    state["worst_prefix"] = record

                if surplus >= 0:
                    continue

                state["deficit_windows"] += 1
                recovery = recovery_time(pattern, start, length, max_multiple)
                record["recovery"] = recovery

                if recovery is None:
                    state["recovery_buckets"][f">{max_multiple}L/censored"] += 1
                else:
                    multiple = math.ceil(recovery / length)
                    state["recovery_buckets"][f"<={multiple}L"] += 1
                    if (
                        state["longest_recovery"] is None
                        or recovery > state["longest_recovery"]["recovery"]
                    ):
                        state["longest_recovery"] = record

                state["top_deficits"].append(record)

    for state in stats.values():
        state["top_deficits"].sort(key=lambda item: item["surplus"])
        del state["top_deficits"][12:]

    return stats, time.perf_counter() - started


def compact(values, width=24):
    if len(values) <= width:
        return ",".join(map(str, values))
    half = width // 2
    return (
        ",".join(map(str, values[:half]))
        + ",...,"
        + ",".join(map(str, values[-half:]))
    )


def print_record(label, record):
    if record is None:
        print(f"  {label}: none")
        return
    recovery = record.get("recovery")
    recovery_text = "n/a" if recovery is None else str(recovery)
    print(
        f"  {label}: n={record['n']} start={record['start']} "
        f"E={record['total_e']} mean={record['mean_e']:.6f} "
        f"surplus={record['surplus']:.6f} "
        f"min_prefix={record['minimum_prefix']:.6f}@{record['minimum_at']} "
        f"ones={record['max_ones']} recovery={recovery_text}"
    )
    print(f"    block={compact(record['block'])}")


def print_report(stats, limit, max_multiple, elapsed, primitive_only):
    print("== Repunit-tail valuation block deficits ==")
    print(
        f"finite domain: odd 7 <= n <= {limit}; tails stop at first descent; "
        f"recovery search <= {max_multiple}L; "
        f"population={'primitive tails' if primitive_only else 'all tails'}"
    )

    for length, state in stats.items():
        print(f"\nL={length}")
        print(
            f"  windows={state['windows']} "
            f"deficit={state['deficit_windows']} "
            f"({state['deficit_windows']/state['windows']:.2%})"
        )
        low_totals = sorted(state["total_e_counts"].items())[:8]
        print(f"  lowest total-valuation counts: {low_totals}")
        print(f"  recovery buckets: {dict(state['recovery_buckets'])}")
        print_record("lowest mean", state["worst_mean"])
        print_record("lowest prefix", state["worst_prefix"])
        print_record("longest observed recovery", state["longest_recovery"])
        print("  most severe deficit blocks:")
        for record in state["top_deficits"][:5]:
            print_record("deficit", record)

    print(f"\nelapsed={elapsed:.2f}s")


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=2001)
    parser.add_argument("--lengths", default="8,16,32,64")
    parser.add_argument("--max-multiple", type=int, default=4)
    parser.add_argument(
        "--primitive-only",
        action="store_true",
        help="analyse only tails that do not merge into a smaller tail first",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    lengths = tuple(int(value) for value in args.lengths.split(","))
    stats, elapsed = scan(
        args.limit,
        lengths,
        args.max_multiple,
        primitive_only=args.primitive_only,
    )
    print_report(
        stats,
        args.limit,
        args.max_multiple,
        elapsed,
        args.primitive_only,
    )


if __name__ == "__main__":
    main()
