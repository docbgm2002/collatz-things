#!/usr/bin/env python3
"""Measure finite factor-complexity proxies for words and dual-digit streams.

Problems D1 / D1R (docs/repunit/dio1_cocycle_problem.md) ask whether the
dual-digit cocycle of an aperiodic dio(w)=1 word can be eventually zero.
One candidate discharge was Adamczewski-Bugeaud via low cocycle complexity.
This script checks that hypothesis on residual-axis families: if the stream
is high-complexity even for Sturmian words, the complexity route is blocked
in the finite sample.

This script is a diagnostic.  Finite p(n)/n ratios do not prove an infinite
complexity law.
"""

from __future__ import annotations

import argparse
from collections.abc import Iterable, Sequence
from math import log

from explore_balanced_q3_dual_frontier import analyse as analyse_mechanical_frontier
from explore_balanced_q3_residual_axes import make_family
from explore_balanced_q3_zero_cylinders import BLOCK_DATA, mechanical_blocks


def dual_digit_stream(word: Sequence[int]) -> list[int]:
    """Return the IEF4 dual-digit sequence for a {3,4}-block word.

    At each transition, with prior residue q mod 3^R and next block r,

        2^δ h = q - d + j · 3^R,    0 ≤ j < 2^δ,

    and the next residue is q' = 20 + 3^r h.  The integer j is the dual digit.
    """
    endpoint_residue = 0
    endpoint_modulus = 1
    digits: list[int] = []
    for block in word:
        if block not in BLOCK_DATA:
            raise ValueError(f"unsupported block length {block}")
        block_valuation, _correction, block_carry = BLOCK_DATA[block]
        low_modulus = 3**block
        low_residue = 20
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
        digits.append(dual_digit)
        endpoint_residue = low_residue + low_modulus * high_lift
        endpoint_modulus *= low_modulus
    return digits


def tagged_dual_stream(word: Sequence[int], digits: Sequence[int]) -> list[int]:
    """Encode (block, digit) pairs into a single finite alphabet."""
    return [digit + (0 if block == 3 else 32) for block, digit in zip(word, digits)]


def zero_nonzero_stream(digits: Sequence[int]) -> list[int]:
    return [0 if digit == 0 else 1 for digit in digits]


def factor_counts(sequence: Sequence[int], lengths: Iterable[int]) -> dict[int, int]:
    """Count distinct factors of each requested length in a finite prefix."""
    text = tuple(sequence)
    limit = len(text)
    counts: dict[int, int] = {}
    for length in lengths:
        if length < 1 or length > limit:
            counts[length] = 0
            continue
        factors = {text[i : i + length] for i in range(limit - length + 1)}
        counts[length] = len(factors)
    return counts


def factor_ceiling(n_symbols: int, length: int, alphabet_size: int) -> int:
    """Upper bound on distinct length-n factors in a finite prefix."""
    window_cap = max(n_symbols - length + 1, 0)
    if window_cap == 0:
        return 0
    if alphabet_size <= 1:
        return min(window_cap, 1)
    # Avoid computing alphabet^length when it already exceeds the window.
    if length * log(alphabet_size) > log(window_cap) + 1e-12:
        return window_cap
    return min(window_cap, alphabet_size**length)


def complexity_rows(
    sequence: Sequence[int],
    lengths: Sequence[int],
    alphabet_size: int,
) -> list[tuple[int, int, float, float, int]]:
    counts = factor_counts(sequence, lengths)
    rows = []
    n_symbols = len(sequence)
    for length in lengths:
        count = counts[length]
        ceiling = factor_ceiling(n_symbols, length, alphabet_size)
        ratio = count / length if length else 0.0
        saturation = count / ceiling if ceiling else 0.0
        rows.append((length, count, ratio, saturation, ceiling))
    return rows


def cross_check_mechanical(blocks: int) -> None:
    """Agree with explore_balanced_q3_dual_frontier on the mechanical word."""
    mech = mechanical_blocks(blocks)
    digits = dual_digit_stream(mech)
    frontier = analyse_mechanical_frontier(blocks, direct_check_blocks=0)
    assert len(frontier) == blocks
    assert [row["dual_digit"] for row in frontier] == digits


def print_stream_report(
    label: str,
    sequence: Sequence[int],
    lengths: Sequence[int],
    alphabet_size: int,
) -> None:
    occupied = len(set(sequence))
    print(
        f"  stream={label} length={len(sequence)} "
        f"alphabet_cap={alphabet_size} occupied={occupied}"
    )
    for length, count, ratio, saturation, ceiling in complexity_rows(
        sequence, lengths, alphabet_size
    ):
        print(
            f"    n={length:4d} p(n)={count:7d} p(n)/n={ratio:10.4f} "
            f"sat={saturation:6.3f} ceiling={ceiling}"
        )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--blocks", type=int, default=4000)
    parser.add_argument(
        "--lengths",
        default="1,2,4,8,16,32,64,128",
        help="comma-separated factor lengths at which to report p(n)",
    )
    parser.add_argument(
        "--families",
        default=(
            "mechanical,square-flips,periodic-17-flips,negative-bias,xorshift"
        ),
    )
    parser.add_argument("--intercept", default="0.314159")
    parser.add_argument("--precision", type=int, default=100)
    parser.add_argument(
        "--cross-check-blocks",
        type=int,
        default=200,
        help="mechanical dual-digit agreement check against dual_frontier",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    lengths = [int(value) for value in args.lengths.split(",")]
    if any(length < 1 for length in lengths):
        raise ValueError("lengths must be positive")
    if args.blocks < max(lengths):
        raise ValueError("--blocks must be at least the largest requested length")

    print("== Cocycle / word factor-complexity probe ==")
    print(
        "Finite diagnostic for Route A Adamczewski-Bugeaud question: "
        "does the IEF4 dual-digit stream stay low-complexity?"
    )
    print(f"prefix blocks={args.blocks}")
    if args.cross_check_blocks > 0:
        cross_check_mechanical(args.cross_check_blocks)
        print(
            "IEF4 dual-digit cross-check: PASS "
            f"against dual_frontier through {args.cross_check_blocks} blocks"
        )

    for family in args.families.split(","):
        word = make_family(
            family, args.blocks, args.intercept, args.precision
        )
        digits = dual_digit_stream(word)
        tagged = tagged_dual_stream(word, digits)
        support = zero_nonzero_stream(digits)
        zero_count = support.count(0)
        print(
            f"family={family} word_occupied={len(set(word))}/2 "
            f"dual_occupied={len(set(digits))} "
            f"zero_digits={zero_count}/{len(digits)} "
            f"zero_rate={zero_count / len(digits):.6f}"
        )
        print_stream_report("block-word", word, lengths, alphabet_size=2)
        print_stream_report("dual-digit", digits, lengths, alphabet_size=64)
        print_stream_report("tagged-dual", tagged, lengths, alphabet_size=96)
        print_stream_report("zero-nonzero", support, lengths, alphabet_size=2)


if __name__ == "__main__":
    main()
