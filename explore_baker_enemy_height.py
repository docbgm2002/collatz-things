#!/usr/bin/env python3
"""Measure reduced enemy heights for primitive repunit-tail prefixes."""

import argparse
import statistics

from explore_repunit_tail_merges import scan as scan_merges


def v2(value):
    return (value & -value).bit_length() - 1


def reduced_enemy_rows(n, checkpoints):
    """Return the Baker-normalized enemy data at selected prefix lengths."""
    x = (3**n - 1) // 2
    E = 0
    A = -1
    rows = {}

    for K in range(1, max(checkpoints) + 1):
        value = 3 * x + 1
        e = v2(value)
        x = value >> e

        A = 3 * A + (1 << (E + 1))
        E += e

        if K not in checkpoints:
            continue

        R = A + (1 << (E + 1))
        modulus = 1 << (E + 2)
        assert (pow(3, n + K, modulus) + R) % modulus == 0
        assert R != 0
        r = 0
        reduced = R
        while reduced % 3 == 0:
            reduced //= 3
            r += 1

        height = abs(reduced).bit_length()
        rows[K] = {
            "n": n,
            "K": K,
            "E": E,
            "r": r,
            "height": height,
            "height_ratio": height / E,
        }

    return rows


def scan(limit, checkpoints):
    merge_result = scan_merges(limit=limit, factor=3)
    primitives = sorted(row["n"] for row in merge_result["primitives"])
    grouped = {K: [] for K in checkpoints}

    for n in primitives:
        for K, row in reduced_enemy_rows(n, checkpoints).items():
            grouped[K].append(row)

    return primitives, grouped


def print_report(primitives, grouped, limit):
    print(f"primitive tails: {len(primitives)} through odd n <= {limit}")
    print("K  samples  min(h/E)  median(h/E)  max(h/E)  min-height case")

    for K in sorted(grouped):
        rows = grouped[K]
        ratios = [row["height_ratio"] for row in rows]
        minimum = min(rows, key=lambda row: row["height_ratio"])
        print(
            f"{K:3d} {len(rows):8d} "
            f"{min(ratios):9.4f} {statistics.median(ratios):12.4f} "
            f"{max(ratios):9.4f} "
            f"n={minimum['n']}, E={minimum['E']}, "
            f"h={minimum['height']}, v3(R)={minimum['r']}"
        )


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=2001)
    parser.add_argument(
        "--checkpoints",
        type=int,
        nargs="+",
        default=[16, 32, 64, 128, 256],
    )
    return parser.parse_args()


def main():
    args = parse_args()
    checkpoints = sorted(set(args.checkpoints))
    primitives, grouped = scan(args.limit, checkpoints)
    print_report(primitives, grouped, args.limit)


if __name__ == "__main__":
    main()
