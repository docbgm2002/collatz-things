#!/usr/bin/env python3
"""Probe Gap SD-K-block-8 on the tight class n ≡ 17 mod 64."""

from __future__ import annotations

import argparse
from collections import Counter


def v2(v: int) -> int:
    return (v & -v).bit_length() - 1


def h_of(x: int) -> int:
    return v2(x + 1)


def x1_of(n: int) -> int:
    return (3 ** (n + 1) - 1) // 8


def first_h_formula(n: int) -> int:
    """h of first landing after e=2 payout at x1."""
    # y = (3^{n+2}+5)/32
    return h_of((3 ** (n + 2) + 5) // 32)


def trajectory(n: int) -> dict:
    t = 6 * n
    steps = 2
    x = x1_of(n)
    assert h_of(x) == 1
    deltas = []
    pairs = []
    states = [x]
    while steps < t:
        raw = 3 * x + 1
        e = v2(raw)
        rem = t - steps
        if e > rem:
            heff = 1
            deltas.append(11 * max(0, rem - 1) - 9)
            pairs.append((e, heff))
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
        pairs.append((e, heff))
        # next h=1 state
        states.append(x)
    d1 = deltas[0]
    rest = sum(deltas[1:])
    # running sum after first
    s = d1
    min_after = s
    recover_at = None
    for i, d in enumerate(deltas[1:], start=2):
        s += d
        if s < min_after:
            min_after = s
        if recover_at is None and s >= 0:
            recover_at = i
    return {
        "n": n,
        "h1": pairs[0][1],
        "d1": d1,
        "rest": rest,
        "sum": d1 + rest,
        "min_after_first": min_after,
        "recover_at": recover_at,
        "blocks": len(deltas),
        "pairs": pairs,
        "deltas": deltas,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=2001)
    args = parser.parse_args()

    rows = []
    for n in range(17, args.limit + 1, 64):
        r = trajectory(n)
        assert r["h1"] == first_h_formula(n)
        rows.append(r)

    rows.sort(key=lambda r: r["sum"])
    print(f"class n=17 mod 64: count={len(rows)}")
    print("tightest sums:")
    for r in rows[:15]:
        print(
            f"  n={r['n']} h1={r['h1']} D1={r['d1']} rest={r['rest']} "
            f"sum={r['sum']} min_after={r['min_after_first']} "
            f"recover_at={r['recover_at']}/{r['blocks']}"
        )

    # h1 distribution
    hcount = Counter(r["h1"] for r in rows)
    print("h1 histogram:", dict(sorted(hcount.items())))

    # Is h1 related to v2(n-17) or similar?
    print("h1 vs v2(n-17)+c:")
    for r in rows[:20]:
        n = r["n"]
        print(
            f"  n={n} h1={r['h1']} v2(n-17)={v2(n-17) if n>17 else None} "
            f"v2(n+47)={v2(n+47)} v2(3^{n}+something) try"
        )

    # Search for 2-adic formula for h1 = v2((3^{n+2}+5)/32 + 1) = v2(3^{n+2}+37)-5
    print("check h1 == v2(3^{n+2}+37)-5:")
    bad = []
    for r in rows:
        n = r["n"]
        pred = v2(3 ** (n + 2) + 37) - 5
        if pred != r["h1"]:
            bad.append((n, r["h1"], pred))
    print("  mismatches", bad[:5], "count", len(bad))

    # Recovery: rest >= -D1?
    fails_rec = [r for r in rows if r["rest"] < -r["d1"]]
    print(
        f"rest >= -D1? fails={len(fails_rec)} "
        f"(should be 0 iff sum>=0; tautology sum=D1+rest)"
    )
    # Stronger: rest >= 34 (worst D1 for h=5 is -34; if h unbounded need more)
    # Bound h1?
    print("max h1", max(r["h1"] for r in rows), "at", max(rows, key=lambda r: r["h1"])["n"])
    print(
        "min rest",
        min(rows, key=lambda r: r["rest"])["n"],
        min(r["rest"] for r in rows),
    )
    print(
        "min (rest + D1)",
        min(rows, key=lambda r: r["sum"])["n"],
        min(r["sum"] for r in rows),
    )

    # After first block, state congruence
    print("post-first h=1 state mod 16 for small n:")
    for n in (17, 81, 145, 209, 273, 337):
        if n > args.limit:
            break
        x = x1_of(n)
        e = v2(3 * x + 1)
        x = (3 * x + 1) >> e
        while h_of(x) >= 2:
            x = (3 * x + 1) >> 1
        print(f"  n={n} h1={first_h_formula(n)} x2 mod 64={x%64} mod 256={x%256}")


if __name__ == "__main__":
    main()
