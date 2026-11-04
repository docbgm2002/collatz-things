#!/usr/bin/env python3
"""
explore_epoch_bias.py
=====================

Bias propagation across epochs of the 3x+1 map.

Epoch map: Phi(x) = T^{len(x)}(x), i.e. apply T exactly as many times as x
has bits.  Exact identity (checked here): Phi(x) = (3^k x + c)/2^l with k the
number of odd letters among the first l letters of the parity word of x, and
Phi(x) in {rho, rho + 3^k} where rho = c 2^{-l} mod 3^k.  Descent in an
epoch iff k/l < 1/log2 3.

Let B = {x : Phi(x) >= x} (no descent in one epoch).  The "memoryless"
hypothesis says: conditional on the LENGTH of Phi(x), the event Phi(x) in B is
independent of x in B, to all orders.  This script measures

  (1) the baseline p(L) = P(x in B | len(x) = L) for a range of L;
  (2) for chains x_0 = x, x_{i+1} = Phi(x_i): the conditional probability
      P(x_j in B | x_0..x_{j-1} in B) against the length-matched prediction
      mean_j p(len(x_j)), for j = 1..J;
  (3) the correlation of the continuous bias k/l - theta between consecutive
      epochs, overall and conditional on the input bias.

Exploratory: finite sampling evidence only.  Usage:
    python3 scripts/explore_epoch_bias.py --l 32 --n 20000000 --J 5
"""

import argparse
import math
import sys
import time

import numpy as np

THETA = 1 / math.log2(3)


def epoch_np(x):
    """Vectorised epoch for int64 x with len(x) <= 36 (values stay < 2^63)."""
    l = np.ceil(np.log2(x.astype(np.float64) + 0.5)).astype(np.int64)
    # exact bit length
    l = np.array([int(v).bit_length() for v in x], dtype=np.int64) if len(x) < 1000 else l
    # correct l exactly via comparison (float log2 may be off by one near powers of 2)
    l = np.where(x >= (1 << np.minimum(l, 62)), l + 1, l)
    l = np.where((l > 0) & (x < (1 << np.maximum(l - 1, 0))), l - 1, l)
    y = x.copy()
    k = np.zeros_like(x)
    steps = int(l.max())
    for i in range(steps):
        active = i < l
        odd = (y & 1).astype(bool) & active
        k += odd
        y = np.where(active, np.where(odd, (3 * y + 1) // 2, y // 2), y)
    return y, k, l


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


def baseline(rng, Ls, n_per):
    p = {}
    for L in Ls:
        if L <= 36:
            x = rng.integers(1 << (L - 1), 1 << L, size=n_per, dtype=np.int64)
            y, k, l = epoch_np(x)
            p[L] = float(np.mean(y >= x))
        else:
            cnt = 0
            for _ in range(n_per // 4):
                x = int(rng.integers(1 << (L - 1), 1 << L, dtype=np.int64)) if L <= 62 else (1 << (L - 1)) + int.from_bytes(rng.bytes(16), "big") % (1 << (L - 1))
                y, k, l = epoch_py(x)
                cnt += y >= x
            p[L] = cnt / (n_per // 4)
    return p


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--l", type=int, default=32)
    ap.add_argument("--n", type=int, default=20_000_000)
    ap.add_argument("--J", type=int, default=5)
    ap.add_argument("--seed", type=int, default=1)
    args = ap.parse_args()
    rng = np.random.default_rng(args.seed)
    L0 = args.l
    t0 = time.time()

    # identity check on a small sample
    for _ in range(2000):
        l = int(rng.integers(8, 60))
        x = (1 << (l - 1)) + int(rng.integers(0, 1 << (l - 1)))
        y, k, _ = epoch_py(x)
        c = y * 2 ** l - 3 ** k * x
        assert c >= 0 and 2 * y >= 3 ** k and 2 * y < 3 * 3 ** k and (y - c * pow(2, -l, 3 ** k)) % 3 ** k == 0
    print("epoch identity: PASS (2000 random x, 8..59 bits)")

    # (1) baseline p(L)
    Ls = list(range(max(8, L0 - 8), int(1.6 * L0) + 24))
    p = baseline(rng, Ls, 40000)
    print("baseline p(L) = P(no descent in one epoch | length L):")
    print("   " + "  ".join(f"{L}:{p[L]:.4f}" for L in Ls if L % 4 == 0))

    # (2) chains
    x = rng.integers(1 << (L0 - 1), 1 << L0, size=args.n, dtype=np.int64)
    y, k, l = epoch_np(x)
    bias0 = k / l - THETA
    inB = y >= x
    print(f"\nl={L0}, n={args.n}: P(x in B) = {inB.mean():.5f}  ({time.time()-t0:.0f}s)")
    # (3) continuous bias memory over the whole sample (second epoch on a subsample, python ints)
    sub = rng.choice(args.n, size=min(200000, args.n), replace=False)
    b1 = np.empty(len(sub))
    for idx, i in enumerate(sub):
        y1, k1, l1 = epoch_py(int(y[i]))
        b1[idx] = k1 / l1 - THETA
    b0s = bias0[sub]
    r = np.corrcoef(b0s, b1)[0, 1]
    print(f"correlation of consecutive epoch biases (k/l - theta): r = {r:+.4f}  (n={len(sub)})")
    qs = np.quantile(b0s, [0, .2, .4, .6, .8, .9, .97, 1.0])
    print("   input-bias bin          mean output bias   P(output in B)")
    for a, b in zip(qs[:-1], qs[1:]):
        m = (b0s >= a) & (b0s <= b)
        if m.sum() == 0:
            continue
        print(f"   [{a:+.3f},{b:+.3f}]  n={m.sum():6d}   {b1[m].mean():+.4f}          {(b1[m] > 0).mean():.4f}")

    # survivors chain
    surv = np.flatnonzero(inB)
    cur = [int(v) for v in y[surv]]  # x_1 for survivors of epoch 0
    print(f"\nchain statistics (survivors of j consecutive non-descending epochs):")
    print(f"   j=0: survivors {len(cur)}")
    for j in range(1, args.J + 1):
        nxt = []
        pred = []
        hits = 0
        lens = []
        for xv in cur:
            yv, kv, lv = epoch_py(xv)
            lens.append(lv)
            # length-matched prediction uses baseline p at len(x_j) = lv
            pL = p.get(lv)
            if pL is None:
                pL = baseline(rng, [lv], 4000)[lv]
                p[lv] = pL
            pred.append(pL)
            if yv >= xv:
                hits += 1
                nxt.append(yv)
        if not cur:
            break
        obs = hits / len(cur)
        exp = float(np.mean(pred))
        print(f"   j={j}: tested {len(cur):8d}  mean length {np.mean(lens):6.1f}  observed P(B | survived {j}) = {obs:.5f}   length-matched independent prediction = {exp:.5f}   ratio {obs/exp if exp else float('nan'):.3f}   survivors {hits}")
        cur = nxt
        if len(cur) < 30:
            break
    print(f"\ndone in {time.time()-t0:.0f}s")




# ---------------------------------------------------------------------------
# importance sampling: uniform samples of B at a fixed length via Terras inversion
# ---------------------------------------------------------------------------

def sample_B(rng, L, n, chunk=500000):
    """n uniform samples of {x in [2^(L-1), 2^L): word has >= k* odd letters},
    k* = least k with 3^k > 2^L (vectorised Terras inversion, chunked)."""
    kstar = 0
    while 3 ** kstar <= 2 ** L:
        kstar += 1
    from math import comb
    ks = np.arange(kstar, L + 1)
    w = np.array([comb(L, int(k)) for k in ks], dtype=np.float64)
    w /= w.sum()
    out = []
    got = 0
    while got < n:
        m = chunk
        kk = rng.choice(ks, size=m, p=w)
        keys = rng.random((m, L), dtype=np.float32)
        order = np.argsort(keys, axis=1)
        del keys
        words = np.zeros((m, L), dtype=np.int8)
        rows = np.arange(m)[:, None]
        mask = np.arange(L)[None, :] < kk[:, None]
        words[rows, order] = mask.astype(np.int8)
        del order, mask
        x = np.zeros(m, dtype=np.int64)
        for i in range(L):
            y = x.copy()
            for _ in range(i):
                odd = (y & 1).astype(bool)
                y = np.where(odd, (3 * y + 1) // 2, y // 2)
            x = x + (((y & 1) != words[:, i]).astype(np.int64) << i)
        x = x[x >= (1 << (L - 1))]
        out.append(x)
        got += len(x)
    return np.concatenate(out)[:n]


def chain_from_B(L, n, J, seed):
    rng = np.random.default_rng(seed)
    t0 = time.time()
    x = sample_B(rng, L, n)
    print(f"\n[importance] {len(x)} uniform samples of B at length {L} ({time.time()-t0:.0f}s)")
    y, k, l = epoch_np(x)
    inB = y >= x
    print(f"   exact check: fraction with Phi(x) >= x among word-sampled B = {inB.mean():.5f}")
    Ls = list(range(L - 4, int(2.0 * L) + 10))
    p = baseline(rng, Ls, 20000)
    cur = [int(v) for v in y[inB]]
    print(f"   j=0: survivors {len(cur)}")
    for j in range(1, J + 1):
        nxt, pred, lens, hits = [], [], [], 0
        for xv in cur:
            yv, kv, lv = epoch_py(xv)
            lens.append(lv)
            pL = p.get(lv)
            if pL is None:
                pL = baseline(rng, [lv], 4000)[lv]
                p[lv] = pL
            pred.append(pL)
            if yv >= xv:
                hits += 1
                nxt.append(yv)
        obs = hits / len(cur)
        exp = float(np.mean(pred))
        se = math.sqrt(obs * (1 - obs) / len(cur)) if len(cur) else 0
        print(f"   j={j}: tested {len(cur):8d}  mean length {np.mean(lens):6.1f}  observed {obs:.5f} +- {se:.5f}   length-matched prediction {exp:.5f}   ratio {obs/exp:.3f}   survivors {hits}   ({time.time()-t0:.0f}s)")
        cur = nxt
        if len(cur) < 30:
            break


if __name__ == "__main__" and "--importance" in sys.argv:
    L = int(sys.argv[sys.argv.index("--l") + 1]) if "--l" in sys.argv else 32
    n = int(sys.argv[sys.argv.index("--n") + 1]) if "--n" in sys.argv else 2000000
    J = int(sys.argv[sys.argv.index("--J") + 1]) if "--J" in sys.argv else 6
    chain_from_B(L, n, J, 2)
    sys.exit(0)

if __name__ == "__main__":
    main()
