#!/usr/bin/env python3
"""Probe residual recovery after first block for n ≡ 17 mod 64."""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict


def v2(v: int) -> int:
    return (v & -v).bit_length() - 1


def h_of(x: int) -> int:
    return v2(x + 1)


def first_landing(n: int) -> tuple[int, int, int]:
    """Return (e1, h1, x2) where x2 is the next h=1 state after first block."""
    x1 = (3 ** (n + 1) - 1) // 8
    e = v2(3 * x1 + 1)
    y = (3 * x1 + 1) >> e
    # rail down from height h1 to h=1
    while h_of(y) >= 2:
        y = (3 * y + 1) >> 1
    return e, h_of((3 * x1 + 1) >> e), y


def block_stream(n: int, max_blocks: int | None = None):
    t = 6 * n
    steps = 2
    x = (3 ** (n + 1) - 1) // 8
    out = []
    while steps < t:
        if max_blocks is not None and len(out) >= max_blocks:
            break
        raw = 3 * x + 1
        e = v2(raw)
        rem = t - steps
        if e > rem:
            out.append(
                {
                    "e": e,
                    "heff": 1,
                    "delta": 11 * max(0, rem - 1) - 9,
                    "trunc": True,
                    "x_in": x,
                }
            )
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
        out.append(
            {
                "e": e,
                "heff": heff,
                "hl": hl,
                "delta": 11 * (e - 1) - 9 * heff,
                "trunc": False,
                "x_out": x,
                "steps": steps,
            }
        )
    return out


def second_e_formula_candidates(n: int, x2: int) -> dict:
    """Try closed forms for e2 / h2 from x2."""
    e2 = v2(3 * x2 + 1)
    y = (3 * x2 + 1) >> e2
    h2 = h_of(y)
    return {
        "e2": e2,
        "h2": h2,
        "delta2": 11 * (e2 - 1) - 9 * h2,
        "v2_3x2p1": e2,
        "x2_mod_32": x2 % 32,
        "x2_mod_64": x2 % 64,
        "x2_mod_128": x2 % 128,
        "x2_mod_256": x2 % 256,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=2001)
    args = parser.parse_args()

    print("=== hard subclasses (odd k or k=2 mod 4): early blocks ===")
    for n in range(17, args.limit + 1, 64):
        k = (n - 17) // 64
        if k == 0:
            continue
        if not (k % 2 == 1 or k % 4 == 2):
            continue
        b = block_stream(n)
        h1 = b[0]["heff"]
        need = 9 * h1 - 11
        rest = sum(x["delta"] for x in b[1:])
        print(
            f"n={n} k={k} h1={h1} need={need} rest={rest} "
            f"margin={rest - need} sum={b[0]['delta'] + rest}"
        )
        for i, x in enumerate(b[:6]):
            print(
                f"  j={i + 1} e={x['e']} h={x['heff']} D={x['delta']}"
            )

    print("\n=== second block after first landing (all k>=1) ===")
    e2s = Counter()
    h2s = Counter()
    d2s = []
    mod_to_eh = defaultdict(Counter)
    for n in range(81, args.limit + 1, 64):
        e1, h1, x2 = first_landing(n)
        info = second_e_formula_candidates(n, x2)
        e2s[info["e2"]] += 1
        h2s[info["h2"]] += 1
        d2s.append((n, h1, info["delta2"], info["e2"], info["h2"], x2 % 256))
        mod_to_eh[n % 256][(info["e2"], info["h2"])] += 1

    print("e2 histogram:", dict(sorted(e2s.items())))
    print("h2 histogram:", dict(sorted(h2s.items())))
    print("tightest Delta2:")
    for row in sorted(d2s, key=lambda r: r[2])[:12]:
        n, h1, d2, e2, h2, xm = row
        print(f"  n={n} h1={h1} e2={e2} h2={h2} D2={d2} x2%256={xm}")

    print("\n=== cumulative rest after m blocks vs need ===")
    for m in [2, 3, 4, 5, 8, 12]:
        fails = 0
        worst = None
        for n in range(81, args.limit + 1, 64):
            b = block_stream(n, max_blocks=m)
            h1 = b[0]["heff"]
            need = 9 * h1 - 11
            partial = sum(x["delta"] for x in b[1:])
            # only fair if we consumed all of rest window — partial may undercount
            # here we measure whether early recovery already clears need
            if partial >= need:
                ok = True
            else:
                ok = False
                fails += 1
            margin = partial - need
            if worst is None or margin < worst[0]:
                worst = (margin, n, h1, need, partial)
        print(
            f"m={m}: early_clear fails={fails}/{((args.limit - 81) // 64) + 1} "
            f"worst_margin={worst}"
        )

    print("\n=== mean Delta per residual block (k>=1) ===")
    totals = []
    for n in range(81, args.limit + 1, 64):
        b = block_stream(n)
        rest_blocks = b[1:]
        if not rest_blocks:
            continue
        avg = sum(x["delta"] for x in rest_blocks) / len(rest_blocks)
        totals.append((n, len(rest_blocks), avg, sum(x["delta"] for x in rest_blocks) / n))
    print(
        "rest/n range:",
        min(t[3] for t in totals),
        max(t[3] for t in totals),
        "mean",
        sum(t[3] for t in totals) / len(totals),
    )
    print(
        "avg Delta/block range:",
        min(t[2] for t in totals),
        max(t[2] for t in totals),
        "mean",
        sum(t[2] for t in totals) / len(totals),
    )

    # Try to find closed form for x2 after first rail
    print("\n=== x2 closed form search ===")
    # After e=2 at x1: y=(3*x1+1)/4 = (3^{n+2}+5)/32
    # Then rail h1-1 times: each step x |-> (3x+1)/2
    # After r rails: x = 3^r * y + (3^r - 1)/2  all over 2^r? 
    # Actually (3x+1)/2 iterated: x_{i+1}=(3x_i+1)/2
    # => x_r = 3^r y / 2^r + (3^r - 1)/(2^r * 1?) wait
    # x_r = 3^r * y * 2^{-r} + sum_{j=0}^{r-1} 3^j * 2^{-(j+1)} * 2^{?}
    # Standard: x_r = 3^r y / 2^r + (3^r - 1)/2^{r+?} no:
    # x <- (3x+1)/2 : x_r = (3^r y + 3^{r-1} + ... + 1)/2^r = (3^r y + (3^r-1)/2)/2^r
    # = (2*3^r y + 3^r - 1)/(2^{r+1})
    for n in [81, 145, 209, 273, 337]:
        e1, h1, x2 = first_landing(n)
        y = (3 ** (n + 2) + 5) // 32
        r = h1 - 1
        pred = (2 * (3**r) * y + (3**r) - 1) // (2 ** (r + 1))
        # wait check integer formula
        z = y
        for _ in range(r):
            z = (3 * z + 1) // 2
        print(
            f"n={n} h1={h1} r={r} x2={x2} rail_end={z} match={x2 == z} "
            f"pred={pred} pred_ok={pred == z}"
        )
        # simplify with y=(3^{n+2}+5)/32
        # x2 = (2*3^r * y + 3^r - 1)/(2^{r+1})
        # = (3^r (2y+1) - 1)/(2^{r+1})
        # 2y+1 = (3^{n+2}+5)/16 + 1 = (3^{n+2}+21)/16
        # x2 = (3^r (3^{n+2}+21)/16 - 1)/(2^{r+1})
        # = (3^r (3^{n+2}+21) - 16)/(16 * 2^{r+1})
        # = (3^{n+2+r} + 21*3^r - 16)/(2^{r+5})
        alt = (3 ** (n + 2 + r) + 21 * (3**r) - 16) // (2 ** (r + 5))
        print(f"  closed={alt} ok={alt == x2}")
        # e2 = v2(3*x2+1)
        num = 3 * (3 ** (n + 2 + r) + 21 * (3**r) - 16) + 2 ** (r + 5)
        # 3*x2+1 = [3*(3^{n+2+r}+21*3^r-16) + 2^{r+5}] / 2^{r+5}
        print(
            f"  e2={v2(3 * x2 + 1)} "
            f"v2(num)={v2(3 * (3 ** (n + 2 + r) + 21 * (3**r) - 16) + 2 ** (r + 5))} "
            f"minus denom {r + 5}"
        )


if __name__ == "__main__":
    main()
