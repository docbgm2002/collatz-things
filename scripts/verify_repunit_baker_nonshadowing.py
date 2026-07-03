#!/usr/bin/env python3
"""Verify the finite ingredients of repunit_baker_nonshadowing.md.

This checks the exact enemy-branch equivalence
    (2, 1^{K-1})  <=>  v_2(3^{n+1} + 7) >= K + 3
and a finite logarithmic envelope. It does not trace full repunit orbits.
"""

import math

from verify_repunit_low_prefix import (
    N256,
    exponent_class,
    verify_modular_pattern,
    v2,
)


BAKER_SLOPE = 30.0
BAKER_OFFSET = 10.0


def enemy_valuation(n):
    """v_2(3^{n+1} + 7) using only the required 2-adic modulus."""
    bits = 64
    while True:
        modulus = 1 << bits
        residue = (pow(3, n + 1, modulus) + 7) % modulus
        if residue:
            return v2(residue)
        bits *= 2


def enemy_prefix_length(n):
    """Longest initial word (2, 1^{K-1}) forced by the enemy valuation."""
    enemy_v = enemy_valuation(n)
    if enemy_v < 4:
        return 0
    return enemy_v - 3


def enemy_pattern(length):
    return (2,) + (1,) * (length - 1)


def check_nested_classes():
    previous = None
    for K in range(1, 65):
        pattern = enemy_pattern(K)
        exponent, _E = exponent_class(pattern)
        enemy_v = enemy_valuation(exponent)

        assert verify_modular_pattern(exponent, pattern) == pattern
        assert enemy_v >= K + 3
        assert enemy_prefix_length(exponent) >= K

        if previous is not None:
            assert exponent % (1 << K) == previous
        previous = exponent

    pattern256 = enemy_pattern(256)
    exponent, _E = exponent_class(pattern256)
    assert exponent == N256
    assert verify_modular_pattern(exponent, pattern256) == pattern256
    assert enemy_valuation(exponent) >= 259
    assert enemy_prefix_length(exponent) >= 256

    print("BAKER1 nested enemy classes K=1..64 and K=256: PASS")


def observe_modular_pattern(exponent, pattern):
    """Return the realised valuation prefix, stopping at the first mismatch."""
    E = sum(pattern)
    modulus = 1 << (E + 1)
    x = ((pow(3, exponent, 1 << (E + 2)) - 1) // 2) % modulus

    observed = []
    for expected in pattern:
        value = 3 * x + 1
        valuation = v2(value)
        observed.append(valuation)
        if valuation != expected:
            return tuple(observed)
        x = value >> valuation
        modulus >>= valuation
        x %= modulus
    return tuple(observed)


def check_equivalence(limit=50001):
    """Bidirectional equivalence on odd exponents via modular prefix replay."""
    checked = 0
    for n in range(7, limit + 1, 2):
        enemy_v = enemy_valuation(n)
        prefix_len = enemy_prefix_length(n)

        if prefix_len >= 1:
            pattern = enemy_pattern(prefix_len)
            assert observe_modular_pattern(n, pattern) == pattern
            assert enemy_v == prefix_len + 3
            checked += 1

            longer = enemy_pattern(prefix_len + 1)
            assert observe_modular_pattern(n, longer) != longer

    assert checked > 0
    print(
        "BAKER2 enemy equivalence via valuation and modular replay "
        f"for odd 7 <= n <= {limit}: PASS ({checked} nontrivial samples)"
    )


def check_finite_log_envelope(limit=50001):
    worst_ratio = 0.0
    worst_case = None

    for n in range(7, limit + 1, 2):
        prefix_len = enemy_prefix_length(n)
        if prefix_len < 3:
            continue

        bound = BAKER_SLOPE * math.log2(n + 1) + BAKER_OFFSET
        assert prefix_len <= bound, (n, prefix_len, bound)
        ratio = prefix_len / math.log2(n + 1)
        if ratio > worst_ratio:
            worst_ratio = ratio
            worst_case = (n, prefix_len, enemy_valuation(n))

    assert worst_case is not None
    n, prefix_len, enemy_v = worst_case
    print(
        "BAKER3 finite logarithmic envelope "
        f"K <= {BAKER_SLOPE:g} log2(n+1) + {BAKER_OFFSET:g} "
        f"for odd 7 <= n <= {limit}: PASS "
        f"(worst ratio {worst_ratio:.3f} at n={n}, K={prefix_len}, "
        f"v2(3^(n+1)+7)={enemy_v})"
    )


def main():
    check_nested_classes()
    check_equivalence()
    check_finite_log_envelope()
    print("BAKER: PASS")


if __name__ == "__main__":
    main()
