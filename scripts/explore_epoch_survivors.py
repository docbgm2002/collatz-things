#!/usr/bin/env python3
"""
explore_epoch_survivors.py
==========================

Census of multi-epoch survivors and probes for structured families.

Epoch map Phi(x) = T^{len(x)}(x); B = {x : Phi(x) >= x}.  A j-survivor is an
x with x, Phi(x), ..., Phi^{j-1}(x) all in B.

Part 1 (census).  All x < 2^LMAX: the number of j-survivors for each j,
against the independent-miracles prediction (product of length-matched
baseline probabilities along the chain), and the list of champions (largest
j) with their binary expansions and residues.

Part 2 (periodic words = rational-cycle shadows).  For every primitive binary
word u of length <= UMAX with an expanding cycle (3^{#O} > 2^{|u|}) and every
l = r|u| <= 64, the integer x = (least residue of the cycle point mod 2^l)
has parity word u^r.  How many epochs does it survive?  (Expectation: 1, since
the second epoch's word is the binary expansion of 3^k minus a small number.)

Part 3 (epoch-fixed points).  x < 2^LMAX with Phi(x) = x (mod 2^len(x)): the
next epoch repeats the word.  Count them and their survival.

Part 4 (Sturmian words).  Mechanical words with slope alpha in (theta, 1) and
random intercepts, length l: x = Terras inverse; epochs survived.

Everything here is exploratory.  Usage: python3 scripts/explore_epoch_survivors.py --lmax 27
"""

import argparse
import math
import sys
import time
from fractions import Fraction

import numpy as np

THETA = 1 / math.log2(3)


def T(x):
    return x // 2 if x % 2 == 0 else (3 * x + 1) // 2


def epoch_py(x):
    l = x.bit_length()
    y, k = x, 0
    for _ in range(l):
        if y & 1:
            k += 1
            y = (3 * y + 1) // 2
        else:
            y //= 2
    return y, k, l


def survive(x, jmax=40):
    j = 0
    while j < jmax:
        y, k, l = epoch_py(x)
        if y < x:
            return j
        j += 1
        x = y
    return j


def epoch_np_fixed(x, l):
    """vectorised epoch for int64 x all of bit length exactly l (l <= 36)."""
    y = x.copy()
    k = np.zeros_like(x)
    for _ in range(l):
        odd = (y & 1).astype(bool)
        k += odd
        y = np.where(odd, (3 * y + 1) // 2, y // 2)
    return y, k


def baseline_p(L, rng, n=20000):
    if L <= 36:
        x = rng.integers(1 << (L - 1), 1 << L, size=n, dtype=np.int64)
        y, k = epoch_np_fixed(x, L)
        return float(np.mean(y >= x))
    cnt = 0
    m = max(2000, n // 8)
    for _ in range(m):
        x = (1 << (L - 1)) + int.from_bytes(rng.bytes(16), "big") % (1 << (L - 1))
        y, k, l = epoch_py(x)
        cnt += y >= x
    return cnt / m


def terras_inverse(word):
    """least x >= 0 with the given parity word (length l) as x mod 2^l."""
    l = len(word)
    x = 0
    for i in range(l):
        y = x
        for _ in range(i):
            y = T(y)
        if (y & 1) != word[i]:
            x += 1 << i
    return x


def census(lmax, rng):
    print(f"\n== Part 1: census of all x < 2^{lmax} ==", flush=True)
    t0 = time.time()
    counts = {}
    champions = []
    for L in range(2, lmax + 1):
        lo, hi = 1 << (L - 1), 1 << L
        xs = np.arange(lo, hi, dtype=np.int64)
        y, k = epoch_np_fixed(xs, L)
        inB = y >= xs
        s1 = xs[inB]
        counts[L] = {0: len(xs), 1: int(len(s1))}
        cur = [(a, b) for a, b in zip(s1.tolist(), y[inB].tolist()) if b > 2]  # drop the trivial cycle
        j = 1
        while cur and j < 60:
            nxt = []
            for x0, xv in cur:
                yv, kv, lv = epoch_py(xv)
                if yv >= xv and yv > 2:
                    nxt.append((x0, yv))
            j += 1
            counts[L][j] = len(nxt)
            if not nxt:
                break
            if len(nxt) <= 50:
                champions.extend((j, x0, L) for x0, _ in nxt)
            cur = nxt
        print(f"   L={L:2d}: " + " ".join(f"j{jj}={c}" for jj, c in sorted(counts[L].items()) if jj >= 1) + f"   ({time.time()-t0:.0f}s)", flush=True)
    tot = {}
    for L in counts:
        for j, c in counts[L].items():
            tot[j] = tot.get(j, 0) + c
    print("   j   survivors(all L)   ratio N_j/N_{j-1}   predicted ratio (length-matched baseline)", flush=True)
    pcache = {}
    for j in sorted(tot):
        if j == 0:
            continue
        num = den = 0.0
        for L in counts:
            c_prev = counts[L].get(j - 1, 0)
            if c_prev == 0:
                continue
            Lj = int(round(L + 1.8 * (j - 1)))
            if Lj not in pcache:
                pcache[Lj] = baseline_p(Lj, rng)
            num += c_prev * pcache[Lj]
            den += c_prev
        pred = num / den if den else float("nan")
        ratio = tot[j] / tot[j - 1] if tot.get(j - 1) else float("nan")
        print(f"   {j:2d}   {tot[j]:14d}   {ratio:.5f}            {pred:.5f}     (obs/pred {ratio/pred if pred else float('nan'):.3f})", flush=True)
    # champions: keep the best j per x0
    best = {}
    for j, x0, L in champions:
        best[x0] = max(best.get(x0, 0), j)
    top = sorted(best.items(), key=lambda t: (-t[1], t[0]))[:15]
    print(f"   top survivors:", flush=True)
    for x0, j in top:
        print(f"     j={j}  x={x0:>10d}  bits={bin(x0)[2:]}  x mod 9={x0%9}  x mod 64={x0%64}", flush=True)
    return top


def periodic_words(umax):
    print(f"\n== Part 2: periodic words (rational-cycle shadows), |u| <= {umax} ==")
    best = {}
    for n in range(1, umax + 1):
        for bits in range(1 << n):
            u = tuple((bits >> i) & 1 for i in range(n))
            if u[0] != 1:
                continue
            # primitive and expanding
            if any(u == u[i:] + u[:i] for i in range(1, n)):
                continue
            kk = sum(u)
            if 3 ** kk <= 2 ** n:
                continue
            for r in range(1, 64 // n + 1):
                l = n * r
                if l < 4:
                    continue
                x = terras_inverse(u * r)
                if x < (1 << (l - 1)):
                    continue  # not of length l; skip
                s = survive(x)
                key = u
                if s > best.get(key, (0, 0, 0))[0]:
                    best[key] = (s, l, x)
    hist = {}
    for u, (s, l, x) in best.items():
        hist[s] = hist.get(s, 0) + 1
    print(f"   {len(best)} expanding primitive words; max epochs survived by any shadow of length <= 64:")
    print("   epochs -> number of words:", dict(sorted(hist.items())))
    top = sorted(best.items(), key=lambda t: -t[1][0])[:6]
    for u, (s, l, x) in top:
        print(f"     word {''.join('O' if b else 'E' for b in u)} : {s} epochs at l={l}, x={x}")


def epoch_fixed(lmax):
    print(f"\n== Part 3: epoch-fixed points Phi(x) = x mod 2^len(x), x < 2^{lmax} ==")
    found = []
    for L in range(3, lmax + 1):
        xs = np.arange(1 << (L - 1), 1 << L, dtype=np.int64)
        y, k = epoch_np_fixed(xs, L)
        m = (y - xs) % (1 << L) == 0
        for x0 in xs[m].tolist():
            found.append((L, x0, survive(x0), int(y[xs == x0][0] >= x0)))
    print(f"   {found.__len__()} epoch-fixed points; (L, x, epochs survived, in B):")
    for L, x0, s, b in found[:40]:
        print(f"     L={L:2d} x={x0:>10d} bits={bin(x0)[2:]:>28s} survived={s} inB={b}")


def sturmian(rng, n_words=400):
    print("\n== Part 4: Sturmian (mechanical) words with slope in (theta, 1) ==")
    hist = {}
    best = (0, None)
    for _ in range(n_words):
        l = int(rng.integers(20, 40))
        alpha = THETA + (1 - THETA) * rng.random()
        rho = rng.random()
        w = tuple(int(math.floor((i + 1) * alpha + rho) - math.floor(i * alpha + rho)) for i in range(l))
        x = terras_inverse(w)
        if x < (1 << (l - 1)):
            x += 1 << (l - 1)  # force length l (changes only bit l-1, which affects no first-l letters? it does: skip)
            continue
        s = survive(x)
        hist[s] = hist.get(s, 0) + 1
        if s > best[0]:
            best = (s, (alpha, rho, l, x))
    print("   epochs survived -> count:", dict(sorted(hist.items())))
    print("   best:", best)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lmax", type=int, default=27)
    ap.add_argument("--umax", type=int, default=9)
    ap.add_argument("--parts", default="1234")
    args = ap.parse_args()
    rng = np.random.default_rng(3)
    if "1" in args.parts:
        census(args.lmax, rng)
    if "2" in args.parts:
        periodic_words(args.umax)
    if "3" in args.parts:
        epoch_fixed(min(args.lmax, 24))
    if "4" in args.parts:
        sturmian(rng)


if __name__ == "__main__":
    main()
