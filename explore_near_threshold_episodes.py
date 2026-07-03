#!/usr/bin/env python3
"""
Focused diagnostic for near-threshold repunit-tail episodes.

This is not a range search. It inspects named exponents whose first-descent
margin is unusually tight and records the orbit segment after it first enters
a narrow band below the Mersenne target.
"""
import argparse
import math
from collections import Counter


THETA = math.log2(3)


def v2(value):
    return (value & -value).bit_length() - 1 if value else 10**9


def f_with_e(x):
    value = 3 * x + 1
    e = v2(value)
    return value >> e, e


def a(n):
    return (3**n - 1) // 2


def log2_int(value):
    bits = value.bit_length()
    if bits <= 1024:
        return math.log2(value)
    shift = bits - 1024
    top = value >> shift
    return shift + math.log2(top)


def run_lengths(values, target=1):
    runs = []
    start = None
    for index, value in enumerate(values, 1):
        if value == target and start is None:
            start = index
        elif value != target and start is not None:
            runs.append((index - start, start, index - 1))
            start = None
    if start is not None:
        runs.append((len(values) + 1 - start, start, len(values)))
    return sorted(runs, reverse=True)


def tail_rows(n, max_factor):
    target = 2**n - 1
    x = a(n)
    start_gap = log2_int(x) - log2_int(target)
    E = 0
    rows = []
    for K in range(1, max_factor * n + 1):
        x, e = f_with_e(x)
        E += e
        raw_margin = E - THETA * K - start_gap
        exact_margin = log2_int(target) - log2_int(x)
        deficit = THETA * K - E
        rows.append(
            {
                "K": K,
                "e": e,
                "E": E,
                "D": deficit,
                "raw": raw_margin,
                "exact": exact_margin,
                "x": x,
            }
        )
        if x < target:
            break
    return rows


def summarize_case(n, band_low, max_factor, tail):
    rows = tail_rows(n, max_factor)
    if not rows or rows[-1]["exact"] <= 0:
        print(f"\n== n={n} ==")
        print(f"No descent found within {max_factor}n.")
        return

    sigma = rows[-1]["K"]
    entered = [row for row in rows if band_low < row["exact"] < 0]
    if entered:
        first_band = entered[0]["K"]
    else:
        first_band = sigma
    episode_rows = [row for row in rows if first_band <= row["K"] <= sigma]
    actual_band_rows = [row for row in episode_rows if band_low < row["exact"] < 0]
    valuations = [row["e"] for row in episode_rows]
    counts = Counter(valuations)
    one_runs = run_lengths(valuations, 1)[:5]
    payouts = [row for row in episode_rows if row["e"] >= 3]
    final_payout = rows[-1]["e"]

    print(f"\n== n={n} ==")
    print(
        f"sigma={sigma}, sigma/n={sigma / n:.6f}, "
        f"final_exact={rows[-1]['exact']:.6f}, final_e={final_payout}"
    )
    print(
        f"band=({band_low}, 0), first_band_K={first_band}, "
        f"entry_episode_length={len(episode_rows)}, "
        f"actual_band_hits={len(actual_band_rows)}, "
        f"pre_band_steps={first_band - 1}"
    )
    print(
        "entry episode margins: "
        f"min={min(row['exact'] for row in episode_rows):.6f}, "
        f"max={max(row['exact'] for row in episode_rows):.6f}"
    )
    print(
        "valuation counts in entry episode: "
        + ", ".join(f"e={e}:{counts[e]}" for e in sorted(counts))
    )
    if one_runs:
        print(
            "longest e=1 runs in entry episode: "
            + ", ".join(
                f"len={length}@K={first_band + start - 1}-{first_band + end - 1}"
                for length, start, end in one_runs
            )
        )
    if payouts:
        print(
            "largest payouts in entry episode: "
            + ", ".join(
                f"K={row['K']},e={row['e']},exact={row['exact']:.4f}"
                for row in sorted(payouts, key=lambda r: (-r["e"], r["K"]))[:8]
            )
        )
    print(f"last {tail} rows: K e E D exact")
    for row in rows[-tail:]:
        print(
            f"  {row['K']:7d} {row['e']:2d} {row['E']:7d} "
            f"{row['D']:10.4f} {row['exact']:10.6f}"
        )


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--cases",
        type=int,
        nargs="*",
        default=[6035, 18707, 18921, 3871, 10397, 23],
    )
    parser.add_argument("--band-low", type=float, default=-10.0)
    parser.add_argument("--max-factor", type=int, default=4)
    parser.add_argument("--tail", type=int, default=16)
    return parser.parse_args()


def main():
    args = parse_args()
    print("Near-threshold repunit-tail diagnostic")
    print(f"cases={args.cases}")
    for n in args.cases:
        summarize_case(n, args.band_low, args.max_factor, args.tail)


if __name__ == "__main__":
    main()
