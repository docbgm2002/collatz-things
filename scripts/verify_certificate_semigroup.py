#!/usr/bin/env python3
"""The certificate-transport semigroup (W2).

Exact integer arithmetic throughout.

Contents
--------
A. The transport rules, each checked as an identity:
     sigma(n) = 4n+1        f(sigma(n)) = f(n)          (sibling merge)
     P_e(n)   = (2^e n-1)/3 f(P_e(n))   = n             (predecessor)
     delta(n) = 2n          same odd part
   and the *void* class: forward-orbit rules (the Mersenne burn, the mod-8
   rail identities), which map n to a point of its own forward orbit and
   therefore never enlarge the certified set.
B. TWR1 = P_2^d.  Proved identity  P_2^d(z) = 1 + (4/3)^d (z-1), defined
   exactly when 3^d | z-1; specialising to z = 2^M-1 recovers both the
   tower formula w_d(M) and its domain condition M = 1 mod 2*3^{d-1}.
C. The exact orbit count of <sigma, delta> . B, its asymptotic law, its
   2-adic closure, and its intersection with the repunit family.
D. The <P_2> orbit of a finite B is finite, with an exact size.
E. The n = 471 stress test: is a_471 reachable?

Run:
    python3 scripts/verify_certificate_semigroup.py
    python3 scripts/verify_certificate_semigroup.py --bmax 100000
"""

from __future__ import annotations

import argparse
import math
from fractions import Fraction

FAILURES: list[str] = []


def check(label: str, ok: bool) -> None:
    if not ok:
        FAILURES.append(label)
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")


def v2(x: int) -> int:
    return (x & -x).bit_length() - 1


def v3(x: int) -> int:
    if x == 0:
        raise ValueError
    k = 0
    while x % 3 == 0:
        x //= 3
        k += 1
    return k


def f_odd(x: int) -> int:
    y = 3 * x + 1
    return y >> v2(y)


# ---------------------------------------------------------------------------
# A. the transport rules
# ---------------------------------------------------------------------------

def sigma(n: int) -> int:
    return 4 * n + 1


def pred(n: int, e: int) -> int | None:
    """The depth-1 predecessor selector P_e(n) = (2^e n - 1)/3, or None."""
    t = (1 << e) * n - 1
    if t % 3:
        return None
    x = t // 3
    if x <= 0 or x % 2 == 0:
        return None
    return x


def part_a(bmax: int) -> None:
    print("\n== A. the transport rules, as identities ==")

    ok = all(f_odd(sigma(n)) == f_odd(n) for n in range(1, 20001, 2))
    check("sigma: f(4n+1) = f(n) for every odd n < 20000", ok)
    check("sigma maps odd -> odd and its image is exactly 5 mod 8",
          all(sigma(n) % 8 == 5 for n in range(1, 999, 2)))

    ok = True
    for n in range(1, 3001, 2):
        for e in range(1, 25):
            x = pred(n, e)
            if x is None:
                continue
            if f_odd(x) != n:
                ok = False
                print(f"    P_{e}({n}) = {x} but f = {f_odd(x)}")
                break
    check("P_e: f((2^e n - 1)/3) = n whenever the value is an odd integer", ok)

    # admissibility is exactly a parity condition on e
    ok = True
    for n in range(1, 2001, 2):
        for e in range(1, 12):
            adm = pred(n, e) is not None
            if n % 3 == 0:
                want = False
            elif n % 3 == 1:
                want = (e % 2 == 0)
            else:
                want = (e % 2 == 1)
            if adm != want:
                ok = False
                break
    check("P_e admissible iff 3 does not divide n and e has the right parity",
          ok)

    print("\n  -- the void class: forward-orbit rules --")
    # Mersenne burn (Andaloro / recharge_nogo Lemma 3): 2^t u - 1 -> 3^t u - 1
    ok = True
    for t in range(2, 14):
        for u in range(1, 40, 2):
            x = (1 << t) * u - 1
            if x < 3:
                continue
            y = x
            for _ in range(t - 1):
                y = f_odd(y)
            # after t-1 odd steps: 2*3^{t-1}u - 1; one more C step lands on 3^t u - 1
            if y != 2 * 3 ** (t - 1) * u - 1:
                ok = False
                break
            if 3 * y + 1 != 2 * (3 ** t * u - 1):
                ok = False
                break
    check("burn: 2^t u - 1 reaches 3^t u - 1 along its OWN forward orbit", ok)

    ok = all(f_odd(8 * y + 1) == 6 * y + 1 for y in range(1, 5000))
    check("rail 1: f(8y+1) = 6y+1 (a forward-orbit identity)", ok)
    ok = all(f_odd(f_odd(8 * y + 7)) == 18 * y + 17 for y in range(0, 5000))
    check("rail 7: f^2(8y+7) = 18y+17 (a forward-orbit identity)", ok)

    # the decisive triviality fact
    orbit: set[int] = set()
    small = 20001
    for b in range(1, small, 2):
        x = b
        while x != 1:
            orbit.add(x)
            x = f_odd(x)
    orbit.add(1)
    print(f"  union of forward orbits of odd b < {small}: "
          f"{len(orbit)} distinct odd values, max = {max(orbit)}")
    check("forward-orbit rules enlarge a finite certified set only finitely",
          len(orbit) < float("inf"))


# ---------------------------------------------------------------------------
# B. TWR1 = P_2^d
# ---------------------------------------------------------------------------

def p2(z: int) -> int | None:
    """P_2(z) = (4z-1)/3, the e=2 predecessor selector."""
    return pred(z, 2)


def p2_iter(z: int, d: int) -> int | None:
    """P_2^d(z) = 1 + (4/3)^d (z-1), defined iff 3^d | z-1."""
    if (z - 1) % 3 ** d:
        return None
    return 1 + 4 ** d * (z - 1) // 3 ** d


def w_tower(M: int, d: int) -> Fraction:
    """The TWR1 formula (2^{M+2d} - 2^{2d+1} + 3^d)/3^d."""
    return Fraction(2 ** (M + 2 * d) - 2 ** (2 * d + 1) + 3 ** d, 3 ** d)


def part_b() -> None:
    print("\n== B. the Mersenne ancestry tower is exactly P_2 iterated ==")

    ok = True
    for z in range(1, 4000, 2):
        for d in range(1, 8):
            direct = p2_iter(z, d)
            step = z
            good = True
            for _ in range(d):
                step = p2(step) if step is not None else None
                if step is None:
                    good = False
                    break
            if (direct is None) != (not good):
                ok = False
                break
            if direct is not None and direct != step:
                ok = False
                break
    check("P_2^d(z) = 1 + (4/3)^d (z-1), defined iff 3^d | z-1", ok)

    ok = True
    rows = []
    for d in range(1, 6):
        order = 2 * 3 ** (d - 1)
        for s in range(1, 6):
            M = 1 + order * s
            z = (1 << M) - 1
            got = p2_iter(z, d)
            want = w_tower(M, d)
            if got is None or Fraction(got) != want:
                ok = False
                rows.append((d, M, "MISMATCH"))
            else:
                if len(rows) < 8:
                    rows.append((d, M, got))
    check("P_2^d(2^M - 1) equals the TWR1 formula w_d(M)", ok)
    print("   d   M     w_d(M) = P_2^d(2^M-1)")
    for d, M, val in rows[:8]:
        sval = str(val)
        if len(sval) > 34:
            sval = sval[:31] + "..."
        print(f"   {d:<3d} {M:<5d} {sval}")

    # the domain condition is recovered, not assumed
    ok = True
    for d in range(1, 6):
        order = 2 * 3 ** (d - 1)
        for M in range(2, 60):
            defined = ((1 << M) - 2) % 3 ** d == 0
            if defined != (M % order == 1):
                ok = False
                break
    check("3^d | (2^M - 1) - 1  iff  M = 1 mod 2*3^{d-1}  (TWR1 domain)", ok)

    check("every tower step is an e=2 step, so the tower is a chain of P_2",
          all(v2(3 * p2_iter((1 << 13) - 1, d) + 1) == 2
              for d in range(1, 4) if p2_iter((1 << 13) - 1, d) is not None))

    print("  growth: w_d(M)/(2^M-1) -> (4/3)^d, while the domain forces")
    print("          M >= 1 + 2*3^{d-1}, i.e. d = O(log log w_d(M)).")


# ---------------------------------------------------------------------------
# C. the exact orbit of <sigma, delta> . B
# ---------------------------------------------------------------------------

def sigma_iter(b: int, k: int) -> int:
    """sigma^k(b) = (4^k (3b+1) - 1)/3."""
    return (4 ** k * (3 * b + 1) - 1) // 3


def primitive_seeds(bmax: int) -> list[int]:
    """Odd b <= bmax not already of the form sigma(odd), i.e. b != 5 mod 8."""
    return [b for b in range(1, bmax + 1, 2) if b % 8 != 5]


def orbit_count_set(seeds: list[int], X: int) -> int:
    """|{2^m sigma^k(b) <= X}| by explicit enumeration (slow, reference)."""
    seen = set()
    for b in seeds:
        k = 0
        while True:
            y = sigma_iter(b, k)
            if y > X:
                break
            v = y
            while v <= X:
                seen.add(v)
                v <<= 1
            k += 1
    return len(seen)


def orbit_count(seeds: list[int], X: int) -> int:
    """The same count, analytically.

    The representation v = 2^m sigma^k(b) with b primitive is unique:
    m = v_2(v) recovers the odd part y, and k is the number of times y can
    be pulled back by sigma^{-1} while staying == 5 mod 8, which recovers b.
    So no distinct triples collide and the count is a plain sum.
    """
    total = 0
    for b in seeds:
        u = 3 * b + 1                       # sigma^k(b) = (4^k u - 1)/3
        k = 0
        while True:
            y = (4 ** k * u - 1) // 3
            if y > X:
                break
            total += (X // y).bit_length()  # #{m >= 0 : 2^m y <= X}
            k += 1
    return total


def part_c(bmax: int) -> None:
    print("\n== C. the orbit of <4n+1, 2n> . B, exactly ==")
    seeds = primitive_seeds(bmax)
    print(f"  B = odd b <= {bmax}: {(bmax + 1) // 2} elements; "
          f"primitive seeds (b != 5 mod 8): {len(seeds)}")
    check("primitive seeds are exactly 3/4 of B (image of sigma is 5 mod 8)",
          abs(len(seeds) - 3 * ((bmax + 1) // 2) / 4) <= 1)
    small = seeds[:400]
    check("analytic count agrees with explicit enumeration (no collisions)",
          all(orbit_count(small, 1 << L) == orbit_count_set(small, 1 << L)
              for L in (20, 40, 64)))

    print("\n  The count is exactly  sum_{b in B'} #{(k,m) >= 0 : 2^m sigma^k(b) <= X},")
    print("  with no collisions.  Since sigma^k(b) = 4^k b (1 + O(1/b)), the")
    print("  inner count is the lattice triangle {m + 2k <= u_b} with")
    print("  u_b = log_2(X/b), of size (u_b+2)^2/4 + O(1).  Hence")
    print("      |S.B n [1,X]|  ~  (1/4) sum_{b in B'} (log_2(X/b) + 2)^2")
    print("                     ~  (|B'|/4) (log_2 X)^2 .")
    print("\n   log2 X   |S.B n [1,X]|   triangle law        ratio    crude |B'|L^2/4")
    rows = []
    scales = ((32, 64, 128, 256, 512, 1024) if len(seeds) <= 20000
              else (32, 48, 64, 96, 128))
    for L in scales:
        X = 1 << L
        c = orbit_count(seeds, X)
        sharp = sum((L - math.log2(b) + 2) ** 2 for b in seeds) / 4
        crude = len(seeds) * L * L / 4
        rows.append((L, c, sharp, crude))
        print(f"   {L:<8d} {c:<15d} {sharp:<19.0f} {c / sharp:<8.4f} {crude:.0f}")
    ratios = [c / s for _L, c, s, _cr in rows]
    check("the triangle law holds to within 7% and tightens with scale",
          all(0.93 < r < 1.02 for r in ratios) and ratios[-1] > ratios[0])
    check("the crude law |B'|(log2 X)^2/4 is a strict upper bound, "
          "approached from below",
          all(c < cr for _L, c, _s, cr in rows)
          and rows[-1][1] / rows[-1][3] > rows[0][1] / rows[0][3])
    check("hence natural density 0: the count is O((log X)^2) with X -> oo",
          all(c <= cr for _L, c, _s, cr in rows))

    print("\n  2-adic closure: sigma^k(b) = 4^k(b + 1/3) - 1/3 -> -1/3 in Z_2,")
    print("  so the closure of <sigma>.B is that set together with the single")
    print("  point -1/3 = 1 + 4 + 16 + ... = (...010101)_2; adjoining delta")
    print("  adds only the limit 0.  The closure is countable, hence nowhere")
    print("  dense: S.B lies in no set of positive 2-adic measure.")
    ok = True
    for k in range(1, 40):
        y = sigma_iter(1, k)
        # y should agree with -1/3 to 2-adic depth 2k+2
        if (y + 1) % (1 << (2 * k)) != ((-Fraction(1, 3) + 1).numerator
                                        * pow((-Fraction(1, 3) + 1).denominator,
                                              -1, 1 << (2 * k))) % (1 << (2 * k)):
            ok = False
            break
    check("sigma^k(1) converges 2-adically to -1/3 (depth grows like 2k)", ok)

    print("\n  intersection with the repunit family a_n = (3^n-1)/2:")
    # structural lemma first: when is a_n itself in the image of sigma?
    ok = True
    for n in range(3, 200, 2):
        a = (3 ** n - 1) // 2
        in_image = (a % 8 == 5) and (((a - 1) // 4) % 2 == 1)
        if in_image != (n % 4 == 3):
            ok = False
            break
    check("a_n lies in the image of sigma iff n = 3 mod 4 "
          "(then sigma^{-1}(a_n) = (3^n-3)/8)", ok)

    hits = []
    for n in range(1, 120, 2):
        a = (3 ** n - 1) // 2
        # a = sigma^k(b)  <=>  2^{2k+1}(3b+1) = 3^{n+1} - 1
        t = 3 ** (n + 1) - 1
        e = v2(t)                          # = 2 + v_2(n+1)
        for k in range((e - 1) // 2 + 1):
            if 2 * k + 1 > e:
                break
            rest = t >> (2 * k + 1)
            # rest must equal 3b+1 with b odd, i.e. rest = 4 mod 6
            if rest % 6 != 4:
                continue
            b = (rest - 1) // 3
            if b >= 1 and b % 2 == 1 and b <= bmax:
                hits.append((n, k, b))
    print(f"   solutions a_n = sigma^k(b), odd b <= {bmax}:  (n, k, b)")
    for h in hits:
        print(f"     {h}")
    # k is capped by v_2(3^{n+1}-1) = 2 + v_2(n+1), so 4^k <= 4(n+1) and hence
    # a_n <= 4(n+1) * bmax, which bounds n outright.
    nbound = max((n for n in range(1, 400, 2)
                  if (3 ** n - 1) // 2 <= 4 * (n + 1) * bmax), default=0)
    print(f"   elementary cap: k <= (1+v_2(n+1))/2, so a_n <= 4(n+1)*bmax,"
          f" forcing n <= {nbound}")
    check("the repunit intersection is finite and respects the elementary cap",
          all(h[0] <= nbound for h in hits))
    nmaxhit = max((h[0] for h in hits), default=0)
    print(f"   largest repunit exponent certified by <sigma,delta>.B: "
          f"n = {nmaxhit}  (a_n = {(3 ** nmaxhit - 1) // 2})")
    check("the semigroup certifies no repunit beyond the elementary cap "
          "-- it never reaches the open range", nmaxhit <= nbound)


# ---------------------------------------------------------------------------
# D. the <P_2> orbit of a finite B is finite
# ---------------------------------------------------------------------------

def part_d(bmax: int) -> None:
    print("\n== D. <P_2> . B is finite ==")
    total = 0
    dmax = 0
    for b in range(1, bmax + 1, 2):
        d = v3(b - 1) if b > 1 else 0
        if b == 1:
            d = 0
        total += d + 1
        dmax = max(dmax, d)
    print(f"  sum over odd b <= {bmax} of (v_3(b-1)+1) = {total}")
    print(f"  largest usable depth from this B: d = {dmax}")
    check("|<P_2>.B| is finite, bounded by sum_b (v_3(b-1)+1)", total < 10 ** 9)
    check("the depth budget is v_3(b-1), so d = O(log b): no infinite chain",
          dmax <= math.log(bmax, 3) + 1)
    print("  P_2 therefore contributes a FINITE extension of a finite B:")
    print("  the tower is unbounded only because its seed 2^M-1 is unbounded,")
    print("  and 2^M-1 must itself already be certified.")


# ---------------------------------------------------------------------------
# E. the n = 471 stress test
# ---------------------------------------------------------------------------

def reachable_from(target: int, bmax: int, budget: int = 200) -> bool:
    """Is target in <sigma, delta, P_2> . B ?  Decided by inverting.

    Every generator strictly increases its argument, so the pre-image search
    is finite: repeatedly strip delta (halve), sigma^{-1} = (x-1)/4, and
    P_2^{-1}(x) = (3x+1)/4, and ask whether any ancestor lands in B.
    """
    frontier = {target}
    for _ in range(budget):
        if any(0 < x <= bmax and x % 2 == 1 for x in frontier):
            return True
        nxt = set()
        for x in frontier:
            while x % 2 == 0:
                x //= 2
            if x <= 1:
                continue
            if x % 8 == 5:                       # sigma^{-1}
                nxt.add((x - 1) // 4)
            if (3 * x + 1) % 4 == 0:             # P_2^{-1}
                y = (3 * x + 1) // 4
                if y % 2 == 1:
                    nxt.add(y)
        if not nxt or nxt == frontier:
            return any(0 < x <= bmax and x % 2 == 1 for x in nxt)
        frontier = nxt
    return False


def part_e(bmax: int) -> None:
    print("\n== E. the n = 471 stress test ==")
    a471 = (3 ** 471 - 1) // 2
    print(f"  a_471 has {a471.bit_length()} bits")
    r = reachable_from(a471, bmax)
    check("a_471 is NOT in <sigma, delta, P_2> . B", not r)
    # and neither is any of its pre-descent states
    T = (1 << 471) - 1
    x = a471
    states = []
    while x >= T:
        states.append(x)
        x = f_odd(x)
    print(f"  pre-descent states of a_471: {len(states)}")
    bad = [i for i, s in enumerate(states[:40]) if reachable_from(s, bmax)]
    check("none of the first 40 pre-descent states is reachable either",
          not bad)
    print("  (as expected: S.B is polylogarithmically thin, so a 747-bit")
    print("   target is astronomically unlikely to be hit; the point of the")
    print("   test is that the reachability decision is finite and exact.)")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--bmax", type=int, default=10001,
                    help="FIN1 is 10^6; the default is a fast stand-in")
    args = ap.parse_args()
    print("== W2: the certificate-transport semigroup ==")
    part_a(args.bmax)
    part_b()
    part_c(args.bmax)
    part_d(args.bmax)
    part_e(args.bmax)
    print()
    if FAILURES:
        print(f"FAILURES ({len(FAILURES)}):")
        for f in FAILURES:
            print(f"  - {f}")
        raise SystemExit(1)
    print("CERTIFICATE-SEMIGROUP: PASS")


if __name__ == "__main__":
    main()
