#!/usr/bin/env python3
"""Classify mixed GPA2-blocked/eligible canonical shell pairs.

For payout ancestors p < q, transport the earlier canonical shell to time q
and form

    abs(3^(q-p) S_p - S_q).

The pair is called a shell fusion when this difference is itself exactly a
collision-shell displacement S(V, 2H).  The computation uses integers only.
It is an algebraic diagnostic: shell fusion does not by itself prove that the
resulting virtual partner lies on a smaller repunit tail.
"""

import argparse
from collections import Counter

from explore_repunit_extremal_prefixes import census


def shell_displacement(u, h):
    return (1 << (u + 1)) * ((1 << (2 * h)) - 1) // 3


def canonical_shell(term):
    q = term["q"]
    h = q // 2
    u = term["pre_E"] + q - 2 * h
    return shell_displacement(u, h), u, h


def shell_coordinates(value):
    """Return (V,H) when value=S(V,2H), otherwise None."""
    if value <= 0:
        return None
    valuation = (value & -value).bit_length() - 1
    if valuation < 1:
        return None
    odd = value >> valuation
    power = 3 * odd + 1
    if power & (power - 1):
        return None
    exponent = power.bit_length() - 1
    if exponent == 0 or exponent % 2:
        return None
    return valuation - 1, exponent // 2


def canonical_correction(A, E, payout):
    post_A = 3 * A + (1 << (E + 1))
    post_E = E + payout
    h = payout // 2
    u = post_E - 2 * h
    C = post_A + shell_displacement(u, h)
    return post_A, post_E, C, u


def correction_lift_defect(word, initial_E=0, initial_A=0):
    """Compare complete canonical corrections at first and last payouts."""
    A = initial_A
    E = initial_E
    first_C = None
    first_u = None
    for index, payout in enumerate(word):
        A, E, C, u = canonical_correction(A, E, payout)
        if index == 0:
            first_C = C
            first_u = u
    gap = len(word) - 1
    defect = C - 3**gap * first_C
    return defect, first_u, u


def print_short_pattern_defects():
    patterns = (
        (2, 3),
        (3, 2),
        (4, 2),
        (3, 1, 2),
        (2, 1, 1, 3),
        (3, 1, 2, 2),
        (3, 2, 1, 2),
    )
    print("\nFull-correction lift defects for the short fusion blocks:")
    for word in patterns:
        defect, first_u, later_u = correction_lift_defect(word)
        coordinates = shell_coordinates(abs(defect))
        print(
            f"  word={word} u={first_u}->{later_u} defect={defect} "
            f"shell={coordinates}"
        )


def mixed_pair_rows(limit, factor, min_deficit):
    merge_result, rows = census(limit, factor)
    if min_deficit == 2.0:
        dangerous = [
            row for row in rows
            if 3 ** row["K"] >= 2 ** (row["E"] + 2)
        ]
    else:
        dangerous = [row for row in rows if row["deficit"] >= min_deficit]

    pairs = {}
    for row in dangerous:
        terms = row["exact_payout_terms"]
        for left_index, left in enumerate(terms):
            left_blocked = left["q"] % 6 in (3, 4)
            for right in terms[left_index + 1 :]:
                right_blocked = right["q"] % 6 in (3, 4)
                if left_blocked == right_blocked:
                    continue
                earlier, later = (
                    (left, right)
                    if left["step"] < right["step"]
                    else (right, left)
                )
                key = (row["n"], earlier["step"], later["step"])
                if key in pairs:
                    continue
                earlier_shell, earlier_u, earlier_h = canonical_shell(earlier)
                later_shell, later_u, later_h = canonical_shell(later)
                transported = 3 ** (later["step"] - earlier["step"]) * earlier_shell
                difference = abs(transported - later_shell)
                pairs[key] = {
                    "n": row["n"],
                    "record_K": row["K"],
                    "deficit": row["deficit"],
                    "earlier_step": earlier["step"],
                    "earlier_q": earlier["q"],
                    "earlier_E": earlier["pre_E"],
                    "earlier_u": earlier_u,
                    "earlier_h": earlier_h,
                    "later_step": later["step"],
                    "later_q": later["q"],
                    "later_E": later["pre_E"],
                    "later_u": later_u,
                    "later_h": later_h,
                    "gap": later["step"] - earlier["step"],
                    "sign": 1 if transported > later_shell else -1,
                    "difference": difference,
                    "fusion": shell_coordinates(difference),
                }
    return merge_result, dangerous, list(pairs.values())


def print_report(limit, factor, min_deficit, top):
    merge_result, dangerous, pairs = mixed_pair_rows(
        limit, factor, min_deficit
    )
    fusions = [row for row in pairs if row["fusion"] is not None]
    patterns = Counter(
        (
            row["earlier_q"],
            row["later_q"],
            row["gap"],
            row["later_u"] - row["earlier_u"],
            row["sign"],
            row["fusion"][1] if row["fusion"] else None,
        )
        for row in fusions
    )

    print("== Mixed blocked/eligible shell pairs ==")
    print(
        f"finite domain: odd 7 <= n <= {limit}; "
        f"primitive tails={len(merge_result['primitives'])}; "
        f"dangerous records={len(dangerous)}"
    )
    print(
        f"distinct mixed pairs={len(pairs)}; "
        f"exact shell fusions={len(fusions)}"
    )
    print("Fusion pattern key: (q_early,q_late,gap,delta_u,sign,H)")
    for pattern, count in patterns.most_common():
        print(f"  {pattern}: {count}")

    print("\nFirst exact mixed fusions:")
    for row in sorted(
        fusions,
        key=lambda item: (
            item["gap"],
            item["n"],
            item["earlier_step"],
        ),
    )[:top]:
        V, H = row["fusion"]
        sign = "earlier>later" if row["sign"] > 0 else "later>earlier"
        print(
            f"  n={row['n']:4d} recordK={row['record_K']:3d} "
            f"j={row['earlier_step']:2d}:E={row['earlier_E']:2d}:q={row['earlier_q']} "
            f"-> j={row['later_step']:2d}:E={row['later_E']:2d}:q={row['later_q']} "
            f"gap={row['gap']:2d} du={row['later_u']-row['earlier_u']:3d} "
            f"{sign} fusion=S({V},{2*H})"
        )
    print_short_pattern_defects()


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=5001)
    parser.add_argument("--factor", type=int, default=3)
    parser.add_argument("--min-deficit", type=float, default=2.0)
    parser.add_argument("--top", type=int, default=50)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    print_report(args.limit, args.factor, args.min_deficit, args.top)
