#!/usr/bin/env python3
"""Test the q=2 ancestry correlation on the finite primitive-record census.

This is deliberately narrower than the unqualified cylinder experiment in
``explore_ancestry_reachability.py``.  It keeps only strict record-deficit
prefixes on tails classified as primitive by the finite merger scan, and only
when the largest historical payout term has valuation two.

For each distinct dominant payout ancestor it reports:

* the admissible correction-layer lengths from REPANC1;
* exact correction membership (the tested totals are small in this census);
* the least positive exponent representative of the payout cylinder; and
* the least positive representative after extending to each record prefix.

The output is a finite diagnostic, not a universal implication.
"""

import argparse
from functools import lru_cache

from explore_repunit_extremal_prefixes import census


def v2(value):
    return (value & -value).bit_length() - 1


def valuation_word(n, length):
    x = (3**n - 1) // 2
    word = []
    for _ in range(length):
        value = 3 * x + 1
        q = v2(value)
        word.append(q)
        x = value >> q
    return tuple(word)


def A_of(word):
    A = -1
    E = 0
    for q in word:
        A = 3 * A + (1 << (E + 1))
        E += q
    return A


def compositions(total, parts):
    if parts == 1:
        yield (total,)
        return
    for first in range(1, total - parts + 2):
        for rest in compositions(total - first, parts - 1):
            yield (first,) + rest


@lru_cache(maxsize=None)
def correction_layer(total, parts):
    return frozenset(A_of(word) for word in compositions(total, parts))


def least_representative(n, total):
    residue = n % (1 << total)
    assert residue > 0 and residue % 2 == 1
    return residue


def ancestor_summary(n, step, record_rows):
    max_length = max(row["K"] for row in record_rows)
    word = valuation_word(n, max_length)
    assert word[step] == 2
    u = sum(word[:step])
    high_word = word[: step + 1]
    correction = A_of(high_word) + (1 << (u + 1))
    d = n + step + 1
    lengths = tuple(
        i
        for i in range(step + 2, min(u, d - 1) + 1)
        if i % 2 == (step + 1) % 2
    )
    matches = tuple(i for i in lengths if correction in correction_layer(u, i))
    payout_rep = least_representative(n, u + 2)
    records = tuple(
        {
            "K": row["K"],
            "E": row["E"],
            "deficit": row["deficit"],
            "share": row["dominant_share"],
            "record_rep": least_representative(n, row["E"]),
        }
        for row in record_rows
    )
    return {
        "n": n,
        "step": step,
        "u": u,
        "lengths": lengths,
        "matches": matches,
        "payout_rep": payout_rep,
        "records": records,
    }


def analyse(limit, factor, min_deficit):
    merge_result, rows = census(limit, factor)
    grouped = {}
    for row in rows:
        if row["dominant_q"] != 2 or row["deficit"] < min_deficit:
            continue
        grouped.setdefault((row["n"], row["dominant_step"]), []).append(row)
    summaries = [
        ancestor_summary(n, step, record_rows)
        for (n, step), record_rows in sorted(grouped.items())
    ]
    return merge_result, summaries


def print_report(merge_result, summaries, limit, min_deficit):
    print("== Primitive dominant-q=2 cylinder correlation ==")
    print(
        f"finite domain: odd 7 <= n <= {limit}; "
        f"primitive tails={len(merge_result['primitives'])}; "
        f"minimum record deficit={min_deficit:g}"
    )
    print(f"distinct dominant payout ancestors={len(summaries)}")

    eligible = [row for row in summaries if row["lengths"]]
    matched = [row for row in eligible if row["matches"]]
    print(
        f"ancestors with admissible source lengths={len(eligible)}; "
        f"exact correction matches={len(matched)}"
    )

    for row in summaries:
        record_text = ", ".join(
            f"K={record['K']}:D={record['deficit']:.4f}:"
            f"E={record['E']}:n0={record['record_rep']}:"
            f"share={record['share']:.2%}"
            for record in row["records"]
        )
        print(
            f"  n={row['n']:4d} j={row['step']:2d} u={row['u']:2d} "
            f"payout_n0={row['payout_rep']:4d} "
            f"lengths={row['lengths']} matches={row['matches']} | {record_text}"
        )


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=2001)
    parser.add_argument("--factor", type=int, default=3)
    parser.add_argument("--min-deficit", type=float, default=2.0)
    return parser.parse_args()


def main():
    args = parse_args()
    result, summaries = analyse(args.limit, args.factor, args.min_deficit)
    print_report(result, summaries, args.limit, args.min_deficit)


if __name__ == "__main__":
    main()
