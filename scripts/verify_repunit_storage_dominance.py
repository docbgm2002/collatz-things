#!/usr/bin/env python3
"""Finite check of first-descent storage-dominance (Avenue A).

For every odd repunit exponent n in the stated range, through and including
the first accelerated step with x_i < 2^n - 1, verify

    0 < R_i < 3^{n+i},

where R_0 = 1 and R_{i+1} = 3 R_i + 2^{E_i+1}(2^{e_i}-2).

This is a finite certificate, not a proof of the universal lemma.
"""

from __future__ import annotations

import argparse


def v2(value: int) -> int:
    return (value & -value).bit_length() - 1


def scan_tail(n: int, step_limit: int = 200_000) -> dict[str, int]:
    threshold = (1 << n) - 1
    x = (3**n - 1) // 2
    E = 0
    R = 1
    min_slack = None
    min_slack_step = 0
    # Maximize theta = R/bound by comparing cross-products.
    max_R = 1
    max_bound = 3**n
    max_theta_step = 0

    for step in range(0, step_limit + 1):
        bound = 3 ** (n + step)
        assert R > 0, (n, step, R)
        assert R < bound, (n, step, R, bound)
        # Optional stronger finite probe used in the Avenue A note.
        assert 27 * R <= 5 * bound, (n, step, R, bound)
        slack = bound - R
        if min_slack is None or slack < min_slack:
            min_slack = slack
            min_slack_step = step
        if R * max_bound > max_R * bound:
            max_R = R
            max_bound = bound
            max_theta_step = step

        if step > 0 and x < threshold:
            return {
                "n": n,
                "descent_step": step,
                "min_slack": min_slack,
                "min_slack_step": min_slack_step,
                "max_R": max_R,
                "max_bound": max_bound,
                "max_theta_step": max_theta_step,
            }

        value = 3 * x + 1
        e = v2(value)
        R = 3 * R + (1 << (E + 1)) * ((1 << e) - 2)
        E += e
        x = value >> e

    raise RuntimeError(f"no descent within step limit for n={n}")


def verify(limit: int) -> None:
    worst_slack = None
    worst_slack_n = 3
    max_R = 1
    max_bound = 3**3
    max_theta_n = 3
    max_descent = 0
    max_descent_n = 3
    worst_k_over_t_n = 3
    worst_k_over_t_num = 0
    worst_k_over_t_den = 1

    for n in range(3, limit + 1, 2):
        row = scan_tail(n)
        threshold = (1 << n) - 1
        k_down = row["descent_step"]
        assert k_down <= threshold, (n, k_down, threshold)
        if k_down * worst_k_over_t_den > worst_k_over_t_num * threshold:
            worst_k_over_t_num = k_down
            worst_k_over_t_den = threshold
            worst_k_over_t_n = n
        if worst_slack is None or row["min_slack"] < worst_slack:
            worst_slack = row["min_slack"]
            worst_slack_n = n
        if row["max_R"] * max_bound > max_R * row["max_bound"]:
            max_R = row["max_R"]
            max_bound = row["max_bound"]
            max_theta_n = n
        if k_down > max_descent:
            max_descent = k_down
            max_descent_n = n

    # max_R/max_bound is the global max theta; compare to 5/27 from n=3.
    assert 27 * max_R <= 5 * max_bound
    print("Storage-dominance through first descent: PASS")
    print(f"domain: odd 3 <= n <= {limit}")
    print(f"worst absolute slack={worst_slack} at n={worst_slack_n}")
    print(
        "max theta = R/3^(n+i) realised at n="
        f"{max_theta_n}; integer check 27R <= 5*bound holds "
        "(matches the n=3 prototype theta=5/27)"
    )
    print(f"longest first descent={max_descent} steps at n={max_descent_n}")
    print(
        "K_down <= T gate: PASS "
        f"(worst K/T at n={worst_k_over_t_n}: "
        f"{worst_k_over_t_num}/{worst_k_over_t_den})"
    )


def gamma(n: int) -> int:
    t = (1 << n) - 1
    return (3**n - 1) * t - (1 << (n - 1)) * (3**n + 1)


def check_stay_reduction(limit: int) -> None:
    """Check SD1S, SD½, strong slack, and SD½P on stay-above payouts."""
    stay_checked = 0
    strong_checked = 0
    half_checked = 0
    mass_checked = 0
    max_half_num = 0
    max_half_den = 1
    max_half_n = 3
    for n in range(3, limit + 1, 2):
        assert gamma(n) > 0
        threshold = (1 << n) - 1
        x = (3**n - 1) // 2
        E = 0
        R = 1
        for step in range(0, 200_000):
            bound = 3 ** (n + step)
            sigma = bound - (x + 1) * (1 << E)
            assert sigma > 0
            assert sigma * (1 << n) > bound  # SD1+
            strong_checked += 1
            # SD½: sigma > 3^step
            assert sigma > 3**step
            half_u = (3**step) * (3**n - 1)
            half_lhs = (x + 1) << E
            assert half_lhs < half_u
            half_checked += 1
            if half_lhs * max_half_den > max_half_num * half_u:
                max_half_num = half_lhs
                max_half_den = half_u
                max_half_n = n
            if step > 0 and x < threshold:
                assert x != 1
                break
            value = 3 * x + 1
            e = v2(value)
            nxt = value >> e
            if e >= 2 and nxt >= threshold:
                assert 3 ** (n + step + 1) < (1 << n) * (
                    3 * sigma + (1 << (E + 1))
                )
                stay_checked += 1
                payout_mass = R - 3**step
                assert payout_mass >= 0
                # SD½P and the stronger SD½P⁻ (drop 2^{E+n+1})
                assert (3 ** (step + 1)) * gamma(n) + (
                    1 << (E + n + 1)
                ) > 3 * (1 << (n - 1)) * payout_mass
                assert (payout_mass << (n - 1)) < (3**step) * gamma(n)
                mass_checked += 1
                assert x != threshold  # observed barrier used in IH attempts
            R = 3 * R + (1 << (E + 1)) * ((1 << e) - 2)
            E += e
            x = nxt
        else:
            raise RuntimeError(f"no descent within step limit for n={n}")

    print(
        "SD1S/SD½/SD½P stay reductions: PASS "
        f"(stay={stay_checked}, mass={mass_checked}, "
        f"half-states={half_checked}, strong={strong_checked}; "
        f"odd 3 <= n <= {limit})"
    )
    print(
        f"worst SD½ ratio at n={max_half_n} "
        f"(prototype n=3 has phi=16/13)"
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=5001)
    parser.add_argument(
        "--check-stay",
        action="store_true",
        help="also verify SD1S and the strong slack bound",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    verify(args.limit)
    if args.check_stay:
        check_stay_reduction(args.limit)
