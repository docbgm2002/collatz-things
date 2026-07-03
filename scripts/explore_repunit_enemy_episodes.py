#!/usr/bin/env python3
"""Explore persistent-enemy episodes on primitive repunit tails.

An enemy episode is a maximal run of L consecutive valuations equal to 1,
followed by its terminating valuation q > 1. The enemy coordinate (m, d)
is invariant through the run. The complete episode has raw surplus

    L + q - (L + 1) log2(3).

This tool measures whether the terminal payout repairs the run deficit,
how much later recovery requires, and whether the entry or exit enemy
coordinate already occurred on a smaller primitive tail.

All results are finite diagnostics.
"""

import argparse
import csv
import math
from collections import Counter

from explore_repunit_diagonal_survivors import log2_int
from explore_repunit_tail_merges import scan as scan_merges


THETA = math.log2(3)


def v2(value):
    return (value & -value).bit_length() - 1


def compact_integer(value, decimal_digits=18):
    magnitude = abs(value)
    bits = magnitude.bit_length()
    if bits > 256:
        high = magnitude >> (bits - 32)
        low = magnitude & ((1 << 32) - 1)
        sign = "-" if value < 0 else ""
        return f"{sign}0x{high:08x}...{low:08x}({bits}b)"
    text = str(value)
    if len(text) <= decimal_digits:
        return text
    sign = "-" if value < 0 else ""
    digits = text.lstrip("-")
    return f"{sign}{digits[:8]}...{digits[-8:]}({bits}b)"


def enemy_coordinate(n, K, E, A):
    R = A + (1 << (E + 1))
    assert R != 0
    r = 0
    d = R
    while d % 3 == 0:
        d //= 3
        r += 1
    m = n + K - r
    return {
        "m": m,
        "d": d,
        "r": r,
        "height": abs(d).bit_length(),
        "height_ratio": math.inf if E == 0 else abs(d).bit_length() / E,
    }


def trace_to_descent(n, sigma):
    x = (3**n - 1) // 2
    xs = [x]
    valuations = []
    cumulative = [0]
    corrections = [-1]
    E = 0
    A = -1

    for _ in range(sigma):
        value = 3 * x + 1
        e = v2(value)
        x = value >> e

        A = 3 * A + (1 << (E + 1))
        E += e

        valuations.append(e)
        xs.append(x)
        cumulative.append(E)
        corrections.append(A)

    assert xs[-1] < (1 << n) - 1
    return xs, valuations, cumulative, corrections


def local_recovery(valuations, start):
    """First transition count from start with nonnegative raw surplus."""
    surplus = 0.0
    for end in range(start, len(valuations)):
        surplus += valuations[end] - THETA
        if surplus >= 0:
            return end - start + 1, surplus
    return None, surplus


def extract_episodes(n, sigma, previous_coordinates, min_run):
    xs, valuations, cumulative, corrections = trace_to_descent(n, sigma)
    episodes = []
    K = 0

    while K < len(valuations):
        if valuations[K] != 1:
            K += 1
            continue

        start = K
        while K < len(valuations) and valuations[K] == 1:
            K += 1

        # A run ending at first descent without a terminating q is censored.
        if K == len(valuations):
            continue

        run_length = K - start
        if run_length < min_run:
            K += 1
            continue

        terminal_index = K
        terminal_q = valuations[terminal_index]
        assert terminal_q > 1
        exit_K = terminal_index + 1

        entry = enemy_coordinate(
            n, start, cumulative[start], corrections[start]
        )
        exit_coord = enemy_coordinate(
            n, exit_K, cumulative[exit_K], corrections[exit_K]
        )

        entry_key = (entry["m"], entry["d"])
        exit_key = (exit_coord["m"], exit_coord["d"])
        entry_prior = previous_coordinates.get(entry_key)
        exit_prior = previous_coordinates.get(exit_key)

        episode_surplus = (
            run_length
            + terminal_q
            - (run_length + 1) * THETA
        )
        required_q = math.ceil(
            (run_length + 1) * THETA - run_length
        )
        recovery_steps, recovery_surplus = local_recovery(
            valuations, start
        )
        exact_contraction = log2_int(xs[start]) - log2_int(xs[exit_K])

        episodes.append(
            {
                "n": n,
                "sigma": sigma,
                "start_K": start,
                "exit_K": exit_K,
                "run_length": run_length,
                "terminal_q": terminal_q,
                "required_q": required_q,
                "payout_gap": terminal_q - required_q,
                "episode_surplus": episode_surplus,
                "terminal_compensates": episode_surplus >= 0,
                "exact_contraction": exact_contraction,
                "recovery_steps": recovery_steps,
                "extra_recovery": (
                    None
                    if recovery_steps is None
                    else recovery_steps - (run_length + 1)
                ),
                "recovery_surplus": recovery_surplus,
                "ends_in_descent": exit_K == sigma,
                "entry_E": cumulative[start],
                "entry_m": entry["m"],
                "entry_d": entry["d"],
                "entry_height": entry["height"],
                "entry_height_ratio": entry["height_ratio"],
                "entry_prior_n": None if entry_prior is None else entry_prior[0],
                "entry_prior_K": None if entry_prior is None else entry_prior[1],
                "exit_E": cumulative[exit_K],
                "exit_m": exit_coord["m"],
                "exit_d": exit_coord["d"],
                "exit_height": exit_coord["height"],
                "exit_height_ratio": exit_coord["height_ratio"],
                "exit_prior_n": None if exit_prior is None else exit_prior[0],
                "exit_prior_K": None if exit_prior is None else exit_prior[1],
            }
        )

        # The terminal valuation cannot itself begin a one-run.
        K += 1

    coordinates = []
    for state_K in range(sigma + 1):
        coord = enemy_coordinate(
            n,
            state_K,
            cumulative[state_K],
            corrections[state_K],
        )
        coordinates.append(((coord["m"], coord["d"]), state_K))

    return episodes, coordinates


def scan(limit, factor, min_run):
    merge_result = scan_merges(limit=limit, factor=factor)
    primitives = sorted(merge_result["primitives"], key=lambda row: row["n"])
    previous_coordinates = {}
    episodes = []

    for primitive in primitives:
        n = primitive["n"]
        tail_episodes, coordinates = extract_episodes(
            n,
            primitive["sigma"],
            previous_coordinates,
            min_run,
        )
        episodes.extend(tail_episodes)

        # Add the current tail only after all lookups, so "prior" means a
        # strictly smaller primitive exponent.
        for key, state_K in coordinates:
            previous_coordinates.setdefault(key, (n, state_K))

    return primitives, episodes


def episode_is_high(row, threshold):
    return (
        math.isfinite(row["entry_height_ratio"])
        and row["entry_height_ratio"] >= threshold
    )


def summarize(rows, high_height_ratio):
    high = [row for row in rows if episode_is_high(row, high_height_ratio)]

    def counts(population):
        return {
            "episodes": len(population),
            "terminal_compensates": sum(
                row["terminal_compensates"] for row in population
            ),
            "eventual_recovery": sum(
                row["recovery_steps"] is not None for row in population
            ),
            "ends_in_descent": sum(
                row["ends_in_descent"] for row in population
            ),
            "entry_prior": sum(
                row["entry_prior_n"] is not None for row in population
            ),
            "exit_prior": sum(
                row["exit_prior_n"] is not None for row in population
            ),
            "terminal_or_exit_prior": sum(
                row["terminal_compensates"]
                or row["exit_prior_n"] is not None
                for row in population
            ),
            "recovery_or_exit_prior": sum(
                row["recovery_steps"] is not None
                or row["exit_prior_n"] is not None
                for row in population
            ),
        }

    return counts(rows), counts(high), high


def print_population(label, counts):
    total = counts["episodes"]
    print(f"\n{label}: {total}")
    if not total:
        return
    for key in (
        "terminal_compensates",
        "eventual_recovery",
        "ends_in_descent",
        "entry_prior",
        "exit_prior",
        "terminal_or_exit_prior",
        "recovery_or_exit_prior",
    ):
        value = counts[key]
        print(f"  {key}={value} ({value / total:.2%})")


def print_episode(label, row):
    recovery = (
        "censored"
        if row["recovery_steps"] is None
        else f"{row['recovery_steps']} steps "
        f"(+{row['extra_recovery']} after terminal)"
    )
    prior = (
        "none"
        if row["exit_prior_n"] is None
        else f"n={row['exit_prior_n']} K={row['exit_prior_K']}"
    )
    print(
        f"  {label}: n={row['n']} K={row['start_K']} "
        f"L={row['run_length']} q={row['terminal_q']} "
        f"need={row['required_q']} gap={row['payout_gap']} "
        f"surplus={row['episode_surplus']:.6f} "
        f"exact={row['exact_contraction']:.6f} "
        f"entry_h/E={row['entry_height_ratio']:.4f} "
        f"entry_d={compact_integer(row['entry_d'])} "
        f"recovery={recovery} exit_prior={prior} "
        f"descent={row['ends_in_descent']}"
    )


def print_report(
    primitives,
    episodes,
    limit,
    min_run,
    high_height_ratio,
    top,
):
    all_counts, high_counts, high = summarize(
        episodes, high_height_ratio
    )
    print("== Repunit enemy episodes ==")
    print(
        f"finite domain: odd 7 <= n <= {limit}; "
        f"primitive tails={len(primitives)}; min run={min_run}"
    )
    print_population("all terminated one-runs", all_counts)
    print_population(
        f"Case B entry height h/E >= {high_height_ratio:g}",
        high_counts,
    )
    print(
        "\nNote: recovery by first descent is guaranteed once first descent "
        "is known; it is not an independent bound on the descent time."
    )

    print("\nRun-length distribution:")
    print(Counter(row["run_length"] for row in episodes).most_common(20))
    print("Terminal-payout distribution:")
    print(Counter(row["terminal_q"] for row in episodes).most_common(20))

    recovered = [
        row for row in high if row["recovery_steps"] is not None
    ]
    if recovered:
        max_steps = max(recovered, key=lambda row: row["recovery_steps"])
        max_run_multiple = max(
            recovered,
            key=lambda row: row["recovery_steps"]
            / (row["run_length"] + 1),
        )
        max_n_ratio = max(
            recovered,
            key=lambda row: row["recovery_steps"] / row["n"],
        )
        buckets = Counter()
        for row in recovered:
            steps = row["recovery_steps"]
            if steps <= 16:
                buckets["<=16"] += 1
            elif steps <= 32:
                buckets["17..32"] += 1
            elif steps <= 64:
                buckets["33..64"] += 1
            elif steps <= 128:
                buckets["65..128"] += 1
            else:
                buckets[">128"] += 1
        print("\nCase B recovery scaling:")
        print(f"  buckets={dict(buckets)}")
        print_episode("largest absolute recovery", max_steps)
        print(
            "  largest recovery/run ratio="
            f"{max_run_multiple['recovery_steps'] / (max_run_multiple['run_length'] + 1):.3f}"
        )
        print_episode("largest recovery/run case", max_run_multiple)
        print(
            "  largest recovery/n ratio="
            f"{max_n_ratio['recovery_steps'] / max_n_ratio['n']:.6f}"
        )
        print_episode("largest recovery/n case", max_n_ratio)

    longest = sorted(
        episodes,
        key=lambda row: (
            row["run_length"],
            -row["episode_surplus"],
        ),
        reverse=True,
    )
    print("\nLongest episodes:")
    for row in longest[:top]:
        print_episode("long", row)

    failed = sorted(
        high,
        key=lambda row: (
            row["episode_surplus"],
            -row["run_length"],
        ),
    )
    print("\nWorst Case B terminal shortfalls:")
    for row in failed[:top]:
        print_episode("shortfall", row)

    slow = sorted(
        (
            row
            for row in high
            if row["recovery_steps"] is not None
        ),
        key=lambda row: (
            row["extra_recovery"],
            row["run_length"],
        ),
        reverse=True,
    )
    print("\nSlowest Case B local recoveries:")
    for row in slow[:top]:
        print_episode("recovery", row)

    return all_counts, high_counts


def write_csv(path, episodes):
    fields = list(episodes[0]) if episodes else []
    with open(path, "w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        if fields:
            writer.writeheader()
            writer.writerows(episodes)


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=2001)
    parser.add_argument("--factor", type=int, default=3)
    parser.add_argument("--min-run", type=int, default=2)
    parser.add_argument("--high-height-ratio", type=float, default=0.75)
    parser.add_argument("--top", type=int, default=12)
    parser.add_argument("--csv")
    return parser.parse_args()


def main():
    args = parse_args()
    primitives, episodes = scan(args.limit, args.factor, args.min_run)
    print_report(
        primitives,
        episodes,
        args.limit,
        args.min_run,
        args.high_height_ratio,
        args.top,
    )
    if args.csv:
        write_csv(args.csv, episodes)
        print(f"\nwrote {args.csv}")


if __name__ == "__main__":
    main()
