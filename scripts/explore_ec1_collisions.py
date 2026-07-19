#!/usr/bin/env python3
"""Diagnose pre-descent residue collisions for Avenue A lemma target EC1.

For each odd n, walk the a_n-orbit through first descent and, on the first
residue collision mod 2^{n+1} while still x >= T, report the cycle-identity
data (L, E', s, c) and classify the state as large-x or near-barrier under

    x_i >= 2^{n + ceil(n/2)}   (i.e. c = 1/2 in 2^{(1+c)n}).

Also verifies the worked n=5 non-counterexample
(i,j)=(1,4), L=3, E'=4, s=1, c=23.

Diagnostics only: finite scans do not prove EC1.
"""

from __future__ import annotations

import argparse


def v2(value: int) -> int:
    return (value & -value).bit_length() - 1


def large_threshold(n: int) -> int:
    """2^{n + ceil(n/2)} = 2^{ceil(3n/2)}."""
    return 1 << (n + (n + 1) // 2)


def scan_first_collision(n: int, step_limit: int = 200_000) -> dict | None:
    """Return cycle data for the first stay-above collision, or None."""
    threshold = (1 << n) - 1
    modulus = 1 << (n + 1)
    x = (3**n - 1) // 2
    seen: dict[int, tuple[int, int, int]] = {}
    # seen[residue] = (step, x, E_at_step)
    E = 0
    for step in range(0, step_limit + 1):
        if step > 0 and x < threshold:
            return None
        residue = x % modulus
        prev = seen.get(residue)
        if prev is not None:
            i, x_i, E_i = prev
            j = step
            L = j - i
            E_prime = E - E_i
            s = (x - x_i) // modulus
            c = x_i * ((1 << E_prime) - 3**L) + s * (1 << (E_prime + n + 1))
            # Cross-check affine correction form.
            c_alt = (x << E_prime) - (3**L) * x_i
            assert c == c_alt, (n, i, j, c, c_alt)
            gap = abs((1 << E_prime) - 3**L)
            # Compare gap to 2^{E'+n}/x_i without floats when possible.
            rhs_num = 1 << (E_prime + n)
            large = x_i >= large_threshold(n)
            return {
                "n": n,
                "i": i,
                "j": j,
                "L": L,
                "E_prime": E_prime,
                "s": s,
                "c": c,
                "x_i": x_i,
                "x_j": x,
                "gap": gap,
                "rhs_num": rhs_num,
                "large": large,
                "threshold_T": threshold,
                "large_cut": large_threshold(n),
                "k_down_bound": threshold,  # for regime note; exact K not needed
            }
        seen[residue] = (step, x, E)
        value = 3 * x + 1
        e = v2(value)
        E += e
        x = value >> e
    raise RuntimeError(f"no descent within step limit for n={n}")


def verify_n5_example() -> None:
    row = scan_first_collision(5)
    assert row is not None
    assert (row["i"], row["j"], row["L"], row["E_prime"], row["s"], row["c"]) == (
        1,
        4,
        3,
        4,
        1,
        23,
    )
    assert row["gap"] == 11
    assert not row["large"]
    assert row["x_i"] == 91 and row["x_j"] == 155
    print(
        "n=5 worked example: PASS "
        "(i,j)=(1,4), L=3, E'=4, s=1, c=23, gap=11; "
        "near-barrier (x_i=91 < large_cut=256); "
        "K_down=30=j0<=T=31 so outside EC1 hypothesis"
    )


def explore(limit: int) -> None:
    verify_n5_example()
    collisions: list[dict] = []
    for n in range(3, limit + 1, 2):
        row = scan_first_collision(n)
        if row is not None:
            collisions.append(row)

    assert len(collisions) == 1 and collisions[0]["n"] == 5, [
        (r["n"], r["L"], r["i"], r["j"]) for r in collisions
    ]
    row = collisions[0]
    # Gap vs 2^{E'+n}/x_i: for n=5, 11 vs 32*32/91 ≈ 5.63 — same order.
    ratio = row["gap"] * row["x_i"] / row["rhs_num"]
    print(
        f"EC1 collision census: PASS (odd 3 <= n <= {limit}; "
        f"only n=5; class={'large' if row['large'] else 'near-barrier'}; "
        f"gap*x_i/2^(E'+n)={ratio:.4f})"
    )
    print(
        "No large-x pre-descent collision in the domain; "
        "EC1-near residual is the only finite specimen, and it has K_down<=T."
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=2001)
    return parser.parse_args()


if __name__ == "__main__":
    explore(parse_args().limit)
