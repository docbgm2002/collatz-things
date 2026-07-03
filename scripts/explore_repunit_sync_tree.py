#!/usr/bin/env python3
"""Enumerate exact early repunit synchronization cylinders.

For an even exponent gap g, at large-tail step s compare

    x_s(n) and x_(s+g)(n-g).

For fixed predecessor valuation words of lengths s-1 and s+1, equality of
the successor correction H=3A+2^(E+1) gives an exact synchronization
cylinder in the exponent n. This script enumerates those cylinders up to a
chosen cumulative-valuation depth and measures their residue mass.

The enumeration is symbolic in valuation words; it does not scan a finite
interval of exponents.
"""

import argparse
from collections import Counter, defaultdict

from explore_entropy_balance import discrete_log_base3
from verify_repunit_low_prefix import exact_pattern_class


def compositions(total, length, prefix=()):
    if length == 1:
        yield prefix + (total,)
        return
    for first in range(1, total - length + 2):
        yield from compositions(total - first, length - 1, prefix + (first,))


def correction_state(pattern):
    E = 0
    A = -1
    for e in pattern:
        A = 3 * A + (1 << (E + 1))
        E += e
    return E, A


def exponent_cylinder(pattern):
    residue, E = exact_pattern_class(pattern)
    target = (2 * residue + 1) % (1 << (E + 2))
    exponent = discrete_log_base3(target, E + 2)
    if exponent is None or exponent % 2 == 0:
        return None
    return exponent % (1 << E), E


def pattern_records(length, max_total):
    records = []
    for total in range(length, max_total + 1):
        for pattern in compositions(total, length):
            cylinder = exponent_cylinder(pattern)
            if cylinder is None:
                continue
            E, A = correction_state(pattern)
            assert E == total
            records.append(
                {
                    "pattern": pattern,
                    "E": E,
                    "A": A,
                    "H": 3 * A + (1 << (E + 1)),
                    "residue": cylinder[0],
                    "depth": cylinder[1],
                }
            )
    return records


def compatible_cylinder(large, small, gap):
    """Intersect n-class of large with shifted (n-gap)-class of small."""
    r1, q1 = large["residue"], large["depth"]
    r2, q2 = (
        (small["residue"] + gap) % (1 << small["depth"]),
        small["depth"],
    )
    common = min(q1, q2)
    if r1 % (1 << common) != r2 % (1 << common):
        return None
    if q1 >= q2:
        return r1, q1
    return r2, q2


def enumerate_step(step, max_total, gap=2):
    large_records = pattern_records(step - 1, max_total)
    small_records = pattern_records(step + gap - 1, max_total)
    small_by_H = defaultdict(list)
    for record in small_records:
        small_by_H[record["H"]].append(record)

    cylinders = {}
    for large in large_records:
        for small in small_by_H.get(large["H"], ()):
            cylinder = compatible_cylinder(large, small, gap)
            if cylinder is None:
                continue
            residue, depth = cylinder
            key = (residue, depth)
            cylinders[key] = {
                "residue": residue,
                "depth": depth,
                "gap": gap,
                "step": step,
                "large_pattern": large["pattern"],
                "small_pattern": small["pattern"],
                "large_E": large["E"],
                "small_E": small["E"],
                "valuation_gap": abs(large["E"] - small["E"]),
            }

    return sorted(cylinders.values(), key=lambda row: (row["depth"], row["residue"]))


def is_in_cylinder(value, residue, depth):
    return value % (1 << depth) == residue


def first_hit_cylinders(step, max_total, gap=2):
    """Cylinders whose predecessor states are distinct."""
    return [
        row
        for row in enumerate_step(step, max_total, gap)
        if row["valuation_gap"] > 0
    ]


def residue_mass(cylinders, common_depth):
    hits = set()
    for row in cylinders:
        if row["depth"] > common_depth:
            continue
        count = 1 << (common_depth - row["depth"])
        for lift in range(count):
            value = row["residue"] + (lift << row["depth"])
            hits.add(value)
    return hits


def print_level(step, max_total, common_depth, cylinders):
    hits = residue_mass(cylinders, common_depth)
    odd_classes = 1 << (common_depth - 1)

    print(
        f"step={step} first-hit cylinders={len(cylinders)} "
        f"resolved mass={len(hits)}/{odd_classes} "
        f"({len(hits) / odd_classes:.6%})"
    )

    depths = Counter(row["depth"] for row in cylinders)
    shells = Counter(row["valuation_gap"] for row in cylinders)
    print(
        f"  depths={sorted(depths.items())} "
        f"shells={sorted(shells.items())}"
    )

    print("  exact first-hit cylinders:")
    for row in cylinders:
        print(
            f"    n={row['residue']} mod 2^{row['depth']} "
            f"large={row['large_pattern']} small={row['small_pattern']} "
            f"(E,F)=({row['large_E']},{row['small_E']}) "
            f"delta={row['valuation_gap']}"
        )

    return hits


def tree_level_hits(gap, through_step, max_total, common_depth):
    levels = {}
    for step in range(2, through_step + 1):
        cylinders = first_hit_cylinders(step, max_total, gap)
        levels[step] = {
            "cylinders": cylinders,
            "hits": residue_mass(cylinders, common_depth),
        }
    return levels


def print_report(gap, through_step, max_total, common_depth):
    print(f"== Gap-{gap} synchronization residue tree ==")
    print(
        f"symbolic levels 2..{through_step}; "
        f"max cumulative valuation={max_total}; "
        f"common modulus=2^{common_depth}"
    )

    cumulative = set()
    previous_mass = None
    for step in range(2, through_step + 1):
        cylinders = first_hit_cylinders(step, max_total, gap)
        hits = print_level(step, max_total, common_depth, cylinders)
        overlap = len(cumulative & hits)
        assert overlap == 0
        cumulative |= hits
        ratio = (
            "n/a"
            if previous_mass is None
            else f"{len(hits) / previous_mass:.6f}"
        )
        print(
            f"  overlap with earlier levels={overlap}; "
            f"level-mass ratio={ratio}; "
            f"cumulative={len(cumulative)}/"
            f"{1 << (common_depth - 1)} "
            f"({len(cumulative) / (1 << (common_depth - 1)):.6%})"
        )
        previous_mass = len(hits)

    print(
        "\nAll masses are depth-truncated lower bounds: cylinders requiring "
        "more than the selected cumulative depth are unresolved."
    )
    return cumulative


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--gap", type=int, default=2)
    parser.add_argument("--through-step", type=int, default=4)
    parser.add_argument("--max-total", type=int, default=16)
    parser.add_argument("--common-depth", type=int, default=16)
    return parser.parse_args()


def main():
    args = parse_args()
    assert args.gap >= 2 and args.gap % 2 == 0
    print_report(
        args.gap,
        args.through_step,
        args.max_total,
        args.common_depth,
    )


if __name__ == "__main__":
    main()
