#!/usr/bin/env python3
"""Verify periodic rational approximants to the characteristic balanced tail.

For a standard block prefix S_k, expand 3 -> 11100 and 4 -> 111100 in
shortcut parity.  Repeating that binary word gives a rational 2-adic inverse
whose height is O(E*2^E).  The true characteristic word begins S_k S_(k-1),
so the two inverse values agree modulo 2^(E_k+E_(k-1)).  A fixed block phase
shift rotates the periodic word and loses only the corresponding fixed number
of initial parity bits.
"""

import argparse
from math import gcd

from explore_balanced_q3_sturmian_renormalization import continued_fraction
from explore_balanced_q3_zero_cylinders import mechanical_blocks


def parity_block(block_steps):
    return "1" * (block_steps - 1) + "100"


def expand_blocks(blocks):
    return "".join(parity_block(block_steps) for block_steps in blocks)


def periodic_inverse(word):
    length = len(word)
    positions = [index for index, bit in enumerate(word) if bit == "1"]
    weight = len(positions)
    numerator = sum(
        (1 << position) * pow(3, weight - one_index - 1)
        for one_index, position in enumerate(positions)
    )
    denominator = (1 << length) - pow(3, weight)
    divisor = gcd(numerator, abs(denominator))
    return (
        numerator // divisor,
        denominator // divisor,
        numerator,
        denominator,
        weight,
    )


def inverse_residue(bits, modulus):
    inverse_three = pow(3, -1, modulus)
    inverse_power = inverse_three
    total = 0
    for position, bit in enumerate(bits):
        if bit == "1":
            total -= (1 << position) * inverse_power
            inverse_power = inverse_power * inverse_three % modulus
    return total % modulus


def analyse(max_denominator, precision, phase_blocks):
    cf = continued_fraction(max_denominator, precision)
    confirmation = continued_fraction(max_denominator, precision + 30)
    if cf != confirmation:
        raise ValueError("continued fraction is unstable at this precision")
    if len(cf) < 4:
        raise ValueError("max-denominator must reach the convergent 7")

    largest_denominator = cf[-1][2]
    previous_denominator = cf[-2][2]
    plan = mechanical_blocks(
        largest_denominator + previous_denominator + phase_blocks,
        phase=1,
    )
    phase_bits = len(expand_blocks(plan[:phase_blocks]))
    rows = []

    for index in range(3, len(cf)):
        denominator_blocks = cf[index][2]
        previous_blocks = cf[index - 1][2]
        prefix_blocks = plan[:denominator_blocks]
        previous_prefix = plan[:previous_blocks]
        assert (
            plan[: denominator_blocks + previous_blocks]
            == prefix_blocks + previous_prefix
        )

        word = expand_blocks(prefix_blocks)
        previous_word = expand_blocks(previous_prefix)
        unshifted_shared_bits = len(word) + len(previous_word)
        if phase_bits >= unshifted_shared_bits:
            continue
        shared_bits = unshifted_shared_bits - phase_bits
        true_unshifted_bits = expand_blocks(
            plan[: denominator_blocks + previous_blocks]
        )
        true_bits = true_unshifted_bits[phase_bits:]
        rotation = phase_bits % len(word)
        rotated_word = word[rotation:] + word[:rotation]
        periodic_bits = (
            rotated_word * (shared_bits // len(rotated_word) + 1)
        )[:shared_bits]
        assert true_bits == periodic_bits

        reduced_numerator, reduced_denominator, numerator, raw_denominator, weight = (
            periodic_inverse(rotated_word)
        )
        assert reduced_denominator & 1
        modulus = 1 << shared_bits
        periodic_residue = (
            reduced_numerator * pow(reduced_denominator, -1, modulus)
        ) % modulus
        assert periodic_residue == inverse_residue(true_bits, modulus)

        length = len(word)
        assert numerator <= 8 * length * (1 << length)
        assert abs(raw_denominator) <= 3 * (1 << length)
        rows.append(
            {
                "index": index,
                "Q": denominator_blocks,
                "previous_Q": previous_blocks,
                "E": length,
                "previous_E": len(previous_word),
                "R": weight,
                "shared_bits": shared_bits,
                "phase_bits": phase_bits,
                "numerator_bits": abs(reduced_numerator).bit_length(),
                "denominator_bits": abs(reduced_denominator).bit_length(),
            }
        )
    return rows


def print_report(rows, phase_blocks):
    print("== Balanced q=3 periodic approximants ==")
    print(f"fixed block phase={phase_blocks}")
    print(f"exact standard approximants={len(rows)}")
    for row in rows:
        print(
            f"  k={row['index']:2d} Q={row['Q']:6d} "
            f"E={row['E']:6d} previous_E={row['previous_E']:6d} "
            f"shared={row['shared_bits']:6d} "
            f"lost={row['phase_bits']:4d} "
            f"height_bits={max(row['numerator_bits'], row['denominator_bits']):6d}"
        )


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-denominator", type=int, default=4563)
    parser.add_argument("--precision", type=int, default=120)
    parser.add_argument("--phase-blocks", type=int, default=0)
    return parser.parse_args()


def main():
    args = parse_args()
    if args.phase_blocks < 0:
        raise ValueError("phase-blocks must be nonnegative")
    print_report(
        analyse(args.max_denominator, args.precision, args.phase_blocks),
        args.phase_blocks,
    )


if __name__ == "__main__":
    main()
