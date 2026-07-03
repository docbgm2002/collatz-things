#!/usr/bin/env python3
"""
Explore Collatz potential functions based on value and trailing-one fuel.

This is not a proof. It tests whether simple potentials of the form

    P_c(x) = log2(x) + c * tau(x)

where tau(x) = v2(x + 1), decrease across natural macro-steps. The goal is to
identify whether Block-Fracture-style "fuel burn" can be turned into a usable
Lyapunov function, and to collect the obstruction patterns when it cannot.
"""

import math
from collections import Counter


def v2(n):
    return (n & -n).bit_length() - 1 if n else 10**9


def f(x):
    t = 3 * x + 1
    return t >> v2(t)


def tau(x):
    """Trailing-one run length for odd x."""
    return v2(x + 1)


def rail(x):
    return x % 8


def potential(x, c):
    return math.log2(x) + c * tau(x)


def rail7_escape(x):
    """Compress a rail-7 episode into the first value not on rail 7."""
    assert x % 8 == 7
    cur = x
    odd_steps = 0
    while cur % 8 == 7:
        cur = f(f(cur))
        odd_steps += 2
    return cur, odd_steps


def first_descent_epoch(x, step_limit=10000):
    cur = x
    steps = 0
    while cur >= x and steps < step_limit:
        cur = f(cur)
        steps += 1
    return cur, steps


def fuel_macro(x):
    """One shortcut step, then immediately burn any rail-7 episode it creates."""
    cur = f(x)
    steps = 1
    if cur % 8 == 7:
        cur, extra = rail7_escape(cur)
        steps += extra
    return cur, steps


def burn_if_high_fuel(x, min_tau=3):
    """Burn a high trailing-one state if it lies on Rail 7."""
    if tau(x) >= min_tau and x % 8 == 7:
        return rail7_escape(x)
    return x, 0


def recharge_burn_macro(x, min_gain=2, step_limit=1000):
    """
    Follow shortcut steps until fuel increases by min_gain, then burn rail-7
    fuel if the recharge lands there. Return the resulting state.
    """
    start_tau = tau(x)
    cur = x
    steps = 0
    while steps < step_limit:
        cur = f(cur)
        steps += 1
        if tau(cur) >= start_tau + min_gain:
            burned, extra = burn_if_high_fuel(cur, min_tau=start_tau + min_gain)
            return burned, steps + extra, cur
        if cur < x:
            return cur, steps, None
    return cur, steps, None


def fixed_length_macro(x, length):
    cur = x
    for _ in range(length):
        cur = f(cur)
    return cur, length


def scan_c_for_rail7(max_y=20000):
    """Find the c interval that would force rail-7 escape potential descent."""
    lower = 0.0
    upper = float("inf")
    blockers = []

    for y in range(max_y + 1):
        x = 8 * y + 7
        end, steps = rail7_escape(x)
        dtau = tau(end) - tau(x)
        dlog = math.log2(end) - math.log2(x)

        # Need dlog + c*dtau < 0.
        if dtau > 0:
            upper = min(upper, -dlog / dtau)
        elif dtau < 0:
            lower = max(lower, dlog / (-dtau))
        else:
            if dlog >= 0:
                blockers.append((x, end, steps, dlog, tau(x), tau(end)))

    return lower, upper, blockers[:20]


def scan_fixed_c(c, max_x=200000):
    """Check P_c across first-descent epochs for odd x."""
    worst = (-10**9, None)
    failures = []
    by_rail = Counter()

    for x in range(3, max_x + 1, 2):
        end, steps = first_descent_epoch(x)
        delta = potential(end, c) - potential(x, c)
        if delta > worst[0]:
            worst = (delta, (x, end, steps, tau(x), tau(end), rail(x), rail(end)))
        if delta >= 0:
            failures.append((x, end, steps, delta, tau(x), tau(end), rail(x), rail(end)))
            by_rail[rail(x)] += 1

    return worst, failures[:20], by_rail, len(failures)


def scan_macro_c(c, max_x=200000):
    """Check P_c across one fuel macro for odd x."""
    worst = (-10**9, None)
    failures = []
    by_rail = Counter()

    for x in range(3, max_x + 1, 2):
        end, steps = fuel_macro(x)
        delta = potential(end, c) - potential(x, c)
        if delta > worst[0]:
            worst = (delta, (x, end, steps, tau(x), tau(end), rail(x), rail(end)))
        if delta >= 0:
            failures.append((x, end, steps, delta, tau(x), tau(end), rail(x), rail(end)))
            by_rail[rail(x)] += 1

    return worst, failures[:20], by_rail, len(failures)


def scan_recharge_burn(c, max_x=200000, min_gain=2):
    worst = (-10**9, None)
    failures = []
    by_rail = Counter()
    recharges = 0

    for x in range(3, max_x + 1, 2):
        end, steps, recharge = recharge_burn_macro(x, min_gain=min_gain)
        if recharge is not None:
            recharges += 1
        delta = potential(end, c) - potential(x, c)
        if delta > worst[0]:
            worst = (delta, (x, end, steps, recharge, tau(x), tau(end), rail(x), rail(end)))
        if delta >= 0:
            failures.append((x, end, steps, recharge, delta, tau(x), tau(end), rail(x), rail(end)))
            by_rail[rail(x)] += 1

    return worst, failures[:20], by_rail, len(failures), recharges


def scan_fixed_length(c, length, max_x=200000):
    worst = (-10**9, None)
    failures = []
    by_rail = Counter()

    for x in range(3, max_x + 1, 2):
        end, steps = fixed_length_macro(x, length)
        delta = potential(end, c) - potential(x, c)
        if delta > worst[0]:
            worst = (delta, (x, end, steps, tau(x), tau(end), rail(x), rail(end)))
        if delta >= 0:
            failures.append((x, end, steps, delta, tau(x), tau(end), rail(x), rail(end)))
            by_rail[rail(x)] += 1

    return worst, failures[:20], by_rail, len(failures)


def summarize():
    lower, upper, blockers = scan_c_for_rail7()
    print("Rail-7 escape potential P_c(x)=log2(x)+c*tau(x)")
    print(f"  c interval from sampled rail-7 escapes: lower={lower:.6f}, upper={upper:.6f}")
    if blockers:
        print("  blockers with dtau=0 and growth:")
        for row in blockers[:8]:
            print("   ", row)
    else:
        print("  no dtau=0 growth blockers in sample")

    print("\nFirst-descent epoch scan")
    for c in [0.0, 0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.75, 1.00]:
        worst, sample, by_rail, fail_count = scan_fixed_c(c)
        print(f"  c={c:.2f}: failures={fail_count}, worst_delta={worst[0]:+.6f}, worst={worst[1]}")
        if sample:
            print(f"       first failure: {sample[0]}; by rail={dict(by_rail)}")

    print("\nOne-step-plus-rail7-burn macro scan")
    for c in [0.0, 0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.75, 1.00]:
        worst, sample, by_rail, fail_count = scan_macro_c(c)
        print(f"  c={c:.2f}: failures={fail_count}, worst_delta={worst[0]:+.6f}, worst={worst[1]}")
        if sample:
            print(f"       first failure: {sample[0]}; by rail={dict(by_rail)}")

    print("\nRecharge-burn macro scan")
    for gain in [1, 2, 3, 4, 5]:
        print(f"  min fuel gain = {gain}")
        for c in [0.10, 0.25, 0.50, 0.64, 0.75, 1.00]:
            worst, sample, by_rail, fail_count, recharges = scan_recharge_burn(c, min_gain=gain)
            print(
                f"    c={c:.2f}: failures={fail_count}, recharges={recharges}, "
                f"worst_delta={worst[0]:+.6f}, worst={worst[1]}"
            )
            if sample:
                print(f"         first failure: {sample[0]}; by rail={dict(by_rail)}")

    print("\nFixed-length macro scan")
    for length in [2, 4, 8, 16, 32, 64]:
        best = None
        for c in [0.0, 0.05, 0.10, 0.20, 0.40, 0.64, 1.00]:
            worst, sample, by_rail, fail_count = scan_fixed_length(c, length)
            if best is None or fail_count < best[0]:
                best = (fail_count, c, worst)
        print(f"  length={length}: best failures={best[0]} at c={best[1]:.2f}, worst={best[2]}")


if __name__ == "__main__":
    summarize()
