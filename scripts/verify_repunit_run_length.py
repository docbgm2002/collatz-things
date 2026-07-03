#!/usr/bin/env python3
"""Verify the fuel-enemy bridge identity and the run-length corollary.

For a repunit tail x_K = f^{(K)}(a_n), write the normal form

    x_K = (3^{n+K} + A_K) / 2^{E_K + 1},     R_K = A_K + 2^{E_K+1},
    R_K = 3^{r_K} d_K  (3 does not divide d_K),     m_K = n + K - r_K.

Two exact statements are checked at every step before first descent:

1. Fuel-enemy bridge:
        v2(x_K + 1) = v2(3^{m_K} + d_K) - E_K - 1.
   The left side is the trailing-ones fuel tau(x_K); the right side is the
   enemy 2-adic valuation minus the accumulated valuation.

2. Run-length corollary: a maximal valuation-one run starting at step K0 has
   length exactly
        L = v2(3^{m_{K0}} + d_{K0}) - E_{K0} - 2 = tau(x_{K0}) - 1,
   and the enemy coordinate (m, d) is invariant throughout the run.

These are exact identities, not finite heuristics.
"""

import argparse


def v2(value):
    return (value & -value).bit_length() - 1


def enemy_coordinate(n, K, E, A):
    R = A + (1 << (E + 1))
    r = 0
    d = R
    while d % 3 == 0:
        d //= 3
        r += 1
    return n + K - r, d


def verify(limit=151, factor=3):
    bridge_checks = 0
    run_checks = 0

    for n in range(3, limit + 1, 2):
        target = (1 << n) - 1
        x = (3**n - 1) // 2
        E = 0
        A = -1

        run_start = None
        run_len = 0
        run_enemy = None
        run_start_fuel = None

        K = 0
        while True:
            m, d = enemy_coordinate(n, K, E, A)
            enemy_val = v2(3**m + d)
            fuel = v2(x + 1)

            # Statement 1: fuel-enemy bridge.
            assert fuel == enemy_val - E - 1, (n, K, fuel, enemy_val, E)
            bridge_checks += 1

            value = 3 * x + 1
            e = v2(value)

            if e == 1:
                if run_start is None:
                    run_start = K
                    run_enemy = (m, d)
                    run_start_fuel = fuel
                    run_len = 0
                else:
                    # Statement 2 (invariance): (m, d) fixed inside the run.
                    assert (m, d) == run_enemy, (n, K)
                run_len += 1
            else:
                if run_start is not None:
                    expected = run_start_fuel - 1
                    assert run_len == expected, (n, run_start, run_len, expected)
                    run_checks += 1
                    run_start = None

            x = value >> e
            A = 3 * A + (1 << (E + 1))
            E += e
            K += 1

            if x < target:
                break

        # A run abutting first descent is not closed by a payout; ignore it.

    print(
        "RUNLEN fuel-enemy bridge and run-length corollary: PASS "
        f"(odd 3 <= n <= {limit}; {bridge_checks} bridge checks, "
        f"{run_checks} closed runs)"
    )


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=151)
    parser.add_argument("--factor", type=int, default=3)
    return parser.parse_args()


def main():
    args = parse_args()
    verify(args.limit, args.factor)


if __name__ == "__main__":
    main()
