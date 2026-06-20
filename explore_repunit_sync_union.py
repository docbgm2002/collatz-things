#!/usr/bin/env python3
"""Measure the union of several repunit synchronization residue trees."""

import argparse
from itertools import combinations

from explore_repunit_sync_tree import tree_level_hits


def build_gap_tree(gap, through_step, max_total, common_depth):
    levels = tree_level_hits(gap, through_step, max_total, common_depth)
    union = set()
    for level in levels.values():
        assert not (union & level["hits"])
        union |= level["hits"]
    return levels, union


def scan(gaps, through_step, max_total, common_depth):
    trees = {}
    for gap in gaps:
        levels, union = build_gap_tree(
            gap, through_step, max_total, common_depth
        )
        trees[gap] = {"levels": levels, "union": union}
    return trees


def print_report(trees, common_depth):
    odd_classes = 1 << (common_depth - 1)
    print("== Synchronization-tree union ==")
    print(f"common modulus=2^{common_depth}; odd classes={odd_classes}")

    all_union = set()
    for gap in sorted(trees):
        tree = trees[gap]
        print(f"\ngap {gap}:")
        for step, level in sorted(tree["levels"].items()):
            print(
                f"  step={step} cylinders={len(level['cylinders'])} "
                f"mass={len(level['hits'])}/{odd_classes} "
                f"({len(level['hits']) / odd_classes:.6%})"
            )
        print(
            f"  tree union={len(tree['union'])}/{odd_classes} "
            f"({len(tree['union']) / odd_classes:.6%})"
        )
        all_union |= tree["union"]

    print("\nCross-gap intersections:")
    for left, right in combinations(sorted(trees), 2):
        overlap = trees[left]["union"] & trees[right]["union"]
        print(
            f"  gaps {left},{right}: {len(overlap)}/{odd_classes} "
            f"({len(overlap) / odd_classes:.6%})"
        )

    if len(trees) >= 3:
        common = set.intersection(
            *(trees[gap]["union"] for gap in sorted(trees))
        )
        print(
            f"  all gaps: {len(common)}/{odd_classes} "
            f"({len(common) / odd_classes:.6%})"
        )

    print(
        f"\ncombined union={len(all_union)}/{odd_classes} "
        f"({len(all_union) / odd_classes:.6%})"
    )
    print(
        f"unresolved complement={odd_classes - len(all_union)}/"
        f"{odd_classes} "
        f"({(odd_classes - len(all_union)) / odd_classes:.6%})"
    )
    print(
        "All figures are depth-truncated lower bounds on synchronization "
        "coverage."
    )
    return all_union


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--gaps", default="2,4,6")
    parser.add_argument("--through-step", type=int, default=7)
    parser.add_argument("--max-total", type=int, default=24)
    parser.add_argument("--common-depth", type=int, default=24)
    return parser.parse_args()


def main():
    args = parse_args()
    gaps = tuple(sorted({int(value) for value in args.gaps.split(",")}))
    assert all(gap >= 2 and gap % 2 == 0 for gap in gaps)
    trees = scan(
        gaps,
        args.through_step,
        args.max_total,
        args.common_depth,
    )
    print_report(trees, args.common_depth)


if __name__ == "__main__":
    main()
