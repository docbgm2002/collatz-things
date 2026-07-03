"""Numeric box of the {A,B,C} fuel-motif inverse IFS attractor.

Companion to `binary_fuel_bad_block_notes.md` (Section 3). The cheap
near-threshold motifs

    A = (2,1,2),  B = (2,1,3)(3,1,2),  C = (2,1,4)(4,1,2)

act affinely on the odd part u. Their inverse maps are real contractions
with negative offsets, so every infinite backward word converges to a
negative real ghost. This script boxes that attractor numerically and
reports the (weak) contraction constant.

Diagnostic only; uses floats. Reproduce:

    python explore_fuel_motif_attractor.py
"""
import random

# Forward affine actions on the odd part u.
fwd = {'A': (9 / 8, 1 / 8), 'B': (243 / 128, 43 / 128), 'C': (729 / 256, 113 / 256)}
# Inverse maps (contractions): u -> (1/m) u - b/m.
inv = {k: (1 / m, -b / m) for k, (m, b) in fwd.items()}


def main():
    print("inverse-map slopes (contraction ratios) and fixed points:")
    for k, (m, b) in inv.items():
        print(f"  {k}^-1: slope={m:.4f}  fixed point u*={b/(1-m):+.6f}")
    maxslope = max(m for m, _ in inv.values())
    print(f"max contraction ratio = {maxslope:.4f}")

    random.seed(0)
    keys = list(inv.keys())
    pts = []
    for _ in range(300000):
        u = 0.0
        for _ in range(80):
            m, b = inv[random.choice(keys)]
            u = m * u + b
        pts.append(u)
    lo, hi = min(pts), max(pts)
    print(f"\nattractor numeric box: [{lo:+.6f}, {hi:+.6f}]")
    print(f"bounded away from 0 by eps = {min(abs(lo), abs(hi)):.6f}; "
          f"all negative: {hi < 0}")
    for N in (10, 20, 40, 80):
        print(f"  N={N:3d}: maxslope^N = {maxslope**N:.3e}")


if __name__ == "__main__":
    main()
