#!/usr/bin/env python3
"""Inspect record valuation deficits on primitive repunit tails.

This is a narrow diagnostic for the proposed extremal approach.  It removes
tails that merge into smaller exponents, then records only prefix times K at
which

    D_K = K log2(3) - E_K

sets a new maximum on that primitive tail.  At each such time it computes the
reduced enemy equation

    v2(3^m + d) >= E_K + 2,    3 does not divide d.

The output distinguishes low-height corrections, where an Archimedean or
Baker bound may be useful, from generic corrections that retain essentially
all of the 2-adic information.

All results are finite diagnostics, not universal claims.
"""

import argparse
import math
from collections import Counter

from explore_repunit_tail_merges import scan as scan_merges


THETA = math.log2(3)


def v2(value):
    return (value & -value).bit_length() - 1


def log2_int(value):
    bits = value.bit_length()
    if bits <= 1022:
        return math.log2(value)
    shift = bits - 1022
    return shift + math.log2(value >> shift)


def logaddexp2(a, b):
    hi = max(a, b)
    lo = min(a, b)
    if hi - lo > 55:
        return hi
    return hi + math.log2(1 + math.exp2(lo - hi))


def record_deficit_rows(n, sigma):
    x = (3**n - 1) // 2
    E = 0
    A = -1
    # D_0=0.  A strict record must exceed the initial state as well as all
    # later prefixes; starting at -infinity would incorrectly count K=1 on
    # tails whose first deficit is negative.
    record_K = 0
    record_E = 0
    payout_terms = []
    log_budget = -1.0

    for K in range(1, sigma):
        value = 3 * x + 1
        e = v2(value)
        x = value >> e
        A = 3 * A + (1 << (E + 1))
        E += e

        deficit = K * THETA - E
        if e > 1:
            log_weight = math.log2(1 - math.exp2(1 - e)) - deficit
            payout_terms.append(
                {
                    "step": K - 1,
                    "q": e,
                    "post_deficit": deficit,
                    "log_weight": log_weight,
                }
            )
            log_budget = logaddexp2(log_budget, log_weight)
        # Compare 3^K/2^E against the previous record 3^record_K/2^record_E
        # exactly.  This is equivalent to comparing D_K values without
        # relying on floating-point logarithms.
        if K >= record_K:
            is_record = 3 ** (K - record_K) > 2 ** (E - record_E)
        else:
            is_record = 2 ** (record_E - E) > 3 ** (record_K - K)
        if not is_record:
            continue
        record_K = K
        record_E = E

        R = A + (1 << (E + 1))
        r = 0
        d = R
        while d % 3 == 0:
            d //= 3
            r += 1
        m = n + K - r
        modulus = 1 << (E + 2)
        assert (pow(3, m, modulus) + d) % modulus == 0

        height = abs(d).bit_length()
        log_z_from_budget = deficit + log_budget
        log_z_exact = log2_int(R) - (E + 1)
        assert math.isclose(
            log_z_from_budget, log_z_exact, rel_tol=2e-12, abs_tol=2e-12
        )
        dominant = max(
            payout_terms,
            key=lambda term: term["log_weight"],
            default=None,
        )
        ranked_terms = sorted(
            payout_terms,
            key=lambda term: term["log_weight"],
            reverse=True,
        )
        top_shares = [
            sum(
                math.exp2(term["log_weight"] - log_budget)
                for term in ranked_terms[:count]
            )
            for count in (2, 3, 4)
        ]
        odd_payout_share = sum(
            math.exp2(term["log_weight"] - log_budget)
            for term in payout_terms
            if term["q"] % 2 == 1
        )
        yield {
            "n": n,
            "K": K,
            "E": E,
            "deficit": deficit,
            "e": e,
            "m": m,
            "d": d,
            "height": height,
            "height_ratio": height / E,
            "saving": E - height,
            "arch_side": max(m * THETA, math.log2(abs(d))),
            "log_budget": log_budget,
            "payout_count": len(payout_terms),
            "dominant_share": (
                math.exp2(dominant["log_weight"] - log_budget)
                if dominant is not None
                else 0.0
            ),
            "dominant_age": (
                K - 1 - dominant["step"] if dominant is not None else None
            ),
            "dominant_q": dominant["q"] if dominant is not None else None,
            "dominant_post_deficit": (
                dominant["post_deficit"] if dominant is not None else None
            ),
            "top2_share": top_shares[0],
            "top3_share": top_shares[1],
            "top4_share": top_shares[2],
            "odd_payout_share": odd_payout_share,
            "top_qs": tuple(term["q"] for term in ranked_terms[:4]),
        }


def census(limit, factor):
    merge_result = scan_merges(limit=limit, factor=factor)
    rows = []
    for primitive in merge_result["primitives"]:
        rows.extend(record_deficit_rows(primitive["n"], primitive["sigma"]))
    return merge_result, rows


def compact_integer(value):
    magnitude = abs(value)
    bits = magnitude.bit_length()
    if bits <= 80:
        return str(value)
    high = magnitude >> (bits - 24)
    low = magnitude & ((1 << 24) - 1)
    sign = "-" if value < 0 else ""
    return f"{sign}0x{high:06x}...{low:06x}({bits}b)"


def print_report(result, rows, limit, top):
    print("== Primitive record-deficit prefixes ==")
    print(
        f"finite domain: odd 7 <= n <= {limit}; "
        f"primitive tails={len(result['primitives'])}; "
        f"record prefixes={len(rows)}"
    )

    bands = Counter()
    for row in rows:
        ratio = row["height_ratio"]
        if ratio <= 0.50:
            bands["<=0.50"] += 1
        elif ratio <= 0.75:
            bands["0.50..0.75"] += 1
        elif ratio <= 1.00:
            bands["0.75..1.00"] += 1
        else:
            bands[">1.00"] += 1
    print(f"enemy-height bands: {dict(bands)}")

    ranked = sorted(
        rows,
        key=lambda row: (row["deficit"], row["K"], -row["height_ratio"]),
        reverse=True,
    )
    print("\nLargest record deficits:")
    for row in ranked[:top]:
        print(
            f"  n={row['n']:5d} K={row['K']:6d} E={row['E']:6d} "
            f"D={row['deficit']:10.4f} e={row['e']:2d} "
            f"h/E={row['height_ratio']:.4f} saving={row['saving']:4d} "
            f"dom={row['dominant_share']:.2%}/"
            f"{row['top3_share']:.2%}@-{row['dominant_age']} "
            f"odd={row['odd_payout_share']:.2%} qs={row['top_qs']} "
            f"m={row['m']:6d} d={compact_integer(row['d'])}"
        )

    low_height = sorted(
        (row for row in rows if row["height_ratio"] <= 0.75),
        key=lambda row: (row["deficit"], row["saving"]),
        reverse=True,
    )
    print(f"\nLow-height record prefixes (h/E <= 0.75): {len(low_height)}")
    for row in low_height[:top]:
        print(
            f"  n={row['n']:5d} K={row['K']:6d} E={row['E']:6d} "
            f"D={row['deficit']:10.4f} h={row['height']:5d} "
            f"saving={row['saving']:4d} m={row['m']:6d} "
            f"d={compact_integer(row['d'])}"
        )

    concentration = Counter()
    top3_concentration = Counter()
    for row in rows:
        share = row["dominant_share"]
        if share >= 0.75:
            concentration[">=0.75"] += 1
        elif share >= 0.50:
            concentration["0.50..0.75"] += 1
        elif share >= 0.25:
            concentration["0.25..0.50"] += 1
        else:
            concentration["<0.25"] += 1
        share3 = row["top3_share"]
        if share3 >= 0.90:
            top3_concentration[">=0.90"] += 1
        elif share3 >= 0.75:
            top3_concentration["0.75..0.90"] += 1
        elif share3 >= 0.50:
            top3_concentration["0.50..0.75"] += 1
        else:
            top3_concentration["<0.50"] += 1
    print(f"\nDominant payout share bands: {dict(concentration)}")
    print(f"Top-three payout share bands: {dict(top3_concentration)}")

    dangerous = [row for row in rows if row["deficit"] >= 2]
    if dangerous:
        print(
            "Dangerous records D>=2: "
            f"count={len(dangerous)} "
            f"min odd-payout share="
            f"{min(row['odd_payout_share'] for row in dangerous):.2%} "
            f"median="
            f"{sorted(row['odd_payout_share'] for row in dangerous)[len(dangerous)//2]:.2%}"
        )


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=2001)
    parser.add_argument("--factor", type=int, default=3)
    parser.add_argument("--top", type=int, default=20)
    return parser.parse_args()


def main():
    args = parse_args()
    result, rows = census(args.limit, args.factor)
    print_report(result, rows, args.limit, args.top)


if __name__ == "__main__":
    main()
