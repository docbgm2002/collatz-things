#!/usr/bin/env python3
"""
Verification for "The Block-Fracture Identity for the 3x+1 Map".
Every claim is an exact integer identity; this script checks each one,
including the NEGATIVE result (limit 1) that the global longest run is
not bounded. No external dependencies.
"""
import random


def binstr(x):
    return bin(x)[2:] if x else "0"


def maxrun_ones(x):
    runs = [len(r) for r in binstr(x).split("0") if r]
    return max(runs) if runs else 0


def popcount(x):
    return bin(x).count("1")


def v2(x):
    return (x & -x).bit_length() - 1 if x else None


def check_lemma1(max_L=400):
    """3*(2^L - 1) == '10' + '1'*(L-2) + '01' for L >= 2; block weight == L."""
    for L in range(2, max_L + 1):
        val = 3 * (2 ** L - 1)
        predicted = "10" + "1" * (L - 2) + "01"
        assert binstr(val) == predicted, (L, binstr(val), predicted)
        # block weight preserved (interior run L-2 plus two frame ones = L)
        assert popcount(val) == L, (L, popcount(val))
        # interior longest run is exactly L-2
        assert maxrun_ones(val) == max(L - 2, 1) if L > 2 else True
    print(f"Lemma 1 / Corollary 1: PASS for L=2..{max_L} "
          f"(triple identity + weight preserved + run L->L-2)")


def check_lemma2(trials=200_000):
    """Isolated block in arbitrary surroundings: the protected interior
    window inherited from the block contains L-2 ones. The maximal run may
    extend through a boundary. Also verifies the two carry claims
    the proof rests on:
      (b) low term 3*ell+1 < 2^(k+1)  =>  no carry into bit k+2 from below;
      (c) high term lives at bits >= k+L+1  =>  cannot affect interior.
    """
    for _ in range(trials):
        L = random.randint(2, 14)
        k = random.randint(1, 12)
        lo = random.getrandbits(k - 1) if k >= 1 else 0     # bit k-1 == 0
        H = random.getrandbits(8)
        block = (2 ** L - 1) << k
        n = (H << (k + L + 1)) + block + lo                 # bit k+L == 0
        assert (n >> (k + L)) & 1 == 0
        assert k == 0 or (n >> (k - 1)) & 1 == 0

        # claim (b): magnitude bound on the low term (covers full 3n+1)
        assert 3 * lo + 1 < (1 << (k + 1)), (k, lo)
        # claim (b) operationally: no carry out of bit (k+1) region into bit k+2
        low_3B = (3 * block) & ((1 << (k + 2)) - 1)
        low_3l = (3 * lo + 1) & ((1 << (k + 2)) - 1)
        assert (low_3B + low_3l) >> (k + 2) == 0, (k, L, lo)

        # claim (c): interior is independent of H (vary H, interior must not move)
        if L >= 3:
            want = (1 << (L - 2)) - 1
            for Halt in (0, H, H ^ 0xABC, random.getrandbits(10)):
                nn = (Halt << (k + L + 1)) + block + lo
                for m in (3 * nn, 3 * nn + 1):     # both 3n and 3n+1
                    interior = (m >> (k + 2)) & want
                    assert interior == want, (L, k, Halt, bin(m))
    print(f"Lemma 2: PASS over {trials} random isolated-block configs "
          f"(protected L-2 window; low-carry bound (b) and high-term independence (c) verified)")


def check_theorem1(max_L=400):
    """(3 M_L + 1)/2 == 2^L + 2^(L-1) - 1 == '10' 1^(L-1); v2 == 1; run L->L-1."""
    for L in range(2, max_L + 1):
        M = 2 ** L - 1
        val = 3 * M + 1
        assert v2(val) == 1, (L, v2(val))
        img = val >> 1
        assert img == 2 ** L + 2 ** (L - 1) - 1, (L, img)
        assert binstr(img) == "10" + "1" * (L - 1), (L, binstr(img))
        assert maxrun_ones(M) == L and maxrun_ones(img) == L - 1, (L,)
    print(f"Theorem 1: PASS for L=2..{max_L} "
          f"(Mersenne odd-step: v2=1, image 10 1^(L-1), run L->L-1)")


def check_limit1(trials=200_000):
    """NEGATIVE control: the GLOBAL longest run is NOT bounded by old+2."""
    worst = -10 ** 9
    grew_gt2 = 0
    total = 0
    for _ in range(trials):
        n = random.getrandbits(random.randint(4, 80)) | 1   # odd
        if n < 3:
            continue
        d = maxrun_ones(3 * n + 1) - maxrun_ones(n)
        worst = max(worst, d)
        grew_gt2 += (d > 2)
        total += 1
    print(f"Limit 1 (negative control): over {total} random odd n, "
          f"longest-run delta exceeded +2 in {grew_gt2} cases; "
          f"worst delta observed = {worst:+d}")
    assert worst > 2, "expected the global run to grow by more than 2 somewhere"
    print("  -> confirms the global longest-run claim would be FALSE; "
          "the identity is correctly restricted to isolated blocks.")


if __name__ == "__main__":
    random.seed(20251128)
    check_lemma1()
    check_lemma2()
    check_theorem1()
    check_limit1()
    print("\nAll checks passed.")
