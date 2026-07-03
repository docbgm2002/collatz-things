#!/usr/bin/env python3
"""
Explore the exact trailing-one fuse burn macro.

If odd x has tau(x)=L, then x = 2^L*m - 1 with m odd. For L>=2,

    f(x) = 3*2^(L-1)*m - 1,

so tau drops from L to L-1 exactly. After L-1 such shortcut steps the
trajectory reaches a tau=1 state, and the next shortcut step is the payout:

    2*(3^(L-1)*m) - 1  -> oddpart(3^L*m - 1).

This script explores whether burn+payout macros have usable drift.
"""

from collections import Counter


def v2(n):
    return (n & -n).bit_length() - 1 if n else 10**9


def oddpart(n):
    return n >> v2(n)


def f(x):
    return oddpart(3 * x + 1)


def tau(x):
    return v2(x + 1)


def burn_formula(x):
    L = tau(x)
    if L < 2:
        return x, 0
    m = (x + 1) >> L
    return (3 ** (L - 1)) * 2 * m - 1, L - 1


def burn_payout_formula(x):
    L = tau(x)
    m = (x + 1) >> L
    return oddpart((3**L) * m - 1), L, v2((3**L) * m - 1)


def fuse_map(x):
    """Global accelerated fuse map, valid for every odd x > 1."""
    return burn_payout_formula(x)


def verify_formula(limit=1_000_000):
    for x in range(3, limit + 1, 2):
        L = tau(x)
        cur = x
        if L >= 2:
            for _ in range(L - 1):
                cur = f(cur)
            predicted, steps = burn_formula(x)
            assert cur == predicted and steps == L - 1, (x, L, cur, predicted)
        cur = f(cur)
        predicted, steps, payout = burn_payout_formula(x)
        assert cur == predicted and steps == L, (x, L, cur, predicted, payout)
    print(f"Formula verification: PASS for odd x <= {limit}")


def scan_burn_payout(max_L=40, max_m=5000):
    print("L count desc pct_desc worst_ratio worst_m payout_v2_counts")
    for L in range(2, max_L + 1):
        count = desc = 0
        worst_ratio = 0.0
        worst_m = None
        payouts = Counter()
        for m in range(1, max_m + 1, 2):
            x = (1 << L) * m - 1
            y, steps, payout = burn_payout_formula(x)
            ratio = y / x
            count += 1
            desc += y < x
            payouts[payout] += 1
            if ratio > worst_ratio:
                worst_ratio = ratio
                worst_m = m
        print(
            L,
            count,
            desc,
            f"{100*desc/count:6.2f}",
            f"{worst_ratio:10.6f}",
            worst_m,
            payouts.most_common(6),
        )


def transition_stats(max_L=24, max_m=20000):
    print("\nTransition stats by initial tau L")
    print("L avg_log2_ratio avg_next_tau top_(payout,next_tau)")
    for L in range(2, max_L + 1):
        total_log_ratio = 0.0
        total_next_tau = 0
        pairs = Counter()
        count = 0
        for m in range(1, max_m + 1, 2):
            x = (1 << L) * m - 1
            y, _, payout = burn_payout_formula(x)
            # Avoid importing math for one log call? Do it here.
            import math

            total_log_ratio += math.log2(y / x)
            nt = tau(y)
            total_next_tau += nt
            pairs[(payout, nt)] += 1
            count += 1
        print(
            L,
            f"{total_log_ratio / count:+.6f}",
            f"{total_next_tau / count:.3f}",
            pairs.most_common(8),
        )


def find_growth_chains(max_start=200_000, chain_limit=50):
    """Track repeated fuse-map macros while value has not descended."""
    worst = (0, None)
    examples = []
    for x in range(3, max_start + 1, 2):
        cur = x
        chain = []
        while cur > 1 and len(chain) < chain_limit and cur >= x:
            nxt, steps, payout = burn_payout_formula(cur)
            chain.append((cur, tau(cur), nxt, tau(nxt), payout, nxt / cur))
            cur = nxt
        if len(chain) > worst[0]:
            worst = (len(chain), x, chain)
        if chain and cur >= x and tau(cur) >= 2:
            examples.append((x, chain[:5]))
    print(f"Longest non-descending burn chain <= {max_start}: length {worst[0]} at x={worst[1]}")
    for row in worst[2][:12]:
        print("  ", row)
    print(f"Still active after chain limit examples: {len(examples)}")


def growth_chain_records(max_start=1_000_000, min_growth_ratio=1.0):
    """Summarize fuse-map chains that keep value from descending."""
    length_counts = Counter()
    max_length = 0
    max_record = None
    total_growth_steps = Counter()

    for x in range(3, max_start + 1, 2):
        cur = x
        chain = []
        while cur > 1 and cur >= x:
            nxt, _, payout = burn_payout_formula(cur)
            ratio = nxt / cur
            chain.append((tau(cur), payout, tau(nxt), ratio))
            total_growth_steps[(tau(cur), payout, tau(nxt))] += ratio >= min_growth_ratio
            cur = nxt
            if len(chain) > 100:
                break
        length_counts[len(chain)] += 1
        if len(chain) > max_length:
            max_length = len(chain)
            max_record = (x, chain, cur)

    print(f"\nGrowth-chain distribution up to {max_start}")
    print("  lengths:", length_counts.most_common(20))
    print(f"  max length: {max_length} at x={max_record[0]}, terminal={max_record[2]}")
    for i, row in enumerate(max_record[1], 1):
        print(f"    {i:02d}: L={row[0]}, payout={row[1]}, next_tau={row[2]}, ratio={row[3]:.6f}")


if __name__ == "__main__":
    verify_formula()
    scan_burn_payout()
    transition_stats()
    find_growth_chains()
    growth_chain_records()
