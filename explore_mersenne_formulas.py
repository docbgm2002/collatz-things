#!/usr/bin/env python3
"""
Probe exact valuation formulas on the Mersenne spine.

For M_L = 2^L - 1, the first fuse-map step is

    Phi(M_L) = oddpart(3^L - 1).

This script explores the next few fuse-map valuations as functions of L,
looking for LTE-style formulas.
"""

from collections import defaultdict

from explore_fuse_burn import tau, burn_payout_formula, v2

LOG32_NUM = 5849625007211562  # approx log2(3/2) * 1e16
LOG32_DEN = 10_000_000_000_000_000


def first_step_formula(L):
    s = v2(3**L - 1)
    x1 = (3**L - 1) >> s
    return s, tau(x1), x1


def spine_terms(L, count=8):
    cur = (1 << L) - 1
    rows = []
    for _ in range(count):
        nxt, _, payout = burn_payout_formula(cur)
        rows.append(
            {
                "x": cur,
                "L": tau(cur),
                "s": payout,
                "next_L": tau(nxt),
                "ratio_num": nxt,
                "ratio_den": cur,
            }
        )
        cur = nxt
    return rows


def ledger_until_compensated(L, max_terms=10000):
    """Return first prefix whose payout ledger beats log2(3/2)*fuel ledger."""
    cur = (1 << L) - 1
    sum_L = 0
    sum_s = 0
    rows = []
    for i in range(1, max_terms + 1):
        nxt, _, payout = burn_payout_formula(cur)
        Li = tau(cur)
        sum_L += Li
        sum_s += payout
        rows.append((Li, payout, tau(nxt)))
        if sum_s * LOG32_DEN > sum_L * LOG32_NUM:
            return i, sum_L, sum_s, rows, nxt
        cur = nxt
    return None, sum_L, sum_s, rows, cur


def summarize(max_L=96):
    print("First Mersenne fuse step")
    print("L parity v2(L) s1 next_L predicted_next_L")
    for L in range(2, max_L + 1):
        s, next_L, _ = first_step_formula(L)
        if L % 2:
            predicted = v2(L) + 1  # v2((3^L+1)/2)
        else:
            predicted = None
        print(L, L % 2, v2(L), s, next_L, predicted)


def group_second_terms(max_L=200):
    groups = defaultdict(list)
    for L in range(2, max_L + 1):
        rows = spine_terms(L, 4)
        key = (L % 2, v2(L), rows[0]["s"], rows[0]["next_L"])
        groups[key].append((L, [(r["L"], r["s"], r["next_L"]) for r in rows]))

    print("\nGrouped first-step signatures")
    for key, vals in sorted(groups.items(), key=lambda kv: (kv[0], kv[1][0][0])):
        sample = vals[:5]
        print("KEY", key, "count", len(vals), "sample", sample)


def even_compensation_summary(max_L=512):
    print("\nEven Mersenne compensation windows")
    print("L v2L first_next_tau terms sum_L sum_s margin terminal_ratio first_terms")
    for L in range(2, max_L + 1, 2):
        terms, sum_L, sum_s, rows, terminal = ledger_until_compensated(L)
        start = (1 << L) - 1
        margin = sum_s - (sum_L * LOG32_NUM / LOG32_DEN)
        first_next_tau = rows[0][2]
        print(
            L,
            v2(L),
            first_next_tau,
            terms,
            sum_L,
            sum_s,
            f"{margin:+.6f}",
            f"{terminal/start:.6e}",
            rows[:12],
        )


if __name__ == "__main__":
    summarize()
    group_second_terms()
    even_compensation_summary()
