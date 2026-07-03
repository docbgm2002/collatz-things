#!/usr/bin/env python3
"""
Exploration: tight exact descent margins for repunit tails.

For odd n, x_0 = a_n = (3^n - 1)/2. This scans first descent below
2^n - 1 and records the smallest exact log margins.
"""
import argparse
import heapq
import math

THETA = math.log2(3)


def v2(n):
    return (n & -n).bit_length() - 1 if n else 10 ** 9


def f_with_e(x):
    t = 3 * x + 1
    e = v2(t)
    return t >> e, e


def a(n):
    return (3 ** n - 1) // 2


def log2_int(n):
    bits = n.bit_length()
    if bits <= 1024:
        return math.log2(n)
    shift = bits - 1024
    top = n >> shift
    return shift + math.log2(top)


def tail_summary(n, max_factor=4, keep_rows=False):
    target = 2 ** n - 1
    x = a(n)
    start_log_gap = log2_int(x) - log2_int(target)
    E = 0
    rows = []
    max_x = x
    for K in range(1, max_factor * n + 1):
        x, e = f_with_e(x)
        E += e
        if x > max_x:
            max_x = x
        raw_margin = E - THETA * K - start_log_gap
        exact_margin = log2_int(target) - log2_int(x)
        if keep_rows:
            rows.append((K, e, E, raw_margin, exact_margin, x.bit_length()))
        if x < target:
            return {
                "n": n,
                "sigma": K,
                "ratio": K / n,
                "E": E,
                "raw_margin": raw_margin,
                "exact_margin": exact_margin,
                "max_ratio_log2": log2_int(max_x) - log2_int(a(n)),
                "rows": rows,
            }
    return None


def scan(limit, top, max_factor):
    tight = []
    worst_ratio = (0.0, None)
    failures = []
    for n in range(5, limit + 1, 2):
        result = tail_summary(n, max_factor=max_factor)
        if result is None:
            failures.append(n)
            continue
        item = (-result["exact_margin"], result["n"], result)
        if len(tight) < top:
            heapq.heappush(tight, item)
        elif result["exact_margin"] < -tight[0][0]:
            heapq.heapreplace(tight, item)
        if result["ratio"] > worst_ratio[0]:
            worst_ratio = (result["ratio"], result)
    return sorted((item[2] for item in tight), key=lambda r: r["exact_margin"]), worst_ratio, failures


def print_tight_table(tight):
    print("== Tightest exact descent margins ==")
    print(f"{'rank':>4} {'n':>7} {'sigma':>7} {'sig/n':>8} {'E':>7} {'raw':>12} {'exact':>12} {'maxlog':>10}")
    print("-" * 82)
    for i, r in enumerate(tight, 1):
        print(
            f"{i:4d} {r['n']:7d} {r['sigma']:7d} {r['ratio']:8.5f} "
            f"{r['E']:7d} {r['raw_margin']:12.6f} {r['exact_margin']:12.6f} "
            f"{r['max_ratio_log2']:10.3f}"
        )


def run_lengths(values, target=1):
    best = []
    i = 0
    while i < len(values):
        if values[i] != target:
            i += 1
            continue
        j = i
        while j < len(values) and values[j] == target:
            j += 1
        best.append((j - i, i + 1, j))
        i = j
    return sorted(best, reverse=True)


def detail_case(n, window, max_factor):
    result = tail_summary(n, max_factor=max_factor, keep_rows=True)
    if result is None:
        print(f"\nNo descent found for n={n} within {max_factor}n")
        return
    rows = result["rows"]
    vals = [row[1] for row in rows]
    long_ones = run_lengths(vals, target=1)[:8]
    large_payouts = sorted((row for row in rows if row[1] >= 6), key=lambda r: (-r[1], r[0]))[:12]
    print(f"\n== Detail n={n} ==")
    print(
        f"sigma={result['sigma']}, ratio={result['ratio']:.6f}, E={result['E']}, "
        f"raw={result['raw_margin']:.6f}, exact={result['exact_margin']:.6f}, "
        f"maxlog={result['max_ratio_log2']:.3f}"
    )
    print("\nLongest valuation-one runs: length, first K, last K")
    for length, first, last in long_ones:
        print(f"  {length:4d} {first:7d} {last:7d}")
    print("\nLargest payouts: K, e_K, E_K, raw, exact")
    for K, e, E, raw, exact, bits in large_payouts:
        print(f"  {K:7d} {e:4d} {E:7d} {raw:12.6f} {exact:12.6f}")
    print(f"\nLast {window} rows before descent: K, e_K, E_K, raw, exact, bitlen(x_K)")
    for K, e, E, raw, exact, bits in rows[-window:]:
        print(f"  {K:7d} {e:4d} {E:7d} {raw:12.6f} {exact:12.6f} {bits:8d}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=20001)
    parser.add_argument("--top", type=int, default=20)
    parser.add_argument("--window", type=int, default=80)
    parser.add_argument("--max-factor", type=int, default=4)
    parser.add_argument("--detail", type=int, nargs="*", default=[])
    args = parser.parse_args()

    tight, worst_ratio, failures = scan(args.limit, args.top, args.max_factor)
    print_tight_table(tight)
    print("\n== Ratio record within scan ==")
    r = worst_ratio[1]
    print(
        f"n={r['n']}, sigma={r['sigma']}, sigma/n={r['ratio']:.6f}, "
        f"exact_margin={r['exact_margin']:.6f}"
    )
    print(f"Failures within {args.max_factor}n: {len(failures)}")
    if failures:
        print(f"First failures: {failures[:10]}")

    detail_ns = args.detail or [tight[0]["n"], tight[1]["n"], tight[2]["n"], r["n"]]
    for n in dict.fromkeys(detail_ns):
        detail_case(n, args.window, args.max_factor)


if __name__ == "__main__":
    main()
