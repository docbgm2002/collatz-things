"""Extended Mersenne-spike recovery scan.

Companion to `binary_fuel_bad_block_notes.md` (Section 3, "High-recharge
spike family"). For R == 5 (mod 6) the cheap bad block (2,1,R) recharges
directly to the Mersenne spine:

    x_0 = 4 * (2^{R+1} - 1) / 9 - 1   ->   x_1 = 2^R - 1.

The candidate spike-recovery lemma is that descent below x_0 first occurs
exactly when the cumulative fuel-block surplus first becomes nonnegative.

This script tests that coincidence on exact integer orbits (floats used only
for the surplus diagnostic). Reproduce:

    python explore_spike_recovery.py
"""
import math

L23 = math.log2(3) - 1.0  # log2(3/2)


def v2(n):
    r = 0
    while n % 2 == 0:
        n //= 2
        r += 1
    return r


def block(x):
    """One fuel block on odd x = 2^t u - 1:  x+ = (3^t u - 1) / 2^a."""
    t = v2(x + 1)
    u = (x + 1) >> t
    num = 3 ** t * u - 1
    a = v2(num)
    return num >> a, t, a


def scan(R, cap=200000):
    x0 = 4 * ((2 ** (R + 1) - 1) // 9) - 1
    assert (x0 + 1) % 4 == 0
    x = x0
    S = 0.0
    first_desc = None
    first_nonneg = None
    k = 0
    while k < cap:
        xp, t, a = block(x)
        k += 1
        S += a - t * L23
        if first_nonneg is None and S >= 0:
            first_nonneg = k
        if x < x0 and first_desc is None:
            first_desc = k - 1
        if xp < x0:
            first_desc = k
            break
        x = xp
    return first_desc, first_nonneg, k


def main(r_hi=999):
    print(" R    first_descent  first_nonneg_surplus  match?")
    worst = 0
    mism = 0
    tested = 0
    for R in range(5, r_hi + 1, 6):  # R == 5 (mod 6)
        fd, fn, k = scan(R)
        tested += 1
        ok = (fd == fn)
        if not ok:
            mism += 1
        worst = max(worst, fd or 0)
        if R <= 59 or not ok:
            print(f"{R:4d}   {fd}             {fn}                {ok}")
    print(f"\ntested R in 5..{r_hi} (R=5 mod 6): {tested} values")
    print(f"mismatches (first-descent != first-nonneg-surplus): {mism}")
    print(f"worst recovery length (blocks): {worst}")


if __name__ == "__main__":
    main()
