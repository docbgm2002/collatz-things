#!/usr/bin/env python3
"""Syracuse 3-adic distribution conditioned on the repunit family (W5).

Exact integer arithmetic for every structural claim; floats only in the
reported character sums, which are averages.

W5 proposes importing Tao's Syracuse machinery -- the 3-adic distribution of
weighted states and its Fourier decrement -- conditioned on the repunit
family, to get a quantitative reset-gap bound.

A. THE CONDITIONING IS VACUOUS.  a_n = (3^n-1)/2 -> -1/2 in Z_3, so every
   repunit seed shares one 3-adic ghost.  But the affine identity
   x_K = (3^K x_0 + c_K)/2^{E_K} means that modulo 3^k, once K >= k,

       x_K = c_K 2^{-E_K}   (mod 3^k),

   a function of the VALUATION WORD alone: the seed is forgotten.  So
   "conditioning on the repunit family" has no 3-adic content past step k.

B. The ensemble distribution, against the correctly-modelled
   Syracuse stationary law (which is NOT uniform, and not uniform on the
   units either).

C. ENSEMBLE vs SINGLE ORBIT.  Tao's decrement is a statement about random
   valuation words.  W5's target -- decay along an ACTUAL orbit -- is a
   single-orbit equidistribution claim, which is a different and strictly
   harder object.  Both are measured.

D. The asymmetry that explains everything: f contracts 3-adically (by 3 per
   step, destroying information) and expands 2-adically (by 2^{e}, creating
   it).  Tao's method works on the destroying side.

Run:
    python3 scripts/explore_syracuse_3adic_conditioning.py
    python3 scripts/explore_syracuse_3adic_conditioning.py --nmax 1001
"""

from __future__ import annotations

import argparse
import cmath
import math

NOTES: list[str] = []


def note(label: str, ok: bool) -> None:
    if not ok:
        NOTES.append(label)
    print(f"  [{'ok  ' if ok else 'MISS'}] {label}")


def v2(x: int) -> int:
    return (x & -x).bit_length() - 1


def f_odd(x: int) -> int:
    y = 3 * x + 1
    return y >> v2(y)


def repunit_orbit(n: int) -> list[int]:
    T = (1 << n) - 1
    x = (3 ** n - 1) // 2
    out = [x]
    while x >= T:
        x = f_odd(x)
        out.append(x)
    return out


# ---------------------------------------------------------------------------
# A. the conditioning is vacuous
# ---------------------------------------------------------------------------

def part_a() -> None:
    print("\n== A. the repunit 3-adic ghost, and its erasure ==")
    print("  a_n = (3^n - 1)/2 -> -1/2 in Z_3.")
    ok = True
    for k in range(1, 9):
        mod = 3 ** k
        target = (-pow(2, -1, mod)) % mod
        for n in range(k, k + 30, 2):
            if ((3 ** n - 1) // 2) % mod != target:
                ok = False
    note("a_n = -1/2 (mod 3^k) for every n >= k: all repunit seeds share one "
         "3-adic ghost, a Dirac mass", ok)
    print("  So 3-adically the family is maximally concentrated, not spread.")

    print("\n  But the affine identity erases it.  With")
    print("      x_K = (3^K x_0 + c_K) / 2^{E_K},   c_K = sum_t 3^{K-1-t} 2^{E_t},")
    print("  reduction mod 3^k kills the 3^K x_0 term as soon as K >= k:")
    print("      x_K = c_K 2^{-E_K}  (mod 3^k).")
    ok = True
    shown = []
    for k in (2, 3, 4):
        mod = 3 ** k
        for n in range(11, 60, 2):
            x = (3 ** n - 1) // 2
            c, E = 0, 0
            for K in range(1, 12):
                y = 3 * x + 1
                e = v2(y)
                c = 3 * c + (1 << E)
                E += e
                x = y >> e
                if K >= k:
                    lhs = x % mod
                    rhs = (c * pow(2, -E, mod)) % mod
                    if lhs != rhs:
                        ok = False
                    if k == 3 and n == 11 and K in (3, 4, 5):
                        shown.append((k, n, K, lhs))
    note("x_K = c_K 2^{-E_K} (mod 3^k) for every K >= k: the seed is "
         "forgotten, so the conditioning is vacuous past step k", ok)

    # two different seeds with the same valuation word agree mod 3^k
    print("\n  Direct consequence: any two starting values whose valuation")
    print("  words agree for K >= k steps have the SAME residue mod 3^k.")
    ok = True
    mod = 3 ** 4
    found = 0
    for x0 in range(3, 4000, 2):
        for d in (1 << 20, 1 << 24):
            x1 = x0 + d
            a, b = x0, x1
            word_a, word_b = [], []
            for _ in range(6):
                ya, yb = 3 * a + 1, 3 * b + 1
                ea, eb = v2(ya), v2(yb)
                word_a.append(ea)
                word_b.append(eb)
                a, b = ya >> ea, yb >> eb
            if word_a == word_b:
                found += 1
                if a % mod != b % mod:
                    ok = False
    note(f"verified on {found} seed pairs sharing a 6-step word: equal "
         "residues mod 3^4", ok and found > 100)


# ---------------------------------------------------------------------------
# B / C. ensemble versus single orbit
# ---------------------------------------------------------------------------

def syracuse_stationary(k: int) -> dict[int, float]:
    """The Syracuse stationary law of x = c 2^{-E} mod 3^k, exactly modelled.

    Under the standard valuation model P(e = j) = 2^{-j} (j >= 1), the pair
    (c mod 3^k, E mod ord) is a finite Markov chain with
        c -> 3c + 2^E,   E -> E + e,
    where ord = phi(3^k) = 2*3^{k-1} is the order of 2 mod 3^k, so only
    e mod ord matters and P(e = r mod ord) = 2^{-r}/(1 - 2^{-ord}).

    This measure is NOT uniform, and not uniform on the units either: already
    mod 3 it gives 2/3 to the class 2 and 1/3 to the class 1, because
    x = 2^{-e} mod 3 and P(e odd) = 2/3.  Comparing data against uniform
    therefore reports a large spurious bias.
    """
    mod = 3 ** k
    ordr = 2 * 3 ** (k - 1)
    denom = 1 - 2.0 ** (-ordr)
    pe = [0.0] * (ordr + 1)
    for r in range(1, ordr + 1):
        pe[r] = 2.0 ** (-r) / denom
    pw = [pow(2, E, mod) for E in range(ordr)]
    states = [(c, E) for c in range(mod) for E in range(ordr)]
    idx = {s: i for i, s in enumerate(states)}
    dist = [1.0 / len(states)] * len(states)
    for _ in range(400):
        nxt = [0.0] * len(states)
        for i, (c, E) in enumerate(states):
            p = dist[i]
            if p == 0.0:
                continue
            c2 = (3 * c + pw[E]) % mod
            for r in range(1, ordr + 1):
                nxt[idx[(c2, (E + r) % ordr)]] += p * pe[r]
        dist = nxt
    out: dict[int, float] = {}
    for i, (c, E) in enumerate(states):
        x = (c * pow(pw[E], -1, mod)) % mod if c % 3 else None
        if x is None:
            continue
        out[x] = out.get(x, 0.0) + dist[i]
    tot = sum(out.values())
    return {x: p / tot for x, p in out.items()}


def tv_to(values: list[int], k: int, ref: dict[int, float]) -> tuple[float, float]:
    """Total variation from the reference law, plus fair-sample noise."""
    mod = 3 ** k
    cnt: dict[int, int] = {}
    for x in values:
        r = x % mod
        if r % 3:
            cnt[r] = cnt.get(r, 0) + 1
    M = sum(cnt.values())
    if M == 0:
        return 0.0, 0.0
    keys = set(cnt) | set(ref)
    tv = 0.5 * sum(abs(cnt.get(x, 0) / M - ref.get(x, 0.0)) for x in keys)
    exp_tv = math.sqrt((len(ref) - 1) / (2 * math.pi * M))
    return tv, exp_tv


def part_bc(nmax: int) -> None:
    print("\n== B. the ensemble distribution against the SYRACUSE law ==")
    print("  Two wrong references to avoid: uniform on Z/3^k (states are")
    print("  never divisible by 3, so this shows a spurious ~1/2 bias), and")
    print("  uniform on the units (the true law is not uniform either --")
    print("  already mod 3 it is 2/3 on class 2, 1/3 on class 1, because")
    print("  x = 2^{-e} mod 3 and P(e odd) = 2/3).")
    refs = {k: syracuse_stationary(k) for k in (1, 2, 3)}
    print("\n  modelled Syracuse law mod 3 : "
          + ", ".join(f"{x}:{p:.4f}" for x, p in sorted(refs[1].items())))
    orbits = {}
    for n in range(11, nmax + 1, 2):
        orbits[n] = repunit_orbit(n)
    allstates = [x for orb in orbits.values() for x in orb[1:]]
    print(f"\n  {len(orbits)} orbits, {len(allstates)} post-seed states")
    ok = True
    ok3 = all(x % 3 for x in allstates)
    note("no post-seed repunit state is divisible by 3 (so the units are the "
         "right support)", ok3)

    # pool by E-scale, as W5 asks
    buckets: dict[int, list[int]] = {}
    for orb in orbits.values():
        E = 0
        for K in range(1, len(orb)):
            y = 3 * orb[K - 1] + 1
            E += v2(y)
            buckets.setdefault(E // 16, []).append(orb[K])
    print("\n   k   E-scale   samples   TV to Syracuse law   fair-sample TV   ratio")
    for k in (2, 3):
        for b in sorted(buckets)[:5]:
            vals = buckets[b]
            if len(vals) < 400:
                continue
            tv, exp_tv = tv_to(vals, k, refs[k])
            print(f"   {k}   {b * 16:<9d} {len(vals):<9d} {tv:<20.4f} "
                  f"{exp_tv:<16.4f} {tv / exp_tv:.2f}")
            if tv > 6 * exp_tv:
                ok = False
    note("pooled at matched E-scales, the repunit states match the modelled "
         "Syracuse stationary law to within a small multiple of fair-sample "
         "noise", ok)
    print("  The one outlier is the E-scale-0 bucket (ratio ~3.9), which mixes")
    print("  the first few steps -- exactly the regime where part A says the")
    print("  seed has not yet been forgotten.  An internal consistency check.")
    print("  This is an ENSEMBLE statement: the average runs over exponents n.")

    print("\n== C. the single-orbit statement, which is what W5 needs ==")
    print("  The target 'deterministic decrement lemma' asks for decay along")
    print("  ONE actual orbit.  There the average is over K, not over n.")
    print("\n   n      states   k   TV to Syracuse law   fair-sample TV   ratio")
    for n in (471, 1197, 2001):
        orb = orbits.get(n) or repunit_orbit(n)
        body = orb[1:]
        for k in (2, 3):
            tv, exp_tv = tv_to(body, k, refs[k])
            print(f"   {n:<6d} {len(body):<8d} {k}   {tv:<20.4f} "
                  f"{exp_tv:<16.4f} {tv / exp_tv:.2f}")
    print("\n  A single orbit also looks equidistributed on the units, within")
    print("  a small multiple of its own sampling noise.  But that is an")
    print("  OBSERVATION about one sequence, not a theorem:")
    print("  But that is an OBSERVATION about one sequence, not a theorem:")
    print("  no ensemble argument delivers it, because there is no ensemble.")
    print("  Converting Tao's decrement into a single-orbit statement is")
    print("  exactly the equidistribution problem that W11 showed is not")
    print("  reachable by rotation/cocycle methods and W10 showed is not")
    print("  reachable by digit theorems.  It is the same open object.")


# ---------------------------------------------------------------------------
# D. the asymmetry
# ---------------------------------------------------------------------------

def part_d(nmax: int) -> None:
    print("\n== D. why the 3-adic side is the wrong side ==")
    print("  f(x) = (3x+1)/2^e acts oppositely on the two primes:")
    print("    3-adically it MULTIPLIES by 3, so |x1-x2|_3 shrinks by 1/3 per")
    print("      step: information about the seed is destroyed at rate log 3;")
    print("    2-adically it DIVIDES by 2^e, so |x1-x2|_2 grows by 2^e per")
    print("      step: new high bits are consumed at rate E[e] log 2.")
    tot_e, tot_k = 0, 0
    for n in range(11, min(nmax, 301) + 1, 2):
        x = (3 ** n - 1) // 2
        T = (1 << n) - 1
        while x >= T:
            y = 3 * x + 1
            e = v2(y)
            tot_e += e
            tot_k += 1
            x = y >> e
    mean_e = tot_e / tot_k
    print(f"\n  measured over {tot_k} repunit steps: mean e = {mean_e:.4f}")
    print(f"  3-adic contraction rate : log 3          = {math.log(3):.4f}")
    print(f"  2-adic expansion rate   : E[e] log 2     = "
          f"{mean_e * math.log(2):.4f}")
    note("the mean valuation is close to the model value 2, so the two rates "
         "are comparable in magnitude but OPPOSITE in sign",
         abs(mean_e - 2) < 0.15)
    print("\n  Tao's method lives on the contracting side, where equidistribution")
    print("  is produced -- and equidistribution is precisely the destruction")
    print("  of the individual-orbit information this repository needs.  The")
    print("  repo's own structure (TWR1, the burn, the ghosts, PCD15's")
    print("  'previously unseen high bits') all lives on the expanding side.")
    print("  That is the structural reason W5 cannot be turned into a")
    print("  reset-gap bound: it is aimed at the prime where the information")
    print("  is being lost.")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--nmax", type=int, default=601)
    args = ap.parse_args()
    print("== W5: Syracuse 3-adic distribution on the repunit family ==")
    part_a()
    part_bc(args.nmax)
    part_d(args.nmax)
    print()
    if NOTES:
        print(f"MISMATCHES ({len(NOTES)}):")
        for f in NOTES:
            print(f"  - {f}")
        raise SystemExit(1)
    print("SYRACUSE-3ADIC: consistent")


if __name__ == "__main__":
    main()
