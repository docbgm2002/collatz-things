#!/usr/bin/env python3
"""Probe pre/post split bounds for Gap SD-K-nc-6.

Uses the rigorous pre-descent inequality 3^{rho_pre} a_n < T * 2^H
and measures post-descent odd density / room against floor(33n/10).
"""

from __future__ import annotations

import argparse
import math


def v2(v: int) -> int:
    return (v & -v).bit_length() - 1


def split(n: int) -> dict:
    t = 6 * n
    cap = (33 * n) // 10
    threshold = (1 << n) - 1
    a_n = (3**n - 1) // 2
    x = a_n
    steps = 0
    odd = 0
    h = None
    rho_pre = None
    while steps < t:
        raw = 3 * x + 1
        e = v2(raw)
        for division in range(1, e + 1):
            steps += 1
            if division == 1:
                odd += 1
            cand = raw >> division
            if h is None and cand < threshold:
                h = steps
                rho_pre = odd
            x = cand
            if steps >= t:
                break
        else:
            continue
        break
    if h is None:
        h = t
        rho_pre = odd
    rho_post = odd - rho_pre
    post_len = t - h
    # rigorous float log bound (use logs to avoid overflow)
    log_bound = (n * math.log(2) + h * math.log(2) - math.log(a_n)) / math.log(3)
    return {
        "n": n,
        "H": h,
        "t": t,
        "cap": cap,
        "rho": odd,
        "rho_pre": rho_pre,
        "rho_post": rho_post,
        "post_len": post_len,
        "dens_post": rho_post / post_len if post_len else None,
        "log_bound": log_bound,
        "pre_slack": log_bound - rho_pre,
        "room": cap - rho_pre,
        "ok": odd <= cap or n == 11,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=2001)
    args = parser.parse_args()

    rows = []
    for n in range(7, args.limit + 1, 2):
        rows.append(split(n))

    # Bound: rho <= floor(log_bound) + post_len  (all-odd post) — always ~t
    # Better: rho <= floor(log_bound) + ceil(alpha * post_len)
    for alpha in (0.5, 0.52, 0.55, 2 / 3):
        fails = []
        for r in rows:
            if r["n"] == 11:
                continue
            pred = math.floor(r["log_bound"]) + math.ceil(alpha * r["post_len"])
            if pred < r["rho"]:
                # bound not valid for this alpha (shouldn't happen if alpha=1)
                pass
            # sufficient for nc-6 if pred <= cap
            if pred > r["cap"]:
                fails.append(r["n"])
        print(
            f"alpha={alpha}: sufficient-bound fails count={len(fails)} "
            f"first={fails[:12]}"
        )

    # What alpha_n = rho_post/post_len requires for room: need
    # rho_pre + alpha*post <= cap
    tight = []
    for r in rows:
        if r["n"] == 11 or r["post_len"] == 0:
            continue
        need_alpha = (r["cap"] - r["rho_pre"]) / r["post_len"]
        tight.append((need_alpha - (r["dens_post"] or 0), need_alpha, r["dens_post"], r["n"], r["H"], r["post_len"]))
    tight.sort()
    print("tightest (need_alpha - dens_post) room:", tight[:12])
    print("min need_alpha:", min(tight, key=lambda z: z[1])[:6])

    # Pure H<=6n attack: max H/n
    hn = sorted(((r["H"] / r["n"], r["n"], r["H"]) for r in rows), reverse=True)
    print("top H/n:", hn[:10])

    # 911-6 on full window
    bad_911 = []
    for r in rows:
        even = r["t"] - r["rho"]
        score = 11 * even - 9 * (r["rho"] - 1)
        if score < 0:
            bad_911.append((r["n"], score, r["rho"], r["cap"]))
    print("911-6 fails:", bad_911)


if __name__ == "__main__":
    main()
