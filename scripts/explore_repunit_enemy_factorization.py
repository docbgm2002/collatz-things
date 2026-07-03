#!/usr/bin/env python3
"""Probe the arithmetic structure of repunit enemy constants.

For each primitive record-deficit prefix, the enemy equation is

    v2(3^m + d) >= E + 2,    3 does not divide d.

A multi-term p-adic logarithmic-form (Baker/Yu) bound on the valuation is
only useful when -d factors into a *bounded number* of *small-height*
algebraic pieces.  Concretely it helps when d is smooth (few small primes)
rather than a single large prime or a generic rough integer.

This script trial-divides each enemy constant up to a smoothness bound,
reports the smooth part and the remaining rough cofactor, and runs a
Miller-Rabin test on the rough cofactor.  The verdict decides whether the
"smoothness route" to a multi-term Baker bound is viable for the dangerous
high-height records, or whether the diffusion is genuinely unstructured.

Finite diagnostic only; no universal claim.
"""

import argparse
import math
import random
from collections import Counter

from explore_repunit_extremal_prefixes import census


def small_primes(bound):
    sieve = bytearray([1]) * (bound + 1)
    sieve[0:2] = b"\x00\x00"
    for i in range(2, int(bound**0.5) + 1):
        if sieve[i]:
            sieve[i * i :: i] = bytearray(len(sieve[i * i :: i]))
    return [i for i in range(2, bound + 1) if sieve[i]]


def smooth_factor(value, primes):
    """Trial-divide |value| by the given primes.

    Returns (distinct_small_primes, smooth_part_bitlength, rough_cofactor).
    """
    value = abs(value)
    distinct = 0
    smooth_part = 1
    for p in primes:
        if p * p > value:
            break
        if value % p == 0:
            distinct += 1
            while value % p == 0:
                value //= p
                smooth_part *= p
    if value > 1 and value <= primes[-1]:
        # remaining value is itself a small prime
        distinct += 1
        smooth_part *= value
        value = 1
    return distinct, smooth_part.bit_length() - 1, value


def is_probable_prime(n, rounds=20):
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for _ in range(rounds):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True


def analyze(limit, factor, bound, deficit_floor, max_rows):
    result, rows = census(limit, factor)

    selected = [
        row
        for row in rows
        if row["deficit"] >= deficit_floor or row["height_ratio"] <= 0.75
    ]
    selected.sort(key=lambda row: row["deficit"], reverse=True)
    selected = selected[:max_rows]

    primes = small_primes(bound)
    analyzed = []
    for row in selected:
        distinct, smooth_bits, rough = smooth_factor(row["d"], primes)
        rough_bits = rough.bit_length() if rough > 1 else 0
        rough_prime = rough > 1 and is_probable_prime(rough)
        analyzed.append(
            {
                **row,
                "small_primes": distinct,
                "smooth_bits": smooth_bits,
                "rough_bits": rough_bits,
                "rough_over_E": rough_bits / row["E"] if row["E"] else 0.0,
                "fully_smooth": rough == 1,
                "rough_prime": rough_prime,
            }
        )
    return result, rows, analyzed, primes


def print_report(result, rows, analyzed, primes, limit, bound, top):
    print("== Enemy-constant factorization probe ==")
    print(
        f"finite domain: odd 7 <= n <= {limit}; "
        f"primitive tails={len(result['primitives'])}; "
        f"record prefixes={len(rows)}; analyzed={len(analyzed)}; "
        f"smoothness bound={bound} ({len(primes)} primes)"
    )

    dangerous = [row for row in analyzed if row["deficit"] >= 2]
    print(
        f"\nDangerous records (D>=2) analyzed: {len(dangerous)}"
    )
    if dangerous:
        fully_smooth = sum(row["fully_smooth"] for row in dangerous)
        rough_prime = sum(row["rough_prime"] for row in dangerous)
        rough_ratios = sorted(row["rough_over_E"] for row in dangerous)
        median_rough = rough_ratios[len(rough_ratios) // 2]
        min_rough = rough_ratios[0]
        small_prime_counts = Counter(row["small_primes"] for row in dangerous)
        print(f"  fully {bound}-smooth:        {fully_smooth}/{len(dangerous)}")
        print(f"  rough cofactor is prime:  {rough_prime}/{len(dangerous)}")
        print(
            f"  rough_bits/E:  min={min_rough:.3f} "
            f"median={median_rough:.3f} max={rough_ratios[-1]:.3f}"
        )
        print(f"  #small-prime-factors distribution: {dict(sorted(small_prime_counts.items()))}")

    print("\nLargest-deficit records (factor structure):")
    for row in analyzed[:top]:
        tag = []
        if row["fully_smooth"]:
            tag.append("SMOOTH")
        elif row["rough_prime"]:
            tag.append("ROUGH-PRIME")
        else:
            tag.append("composite-rough")
        print(
            f"  n={row['n']:5d} K={row['K']:6d} E={row['E']:6d} "
            f"D={row['deficit']:8.4f} h/E={row['height_ratio']:.3f} "
            f"#sp={row['small_primes']:2d} "
            f"smooth_bits={row['smooth_bits']:5d} "
            f"rough_bits={row['rough_bits']:5d} "
            f"({row['rough_over_E']:.2f}E) {' '.join(tag)}"
        )

    low_height = [row for row in analyzed if row["height_ratio"] <= 0.75]
    print(f"\nLow-height records (h/E<=0.75) analyzed: {len(low_height)}")
    for row in sorted(low_height, key=lambda r: r["deficit"], reverse=True)[:top]:
        print(
            f"  n={row['n']:5d} K={row['K']:6d} E={row['E']:6d} "
            f"D={row['deficit']:8.4f} h/E={row['height_ratio']:.3f} "
            f"#sp={row['small_primes']:2d} rough_bits={row['rough_bits']:5d} "
            f"{'SMOOTH' if row['fully_smooth'] else ('ROUGH-PRIME' if row['rough_prime'] else 'composite-rough')}"
        )

    print("\nHeight x structure crosstab (all analyzed records):")
    crosstab = Counter()
    for row in analyzed:
        hi = row["height_ratio"] > 0.9
        if row["fully_smooth"]:
            kind = "smooth"
        elif row["rough_prime"]:
            kind = "rough-prime"
        else:
            kind = "composite-rough"
        crosstab[("h/E>0.9" if hi else "h/E<=0.9", kind)] += 1
    for height_band in ("h/E<=0.9", "h/E>0.9"):
        line = ", ".join(
            f"{kind}={crosstab[(height_band, kind)]}"
            for kind in ("smooth", "rough-prime", "composite-rough")
        )
        print(f"  {height_band}: {line}")
    smooth_high = sum(
        row["fully_smooth"] for row in analyzed if row["height_ratio"] > 0.9
    )
    print(
        f"  fully-smooth records with h/E>0.9: {smooth_high} "
        "(if 0, smoothness is a strict proxy for low height)"
    )

    print("\nVerdict:")
    if dangerous:
        structured = sum(
            row["fully_smooth"] or row["rough_over_E"] < 0.5
            for row in dangerous
        )
        frac = structured / len(dangerous)
        print(
            f"  {frac:.1%} of dangerous records have a smooth or "
            f"sub-half-height rough part."
        )
        if frac < 0.1:
            print(
                "  => Smoothness route is DEAD: dangerous enemy constants are "
                "generically rough/large-prime. Multi-term Baker via "
                "factorization will not control them."
            )
        elif frac > 0.5:
            print(
                "  => Smoothness route is LIVE: a large fraction of dangerous "
                "enemy constants factor into controllable pieces."
            )
        else:
            print(
                "  => Mixed: some dangerous enemy constants are structured. "
                "Worth isolating which payout ancestries produce them."
            )


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=2001)
    parser.add_argument("--factor", type=int, default=3)
    parser.add_argument("--bound", type=int, default=100000)
    parser.add_argument("--deficit-floor", type=float, default=1.0)
    parser.add_argument("--max-rows", type=int, default=300)
    parser.add_argument("--top", type=int, default=20)
    return parser.parse_args()


def main():
    args = parse_args()
    result, rows, analyzed, primes = analyze(
        args.limit,
        args.factor,
        args.bound,
        args.deficit_floor,
        args.max_rows,
    )
    print_report(result, rows, analyzed, primes, args.limit, args.bound, args.top)


if __name__ == "__main__":
    main()
