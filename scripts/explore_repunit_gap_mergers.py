#!/usr/bin/env python3
"""Analyse predecessor-state algebra for same-diagonal repunit mergers.

For a first exact merge

    x_i(n) = x_j(m),  n > m,  n+i = m+j,

compare the predecessor diagonal states

    (d-1, E, A), (d-1, F, B).

They coalesce on the next step exactly when

    3A + 2^(E+1) = 3B + 2^(F+1).

The script extracts the valuation-gap and correction-gap templates for
selected exponent gaps. All output is a finite diagnostic.
"""

import argparse
from collections import Counter, defaultdict

from explore_repunit_tail_merges import scan as scan_merges


def v2(value):
    return (value & -value).bit_length() - 1


def normal_states(n, last_step):
    """Return states (x, E, A) and outgoing valuations through last_step."""
    x = (3**n - 1) // 2
    E = 0
    A = -1
    states = [(x, E, A)]
    valuations = []

    for _ in range(last_step):
        value = 3 * x + 1
        e = v2(value)
        x = value >> e
        A = 3 * A + (1 << (E + 1))
        E += e
        valuations.append(e)
        states.append((x, E, A))

    return states, valuations


def analyse_merge(row):
    n = row["n"]
    i = row["step"]
    m = row["source_n"]
    j = row["source_step"]
    assert i >= 1 and j >= 1
    assert n + i == m + j

    n_states, n_vals = normal_states(n, i)
    m_states, m_vals = normal_states(m, j)

    x, E, A = n_states[i - 1]
    y, F, B = m_states[j - 1]
    e = n_vals[i - 1]
    f = m_vals[j - 1]

    H_left = 3 * A + (1 << (E + 1))
    H_right = 3 * B + (1 << (F + 1))
    assert x != y
    assert H_left == H_right
    assert n_states[i] == m_states[j]
    assert E + e == F + f

    low_E = min(E, F)
    high_E = max(E, F)
    delta = high_E - low_E
    assert delta > 0 and delta % 2 == 0

    if E < F:
        low_side = "large"
        low_state = x
        high_state = y
        high_incoming_e = m_vals[j - 2] if j >= 2 else None
        correction_quotient = (A - B) >> (E + 1)
        low_next = e
        high_next = f
    else:
        low_side = "small"
        low_state = y
        high_state = x
        high_incoming_e = n_vals[i - 2] if i >= 2 else None
        correction_quotient = (B - A) >> (F + 1)
        low_next = f
        high_next = e

    expected_quotient = ((1 << delta) - 1) // 3
    assert correction_quotient == expected_quotient
    assert low_next - high_next == delta
    h = delta // 2
    virtual_partner = (1 << (2 * h)) * high_state + (
        (1 << (2 * h)) - 1
    ) // 3
    assert low_state == virtual_partner
    incoming_selects_shell = (
        high_incoming_e is not None
        and 2 * (high_incoming_e // 2) == delta
    )

    return {
        **row,
        "pre_diagonal": n + i - 1,
        "large_E": E,
        "small_E": F,
        "large_A": A,
        "small_A": B,
        "large_next_e": e,
        "small_next_e": f,
        "low_side": low_side,
        "valuation_gap": delta,
        "low_next_e": low_next,
        "high_next_e": high_next,
        "high_incoming_e": high_incoming_e,
        "incoming_selects_shell": incoming_selects_shell,
        "correction_quotient": correction_quotient,
    }


def scan(limit, gaps, factor):
    merge_result = scan_merges(limit=limit, factor=factor)
    selected = [
        analyse_merge(row)
        for row in merge_result["merges"]
        if row["gap"] in gaps
    ]
    return merge_result, selected


def template_key(row):
    return (
        row["low_side"],
        row["valuation_gap"],
        row["low_next_e"],
        row["high_next_e"],
    )


def print_gap_report(gap, rows, top):
    print(f"\n== exponent gap {gap} ==")
    print(f"mergers={len(rows)}")

    valuation_gaps = Counter(row["valuation_gap"] for row in rows)
    orientations = Counter(row["low_side"] for row in rows)
    templates = Counter(template_key(row) for row in rows)
    merge_steps = Counter(row["step"] for row in rows)

    print(f"valuation-gap counts: {valuation_gaps.most_common(20)}")
    print(f"lower-cumulative-valuation side: {dict(orientations)}")
    print(f"most common predecessor templates:")
    for key, count in templates.most_common(top):
        low_side, delta, low_next, high_next = key
        quotient = ((1 << delta) - 1) // 3
        print(
            f"  count={count} low_side={low_side} delta={delta} "
            f"next valuations=({low_next},{high_next}) "
            f"correction quotient=(2^{delta}-1)/3={quotient}"
        )

    early = sorted(rows, key=lambda row: (row["step"], row["n"]))
    print(f"smallest large-tail merge steps: {merge_steps.most_common(10)}")
    print("first examples:")
    for row in early[:top]:
        print(
            f"  n={row['n']} step={row['step']} -> "
            f"m={row['source_n']} step={row['source_step']} "
            f"pre=(E,F)=({row['large_E']},{row['small_E']}) "
            f"next=(e,f)=({row['large_next_e']},{row['small_next_e']}) "
            f"delta={row['valuation_gap']} low={row['low_side']}"
        )


def print_cross_gap_summary(rows):
    by_template = defaultdict(Counter)
    for row in rows:
        by_template[template_key(row)][row["gap"]] += 1

    ranked = sorted(
        by_template.items(),
        key=lambda item: sum(item[1].values()),
        reverse=True,
    )
    print("\n== templates shared across exponent gaps ==")
    for key, gaps in ranked[:20]:
        if len(gaps) < 2:
            continue
        print(
            f"template={key} total={sum(gaps.values())} "
            f"gap_counts={dict(gaps)}"
        )


def print_virtual_partner_summary(rows):
    selected = [row for row in rows if row["incoming_selects_shell"]]
    print("\n== canonical virtual-partner selection ==")
    print(
        f"first mergers selected by the high state's incoming payout: "
        f"{len(selected)}/{len(rows)}="
        f"{len(selected)/len(rows):.2%}"
    )
    print(
        "selected incoming valuations: "
        f"{Counter(row['high_incoming_e'] for row in selected).most_common()}"
    )
    print(
        "selected collision shells: "
        f"{Counter(row['valuation_gap'] for row in selected).most_common()}"
    )


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=2001)
    parser.add_argument("--gaps", default="2,4,6")
    parser.add_argument("--factor", type=int, default=3)
    parser.add_argument("--top", type=int, default=12)
    return parser.parse_args()


def main():
    args = parse_args()
    gaps = {int(value) for value in args.gaps.split(",")}
    merge_result, rows = scan(args.limit, gaps, args.factor)
    print("== Repunit gap-merger algebra ==")
    print(
        f"finite domain: odd 7 <= n <= {args.limit}; "
        f"all merges={len(merge_result['merges'])}; "
        f"selected={len(rows)}"
    )
    all_rows = [analyse_merge(row) for row in merge_result["merges"]]
    all_shells = Counter(row["valuation_gap"] for row in all_rows)
    shell_two = all_shells[2]
    print(
        f"all collision shells: {all_shells.most_common()} "
        f"(delta=2: {shell_two}/{len(all_rows)}="
        f"{shell_two / len(all_rows):.2%})"
    )

    for gap in sorted(gaps):
        print_gap_report(
            gap,
            [row for row in rows if row["gap"] == gap],
            args.top,
        )
    print_cross_gap_summary(rows)
    print_virtual_partner_summary(all_rows)


if __name__ == "__main__":
    main()
