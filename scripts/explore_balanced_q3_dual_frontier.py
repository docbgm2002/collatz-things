#!/usr/bin/env python3
"""Explore the dual mod-3 endpoint frontier of the balanced q=3 word.

After L balanced blocks, write the exact affine composition as

    x_L = (3^R x_0 + B) / 2^E,     E = R + 2L.

Every integral endpoint therefore belongs to the word-dependent class

    x_L = q_L (mod 3^R),  q_L = B * 2^(-E) (mod 3^R).

PCD16 bounds a positive orbit following the word by O(x_0 + L).  Hence a
proof that q_L/L tends to infinity would exclude every fixed positive x_0
from the infinite balanced itinerary.  This script measures q_L exactly.
Its inequalities are finite diagnostics, not universal claims.
"""

import argparse
from collections import Counter

from explore_balanced_q3_cylinders import balanced_prefixes


def analyse(blocks, direct_check_blocks=2000):
    if blocks < 1:
        raise ValueError("blocks must be positive")
    if direct_check_blocks < 0:
        raise ValueError("direct_check_blocks must be nonnegative")

    correction = 0
    total_valuation = 0
    odd_steps = 0
    endpoint_residue = 0
    endpoint_modulus = 1
    rows = []

    # balanced_prefixes starts with the initial q=3 payout.  The dual
    # frontier begins immediately after it and studies the appended blocks.
    plan = list(balanced_prefixes(blocks + 1))[1:]
    for block_index, (_, _, suffix) in enumerate(plan, 1):
        block_steps = len(suffix)
        block_valuation = sum(suffix)
        block_correction = 0
        block_E = 0
        for valuation in suffix:
            block_correction = 3 * block_correction + (1 << block_E)
            block_E += valuation

        low_modulus = 3**block_steps
        low_residue = (
            block_correction
            * pow(1 << block_valuation, -1, low_modulus)
        ) % low_modulus
        block_carry = (
            (1 << block_valuation) * low_residue - block_correction
        ) // low_modulus
        assert low_residue == 20
        assert (block_steps, block_valuation, block_carry) in (
            (3, 5, 23),
            (4, 6, 15),
        )

        if endpoint_modulus == 1:
            high_lift = 0
        else:
            high_lift = (
                (endpoint_residue - block_carry)
                * pow(1 << block_valuation, -1, endpoint_modulus)
            ) % endpoint_modulus
        digit_numerator = (
            (1 << block_valuation) * high_lift
            - (endpoint_residue - block_carry)
        )
        assert digit_numerator % endpoint_modulus == 0
        dual_digit = digit_numerator // endpoint_modulus
        assert 0 <= dual_digit < (1 << block_valuation)

        endpoint_residue = low_residue + low_modulus * high_lift
        endpoint_modulus *= low_modulus
        total_valuation += block_valuation
        odd_steps += block_steps
        assert total_valuation == odd_steps + 2 * block_index

        canonical_preimage = None
        if block_index <= direct_check_blocks:
            check_E = total_valuation - block_valuation
            for valuation in suffix:
                correction = 3 * correction + (1 << check_E)
                check_E += valuation
            assert check_E == total_valuation
            direct_residue = (
                correction
                * pow(1 << total_valuation, -1, endpoint_modulus)
            ) % endpoint_modulus
            assert endpoint_residue == direct_residue
            assert (
                (1 << total_valuation) * endpoint_residue - correction
            ) % endpoint_modulus == 0

            # This is the integral affine preimage of the canonical endpoint
            # residue. It need not be positive or realize every intermediate
            # valuation; it is retained as an exact diagnostic coordinate.
            canonical_preimage = (
                (1 << total_valuation) * endpoint_residue - correction
            ) // endpoint_modulus

        candidate_floor = 1 << (5 * block_index - 1)
        rows.append(
            {
                "L": block_index,
                "R": odd_steps,
                "E": total_valuation,
                "q": endpoint_residue,
                "q_bits": endpoint_residue.bit_length(),
                "modulus_bits": endpoint_modulus.bit_length(),
                "modulus_bit_gap": (
                    endpoint_modulus.bit_length()
                    - endpoint_residue.bit_length()
                ),
                "candidate_floor_holds": (
                    endpoint_residue >= candidate_floor
                ),
                "canonical_preimage": canonical_preimage,
                "block_steps": block_steps,
                "block_valuation": block_valuation,
                "dual_high_lift": high_lift,
                "dual_digit": dual_digit,
            }
        )

    return rows


def print_report(rows, show):
    first_failure = next(
        (row for row in rows if not row["candidate_floor_holds"]),
        None,
    )
    widest_gap = max(
        rows,
        key=lambda row: (row["modulus_bit_gap"], -row["L"]),
    )
    weakest_five_bit_margin = min(
        rows,
        key=lambda row: (row["q_bits"] - 5 * row["L"], row["L"]),
    )
    weakest_linear_escape = min(
        rows,
        key=lambda row: (
            row["q_bits"] - row["L"].bit_length(),
            row["L"],
        ),
    )
    digit_histograms = {}
    zero_runs = []
    current_zero_start = None
    for row in rows:
        bits = row["block_valuation"]
        histogram = digit_histograms.setdefault(bits, Counter())
        histogram[row["dual_digit"]] += 1
        if row["dual_digit"] == 0:
            if current_zero_start is None:
                current_zero_start = row["L"]
        elif current_zero_start is not None:
            zero_runs.append((current_zero_start, row["L"] - 1))
            current_zero_start = None
    if current_zero_start is not None:
        zero_runs.append((current_zero_start, rows[-1]["L"]))
    longest_zero_run = max(
        ((end - start + 1, start, end) for start, end in zero_runs),
        default=(0, None, None),
    )

    print("== Balanced q=3 dual endpoint frontier ==")
    print(f"exact appended blocks={len(rows)}")
    if first_failure is None:
        print(
            "finite candidate q_L >= 2^(5L-1): PASS "
            f"through L={len(rows)}"
        )
    else:
        print(
            "finite candidate q_L >= 2^(5L-1): FAIL "
            f"first at L={first_failure['L']}"
        )
    print(
        "largest bit deficit below modulus: "
        f"{widest_gap['modulus_bit_gap']} at L={widest_gap['L']} "
        f"(q_bits={widest_gap['q_bits']}, "
        f"modulus_bits={widest_gap['modulus_bits']})"
    )
    print(
        "smallest q_bits-5L: "
        f"{weakest_five_bit_margin['q_bits'] - 5 * weakest_five_bit_margin['L']} "
        f"at L={weakest_five_bit_margin['L']}"
    )
    print(
        "smallest bit escape over linear scale: "
        f"{weakest_linear_escape['q_bits'] - weakest_linear_escape['L'].bit_length()} "
        f"at L={weakest_linear_escape['L']}"
    )
    for bits, histogram in sorted(digit_histograms.items()):
        print(
            f"{bits}-bit dual digits: occupied={len(histogram)}/{1 << bits}; "
            f"zero={histogram.get(0, 0)}; "
            f"count range={min(histogram.values())}..{max(histogram.values())}"
        )
    print(
        "longest zero-digit run: "
        f"{longest_zero_run[0]} at "
        f"L={longest_zero_run[1]}..{longest_zero_run[2]}"
    )

    selected = rows if show <= 0 else rows[:show]
    for row in selected:
        print(
            f"  L={row['L']:5d} R={row['R']:6d} E={row['E']:6d} "
            f"q_bits={row['q_bits']:6d} "
            f"mod_bits={row['modulus_bits']:6d} "
            f"gap={row['modulus_bit_gap']:3d}"
        )


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--blocks", type=int, default=1000)
    parser.add_argument(
        "--direct-check",
        type=int,
        default=2000,
        help="prefix blocks also checked from the full affine correction",
    )
    parser.add_argument(
        "--show",
        type=int,
        default=12,
        help="number of initial rows to print; use 0 for all",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    print_report(analyse(args.blocks, args.direct_check), args.show)


if __name__ == "__main__":
    main()
