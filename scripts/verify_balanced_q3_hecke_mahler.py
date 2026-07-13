#!/usr/bin/env python3
"""Verify the Hecke--Mahler representation of the balanced q=3 word.

For c=log2(3/2), gamma=c/2, the full balanced valuation schedule has odd
shortcut positions

    d_0=0,  d_i=i+2*ceil(gamma*i)  (i>=1).

The inverse parity conjugacy is therefore the 2-adic value

    xi = -1/3 - (4/3) sum_{i>=1} (2/3)^i 4^floor(gamma*i).

This script checks the position formula against the mechanical payout word
and checks both series forms against the exact finite parity cylinder.
"""

import argparse
from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, localcontext

from explore_balanced_q3_cylinders import (
    balanced_prefixes,
    starting_residue_for_word,
)


def floor_and_ceil_gamma_multiples(count, precision):
    with localcontext() as context:
        context.prec = precision
        gamma = (
            Decimal(3).ln() / Decimal(2).ln() - Decimal(1)
        ) / Decimal(2)
        rows = []
        for index in range(count + 1):
            value = gamma * index
            floor_value = int(value.to_integral_value(rounding=ROUND_FLOOR))
            ceil_value = int(value.to_integral_value(rounding=ROUND_CEILING))
            rows.append((floor_value, ceil_value))
    return rows


def mechanical_valuations(odd_steps):
    if odd_steps < 1:
        raise ValueError("odd-steps must be positive")
    valuations = []
    # Each balanced_prefixes item contributes its complete valuation suffix.
    # odd_steps payouts are more than enough to expose odd_steps valuations.
    for _, _, suffix in balanced_prefixes(odd_steps):
        valuations.extend(suffix)
        if len(valuations) >= odd_steps:
            break
    return tuple(valuations[:odd_steps])


def parity_series_residue(positions, modulus):
    inverse_three = pow(3, -1, modulus)
    inverse_power = inverse_three
    total = 0
    for position in positions:
        total -= (1 << position) * inverse_power
        inverse_power = inverse_power * inverse_three % modulus
    return total % modulus


def hecke_mahler_residue(floors, positions, modulus):
    inverse_three = pow(3, -1, modulus)
    ratio = 2 * inverse_three % modulus
    ratio_power = ratio
    total = -inverse_three
    for index in range(1, len(positions)):
        total -= (
            4
            * inverse_three
            * ratio_power
            * pow(4, floors[index], modulus)
        )
        ratio_power = ratio_power * ratio % modulus
    return total % modulus


def verify(odd_steps, precision):
    floor_ceil = floor_and_ceil_gamma_multiples(odd_steps, precision)
    confirmation = floor_and_ceil_gamma_multiples(odd_steps, precision + 30)
    if floor_ceil != confirmation:
        raise ValueError("mechanical floors are unstable at this precision")

    positions = [0]
    for index in range(1, odd_steps + 1):
        positions.append(index + 2 * floor_ceil[index][1])
    formula_valuations = tuple(
        positions[index + 1] - positions[index]
        for index in range(odd_steps)
    )
    assert set(formula_valuations) <= {1, 3}

    mechanical = mechanical_valuations(odd_steps)
    assert formula_valuations == mechanical

    exact_start, total_valuation = starting_residue_for_word(mechanical)
    assert total_valuation == positions[-1]
    modulus = 1 << (total_valuation + 1)
    parity_residue = parity_series_residue(positions, modulus)
    hecke_residue = hecke_mahler_residue(
        [row[0] for row in floor_ceil],
        positions,
        modulus,
    )
    assert parity_residue == exact_start
    assert hecke_residue == exact_start

    return {
        "odd_steps": odd_steps,
        "shortcut_depth": total_valuation,
        "payouts": formula_valuations.count(3),
        "start_bits": exact_start.bit_length(),
        "modulus_bits": modulus.bit_length(),
    }


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--odd-steps", type=int, default=5000)
    parser.add_argument("--precision", type=int, default=100)
    return parser.parse_args()


def main():
    args = parse_args()
    report = verify(args.odd_steps, args.precision)
    print("== Balanced q=3 Hecke--Mahler identity ==")
    print("mechanical position formula: PASS")
    print("inverse parity series: PASS")
    print("Hecke--Mahler rewrite: PASS")
    print(
        f"odd_steps={report['odd_steps']} "
        f"shortcut_depth={report['shortcut_depth']} "
        f"payouts={report['payouts']} "
        f"start_bits={report['start_bits']} "
        f"modulus_bits={report['modulus_bits']}"
    )


if __name__ == "__main__":
    main()
