#!/usr/bin/env python3
"""
Exploration: cumulative valuation debt for the post-Mersenne repunit tail.

For odd n, the Mersenne spine reaches a_n=(3^n-1)/2 after n odd-steps.
This script measures how the cumulative valuation

    E_K = sum_{i<K} v2(3 x_i + 1),   x_0 = a_n

pays off the initial height gap above 2^n-1.  Research tool, not a proof.
"""
import math


THETA = math.log2(3)
LAMBDA = math.log2(3 / 2)


def v2(n):
    return (n & -n).bit_length() - 1 if n else 10 ** 9


def f_with_e(x):
    t = 3 * x + 1
    e = v2(t)
    return t >> e, e


def a(n):
    return (3 ** n - 1) // 2


def log2_int(n):
    """High-accuracy log2 for huge positive integers."""
    bits = n.bit_length()
    if bits <= 1024:
        return math.log2(n)
    shift = bits - 1024
    top = n >> shift
    return shift + math.log2(top)


def repunit_tail(n, max_factor=8):
    target = 2 ** n - 1
    x = a(n)
    start = x
    E = 0
    rows = []
    max_x = x
    for K in range(1, max_factor * n + 1):
        x, e = f_with_e(x)
        E += e
        max_x = max(max_x, x)
        # Multiplicative ledger without the positive affine tail.
        raw_margin = E - THETA * K - (log2_int(start) - log2_int(target))
        exact_margin = log2_int(target) - log2_int(x)
        rows.append((K, e, E, raw_margin, exact_margin, x, max_x))
        if x < target:
            break
    return rows


def first_val_formula(limit=101):
    print("== First valuation from a_n ==")
    print("For odd n: v2(3 a_n + 1) = 1 + v2(n+1).")
    bad = []
    for n in range(3, limit + 1, 2):
        e = v2(3 * a(n) + 1)
        formula = 1 + v2(n + 1)
        if e != formula:
            bad.append((n, e, formula))
    print(f"  checked odd n=3..{limit}: {'PASS' if not bad else bad[:3]}")


def summary(limit=301):
    print("\n== Repunit tail cumulative ledger ==")
    header = (
        f"{'n':>4} {'sigma':>6} {'sig/n':>7} {'E':>5} {'E/K':>6} "
        f"{'needK':>7} {'raw':>8} {'exact':>8} {'max/e0':>9}"
    )
    print(header)
    worst_ratio = (0, 0)
    worst_slack = (10 ** 9, 0)
    for n in range(5, limit + 1, 2):
        rows = repunit_tail(n)
        K, _e, E, raw_margin, exact_margin, x, max_x = rows[-1]
        # Mean-model K needed to pay the initial gap:
        needK = (math.log2(a(n) / (2 ** n - 1))) / (2 - THETA)
        ratio = K / n
        if ratio > worst_ratio[0]:
            worst_ratio = (ratio, n)
        if raw_margin < worst_slack[0]:
            worst_slack = (raw_margin, n)
        print(
            f"{n:4d} {K:6d} {ratio:7.3f} {E:5d} {E/K:6.3f} "
            f"{needK/n:7.3f} {raw_margin:8.3f} {exact_margin:8.3f} "
            f"{max_x/a(n):9.3f}"
        )
    print(f"\n  worst sigma/n up to {limit}: {worst_ratio[0]:.3f} at n={worst_ratio[1]}")
    print(f"  smallest raw ledger margin at descent: {worst_slack[0]:.3f} at n={worst_slack[1]}")


def window_minima(limit=401, factors=(1.5, 2.0, 2.5, 3.0)):
    print("\n== Fixed linear windows: min cumulative surplus ==")
    print("raw surplus = E_K - log2(3)K - log2(a_n/(2^n-1)); ignores the affine tail")
    print("exact margin = log2((2^n-1)/x_K); positive means actual descent")
    print(f"{'c':>5} {'min raw':>12} {'min exact':>12} {'at n':>6} {'K':>6}")
    for c in factors:
        best = (10 ** 9, 10 ** 9, None, None)
        for n in range(11, limit + 1, 2):
            rows = repunit_tail(n, max_factor=max(4, int(c) + 2))
            idx = min(len(rows), max(1, int(c * n))) - 1
            K, _e, _E, raw_margin, exact_margin, _x, _max_x = rows[idx]
            if raw_margin < best[0]:
                best = (raw_margin, exact_margin, n, K)
        print(f"{c:5.2f} {best[0]:12.3f} {best[1]:12.3f} {best[2]:6d} {best[3]:6d}")


def quiet_range_check(limit=2001, factor=3):
    print(f"\n== Quiet range check: sigma(a_n) <= {factor}n? ==")
    worst = (0.0, 0, 0)
    bad = []
    min_margin = (10 ** 9, 0, 0)
    for n in range(5, limit + 1, 2):
        target = 2 ** n - 1
        rows = repunit_tail(n, max_factor=max(8, factor + 1))
        K, _e, _E, _raw_margin, exact_margin, _x, _max_x = rows[-1]
        if _x >= target:
            bad.append((n, "not found"))
            continue
        if K / n > worst[0]:
            worst = (K / n, n, K)
        if K > factor * n:
            bad.append((n, K))
        if exact_margin < min_margin[0]:
            min_margin = (exact_margin, n, K)
    print(f"  checked odd n=5..{limit}")
    print(f"  worst sigma/n = {worst[0]:.3f} at n={worst[1]} (sigma={worst[2]})")
    print(f"  exceptions above {factor}n or not found: {len(bad)}")
    if bad:
        print(f"  first exceptions: {bad[:5]}")
    print(
        f"  smallest exact margin at descent = {min_margin[0]:.6f} "
        f"at n={min_margin[1]} (sigma={min_margin[2]})"
    )


def extended_empirical_search(limit=20001, factor=3, checkpoint=2000, start=7):
    """Scan an explicit odd-exponent range and report finite diagnostics."""
    if start < 7 or start % 2 == 0 or limit < start or limit % 2 == 0:
        raise ValueError("start and limit must be odd, with 7 <= start <= limit")

    print(f"Extended empirical search: n = {start:,} to {limit:,} (odd)")
    print(
        f"{'n':>7} {'sigma':>7} {'ratio':>8} {'E_K':>6} "
        f"{'raw_margin':>12} {'exact':>12} status"
    )
    print("-" * 85)

    checked = 0
    failures = []
    records = []
    worst = (0.0, None)
    min_margin = (math.inf, None)

    for n in range(start, limit + 1, 2):
        target = 2 ** n - 1
        rows = repunit_tail(n, max_factor=factor)
        K, _e, E, raw_margin, exact_margin, x, _max_x = rows[-1]
        checked += 1

        if x >= target:
            failures.append(n)
            continue

        ratio = K / n
        status = ""
        if ratio > worst[0]:
            worst = (ratio, (n, K, E, raw_margin, exact_margin))
            records.append(worst[1])
            status = "*** NEW RECORD ***"
        if exact_margin < min_margin[0]:
            min_margin = (exact_margin, (n, K))

        if status or (checkpoint and n > start and (n - 1) % checkpoint == 0):
            print(
                f"{n:7d} {K:7d} {ratio:8.5f} {E:6d} "
                f"{raw_margin:12.4f} {exact_margin:12.6f} {status}"
            )

    print("-" * 85)
    print(f"\nResults for n = {start:,} to {limit:,}:")
    print(f"  Checked: {checked} odd values")
    if worst[1] is not None:
        n, K, _E, _raw, _exact = worst[1]
        print(f"  Worst sigma/n = {worst[0]:.6f} at n={n} (sigma={K})")
    if min_margin[1] is not None:
        n, K = min_margin[1]
        print(
            f"  Smallest exact margin = {min_margin[0]:.6f} "
            f"at n={n} (sigma={K})"
        )
    print(f"  Failures within {factor}n: {len(failures)}")
    if failures:
        print(f"  First failures: {failures[:10]}")
    print(f"  Record-breaking exponents: {len(records)}")
    print("\n  Record setters:")
    for n, K, _E, _raw, exact_margin in records:
        print(
            f"    n={n:5d}: sigma={K:7d}, ratio={K / n:.6f}, "
            f"exact_margin={exact_margin:.6f}"
        )


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "extended":
        extended_empirical_search(limit=20001, factor=3, checkpoint=2000)
    else:
        first_val_formula()
        summary(limit=201)
        window_minima(limit=201)
        quiet_range_check(limit=2001)
