#!/usr/bin/env python3
"""Probe pre-/post-descent odd density for Gap SD-K-911."""

from __future__ import annotations

import argparse
import statistics as st


def v2(v: int) -> int:
    return (v & -v).bit_length() - 1


def split_stats(n: int) -> dict:
    t = 5 * n - 2
    threshold = (1 << n) - 1
    cap = (11 * n) // 4
    x = (3**n - 1) // 2
    odd_pre = even_pre = 0
    odd_post = even_post = 0
    steps = 0
    h = None
    pre = True
    while steps < t:
        if pre and steps > 0 and x < threshold:
            h = steps
            pre = False
        raw = 3 * x + 1
        e = v2(raw)
        for division in range(1, e + 1):
            steps += 1
            if division == 1:
                if pre:
                    odd_pre += 1
                else:
                    odd_post += 1
            else:
                if pre:
                    even_pre += 1
                else:
                    even_post += 1
            x = raw >> division
            if steps >= t:
                break
        else:
            continue
        break
    if h is None:
        h = t
    odd = odd_pre + odd_post
    even = even_pre + even_post
    need = t - cap
    post_len = t - h
    return {
        "n": n,
        "H": h,
        "t": t,
        "odd_pre": odd_pre,
        "even_pre": even_pre,
        "odd_post": odd_post,
        "even_post": even_post,
        "dens_pre": odd_pre / h if h else None,
        "dens_post": odd_post / post_len if post_len else None,
        "even": even,
        "need": need,
        "slack": even - need,
        "rho": odd,
        "cap": cap,
        "score": 11 * even - 9 * (odd - 1),
        "survivor": h >= t,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=2001)
    args = parser.parse_args()
    limit = args.limit

    rows = [split_stats(n) for n in range(7, min(limit, 501) + 1, 2)]
    surv = [r for r in rows if r["survivor"]]
    print("survivors H>=t in probed<=501:", [(r["n"], r["H"], r["rho"], r["cap"]) for r in surv])

    for lo, hi in ((7, 50), (51, 100), (101, 250), (251, 500)):
        sub = [r for r in rows if lo <= r["n"] <= hi]
        if not sub:
            continue
        print(
            f"n={lo}-{hi}: min_slack={min(r['slack'] for r in sub)}, "
            f"min_score={min(r['score'] for r in sub)}, "
            f"mean H/t={st.mean(r['H']/r['t'] for r in sub):.3f}, "
            f"mean dens_pre={st.mean(r['dens_pre'] for r in sub):.3f}, "
            f"mean dens_post={st.mean(r['dens_post'] for r in sub if r['dens_post'] is not None):.3f}"
        )

    print("selected:")
    for n in (17, 23, 25, 43, 131, 193, 501, 1001, 2001, 3001, 4001):
        if n > limit:
            break
        r = split_stats(n)
        dp = f"{r['dens_post']:.3f}" if r["dens_post"] is not None else "None"
        print(
            f"  n={n}: H={r['H']}/{r['t']} dens_pre={r['dens_pre']:.3f} "
            f"dens_post={dp} slack={r['slack']} score={r['score']} "
            f"surv={r['survivor']}"
        )

    # Large-n margin census
    if limit >= 101:
        worst = []
        for n in range(101, limit + 1, 2):
            r = split_stats(n)
            worst.append((r["slack"], r["score"], r["even"] / r["need"], n, r["H"], r["t"]))
        worst.sort()
        print("10 tightest slack for n>=101:", worst[:10])
        print(
            "min even/need n>=101:",
            min(worst, key=lambda z: z[2]),
        )


if __name__ == "__main__":
    main()
