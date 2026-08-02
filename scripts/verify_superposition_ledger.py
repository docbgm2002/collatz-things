#!/usr/bin/env python3
"""Additive superposition and the interaction ledger (W1).

Exact integer / rational arithmetic throughout.

W1 asks whether descent certificates for the parts of a decomposition
n = a + b can be combined into one for n.  The entire content lives in the
interaction ledger

    I_T(a,b) = C^(T)(a+b) - C^(T)(a) - C^(T)(b).

A. Deliverable (ii): the exact expansion.  On the cylinders of the three
   parity words u = w(n), w = w(a), v = w(b),

       C^(T)(x) = lam_word * x + rho_word,   lam_word = 6^{o} / 2^T,

   so

       I_T(a,b) = (lam_u - lam_w) a + (lam_u - lam_v) b
                  + (rho_u - rho_w - rho_v).

B. Deliverable (i): W1.a, in two forms.
   W1.a-1  For odd n, a and b have opposite parity, so w(a) and w(b) differ
           in the FIRST letter.  The closed-form regime "all three words
           agree" is empty from step 1, for every decomposition.
   W1.a-2  The one regime where superposition is exact, n = a + 2^N t with
           N >= E_K(a)+1, is the repo's cylinder/affine identity; the part
           b = 2^N t never has its own trajectory used.  It is a VIRTUAL
           part, void under barrier 4 and under this file's own global kill
           rule for W1/W8.

C. Deliverable (iii): the census.  Over every two-part decomposition, the
   normalised interaction max_T |I_T| / scale_T is bounded below.

D. The n = 471 testbed: Mersenne / tower part plus remainder.

Run:
    python3 scripts/verify_superposition_ledger.py
    python3 scripts/verify_superposition_ledger.py --nmax 501
"""

from __future__ import annotations

import argparse
from fractions import Fraction

FAILURES: list[str] = []


def check(label: str, ok: bool) -> None:
    if not ok:
        FAILURES.append(label)
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")


def collatz(x: int) -> int:
    return x // 2 if x % 2 == 0 else 3 * x + 1


def orbit(x: int, T: int) -> list[int]:
    out = [x]
    for _ in range(T):
        x = collatz(x)
        out.append(x)
    return out


def parity_word(x: int, T: int) -> tuple[int, ...]:
    w = []
    for _ in range(T):
        w.append(x % 2)
        x = collatz(x)
    return tuple(w)


def lam_rho(word: tuple[int, ...]) -> tuple[Fraction, Fraction]:
    """C^(T)(x) = lam*x + rho on the cylinder of `word`."""
    T = len(word)
    lam = Fraction(6 ** sum(word), 1 << T)
    rho = Fraction(0)
    for i, wi in enumerate(word):
        if not wi:
            continue
        tail = word[i + 1:]
        rho += Fraction(6 ** sum(tail), 1 << (T - 1 - i))
    return lam, rho


# ---------------------------------------------------------------------------
# A. the exact expansion
# ---------------------------------------------------------------------------

def part_a() -> None:
    print("\n== A. deliverable (ii): the exact expansion of I_T ==")
    print("  C^(T)(x) = lam_w x + rho_w on the cylinder of w, lam_w = 6^{o_w}/2^T")
    ok_affine = True
    ok_exp = True
    for x in range(1, 400):
        for T in range(1, 14):
            w = parity_word(x, T)
            lam, rho = lam_rho(w)
            if lam * x + rho != orbit(x, T)[-1]:
                ok_affine = False
    check("C^(T)(x) = lam_{w(x)} x + rho_{w(x)}, exactly, for x < 400, T <= 13",
          ok_affine)

    rows = []
    for n in range(3, 300, 2):
        for a in range(1, n):
            b = n - a
            for T in (1, 3, 5, 8, 11):
                u = parity_word(n, T)
                w = parity_word(a, T)
                v = parity_word(b, T)
                lu, ru = lam_rho(u)
                lw, rw = lam_rho(w)
                lv, rv = lam_rho(v)
                lhs = orbit(n, T)[-1] - orbit(a, T)[-1] - orbit(b, T)[-1]
                rhs = (lu - lw) * a + (lu - lv) * b + (ru - rw - rv)
                if Fraction(lhs) != rhs:
                    ok_exp = False
                    rows.append((n, a, T, lhs, rhs))
    check("I_T(a,b) = (lam_u-lam_w)a + (lam_u-lam_v)b + (rho_u-rho_w-rho_v)",
          ok_exp)
    if rows:
        print(f"    first mismatch: {rows[0]}")

    print("\n  Two structural corollaries of the expansion:")
    print("   * if u = w = v then I_T = -rho_u exactly: the interaction ledger")
    print("     IS the raw correction ledger, with no new information;")
    print("   * lam = 6^o/2^T, so o_u != o_w forces")
    print("     |lam_u - lam_w| >= (5/6) max(lam_u, lam_w):")
    print("     once the words diverge the coefficients are of full size.")
    ok = True
    for ou in range(0, 12):
        for ow in range(0, 12):
            if ou == ow:
                continue
            hi = max(6 ** ou, 6 ** ow)
            if Fraction(abs(6 ** ou - 6 ** ow), hi) < Fraction(5, 6):
                ok = False
    check("o_u != o_w implies |lam_u - lam_w| >= (5/6) max(lam_u, lam_w)", ok)

    # How large is the agreeing regime, really?
    print("\n  How large is the agreeing regime u = w = v?")
    agree = []
    nontrivial = []
    for a in range(1, 200):
        for b in range(a, 200):
            for T in range(1, 9):
                if (parity_word(a + b, T) == parity_word(a, T)
                        == parity_word(b, T)):
                    agree.append((a, b, T))
                    if lam_rho(parity_word(a, T))[1] != 0:
                        nontrivial.append((a, b, T))
    print(f"   triples (a,b,T) with a,b < 200, T <= 8 and u = w = v: "
          f"{len(agree)}")
    print(f"   of those, with rho_u != 0 (i.e. I_T != 0): {len(nontrivial)}")
    check("every agreeing triple has rho_u = 0, i.e. the word is all-zeros "
          "and I_T = 0 trivially: the closed-form regime carries no content",
          not nontrivial)


# ---------------------------------------------------------------------------
# B. W1.a
# ---------------------------------------------------------------------------

def part_b(nmax: int) -> None:
    print("\n== B. deliverable (i): W1.a ==")
    print("  W1.a-1  For odd n = a + b with a,b >= 1, exactly one of a,b is")
    print("  odd, so w(a) and w(b) differ in the first letter.")
    ok = True
    for n in range(3, min(nmax, 2001), 2):
        for a in range(1, n):
            if (a % 2) == ((n - a) % 2):
                ok = False
    check("for every odd n and every decomposition, a and b have opposite "
          "parity: the all-agree regime is EMPTY at T = 1", ok)
    print("  Hence I_T never lies in the closed-form regime, for any T >= 1,")
    print("  for any two-part decomposition of an odd number.")

    print("\n  W1.a-2  The one exact regime is the cylinder/affine identity.")
    # accelerated map, repo notation
    def v2(y: int) -> int:
        return (y & -y).bit_length() - 1

    def f_odd(y: int) -> int:
        z = 3 * y + 1
        return z >> v2(z)

    ok = True
    tested = 0
    for a in range(1, 4000, 2):
        E = 0
        x = a
        for K in range(1, 9):
            e = v2(3 * x + 1)
            E += e
            x = f_odd(x)
            N = E + 1
            for t in (1, 2, 3, 7):
                n = a + (t << N)
                # itineraries agree for K steps, and:
                y = n
                Ey = 0
                good = True
                for _ in range(K):
                    ey = v2(3 * y + 1)
                    Ey += ey
                    y = f_odd(y)
                if Ey != E:
                    good = False
                if good and y != x + 3 ** K * (t << (N - E)):
                    ok = False
                if not good:
                    ok = False
                tested += 1
    check(f"cylinder identity x_K(a + 2^N t) = x_K(a) + 3^K 2^{{N-E_K}} t "
          f"for N = E_K+1 ({tested} cases)", ok)
    print("  In this identity the part b = 2^N t never has its own trajectory")
    print("  computed or used -- only its residue.  It is a VIRTUAL part.")
    print("  The file's own global kill rule: 'any W1/W8 statement whose")
    print("  parts do not each carry an actual computed trajectory is void")
    print("  (barrier 4)'.  So the exact regime is void, and the non-void")
    print("  regime (B, first half) never has agreeing words.  PINCER.")


# ---------------------------------------------------------------------------
# C. the census
# ---------------------------------------------------------------------------

def sigma_c(n: int, cap: int = 400) -> int:
    """First T >= 1 with C^(T)(n) < n (raw Collatz)."""
    x = n
    for T in range(1, cap + 1):
        x = collatz(x)
        if x < n:
            return T
    return cap


def rho_at(n: int, T: int) -> Fraction:
    """The raw correction ledger of n's own trajectory at time T."""
    _lam, rho = lam_rho(parity_word(n, T))
    return rho


def census_one(n: int, T: int) -> tuple[Fraction, int, float]:
    """min over decompositions of max_T |I_T| / rho_T, the minimising a, and
    the peak trajectory-relative size of the same decomposition.

    The kill criterion asks whether any decomposition makes the interaction
    ledger grow more slowly than the RAW correction ledger rho_T of n's own
    trajectory.  A ratio >= 1 means it does not.
    """
    on = orbit(n, T)
    rhos = [rho_at(n, t) for t in range(1, T + 1)]
    best = None
    best_a = 0
    best_scale = 0.0
    for a in range(1, n // 2 + 1):
        b = n - a
        oa = orbit(a, T)
        ob = orbit(b, T)
        worst = Fraction(0)
        worst_scale = 0.0
        for t in range(1, T + 1):
            I = on[t] - oa[t] - ob[t]
            r = rhos[t - 1]
            if r == 0:
                continue
            worst = max(worst, Fraction(abs(I)) / r)
            worst_scale = max(worst_scale,
                              abs(I) / max(on[t], oa[t], ob[t]))
        if best is None or worst < best:
            best = worst
            best_a = a
            best_scale = worst_scale
    return best, best_a, best_scale


def part_c(nmax: int) -> None:
    print("\n== C. deliverable (iii): the census over all decompositions ==")
    print("  Family: every n = a + b with 1 <= a <= n/2, both parts positive")
    print("  integers (all of which reach 1, by FIN1).  The kill criterion")
    print("  asks whether the interaction ledger can grow more slowly than the")
    print("  RAW correction ledger rho_T of n's own trajectory, so the")
    print("  statistic is")
    print("      M(a,b) = max_{1<=T<=H} |I_T| / rho_T ,")
    print("  minimised over the decomposition.  M >= 1 means no gain.")
    print("\n   n      min_a M(a,b)     at a     also |I|/traj   horizon H")
    ok = True
    worst_min = None
    min_traj = 1.0
    pow2_best = 0
    sample = [n for n in range(3, min(nmax, 501) + 1, 2)]
    shown = {3, 5, 7, 27, 31, 71, 101, 251, 351, 471, 501}
    for n in sample:
        H = max(sigma_c(n), 20)
        m, a, sc = census_one(n, H)
        if worst_min is None or m < worst_min:
            worst_min = m
        min_traj = min(min_traj, sc)
        if a & (a - 1) == 0:
            pow2_best += 1
        if m < 1:
            ok = False
            print(f"    BELOW 1 at n={n}, a={a}: M={float(m):.4f}")
        if n in shown:
            print(f"   {n:<6d} {float(m):<16.4f} {a:<8d} {sc:<15.4f} {H}")
    print(f"\n  minimum over all odd n <= {min(nmax, 501)} of min_a M(a,b) "
          f"= {float(worst_min):.4f}")
    print(f"  minimum over the same range of the trajectory-relative size "
          f"= {min_traj:.4f}")
    print(f"  best decomposition had a a power of two in {pow2_best} of "
          f"{len(sample)} cases")
    check("no two-part decomposition brings the interaction ledger below the "
          "raw correction ledger: min_a max_T |I_T|/rho_T >= 1 for every "
          "tested n", ok)
    check("at the best decomposition the interaction is still at least half "
          "the trajectory: |I_T|/traj >= 0.5, as the expansion predicts",
          min_traj >= 0.5)
    print("  So I_T is not a smaller object than the ledger it was meant to")
    print("  replace.  By the expansion in A it is the trajectory itself.")


# ---------------------------------------------------------------------------
# D. the n = 471 testbed
# ---------------------------------------------------------------------------

def part_d() -> None:
    print("\n== D. the n = 471 testbed: Mersenne/tower part + remainder ==")

    def v2(y: int) -> int:
        return (y & -y).bit_length() - 1

    def f_odd(y: int) -> int:
        z = 3 * y + 1
        return z >> v2(z)

    a471 = (3 ** 471 - 1) // 2
    Tthr = (1 << 471) - 1
    states = []
    x = a471
    while x >= Tthr and len(states) < 12:
        states.append(x)
        x = f_odd(x)
    print(f"  first {len(states)} pre-descent states of a_471 "
          f"({a471.bit_length()} bits)")
    H = 24
    print(f"\n   state #  decomposition          max_T |I_T|/rho_T   "
          f"max_T |I_T|/traj   (H={H})")
    ok = True
    for idx, s in enumerate(states[:6]):
        k = s.bit_length()
        cands = [("Mersenne 2^(k-1)-1", (1 << (k - 1)) - 1),
                 ("Mersenne 2^(k-1)   ", 1 << (k - 1))]
        for label, A in cands:
            if A >= s or A < 1:
                continue
            B = s - A
            if B < 1:
                continue
            os_, oa, ob = orbit(s, H), orbit(A, H), orbit(B, H)
            rhos = [rho_at(s, t) for t in range(1, H + 1)]
            wr = Fraction(0)
            wt = 0.0
            for t in range(1, H + 1):
                I = os_[t] - oa[t] - ob[t]
                if rhos[t - 1] != 0:
                    wr = max(wr, Fraction(abs(I)) / rhos[t - 1])
                wt = max(wt, abs(I) / max(os_[t], oa[t], ob[t]))
            if idx < 3:
                print(f"   {idx:<8d} {label:<22s} {float(wr):<19.3e} "
                      f"{wt:.4f}")
            if wr < 1:
                ok = False
    check("on a_471's pre-descent states, the Mersenne-plus-remainder "
          "decomposition also has interaction far above the raw ledger "
          "(no sub-ledger growth)", ok)
    print("  So the n = 471 clause of the kill criterion fires: no tested")
    print("  decomposition of a_471's pre-descent states admits sub-ledger")
    print("  interaction growth.  CLOSE THE AVENUE.")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--nmax", type=int, default=501)
    args = ap.parse_args()
    print("== W1: additive superposition and the interaction ledger ==")
    part_a()
    part_b(args.nmax)
    part_c(args.nmax)
    part_d()
    print()
    if FAILURES:
        print(f"FAILURES ({len(FAILURES)}):")
        for f in FAILURES:
            print(f"  - {f}")
        raise SystemExit(1)
    print("SUPERPOSITION-LEDGER: PASS")


if __name__ == "__main__":
    main()
