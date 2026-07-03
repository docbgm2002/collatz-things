#!/usr/bin/env python3
"""Verify finite ingredients of repunit_rail5_survivor_geometry.md."""

from itertools import product
from math import isclose, log2, sqrt


def v2(n):
    return (n & -n).bit_length() - 1


def f(x):
    value = 3 * x + 1
    return value >> v2(value)


def phi_mod(e, y, bits):
    """Return the 2-adic inverse branch modulo 2^bits."""
    modulus = 1 << bits
    inverse_3 = pow(3, -1, modulus)
    return (((1 << e) * y - 1) * inverse_3) % modulus


def valuation_word(x, length):
    word = []
    for _ in range(length):
        e = v2(3 * x + 1)
        word.append(e)
        x = f(x)
    return tuple(word)


def base9_repunit_mod(m, modulus):
    return ((pow(9, m, 8 * modulus) - 1) // 8) % modulus


def check_inverse_branches(bits=14):
    modulus = 1 << bits
    for y in range(1, modulus, 2):
        for e in (1, 2):
            x = phi_mod(e, y, bits)
            assert x & 1
            assert v2(3 * x + 1) == e
            assert f(x) % (1 << (bits - e)) == y % (1 << (bits - e))

    residues_1 = {phi_mod(1, y, 3) for y in range(1, 8, 2)}
    residues_2 = {phi_mod(2, y, 3) for y in range(1, 8, 2)}
    assert residues_1 == {3, 7}
    assert residues_2 == {1}
    assert residues_1.isdisjoint(residues_2)
    print("SG1 inverse branches and disjoint images: PASS")


def check_similarity(limit=129, bits=12):
    odds = list(range(1, limit, 2))
    for e in (1, 2):
        for i, y in enumerate(odds):
            for z in odds[:i]:
                delta = (
                    phi_mod(e, y, bits) - phi_mod(e, z, bits)
                ) % (1 << bits)
                assert v2(delta) == v2(y - z) + e
    print("SG2 exact 2-adic contraction ratios: PASS")


def check_word_cylinders(max_k=8):
    for k in range(max_k + 1):
        bits = 2 * k + 1
        modulus = 1 << bits
        odds = range(1, modulus, 2)
        counts = {}
        for x in odds:
            word = valuation_word(x, k)
            if all(e in (1, 2) for e in word):
                counts[word] = counts.get(word, 0) + 1

        assert len(counts) == 2**k
        for word in product((1, 2), repeat=k):
            total = sum(word)
            assert counts[word] == 1 << (2 * k - total)
        assert sum(counts.values()) == 3**k
    print(f"SG3 valuation-word cylinders and counts: PASS (K=0..{max_k})")


def check_weighted_sums(max_k=12):
    phi_golden = (1 + sqrt(5)) / 2
    dimension = log2(phi_golden)
    assert isclose(2 ** (-dimension) + 2 ** (-2 * dimension), 1.0)

    for k in range(max_k + 1):
        weight = sum(
            2 ** (-dimension * sum(word))
            for word in product((1, 2), repeat=k)
        )
        assert isclose(weight, 1.0, rel_tol=1e-12, abs_tol=1e-12)

        haar_weight = sum(
            2 ** (-sum(word)) for word in product((1, 2), repeat=k)
        )
        assert isclose(haar_weight, (3 / 4) ** k)
    print(
        "SG4 Haar decay and golden-ratio dimension equation: PASS "
        f"(dimension={dimension:.10f})"
    )


def check_repunit_transfer(max_q=11):
    for q in range(2, max_q + 1):
        modulus = 1 << q
        odds = list(range(1, modulus, 2))
        images = [base9_repunit_mod(m, modulus) for m in odds]
        assert set(images) == set(odds)
        for i, m in enumerate(odds):
            for ell in odds[:i]:
                delta_m = v2(m - ell)
                delta_b = v2(
                    base9_repunit_mod(m, 1 << (q + 1))
                    - base9_repunit_mod(ell, 1 << (q + 1))
                )
                assert min(delta_b, q) == delta_m
    print(
        "SG5 base-9 isometry and repunit-index transfer: PASS "
        f"(q=2..{max_q})"
    )


def check_trivial_survivor(steps=100):
    x = 1
    for _ in range(steps):
        assert x % 8 != 5
        assert v2(3 * x + 1) == 2
        x = f(x)
    assert x == 1
    print("SG6 trivial positive survivor n=1: PASS")


if __name__ == "__main__":
    check_inverse_branches()
    check_similarity()
    check_word_cylinders()
    check_weighted_sums()
    check_repunit_transfer()
    check_trivial_survivor()
