#!/usr/bin/env python3
"""Measure payout concentration on primitive record-deficit prefixes.

The normalized ledger is split into three exact masses:

    I = initial ancestor;
    R = payouts whose canonical shell is not excluded by GPA2;
    B = payouts q == 3 or 4 (mod 6), whose canonical shell is GPA2-blocked.

Thus I + R + B = 1.  The report uses a transparent one-third trichotomy and,
inside the blocked branch, a one-half concentration test.  These thresholds
are diagnostic choices; the underlying masses and effective counts are exact
up to their printed floating-point presentation.
"""

import argparse
from collections import Counter

from explore_repunit_extremal_prefixes import census


def quantile(values, fraction):
    values = sorted(values)
    if not values:
        return 0.0
    index = round((len(values) - 1) * fraction)
    return values[index]


def branch(row):
    total = row["ledger_numerator"]
    if 3 * row["eligible_numerator"] >= total:
        return "eligible>=1/3"
    if 3 * row["initial_numerator"] >= total:
        return "initial>=1/3"
    if 2 * row["blocked_max_numerator"] >= row["blocked_numerator"]:
        return "blocked-concentrated"
    return "blocked-diffuse"


def print_report(limit, factor, min_deficit, top):
    merge_result, rows = census(limit, factor)
    if min_deficit == 2.0:
        dangerous = [
            row for row in rows
            if 3 ** row["K"] >= 2 ** (row["E"] + 2)
        ]
    else:
        dangerous = [row for row in rows if row["deficit"] >= min_deficit]
    branches = Counter(branch(row) for row in dangerous)

    print("== Primitive payout concentration versus diffusion ==")
    print(
        f"finite domain: odd 7 <= n <= {limit}; "
        f"primitive tails={len(merge_result['primitives'])}; "
        f"records D>={min_deficit:g}: {len(dangerous)}"
    )
    print(f"one-third trichotomy: {dict(branches)}")

    for key, label in (
        ("initial_share", "initial mass"),
        ("eligible_share", "GPA2-eligible payout mass"),
        ("blocked_share", "GPA2-blocked payout mass"),
        ("effective_ancestor_count", "effective ancestor count"),
        ("blocked_effective_count", "blocked effective count"),
    ):
        values = [row[key] for row in dangerous]
        print(
            f"{label}: min={min(values):.4f} "
            f"q25={quantile(values, 0.25):.4f} "
            f"median={quantile(values, 0.50):.4f} "
            f"q75={quantile(values, 0.75):.4f} "
            f"max={max(values):.4f}"
        )

    ranked = sorted(dangerous, key=lambda row: row["deficit"], reverse=True)
    print("\nLargest dangerous records:")
    for row in ranked[:top]:
        print(
            f"  n={row['n']:4d} K={row['K']:3d} D={row['deficit']:7.4f} "
            f"I={row['initial_share']:.2%} "
            f"R={row['eligible_share']:.2%} "
            f"B={row['blocked_share']:.2%} "
            f"Neff={row['effective_ancestor_count']:.2f} "
            f"BNeff={row['blocked_effective_count']:.2f} "
            f"Bmax|B={row['blocked_max_conditional_share']:.2%} "
            f"branch={branch(row)}"
        )

    exceptional = [
        row for row in ranked if not branch(row).startswith("eligible")
    ]
    print("\nRecords outside the eligible-mass branch:")
    for row in exceptional:
        print(
            f"  n={row['n']:4d} K={row['K']:3d} D={row['deficit']:7.4f} "
            f"I={row['initial_share']:.2%} "
            f"R={row['eligible_share']:.2%} "
            f"B={row['blocked_share']:.2%} "
            f"blocked_count={row['blocked_count']} "
            f"BNeff={row['blocked_effective_count']:.2f} "
            f"Bmax|B={row['blocked_max_conditional_share']:.2%} "
            f"qs={row['top_qs']} branch={branch(row)}"
        )

    print("\nHighest-deficit representative for each exceptional tail:")
    seen_n = set()
    for row in exceptional:
        if row["n"] in seen_n:
            continue
        seen_n.add(row["n"])
        terms = sorted(
            row["exact_payout_terms"],
            key=lambda term: term["numerator"],
            reverse=True,
        )
        profile = ", ".join(
            f"j={term['step']}:E={term['pre_E']}:q={term['q']}:"
            f"{'B' if term['q'] % 6 in (3, 4) else 'R'}:"
            f"{term['numerator']/row['ledger_numerator']:.2%}"
            for term in terms
        )
        print(
            f"  n={row['n']:4d} K={row['K']:3d} "
            f"branch={branch(row)} | {profile}"
        )


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=2001)
    parser.add_argument("--factor", type=int, default=3)
    parser.add_argument("--min-deficit", type=float, default=2.0)
    parser.add_argument("--top", type=int, default=20)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    print_report(args.limit, args.factor, args.min_deficit, args.top)
