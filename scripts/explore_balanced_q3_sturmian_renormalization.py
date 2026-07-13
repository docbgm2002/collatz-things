#!/usr/bin/env python3
"""Renormalize the balanced q=3 bridge at Sturmian convergent scales.

After the first appended block, the 3/4 block indicator is the
characteristic Sturmian word of slope

    beta = 2/log2(3/2) - 3.

Its standard prefixes obey S_k = S_(k-1)^a_k S_(k-2).  This script composes
their exact relaxed integral bridges without expanding the words.  It reports
the 2-adic valuation of the one cross-congruence whose failure forces a
nonzero renormalized lift.  All results are finite diagnostics.
"""

import argparse
from dataclasses import dataclass
from decimal import Decimal, localcontext

from explore_balanced_q3_zero_cylinders import BLOCK_DATA, mechanical_blocks


@dataclass(frozen=True)
class Bridge:
    blocks: int
    odd_steps: int
    valuation: int
    odd_power: int
    two_power: int
    start: int
    endpoint: int


IDENTITY = Bridge(0, 0, 0, 1, 1, 0, 0)


def atom(block_steps):
    valuation, correction, start = BLOCK_DATA[block_steps]
    odd_power = 3**block_steps
    two_power = 1 << valuation
    endpoint = 20
    assert odd_power * start + correction == two_power * endpoint
    return Bridge(
        1,
        block_steps,
        valuation,
        odd_power,
        two_power,
        start,
        endpoint,
    )


def compose(left, right):
    """Compose bridge words left then right, returning state and lift."""
    lift = (
        (right.start - left.endpoint)
        * pow(left.odd_power, -1, right.two_power)
    ) % right.two_power
    carry_numerator = (
        left.endpoint
        + lift * left.odd_power
        - right.start
    )
    assert carry_numerator % right.two_power == 0
    carry = carry_numerator // right.two_power
    assert 0 <= carry < left.odd_power

    result = Bridge(
        left.blocks + right.blocks,
        left.odd_steps + right.odd_steps,
        left.valuation + right.valuation,
        left.odd_power * right.odd_power,
        left.two_power * right.two_power,
        left.start + lift * left.two_power,
        right.endpoint + carry * right.odd_power,
    )
    assert 0 <= result.start < result.two_power
    assert 0 <= result.endpoint < result.odd_power
    return result, lift


def power(state, exponent):
    result = IDENTITY
    base = state
    remaining = exponent
    while remaining:
        if remaining & 1:
            result, _ = compose(result, base)
        remaining >>= 1
        if remaining:
            base, _ = compose(base, base)
    return result


def fold(block_plan):
    result = IDENTITY
    for block_steps in block_plan:
        result, _ = compose(result, atom(block_steps))
    return result


def v2(value):
    if value == 0:
        return None
    value = abs(value)
    return (value & -value).bit_length() - 1


def continued_fraction(max_denominator, precision):
    with localcontext() as context:
        context.prec = precision
        beta = (
            Decimal(2)
            / (Decimal(3).ln() / Decimal(2).ln() - Decimal(1))
            - Decimal(3)
        )
        value = beta
        p_previous, p = 0, 1
        q_previous, q = 1, 0
        rows = []
        for _ in range(128):
            partial_quotient = int(value)
            p_previous, p = p, partial_quotient * p + p_previous
            q_previous, q = q, partial_quotient * q + q_previous
            if q > max_denominator:
                break
            if q > 0:
                rows.append((partial_quotient, p, q))
            remainder = value - partial_quotient
            if remainder == 0:
                break
            value = Decimal(1) / remainder
    return rows


def analyse(max_denominator, precision=120, direct_check=5000):
    cf = continued_fraction(max_denominator, precision)
    confirmation = continued_fraction(max_denominator, precision + 30)
    if cf != confirmation:
        raise ValueError("continued fraction is unstable at this precision")
    if len(cf) < 4:
        raise ValueError("max-denominator must reach the convergent 7")

    # Skipping the first appended block changes the lower mechanical word
    # into the characteristic word.  Its q=2 and q=5 prefixes seed the
    # standard recursion from q=7 onward.
    seed_plan = mechanical_blocks(5, phase=1)
    states = {
        2: fold(seed_plan[:2]),
        5: fold(seed_plan[:5]),
    }
    direct_plan = (
        mechanical_blocks(direct_check, phase=1)
        if direct_check > 0
        else []
    )
    rows = []

    for index in range(3, len(cf)):
        partial_quotient, numerator, denominator = cf[index]
        previous_denominator = cf[index - 1][2]
        tail_denominator = cf[index - 2][2]
        repeated = power(states[previous_denominator], partial_quotient)
        difference = repeated.endpoint - states[tail_denominator].start
        state, top_lift = compose(repeated, states[tail_denominator])
        assert state.blocks == denominator
        states[denominator] = state

        if denominator <= direct_check:
            assert state == fold(direct_plan[:denominator])

        difference_valuation = v2(difference)
        assert (top_lift == 0) == (difference_valuation is None)
        if difference_valuation is not None:
            assert difference_valuation == v2(top_lift)

        rows.append(
            {
                "index": index,
                "a": partial_quotient,
                "p": numerator,
                "Q": denominator,
                "tail_Q": tail_denominator,
                "tail_E": states[tail_denominator].valuation,
                "difference_v2": difference_valuation,
                "difference_sign": (difference > 0) - (difference < 0),
                "top_lift": top_lift,
                "top_lift_bits": top_lift.bit_length(),
                "top_lift_gap": (
                    states[tail_denominator].valuation
                    - top_lift.bit_length()
                ),
                "repeated_endpoint_mod32": repeated.endpoint % 32,
                "tail_start_mod32": states[tail_denominator].start % 32,
            }
        )
    return rows


def print_report(rows):
    print("== Balanced q=3 Sturmian bridge renormalization ==")
    print(f"renormalized convergent transitions={len(rows)}")
    finite_valuations = [
        row["difference_v2"]
        for row in rows
        if row["difference_v2"] is not None
    ]
    print(
        "top-level standard lifts nonzero: "
        f"{len(finite_valuations)}/{len(rows)}"
    )
    if finite_valuations:
        print(f"largest observed cross-difference v2={max(finite_valuations)}")
    for row in rows:
        valuation = (
            "infinity"
            if row["difference_v2"] is None
            else str(row["difference_v2"])
        )
        print(
            f"  k={row['index']:2d} Q={row['Q']:8d} "
            f"a={row['a']:2d} tail_Q={row['tail_Q']:7d} "
            f"tail_E={row['tail_E']:8d} v2(diff)={valuation:>8} "
            f"lift_gap={row['top_lift_gap']:3d} "
            f"low32={row['repeated_endpoint_mod32']:2d}/"
            f"{row['tail_start_mod32']:2d}"
        )


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-denominator", type=int, default=111457)
    parser.add_argument("--precision", type=int, default=120)
    parser.add_argument(
        "--direct-check",
        type=int,
        default=5000,
        help="largest expanded characteristic prefix checked independently",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    rows = analyse(
        args.max_denominator,
        args.precision,
        args.direct_check,
    )
    print_report(rows)


if __name__ == "__main__":
    main()
