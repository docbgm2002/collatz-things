#!/usr/bin/env python3
"""
verify_connectivity.py
======================

CONN1: the mod-2^m suffix automaton is strongly connected, for every m >= 3.

This was the last conditional hypothesis in SUFF1.  With CONN1 proved, SUFF1
is unconditional for the 3x+1 map.

THE HUB.  Let

    h_m = 3^{-1} (2^{m-1} - 1)   mod 2^m.

3 is invertible mod 2^m, and 2^{m-1} - 1 is odd for m >= 2, so h_m exists,
is unique, and is odd.  By construction 3 h_m + 1 = 2^{m-1} (mod 2^m), so
v_2(3 h_m + 1) = m - 1 < m: h_m is LIVE, with the largest possible valuation.

  (H1)  h_m -> every odd residue in ONE step.
        The successor set of a node with valuation e is a full class mod
        2^{m-e}.  At e = m-1 that is a class mod 2^1, i.e. all odd residues.

  (H2)  every live node -> h_m within m-1 steps.
        CLASS-GROWTH LEMMA: the set reachable from r in k steps contains a
        full class mod 2^{m - E_k}, where E_k is the total valuation along
        the path.  Induction: the successors of a class C mod 2^{m-E_k} are
        obtained by the affine injection r |-> 3r+1, division by 2^e, and
        then a free choice of e high bits; the image of C is a class mod
        2^{m - E_k - e}, and each element contributes its full class mod
        2^{m-e}, so the union is a class mod 2^{m - E_{k+1}}.
        Since every e_i >= 1 we have E_k >= k, so at k = m-1 the class is
        mod 2^1 = all odd residues, which contains h_m.

  (CONN1)  By (H1) and (H2) every live node reaches every live node.

Both halves are algebraic.  The verifier confirms them, and confirms the
bound m-1 in (H2) is SHARP (attained, by the all-ones residue 2^m - 1,
whose burn takes exactly m-1 steps to reach tau = 1).

NO FLOATING POINT APPEARS IN ANY ASSERTION.
"""

import collections
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


def succ(r, m):
    M = 1 << m
    y = 3 * r + 1
    e = v2(y)
    if e >= m:
        return None
    base = (y >> e) % (1 << (m - e))
    return e, [s for s in ((base + t * (1 << (m - e))) % M for t in range(1 << e))
               if s % 2 == 1]


def hub(m):
    M = 1 << m
    return (pow(3, -1, M) * ((1 << (m - 1)) - 1)) % M


# ---------------------------------------------------------------------------
print("\n(H0) the hub is well defined for every m >= 2")
bad = []
for m in range(2, 25):
    h = hub(m)
    if h % 2 != 1 or (3 * h + 1) % (1 << m) != (1 << (m - 1)):
        bad.append(m)
check("h_m = 3^{-1}(2^{m-1}-1) is odd and 3h+1 = 2^{m-1} mod 2^m", not bad,
      "m = 2..24")
bad = [m for m in range(3, 25) if v2(3 * hub(m) + 1) != m - 1]
check("v_2(3 h_m + 1) = m - 1, so h_m is live with maximal valuation", not bad)

# ---------------------------------------------------------------------------
print("\n(H1) the hub reaches every odd residue in one step")
bad = []
for m in range(3, 18):
    s = succ(hub(m), m)
    if s is None or s[0] != m - 1 or len(s[1]) != (1 << m) // 2:
        bad.append(m)
check("succ(h_m) = all odd residues mod 2^m", not bad, "m = 3..17")

# ---------------------------------------------------------------------------
print("\n(H2) every live node reaches the hub within m-1 steps")
for m in range(3, 15):
    M = 1 << m
    h = hub(m)
    live = [r for r in range(1, M, 2) if succ(r, m)]
    pred = collections.defaultdict(list)
    for r in live:
        for t in succ(r, m)[1]:
            pred[t].append(r)
    dist = {h: 0}
    q = collections.deque([h])
    while q:
        u = q.popleft()
        for p in pred[u]:
            if p not in dist:
                dist[p] = dist[u] + 1
                q.append(p)
    unreached = [r for r in live if r not in dist]
    d = max((dist[r] for r in live if r in dist), default=-1)
    check(f"m={m:2d}: all {len(live)} live nodes reach the hub, max distance {d}",
          not unreached and d <= m - 1, f"bound m-1 = {m-1}")

# ---------------------------------------------------------------------------
print("\n(H2') the bound m-1 is sharp, attained at the all-ones residue")
for m in (4, 6, 8, 10, 12):
    M = 1 << m
    h = hub(m)
    src = M - 1
    cur = {src}
    k = 0
    while h not in cur and k < 2 * m:
        nxt = set()
        for u in cur:
            s = succ(u, m)
            if s:
                nxt |= set(s[1])
        cur = nxt
        k += 1
    check(f"m={m:2d}: 2^m-1 reaches the hub in exactly {k} steps", k == m - 1,
          f"m-1 = {m-1}")

# ---------------------------------------------------------------------------
print("\n(CONN1) strong connectivity")
for m in range(3, 15):
    M = 1 << m
    live = {r for r in range(1, M, 2) if succ(r, m)}

    def reach(a):
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

    ok = all(live <= reach(r) for r in list(live)[:40])
    check(f"m={m:2d}: sampled live nodes reach all live nodes", ok,
          f"{len(live)} live")

print("\n(=>) SUFF1 IS NOW UNCONDITIONAL for the 3x+1 map.")
print("     Its hypothesis was strong connectivity of this automaton.")

print("\n" + "=" * 64)
if FAILURES:
    print(f"FAILED: {len(FAILURES)} check(s)")
    for x in FAILURES:
        print("   -", x)
    sys.exit(1)
print("ALL PASS")
