#!/usr/bin/env python3
"""Block-7 expansion diagnostics for deferred 267-family rows."""

from __future__ import annotations

import argparse
import sys
from collections import defaultdict

sys.path.insert(0, "scripts")
from verify_repunit_storage_dominance import h_of, v2, _block_deltas_after_first

# Leading 3x7+1 mod 8192 on deferred rows, by h6 class (from rail + landing).
E7_H1 = (4808, 6716)  # base at t=1, step 1476 mod 8192 (=8192-6716) every t+=4
E7_H3 = (5064, 4168)  # base at t=3, step every t+=11
E7_H5 = (4568, 2124)  # base at t=4, step every t+=7
E7_H2_TABLE = {6: 176, 7: 3892, 15: 7656}


def z6_from_t(t: int) -> tuple[int, int]:
    lt = 1440 - 492 * t
    e6 = v2(abs(lt))
    for cand in range(1, 8192, 2):
        if (cand << e6) % 8192 == lt % 8192:
            return cand, e6
    raise ValueError(t)


def get_row(t: int) -> dict:
    k = 267 + 512 * t
    n = 64 * k + 17
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
    y6 = (3 * x + 1) >> v2(3 * x + 1)
    h6 = h_of(y6)
    z = y6
    while h_of(z) >= 2:
        z = (3 * z + 1) >> 1
    while h_of(z) >= 2:
        z = (3 * z + 1) >> 1
    raw7 = 3 * z + 1
    _, d = _block_deltas_after_first(n, max_blocks=7)
    z6, e6 = z6_from_t(t)
    return {
        "t": t,
        "k8192": k % 8192,
        "h6": h6,
        "e6": e6,
        "z6": z6,
        "raw7": raw7,
        "raw7m": raw7 % 8192,
        "e7": v2(raw7),
        "d7": d[5],
        "d6": d[4],
        "cum6": sum(d[:5]),
    }


def h6_from_t(t: int) -> int:
    lt = 1440 - 492 * t
    e6 = v2(abs(lt))
    z6, _ = z6_from_t(t)
    return h_of(z6)


def predict_raw7_mod8192(t: int) -> int | None:
    h6 = h6_from_t(t)
    if h6 == 1 and t % 4 == 1:
        s = (t - 1) // 4
        return (E7_H1[0] - (8192 - E7_H1[1]) * s) % 8192
    if h6 == 3 and (t - 3) % 11 == 0:
        s = (t - 3) // 11
        return (E7_H3[0] + E7_H3[1] * s) % 8192
    if h6 == 5 and (t - 4) % 7 == 0:
        s = (t - 4) // 7
        return (E7_H5[0] + E7_H5[1] * s) % 8192
    if h6 == 2:
        return E7_H2_TABLE.get(t)
    return None


def h7_eff_from_raw7(raw7: int) -> tuple[int, int]:
    e7 = v2(raw7)
    y7 = raw7 >> e7
    hl = h_of(y7)
    rails = 0
    z = y7
    while h_of(z) >= 2:
        z = (3 * z + 1) >> 1
        rails += 1
    heff = 1 + rails if rails < hl - 1 else hl
    return hl, heff


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check-e7-param", action="store_true")
    parser.add_argument("--check-d7-param", action="store_true")
    args = parser.parse_args()

    deferred = [
        t
        for t in range(16)
        if sum(_block_deltas_after_first(64 * (267 + 512 * t) + 17, 6)[1][:5]) < 16
    ]
    rows = [get_row(t) for t in deferred]
    e7_fail = 0
    d7_fail = 0
    by_h: dict[int, list] = defaultdict(list)
    for r in rows:
        by_h[r["h6"]].append(r)

    print(f"deferred t: {deferred}")
    print()
    print("t | h6 | raw7%8192 | pred | e7 | d7 | cum6 | cum7")
    for r in rows:
        pred = predict_raw7_mod8192(r["t"])
        n = 64 * (267 + 512 * r["t"]) + 17
        _, d = _block_deltas_after_first(n, 7)
        cum7 = sum(d[:6])
        if pred is None or pred != r["raw7m"]:
            e7_fail += 1
        h7, heff = h7_eff_from_raw7(r["raw7"])
        d7_pred = 11 * (r["e7"] - 1) - 9 * heff
        if heff != h7 or d7_pred != r["d7"]:
            d7_fail += 1
        pred_s = "?" if pred is None else str(pred)
        ok = pred == r["raw7m"]
        print(
            f"{r['t']:2d} | {r['h6']:2d} | {r['raw7m']:4d}     | {pred_s:>4} "
            f"{'ok' if ok else 'FAIL'} | {r['e7']:2d} | {r['d7']:4d} | "
            f"{r['cum6']:4d} | {cum7:4d}"
        )

    for h, grp in sorted(by_h.items()):
        print(f"\n=== h6={h} ({len(grp)} rows) ===")
        for r in grp:
            print(
                f"  t={r['t']:2d} k%8192={r['k8192']:4d} "
                f"raw7%8192={r['raw7m']:4d} e7={r['e7']} d7={r['d7']:4d} z6={r['z6']}"
            )
        if len(grp) >= 2:
            t0, g0 = grp[0]["t"], grp[0]["raw7m"]
            t1, g1 = grp[1]["t"], grp[1]["raw7m"]
            dt = t1 - t0
            dg = (g1 - g0) % 8192
            ok = all(
                (g0 + dg * (r["t"] - t0) // dt) % 8192 == r["raw7m"]
                for r in grp
                if (r["t"] - t0) % dt == 0
            )
            print(f"  linear in t (step {dt}): dg={dg} ok={ok}")

    print("\n=== block-7 closers (cum6<16, cum7>=16) ===")
    for t in range(16):
        n = 64 * (267 + 512 * t) + 17
        _, d = _block_deltas_after_first(n, 7)
        if sum(d[:5]) >= 16 or sum(d[:6]) < 16:
            continue
        r = get_row(t)
        print(
            f"t={t:2d} k%8192={r['k8192']:4d} cum7={sum(d[:6]):3d} "
            f"d7={d[5]:4d} raw7%8192={r['raw7m']:4d} h6={r['h6']}"
        )

    print()
    print(f"e7 param failures: {e7_fail}")
    print(f"d7 param failures: {d7_fail}")
    if args.check_e7_param and e7_fail:
        raise SystemExit(1)
    if args.check_d7_param and d7_fail:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
