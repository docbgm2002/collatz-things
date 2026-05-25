#!/usr/bin/env python3
"""
Explore the Mersenne spine under the global fuse map.

The fuse-map obstruction is sharpest at x = 2^L - 1. This script records the
sequence of fuse lengths and payout valuations until the orbit first falls
below the Mersenne start.
"""

from explore_fuse_burn import tau, burn_payout_formula


def mersenne_spine(L, limit=10000):
    start = (1 << L) - 1
    cur = start
    rows = []
    while cur >= start and len(rows) < limit:
        nxt, _, payout = burn_payout_formula(cur)
        rows.append((cur, tau(cur), payout, tau(nxt), nxt, nxt / cur))
        cur = nxt
    return start, cur, rows


def summarize(max_L=80):
    print("L start_bits episodes terminal_ratio max_tau sum_L sum_s first_terms")
    for L in range(2, max_L + 1):
        start, terminal, rows = mersenne_spine(L)
        max_tau = max(row[1] for row in rows)
        sum_L = sum(row[1] for row in rows)
        sum_s = sum(row[2] for row in rows)
        first_terms = [(row[1], row[2], row[3]) for row in rows[:10]]
        print(
            L,
            start.bit_length(),
            len(rows),
            f"{terminal/start:.6f}",
            max_tau,
            sum_L,
            sum_s,
            first_terms,
        )


if __name__ == "__main__":
    summarize()
