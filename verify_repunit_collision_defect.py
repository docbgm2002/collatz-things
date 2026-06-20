#!/usr/bin/env python3
"""Verify the exact recurrence and explicit non-closure counterexample."""

from explore_repunit_collision_defect import aligned_rows, relative_state, trace_normal


def check_recurrence():
    checked = 0
    for gap in (2, 4, 6):
        for n in range(31, 202, 2):
            rows = aligned_rows(n, gap, 32)
            checked += len(rows)
    assert checked == 7638
    print(f"COLDEF1 normalized recurrence: PASS ({checked} transitions)")


def check_nonclosure_counterexample():
    cases = (
        # n, gap, aligned large-tail step, expected outgoing pair
        (3259, 2, 61, (1, 2)),
        (3261, 2, 59, (3, 1)),
    )
    relative = []
    corrections = []

    for n, gap, step, expected_pair in cases:
        left, left_vals = trace_normal(n, step + 1)
        right, right_vals = trace_normal(n - gap, step + gap + 1)
        state = relative_state(left[step], right[step + gap])
        relative.append((n + step, left[step][1], right[step + gap][1], *state[:2]))
        corrections.append((left[step][2], right[step + gap][2]))
        assert (left_vals[step], right_vals[step + gap]) == expected_pair

    assert relative[0] == relative[1] == (3320, 128, 128, 0, -6)
    assert corrections[0] != corrections[1]
    print(
        "COLDEF2 non-closure counterexample: PASS "
        "(same d,E,F,delta,z; outgoing pairs (1,2) and (3,1))"
    )


def main():
    check_recurrence()
    check_nonclosure_counterexample()
    print("COLDEF: PASS")


if __name__ == "__main__":
    main()
