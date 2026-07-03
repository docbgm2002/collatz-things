#!/usr/bin/env python3
"""Verify the low-prefix construction."""

from explore_entropy_balance import discrete_log_base3


N256 = int(
    "45668407499936535198320256527201491097067812606246254032465685587732141442221"
)


def v2(n):
    return (n & -n).bit_length() - 1


def exact_pattern_class(pattern):
    K = len(pattern)
    E = sum(pattern)
    c = 0
    prefix = 0
    for i, valuation in enumerate(pattern):
        c += 3 ** (K - 1 - i) * (1 << prefix)
        prefix += valuation

    modulus = 1 << (E + 1)
    residue = ((1 << E) - c) * pow(3**K, -1, modulus) % modulus
    return residue, E


def exponent_class(pattern):
    residue, E = exact_pattern_class(pattern)
    target = (2 * residue + 1) % (1 << (E + 2))
    exponent = discrete_log_base3(target, E + 2)
    assert exponent is not None and exponent & 1
    return exponent, E


def verify_modular_pattern(exponent, pattern):
    E = sum(pattern)
    modulus = 1 << (E + 1)
    x = ((pow(3, exponent, 1 << (E + 2)) - 1) // 2) % modulus

    observed = []
    for expected in pattern:
        value = 3 * x + 1
        valuation = v2(value)
        observed.append(valuation)
        assert valuation == expected
        x = value >> valuation
        modulus >>= valuation
        x %= modulus
    return tuple(observed)


def main():
    previous = None
    for K in range(1, 65):
        pattern = (2,) + (1,) * (K - 1)
        exponent, E = exponent_class(pattern)
        assert E == K + 1
        assert verify_modular_pattern(exponent, pattern) == pattern
        assert (pow(3, exponent + 1, 1 << (K + 3)) + 7) % (1 << (K + 3)) == 0
        if exponent >= 3:
            assert K < (exponent + 1) * 1.584962500721156 - 2
        if previous is not None:
            assert exponent % (1 << (K + 0)) == previous
        previous = exponent

    pattern256 = (2,) + (1,) * 255
    exponent, E = exponent_class(pattern256)
    assert E == 257
    assert exponent == N256
    assert exponent.bit_length() == 255
    assert verify_modular_pattern(exponent, pattern256) == pattern256
    assert (pow(3, exponent + 1, 1 << 259) + 7) % (1 << 259) == 0
    assert 256 < (exponent + 1) * 1.584962500721156 - 2

    print(
        "LOWPREFIX: PASS "
        "(nested exact classes K=1..64; explicit K=256 residue and valuations)"
    )


if __name__ == "__main__":
    main()
