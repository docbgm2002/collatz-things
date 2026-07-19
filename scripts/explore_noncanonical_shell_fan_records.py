#!/usr/bin/env python3
"""Test noncanonical shell fans on the named exceptional PCD records.

This is a residue-sieve diagnostic, not a merger certificate.  For each
blocked payout ancestor in the highest dangerous record of each exceptional
primitive tail, it constructs every admissible modulo-3-eligible shell-fan
target.  It then asks whether the target correction survives membership in
the aligned source layers modulo 3^s.
"""

from __future__ import annotations

import argparse
from functools import lru_cache

from explore_payout_concentration import branch
from explore_repunit_extremal_prefixes import census, v2
from verify_repunit_ancestry_realization import A_of, compositions
from verify_noncanonical_shell_fan import aligned_lengths, shell_displacement


@lru_cache(maxsize=None)
def correction_residues(total: int, parts: int, modulus: int) -> frozenset[int]:
    """Residues of A_parts for positive compositions of the given total."""
    if parts == 0:
        return frozenset({-1 % modulus}) if total == 0 else frozenset()
    if total < parts:
        return frozenset()

    residues: set[int] = set()
    # Append a final valuation e to a word of total total-e.
    for e in range(1, total - parts + 2):
        previous_total = total - e
        injection = pow(2, previous_total + 1, modulus)
        residues.update(
            (3 * previous + injection) % modulus
            for previous in correction_residues(
                previous_total, parts - 1, modulus
            )
        )
        if len(residues) == modulus:
            break
    return frozenset(residues)


def aligned_source_residues(
    j: int, u: int, d: int, modulus: int
) -> frozenset[int]:
    residues: set[int] = set()
    upper = min(u, d - 1)
    for i in aligned_lengths(j, upper):
        residues.update(correction_residues(u, i, modulus))
    return frozenset(residues)


def layer_bounds(total: int, parts: int) -> tuple[int, int] | None:
    if parts == 0:
        return (-1, -1) if total == 0 else None
    if total < parts:
        return None
    lower = 3**parts - 2 ** (parts + 1)
    upper = (
        2 ** (total - parts + 1) * (3**parts - 2**parts) - 3**parts
    )
    return lower, upper


@lru_cache(maxsize=None)
def correction_witness(
    total: int, parts: int, target: int
) -> tuple[int, ...] | None:
    """Find an exact source word by reversing A'=3A+2^(E+1)."""
    bounds = layer_bounds(total, parts)
    if bounds is None or not (bounds[0] <= target <= bounds[1]):
        return None
    if parts == 0:
        return () if total == 0 and target == -1 else None

    for final_e in range(1, total - parts + 2):
        previous_total = total - final_e
        difference = target - (1 << (previous_total + 1))
        if difference % 3:
            continue
        previous_target = difference // 3
        prefix = correction_witness(
            previous_total, parts - 1, previous_target
        )
        if prefix is not None:
            return prefix + (final_e,)
    return None


def verify_exact_witness(max_total: int = 10) -> None:
    checked = 0
    for total in range(1, max_total + 1):
        for parts in range(1, total + 1):
            layer = {A_of(word): word for word in compositions(total, parts)}
            for target, expected in layer.items():
                witness = correction_witness(total, parts, target)
                assert witness is not None
                assert sum(witness) == total and len(witness) == parts
                assert A_of(witness) == target
                depth, tree_witness, _ = obstruction_depth(
                    total, parts, target
                )
                assert depth is None and tree_witness is not None
                checked += 1
            if layer:
                nonmember = max(layer) + 1
                while nonmember in layer:
                    nonmember += 1
                assert correction_witness(total, parts, nonmember) is None
                depth, tree_witness, _ = obstruction_depth(
                    total, parts, nonmember
                )
                assert depth is not None and tree_witness is None
                if depth > 1:
                    assert (
                        nonmember % (3 ** (depth - 1))
                        in correction_residues(
                            total, parts, 3 ** (depth - 1)
                        )
                    )
                assert (
                    nonmember % (3**depth)
                    not in correction_residues(total, parts, 3**depth)
                )
    print(f"Exact reverse correction recursion: PASS ({checked} layer values)")


def v3(value: int) -> int:
    order = 0
    while value and value % 3 == 0:
        value //= 3
        order += 1
    return order


def obstruction_depth(
    total: int, parts: int, target: int
) -> tuple[int | None, tuple[int, ...] | None, int]:
    """Return first failed 3-adic digit, exact witness, and peak states.

    At depth s, A_parts modulo 3^s depends only on the final s valuations.
    The total excess total-parts bounds the suffix tree independently of the
    sizes of the correction layers.
    """
    # (suffix word, suffix valuation, suffix contribution)
    states = [((), 0, 0)]
    peak = 1
    power3 = 1
    for depth in range(1, parts + 1):
        power3 *= 3
        coefficient = power3 // 3
        remaining_parts = parts - depth
        next_states = []
        for suffix, suffix_total, contribution in states:
            max_e = total - suffix_total - remaining_parts
            for e in range(1, max_e + 1):
                new_total = suffix_total + e
                if remaining_parts == 0 and new_total != total:
                    continue
                injection = coefficient * (1 << (total - new_total + 1))
                new_contribution = contribution + injection
                if (new_contribution - target) % power3:
                    continue
                next_states.append(
                    ((e,) + suffix, new_total, new_contribution)
                )
        states = next_states
        peak = max(peak, len(states))
        if not states:
            return depth, None, peak

    exact_words = [
        word for word, word_total, _ in states
        if word_total == total and A_of(word) == target
    ]
    if exact_words:
        return None, exact_words[0], peak

    differences = [
        abs(A_of(word) - target)
        for word, word_total, _ in states
        if word_total == total
    ]
    assert differences
    return max(v3(difference) + 1 for difference in differences), None, peak


def payout_corrections(n: int, last_step: int) -> dict[int, int]:
    """Return A_{j+1} for every payout step j through last_step."""
    x = (3**n - 1) // 2
    E = 0
    A = -1
    result = {}
    for j in range(last_step + 1):
        value = 3 * x + 1
        q = v2(value)
        x = value >> q
        A = 3 * A + (1 << (E + 1))
        if q > 1:
            result[j] = A
        E += q
    return result


def exceptional_rows(limit: int, factor: int):
    _, rows = census(limit, factor)
    dangerous = [
        row for row in rows if 3 ** row["K"] >= 2 ** (row["E"] + 2)
    ]
    exceptional = [
        row for row in dangerous if not branch(row).startswith("eligible")
    ]
    ranked = sorted(exceptional, key=lambda row: row["deficit"], reverse=True)
    seen = set()
    for row in ranked:
        if row["n"] not in seen:
            seen.add(row["n"])
            yield row


def report(
    limit: int, factor: int, max_power: int, exact_survivors: bool
) -> None:
    moduli = tuple(3**power for power in range(1, max_power + 1))
    print("== Noncanonical shell fan on exceptional primitive records ==")
    print(f"domain: odd 7 <= n <= {limit}; moduli={moduli}")

    total_fans = 0
    total_survivors = {modulus: 0 for modulus in moduli}
    nonempty_ancestors = 0

    for row in exceptional_rows(limit, factor):
        terms = [
            term
            for term in row["exact_payout_terms"]
            if term["q"] % 6 in (3, 4)
        ]
        corrections = payout_corrections(
            row["n"], max(term["step"] for term in terms)
        )
        print(
            f"\nn={row['n']} K={row['K']} branch={branch(row)} "
            f"blocked_ancestors={len(terms)}"
        )

        for term in terms:
            j = term["step"]
            E = term["pre_E"]
            q = term["q"]
            d = row["n"] + j + 1
            post_A = corrections[j]
            candidates = []
            for h in range(1, (E + q) // 2 + 1):
                u = E + q - 2 * h
                if not tuple(aligned_lengths(j, min(u, d - 1))):
                    continue
                C = post_A + shell_displacement(u, h)
                if C % 3 == 0:
                    continue
                candidates.append((h, u, C))

            if not candidates:
                print(f"  j={j:2d} E={E:2d} q={q}: fan empty")
                continue

            nonempty_ancestors += 1
            total_fans += len(candidates)
            survivor_counts = {modulus: 0 for modulus in moduli}
            signatures = []
            for h, u, C in candidates:
                survived = []
                for modulus in moduli:
                    source = aligned_source_residues(j, u, d, modulus)
                    keep = C % modulus in source
                    survived.append(keep)
                    if keep:
                        survivor_counts[modulus] += 1
                        total_survivors[modulus] += 1
                last_lengths = [
                    i
                    for i in aligned_lengths(j, min(u, d - 1))
                    if C % moduli[-1]
                    in correction_residues(u, i, moduli[-1])
                ]
                exact = []
                if exact_survivors:
                    exact = [
                        (
                            i,
                            correction_witness(u, i, C),
                            obstruction_depth(u, i, C),
                        )
                        for i in last_lengths
                    ]
                signatures.append(
                    f"h={h},u={u}:"
                    + (f"through {moduli[-1]} at i={last_lengths}"
                       + (f", exact={exact}" if exact_survivors else "")
                       if all(survived) else
                       f"fails {moduli[survived.index(False)]}")
                )

            counts = ", ".join(
                f"mod {modulus} {survivor_counts[modulus]}/{len(candidates)}"
                for modulus in moduli
            )
            print(f"  j={j:2d} E={E:2d} q={q}: {counts}")
            print("    " + "; ".join(signatures))

    print("\nAggregate:")
    print(
        f"  ancestors with nonempty eligible fan={nonempty_ancestors}; "
        f"fan targets={total_fans}"
    )
    for modulus in moduli:
        print(
            f"  mod {modulus}: "
            f"{total_survivors[modulus]}/{total_fans} targets survive"
        )
    if total_fans and total_survivors[moduli[-1]]:
        print(
            "  verdict: the named primitive records do not expose a uniform "
            f"fan obstruction through modulus {moduli[-1]}"
        )
    elif total_fans:
        print(
            "  verdict: every tested fan is killed by the bounded residue "
            "sieve; seek a symbolic obstruction before continuing"
        )


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=5001)
    parser.add_argument("--factor", type=int, default=3)
    parser.add_argument("--max-power", type=int, default=5)
    parser.add_argument("--exact-survivors", action="store_true")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    verify_exact_witness()
    report(args.limit, args.factor, args.max_power, args.exact_survivors)
