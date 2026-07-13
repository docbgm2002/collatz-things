#!/usr/bin/env python3
"""Probe eventually periodic approximants for arbitrary Sturmian intercepts.

This is a finite diagnostic for IEF12, not its proof.  For sampled intercepts
it searches prefixes of the 3/4 mechanical block word for a decomposition
U V^infinity, applies 3 -> 11100 and 4 -> 111100, and checks the exact
rational inverse against the true parity prefix modulo its agreement depth.
"""

import argparse
from decimal import Decimal, ROUND_FLOOR, localcontext
from math import gcd

from verify_balanced_q3_periodic_approximants import (
    expand_blocks,
    inverse_residue,
    periodic_inverse,
)


def slope(precision):
    with localcontext() as context:
        context.prec = precision
        two = Decimal(2)
        return +(two * two.ln() / (Decimal(3) / two).ln() - Decimal(3))


def mechanical_word(count, intercept, precision):
    alpha = slope(precision)
    rho = Decimal(intercept)
    result = []
    with localcontext() as context:
        context.prec = precision
        for index in range(count):
            left = (Decimal(index) * alpha + rho).to_integral_value(
                rounding=ROUND_FLOOR
            )
            right = (Decimal(index + 1) * alpha + rho).to_integral_value(
                rounding=ROUND_FLOOR
            )
            result.append(4 if right - left else 3)
    return result


def best_completion(word, footprint_cap):
    best = None
    footprint_floor = max(1, footprint_cap // 2)
    for preperiod in range(footprint_cap):
        for period in range(1, footprint_cap - preperiod + 1):
            footprint = preperiod + period
            if footprint < footprint_floor or footprint >= len(word):
                continue
            agreement = preperiod
            while agreement < len(word):
                expected = word[
                    preperiod + (agreement - preperiod) % period
                ]
                if word[agreement] != expected:
                    break
                agreement += 1
            candidate = (agreement / footprint, agreement, preperiod, period)
            if best is None or candidate > best:
                best = candidate
    if best is None:
        raise ValueError("word is too short for the requested footprint")
    return best


def affine_correction(bits):
    correction = 0
    one_count = 0
    for position, bit in enumerate(bits):
        if bit == "1":
            correction = 3 * correction + (1 << position)
            one_count += 1
    return correction, one_count


def eventually_periodic_inverse(preperiod, period):
    period_p, period_q, _, _, _ = periodic_inverse(period)
    correction, one_count = affine_correction(preperiod)
    numerator = (1 << len(preperiod)) * period_p - correction * period_q
    denominator = pow(3, one_count) * period_q
    divisor = gcd(abs(numerator), abs(denominator))
    return numerator // divisor, denominator // divisor


def analyse(intercept, block_count, caps, precision):
    word = mechanical_word(block_count, intercept, precision)
    rows = []
    for cap in caps:
        ratio, agreement_blocks, preperiod_blocks, period_blocks = (
            best_completion(word, cap)
        )
        preperiod = expand_blocks(word[:preperiod_blocks])
        period = expand_blocks(
            word[preperiod_blocks : preperiod_blocks + period_blocks]
        )
        true_bits = expand_blocks(word[:agreement_blocks])
        footprint_bits = len(preperiod) + len(period)
        agreement_bits = len(true_bits)
        numerator, denominator = eventually_periodic_inverse(preperiod, period)
        assert denominator & 1
        modulus = 1 << agreement_bits
        rational_residue = numerator * pow(denominator, -1, modulus) % modulus
        assert rational_residue == inverse_residue(true_bits, modulus)
        rows.append(
            {
                "cap": cap,
                "preperiod": preperiod_blocks,
                "period": period_blocks,
                "agreement": agreement_blocks,
                "ratio": ratio,
                "footprint_bits": footprint_bits,
                "agreement_bits": agreement_bits,
                "excess_bits": agreement_bits - footprint_bits,
                "height_bits": max(
                    abs(numerator).bit_length(), abs(denominator).bit_length()
                ),
            }
        )
    return rows


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--blocks", type=int, default=1200)
    parser.add_argument("--caps", default="16,32,64,128")
    parser.add_argument("--intercepts", default="0,0.1,0.314159,0.5,0.9")
    parser.add_argument("--precision", type=int, default=100)
    return parser.parse_args()


def main():
    args = parse_args()
    caps = [int(value) for value in args.caps.split(",")]
    if min(caps) < 1:
        raise ValueError("caps must be positive")
    print("== Arbitrary-intercept Sturmian periodic completions ==")
    for intercept in args.intercepts.split(","):
        print(f"intercept={intercept}")
        for row in analyse(intercept, args.blocks, caps, args.precision):
            print(
                f"  cap={row['cap']:3d} U={row['preperiod']:3d} "
                f"V={row['period']:3d} L={row['agreement']:4d} "
                f"ratio={row['ratio']:.3f} "
                f"bits={row['footprint_bits']:4d}+{row['excess_bits']:4d} "
                f"height_bits={row['height_bits']:4d}"
            )


if __name__ == "__main__":
    main()
