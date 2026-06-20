#!/usr/bin/env python3
"""Verify the finite ingredients of repunit_affine_tail_bound.md."""

import math
from fractions import Fraction


def v2(n):
    return (n & -n).bit_length() - 1


def log2_int(n):
    bits = n.bit_length()
    if bits <= 1022:
        return math.log2(n)
    shift = bits - 1022
    return shift + math.log2(n >> shift)


def check_recurrence(limit=121):
    for n in range(3, limit + 1, 2):
        a = (3**n - 1) // 2
        x = a
        c = 0
        E = 0
        q = Fraction(0)
        product = Fraction(1)

        for i in range(80):
            assert q == Fraction(c, 3**i * a)
            assert x * 2**E == 3**i * a + c

            next_q = q + Fraction(1 + q, 3 * x)
            product *= Fraction(3 * x + 1, 3 * x)

            c = 3 * c + 2**E
            value = 3 * x + 1
            e = v2(value)
            x = value >> e
            E += e
            q = next_q

            assert 1 + q == product

    print(f"AFF1 exact recurrence and product: PASS (odd n <= {limit})")


def check_bound_and_margin(limit=301):
    tested = 0
    for n in range(3, limit + 1, 2):
        a = (3**n - 1) // 2
        target = 2**n - 1
        x = a
        c = 0
        E = 0

        for k in range(1, 3 * n + 1):
            c = 3 * c + 2**E
            value = 3 * x + 1
            e = v2(value)
            x = value >> e
            E += e

            q = Fraction(c, 3**k * a)
            exact_penalty = math.log2(float(1 + q))
            exact_margin = log2_int(target) - log2_int(x)
            raw_surplus = (
                E
                - k * math.log2(3)
                - (log2_int(a) - log2_int(target))
            )
            assert abs(exact_margin - (raw_surplus - exact_penalty)) < 1e-10

            if x < target:
                break

            bound = k * math.log2(1 + 1 / (3 * target))
            # The floating expression underflows to zero for large n; the
            # exact rational comparison remains authoritative.
            exact_bound = Fraction(3 * target + 1, 3 * target) ** k
            assert 1 + q <= exact_bound
            assert exact_penalty <= bound + 1e-15
            tested += 1

    print(
        "AFF2 pre-descent bound and exact margin decomposition: PASS "
        f"({tested} finite states)"
    )


if __name__ == "__main__":
    check_recurrence()
    check_bound_and_margin()

