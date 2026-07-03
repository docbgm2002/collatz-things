#!/usr/bin/env python3
"""Verify the bounded merger certificate in repunit_tail_merge_reduction.md."""

from explore_repunit_tail_merges import scan


def main():
    result = scan(limit=10001, factor=3)
    merges = result["merges"]
    primitives = result["primitives"]

    assert len(merges) == 4783
    assert len(primitives) == 215
    assert not result["unresolved"]
    assert all(
        row["diagonal"] == row["source_diagonal"] for row in merges
    )

    worst = max(primitives, key=lambda row: row["ratio"])
    assert (worst["n"], worst["sigma"]) == (23, 63)

    gap_counts = {}
    for row in merges:
        gap_counts[row["gap"]] = gap_counts.get(row["gap"], 0) + 1
    assert gap_counts[2] == 1547
    assert gap_counts[4] == 806

    print(
        "MERGE finite certificate: PASS "
        "(odd 7 <= n <= 10001; 4783 merges, 215 primitive, "
        "0 off-diagonal, 0 unresolved)"
    )


if __name__ == "__main__":
    main()
