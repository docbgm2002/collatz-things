#!/usr/bin/env python3
"""Explore exact starting cylinders for reset-free balanced q=3 runs.

For a consecutive word W of H balanced blocks, write

    Phi_W(x) = (3^R x + B) / 2^D.

The composition is integral at every block boundary exactly when the
starting value belongs to one residue class u_H modulo 2^D.  Extending the
word exposes a lift digit z_H in

    u_H = u_(H-1) + z_H 2^D_(H-1).

An ordinary positive integer can realize the complete infinite word only if
these canonical representatives eventually stabilize, equivalently only if
the lift digits are eventually zero.  This script computes the cylinders by
an exact streaming lift; its output is finite evidence, not a proof.
"""

import argparse
from collections import Counter
from math import floor, log2

from explore_balanced_q3_cylinders import balanced_prefixes


BLOCK_DATA = {
    3: (5, 19, 23),
    4: (6, 65, 15),
}


def mechanical_blocks(count, phase=0):
    """Return count block lengths after skipping phase appended blocks."""
    if count < 1:
        raise ValueError("count must be positive")
    if phase < 0:
        raise ValueError("phase must be nonnegative")
    prefixes = balanced_prefixes(phase + count + 1)
    next(prefixes)  # initial valuation-three payout
    blocks = [len(suffix) for _, _, suffix in prefixes]
    return blocks[phase:]


def continued_fraction_denominators(limit):
    """Numerical convergent denominators of the 4-block indicator slope."""
    beta = 2 / log2(3 / 2) - 3
    x = beta
    p_prev, p = 0, 1
    q_prev, q = 1, 0
    denominators = []
    for _ in range(64):
        a = floor(x)
        p_prev, p = p, a * p + p_prev
        q_prev, q = q, a * q + q_prev
        if q > limit:
            break
        if q > 0:
            denominators.append((a, p, q))
        remainder = x - a
        if remainder == 0:
            break
        x = 1 / remainder
    return denominators


def analyse(blocks, phase=0):
    plan = mechanical_blocks(blocks, phase)
    start_residue = 0
    endpoint = 0
    total_valuation = 0
    odd_steps = 0
    odd_power = 1
    affine_correction = 0
    rows = []

    for index, block_steps in enumerate(plan, 1):
        block_valuation, correction, required_residue = BLOCK_DATA[block_steps]
        local_modulus = 1 << block_valuation

        # Changing the canonical start by z*2^D changes the old endpoint by
        # z*3^R.  Choose the unique z which puts that endpoint into the next
        # block's integrality class.
        lift_digit = (
            (required_residue - endpoint)
            * pow(odd_power, -1, local_modulus)
        ) % local_modulus
        pre_block_endpoint = endpoint + lift_digit * odd_power
        assert pre_block_endpoint % local_modulus == required_residue

        start_residue += lift_digit << total_valuation
        next_endpoint = (
            pow(3, block_steps) * pre_block_endpoint + correction
        ) >> block_valuation
        high_lift = (
            endpoint - required_residue + lift_digit * odd_power
        ) >> block_valuation
        assert next_endpoint == 20 + pow(3, block_steps) * high_lift

        affine_correction = (
            pow(3, block_steps) * affine_correction
            + (correction << total_valuation)
        )
        odd_power *= pow(3, block_steps)
        total_valuation += block_valuation
        odd_steps += block_steps
        endpoint = next_endpoint

        # Full affine identity: the canonical relaxed starting cylinder maps
        # to the canonical dual endpoint.  The high-lift identity above also
        # verifies that the starting-cylinder digit is the IEF4 dual digit.
        assert 0 <= start_residue < (1 << total_valuation)
        assert odd_power == pow(3, odd_steps)
        assert (
            odd_power * start_residue + affine_correction
            == endpoint << total_valuation
        )
        rows.append(
            {
                "H": index,
                "phase": phase,
                "block_steps": block_steps,
                "D": total_valuation,
                "R": odd_steps,
                "u": start_residue,
                "u_bits": start_residue.bit_length(),
                "bit_gap": total_valuation - start_residue.bit_length(),
                "endpoint": endpoint,
                "lift_digit": lift_digit,
            }
        )

    return rows


def print_report(rows, show):
    lift_histograms = {}
    zero_runs = []
    zero_start = None
    for row in rows:
        bits = BLOCK_DATA[row["block_steps"]][0]
        lift_histograms.setdefault(bits, Counter())[row["lift_digit"]] += 1
        if row["lift_digit"] == 0:
            if zero_start is None:
                zero_start = row["H"]
        elif zero_start is not None:
            zero_runs.append((zero_start, row["H"] - 1))
            zero_start = None
    if zero_start is not None:
        zero_runs.append((zero_start, rows[-1]["H"]))

    longest = max(
        ((end - start + 1, start, end) for start, end in zero_runs),
        default=(0, None, None),
    )
    widest_gap = max(rows, key=lambda row: (row["bit_gap"], -row["H"]))

    print("== Balanced q=3 reset-free starting cylinders ==")
    print(f"phase={rows[0]['phase']}; exact blocks={len(rows)}")
    print(
        "largest bit deficit below cylinder modulus: "
        f"{widest_gap['bit_gap']} at H={widest_gap['H']}"
    )
    print(
        "longest zero-lift run: "
        f"{longest[0]} at H={longest[1]}..{longest[2]}"
    )
    for bits, histogram in sorted(lift_histograms.items()):
        print(
            f"{bits}-bit cylinder lifts: occupied={len(histogram)}/{1 << bits}; "
            f"zero={histogram.get(0, 0)}"
        )

    print("continued-fraction scales of beta=2/log2(3/2)-3:")
    by_h = {row["H"]: row for row in rows}
    for partial_quotient, numerator, denominator in continued_fraction_denominators(
        len(rows)
    ):
        row = by_h[denominator]
        print(
            f"  H={denominator:6d} convergent={numerator}/{denominator} "
            f"a={partial_quotient:2d} u_bits={row['u_bits']:6d} "
            f"D={row['D']:6d} gap={row['bit_gap']:3d} "
            f"z={row['lift_digit']:2d}"
        )

    selected = rows if show <= 0 else rows[:show]
    for row in selected:
        print(
            f"  H={row['H']:5d} r={row['block_steps']} "
            f"R={row['R']:6d} D={row['D']:6d} "
            f"u_bits={row['u_bits']:6d} gap={row['bit_gap']:3d} "
            f"z={row['lift_digit']:2d}"
        )


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--blocks", type=int, default=10000)
    parser.add_argument(
        "--phase",
        type=int,
        default=0,
        help="number of appended mechanical blocks to skip",
    )
    parser.add_argument(
        "--show",
        type=int,
        default=8,
        help="number of initial rows to print; use 0 for all",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    print_report(analyse(args.blocks, args.phase), args.show)


if __name__ == "__main__":
    main()
