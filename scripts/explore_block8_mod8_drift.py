#!/usr/bin/env python3
"""Probe h=1 mod-8 imbalance and Extra on residual for n=17 mod 64."""

from __future__ import annotations

import argparse
from collections import Counter


def v2(v: int) -> int:
    return (v & -v).bit_length() - 1


def h_of(x: int) -> int:
    return v2(x + 1)


def residual_mod8(n: int) -> dict:
    y = (3 ** (n + 2) + 5) // 32
    h1 = h_of(y)
    x = (3 ** (h1 - 1) * (y + 1)) // (2 ** (h1 - 1)) - 1
    t = 6 * n
    steps = h1 + 3
    B1 = B5 = 0
    Extra = O = B = 0
    extra5 = 0
    h_sum = 0
    x2_mod = x % 8
    while steps < t:
        assert h_of(x) == 1
        if x % 8 == 1:
            B1 += 1
        else:
            assert x % 8 == 5
            B5 += 1
        raw = 3 * x + 1
        e = v2(raw)
        rem = t - steps
        if e > rem:
            O += 1
            break
        steps += e
        O += 1
        Extra += e - 2
        if x % 8 == 5:
            extra5 += e - 2
        B += 1
        x = raw >> e
        hl = h_of(x)
        h_sum += hl if steps + (hl - 1) <= t else 1  # rough
        rails = 0
        while h_of(x) >= 2 and steps < t:
            steps += 1
            x = (3 * x + 1) >> 1
            rails += 1
            O += 1
        # correct h contribution already in O via rails+1
    L = 6 * n - (h1 + 3)
    # recompute O,E properly from rest identity: use block stream already
    # O counted above; E = Extra + B (if no trunc oddities)
    E = Extra + B
    # fix L from O+E if truncation
    L_act = O + E
    rest = 11 * E - 9 * O
    need = 9 * h1 - 11
    return {
        "n": n,
        "h1": h1,
        "x2_mod8": x2_mod,
        "B": B,
        "B1": B1,
        "B5": B5,
        "f5": B5 / B if B else None,
        "Extra": Extra,
        "extra5": extra5,
        "Extra_over_B": Extra / B if B else None,
        "Extra_over_B5": extra5 / B5 if B5 else None,
        "O": O,
        "O_over_B": O / B if B else None,
        "dens": O / L_act if L_act else None,
        "rest": rest,
        "need": need,
        "margin": rest - need,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=4001)
    args = parser.parse_args()

    rows = []
    for n in range(81, args.limit + 1, 64):
        rows.append(residual_mod8(n))

    print("worst f5 (B5/B):")
    for r in sorted(rows, key=lambda r: r["f5"])[:8]:
        print(
            f"  n={r['n']} f5={r['f5']:.4f} Extra/B={r['Extra_over_B']:.3f} "
            f"Extra/B5={r['Extra_over_B5']:.3f} O/B={r['O_over_B']:.3f} "
            f"dens={r['dens']:.4f} x2%8={r['x2_mod8']} margin={r['margin']}"
        )

    print("\nworst Extra/B:")
    for r in sorted(rows, key=lambda r: r["Extra_over_B"])[:8]:
        print(
            f"  n={r['n']} Extra/B={r['Extra_over_B']:.3f} f5={r['f5']:.4f} "
            f"O/B={r['O_over_B']:.3f} dens={r['dens']:.4f} margin={r['margin']}"
        )

    print("\nworst dens:")
    for r in sorted(rows, key=lambda r: -r["dens"])[:8]:
        print(
            f"  n={r['n']} dens={r['dens']:.4f} f5={r['f5']:.4f} "
            f"Extra/B={r['Extra_over_B']:.3f} O/B={r['O_over_B']:.3f} "
            f"margin={r['margin']}"
        )

    # Sufficient pair: Extra/B >= a and O/B <= b
    print("\nsearch sufficient (a,b) with Extra/B>=a, O/B<=b => rest/B>=16/B:")
    for a in [0.75, 0.80, 0.82, 0.85, 0.90]:
        for b in [2.05, 2.10, 2.12, 2.15, 2.20]:
            pred = 11 * a + 11 - 9 * b
            fails = [
                r
                for r in rows
                if r["Extra_over_B"] < a or r["O_over_B"] > b
            ]
            # among those satisfying the hyp, check rest
            ok_rows = [
                r
                for r in rows
                if r["Extra_over_B"] >= a and r["O_over_B"] <= b
            ]
            if not ok_rows:
                continue
            min_rest_over_B = min(
                (11 * r["Extra_over_B"] + 11 - 9 * r["O_over_B"]) for r in ok_rows
            )
            # does hyp hold for all rows?
            hyp_all = len(fails) == 0
            print(
                f"  a={a} b={b} pred_per_B={pred:.3f} hyp_all={hyp_all} "
                f"fails_hyp={len(fails)} min_rest/B_on_hyp={min_rest_over_B:.3f}"
            )

    # x2 mod 8 by class
    print("\nx2 mod 8 by k class:")
    for label, pred in [
        ("odd k", lambda k: k % 2 == 1),
        ("k=3 mod 8", lambda k: k % 8 == 3),
        ("k=2 mod 4", lambda k: k % 4 == 2),
    ]:
        mods = Counter()
        for n in range(81, args.limit + 1, 64):
            k = (n - 17) // 64
            if not pred(k):
                continue
            mods[residual_mod8(n)["x2_mod8"]] += 1
        print(f"  {label}: {dict(mods)}")


if __name__ == "__main__":
    main()
