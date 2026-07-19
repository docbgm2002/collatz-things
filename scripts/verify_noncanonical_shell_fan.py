#!/usr/bin/env python3
"""Verify and probe noncanonical shell-fan ancestry.

The proved checks cover the exact shell identity, automatic smaller-tail
realisation on exhaustive small correction layers, and the modulo-3 split.
The modulo-3^s report is diagnostic: it asks whether a bounded higher
congruence immediately eliminates every fan target.
"""

from __future__ import annotations

from collections import Counter
from functools import lru_cache

from verify_repunit_ancestry_realization import (
    A_of,
    compositions,
    follow_word,
    odd_step,
    repunit,
    repunit_exponent_class,
)


def shell_displacement(u: int, h: int) -> int:
    return (1 << (u + 1)) * ((1 << (2 * h)) - 1) // 3


def fan_partner(x: int, h: int) -> int:
    return (1 << (2 * h)) * x + ((1 << (2 * h)) - 1) // 3


def fan_target(prefix: tuple[int, ...], payout: int, h: int):
    E = sum(prefix)
    F = E + payout
    u = F - 2 * h
    if u < 0:
        return None
    post_A = A_of(prefix + (payout,))
    return post_A + shell_displacement(u, h), u


@lru_cache(maxsize=None)
def source_layer(total: int, parts: int) -> dict[int, tuple[tuple[int, ...], ...]]:
    layer: dict[int, list[tuple[int, ...]]] = {}
    for word in compositions(total, parts):
        layer.setdefault(A_of(word), []).append(word)
    return {correction: tuple(words) for correction, words in layer.items()}


def aligned_lengths(j: int, u: int):
    first = j + 2
    if first % 2 != (j + 1) % 2:
        first += 1
    return range(first, u + 1, 2)


def verify_shell_identity(max_x: int = 199, max_h: int = 12) -> None:
    checked = 0
    for x in range(1, max_x + 1, 2):
        for h in range(1, max_h + 1):
            y = fan_partner(x, h)
            assert y & 1
            assert 3 * y + 1 == (1 << (2 * h)) * (3 * x + 1)
            assert odd_step(y)[0] == odd_step(x)[0]
            checked += 1
    print(f"NSF1 exact shell fan: PASS  ({checked} odd-state/height pairs)")


def verify_mod3_split(max_pre_total: int = 12, max_q: int = 18) -> None:
    checked = 0
    escaped_canonical_block = Counter()
    for E in range(1, max_pre_total + 1):
        for j in range(1, min(E, 5) + 1):
            for prefix in compositions(E, j):
                for q in range(2, max_q + 1):
                    F = E + q
                    for h in range(1, F // 2 + 1):
                        C, _ = fan_target(prefix, q, h)
                        forbidden = h % 3 == (1 if q & 1 else 2)
                        assert (C % 3 == 0) == forbidden
                        if q % 6 in (3, 4) and not forbidden:
                            escaped_canonical_block[q % 6] += 1
                        checked += 1
    assert escaped_canonical_block[3] and escaped_canonical_block[4]
    print(
        "NSF3 fan modulo-3 split: PASS  "
        f"({checked} targets; q=3/4 canonical obstruction escaped)"
    )


def verify_automatic_realisation(
    max_pre_total: int = 10, max_q: int = 6
) -> None:
    abstract_matches = 0
    realised_matches = 0
    noncanonical_matches = 0

    for E in range(3, max_pre_total + 1):
        for j in range(1, min(E, 4) + 1):
            for prefix in compositions(E, j):
                for q in range(2, max_q + 1):
                    high_word = prefix + (q,)
                    exponent_class = repunit_exponent_class(high_word)
                    if exponent_class is None or not (exponent_class[0] & 1):
                        continue
                    n0, period = exponent_class
                    F = E + q
                    for h in range(1, F // 2 + 1):
                        C, u = fan_target(prefix, q, h)
                        if not tuple(aligned_lengths(j, u)):
                            continue
                        for i in aligned_lengths(j, u):
                            matches = source_layer(u, i).get(C, ())
                            abstract_matches += len(matches)
                            if not matches:
                                continue

                            n = n0
                            if n < 3:
                                n += period
                            while n + j + 1 - i < 1:
                                n += period
                            m = n + j + 1 - i
                            assert 0 < m < n and (m & 1) and (n & 1)

                            X = follow_word(repunit(n), high_word)
                            expected = fan_partner(X, h)
                            for source in matches:
                                Y = follow_word(repunit(m), source)
                                assert Y == expected
                                assert odd_step(Y)[0] == odd_step(X)[0]
                                realised_matches += 1
                                if h != q // 2:
                                    noncanonical_matches += 1

    assert abstract_matches > 0
    assert realised_matches == abstract_matches
    assert noncanonical_matches > 0
    print(
        "NSF2 fan automatic realisation: PASS  "
        f"({realised_matches} aligned matches; "
        f"{noncanonical_matches} noncanonical)"
    )


def diagnose_higher_residues(
    max_pre_total: int = 10,
    moduli: tuple[int, ...] = (3, 9, 27, 81),
) -> None:
    """Report whether small source-layer congruences kill eligible fans."""
    totals = Counter()
    survivors = {modulus: Counter() for modulus in moduli}
    distinct_signatures: dict[tuple[int, int], set[tuple[int, ...]]] = {}

    for E in range(3, max_pre_total + 1):
        for j in range(1, min(E, 4) + 1):
            for prefix in compositions(E, j):
                if prefix[0] < 2:
                    continue
                for q in (3, 4):
                    F = E + q
                    for h in range(1, F // 2 + 1):
                        C, u = fan_target(prefix, q, h)
                        if not tuple(aligned_lengths(j, u)) or C % 3 == 0:
                            continue
                        lengths = tuple(aligned_lengths(j, u))
                        residues = {
                            modulus: {
                                correction % modulus
                                for i in lengths
                                for correction in source_layer(u, i)
                            }
                            for modulus in moduli
                        }
                        totals[q] += 1
                        signature = tuple(C % modulus for modulus in moduli)
                        distinct_signatures.setdefault((q, h), set()).add(signature)
                        for modulus in moduli:
                            if C % modulus in residues[modulus]:
                                survivors[modulus][q] += 1

    print("Higher-residue fan diagnostic (small exhaustive layers):")
    for modulus in moduli:
        fields = []
        for q in (3, 4):
            fields.append(
                f"q={q}: {survivors[modulus][q]}/{totals[q]} survive"
            )
        print(f"  mod {modulus:2d}  " + "; ".join(fields))

    assert survivors[moduli[-1]][3] > 0
    assert survivors[moduli[-1]][4] > 0
    varied = sum(len(values) > 1 for values in distinct_signatures.values())
    print(
        "  bounded-congruence verdict: no universal obstruction through "
        f"mod {moduli[-1]}; {varied} (q,h) slots have multiple signatures"
    )


if __name__ == "__main__":
    verify_shell_identity()
    verify_mod3_split()
    verify_automatic_realisation()
    diagnose_higher_residues()
    print("\nAll noncanonical shell-fan checks passed.")
