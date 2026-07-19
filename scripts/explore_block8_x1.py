#!/usr/bin/env python3
"""Probe Gap SD-K-block-8 from explicit x1 = (3^{n+1}-1)/8 for n ≡ 1 mod 8."""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict


def v2(v: int) -> int:
    return (v & -v).bit_length() - 1


def h_of(x: int) -> int:
    return v2(x + 1)


def x1_of(n: int) -> int:
    assert n % 8 == 1 and n >= 9
    return (3 ** (n + 1) - 1) // 8


def blocks_from_x1(n: int) -> dict:
    t = 6 * n
    e0 = 2
    steps = e0  # seed already consumed
    x = x1_of(n)
    assert h_of(x) == 1
    deltas = []
    pairs = []
    while steps < t:
        raw = 3 * x + 1
        e = v2(raw)
        rem = t - steps
        if e > rem:
            heff = 1
            em1 = max(0, rem - 1)
            deltas.append(11 * em1 - 9 * heff)
            pairs.append((e, heff, True))
            break
        steps += e
        x = raw >> e
        hl = h_of(x)
        rails = 0
        while h_of(x) >= 2 and steps < t:
            steps += 1
            x = (3 * x + 1) >> 1
            rails += 1
        heff = 1 + rails if rails < hl - 1 else hl
        deltas.append(11 * (e - 1) - 9 * heff)
        pairs.append((e, heff, False))
    return {
        "n": n,
        "sum": sum(deltas),
        "deltas": deltas,
        "pairs": pairs,
        "first": pairs[0] if pairs else None,
        "running_min": _runmin(deltas),
        "blocks": len(deltas),
    }


def _runmin(deltas: list[int]) -> int:
    s = 0
    mn = 0
    for d in deltas:
        s += d
        if s < mn:
            mn = s
    return mn


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=2001)
    args = parser.parse_args()

    rows = []
    first_by_mod = defaultdict(list)
    for n in range(17, args.limit + 1, 8):
        r = blocks_from_x1(n)
        rows.append(r)
        e, h, _ = r["first"]
        first_by_mod[n % 64].append((n, e, h, 11 * (e - 1) - 9 * h, r["sum"]))

    rows.sort(key=lambda r: r["sum"])
    print("tightest sum Delta:")
    for r in rows[:12]:
        e, h, _ = r["first"]
        print(
            f"  n={r['n']} sum={r['sum']} first=(e={e},h={h},D={11*(e-1)-9*h}) "
            f"runmin={r['running_min']} blocks={r['blocks']} mod64={r['n']%64}"
        )

    print("first-block pattern by n mod 64:")
    for mod in sorted(first_by_mod):
        sample = first_by_mod[mod][:3]
        # check stability of (e,h) within class
        keys = {(e, h) for _, e, h, _, _ in first_by_mod[mod]}
        minsum = min(s for *_, s in first_by_mod[mod])
        print(f"  mod64={mod:2d}: (e,h) set={sorted(keys)} minsum={minsum} sample={sample}")

    # Cumulative: after k blocks, is sum eventually positive?
    # Stratify: n=1 mod 32 vs others
    c1 = [r for r in rows if r["n"] % 32 == 1]
    cother = [r for r in rows if r["n"] % 32 != 1]
    print(
        f"n=1 mod 32: count={len(c1)} min_sum={min(r['sum'] for r in c1)} "
        f"min_firstD={min(11*(r['first'][0]-1)-9*r['first'][1] for r in c1)}"
    )
    print(
        f"n=1 mod 8, not 1 mod 32: count={len(cother)} "
        f"min_sum={min(r['sum'] for r in cother)}"
    )

    # Count negative first blocks that recover
    neg_first = [r for r in rows if 11 * (r["first"][0] - 1) - 9 * r["first"][1] < 0]
    print(
        f"negative first Delta: {len(neg_first)}; "
        f"all recover to sum>=0? {all(r['sum']>=0 for r in neg_first)}; "
        f"worst sum among them={min(r['sum'] for r in neg_first)}"
    )

    # Joint law on full hard class
    joint = Counter()
    for r in rows:
        for e, h, _ in r["pairs"]:
            joint[(min(e, 6), min(h, 6))] += 1
    print("top (e,h):", joint.most_common(8))


if __name__ == "__main__":
    main()
