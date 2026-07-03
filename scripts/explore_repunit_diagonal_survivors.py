#!/usr/bin/env python3
"""
Explore the diagonal repunit-tail stopping problem.

For odd n, start at

    a_n = (3^n - 1) / 2

and measure the first K for which f^K(a_n) < 2^n - 1.  The script records
linear-window ratio records and tracks the exact affine accumulation

    x_K = (3^K a_n + c_K) / 2^E_K.

The exact descent margin decomposes as

    exact_margin = raw_surplus - affine_penalty,

where

    raw_surplus =
        E_K - K log2(3) - log2(a_n / (2^n - 1)),

    affine_penalty =
        log2(1 + c_K / (3^K a_n)).

Research tool only: all reported statements are finite computations.
"""

import argparse
import csv
import math
import time
from collections import Counter


THETA = math.log2(3)


def v2(n):
    return (n & -n).bit_length() - 1


def log2_int(n):
    """Accurate-enough log2 for a positive integer of arbitrary size."""
    bits = n.bit_length()
    if bits <= 1022:
        return math.log2(n)
    shift = bits - 1022
    return shift + math.log2(n >> shift)


def logaddexp2(a, b):
    """Return log2(2^a + 2^b), including -infinity inputs."""
    if a == -math.inf:
        return b
    if b == -math.inf:
        return a
    hi = max(a, b)
    lo = min(a, b)
    if hi - lo > 55:
        return hi
    return hi + math.log2(1 + math.exp2(lo - hi))


def log2_one_plus_from_log2_ratio(log_ratio):
    """Return log2(1+q) from log2(q), retaining very small ratios."""
    if log_ratio == -math.inf:
        return 0.0
    if log_ratio < -55:
        return math.exp2(log_ratio) / math.log(2)
    return math.log1p(math.exp2(log_ratio)) / math.log(2)


def compact_pattern(values, width=18):
    if len(values) <= 2 * width:
        return ",".join(map(str, values))
    head = ",".join(map(str, values[:width]))
    tail = ",".join(map(str, values[-width:]))
    return f"{head},...,{tail}"


def trace_exponent(n, factor, start=None):
    target = (1 << n) - 1
    if start is None:
        start = (3**n - 1) // 2
    x = start

    # q_K = c_K/(3^K start), evaluated in log-space from the exact
    # valuation ledger:
    #
    # q_K = q_(K-1) + 2^E_(K-1)/(3^K start).
    #
    # This avoids constructing c_K as a second huge integer during large
    # scans while retaining the exact exponents in every summand.
    log_q = -math.inf
    log_start = log2_int(start)
    E = 0
    valuations = []
    min_exact_before_descent = math.inf

    for K in range(1, factor * n + 1):
        affine_term_log = E - THETA * K - log_start
        log_q = logaddexp2(log_q, affine_term_log)

        value = 3 * x + 1
        e = v2(value)
        x = value >> e
        E += e
        valuations.append(e)

        exact_margin = log2_int(target) - log2_int(x)
        if exact_margin < min_exact_before_descent:
            min_exact_before_descent = exact_margin

        if x < target:
            initial_gap = log2_int(start) - log2_int(target)
            raw_surplus = E - THETA * K - initial_gap
            affine_penalty = log2_one_plus_from_log2_ratio(log_q)
            decomposition_error = abs(
                exact_margin - (raw_surplus - affine_penalty)
            )

            return {
                "n": n,
                "sigma": K,
                "ratio": K / n,
                "E": E,
                "mean_e": E / K,
                "exact_margin": exact_margin,
                "raw_surplus": raw_surplus,
                "affine_penalty": affine_penalty,
                "decomposition_error": decomposition_error,
                "min_pre_descent_margin": min_exact_before_descent,
                "pattern": tuple(valuations),
                "found": True,
            }

    initial_gap = log2_int(start) - log2_int(target)
    raw_surplus = E - THETA * factor * n - initial_gap
    affine_penalty = log2_one_plus_from_log2_ratio(log_q)
    exact_margin = log2_int(target) - log2_int(x)
    return {
        "n": n,
        "sigma": None,
        "ratio": math.inf,
        "E": E,
        "mean_e": E / (factor * n),
        "exact_margin": exact_margin,
        "raw_surplus": raw_surplus,
        "affine_penalty": affine_penalty,
        "decomposition_error": abs(
            exact_margin - (raw_surplus - affine_penalty)
        ),
        "min_pre_descent_margin": min_exact_before_descent,
        "pattern": tuple(valuations),
        "found": False,
    }


def scan(limit, factor, constants, progress_every=0):
    records = []
    failures = {constant: [] for constant in constants}
    unresolved = []
    worst_ratio = -1.0
    smallest_margin = None
    largest_penalty = None
    max_decomposition_error = 0.0
    started = time.perf_counter()
    power3 = 3**7

    for n in range(7, limit + 1, 2):
        row = trace_exponent(n, factor, start=(power3 - 1) // 2)
        power3 *= 9
        max_decomposition_error = max(
            max_decomposition_error, row["decomposition_error"]
        )

        if not row["found"]:
            unresolved.append(row)
        else:
            if row["ratio"] > worst_ratio:
                worst_ratio = row["ratio"]
                records.append(row)

            if (
                smallest_margin is None
                or row["exact_margin"] < smallest_margin["exact_margin"]
            ):
                smallest_margin = row

            if (
                largest_penalty is None
                or row["affine_penalty"] > largest_penalty["affine_penalty"]
            ):
                largest_penalty = row

            for constant in constants:
                if row["ratio"] > constant:
                    failures[constant].append(row)

        if progress_every and n % progress_every in (0, 1):
            elapsed = time.perf_counter() - started
            print(
                f"progress n={n}/{limit} records={len(records)} "
                f"worst={worst_ratio:.6f} elapsed={elapsed:.1f}s"
            )

    elapsed = time.perf_counter() - started
    return {
        "records": records,
        "failures": failures,
        "unresolved": unresolved,
        "smallest_margin": smallest_margin,
        "largest_penalty": largest_penalty,
        "max_decomposition_error": max_decomposition_error,
        "elapsed": elapsed,
    }


def print_row(row, include_pattern=False):
    sigma = "unresolved" if row["sigma"] is None else str(row["sigma"])
    ratio = "inf" if not math.isfinite(row["ratio"]) else f"{row['ratio']:.9f}"
    print(
        f"n={row['n']:6d} sigma={sigma:>10} ratio={ratio:>12} "
        f"E={row['E']:7d} mean_e={row['mean_e']:.6f} "
        f"exact={row['exact_margin']:.9f} "
        f"raw={row['raw_surplus']:.9f} "
        f"affine={row['affine_penalty']:.9f}"
    )
    if include_pattern:
        print(f"  valuations: {compact_pattern(row['pattern'])}")


def write_csv(path, rows):
    fields = [
        "n",
        "sigma",
        "ratio",
        "E",
        "mean_e",
        "exact_margin",
        "raw_surplus",
        "affine_penalty",
        "decomposition_error",
    ]
    with open(path, "w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row[field] for field in fields})


def print_survivor_structure(failures, thresholds):
    print("\n== Scaled survivor structure ==")
    print(
        "A threshold C lists exponents with sigma_n/n > C in the finite "
        "domain."
    )
    for threshold in thresholds:
        rows = failures[threshold]
        print(f"\nC={threshold:g}: {len(rows)} survivors")
        if not rows:
            continue

        largest_n = max(rows, key=lambda row: row["n"])
        worst = max(rows, key=lambda row: row["ratio"])
        print(
            f"  largest exponent n={largest_n['n']} "
            f"(ratio={largest_n['ratio']:.6f}); "
            f"worst ratio at n={worst['n']} ({worst['ratio']:.6f})"
        )
        print(
            "  exponents: "
            + ",".join(str(row["n"]) for row in rows[:24])
            + ("..." if len(rows) > 24 else "")
        )

        for bits in (3, 4, 5, 6, 7, 8):
            residues = Counter(row["n"] % (1 << bits) for row in rows)
            occupied = len(residues)
            total_odd_classes = 1 << (bits - 1)
            top = ", ".join(
                f"{residue}:{count}" for residue, count in residues.most_common(4)
            )
            print(
                f"  mod 2^{bits}: {occupied}/{total_odd_classes} odd classes; "
                f"top {top}"
            )

        for width in (4, 8, 12):
            blocks = Counter(row["pattern"][:width] for row in rows)
            most_common = blocks.most_common(1)[0]
            print(
                f"  first {width} valuations: {len(blocks)} distinct; "
                f"max multiplicity={most_common[1]}"
            )


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--limit",
        type=int,
        default=5001,
        help="largest odd exponent to test (default: 5001)",
    )
    parser.add_argument(
        "--factor",
        type=int,
        default=3,
        help="maximum number of steps as factor*n (default: 3)",
    )
    parser.add_argument(
        "--constants",
        default="2.75,2.8,2.9,3.0",
        help="comma-separated candidate linear constants",
    )
    parser.add_argument(
        "--structure-thresholds",
        default="",
        help=(
            "comma-separated scaled survivor thresholds for residue/block "
            "diagnostics, e.g. 1.5,1.75,2.0"
        ),
    )
    parser.add_argument(
        "--progress-every",
        type=int,
        default=0,
        help="print progress approximately every this many exponents",
    )
    parser.add_argument(
        "--csv",
        help="optional CSV path for ratio-record rows",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    constants = tuple(float(value) for value in args.constants.split(","))
    structure_thresholds = tuple(
        float(value)
        for value in args.structure_thresholds.split(",")
        if value.strip()
    )
    scan_thresholds = tuple(dict.fromkeys(constants + structure_thresholds))
    result = scan(
        limit=args.limit,
        factor=args.factor,
        constants=scan_thresholds,
        progress_every=args.progress_every,
    )

    print("== Diagonal repunit-tail constant search ==")
    print(
        f"finite domain: odd 7 <= n <= {args.limit}; "
        f"search window: K <= {args.factor}n"
    )
    print("\nRatio records:")
    for row in result["records"]:
        print_row(row, include_pattern=True)

    print("\nCandidate constants:")
    for constant in constants:
        failed = result["failures"][constant]
        if failed:
            worst = max(failed, key=lambda row: row["ratio"])
            print(
                f"  C={constant:g}: {len(failed)} finite exceptions; "
                f"worst n={worst['n']} ratio={worst['ratio']:.9f}"
            )
        else:
            print(f"  C={constant:g}: no exceptions in the finite domain")

    if structure_thresholds:
        print_survivor_structure(result["failures"], structure_thresholds)

    print("\nSmallest exact first-descent margin:")
    print_row(result["smallest_margin"], include_pattern=True)
    print("\nLargest affine penalty at first descent:")
    print_row(result["largest_penalty"], include_pattern=True)

    print(
        f"\nUnresolved within {args.factor}n: {len(result['unresolved'])}; "
        f"max decomposition error={result['max_decomposition_error']:.3e}; "
        f"elapsed={result['elapsed']:.2f}s"
    )
    if result["unresolved"]:
        print("First unresolved cases:")
        for row in result["unresolved"][:10]:
            print_row(row, include_pattern=True)

    if args.csv:
        write_csv(args.csv, result["records"])
        print(f"Wrote ratio records to {args.csv}")


if __name__ == "__main__":
    main()
