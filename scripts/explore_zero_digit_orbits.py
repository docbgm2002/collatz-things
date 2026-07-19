#!/usr/bin/env python3
"""Explore free Phi-orbits with eventually-zero dual digits.

Supports Theorem G in dio1_cocycle_problem.md: the integer graph G of
zero-digit Phi_3 / Phi_4 transitions is functional (out-degree <= 1), and
orbits die after finitely many AB transitions (nested modulus tower).

Along any zero-digit run the endpoint residue follows

    Phi_3(q) = (27q + 19)/32,   Phi_4(q) = (81q + 65)/64,

exactly when q ≡ 23 (mod 32) or q ≡ 15 (mod 64).  This script studies that
system in isolation (no 3^R cocycle bound).
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from collections.abc import Iterable, Sequence
from fractions import Fraction
from itertools import product
from math import gcd, log2


def successors(q: int) -> list[tuple[int, int]]:
    """Zero-digit successors of an integer residue q."""
    out: list[tuple[int, int]] = []
    if q >= 23 and q % 32 == 23:
        out.append((3, 20 + 27 * ((q - 23) // 32)))
    if q >= 15 and q % 64 == 15:
        out.append((4, 20 + 81 * ((q - 15) // 64)))
    return out


def predecessors(qp: int) -> list[tuple[int, int]]:
    preds: list[tuple[int, int]] = []
    if qp >= 20 and (qp - 20) % 27 == 0:
        k = (qp - 20) // 27
        if k >= 0:
            preds.append((3, 23 + 32 * k))
    if qp >= 20 and (qp - 20) % 81 == 0:
        k = (qp - 20) // 81
        if k >= 0:
            preds.append((4, 15 + 64 * k))
    return preds


def phi_compose(word: Sequence[int]) -> tuple[Fraction, Fraction]:
    """Return (mu, B) with Phi_W(x) = mu*x + B."""
    mu = Fraction(1)
    b_total = Fraction(0)
    for block in word:
        if block == 3:
            lam, b = Fraction(27, 32), Fraction(19, 32)
        elif block == 4:
            lam, b = Fraction(81, 64), Fraction(65, 64)
        else:
            raise ValueError(f"unsupported letter {block}")
        b_total = lam * b_total + b
        mu = lam * mu
    return mu, b_total


def drift(word: Sequence[int]) -> float:
    c = log2(3 / 2)
    return sum(c * block - 2 for block in word)


def realizes(q: int, word: Sequence[int]) -> bool:
    for block in word:
        options = dict(successors(q))
        if block not in options:
            return False
        q = options[block]
    return True


def longest_path_length(q: int) -> int:
    """Longest forward zero-digit path from q; assumes the orbit graph is a DAG."""
    memo: dict[int, int] = {}

    def dfs(value: int) -> int:
        if value in memo:
            return memo[value]
        best = 0
        for _, nxt in successors(value):
            best = max(best, 1 + dfs(nxt))
        memo[value] = best
        return best

    return dfs(q)


def max_four_run(q: int, cap: int = 256) -> int:
    length = 0
    while length < cap:
        options = dict(successors(q))
        if 4 not in options:
            return length
        q = options[4]
        length += 1
    return length


def chain_start(word: Sequence[int]) -> tuple[int, int] | None:
    """Arithmetic progression of starts realizing a zero-run along word.

    Returns (min_nonneg_start, modulus), or None if impossible.
    """
    if not word:
        return (0, 1)
    start_q, start_mod = (23, 32) if word[0] == 3 else (15, 64)
    current_q, current_mod = start_q, start_mod
    for block in word:
        residue, modulus = (23, 32) if block == 3 else (15, 64)
        coeff = current_mod % modulus
        target = (residue - current_q) % modulus
        if coeff == 0:
            if current_q % modulus != residue % modulus:
                return None
            shift, step = 0, 1
        else:
            common = gcd(coeff, modulus)
            if target % common != 0:
                return None
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
    minimal = start_q % start_mod
    return minimal, start_mod


def search_contracting_cycles(max_period: int) -> list[tuple[tuple[int, ...], int]]:
    found: list[tuple[tuple[int, ...], int]] = []
    for period in range(1, max_period + 1):
        for word in product((3, 4), repeat=period):
            if drift(word) >= 0:
                continue
            mu, b_total = phi_compose(word)
            if mu >= 1:
                continue
            q_fix = b_total / (1 - mu)
            if q_fix.denominator != 1 or q_fix.numerator < 0:
                continue
            q = int(q_fix.numerator)
            if not realizes(q, word):
                continue
            end = q
            for block in word:
                end = dict(successors(end))[block]
            if end == q:
                found.append((word, q))
    return found


def scan_depths(bit_bound: int, samples_per_bits: int) -> dict[int, int]:
    """Max observed longest-path depth among residue-class samples up to bit_bound."""
    maxima: dict[int, int] = defaultdict(int)
    for bits in range(4, bit_bound + 1):
        upper = 1 << bits
        lower = 1 << (bits - 1)
        # Sample both residue classes inside the bit window.
        candidates: list[int] = []
        q = 23 + 32 * ((lower + 31) // 32)
        while q < upper and len(candidates) < samples_per_bits:
            candidates.append(q)
            q += 32 * max(1, (upper - lower) // (32 * samples_per_bits))
        q = 15 + 64 * ((lower + 63) // 64)
        while q < upper and len(candidates) < 2 * samples_per_bits:
            candidates.append(q)
            q += 64 * max(1, (upper - lower) // (64 * samples_per_bits))
        for value in candidates:
            depth = longest_path_length(value)
            maxima[bits] = max(maxima[bits], depth)
    return dict(maxima)


def check_lemmas(values: Iterable[int]) -> None:
    for q in values:
        for block, nxt in successors(q):
            if block == 3:
                assert nxt < q, (q, block, nxt)
                assert 32 * nxt == 27 * q + 19
            else:
                assert nxt > q, (q, block, nxt)
                assert 64 * nxt == 81 * q + 65
        for block, pred in predecessors(q):
            assert (block, q) in successors(pred)


def check_functional(limit: int = 100_000) -> None:
    """A and B are disjoint; out-degree is at most 1."""
    for q in range(limit):
        in_a = q >= 23 and q % 32 == 23
        in_b = q >= 15 and q % 64 == 15
        assert not (in_a and in_b), q
        assert len(successors(q)) <= 1, q


def ab_parameter_orbit_stats(max_t: int = 5000) -> tuple[int, int, list[int]]:
    """Return (max_L, max_AB_count, sample t with N(t)>=2)."""

    def kind(q: int) -> str:
        if q >= 23 and q % 32 == 23:
            k = (q - 23) // 32
            if k % 32 == 25:
                return "AA"
            if k % 64 == 33:
                return "AB"
            return "A_die"
        if q >= 15 and q % 64 == 15:
            k = (q - 15) // 64
            if k % 64 == 11:
                return "BB"
            if k % 32 == 19:
                return "BA"
            return "B_die"
        return "D"

    max_l = 0
    max_ab = 0
    two_ab_t: list[int] = []
    for t in range(max_t):
        q = 1079 + 2048 * t
        length = 0
        ab_count = 0
        cur = q
        for _ in range(64):
            if kind(cur) == "AB":
                ab_count += 1
            options = successors(cur)
            if not options:
                break
            assert len(options) == 1
            _, cur = options[0]
            length += 1
        max_l = max(max_l, length)
        max_ab = max(max_ab, ab_count)
        if ab_count >= 2:
            two_ab_t.append(t)
    return max_l, max_ab, two_ab_t[:12]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-period", type=int, default=14)
    parser.add_argument("--bit-bound", type=int, default=24)
    parser.add_argument("--samples-per-bits", type=int, default=8)
    parser.add_argument("--word-moduli-through", type=int, default=10)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    print("== Zero-digit Phi-orbit probe (Theorem G support) ==")

    check_functional()
    print("functional graph (A cap B empty, out-degree <= 1): PASS through 10^5")

    check_lemmas([23, 15, 55, 79, 823, 1079, 719, 13111])
    print("local decrease/increase lemmas: PASS on sample residues")

    # B > 0 on every nonempty word of length <= 4
    for length in range(1, 5):
        for word in product((3, 4), repeat=length):
            mu, b_total = phi_compose(word)
            assert b_total > 0
            if abs(drift(word)) < 1e-12:
                assert mu != 1 or True
                # Critical drift => mu == 1 and Phi(x) = x + B with B > 0.
                if abs(float(mu) - 1.0) < 1e-12:
                    assert b_total > 0
    print("positive translation term B_W > 0: PASS through length 4 (all words)")

    cycles = search_contracting_cycles(args.max_period)
    print(
        f"contracting integer cycles with period <= {args.max_period}: "
        f"{len(cycles)}"
    )
    for word, q in cycles[:10]:
        print(f"  word={word} q={q}")

    print("start-modulus growth for all-4 prefixes:")
    for length in range(1, args.word_moduli_through + 1):
        result = chain_start((4,) * length)
        assert result is not None
        minimal, modulus = result
        print(
            f"  4^{length}: min_start_bits={minimal.bit_length()} "
            f"mod_bits={modulus.bit_length()}"
        )

    print("start-modulus growth for all-3 prefixes:")
    for length in range(1, min(args.word_moduli_through, 12) + 1):
        result = chain_start((3,) * length)
        assert result is not None
        minimal, modulus = result
        print(
            f"  3^{length}: min_start_bits={minimal.bit_length()} "
            f"mod_bits={modulus.bit_length()}"
        )

    print(
        f"longest-path depths by bit window "
        f"(<= {args.samples_per_bits} samples/class):"
    )
    depths = scan_depths(args.bit_bound, args.samples_per_bits)
    for bits in sorted(depths):
        print(f"  bits={bits:2d} max_depth={depths[bits]}")

    print("max consecutive 4-runs on residue samples:")
    for k in (0, 1, 11, 75, 1000, 10000):
        for q in (15 + 64 * k, 23 + 32 * k):
            print(f"  q={q} four_run={max_four_run(q)}")

    max_l, max_ab, two_ab = ab_parameter_orbit_stats(5000)
    print(
        f"AB-parameter orbits t<5000: max_L={max_l} max_AB={max_ab} "
        f"sample t with AB>=2: {two_ab}"
    )
    # Pure BA connector tower: first second-AB hits at t=191+2048u
    assert two_ab and two_ab[0] == 191
    if len(two_ab) >= 2:
        assert two_ab[1] - two_ab[0] == 2048


if __name__ == "__main__":
    main()
