#!/usr/bin/env python3
"""Independent finite checks for the nested-anchor calculations."""

from explore_mersenne_shortcut_budget import (
    ceiling_forces_descent,
    shortcut_tail_budget,
)
from explore_high_odd_repunit_prefixes import trace as trace_high_odd
from explore_nested_anchor_escape import (
    affine_image_for_prefix,
    first_descent_certificate,
)
from explore_shortcut_anchor_tree import (
    residue_certificate,
    shortcut,
    stopping_time,
)


def check_shortcut_anchor_identity():
    for a in range(1, 501):
        for k in range(1, 13):
            y = a
            odd_count = 0
            for _ in range(k):
                odd_count += y & 1
                y = shortcut(y)
            for m in (0, 1, 2, 7, 31):
                z = a + (1 << k) * m
                for _ in range(k):
                    z = shortcut(z)
                assert z == y + pow(3, odd_count) * m


def check_accelerated_anchor_identity():
    for x in range(3, 1000, 2):
        certificate = first_descent_certificate(x)
        for q in (0, 1, 2, 7, 31):
            affine_image_for_prefix(x, certificate, q)


def check_tree_equivalence():
    for K in range(1, 18):
        for r in range(3, 1 << K, 2):
            result = residue_certificate(r, K)
            concrete = stopping_time(r, K)
            assert (result["status"] == "proved") == (concrete is not None)
            if concrete is not None:
                assert result["step"] == concrete


def check_mersenne_budget_against_direct_shortcut():
    for n in range(7, 202, 2):
        target = (1 << n) - 1
        repunit = (3**n - 1) // 2
        row = shortcut_tail_budget(n, repunit)

        x = target
        direct_steps = 0
        while True:
            x = shortcut(x)
            direct_steps += 1
            if x < target:
                break

        assert direct_steps == row["full_shortcut"]
        assert row["full_shortcut"] == n + 1 + row["tail_shortcut"]


def check_odd_count_base_cases():
    for n in range(9, 18, 2):
        assert ceiling_forces_descent(n)


def check_enemy_coordinate_scaling_merger():
    row_937 = trace_high_odd(937, (3**937 - 1) // 2)
    row_939 = trace_high_odd(939, (3**939 - 1) // 2)
    enemy_937 = row_937["survivor_enemy"]
    enemy_939 = row_939["survivor_enemy"]
    assert (
        enemy_937["m"],
        enemy_937["d"],
        enemy_937["r"],
    ) == (
        enemy_939["m"],
        enemy_939["d"],
        enemy_939["r"],
    )
    gap = row_937["survivor_t"] - row_939["survivor_t"]
    assert gap == 2
    assert row_939["survivor_x"] == row_937["survivor_x"] << gap
    value = row_939["survivor_x"]
    for _ in range(gap):
        assert value % 2 == 0
        value = shortcut(value)
    assert value == row_937["survivor_x"]


def main():
    check_shortcut_anchor_identity()
    print("PASS shortcut anchor identity")
    check_accelerated_anchor_identity()
    print("PASS accelerated anchor identity")
    check_tree_equivalence()
    print("PASS tree/stopping-time equivalence")
    check_mersenne_budget_against_direct_shortcut()
    print("PASS Mersenne budget/direct-shortcut agreement")
    check_odd_count_base_cases()
    print("PASS odd-count exact base cases")
    check_enemy_coordinate_scaling_merger()
    print("PASS enemy-coordinate scaling merger")


if __name__ == "__main__":
    main()
