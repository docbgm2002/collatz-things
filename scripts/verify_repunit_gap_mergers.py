#!/usr/bin/env python3
"""Verify finite ingredients of repunit_gap_merger_analysis.md."""

from collections import Counter

from explore_repunit_gap_mergers import analyse_merge, normal_states
from explore_repunit_sync_tree import first_hit_cylinders, residue_mass
from explore_repunit_tail_merges import scan as scan_merges


def valuation_prefix(n, length):
    _states, valuations = normal_states(n, length)
    return tuple(valuations)


def check_collision_shells():
    result = scan_merges(limit=10001, factor=3)
    rows = [analyse_merge(row) for row in result["merges"]]
    counts = Counter(row["valuation_gap"] for row in rows)

    assert counts == Counter({2: 4527, 4: 192, 6: 60, 8: 4})

    expected = {
        2: (1547, 1496),
        4: (806, 769),
        6: (505, 470),
    }
    for gap, (total, shell_two) in expected.items():
        selected = [row for row in rows if row["gap"] == gap]
        assert len(selected) == total
        assert sum(row["valuation_gap"] == 2 for row in selected) == shell_two

    print("GAPMRG1 collision-shell certificate through n<=10001: PASS")


def check_gap_two_family(limit=10001):
    count = 0
    for n in range(31, limit + 1, 64):
        assert valuation_prefix(n, 1) == (6,)
        assert valuation_prefix(n - 2, 3) == (2, 1, 1)

        large, _ = normal_states(n, 2)
        small, _ = normal_states(n - 2, 4)
        assert large[2] == small[4]
        count += 1

    assert count == 156
    print("GAPMRG2 gap-2 family n=31 mod 64: PASS (156 samples)")


def check_gap_two_step_three_families(limit=10001):
    families = (
        (79, 128, (5, 2), (2, 1, 1, 1)),
        (199, 256, (4, 4), (2, 1, 2, 1)),
        (323, 512, (3, 6), (2, 2, 2, 1)),
        (1289, 4096, (2, 10), (4, 3, 2, 1)),
    )
    count = 0
    for residue, modulus, large_prefix, small_prefix in families:
        for n in range(residue, limit + 1, modulus):
            assert valuation_prefix(n, 2) == large_prefix
            assert valuation_prefix(n - 2, 4) == small_prefix

            large, _ = normal_states(n, 3)
            small, _ = normal_states(n - 2, 5)
            assert large[3] == small[5]
            count += 1

    assert count == 139
    print(
        "GAPMRG2B gap-2 step-3 residue families: "
        "PASS (139 samples)"
    )


def check_gap_four_family(limit=50000):
    count = 0
    for n in range(2047, limit + 1, 4096):
        assert valuation_prefix(n, 1) == (12,)
        assert valuation_prefix(n - 4, 5) == (3, 1, 2, 3, 1)

        large, _ = normal_states(n, 2)
        small, _ = normal_states(n - 4, 6)
        assert large[2] == small[6]
        count += 1

    assert count == 12
    print("GAPMRG3 gap-4 family n=2047 mod 4096: PASS (12 samples)")


def check_gap_two_step_four_cylinders():
    expected = {
        (111, 8),
        (263, 9),
        (423, 10),
        (451, 10),
        (627, 11),
        (631, 11),
        (1795, 11),
        (383, 12),
        (731, 12),
        (1699, 12),
        (3257, 13),
        (6409, 13),
        (1889, 14),
        (4873, 14),
        (10889, 14),
        (969, 15),
        (6153, 15),
    }
    rows = first_hit_cylinders(step=4, max_total=24)
    assert {(row["residue"], row["depth"]) for row in rows} == expected
    assert all(row["valuation_gap"] == 2 for row in rows)

    for row in rows:
        for lift in range(3):
            n = row["residue"] + (lift << row["depth"])
            large, _ = normal_states(n, 4)
            small, _ = normal_states(n - 2, 6)
            assert large[3] != small[5]
            assert large[4] == small[6]

    print("GAPMRG5 gap-2 step-4 cylinders: PASS (17 exact families)")


def check_gap_two_tree_mass():
    expected_masses = {
        2: 262144,
        3: 233472,
        4: 176128,
        5: 138817,
        6: 110065,
        7: 91467,
    }
    seen = set()
    for step, expected in expected_masses.items():
        hits = residue_mass(first_hit_cylinders(step, 24), 24)
        assert len(hits) == expected
        assert not (seen & hits)
        seen |= hits
    assert len(seen) == 1012093
    print(
        "GAPMRG6 depth-24 synchronization-tree mass: PASS "
        "(steps 2..7, cumulative 1012093/8388608)"
    )


def main():
    check_collision_shells()
    check_gap_two_family()
    check_gap_two_step_three_families()
    check_gap_four_family()
    check_gap_two_step_four_cylinders()
    check_gap_two_tree_mass()
    print("GAPMRG: PASS")


if __name__ == "__main__":
    main()
