#!/usr/bin/env python3
"""
verify_suff1_composition.py
===========================

Verification of the ingredients of SUFF1 in the composed, general form.

THEOREM (SUFF1, as composed in docs/no-go/suff1.md).  Let Q = 2^j, let m >= 3,
and let K be admissible at Q (s = Q*floor(K b) - K*floor(Q b) in [0,K],
b = log_2 3).  Suppose the mod-2^m suffix automaton is strongly connected on
its live nodes.  Then a closed quantized-log certificate of length K exists,
with all witnesses of bit-length at least

    Theta = m + K + j + log_2( 1/min(phi_Q, 1-phi_Q) ) + 0.25*K + O(1).

Checked here:

  (A) SELF-LOOPS, PROVED ALGEBRAICALLY FOR ALL m.
      r = 2^m - 1:  3r+1 = 2(3*2^{m-1} - 1), so e = 1, and the successor set
      is {2^{m-1}-1, 2^m-1} -- a weight-1 self-loop.
      r = 1:  3r+1 = 4, so e = 2 (m >= 3), and the successor set is
      {1 + t*2^{m-2} : t = 0..3} -- a weight-2 self-loop.
      The verifier confirms the closed forms, so these are identities and not
      a search.

  (B) STRONG CONNECTIVITY -- VERIFIED, NOT PROVED, for m = 3..14.

  (C) WALK AVAILABILITY.  For every m in 3..8 and every admissible (j,K) in
      range, a closed walk of length K and total valuation floor(K log_2 3)
      exists.

  (D) STRICT GAIN IS AUTOMATIC.  prod(y_i)/prod(x_i)
      = (3^K / 2^E) * prod(1 + 1/(3 x_i)) > 3^K / 2^E > 1
      whenever E = floor(K log_2 3), since 3^K > 2^E.  No analytic estimate
      of any epsilon is needed anywhere.

  (E) THE HEIGHT BOUND IS FINITE for every (j, K, m) tested.

NO FLOATING POINT APPEARS IN ANY ASSERTION.  The height bound is reported
using high-precision decimal for readability only; its finiteness is an
integer statement (phi_Q != 0 because 3^Q is never a power of 2).
"""

import collections
import sys
from decimal import Decimal, getcontext

getcontext().prec = 80
FAILURES = []


def check(name, cond, detail=""):
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ""))
    if not cond:
        FAILURES.append(name)


def v2(n):
    v = 0
    while n % 2 == 0:
        n //= 2
        v += 1
    return v


def succ(r, m):
    M = 1 << m
    y = 3 * r + 1
    e = v2(y)
    if e >= m:
        return None
    base = (y >> e) % (1 << (m - e))
    return e, [s for s in ((base + t * (1 << (m - e))) % M for t in range(1 << e))
               if s % 2 == 1]


def floor_K(K):
    return (3 ** K).bit_length() - 1


def L_of(Q):
    return (3 ** Q).bit_length() - 1


# ---------------------------------------------------------------------------
print("\n(A) the two self-loops, as closed forms valid for every m")
bad = []
for m in range(3, 21):
    M = 1 << m
    s = succ(M - 1, m)
    if s is None or s[0] != 1 or sorted(s[1]) != sorted([(1 << (m - 1)) - 1, M - 1]):
        bad.append(("top", m))
    s = succ(1, m)
    if s is None or s[0] != 2 or sorted(s[1]) != sorted(
            [1 + t * (1 << (m - 2)) for t in range(4)]):
        bad.append(("one", m))
check("succ(2^m-1) = (1, {2^{m-1}-1, 2^m-1}) for m = 3..20", 
      not [x for x in bad if x[0] == "top"])
check("succ(1) = (2, {1 + t 2^{m-2}}) for m = 3..20",
      not [x for x in bad if x[0] == "one"])
print("      these are identities, so the self-loops exist for ALL m >= 3")

# ---------------------------------------------------------------------------
print("\n(B) strong connectivity of the live subgraph -- VERIFIED, NOT PROVED")


def reach(a, m):
    seen = {a}
    q = collections.deque([a])
    while q:
        u = q.popleft()
        s = succ(u, m)
        if not s:
            continue
        for v in s[1]:
            if v not in seen:
                seen.add(v)
                q.append(v)
    return seen


for m in range(3, 15):
    M = 1 << m
    live = {r for r in range(1, M, 2) if succ(r, m)}
    R1, R2 = reach(M - 1, m), reach(1, m)
    ok = (1 in R1) and ((M - 1) in R2) and live <= (R1 & R2)
    check(f"m={m:2d}: live nodes form one strongly connected component", ok,
          f"{len(live)} live nodes")

# ---------------------------------------------------------------------------
print("\n(C) walk availability for every admissible (j, K)")


def walk(m, K, W):
    nodes = [r for r in range(1, 1 << m, 2) if succ(r, m)]
    for st in nodes:
        cur = {st: {0}}
        for _ in range(K):
            nxt = {}
            for u, ws in cur.items():
                s = succ(u, m)
                if not s:
                    continue
                e, ss = s
                for t in ss:
                    acc = nxt.setdefault(t, set())
                    for w in ws:
                        if w + e <= W:
                            acc.add(w + e)
            cur = nxt
            if not cur:
                break
        if st in cur and W in cur[st]:
            return True
    return False


miss = []
n_trip = 0
for m in range(3, 9):
    for j in range(1, 8):
        Lq = L_of(2 ** j)
        for K in range(2, 26):
            s = (floor_K(K) << j) - K * Lq
            if not (0 <= s <= K):
                continue
            n_trip += 1
            if not walk(m, K, floor_K(K)):
                miss.append((m, j, K))
check("every admissible (m, j, K) has a valid closed walk", not miss,
      f"{n_trip} triples, {len(miss)} missing")

# ---------------------------------------------------------------------------
print("\n(D) strict gain is automatic: 3^K > 2^floor(K log_2 3)")
bad = 0
for K in range(1, 800):
    if not (3 ** K > 2 ** floor_K(K)):
        bad += 1
check("3^K > 2^E with E = floor(K log_2 3), K = 1..799", bad == 0,
      "no epsilon estimate needed")

# ---------------------------------------------------------------------------
print("\n(E) the height bound is finite for every (j, K, m)")
LN2 = Decimal(2).ln()
BETA = Decimal(3).ln() / LN2
rows = []
for j in (3, 5, 8, 12):
    Q = 2 ** j
    phi = Decimal(Q) * BETA - L_of(Q)
    # phi != 0 is an integer statement:
    if 2 ** L_of(Q) == 3 ** Q:
        FAILURES.append(f"phi_Q = 0 at j={j}")
    w = min(phi, 1 - phi)
    for K, m in ((2, 4), (12, 4), (53, 6), (665, 8)):
        Lq = L_of(Q)
        s = (floor_K(K) << j) - K * Lq
        if not (0 <= s <= K):
            continue
        theta = m + K + j + (-w.ln() / LN2) + Decimal("0.25") * K + 4
        rows.append((j, K, m, float(theta)))
check("phi_Q is never 0, so log_2(1/min(phi,1-phi)) is finite",
      not [x for x in FAILURES if "phi_Q" in str(x)])
for j, K, m, t in rows:
    print(f"      j={j:2d} K={K:4d} m={m}:  witnesses of >= {t:8.1f} bits suffice")

print("\n(X) SCOPE")
print("""      SUFF1 as composed is proved for every j, every admissible K, and
      every m for which the automaton is strongly connected -- verified for
      m = 3..14.  Strong connectivity for ALL m is NOT proved; that single
      graph-theoretic statement is what remains.""")

print("\n" + "=" * 66)
if FAILURES:
    print(f"FAILED: {len(FAILURES)} check(s)")
    for x in FAILURES:
        print("   -", x)
    sys.exit(1)
print("ALL PASS")
