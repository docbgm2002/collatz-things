#!/usr/bin/env python3
"""
verify_sufficiency_reduction.py
===============================

Machine verification of the pieces of SUFF1 that are now proved, and an
explicit statement of the one piece that is not.

BACKGROUND.  COST1 says when the quantized-log closure criterion CAN be met.
Sufficiency -- that integer witnesses realising it exist -- was the open half.
This file verifies the reduction.

CARRY LEMMA (CARRY1).  Let Q = 2^j, L_Q = floor(Q log_2 3), phi_Q =
{Q log_2 3}.  For odd x with cell C = floor(Q log_2 x), in-cell position
u = Q log_2 x - C in [0,1), and e = v_2(3x+1), SUBJECT TO THE HEIGHT
HYPOTHESIS

    x  >=  Q / ( 3 * ln 2 * (1 - phi_Q) ),                          (H)

we have:

    floor(Q log_2 f(x))  =  C + L_Q - Q e + delta,      delta in {0,1},

and delta = 1 exactly when u lies in the top phi_Q-fraction of the cell.

(H) IS NECESSARY.  delta = floor(u + phi_Q + Q*eps) with
eps = log_2(1 + 1/(3x)).  delta = 2 needs u >= 2 - phi_Q - Q*eps, which is
possible with u < 1 only when Q*eps > 1 - phi_Q.  Since
Q*eps < Q/(3 x ln 2), hypothesis (H) rules that out.  An earlier draft of
this lemma OMITTED (H) and was FALSE for small x at large j; the omission
was caught by the verifier and is logged in CLAIM_LEDGER.md.

Around a closed K-cycle
the cells return, so

    sum(delta_i)  =  Q E - K L_Q  =  s.

So s is literally THE NUMBER OF CARRYING EDGES.  The criterion 0 <= s <= K
is exactly the statement that this count is a legal count.

POSITION FREEDOM (FREE1).  At a junction the witnesses x_{i+1} and f(x_i)
are DISTINCT INTEGERS required only to share a cell.  So the in-cell position
of x_{i+1} is not determined by edge i and may be chosen freely.  Both target
sub-intervals -- [0, 1-phi_Q) for non-carrying and [1-phi_Q, 1) for carrying
-- are nonempty precisely because 0 < phi_Q < 1, i.e. because log_2 3 is
irrational (DICH1).

ARITHMETIC HALF (WALK1).  The mod-2^m suffix automaton admits a closed walk
of length K with total valuation exactly floor(K log_2 3), for every K >= 5,
by an explicit construction using self-loops of weight 1 and 2 lying in one
strongly connected component.  This works because 1 < log_2 3 < 2.

WHAT IS NOT PROVED.  See section (X) at the end.

NO FLOATING POINT APPEARS IN ANY ASSERTION.
"""

import collections
import json
import os
import sys

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


def f(x):
    y = 3 * x + 1
    e = v2(y)
    return y // 2 ** e, e


def qlog2(x, Q):
    return (x ** Q).bit_length() - 1


def L_of(Q):
    return (3 ** Q).bit_length() - 1


def floor_K(K):
    return (3 ** K).bit_length() - 1


# ---------------------------------------------------------------------------
print("\n(CARRY1) cell displacement is L_Q - Q e + delta with delta in {0,1}")
print("         under the height hypothesis (H)")
from decimal import Decimal, getcontext
getcontext().prec = 60
LN2 = Decimal(2).ln()
BETA = Decimal(3).ln() / LN2


def height_threshold(Q):
    """Smallest x for which (H) holds: x >= Q / (3 ln2 (1 - phi_Q))."""
    phi = Decimal(Q) * BETA - L_of(Q)
    return int(Decimal(Q) / (3 * LN2 * (1 - phi))) + 1


bad = 0
tested = 0
for j in (2, 3, 4, 5, 6, 7, 8):
    Q = 2 ** j
    L = L_of(Q)
    lo = max(3, height_threshold(Q)) | 1
    for x in range(lo, lo + 40000, 2):
        y, e = f(x)
        d = (qlog2(y, Q) - qlog2(x, Q)) - L + Q * e
        tested += 1
        if d not in (0, 1):
            bad += 1
check("delta in {0,1} for every (j, x) satisfying (H)", bad == 0,
      f"{tested} edges above threshold, {bad} violations")

# and confirm (H) is not vacuous: violations DO occur below the threshold
viol_below = 0
for j in (6, 7, 8):
    Q = 2 ** j
    L = L_of(Q)
    thr = height_threshold(Q)
    for x in range(3, min(thr, 4000), 2):
        y, e = f(x)
        if ((qlog2(y, Q) - qlog2(x, Q)) - L + Q * e) >= 2:
            viol_below += 1
check("(H) is necessary: delta >= 2 does occur below the threshold",
      viol_below > 0, f"{viol_below} violations found below (H)")

# ---------------------------------------------------------------------------
print("\n(CARRY1) around a mined cycle:  sum(delta) = s")
HERE = os.path.dirname(os.path.abspath(__file__))
CERTS = json.load(open(os.path.join(HERE, "certificates_quantized_log_remined.json")))
for js in sorted(CERTS, key=int):
    j = int(js)
    Q = 2 ** j
    L = L_of(Q)
    W = CERTS[js]["witnesses"]
    K = CERTS[js]["K"]
    check(f"j={j}: all witnesses satisfy the height hypothesis (H)",
          all(x >= height_threshold(Q) for x in W),
          f"min witness {min(W)}, threshold {height_threshold(Q)}")
    ds = []
    E = 0
    for x in W:
        y, e = f(x)
        E += e
        ds.append((qlog2(y, Q) - qlog2(x, Q)) - L + Q * e)
    s = E * Q - K * L
    check(f"j={j}: sum(delta) = s", sum(ds) == s,
          f"sum={sum(ds)}, s={s}, all delta in {{0,1}}={all(d in (0,1) for d in ds)}")
    check(f"j={j}: E = floor(K log_2 3)", E == floor_K(K), f"E={E}")

# ---------------------------------------------------------------------------
print("\n(FREE1) both position sub-intervals are nonempty  <=>  0 < phi_Q < 1")
ok = True
for j in range(1, 16):
    Q = 2 ** j
    # phi_Q > 0 and < 1 iff Q*log_2(3) is not an integer, i.e. 3^Q is not a power of 2
    n = L_of(Q)
    if 2 ** n == 3 ** Q:
        ok = False
check("Q log_2 3 is never an integer (3^Q is never a power of 2)", ok,
      "j = 1..15")

# ---------------------------------------------------------------------------
print("\n(WALK1) the mod-16 automaton and the explicit construction")
m = 4
M = 1 << m


def succ(r):
    y = 3 * r + 1
    e = v2(y)
    if e >= m:
        return None
    base = (y >> e) % (1 << (m - e))
    return e, [s for s in ((base + t * (1 << (m - e))) % M for t in range(1 << e))
               if s % 2 == 1]


loops = {r: succ(r)[0] for r in range(1, M, 2) if succ(r) and r in succ(r)[1]}
check("self-loop of weight 1 exists", loops.get(15) == 1, "at r=15")
check("self-loop of weight 2 exists", loops.get(1) == 2, "at r=1")


def bfs(a, b):
    prev = {a: None}
    q = collections.deque([a])
    while q:
        u = q.popleft()
        if u == b:
            break
        s = succ(u)
        if not s:
            continue
        for v in s[1]:
            if v not in prev:
                prev[v] = u
                q.append(v)
    if b not in prev:
        return None
    p = [b]
    while prev[p[-1]] is not None:
        p.append(prev[p[-1]])
    return p[::-1]


P1, P2 = bfs(15, 1), bfs(1, 15)
check("15 and 1 lie in one strongly connected component", P1 and P2,
      f"{P1} and {P2}")


def wt(p):
    return sum(succ(p[i])[0] for i in range(len(p) - 1))


Lt = (len(P1) - 1) + (len(P2) - 1)
Wt = wt(P1) + wt(P2)
check("travel cost computed", (Lt, Wt) == (5, 7), f"length {Lt}, weight {Wt}")

# the construction: a loops at 15 (w=1), travel, b loops at 1 (w=2), travel
fails = []
for K in range(2, 400):
    E = floor_K(K)
    b = E - K - (Wt - Lt)
    a = (K - Lt) - b
    if a < 0 or b < 0:
        fails.append(K)
        continue
    if not (a + b + Lt == K and a * 1 + b * 2 + Wt == E):
        fails.append(K)
check("construction gives length K, weight floor(K log_2 3) for all K >= 5",
      fails == [2, 3, 4], f"fails only at {fails}")
print("      a = 2K - floor(K log2 3) - 3 >= 0  because log_2 3 < 2")
print("      b = floor(K log2 3) - K - 2 >= 0  because log_2 3 > 1")

# K = 2,3,4 by direct search
def walk_exists(K, W):
    nodes = [r for r in range(1, M, 2) if succ(r)]
    for start in nodes:
        cur = {start: {0}}
        for _ in range(K):
            nxt = {}
            for u, ws in cur.items():
                s = succ(u)
                if not s:
                    continue
                e, ss = s
                for t in ss:
                    acc = nxt.setdefault(t, set())
                    for w in ws:
                        if w + e <= W:
                            acc.add(w + e)
            cur = nxt
        if start in cur and W in cur[start]:
            return True
    return False


check("K = 2, 3, 4 handled by direct search",
      all(walk_exists(K, floor_K(K)) for K in (2, 3, 4)))

# ---------------------------------------------------------------------------
print("\n(X) WHAT IS NOT PROVED")
print("""      The joint realisation.  A witness x_i must simultaneously
      (i) lie in a prescribed sub-interval of its cell (archimedean) and
      (ii) lie in a prescribed class mod 2^m (2-adic).  A counting bound
      gives (i) and (ii) together once

          log_2 x  >~  m + e + j + log_2( 1 / min(phi_Q, 1-phi_Q) ),

      which is finite for each fixed Q.  The residual gap is a COUPLING:
      tau(f(x_i)) depends on the top bits of f(x_i), which are fixed by the
      cell choice for x_i, while tau(x_{i+1}) is fixed by the residue walk.
      Making those agree jointly with (i) and (ii) is not established here.
      SUFF1 therefore remains OPEN, but is now reduced to that single
      coupling statement.""")

print("\n" + "=" * 64)
if FAILURES:
    print(f"FAILED: {len(FAILURES)} check(s)")
    for x in FAILURES:
        print("   -", x)
    sys.exit(1)
print("ALL PASS")
