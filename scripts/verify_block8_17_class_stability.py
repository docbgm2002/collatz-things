#!/usr/bin/env python3
"""Class-stability falsifier for the Gap SD-K-block-8-17 residue-class rows.

Several statements in ``docs/no-go/avenue_a_comparison_dynamics.md`` assert
that a block signature (Delta_2, ..., Delta_B) on n = 64k + 17 depends only on
k modulo 2^j, and were certified by checking one or a few representatives per
residue class.  This script tests each such claim on many members
k = r + M*s of its class.

Only the low bits of the orbit matter for the first few blocks, so the orbit
is run 2-adically with explicit precision tracking: x1 = (3^(n+1)-1)/8 is
computed modulo 2^P and every division by 2^e consumes e bits.  If a block
would need bits beyond the remaining precision the script raises instead of
guessing.

A row passes when every tested member has the claimed property.  Passing is
finite evidence; one failure refutes the class-level statement.

Exit status is 0 when the refuted rows are exactly ``EXPECTED_REFUTED`` (the
set recorded in Correction SD-K-267-class), so the script doubles as a
regression check.
"""

from __future__ import annotations

import argparse
import sys

PREC = 2048


def v2(value: int) -> int:
    return (value & -value).bit_length() - 1


class PrecisionExhausted(RuntimeError):
    pass


def block_deltas(k: int, blocks: int, prec: int = PREC) -> list[int]:
    """Return [Delta_2, ..., Delta_blocks] for n = 64k + 17, computed 2-adically.

    Mirrors ``_block_deltas_after_first`` in verify_repunit_storage_dominance.py.
    """
    n = 64 * k + 17
    mod = 1 << (prec + 3)
    x = ((pow(3, n + 1, mod) - 1) % mod) >> 3  # x1 mod 2^prec
    p = prec

    def step_odd(x: int, p: int) -> tuple[int, int, int]:
        raw = (3 * x + 1) % (1 << p)
        if raw == 0:
            raise PrecisionExhausted(k)
        e = v2(raw)
        return raw >> e, p - e, e

    def height(x: int, p: int) -> int:
        y = (x + 1) % (1 << p)
        if y == 0:
            raise PrecisionExhausted(k)
        return v2(y)

    # First block: e = 2 by Lemma SD-K-first-e, then collapse rails.
    x, p, e = step_odd(x, p)
    assert e == 2, (k, e)
    while height(x, p) >= 2:
        x, p, _ = step_odd(x, p)

    deltas: list[int] = []
    for _ in range(2, blocks + 1):
        x, p, e = step_odd(x, p)
        hl = height(x, p)
        rails = 0
        while height(x, p) >= 2:
            x, p, _ = step_odd(x, p)
            rails += 1
        heff = 1 + rails if rails < hl - 1 else hl
        deltas.append(11 * (e - 1) - 9 * heff)
    return deltas


# (label, residue r, modulus M, blocks B, claim)
# claim is either a tuple (exact signature) or ("sum>=", 16).
CLAIMS: list[tuple[str, int, int, int, object]] = [
    ("Thm SD-K-block-8-17-3mod256", 3, 256, 4, ("sum>=", 16)),
    ("Thm SD-K-block-8-17-171mod256", 171, 256, 4, ("sum>=", 16)),
    ("Thm SD-K-block-8-17-323mod512", 323, 512, 4, ("sum>=", 16)),
    ("Thm SD-K-block-8-17-579mod1024", 579, 1024, 4, ("sum>=", 16)),
    ("Lemma SD-K-blocks25-267mod512", 267, 512, 5, (2, 2, 2, 2)),
    ("Lemma SD-K-b4start-mod512 (203)", 203, 512, 4, (2, 2, -16)),
    ("Lemma SD-K-b4start-mod8192 (3531)", 3531, 8192, 4, (2, 2, -52)),
    ("Lemma SD-K-b4start-mod8192 (7627)", 7627, 8192, 4, (2, 2, -88)),
    ("Cor SD-K-block5 (523 mod 1024)", 523, 1024, 5, None),
    ("Cor SD-K-block5 (779 mod 1024)", 779, 1024, 5, None),
    ("Cor SD-K-block5 (11 mod 2048)", 11, 2048, 5, None),
    ("Cor SD-K-block5-mod8192-1035 (1035)", 1035, 8192, 5, None),
    ("Cor SD-K-block5-mod8192-1035 (3083)", 3083, 8192, 5, None),
    ("Cor SD-K-block5-mod8192-1035 (5131)", 5131, 8192, 5, None),
    ("Cor SD-K-block5-mod8192-1035 (7179)", 7179, 8192, 5, None),
    ("Thm SD-K-block-8-17-267mod8192 (267)", 267, 8192, 6, ("sum>=", 16)),
    ("Thm SD-K-block-8-17-267mod8192 (1291)", 1291, 8192, 6, ("sum>=", 16)),
    ("Thm SD-K-block-8-17-267mod8192 (4363)", 4363, 8192, 6, ("sum>=", 16)),
    ("Thm SD-K-block-8-17-267mod8192 (5387)", 5387, 8192, 6, ("sum>=", 16)),
    ("Thm SD-K-block-8-17-267mod8192 (6411)", 6411, 8192, 6, ("sum>=", 16)),
    ("Thm SD-K-block-8-17-779mod8192 (779)", 779, 8192, 7, ("sum>=", 16)),
    ("Thm SD-K-block-8-17-779mod8192 (3339)", 3339, 8192, 7, ("sum>=", 16)),
    ("Thm SD-K-block-8-17-779mod8192 (4875)", 4875, 8192, 7, ("sum>=", 16)),
    ("Thm SD-K-block-8-17-779mod8192 (7435)", 7435, 8192, 7, ("sum>=", 16)),
    ("Thm SD-K-block-8-17-3851mod8192", 3851, 8192, 8, ("sum>=", 16)),
]

EXPECTED_REFUTED = {
    "Lemma SD-K-b4start-mod8192 (7627)",
    "Cor SD-K-block5-mod8192-1035 (1035)",
    "Thm SD-K-block-8-17-267mod8192 (267)",
    "Thm SD-K-block-8-17-267mod8192 (4363)",
    "Thm SD-K-block-8-17-779mod8192 (779)",
    "Thm SD-K-block-8-17-779mod8192 (3339)",
    "Thm SD-K-block-8-17-779mod8192 (4875)",
    "Thm SD-K-block-8-17-779mod8192 (7435)",
    "Thm SD-K-block-8-17-3851mod8192",
}

# Delta_5 values asserted by Cor SD-K-block5-mod512-k11slice / -mod8192-1035.
DELTA5 = {
    (523, 1024): -7,
    (779, 1024): 2,
    (11, 2048): -16,
    (1035, 8192): -43,
    (3083, 8192): -25,
    (5131, 8192): -34,
    (7179, 8192): -25,
}


def check(label, r, mod, blocks, claim, members):
    failures = []
    for s in range(members):
        k = r + mod * s
        d = block_deltas(k, blocks)
        if claim is None:
            ok = d[-1] == DELTA5[(r, mod)]
        elif isinstance(claim, tuple) and claim and claim[0] == "sum>=":
            ok = sum(d) >= claim[1]
        else:
            ok = tuple(d) == claim
        if not ok:
            failures.append((k, d))
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--members", type=int, default=256,
                        help="class members k = r + M*s tested per row")
    parser.add_argument("--show", type=int, default=3)
    args = parser.parse_args()

    refuted: set[str] = set()
    for label, r, mod, blocks, claim in CLAIMS:
        failures = check(label, r, mod, blocks, claim, args.members)
        if failures:
            refuted.add(label)
            first = "; ".join(f"k={k} {d}" for k, d in failures[: args.show])
            print(f"REFUTED  {label}: {len(failures)}/{args.members} members fail; {first}")
        else:
            print(f"holds    {label}: all {args.members} members")
    print(f"\n{len(refuted)} of {len(CLAIMS)} class-level rows refuted "
          f"(finite test; a pass is evidence, a failure is a counterexample).")
    if refuted == EXPECTED_REFUTED:
        print("PASS: refuted rows match Correction SD-K-267-class.")
        return 0
    print("FAIL: refuted rows differ from Correction SD-K-267-class.")
    print("  newly refuted:", sorted(refuted - EXPECTED_REFUTED))
    print("  no longer refuted:", sorted(EXPECTED_REFUTED - refuted))
    return 1


if __name__ == "__main__":
    sys.exit(main())
