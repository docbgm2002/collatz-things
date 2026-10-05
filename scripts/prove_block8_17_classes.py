#!/usr/bin/env python3
"""Exact residue-class prover for the Gap SD-K-block-8-17 block tables.

Setting: n = 64k + 17, x1 = (3^(n+1) - 1)/8, and the block decomposition of
``_block_deltas_after_first`` in verify_repunit_storage_dominance.py
(Delta_j = 11(e_j - 1) - 9 h_j^eff).

Principle (Lemma SD-K-class-determinacy).  The multiplicative order of 3
modulo 2^(P+3) is 2^(P+1), so 3^(64k+18) mod 2^(P+3), and hence x1 mod 2^P,
depends only on 64k mod 2^(P+1), i.e. on k mod 2^(P-5).  Every block step
reads a finite number of low bits: an odd step x -> (3x+1)/2^e with x known
mod 2^p determines e exactly when 3x+1 is nonzero mod 2^p and leaves the new
state known mod 2^(p-e); a height h(x) = v2(x+1) is determined when x+1 is
nonzero mod 2^p.  So if the block computation for the class k = r (mod 2^j)
completes with x1 known only mod 2^(j+5), its output is the same for every
k in the class.  When it does not complete, the class is split into its two
children mod 2^(j+1) and the procedure recurses.

A claim on a class is PROVED when every leaf of this finite tree satisfies
it, and REFUTED when some leaf violates it; the leaf residue r itself is
then an explicit integer counterexample.  If the tree reaches the depth cap
the claim is reported UNDECIDED.  This is an exhaustive computation over
finitely many residue classes, not sampling.
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass, field


def v2(value: int) -> int:
    return (value & -value).bit_length() - 1


class NeedMoreBits(Exception):
    pass


def class_blocks(r: int, j: int, blocks: int,
                 stop_at: int | None = None) -> tuple[int, list[int]]:
    """Return (h1, [Delta_2..Delta_blocks]) valid for every k = r (mod 2^j).

    With ``stop_at``, stop early once the running sum reaches it.  Raises
    NeedMoreBits if the class does not determine the answer.
    """
    p = j + 5
    mod = 1 << (p + 3)
    x = ((pow(3, 64 * r + 18, mod) - 1) % mod) >> 3  # x1 mod 2^p

    def odd_step(x: int, p: int) -> tuple[int, int, int]:
        if p <= 0:
            raise NeedMoreBits
        raw = (3 * x + 1) % (1 << p)
        if raw == 0:
            raise NeedMoreBits
        e = v2(raw)
        return raw >> e, p - e, e

    def height(x: int, p: int) -> int:
        if p <= 0:
            raise NeedMoreBits
        y = (x + 1) % (1 << p)
        if y == 0:
            raise NeedMoreBits
        return v2(y)

    x, p, e = odd_step(x, p)
    if e != 2:
        raise AssertionError(f"first payout e={e} != 2 at k={r} mod 2^{j}")
    h1 = height(x, p)
    while height(x, p) >= 2:
        x, p, _ = odd_step(x, p)

    deltas: list[int] = []
    for _ in range(2, blocks + 1):
        x, p, e = odd_step(x, p)
        hl = height(x, p)
        rails = 0
        while height(x, p) >= 2:
            x, p, _ = odd_step(x, p)
            rails += 1
        heff = 1 + rails if rails < hl - 1 else hl
        deltas.append(11 * (e - 1) - 9 * heff)
        if stop_at is not None and sum(deltas) >= stop_at:
            break
    return h1, deltas


@dataclass
class Result:
    verdict: str  # PROVED / REFUTED / UNDECIDED
    leaves: list[tuple[int, int, int, list[int]]] = field(default_factory=list)
    bad: list[tuple[int, int, int, list[int]]] = field(default_factory=list)
    undecided: list[tuple[int, int]] = field(default_factory=list)


def decide(r: int, j: int, blocks: int, pred, max_j: int) -> Result:
    res = Result("PROVED")
    stack = [(r, j)]
    while stack:
        rr, jj = stack.pop()
        try:
            h1, d = class_blocks(rr, jj, blocks)
        except NeedMoreBits:
            if jj >= max_j:
                res.undecided.append((rr, jj))
                continue
            stack.append((rr + (1 << jj), jj + 1))
            stack.append((rr, jj + 1))
            continue
        leaf = (rr, jj, h1, d)
        res.leaves.append(leaf)
        if not pred(h1, d):
            res.bad.append(leaf)
    if res.bad:
        res.verdict = "REFUTED"
    elif res.undecided:
        res.verdict = "UNDECIDED"
    return res


def sig(*expected):
    """Delta_2.. prefix equality; None is a wildcard."""
    def pred(h1, d):
        return all(x is None or x == y for x, y in zip(expected, d))
    pred.blocks = len(expected) + 1
    return pred


def total_at_least(blocks: int, need: int):
    def pred(h1, d):
        return sum(d) >= need
    pred.blocks = blocks
    return pred


def h1_is(value: int):
    def pred(h1, d):
        return h1 == value
    pred.blocks = 1
    return pred


def lg(m: int) -> int:
    assert m & (m - 1) == 0
    return m.bit_length() - 1


# (label, residue, modulus, predicate).  Labels follow
# docs/no-go/avenue_a_comparison_dynamics.md.
B6 = {267: 35, 779: 2, 1291: 13, 1803: -16, 2315: -12, 2827: 2, 3339: 4,
      3851: -7, 4363: 46, 4875: 2, 5387: 13, 5899: -34, 6411: 24, 6923: 2,
      7435: -5, 7947: -7}
B7 = {267: 13, 779: 13, 1291: -7, 1803: 13, 2315: 4, 2827: 2, 3339: 15,
      3851: 2, 4363: -7, 4875: 46, 5387: 13, 5899: 2, 6411: -25, 6923: -34,
      7435: 24, 7947: 13}

CLAIMS = [
    ("Lemma SD-K-h1-parity (k odd: h1=3)", 1, 2, h1_is(3)),
    ("Lemma SD-K-h1-parity (k=2 mod 4: h1=4)", 2, 4, h1_is(4)),
    ("Lemma SD-K-h2-3mod8", 3, 8, sig(2)),
    ("Lemma SD-K-e3-stable (3 mod 64)", 3, 64, sig(2, 13)),
    ("Lemma SD-K-e3-stable (11 mod 64)", 11, 64, sig(2, 2)),
    ("Lemma SD-K-e3-stable (43 mod 64)", 43, 64, sig(2, 2)),
    ("Lemma SD-K-e3-stable (59 mod 64)", 59, 64, sig(2, -7)),
    ("Lemma SD-K-e4-3mod256", 3, 256, sig(2, 13, 2)),
    ("Lemma SD-K-e4-171mod256", 171, 256, sig(2, 2, 13)),
    ("Lemma SD-K-e4-67family (323 mod 512)", 323, 512, sig(2, 13, 13)),
    ("Lemma SD-K-e4-67family (579 mod 1024)", 579, 1024, sig(2, 13, 4)),
    ("Thm SD-K-block-8-17-3mod256", 3, 256, total_at_least(4, 16)),
    ("Thm SD-K-block-8-17-171mod256", 171, 256, total_at_least(4, 16)),
    ("Thm SD-K-block-8-17-323mod512", 323, 512, total_at_least(4, 16)),
    ("Thm SD-K-block-8-17-579mod1024", 579, 1024, total_at_least(4, 16)),
    ("Lemma SD-K-b4start-mod256 (11)", 11, 256, sig(2, 2, 2)),
    ("Lemma SD-K-b4start-mod256 (75)", 75, 256, sig(2, 2, -7)),
    ("Lemma SD-K-b4start-mod256 (139)", 139, 256, sig(2, 2, 2)),
    ("Lemma SD-K-b4start-mod512 (203)", 203, 512, sig(2, 2, -16)),
    ("Lemma SD-K-b4start-mod512 (459 mod 2048: -34)", 459, 2048, sig(2, 2, -34)),
    ("Lemma SD-K-b4start-mod8192 (3531)", 3531, 8192, sig(2, 2, -52)),
    ("Lemma SD-K-b4start-mod8192 (7627)", 7627, 8192, sig(2, 2, -88)),
    ("Lemma SD-K-blocks25-267mod512", 267, 512, sig(2, 2, 2, 2)),
    ("Cor SD-K-block5 (523 mod 1024)", 523, 1024, sig(2, 2, 2, -7)),
    ("Cor SD-K-block5 (779 mod 1024)", 779, 1024, sig(2, 2, 2, 2)),
    ("Cor SD-K-block5 (11 mod 2048)", 11, 2048, sig(2, 2, 2, -16)),
    ("Cor SD-K-block5-mod8192-1035 (1035)", 1035, 8192, sig(2, 2, 2, -43)),
    ("Cor SD-K-block5-mod8192-1035 (3083)", 3083, 8192, sig(2, 2, 2, -25)),
    ("Cor SD-K-block5-mod8192-1035 (5131)", 5131, 8192, sig(2, 2, 2, -34)),
    ("Cor SD-K-block5-mod8192-1035 (7179)", 7179, 8192, sig(2, 2, 2, -25)),
]
for r, d6 in B6.items():
    CLAIMS.append((f"Cor SD-K-block6-mod8192 ({r})", r, 8192, sig(2, 2, 2, 2, d6)))
for r, d7 in B7.items():
    CLAIMS.append((f"Cor SD-K-block7-mod8192 ({r})", r, 8192,
                   sig(2, 2, 2, 2, B6[r], d7)))
for r in (267, 1291, 4363, 5387, 6411):
    CLAIMS.append((f"Thm SD-K-block-8-17-267mod8192 ({r})", r, 8192,
                   total_at_least(6, 16)))
for r in (779, 3339, 4875, 7435):
    CLAIMS.append((f"Thm SD-K-block-8-17-779mod8192 ({r})", r, 8192,
                   total_at_least(7, 16)))
CLAIMS.append(("Thm SD-K-block-8-17-3851mod8192", 3851, 8192,
               total_at_least(8, 16)))


def closure_density(blocks: int, max_j: int) -> tuple[float, float, float]:
    """Exact Haar measure, among odd k (h1 = 3, need 16), of classes whose
    running sum Delta_2 + ... reaches 16 within ``blocks`` blocks (closed),
    provably does not (open), or is undetermined at depth max_j."""
    closed = opened = undec = 0.0
    stack = [(1, 1)]
    while stack:
        r, j = stack.pop()
        try:
            _, d = class_blocks(r, j, blocks, stop_at=16)
        except NeedMoreBits:
            if j >= max_j:
                undec += 2.0 ** -(j - 1)
            else:
                stack += [(r, j + 1), (r + (1 << j), j + 1)]
            continue
        if sum(d) >= 16:
            closed += 2.0 ** -(j - 1)
        else:
            opened += 2.0 ** -(j - 1)
    return closed, opened, undec


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--max-bits", type=int, default=40,
                        help="depth cap: largest j in k mod 2^j explored")
    parser.add_argument("--show", type=int, default=2)
    parser.add_argument("--density", type=int, default=0, metavar="B",
                        help="also report odd-k closure measure for blocks 2..B")
    parser.add_argument("--density-bits", type=int, default=20,
                        help="depth cap for --density")
    args = parser.parse_args()

    counts = {"PROVED": 0, "REFUTED": 0, "UNDECIDED": 0}
    for label, r, mod, pred in CLAIMS:
        res = decide(r, lg(mod), pred.blocks, pred, args.max_bits)
        counts[res.verdict] += 1
        depth = max((lf[1] for lf in res.leaves), default=lg(mod))
        line = (f"{res.verdict:9s} {label}: {len(res.leaves)} leaf classes, "
                f"deepest k mod 2^{depth}")
        if res.bad:
            ex = "; ".join(f"k={b[0]} (mod 2^{b[1]}) h1={b[2]} {b[3]}"
                           for b in sorted(res.bad)[: args.show])
            bad_measure = sum(2.0 ** -(b[1] - lg(mod)) for b in res.bad)
            line += f"\n          failing share of class {bad_measure:.4g}; e.g. {ex}"
        if res.undecided:
            line += f"\n          {len(res.undecided)} classes undecided at depth cap"
        print(line)
    print(f"\nPROVED {counts['PROVED']}, REFUTED {counts['REFUTED']}, "
          f"UNDECIDED {counts['UNDECIDED']} of {len(CLAIMS)} class claims.")

    if args.density:
        for b in range(2, args.density + 1):
            c, o, u = closure_density(b, args.density_bits)
            print(f"odd k, blocks 2..{b}: closed {c:.6f}, open {o:.6f}, "
                  f"undetermined {u:.2e}")
    return 0 if counts["UNDECIDED"] == 0 else 2


if __name__ == "__main__":
    sys.exit(main())
