#!/usr/bin/env python3
"""
Exploration: exponential-affine normal form for the repunit tail.

For x_0=a_n=(3^n-1)/2, write after i shortcut steps

    x_i = (3^(n+i) + A_i) / 2^(E_i+1),

where E_i is the cumulative valuation sum.  Then

    A_0 = -1,
    A_{i+1} = 3 A_i + 2^(E_i+1),
    e_i = v2(3^(n+i+1) + A_{i+1}) - (E_i+1).

This separates the moving exponential 3^n from a correction term A_i.
Research tool, not a proof.
"""


def v2(n):
    return (n & -n).bit_length() - 1 if n else 10 ** 9


def f_with_e(x):
    t = 3 * x + 1
    e = v2(t)
    return t >> e, e


def a(n):
    return (3 ** n - 1) // 2


def normal_tail(n, steps):
    x = a(n)
    A = -1
    E = 0
    rows = []
    for i in range(steps):
        assert x == (3 ** (n + i) + A) // (2 ** (E + 1))
        numerator = 3 ** (n + i + 1) + (3 * A + 2 ** (E + 1))
        predicted_e = v2(numerator) - (E + 1)
        y, e = f_with_e(x)
        assert e == predicted_e, (n, i, e, predicted_e)
        A = 3 * A + 2 ** (E + 1)
        rows.append((i, e, E, A, v2(A), A.bit_length()))
        E += e
        x = y
    return rows


def print_examples():
    print("== Exponential-affine normal form examples ==")
    for n in (23, 97, 249):
        print(f"\nn={n}")
        print(f"{'i':>3} {'e_i':>4} {'E_i':>5} {'v2(A)':>6} {'bits(A)':>8} {'A mod 64':>8}")
        rows = normal_tail(n, 16)
        for i, e, E, A, a2, bits in rows:
            print(f"{i:3d} {e:4d} {E:5d} {a2:6d} {bits:8d} {A % 64:8d}")


def verify_range(limit=301, steps=80):
    for n in range(3, limit + 1, 2):
        normal_tail(n, steps)
    print(f"\nPASS normal form for odd n=3..{limit}, first {steps} steps")


if __name__ == "__main__":
    print_examples()
    verify_range()
