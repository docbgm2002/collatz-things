"""Reachability diagnostics for the q=2 smallest-shell ancestry condition.

Companion to `primitive_ancestry_lemma.md` (Sections 8-14). For a source
valuation word e (positive parts, length i, total u),

    A_i(e) = -3^i + 2 * sum_{s<i} 3^{i-1-s} 2^{Q_s},   Q_s = sum of first s parts.

The q=2 smallest-shell high target with a length-j high prefix of total u is

    C = 3 * A_j(highword) + 2^{u+2}.

For a high word realised by an odd repunit exponent, A_i == C at an
admissible positive source index is exactly the reachability condition; see
the automatic-realisation lemma in Section 9A. This abstract diagnostic does
not filter high words by repunit realisability or impose the n-dependent
positivity bound i < d. It uses i in [j+2, u], i == j+1 (mod 2).

Two experiments:
  * sieve   : Monte-Carlo survival fraction of the necessary congruence
              A_i == C (mod 3^r) for r = 1..8.
  * exact   : exhaustive count of true A_i == C solutions for small u.

Diagnostic only. The mod-3^r test is necessary, not sufficient; the exact
correction-match pass is exhaustive only over the stated u range. Reproduce:

    python explore_ancestry_reachability.py
"""
import random
from collections import Counter
from functools import lru_cache


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


def c_of(word):
    return (A_of(word) + 3 ** len(word)) // 2


def starting_residue(word):
    total = sum(word)
    modulus = 1 << (total + 1)
    return (
        ((1 << total) - c_of(word))
        * pow(3 ** len(word), -1, modulus)
        % modulus
    )


@lru_cache(maxsize=None)
def power_log_table(total):
    modulus = 1 << (total + 2)
    order = 1 << total
    table = {}
    value = 1
    for exponent in range(order):
        table[value] = exponent
        value = value * 3 % modulus
    return table, order


def least_odd_repunit_exponent(word):
    total = sum(word)
    target = (2 * starting_residue(word) + 1) % (1 << (total + 2))
    table, _ = power_log_table(total)
    exponent = table.get(target)
    if exponent is None or exponent % 2 == 0:
        return None
    return exponent


def exact(u_lo=8, u_hi=18):
    print("\n[exact] u  j  i   pairs    correction_matches   match_rate")
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


def cylinder_correlation(u_lo=8, u_hi=18):
    """Test the unqualified nonmembership -> large representative heuristic.

    This intentionally omits primitivity, record-deficit, and dominance. It
    asks whether correction nonmembership alone pushes the already-fixed high
    word cylinder to a large least odd exponent representative.
    """
    print("\n[cylinders] u  j  realised  matched  min_n0(nonmatch)  median_n0(nonmatch)")
    for u in range(u_lo, u_hi + 1, 2):
        layers = {
            i: {A_of(word) for word in comps(u, i)}
            for i in range(1, u + 1)
        }
        for j in range(2, 5):
            reachable = set()
            for i in range(j + 2, u + 1):
                if i % 2 == (j + 1) % 2:
                    reachable.update(layers[i])

            matched = []
            unmatched = []
            for high in comps(u, j):
                n0 = least_odd_repunit_exponent(high + (2,))
                if n0 is None:
                    continue
                C = C_of(high, u)
                (matched if C in reachable else unmatched).append(n0)

            unmatched.sort()
            median = unmatched[len(unmatched) // 2] if unmatched else None
            print(
                f"            {u:2d} {j:2d} {len(matched)+len(unmatched):8d}"
                f" {len(matched):8d} {str(unmatched[0] if unmatched else None):>17}"
                f" {str(median):>20}"
            )


if __name__ == "__main__":
    sieve()
    exact()
    cylinder_correlation()
