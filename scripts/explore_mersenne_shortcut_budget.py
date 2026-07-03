#!/usr/bin/env python3
"""
Measure the exact shortcut-step budget of odd Mersenne trajectories.

Let

    U(n) = n/2       (n even),
           (3n+1)/2 (n odd).

For odd exponent n, M_n=2^n-1 reaches a_n=(3^n-1)/2 after exactly n+1
shortcut steps.  Starting from a_n, an accelerated odd episode with valuation
e=v2(3x+1) is exactly e shortcut steps: one odd shortcut followed by e-1 even
shortcuts.

The finite target tested here is

    H(n) <= 5n-2,

where H(n) is the number of shortcut steps from a_n to the first value below
2^n-1.  Equivalently, the full Mersenne stopping time is at most 6n-1.

This is an exact finite diagnostic, not a universal proof.
"""

import argparse
from fractions import Fraction


def v2(value):
    return (value & -value).bit_length() - 1


def shortcut_tail_budget(n, repunit):
    target = (1 << n) - 1
    x = repunit
    accelerated_steps = 0
    completed_valuation = 0
    shortcut_steps = 0
    valuations = []

    while x >= target:
        raw = 3 * x + 1
        e = v2(raw)
        valuations.append(e)
        accelerated_steps += 1

        for division in range(1, e + 1):
            shortcut_steps += 1
            candidate = raw >> division
            if candidate < target:
                return {
                    "n": n,
                    "tail_shortcut": shortcut_steps,
                    "full_shortcut": n + 1 + shortcut_steps,
                    "accelerated_steps": accelerated_steps,
                    "completed_valuation": completed_valuation,
                    "crossing_valuation": e,
                    "crossing_division": division,
                    "endpoint": candidate,
                    "valuations": tuple(valuations),
                }

        completed_valuation += e
        x = raw >> e

    raise AssertionError("unreachable")


def scan(limit):
    records = []
    best_ratio = -1.0
    max_slack_record = None
    repunit = (3**7 - 1) // 2

    for n in range(7, limit + 1, 2):
        if n > 7:
            repunit = 9 * repunit + 4
        row = shortcut_tail_budget(n, repunit)
        assert row["full_shortcut"] == n + 1 + row["tail_shortcut"]
        assert row["tail_shortcut"] <= 5 * n - 2
        assert row["full_shortcut"] <= 6 * n - 1

        ratio = row["full_shortcut"] / n
        if ratio > best_ratio:
            best_ratio = ratio
            records.append(row)

        slack = 5 * n - 2 - row["tail_shortcut"]
        if max_slack_record is None or slack < max_slack_record[0]:
            max_slack_record = (slack, row)

    return records, max_slack_record


def ceiling_forces_descent(n):
    """
    Verify exactly that rho <= floor(11n/4) odd shortcut steps cannot keep the
    repunit tail above target through t=5n-2 steps.

    Before descent, every odd state is at least T=2^n-1, so the affine product
    is at most (1+1/(3T))^rho.
    """
    target = (1 << n) - 1
    repunit = (3**n - 1) // 2
    t = 5 * n - 2
    rho = 11 * n // 4
    upper_ratio = (
        Fraction(repunit, target)
        * Fraction(3**rho, 1 << t)
        * Fraction(3 * target + 1, 3 * target) ** rho
    )
    return upper_ratio < 1


def verify_odd_count_base_cases():
    """Exact finite base cases for the analytic n>=19 reduction."""
    for n in range(9, 18, 2):
        assert ceiling_forces_descent(n), n


def compact(values, width=28):
    if len(values) <= width:
        return ",".join(map(str, values))
    half = width // 2
    return (
        ",".join(map(str, values[:half]))
        + ",...,"
        + ",".join(map(str, values[-half:]))
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=10001)
    args = parser.parse_args()

    records, tightest = scan(args.limit)
    verify_odd_count_base_cases()
    print("== Odd-Mersenne shortcut budget ==")
    print(f"finite domain: odd 7 <= n <= {args.limit}")
    print("tested target: tail H(n) <= 5n-2; full stopping <= 6n-1")
    print(
        "odd-count reduction: exact base cases n=9..17; "
        "analytic envelope applies for n>=19"
    )
    print()
    print("record full stopping-time ratios:")
    for row in records:
        print(
            f"  n={row['n']:5d} full={row['full_shortcut']:6d} "
            f"full/n={row['full_shortcut']/row['n']:.8f} "
            f"tail={row['tail_shortcut']:6d} "
            f"accelerated={row['accelerated_steps']:6d}"
        )

    slack, row = tightest
    print()
    print(
        f"tightest 5n-2 tail budget: n={row['n']} "
        f"H={row['tail_shortcut']} allowance={5*row['n']-2} slack={slack}"
    )
    print(
        f"  crossing episode: e={row['crossing_valuation']} "
        f"division={row['crossing_division']} "
        f"completed valuation={row['completed_valuation']}"
    )
    print(f"  valuation word: {compact(row['valuations'])}")
    print()
    print("PASS (finite certificate only)")


if __name__ == "__main__":
    main()
