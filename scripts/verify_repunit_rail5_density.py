#!/usr/bin/env python3
"""Verify the claims in repunit_rail5_density.md."""


def v2(n):
    return (n & -n).bit_length() - 1


def f(x):
    value = 3 * x + 1
    return value >> v2(value)


def base9_repunit(m):
    return (9**m - 1) // 8


def base9_repunit_mod(m, modulus):
    """Return b_m modulo modulus, using a modulus that permits division by 8."""
    return ((pow(9, m, 8 * modulus) - 1) // 8) % modulus


def avoids_rail5(x, states):
    for _ in range(states):
        if x % 8 == 5:
            return False
        x = f(x)
    return True


def avoids_rail5_mod(x, bits, states):
    """Check a fixed avoidance window using only the required low bits."""
    modulus = 1 << bits
    x %= modulus
    for state in range(states):
        if x % 8 == 5:
            return False
        if state + 1 == states:
            return True

        valuation = v2(3 * x + 1)
        assert valuation in (1, 2)
        value = (3 * x + 1) % modulus
        x = value >> valuation
        bits -= valuation
        modulus >>= valuation
        x %= modulus
    return True


def check_isometry(limit=257):
    odds = list(range(1, limit, 2))
    for i, m in enumerate(odds):
        bm = base9_repunit(m)
        for ell in odds[:i]:
            assert v2(bm - base9_repunit(ell)) == v2(m - ell)

    for q in range(2, 11):
        modulus = 1 << q
        images = {
            base9_repunit_mod(m, modulus) for m in range(1, modulus, 2)
        }
        assert images == set(range(1, modulus, 2))
    print("D1 base-9 repunit isometry and residue permutations: PASS")


def check_odd_avoidance_counts(max_k=8):
    for k in range(max_k + 1):
        if k == 0:
            count = 1
        else:
            bits = 2 * k + 1
            modulus = 1 << bits
            count = sum(
                avoids_rail5_mod(x, bits, k) for x in range(1, modulus, 2)
            )
        assert count == 3**k
        assert count / (4**k) == (3 / 4) ** k
    print(f"D2 exact odd-start avoidance counts: PASS (K=0..{max_k})")


def check_repunit_index_counts(max_k=7):
    for k in range(max_k + 1):
        # Among one complete odd-index period modulo 2^(2K+2), half the
        # indices start on rail 5. The remaining n=4s+1 correspond bijectively
        # to odd m=(n+1)/2 modulo 2^(2K+1).
        if k == 0:
            survivor_count = 1
            odd_index_count = 2
        else:
            bits = 2 * k + 1
            modulus = 1 << bits
            survivor_count = 0
            for m in range(1, modulus, 2):
                x = base9_repunit_mod(m, modulus)
                survivor_count += avoids_rail5_mod(x, bits, k)
            odd_index_count = 2 * (4**k)

        assert survivor_count == 3**k
        expected = 0.5 * (0.75**k)
        assert survivor_count / odd_index_count == expected
    print(f"D3 exact repunit-index survivor counts: PASS (K=0..{max_k})")


def check_direct_complete_periods(max_k=4):
    for k in range(max_k + 1):
        period = 1 << (2 * k + 2)
        survivors = 0
        for n in range(1, period, 2):
            x = (3**n - 1) // 2
            if avoids_rail5(x, k + 1):
                survivors += 1
        assert survivors == 3**k
    print(
        "D4 direct complete exponent-period counts: PASS "
        f"(K=0..{max_k})"
    )


def check_finite_samples(max_n=4095, max_k=10):
    hit_times = []
    for n in range(1, max_n + 1, 2):
        x = (3**n - 1) // 2
        hit = None
        for k in range(max_k + 1):
            if x % 8 == 5:
                hit = k
                break
            x = f(x)
        hit_times.append(hit)

    total = len(hit_times)
    for k in range(max_k + 1):
        measured = sum(hit is not None and hit <= k for hit in hit_times) / total
        expected = 1 - 0.5 * (0.75**k)
        # This is a finite-prefix comparison, not a proof ingredient.
        assert abs(measured - expected) < 0.01
    print(
        "D5 finite repunit samples follow the density formula: PASS "
        f"(odd n <= {max_n}, K=0..{max_k})"
    )


if __name__ == "__main__":
    check_isometry()
    check_odd_avoidance_counts()
    check_repunit_index_counts()
    check_direct_complete_periods()
    check_finite_samples()
