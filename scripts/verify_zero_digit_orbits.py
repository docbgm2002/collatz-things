#!/usr/bin/env python3
"""Finite checks supporting IEF22--IEF23 (Theorem G / dual-digit escape).

The universal claims live in docs/repunit/dio1_cocycle_problem.md.  This
verifier checks the supporting local identities used in that proof: the
functional residue partition, monotone Phi steps, positive translations,
the pure-4 nested start tower, and the first AB-parameter connector
t = 191 + 2048 u.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from itertools import product
from math import gcd


def successors(q: int) -> list[tuple[int, int]]:
    out: list[tuple[int, int]] = []
    if q >= 23 and q % 32 == 23:
        out.append((3, 20 + 27 * ((q - 23) // 32)))
    if q >= 15 and q % 64 == 15:
        out.append((4, 20 + 81 * ((q - 15) // 64)))
    return out


def phi_compose(word: tuple[int, ...]) -> tuple[Fraction, Fraction]:
    mu = Fraction(1)
    b_total = Fraction(0)
    for block in word:
        if block == 3:
            lam, b = Fraction(27, 32), Fraction(19, 32)
        else:
            lam, b = Fraction(81, 64), Fraction(65, 64)
        b_total = lam * b_total + b
        mu = lam * mu
    return mu, b_total


def chain_start(word: tuple[int, ...]) -> tuple[int, int]:
    start_q, start_mod = (23, 32) if word[0] == 3 else (15, 64)
    current_q, current_mod = start_q, start_mod
    for block in word:
        residue, modulus = (23, 32) if block == 3 else (15, 64)
        coeff = current_mod % modulus
        target = (residue - current_q) % modulus
        if coeff == 0:
            if current_q % modulus != residue % modulus:
                raise AssertionError(f"empty zero-run for {word}")
            shift, step = 0, 1
        else:
            common = gcd(coeff, modulus)
            if target % common != 0:
                raise AssertionError(f"empty zero-run for {word}")
            reduced_mod = modulus // common
            shift = (
                (target // common)
                * pow(coeff // common, -1, reduced_mod)
                % reduced_mod
            )
            step = reduced_mod
        start_q = start_q + start_mod * shift
        start_mod *= step
        current_q = current_q + current_mod * shift
        current_mod *= step
        if block == 3:
            k0 = (current_q - 23) // 32
            dk = current_mod // 32
            current_q = 20 + 27 * k0
            current_mod = 27 * dk
        else:
            k0 = (current_q - 15) // 64
            dk = current_mod // 64
            current_q = 20 + 81 * k0
            current_mod = 81 * dk
    return start_q % start_mod, start_mod


def ab_count(t: int, limit: int = 64) -> int:
    q = 1079 + 2048 * t
    count = 0
    cur = q
    for _ in range(limit):
        if cur >= 23 and cur % 32 == 23:
            k = (cur - 23) // 32
            if k % 64 == 33:
                count += 1
        options = successors(cur)
        if not options:
            return count
        _, cur = options[0]
    return count


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--functional-limit", type=int, default=100_000)
    parser.add_argument("--four-tower-through", type=int, default=10)
    parser.add_argument("--ab-t-limit", type=int, default=5000)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    print("== verify_zero_digit_orbits (IEF22--IEF23 support) ==")

    for q in range(args.functional_limit):
        in_a = q >= 23 and q % 32 == 23
        in_b = q >= 15 and q % 64 == 15
        assert not (in_a and in_b)
        assert len(successors(q)) <= 1
    print(f"functional partition: PASS through {args.functional_limit}")

    for q in (23, 55, 823, 1079, 13111, 15, 79, 719, 1231):
        for block, nxt in successors(q):
            if block == 3:
                assert nxt < q
                assert 32 * nxt == 27 * q + 19
            else:
                assert nxt > q
                assert 64 * nxt == 81 * q + 65
    print("monotone Phi identities: PASS on sample residues")

    for length in range(1, 5):
        for word in product((3, 4), repeat=length):
            _, b_total = phi_compose(word)
            assert b_total > 0
    print("positive translation B_W: PASS through length 4")

    prev_min = None
    prev_mod = None
    for length in range(1, args.four_tower_through + 1):
        minimal, modulus = chain_start((4,) * length)
        assert modulus == 64**length
        if prev_min is not None:
            assert (minimal - prev_min) % prev_mod == 0
            assert minimal > prev_min
        prev_min, prev_mod = minimal, modulus
    print(
        f"pure-4 nested starts: PASS through length "
        f"{args.four_tower_through} with moduli 64^n"
    )

    two_ab = [t for t in range(args.ab_t_limit) if ab_count(t) >= 2]
    assert two_ab and two_ab[0] == 191
    assert all((t - 191) % 2048 == 0 for t in two_ab)
    print(
        f"AB connector tower: PASS first second-AB at t=191, "
        f"step 2048 ({len(two_ab)} hits with t<{args.ab_t_limit})"
    )
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    main()
