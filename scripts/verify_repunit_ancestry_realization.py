#!/usr/bin/env python3
"""Verify the q=2 automatic-realisation lemma.

For a positive valuation word w of length i and total u, let

    A_i(w) = -3^i + 2 sum_{s<i} 3^(i-1-s) 2^Q_s.

The lemma proved in primitive_ancestry_lemma.md, Section 9A, says that for a
realised q=2 high payout, an equality A_i(w) = C at an admissible aligned
source length automatically realises w on the smaller repunit exponent. No
additional source-prefix congruence is needed.

This verifier checks:

* the exact-itinerary criterion for every composition through total 11;
* the normal-form identity A_i = 2c_i - 3^i;
* every compatible q=2 correction match for even totals 6..14, high lengths
  2..4, after filtering the high word to the odd repunit curve;
* source-word realisation, Y = 4X+1, and exact next-step merging.
"""

from functools import lru_cache


def v2(n):
    assert n != 0
    return (n & -n).bit_length() - 1


def odd_step(x):
    t = 3 * x + 1
    e = v2(t)
    return t >> e, e


def repunit(n):
    return (3**n - 1) // 2


def compositions(total, parts):
    if parts == 1:
        yield (total,)
        return
    for first in range(1, total - parts + 2):
        for tail in compositions(total - first, parts - 1):
            yield (first,) + tail


def c_of(word):
    k = len(word)
    prefix = 0
    c = 0
    for index, e in enumerate(word):
        c += 3 ** (k - 1 - index) * 2**prefix
        prefix += e
    return c


def A_of(word):
    return 2 * c_of(word) - 3 ** len(word)


def follow_word(x, word):
    for expected in word:
        x, observed = odd_step(x)
        assert observed == expected, (word, expected, observed)
    return x


def starting_residue(word):
    """Unique odd x mod 2^(u+1) realising word."""
    u = sum(word)
    modulus = 1 << (u + 1)
    return ((1 << u) - c_of(word)) * pow(3 ** len(word), -1, modulus) % modulus


@lru_cache(maxsize=None)
def power_log_table(u):
    """Map 3^n mod 2^(u+2) to n modulo its order 2^u."""
    modulus = 1 << (u + 2)
    order = 1 << u
    table = {}
    value = 1
    for n in range(order):
        table[value] = n
        value = value * 3 % modulus
    assert value == 1
    return table, order


def repunit_exponent_class(word):
    """Return n mod 2^u for which a_n realises word, or None."""
    u = sum(word)
    residue = starting_residue(word)
    target = (2 * residue + 1) % (1 << (u + 2))
    table, order = power_log_table(u)
    n = table.get(target)
    if n is None:
        return None
    return n, order


def verify_itinerary_criterion(max_total=11):
    checked = 0
    for total in range(1, max_total + 1):
        for parts in range(1, total + 1):
            for word in compositions(total, parts):
                x = starting_residue(word)
                assert x & 1
                numerator = 3**parts * x + c_of(word)
                assert v2(numerator) == total
                assert A_of(word) == 2 * c_of(word) - 3**parts
                assert follow_word(x, word) == numerator >> total
                checked += 1
    print(f"Exact-itinerary criterion: PASS  ({checked} compositions, total <= {max_total})")


def verify_q2_matches():
    abstract_matches = 0
    realised_matches = 0
    tested_high_words = 0
    cylinder_lifts = 0

    for u in range(6, 15, 2):
        source_layers = {}
        for i in range(4, u + 1):
            layer = {}
            for word in compositions(u, i):
                layer.setdefault(A_of(word), []).append(word)
            source_layers[i] = layer

        for j in range(2, min(4, u - 2) + 1):
            for high in compositions(u, j):
                C = 3 * A_of(high) + 2 ** (u + 2)
                full_high = high + (2,)
                exponent_class = repunit_exponent_class(full_high)
                if exponent_class is not None and exponent_class[0] & 1:
                    tested_high_words += 1

                for i in range(j + 2, u + 1):
                    if i % 2 != (j + 1) % 2:
                        continue
                    matches = source_layers[i].get(C, ())
                    abstract_matches += len(matches)
                    if matches:
                        exact_upper = (
                            3 * 2 ** (u - j + 1) * (3**j - 2**j)
                            - 3 ** (j + 1)
                            + 2 ** (u + 2)
                        )
                        assert 3**i - 2 ** (i + 1) <= exact_upper
                        # Integer form of
                        # 3^(i-1) < 2^u (6(3/2)^j + 4).
                        assert 3 ** (i - 1) * 2**j < 2**u * (
                            6 * 3**j + 4 * 2**j
                        )
                    if not matches or exponent_class is None:
                        continue

                    n0, period = exponent_class
                    if not n0 & 1:
                        continue

                    # Lift within the exponent class until m=n+j+1-i is a
                    # positive odd integer. Parity is already forced by i.
                    n = n0
                    if n < 3:
                        n += period
                    while n + j + 1 - i < 1:
                        n += period
                    m = n + j + 1 - i
                    assert 0 < m < n and (m & 1) and (n & 1)

                    high_start = repunit(n)
                    X = follow_word(high_start, full_high)

                    for source in matches:
                        Y = follow_word(repunit(m), source)
                        assert Y == 4 * X + 1
                        merged_from_y, _ = odd_step(Y)
                        merged_from_x, _ = odd_step(X)
                        assert merged_from_y == merged_from_x
                        realised_matches += 1

                        if u <= 10:
                            lifted_n = n + period
                            lifted_m = lifted_n + j + 1 - i
                            lifted_X = follow_word(repunit(lifted_n), full_high)
                            lifted_Y = follow_word(repunit(lifted_m), source)
                            assert lifted_Y == 4 * lifted_X + 1
                            assert odd_step(lifted_Y)[0] == odd_step(lifted_X)[0]
                            cylinder_lifts += 1

    assert realised_matches > 0
    print(
        "q=2 automatic realisation: PASS  "
        f"({tested_high_words} realised high words, "
        f"{abstract_matches} abstract matches, "
        f"{realised_matches} realised aligned matches)"
    )
    print("q=2 critical source-length bound: PASS  (all abstract matches above)")
    assert cylinder_lifts > 0
    print(f"q=2 cylinder dichotomy: PASS  ({cylinder_lifts} lifted matches)")


if __name__ == "__main__":
    verify_itinerary_criterion()
    verify_q2_matches()
    print("\nAll checks passed.")
