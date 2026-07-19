#!/usr/bin/env python3
"""Test every aligned smaller-exponent descent-transfer comparator.

For odd n and every even gap 2 <= g <= n-3, let s be the first time the
(n-g)-tail falls below M_{n-g}.  If s >= g, test the exact certificate

    x_{s-g}(n) <= 2^g x_s(n-g) + (2^g-1).

Unlike the earlier bounded-fan diagnostic, this script tests every possible
positive smaller odd repunit exponent.  It reports only exact integer
inequalities; the census is evidence about coverage, not a universal proof.
"""

from __future__ import annotations

import argparse


def v2(value: int) -> int:
    return (value & -value).bit_length() - 1


def first_descent(n: int) -> tuple[int, int, int]:
    x = (3**n - 1) // 2
    threshold = (1 << n) - 1
    cumulative = 0
    for step in range(1, 200_000):
        value = 3 * x + 1
        valuation = v2(value)
        cumulative += valuation
        x = value >> valuation
        if x < threshold:
            return step, x, cumulative
    raise RuntimeError(f"no descent found within step limit for n={n}")


def trajectory_prefix(n: int, length: int) -> tuple[list[int], list[int]]:
    x = (3**n - 1) // 2
    result = [x]
    cumulative = [0]
    for _ in range(length):
        value = 3 * x + 1
        valuation = v2(value)
        x = value >> valuation
        result.append(x)
        cumulative.append(cumulative[-1] + valuation)
    return result, cumulative


def census(limit: int) -> dict[str, object]:
    descents = {
        n: first_descent(n)
        for n in range(3, limit + 1, 2)
    }
    gap_two_wins = 0
    rescued: list[tuple[int, int]] = []
    failures: list[int] = []
    sign_table = {
        (False, False): 0,
        (False, True): 0,
        (True, False): 0,
        (True, True): 0,
    }
    sign_mismatches: list[tuple[int, int, int, bool]] = []

    for n in range(9, limit + 1, 2):
        comparators = []
        for gap in range(2, n - 1, 2):
            step, state, cumulative = descents[n - gap]
            if step >= gap:
                comparators.append((gap, step, state, cumulative))

        if not comparators:
            failures.append(n)
            continue

        max_time = max(step - gap for gap, step, _, _ in comparators)
        high, high_cumulative = trajectory_prefix(n, max_time)
        wins = []
        for gap, step, low_state, low_cumulative in comparators:
            high_time = step - gap
            win = (
                high[high_time]
                <= (low_state << gap) + ((1 << gap) - 1)
            )
            surplus_difference = (
                low_cumulative - step
                - (high_cumulative[high_time] - high_time)
            )
            nonpositive = surplus_difference <= 0
            sign_table[(nonpositive, win)] += 1
            if nonpositive != win:
                sign_mismatches.append(
                    (n, gap, surplus_difference, win)
                )
            if win:
                wins.append(gap)

        if 2 in wins:
            gap_two_wins += 1
        elif wins:
            rescued.append((n, min(wins)))
        else:
            failures.append(n)

    return {
        "tested": len(range(9, limit + 1, 2)),
        "gap_two_wins": gap_two_wins,
        "rescued": rescued,
        "failures": failures,
        "sign_table": sign_table,
        "sign_mismatches": sign_mismatches,
    }


def print_report(limit: int) -> None:
    result = census(limit)
    rescued = result["rescued"]
    failures = result["failures"]
    covered = result["gap_two_wins"] + len(rescued)

    print("== Full repunit descent-transfer fan ==")
    print(f"domain: odd 9 <= n <= {limit}; tested={result['tested']}")
    print(
        f"gap-two wins={result['gap_two_wins']}; "
        f"rescued by a larger gap={len(rescued)}; "
        f"all-gap failures={len(failures)}; "
        f"coverage={covered / result['tested']:.4%}"
    )
    print(
        "rescues requiring gap > 80="
        f"{sum(gap > 80 for _, gap in rescued)}; "
        f"largest minimum successful gap="
        f"{max((gap for _, gap in rescued), default=None)}"
    )
    print("gap>80 rescues:", [row for row in rescued if row[1] > 80])
    print("all-gap failures:", failures)
    print("surplus-sign table ((H<=0, win): count):", result["sign_table"])
    print("surplus-sign mismatches:", result["sign_mismatches"])


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=5001)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    print_report(args.limit)
