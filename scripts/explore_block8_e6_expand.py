#!/usr/bin/env python3
"""Expansion diagnostics for the uniform 267-family lemma (SD-K-e6-expand).

On k == 267 (mod 512), write k = 267 + 512t and check:
  - m == 6201 - 512t == 6468 - k (mod 8192)   [Lemma SD-K-m-mod8192-267]
  - (d2,d3,d4,d5) == (2,2,2,2)                [Lemma SD-K-blocks25-267mod512]
  - 3x6+1 == (1440 - 492t) mod 8192, v2(error) >= 13  [Lemma SD-K-e6-param-267]
  - e6 == v2(1440 - 492t) when v2(1440 - 492t) < 13
  - d6 == 11*(e6-1) - 9*h6 from L_t landing [Cor SD-K-d6-param-267]

Also flags when x6 mod 32 fails to determine d6 (heff split).
"""

from __future__ import annotations

import argparse
import sys
from math import comb

from verify_repunit_storage_dominance import h_of, v2, _block_deltas_after_first

B = (3**19 + 37) // 256
U = (3**64 - 1) // 256


def m_of(n: int) -> int:
    h1 = v2(3 ** (n + 2) + 37) - 5
    return (3 ** (n + 2) + 37) // (2 ** (h1 + 5))


def block6_start_x(n: int) -> int:
    x1 = (3 ** (n + 1) - 1) // 8
    x = (3 * x1 + 1) >> 2
    while h_of(x) >= 2:
        x = (3 * x + 1) >> 1
    for _ in range(2, 6):
        raw = 3 * x + 1
        e = v2(raw)
        x = raw >> e
        while h_of(x) >= 2:
            x = (3 * x + 1) >> 1
        while h_of(x) >= 2:
            x = (3 * x + 1) >> 1
    return x


def q_mod8192_j2(k: int) -> int:
    u9 = U % 8192
    return (k * u9 + comb(k, 2) * 256 * (u9 * u9 % 8192)) % 8192


def z6_from_t(t: int) -> int:
    """Odd z with 2^e6 * z == L_t (mod 8192) for L_t = 1440 - 492t."""
    lt = 1440 - 492 * t
    e6 = v2(abs(lt))
    for cand in range(1, 8192, 2):
        if (cand << e6) % 8192 == lt % 8192:
            return cand
    raise ValueError(t)


def h6_eff_from_y(y: int) -> tuple[int, int]:
    hl = h_of(y)
    rails = 0
    z = y
    while h_of(z) >= 2:
        z = (3 * z + 1) >> 1
        rails += 1
    heff = 1 + rails if rails < hl - 1 else hl
    return hl, heff


def block6_landing_y(n: int) -> tuple[int, int]:
    x6 = block6_start_x(n)
    raw = 3 * x6 + 1
    e6 = v2(raw)
    return raw >> e6, e6


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit-k", type=int, default=8001)
    parser.add_argument(
        "--check-m-param",
        action="store_true",
        help="exit 1 if m mod 8192 != (6201-512t) on any sample",
    )
    parser.add_argument(
        "--check-e6-param",
        action="store_true",
        help="exit 1 if e6 param identities fail on any sample",
    )
    parser.add_argument(
        "--check-d6-param",
        action="store_true",
        help="exit 1 if d6 param identities fail on any sample",
    )
    args = parser.parse_args()

    rows: list[dict] = []
    m_fail = 0
    b25_fail = 0
    q_fail = 0
    e6_fail = 0
    err_fail = 0
    d6_fail = 0

    for k in range(267, args.limit_k + 1, 512):
        t = (k - 267) // 512
        n = 64 * k + 17
        m = m_of(n)
        m_pred = (6201 - 512 * t) % 8192
        if m % 8192 != m_pred:
            m_fail += 1
        q_exact = ((pow(1 + 256 * U, k, 1 << 40) - 1) // 256) % 8192
        if q_mod8192_j2(k) != q_exact:
            q_fail += 1
        _, d = _block_deltas_after_first(n, max_blocks=6)
        if tuple(d[:4]) != (2, 2, 2, 2):
            b25_fail += 1
        x6 = block6_start_x(n)
        exact = 3 * x6 + 1
        lead = 1440 - 492 * t
        if exact % 8192 != lead % 8192:
            e6_fail += 1
        err = exact - lead
        err_v2 = v2(abs(err)) if err else 99
        min_err = 14
        if err and err_v2 < min_err:
            err_fail += 1
        lead_v2 = v2(abs(lead))
        e6 = v2(exact)
        if lead_v2 < 13 and e6 != lead_v2:
            e6_fail += 1
        y6, _ = block6_landing_y(n)
        h6, heff = h6_eff_from_y(y6)
        z6 = z6_from_t(t)
        d6_pred = 11 * (e6 - 1) - 9 * h_of(z6)
        if h6 != h_of(z6) or heff != h6 or d[4] != d6_pred:
            d6_fail += 1
        rows.append(
            {
                "t": t,
                "k": k,
                "r": k % 8192,
                "m8192": m % 8192,
                "d6": d[4],
                "x6_32": x6 % 32,
                "e6": e6,
                "lead_v2": lead_v2,
                "err_v2": err_v2 if err else 0,
            }
        )

    print(f"k == 267 mod 512 through k <= {args.limit_k}: {len(rows)} samples")
    print(f"m == 6201-512t (mod 8192) failures: {m_fail}")
    print(f"Q j<=2 vs exact (mod 8192) failures: {q_fail}")
    print(f"blocks 2-5 != (2,2,2,2) failures: {b25_fail}")
    print(f"e6 param failures: {e6_fail}")
    print(f"v2(error) below threshold failures: {err_fail}")
    print(f"d6 param failures: {d6_fail}")
    print()
    print("t | k mod 8192 | m mod 8192 | x6 mod 32 | e6 | v2(1440-492t) | err v2 | d6")
    for r in rows:
        print(
            f"{r['t']:2d} | {r['r']:4d}       | {r['m8192']:4d}       | "
            f"{r['x6_32']:8d} | {r['e6']:2d} | {r['lead_v2']:13d} | "
            f"{r['err_v2']:6d} | {r['d6']:4d}"
        )

    by_x32: dict[int, set[int]] = {}
    for r in rows:
        by_x32.setdefault(r["x6_32"], set()).add(r["d6"])
    print()
    print("x6 mod 32 -> d6 (collisions mean x32 alone is insufficient):")
    for x32 in sorted(by_x32):
        vals = sorted(by_x32[x32])
        tag = "COLLISION" if len(vals) > 1 else "ok"
        print(f"  x6 == {x32:2d} mod 32: d6 in {vals}  [{tag}]")

    if args.check_m_param and (m_fail or q_fail):
        raise SystemExit(1)
    if args.check_e6_param and (e6_fail or err_fail):
        raise SystemExit(1)
    if args.check_d6_param and d6_fail:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
