#!/usr/bin/env python3
"""
SH1 GENERALIZATION TEST  (refined)

Question: does the SH1 shadow argument use anything about 3 and 2 beyond
the existence of an expanding rational cycle (c^E < a^K)?

Map, gcd(a,c)=1, c prime, on integers coprime to c:
    T(x) = (a*x + b) / c^{v_c(a*x+b)}

For every expanding cycle found we test the four ingredients of the proof
separately, so we can see exactly which one is (a,c)-specific:

  I.   valuation itinerary reproduced by the positive shadow
  II.  suffix closure   X == T^K(X)  mod c^(N-E)      [ suffix coordinates ]
  III. exact value gain T^K(X)/X > 1                  [ the contradiction  ]
  IV.  base-c length closure len(X) == len(T^K(X))    [ the len coordinate ]

Exact integer arithmetic throughout.
"""
from math import gcd
from fractions import Fraction

def vc(n, c):
    v = 0
    while n % c == 0:
        n //= c; v += 1
    return v

def T(x, a, b, c):
    y = a * x + b
    v = vc(y, c)
    return y // c ** v, v

def lenc(n, c):
    L = 0
    while n:
        n //= c; L += 1
    return L

def all_cycles(a, b, c, lo=-6000, maxit=6000):
    found = {}
    for seed in range(lo, 0):
        if seed % c == 0: continue
        x, seen, order = seed, {}, []
        for step in range(maxit):
            if x in seen:
                cyc = order[seen[x]:]
                if cyc:
                    found.setdefault(tuple(sorted(cyc)), cyc)
                break
            if abs(x) > 10 ** 14: break
            seen[x] = step; order.append(x)
            x, _ = T(x, a, b, c)
    return list(found.values())

def cyc_KE(cyc, a, b, c):
    x, E = cyc[0], 0
    for _ in range(len(cyc)):
        x, e = T(x, a, b, c); E += e
    return len(cyc), E

def test_shadow(cyc, a, b, c, Nmax=26, wmax=3000):
    """Find a positive shadow; report which ingredients hold."""
    x0, K = cyc[0], len(cyc)
    _, E = cyc_KE(cyc, a, b, c)
    ref, y = [], x0
    for _ in range(K):
        y, e = T(y, a, b, c); ref.append(e)
    best = None
    for N in range(E + 3, Nmax):
        for w in range(1, wmax):
            X = x0 + c ** N * w
            if X <= 0 or X % c == 0: continue
            Y, got = X, []
            for _ in range(K):
                Y, e = T(Y, a, b, c); got.append(e)
            if got != ref: continue
            II  = (Y - X) % c ** (N - E) == 0
            III = Y > X
            IV  = lenc(X, c) == lenc(Y, c)
            if not (II and III): continue
            if best is None:
                best = dict(N=N, w=w, X=X, Y=Y, I=True, II=II, III=III, IV=IV)
            if IV:                       # prefer a witness that also closes len
                return dict(N=N, w=w, X=X, Y=Y, I=True, II=II, III=III, IV=True)
    return best

CASES = [(3,1,2),(5,1,2),(7,1,2),(9,1,2),(11,1,2),(5,3,2),(7,3,2),
         (2,1,3),(4,1,3),(5,1,3),(5,2,3),(7,1,3),(10,1,3),(11,1,3),
         (3,1,5),(7,1,5),(6,1,5),(9,1,5),(4,1,5)]

print("=" * 78)
print("SH1 SHADOW MECHANISM, GENERAL (a, b, c)")
print("  I=itinerary  II=suffix closes  III=value gain>1  IV=base-c len closes")
print("=" * 78)

rows = []
for (a, b, c) in CASES:
    if gcd(a, c) != 1: continue
    exp = []
    for cyc in all_cycles(a, b, c):
        K, E = cyc_KE(cyc, a, b, c)
        if a ** K > c ** E and any(v < 0 for v in cyc):
            exp.append((cyc, K, E))
    if not exp:
        print(f"\n(a,b,c)=({a},{b},{c}):  NO expanding negative cycle found")
        rows.append((a,b,c,None)); continue
    exp.sort(key=lambda t: (-t[1], t[1]))          # prefer longer cycles first
    print(f"\n(a,b,c)=({a},{b},{c}):  {len(exp)} expanding cycle(s)")
    for cyc, K, E in exp[:3]:
        gain = Fraction(a ** K, c ** E)
        r = test_shadow(cyc, a, b, c)
        mem = sorted(cyc)
        tag = f"K={K} E={E} gain={a**K}/{c**E}={float(gain):.5f}"
        if r is None:
            print(f"   {tag}  members={mem[:5]}   -> no shadow found")
            continue
        flags = f"I={r['I']} II={r['II']} III={r['III']} IV={r['IV']}"
        print(f"   {tag}  members={mem[:5]}")
        print(f"      shadow N={r['N']} X={r['X']} -> Y={r['Y']}   {flags}")
        print(f"      gain<c ({float(gain):.4f}<{c}): {gain < c}")
        rows.append((a,b,c,(K,E,float(gain),r['IV'],gain < c)))

print("\n" + "=" * 78)
print("DOES len-CLOSURE (IV) TRACK THE CONDITION gain < c ?")
print("=" * 78)
for row in rows:
    if row[3] is None: continue
    a,b,c,(K,E,g,IV,lt) = row
    mark = "consistent" if IV == lt else "*** MISMATCH ***"
    print(f"  ({a},{b},{c}) K={K} gain={g:.4f}  IV={IV}  gain<c={lt}   {mark}")
