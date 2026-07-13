#!/usr/bin/env python3
"""Measure finite proxies for the IEF13--IEF21 residual criteria.

The report gives the largest critical discrepancy over every factor in a
finite prefix and the best eventually-periodic prefix agreement at selected
footprint scales.  It also reports cumulative drift S and the IEF15 suffix
partition Z, normalized density drift S/L, and its range over the final half
of the prefix. Each approximant also reports the IEF20 drift envelope D and
the IEF21 terminal draw-up H and endpoint loss. No finite statistic proves an
infinite criterion; the script is a classifier for experiments.
"""

import argparse
from math import isclose, log2

from explore_balanced_q3_sturmian_intercepts import (
    best_completion,
    eventually_periodic_inverse,
    mechanical_word,
)
from verify_balanced_q3_periodic_approximants import expand_blocks


def flip(word, positions):
    result = list(word)
    for position in positions:
        if position < len(result):
            result[position] = 7 - result[position]
    return result


def make_family(name, blocks, intercept, precision):
    base = mechanical_word(blocks, intercept, precision)
    if name == "mechanical":
        return base
    if name == "square-flips":
        positions = (index * index for index in range(1, blocks))
        return flip(base, positions)
    if name == "periodic-17-flips":
        return flip(base, range(16, blocks, 17))
    if name == "negative-bias":
        result = list(base)
        for position in range(9, blocks, 10):
            if result[position] == 4:
                result[position] = 3
        return result
    if name == "xorshift":
        result = []
        state = 0x6D2B79F5
        threshold = int((2 / log2(3 / 2) - 3) * (1 << 32))
        for _ in range(blocks):
            state ^= state << 13 & 0xFFFFFFFF
            state ^= state >> 17
            state ^= state << 5 & 0xFFFFFFFF
            state &= 0xFFFFFFFF
            result.append(4 if state < threshold else 3)
        return result
    raise ValueError(f"unknown family: {name}")


def discrepancy(word):
    c = log2(3 / 2)
    prefix = 0.0
    minimum = 0.0
    maximum = 0.0
    for block in word:
        prefix += c * block - 2
        minimum = min(minimum, prefix)
        maximum = max(maximum, prefix)
    return maximum - minimum


def drift_envelope(word):
    c = log2(3 / 2)
    cumulative = 0.0
    envelope = 0.0
    for block in word:
        cumulative += c * block - 2
        envelope = max(envelope, abs(cumulative))
    return envelope


def cumulative_drift(word):
    c = log2(3 / 2)
    return sum(c * block - 2 for block in word)


def block_directional_budget(word):
    c = log2(3 / 2)
    cumulative = 0.0
    minimum = 0.0
    for block in word:
        cumulative += c * block - 2
        minimum = min(minimum, cumulative)
    return cumulative - minimum


def drift_partition(word):
    c = log2(3 / 2)
    cumulative = 0.0
    partition = 0.0
    tail_ratios = []
    tail_start = max(1, len(word) // 2)
    for index, block in enumerate(word, start=1):
        increment = c * block - 2
        cumulative += increment
        partition = 1 + 2**increment * partition
        if index >= tail_start:
            tail_ratios.append(cumulative / index)
    return cumulative, partition, min(tail_ratios), max(tail_ratios)


def directional_budget(bits):
    log_three = log2(3)
    total = bits.count("1") * log_three - len(bits)
    suffix = 0.0
    maximum_suffix = 0.0
    for bit in reversed(bits):
        suffix += log_three - 1 if bit == "1" else -1
        maximum_suffix = max(maximum_suffix, suffix)
    return max(0.0, total, maximum_suffix)


def verify_directional_identity(max_blocks):
    checked = 0
    for length in range(max_blocks + 1):
        for mask in range(1 << length):
            word = [3 + ((mask >> index) & 1) for index in range(length)]
            parity_cost = directional_budget(expand_blocks(word))
            block_cost = block_directional_budget(word)
            assert isclose(
                parity_cost,
                block_cost,
                rel_tol=1e-12,
                abs_tol=1e-12,
            )
            checked += 1
    return checked


def analyse(word, caps):
    rows = []
    for cap in caps:
        ratio, agreement, preperiod, period = best_completion(word, cap)
        footprint = word[: preperiod + period]
        preperiod_bits = expand_blocks(word[:preperiod])
        period_bits = expand_blocks(word[preperiod : preperiod + period])
        footprint_bits = len(preperiod_bits) + len(period_bits)
        agreement_bits = len(expand_blocks(word[:agreement]))
        critical_envelope = drift_envelope(word[:agreement])
        critical_ratio = critical_envelope / max(preperiod + period, 1)
        local_discrepancy = discrepancy(footprint)
        coarse_margin = (
            agreement_bits
            - footprint_bits
            - 2 * local_discrepancy
            - 2 * log2(max(footprint_bits, 2))
        )
        directional_cost = directional_budget(preperiod_bits) + directional_budget(
            period_bits
        )
        block_directional_cost = block_directional_budget(
            word[:preperiod]
        ) + block_directional_budget(
            word[preperiod : preperiod + period]
        )
        assert isclose(
            directional_cost,
            block_directional_cost,
            rel_tol=1e-12,
            abs_tol=1e-12,
        )
        endpoint_loss = max(
            0.0,
            cumulative_drift(footprint) - cumulative_drift(word[:agreement]),
        )
        directional_ratio = block_directional_cost / max(preperiod + period, 1)
        endpoint_loss_ratio = endpoint_loss / max(preperiod + period, 1)
        directional_margin = (
            agreement_bits
            - footprint_bits
            - directional_cost
            - 2 * log2(max(footprint_bits, 2))
        )
        numerator, denominator = eventually_periodic_inverse(
            preperiod_bits, period_bits
        )
        exact_height_bits = max(
            abs(numerator).bit_length(), abs(denominator).bit_length()
        )
        exact_margin = agreement_bits - exact_height_bits
        rows.append(
            (
                cap,
                ratio,
                agreement,
                preperiod,
                period,
                critical_envelope,
                critical_ratio,
                block_directional_cost,
                directional_ratio,
                endpoint_loss,
                endpoint_loss_ratio,
                local_discrepancy,
                coarse_margin,
                directional_margin,
                exact_margin,
            )
        )
    return discrepancy(word), rows


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--blocks", type=int, default=2000)
    parser.add_argument("--caps", default="32,64,128,256")
    parser.add_argument(
        "--families",
        default=(
            "mechanical,square-flips,periodic-17-flips,negative-bias,xorshift"
        ),
    )
    parser.add_argument("--intercept", default="0.314159")
    parser.add_argument("--precision", type=int, default=100)
    parser.add_argument("--identity-check-blocks", type=int, default=12)
    return parser.parse_args()


def main():
    args = parse_args()
    caps = [int(value) for value in args.caps.split(",")]
    print("== IEF13--IEF21 residual diagnostics ==")
    print(f"prefix blocks={args.blocks}")
    checked = verify_directional_identity(args.identity_check_blocks)
    print(
        "IEF21 exact directional identity "
        f"checked on {checked} words through {args.identity_check_blocks} blocks"
    )
    print(f"FIN1 suffix-partition cutoff={64 * 1_000_000 / 65:.6f}")
    for family in args.families.split(","):
        word = make_family(family, args.blocks, args.intercept, args.precision)
        factor_discrepancy, rows = analyse(word, caps)
        cumulative, partition, tail_min, tail_max = drift_partition(word)
        print(
            f"family={family} max_factor_discrepancy={factor_discrepancy:.6f} "
            f"S={cumulative:.6f} S/L={cumulative / len(word):.8f} "
            f"Z={partition:.6f} tail_S/L=[{tail_min:.8f},{tail_max:.8f}]"
        )
        for (
            cap,
            ratio,
            agreement,
            preperiod,
            period,
            critical_envelope,
            critical_ratio,
            block_directional_cost,
            directional_ratio,
            endpoint_loss,
            endpoint_loss_ratio,
            local_discrepancy,
            coarse_margin,
            directional_margin,
            exact_margin,
        ) in rows:
            side = "positive-surplus" if ratio > 1 else "no-surplus"
            print(
                f"  cap={cap:3d} U={preperiod:3d} V={period:3d} "
                f"L={agreement:4d} ratio={ratio:.3f} {side}"
                f" D={critical_envelope:7.3f} D/(U+V)={critical_ratio:8.5f}"
                f" H={block_directional_cost:7.3f} H/(U+V)={directional_ratio:8.5f}"
                f" loss/(U+V)={endpoint_loss_ratio:8.5f}"
                f" K={local_discrepancy:7.3f} coarse={coarse_margin:8.2f}"
                f" directional={directional_margin:8.2f}"
                f" exact={exact_margin:6d}"
            )


if __name__ == "__main__":
    main()
