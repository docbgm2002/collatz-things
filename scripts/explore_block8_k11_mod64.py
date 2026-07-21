#!/usr/bin/env python3
"""Early-block dictionary for Gap SD-K-block-8-17 on k == 11 mod 64.

Supports the Avenue A attack on n = 64k + 17 with k == 11 (mod 64).  This
class does not close in four blocks like the Cor SD-K-block-8-17-early
progressions; block 5+ splits at mod 512 and deeper.  Output is evidence
only, not a universal proof.
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter, defaultdict


def v2(v: int) -> int:
    return (v & -v).bit_length() - 1


def h_of(x: int) -> int:
    return v2(x + 1)


def h1_val(n: int) -> int:
    return v2(3 ** (n + 2) + 37) - 5


def block_deltas(n: int, max_blocks: int = 10) -> tuple[int, list[int], list[tuple[int, int]]]:
    """Return (h1, deltas[1:], (e, heff) pairs) after the first block."""
    h1 = h1_val(n)
    x1 = (3 ** (n + 1) - 1) // 8
    assert v2(3 * x1 + 1) == 2
    x = (3 * x1 + 1) >> 2
    while h_of(x) >= 2:
        x = (3 * x + 1) >> 1
    deltas: list[int] = [11 - 9 * h1]
    pairs: list[tuple[int, int]] = []
    for _ in range(2, max_blocks + 1):
        raw = 3 * x + 1
        e = v2(raw)
        x = raw >> e
        hl = h_of(x)
        rails = 0
        while h_of(x) >= 2:
            x = (3 * x + 1) >> 1
            rails += 1
        heff = 1 + rails if rails < hl - 1 else hl
        deltas.append(11 * (e - 1) - 9 * heff)
        pairs.append((e, heff))
        while h_of(x) >= 2:
            x = (3 * x + 1) >> 1
    return h1, deltas[1:], pairs


def first_clear(rest_prefix: list[int], need: int = 16) -> int | None:
    total = 0
    for i, d in enumerate(rest_prefix, start=2):
        total += d
        if total >= need:
            return i
    return None


def stable_sigs(rows: list[dict], key_fn, delta_len: int) -> None:
    by: dict[int, list[tuple[int, ...]]] = defaultdict(list)
    for r in rows:
        by[key_fn(r)].append(tuple(r["d234"][:delta_len]))
    for residue in sorted(by):
        sigs = {t for t in by[residue]}
        stable = len(sigs) == 1
        sig = next(iter(sigs)) if stable else sorted(sigs)
        print(f"  k == {residue:4d} mod {key_fn.__name__}: stable={stable} signatures={sig}")


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit-k", type=int, default=3000, help="max k with k == 11 mod 64")
    parser.add_argument("--show", type=int, default=12, help="worst samples to print")
    args = parser.parse_args()

    rows: list[dict] = []
    for k in range(11, args.limit_k + 1, 64):
        n = 64 * k + 17
        h1, rest_d, pairs = block_deltas(n, max_blocks=10)
        need = 9 * h1 - 11
        rest = sum(rest_d)
        clear = first_clear(rest_d, need)
        rows.append(
            {
                "k": k,
                "n": n,
                "h1": h1,
                "rest": rest,
                "need": need,
                "clear": clear,
                "d234": tuple(rest_d[:3]),
                "d256": tuple(rest_d[:5]),
                "pairs5": pairs[:4],
            }
        )

    print(f"k == 11 mod 64 through k <= {args.limit_k}: count={len(rows)}")
    print("mod-256 block-2..4 signatures (d2,d3,d4):")
    by256: dict[int, list[tuple[int, int, int]]] = defaultdict(list)
    for r in rows:
        by256[r["k"] % 256].append(r["d234"])
    for residue in sorted(by256):
        sigs = {t for t in by256[residue]}
        stable = len(sigs) == 1
        sig = next(iter(sigs)) if stable else sorted(sigs)
        print(f"  k == {residue:3d} mod 256: stable={stable} signatures={sig}")

    slice11 = [r for r in rows if r["k"] % 256 == 11]
    if slice11:
        print("mod-512 block-2..5 on k == 11 mod 256:")
        by512: dict[int, list[tuple[int, ...]]] = defaultdict(list)
        for r in slice11:
            _, d, _ = block_deltas(r["n"], max_blocks=6)
            by512[r["k"] % 512].append(tuple(d[:4]))
        for residue in sorted(by512):
            sigs = {t for t in by512[residue]}
            stable = len(sigs) == 1
            sig = next(iter(sigs)) if stable else sorted(sigs)
            print(f"  k == {residue:3d} mod 512: stable={stable} signatures={sig}")

    slice267 = [r for r in rows if r["k"] % 512 == 267]
    if slice267:
        print("mod-8192 block-2..6 on k == 267 mod 512:")
        by8192: dict[int, list[tuple[int, ...]]] = defaultdict(list)
        for r in slice267:
            _, d, _ = block_deltas(r["n"], max_blocks=7)
            by8192[r["k"] % 8192].append(tuple(d[:5]))
        for residue in sorted(by8192):
            sigs = {t for t in by8192[residue]}
            stable = len(sigs) == 1
            sig = next(iter(sigs)) if stable else sorted(sigs)
            cum = sum(sig) if stable else None
            print(
                f"  k == {residue:4d} mod 8192: stable={stable} "
                f"signatures={sig}" + (f" cum6={cum}" if cum is not None else "")
            )

    late = [r for r in rows if r["clear"] is None]
    print(f"fail rest >= need within 10 blocks: {len(late)}")
    rows.sort(key=lambda r: (r["clear"] is None, r["clear"] or 99, r["rest"]))
    print("tightest clearance (block index where sum d_j >= 9h1-11):")
    for r in rows[: args.show]:
        d = block_deltas(r["n"], max_blocks=8)[1]
        print(
            f"  k={r['k']:5d} n={r['n']:6d} mod256={r['k'] % 256:3d} "
            f"h1={r['h1']} clear@{r['clear']} rest={r['rest']:4d} need={r['need']:3d} "
            f"d2..6={d[:5]} pairs2..5={r['pairs5']}"
        )

    hist = Counter(r["clear"] for r in rows if r["clear"] is not None)
    print("clearance block histogram:", dict(sorted(hist.items())))


if __name__ == "__main__":
    main()
