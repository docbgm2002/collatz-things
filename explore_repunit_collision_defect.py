#!/usr/bin/env python3
"""Test compressed relative-state dynamics for aligned repunit tails.

At a common diagonal d, compare states

    (E, A), (F, B).

Let u=min(E,F), delta=E-F, and

    z=(A-B)/2^(u+1).

The normalized one-step collision defect is

    c = 3z + 2^max(delta,0) - 2^max(-delta,0).

If the outgoing valuations are e,f, then

    delta' = delta + e - f,
    z' = c / 2^min(max(delta,0)+e, max(-delta,0)+f).

This script verifies the recurrence and tests whether (delta,z) alone
determines (e,f). All output is finite diagnostic evidence.
"""

import argparse
from collections import Counter, defaultdict


def v2(value):
    return (value & -value).bit_length() - 1


def trace_normal(n, steps):
    x = (3**n - 1) // 2
    E = 0
    A = -1
    states = [(x, E, A)]
    valuations = []
    for _ in range(steps):
        value = 3 * x + 1
        e = v2(value)
        x = value >> e
        A = 3 * A + (1 << (E + 1))
        E += e
        valuations.append(e)
        states.append((x, E, A))
    return states, valuations


def relative_state(left, right):
    _x, E, A = left
    _y, F, B = right
    u = min(E, F)
    scale = 1 << (u + 1)
    assert (A - B) % scale == 0
    delta = E - F
    z = (A - B) // scale
    alpha = max(delta, 0)
    beta = max(-delta, 0)
    defect = 3 * z + (1 << alpha) - (1 << beta)
    return delta, z, defect


def aligned_rows(n, gap, steps):
    left, left_vals = trace_normal(n, steps)
    right, right_vals = trace_normal(n - gap, steps + gap)
    rows = []

    for step in range(steps):
        right_step = step + gap
        delta, z, defect = relative_state(
            left[step], right[right_step]
        )
        _left_x, E, A = left[step]
        _right_x, F, B = right[right_step]
        e = left_vals[step]
        f = right_vals[right_step]

        alpha = max(delta, 0)
        beta = max(-delta, 0)
        shift = min(alpha + e, beta + f)
        assert defect % (1 << shift) == 0
        expected_delta = delta + e - f
        expected_z = defect >> shift

        next_delta, next_z, _next_defect = relative_state(
            left[step + 1], right[right_step + 1]
        )
        assert (next_delta, next_z) == (expected_delta, expected_z)

        rows.append(
            {
                "n": n,
                "gap": gap,
                "step": step,
                "diagonal": n + step,
                "delta": delta,
                "z": z,
                "defect": defect,
                "E": E,
                "F": F,
                "A": A,
                "B": B,
                "e": e,
                "f": f,
                "next_delta": next_delta,
                "next_z": next_z,
                "merges_next": defect == 0,
            }
        )
        if defect == 0:
            break

    return rows


def scan(limit, gaps, steps):
    rows = []
    for gap in gaps:
        for n in range(max(7, gap + 1) | 1, limit + 1, 2):
            rows.extend(aligned_rows(n, gap, steps))
    return rows


def branching_report(rows, phase_modulus):
    by_relative = defaultdict(set)
    by_phase = defaultdict(set)
    examples = defaultdict(list)

    for row in rows:
        transition = (row["e"], row["f"])
        key = (row["delta"], row["z"])
        phase_key = (
            row["delta"],
            row["z"],
            row["diagonal"] % phase_modulus,
        )
        by_relative[key].add(transition)
        by_phase[phase_key].add(transition)
        if len(examples[key]) < 6:
            examples[key].append(row)

    repeated = {key: values for key, values in by_relative.items() if len(values) > 1}
    phased = {key: values for key, values in by_phase.items() if len(values) > 1}
    return by_relative, repeated, phased, examples


def compact_integer(value):
    bits = abs(value).bit_length()
    if bits <= 80:
        return str(value)
    magnitude = abs(value)
    high = magnitude >> (bits - 24)
    low = magnitude & ((1 << 24) - 1)
    sign = "-" if value < 0 else ""
    return f"{sign}0x{high:06x}...{low:06x}({bits}b)"


def print_report(rows, limit, gaps, steps, phase_modulus, top):
    by_relative, branching, phased, examples = branching_report(
        rows, phase_modulus
    )
    print("== Repunit collision-defect dynamics ==")
    print(
        f"finite domain: odd n <= {limit}; gaps={gaps}; "
        f"aligned steps per pair={steps}"
    )
    print(
        f"rows={len(rows)} distinct relative states={len(by_relative)} "
        f"branching (delta,z) states={len(branching)}"
    )
    print(
        f"branching after adding diagonal mod {phase_modulus}: "
        f"{len(phased)}"
    )
    print(
        f"next-step mergers={sum(row['merges_next'] for row in rows)}"
    )

    transition_counts = Counter((row["e"], row["f"]) for row in rows)
    print(f"most common outgoing pairs: {transition_counts.most_common(20)}")

    ranked = sorted(
        branching.items(),
        key=lambda item: (len(item[1]), len(examples[item[0]])),
        reverse=True,
    )
    print("\nBranching relative states:")
    for (delta, z), transitions in ranked[:top]:
        print(
            f"  delta={delta} z={compact_integer(z)} "
            f"outgoing={sorted(transitions)}"
        )
        for row in examples[(delta, z)]:
            print(
                f"    n={row['n']} gap={row['gap']} step={row['step']} "
                f"d={row['diagonal']} pair=({row['e']},{row['f']})"
            )

    return branching, phased


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=1001)
    parser.add_argument("--gaps", default="2,4,6")
    parser.add_argument("--steps", type=int, default=64)
    parser.add_argument("--phase-modulus", type=int, default=64)
    parser.add_argument("--top", type=int, default=12)
    return parser.parse_args()


def main():
    args = parse_args()
    gaps = tuple(sorted({int(value) for value in args.gaps.split(",")}))
    rows = scan(args.limit, gaps, args.steps)
    print_report(
        rows,
        args.limit,
        gaps,
        args.steps,
        args.phase_modulus,
        args.top,
    )


if __name__ == "__main__":
    main()
