#!/usr/bin/env python3
"""Verify the exact extremal-storage and payout-ledger identities."""

from fractions import Fraction


def v2(value):
    return (value & -value).bit_length() - 1


def verify(limit=301, max_steps=400):
    transitions = 0
    record_steps = 0

    for n in range(3, limit + 1, 2):
        x = (3**n - 1) // 2
        E = 0
        A = -1
        R = 1
        payout_sum = Fraction(1, 2)
        largest_deficit_key = Fraction(1, 1)
        shell_positive = 0
        shell_negative = 0

        for K in range(max_steps):
            # B_K = R_K/(2*3^K) is the rational version of Z_K/2^D_K.
            B = Fraction(R, 2 * 3**K)
            assert B == payout_sum
            assert R == 3**K + shell_positive - shell_negative
            assert x + 1 == Fraction(3 ** (n + K), 2 ** (E + 1)) + Fraction(
                R, 2 ** (E + 1)
            )

            value = 3 * x + 1
            e = v2(value)
            next_x = value >> e
            next_A = 3 * A + 2 ** (E + 1)
            next_E = E + e
            next_R = next_A + 2 ** (next_E + 1)

            assert next_R == 3 * R + 2 ** (E + 1) * (2**e - 2)
            payout = 2 ** (E + 1) * (2**e - 2)
            next_shell_positive = 3 * shell_positive
            next_shell_negative = 3 * shell_negative
            if e % 2 == 1:
                gap = e - 1
                u = E + 1
                shell = 2 ** (u + 1) * (2**gap - 1) // 3
                assert payout == 3 * shell
                if e > 1:
                    next_shell_positive += 3 * shell
            else:
                gap = e
                u = E
                shell = 2 ** (u + 1) * (2**gap - 1) // 3
                smallest_shell = 2 ** (E + 1) * (2**2 - 1) // 3
                assert smallest_shell == 2 ** (E + 1)
                assert payout == 3 * shell - smallest_shell
                next_shell_positive += 3 * shell
                next_shell_negative += smallest_shell
            if e >= 2:
                h = e // 2
                u = next_E - 2 * h
                collision_shell = (
                    2 ** (u + 1) * (2 ** (2 * h) - 1) // 3
                )
                partner = (
                    4**h * next_x
                    + (4**h - 1) // 3
                )
                partner_from_normal_form = (
                    3 ** (n + K + 1)
                    + next_A
                    + collision_shell
                ) // 2 ** (u + 1)
                assert partner == partner_from_normal_form
                assert partner % 2 == 1
                assert (
                    (3 * partner + 1) >> v2(3 * partner + 1)
                    == (3 * next_x + 1) >> v2(3 * next_x + 1)
                )
            assert next_R == (
                3 ** (K + 1)
                + next_shell_positive
                - next_shell_negative
            )
            Z = Fraction(R, 2 ** (E + 1))
            next_Z = Fraction(next_R, 2 ** (next_E + 1))
            assert next_Z == 1 + Fraction(3 * Z - 2, 2**e)
            if e == 1:
                assert next_Z == Fraction(3, 2) * Z
                # 2^D is represented by 3^K/2^E, so constancy of
                # D-log2(Z) is equivalent to constancy of 2^D/Z.
                assert Fraction(3 ** (K + 1), 2**next_E) / next_Z == (
                    Fraction(3**K, 2**E) / Z
                )

            # Avoid floating point: D_K records are ordered by
            # 3^K / 2^E.  A new strict record at K+1 can only have e=1.
            deficit_key = Fraction(3 ** (K + 1), 2**next_E)
            if deficit_key > largest_deficit_key:
                assert e == 1
                largest_deficit_key = deficit_key
                record_steps += 1

            if e > 1:
                payout_sum += Fraction(
                    (2**e - 2) * 2**E,
                    3 ** (K + 1),
                )

            x = next_x
            E = next_E
            A = next_A
            R = next_R
            shell_positive = next_shell_positive
            shell_negative = next_shell_negative
            transitions += 1

    print(
        "REPEXT storage recurrence and payout ledger: PASS "
        f"({transitions} transitions, {record_steps} record steps)"
    )


if __name__ == "__main__":
    verify()
