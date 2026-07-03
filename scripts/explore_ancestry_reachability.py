"""Reachability diagnostics for the q=2 smallest-shell ancestry condition.

Companion to `primitive_ancestry_lemma.md` (Sections 8-14). For a source
valuation word e (positive parts, length i, total u),

    A_i(e) = -3^i + 2 * sum_{s<i} 3^{i-1-s} 2^{Q_s},   Q_s = sum of first s parts.

The q=2 smallest-shell high target with a length-j high prefix of total u is

    C = 3 * A_j(highword) + 2^{u+2}.

Reachability of the virtual partner requires A_i == C (plus exponent-prefix
congruences not modelled here), with i in [j+2, u], i == j+1 (mod 2).

Two experiments:
  * sieve   : Monte-Carlo survival fraction of the necessary congruence
              A_i == C (mod 3^r) for r = 1..8.
  * exact   : exhaustive count of true A_i == C solutions for small u.

Diagnostic only. The mod-3^r test is necessary, not sufficient; the exact
pass is exhaustive only over the stated u range. Reproduce:

    python explore_ancestry_reachability.py
"""
import random
from collections import Counter


def A_of(word):
    i = len(word)
    A = -3 ** i
    Q = 0
    for s in range(i):
        A += 2 * (3 ** (i - 1 - s)) * (2 ** Q)
        Q += word[s]
    return A


def C_of(highword, u):
    return 3 * A_of(highword) + 2 ** (u + 2)


def rand_comp(u, parts, rng):
    cuts = sorted(rng.sample(range(1, u), parts - 1))
    prev = 0
    out = []
    for c in cuts:
        out.append(c - prev)
        prev = c
    out.append(u - prev)
    return out


def sieve(u=24, j=4, i=9, N=300000, seed=1):
    assert i >= j + 2 and i <= u and (i % 2) == ((j + 1) % 2)
    rng = random.Random(seed)
    hits = [0] * 9
    for _ in range(N):
        C = C_of(rand_comp(u, j, rng), u)
        diff = A_of(rand_comp(u, i, rng)) - C
        for r in range(1, 9):
            if diff % (3 ** r) == 0:
                hits[r] += 1
            else:
                break
    print(f"[sieve] u={u}, j={j}, i={i}, samples={N}")
    print(" r   survivors   frac        ratio_vs_prev   (uniform=1/3)")
    prev = N
    for r in range(1, 9):
        h = hits[r]
        print(f" {r}   {h:9d}   {h/N:.6f}    {(h/prev if prev else 0):.4f}")
        prev = h if h else 1


def comps(u, parts):
    if parts == 1:
        yield (u,)
        return
    for first in range(1, u - parts + 2):
        for rest in comps(u - first, parts - 1):
            yield (first,) + rest


def exact(u_lo=8, u_hi=18):
    print("\n[exact] u  j  i   pairs    exact_reachable   reach_rate")
    for u in range(u_lo, u_hi + 1, 2):
        for j in range(2, 5):
            hws = list(comps(u, j))
            Cs = [3 * A_of(h) + 2 ** (u + 2) for h in hws]
            for i in range(j + 2, u + 1):
                if (i % 2) != ((j + 1) % 2):
                    continue
                cnt = Counter(A_of(s) for s in comps(u, i))
                pairs = len(hws) * sum(cnt.values())
                exactpairs = sum(cnt.get(C, 0) for C in Cs)
                print(f"        {u:2d} {j:2d} {i:2d} {pairs:8d}   {exactpairs:6d}"
                      f"            {(exactpairs/pairs if pairs else 0):.2e}")


if __name__ == "__main__":
    sieve()
    exact()
