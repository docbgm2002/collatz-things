#!/usr/bin/env python3
"""Verify and illustrate the Haar-random Collatz valuation model.

The probability statements concern uniformly distributed odd residue classes.
The optional repunit census uses a fixed window and is descriptive only.
"""

import math
import sys
from collections import Counter
from itertools import product


LOG2_3 = math.log2(3)
MEAN_SURPLUS = 2.0 - LOG2_3


def v2(n):
    return (n & -n).bit_length() - 1


def odd_step(x):
    value = 3 * x + 1
    e = v2(value)
    return value >> e, e


def rate_function(s):
    """Base-2 Cramer rate for e-log2(3), e~Geometric(1/2)."""
    u = s + LOG2_3
    if u < 1.0:
        return math.inf
    if math.isclose(u, 1.0, abs_tol=1e-14):
        return 1.0
    return u + (u - 1.0) * math.log2(u - 1.0) - u * math.log2(u)


def check_moments():
    # Closed-form geometric sums:
    # sum k/2^k = 2 and sum k^2/2^k = 6.
    mean_e = 2.0
    variance_e = 6.0 - mean_e**2
    expected_multiplier = 3.0 * (1.0 / 4.0) / (1.0 - 1.0 / 4.0)

    assert expected_multiplier == 1.0
    assert variance_e == 2.0
    assert math.isclose(LOG2_3 - mean_e, -0.4150374992788439)
    assert math.isclose(math.log(3 / 4), -0.2876820724517809)
    print("M1 multiplier martingale and log moments: PASS")


def valuation_word(x, length):
    word = []
    for _ in range(length):
        x, e = odd_step(x)
        word.append(e)
    return tuple(word)


def check_pattern_counts(max_k=5, bits=16):
    modulus = 1 << bits
    odds = range(1, modulus, 2)

    for k in range(1, max_k + 1):
        counts = Counter(valuation_word(x, k) for x in odds)
        for word in product(range(1, bits), repeat=k):
            total = sum(word)
            if total <= bits - 1:
                assert counts[word] == 1 << (bits - 1 - total)

    print(
        "M2 exact independent-geometric pattern counts: PASS "
        f"(K=1..{max_k}, modulus=2^{bits})"
    )


def check_rate_function():
    lower = 1.0 - LOG2_3
    assert rate_function(lower - 1e-6) == math.inf
    assert rate_function(lower) == 1.0
    assert math.isclose(rate_function(MEAN_SURPLUS), 0.0, abs_tol=1e-14)

    expected = {
        0.234: 0.013018985621848778,
        0.117: 0.03784232975891966,
        0.0: 0.07931861277485552,
    }
    for s, target in expected.items():
        assert math.isclose(rate_function(s), target, rel_tol=1e-12)

    print("M3 cumulant/rate-function values and boundary: PASS")
    print("\nFixed-threshold rate table")
    print(f"{'surplus s':>12} {'I(s)':>12}")
    for s in (lower, 0.0, 0.117, 0.234, MEAN_SURPLUS):
        print(f"{s:12.6f} {rate_function(s):12.6f}")


def repunit_fixed_window(n, window):
    x = (3**n - 1) // 2
    total = 0
    for _ in range(window):
        x, e = odd_step(x)
        total += e
    surplus = total - window * LOG2_3
    return total, surplus


def describe_repunit_windows(limit=1001, window=32):
    """Print descriptive fixed-window data; no random-path claim is made."""
    rows = []
    for n in range(7, limit + 1, 2):
        total, surplus = repunit_fixed_window(n, window)
        standardized = (
            surplus - window * MEAN_SURPLUS
        ) / math.sqrt(2.0 * window)
        rows.append((standardized, n, total, surplus))

    rows.sort()
    mean_surplus = sum(row[3] for row in rows) / len(rows)
    print(
        "\nDescriptive repunit census "
        f"(odd 7 <= n <= {limit}, fixed K={window})"
    )
    print(f"count: {len(rows)}")
    print(f"mean observed surplus: {mean_surplus:.6f}")
    print(f"Haar-model mean surplus: {window * MEAN_SURPLUS:.6f}")
    print("lowest standardized values:")
    for z, n, total, surplus in rows[:5]:
        print(
            f"  n={n:5d} E_K={total:4d} "
            f"surplus={surplus:9.4f} fixed-K z={z:8.4f}"
        )
    print(
        "These fixed-window values are descriptive; the exponents are not "
        "asserted to be independent Haar samples."
    )


def main():
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 1001
    window = int(sys.argv[2]) if len(sys.argv) > 2 else 32
    if limit < 7 or window < 1:
        raise ValueError("require limit >= 7 and window >= 1")

    check_moments()
    check_pattern_counts()
    check_rate_function()
    describe_repunit_windows(limit, window)


if __name__ == "__main__":
    main()
