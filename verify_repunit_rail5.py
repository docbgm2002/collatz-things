#!/usr/bin/env python3
"""Verify the exact and bounded claims in repunit_rail5_exact.md."""


def v2(n):
    return (n & -n).bit_length() - 1


def f(x):
    value = 3 * x + 1
    return value >> v2(value)


def repunit(n):
    return (3**n - 1) // 2


def base9_repunit(m):
    return (9**m - 1) // 8


def check_r5_1(limit=2000):
    for n in range(1, limit, 2):
        expected_rail = 1 if n % 4 == 1 else 5
        assert repunit(n) % 8 == expected_rail
    print(f"R5.1 repunit rail classification: PASS (odd n < {limit})")


def check_r5_2_r5_3(limit=2000):
    for n in range(1, limit, 2):
        m = (n + 1) // 2
        expected = repunit(n + 1) >> (2 + v2(m))
        assert f(repunit(n)) == expected

        if n % 4 == 1:
            b = base9_repunit(m)
            assert f(repunit(n)) == b
            assert b % 8 == m % 8
    print(f"R5.2-R5.3 first-step formulas: PASS (odd n < {limit})")


def check_r5_4(limit=2000):
    # This complete residue calculation is the universal proof ingredient.
    expected_n_mod_128 = {
        1: 32,
        3: 16,
        5: 0,
        7: 112,
        9: 96,
        11: 80,
        13: 64,
        15: 48,
    }
    assert pow(9, 16, 128) == 1
    for residue, expected in expected_n_mod_128.items():
        assert (3 * pow(9, residue, 128) + 5) % 128 == expected

    expected_valuation = {1: 2, 3: 1, 7: 1, 9: 2, 11: 1, 13: 3, 15: 1}
    for m in range(1, limit, 2):
        valuation = v2(3 * base9_repunit(m) + 1)
        residue = m % 16
        if residue == 5:
            assert valuation >= 4
        else:
            assert valuation == expected_valuation[residue]
    print(
        "R5.4 base-9 valuation table: PASS "
        f"(universal mod-128 table; sampled odd m < {limit})"
    )


def check_r5_5_r5_6(limit=2000):
    first_step_rail = {1: 1, 5: 3, 9: 5, 13: 7}
    for n in range(1, limit, 4):
        assert f(repunit(n)) % 8 == first_step_rail[n % 16]

    successful_classes = []
    for n in range(1, 16, 2):
        starts_on_rail5 = n % 4 == 3
        reaches_on_step1 = n % 16 == 9
        if starts_on_rail5 or reaches_on_step1:
            successful_classes.append(n)
    assert successful_classes == [3, 7, 9, 11, 15]
    assert len(successful_classes) / 8 == 5 / 8
    print("R5.5-R5.6 first-step rails and exact density 5/8: PASS")


def check_r5_7(max_n=199):
    worst_steps = -1
    worst_indices = []
    within_five = 0
    total = 0

    for n in range(3, max_n + 1, 2):
        x = repunit(n)
        steps = 0
        while x % 8 != 5:
            x = f(x)
            steps += 1
            assert steps <= 100

        total += 1
        within_five += steps <= 5
        if steps > worst_steps:
            worst_steps = steps
            worst_indices = [n]
        elif steps == worst_steps:
            worst_indices.append(n)

    assert worst_steps == 12
    assert worst_indices == [17, 61]
    print(
        "R5.7 bounded rail-5 observation: PASS "
        f"(odd 3 <= n <= {max_n}; worst=12 at n={worst_indices}; "
        f"within 5 steps={within_five / total:.1%})"
    )


if __name__ == "__main__":
    check_r5_1()
    check_r5_2_r5_3()
    check_r5_4()
    check_r5_5_r5_6()
    check_r5_7()
