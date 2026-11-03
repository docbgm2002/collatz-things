#!/usr/bin/env python3
"""
verify_quantized_log_theorem.py
===============================

Exact-integer verification of manuscript Theorem E (the quantized
logarithm is excluded at every precision) and of the two corollaries that
extend Theorems A, B and F to arbitrary moduli and to multi-step
potentials.  No floating point appears in any assertion; floats are used
only to choose a starting height.

What is checked
---------------

(R)  Rational-cycle lemma.  For every valuation word (e_1..e_K) with
     e_i >= 1 and E = sum e_i, the rational number
         y_1 = sum_i 3^(K-i) 2^(E_{i-1}) / (2^E - 3^K)
     is a 2-adic integer whose orbit under f is purely periodic with
     exactly that valuation word (every member is a 2-adic unit).  Checked
     for every word with K <= 7 and e_i <= 4.

(E)  Theorem E construction.  For each (j, m, N, d, K) in a grid, with
     Q = 2^j and K admissible at Q, the script builds K odd integers
     x_1..x_K by shadowing the rational cycle of the word
     (2,1)^p (3,1,1)^r  [p = 5K-3E, r = 2E-3K]  (or a {1,2}-word when
     d = 0 and 2E < 3K), chooses in-cell positions so that exactly s carries
     occur, and verifies exactly:
       - v_2(3 x_i + 1) = e_i;
       - cell(f(x_i)) = cell(x_{i+1}), where cell(x) = floor(Q log_2 x)
         = bitlength(x^Q) - 1;
       - tau(f(x_i)) = tau(x_{i+1});
       - f(x_i) = x_{i+1} (mod N), N an arbitrary modulus: the 2- and 3-parts
         are handled by congruence to the rational cycle members, which are
         2-adic and 3-adic integers; for the prime-to-6 part q' the cycle is
         traversed t times, t the order of the affine map
         rho -> (3^K rho + c) 2^(-E) on Z/q';
       - lambda_d'(f(x_i)) = lambda_d'(x_{i+1}) = bottom for d' <= d;
       - prod f(x_i) > prod x_i.
     Summing the K monotonicity constraints then contradicts any
     nonincreasing  log_2 x + g(cell, tau, x mod N, lambda_1..lambda_d).

(C)  Cost law.  K_min(Q) for Q = 2^j, j = 0..20, and the facts that K = Q
     is admissible and that admissibility is equivalent to
     floor(K b)/K >= floor(Q b)/Q, b = log_2 3.

(M)  Modulus corollary for Theorems A/B.  For odd q with 3 | q or not: on
     x = -5 (mod 2^N) the 2a-step shadow walk satisfies f^{2a}(x) = x
     (mod q) for every such x, once a is a multiple of ord_{q'}(9/8) and
     2a >= v_3(q), where x = -5 (mod 3^{v_3(q)}).

(S)  Multi-step corollary.  (i) For Theorem B's class: for k = 1..6 and
     j = 2, an index a divisible by k with ||a log_2(9/8)|| < 2^{-j-3}
     exists (Dirichlet on k*beta), and the 2a-step shadow walk closes
     LD_j, residues, tau and detectors with value gain > 1.  (ii) For
     Theorem E's class: certificates whose edges are k-step orbit segments,
     k = 2, 3, 5, built by the same recipe with K_0 = Q segments.

Run:  python3 scripts/verify_quantized_log_theorem.py [--quick]
"""

import argparse
import math
import sys
from fractions import Fraction
from itertools import product

FAIL = []


def check(name, cond, detail=""):
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ""))
    if not cond:
        FAIL.append(name)


# ---------------------------------------------------------------------------
# basic arithmetic
# ---------------------------------------------------------------------------

def v2(n):
    if isinstance(n, Fraction):
        assert n.denominator % 2 == 1
        n = n.numerator
    if n == 0:
        raise ValueError
    return (n & -n).bit_length() - 1


def f(x):
    y = 3 * x + 1
    return y >> v2(y)


def f_steps(x, k):
    for _ in range(k):
        x = f(x)
    return x


def tau(x):
    return v2(x + 1)


def bitlen(x):
    return x.bit_length()


def LD(j, x):
    return x >> (bitlen(x) - j)


def cell(Q, x):
    """floor(Q log_2 x) exactly."""
    return bitlen(x ** Q) - 1


def Lq(Q):
    return bitlen(3 ** Q) - 1


def EK(K):
    return bitlen(3 ** K) - 1


def slack(Q, K):
    return EK(K) * Q - K * Lq(Q)


def admissible(Q, K):
    return slack(Q, K) >= 0


def iroot(n, k):
    """floor(n^(1/k)) for n >= 0."""
    if n < 2:
        return n
    lo, hi = 0, 1 << (bitlen(n) // k + 1)
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if mid ** k <= n:
            lo = mid
        else:
            hi = mid - 1
    return lo


def cell_bottom(Q, c):
    """least integer x with cell(Q, x) = c, i.e. x^Q >= 2^c."""
    r = iroot(1 << c, Q)
    if r ** Q < (1 << c):
        r += 1
    assert cell(Q, r) == c and (r == 1 or cell(Q, r - 1) < c)
    return r


def carry_threshold(Q, c):
    """least x in cell c with theta >= 1 - phi_Q, i.e. (3x)^Q >= 2^(c+1+L_Q)."""
    target = 1 << (c + 1 + Lq(Q))
    r = iroot(target, Q)  # floor((2^target)^(1/Q))
    x = r // 3
    while (3 * x) ** Q < target:
        x += 1
    return x


def crt(residues):
    """residues: list of (r, mod) with pairwise coprime moduli."""
    R, M = 0, 1
    for r, m in residues:
        # solve R + M t = r (mod m)
        t = ((r - R) * pow(M, -1, m)) % m
        R, M = R + M * t, M * m
    return R % M, M


def w_d(d, M):
    num = 2 ** (M + 2 * d) - 2 ** (2 * d + 1) + 3 ** d
    assert num % 3 ** d == 0
    return num // 3 ** d


def lam(d, x, smax=30):
    """Level-d detector of the manuscript (Definition of the detectors)."""
    o = 2 * 3 ** (d - 1)
    best = None
    for s in range(1, smax + 1):
        T = w_d(d, 1 + o * s)
        mod = 1 << (bitlen(T) + 1)
        if x % mod == T % mod:
            best = s
    return best


# ---------------------------------------------------------------------------
# (R) rational cycles for every valuation word
# ---------------------------------------------------------------------------

def rational_cycle(word):
    K, E = len(word), sum(word)
    Epre = [0]
    for e in word:
        Epre.append(Epre[-1] + e)
    num = sum(3 ** (K - 1 - i) * 2 ** Epre[i] for i in range(K))
    y = Fraction(num, 2 ** E - 3 ** K)
    ys = [y]
    for e in word:
        t = 3 * ys[-1] + 1
        if t == 0 or v2(t) != e:
            return None
        ys.append(t / 2 ** e)
    if ys[-1] != ys[0]:
        return None
    return ys[:-1]


def check_rational_cycles(Kmax=7, emax=4):
    print("\n(R) every valuation word is the exact word of a rational 2-adic cycle")
    n = 0
    ok = True
    for K in range(1, Kmax + 1):
        for word in product(range(1, emax + 1), repeat=K):
            ys = rational_cycle(word)
            if ys is None:
                ok = False
                print("    counterexample word", word)
                break
            for y in ys:
                if y.denominator % 2 == 0 or y.numerator % 2 == 0:
                    ok = False
            n += 1
        if not ok:
            break
    check(f"rational cycle with exact word for all {n} words, K <= {Kmax}, e <= {emax}", ok)
    c = rational_cycle((1, 2))
    check("word (1,2) gives the cycle -5 -> -7", c == [Fraction(-5), Fraction(-7)])
    c = rational_cycle((2,) * 1)
    check("word (2) gives the fixed point 1", c == [Fraction(1)])


# ---------------------------------------------------------------------------
# (E) Theorem E construction
# ---------------------------------------------------------------------------

def choose_word(K, E, detectors):
    """Word of length K, sum E.  With detectors: (2,1)^p (3,1,1)^r, which
    avoids the factors (2,2) and (2,1,1) and hence the residues 1, 9 mod 32
    on every cycle member.  Without: any {1,2}-word."""
    if 2 * E >= 3 * K and E <= 5 * K // 3 + 1:
        p, r = 5 * K - 3 * E, 2 * E - 3 * K
        if p >= 0 and r >= 0:
            return [2, 1] * p + [3, 1, 1] * r
    if detectors:
        return None
    assert K <= E <= 2 * K
    ones, twos = 2 * K - E, E - K
    w = []
    while ones or twos:
        if twos:
            w.append(2)
            twos -= 1
        if ones:
            w.append(1)
            ones -= 1
    return w


def split_modulus(N):
    m = v2(N) if N > 1 else 0
    N >>= m
    u = 0
    while N % 3 == 0:
        N //= 3
        u += 1
    return m, u, N  # N is now the prime-to-6 part


def build_certificate(j, m, N, d, K, k=1, verbose=False):
    """Return (witnesses, word, t) for a closed k-step certificate of
    K_0 = K segments (k=1: K witnesses) in the coordinate
    (floor(2^j log2 x), tau, x mod N, lambda_1..lambda_d), or raise."""
    Q = 1 << j
    L = Lq(Q)
    # k-step closure criterion: s = Q*E - K0*floor(k Q beta), E = floor(k K0 beta)
    K0 = K
    Kfull = k * K0
    E = EK(Kfull)
    LkQ = Lq(k * Q) if k > 1 else L  # floor(kQ log2 3)
    s = Q * E - K0 * LkQ
    if not (0 <= s <= K0):
        raise ValueError(f"K0={K0} not admissible for k={k}, j={j}: s={s}")
    word = choose_word(Kfull, E, d > 0)
    if word is None:
        raise ValueError("no detector-safe word")
    ys = rational_cycle(tuple(word))
    assert ys is not None
    taus = [tau(y) for y in ys]  # tau of a 2-adic unit rational: v2(num+den)
    tmax = max(taus)
    m2, u3, qp = split_modulus(N)
    Mp = max(m2, 5, tmax + 1) + E  # 2-adic witness modulus 2^Mp
    # segment valuations
    seg_E = [sum(word[i * k:(i + 1) * k]) for i in range(K0)]
    # prime-to-6 part: residues rho_i along the full word, repeated t times
    if qp > 1:
        rho = [1]
        for e in word:
            rho.append(((3 * rho[-1] + 1) * pow(2, -e, qp)) % qp)
        # order of the affine K-step map on rho_1
        t = 1
        r = rho[-1]
        while r != rho[0]:
            # apply the full word again
            for e in word:
                r = ((3 * r + 1) * pow(2, -e, qp)) % qp
            t += 1
        # extend rho to t traversals
        full = [rho[0]]
        for _ in range(t):
            for e in word:
                full.append(((3 * full[-1] + 1) * pow(2, -e, qp)) % qp)
        assert full[-1] == full[0]
        rho = full
    else:
        t = 1
        rho = None
    n_seg = t * K0
    # choose carries: s per traversal, on the first s segments of each traversal
    deltas = []
    for _ in range(t):
        deltas += [1] * s + [0] * (K0 - s)
    # height: enough room for a full class modulo R = 2^Mp 3^u q' inside the
    # narrower of the two in-cell sub-intervals (floats for guidance only)
    R = (1 << Mp) * 3 ** u3 * qp
    phi = {}
    beta = math.log2(3)
    phi_k = (k * Q * beta) % 1.0
    ell = min(phi_k, 1 - phi_k) / 2
    dip = sum(max(0, Q * e - LkQ + 1) for e in seg_E) * t  # crude lower bound on the dip
    H = Q * (bitlen(R) + j + 4 + int(math.ceil(math.log2(1 / ell)))) + dip
    c = [H]
    xs = []
    for i in range(n_seg):
        seg = i % K0
        e_seg = seg_E[seg]
        word_seg = word[seg * k:(seg + 1) * k]
        y0 = ys[seg * k]  # cycle member at the segment start
        r2 = (y0.numerator * pow(y0.denominator, -1, 1 << Mp)) % (1 << Mp)
        res = [(r2, 1 << Mp)]
        if u3:
            # the cycle members are 3-adic integers: 2^E - 3^K is prime to 3
            r3 = (y0.numerator * pow(y0.denominator, -1, 3 ** u3)) % 3 ** u3
            res.append((r3, 3 ** u3))
        if qp > 1:
            res.append((rho[i * k], qp))
        r, Rm = crt(res)
        assert Rm == R
        ci = c[-1]
        want = ci + LkQ - Q * e_seg + deltas[i]
        if deltas[i] == 0:
            start = cell_bottom(Q, ci)
        else:
            start = carry_threshold(Q, ci)
        x = start + ((r - start) % Rm)
        tries = 0
        while True:
            assert cell(Q, x) == ci, "height too small"
            # valuations along the segment
            z, ok = x, True
            for e in word_seg:
                if v2(3 * z + 1) != e:
                    ok = False
                    break
                z = f(z)
            if ok and cell(Q, z) == want:
                break
            x += Rm
            tries += 1
            assert tries < 64, "sub-interval too narrow at this height"
        xs.append(x)
        c.append(want)
    assert c[-1] == c[0], (c[0], c[-1])
    return xs, word, t, Mp


def verify_certificate(j, m, N, d, xs, k=1):
    Q = 1 << j
    n = len(xs)
    ok = True
    gain_num, gain_den = 1, 1
    for i, x in enumerate(xs):
        y = f_steps(x, k)
        xn = xs[(i + 1) % n]
        if cell(Q, y) != cell(Q, xn):
            ok = False
        if tau(y) != tau(xn):
            ok = False
        if (y - xn) % N != 0:
            ok = False
        for dd in range(1, d + 1):
            if lam(dd, y) is not None or lam(dd, xn) is not None:
                ok = False
        if x % 2 == 0 or x <= 1:
            ok = False
        gain_num *= y
        gain_den *= x
    return ok and gain_num > gain_den


def check_theorem_F(quick):
    print("\n(E) Theorem E: closed certificates in (floor(2^j log2 x), tau, x mod N, lambda_1..d)")
    grid = []
    js = [0, 1, 2, 3, 4, 5, 6] if quick else [0, 1, 2, 3, 4, 5, 6, 7, 8]
    for j in js:
        Q = 1 << j
        Ks = sorted({min(K for K in range(2, 2 * Q + 2) if admissible(Q, K) and 2 * EK(K) >= 3 * K),
                     max(Q, 2)})
        for K in Ks:
            for (m, N, d) in [(4, 16, 0), (16, 1 << 16, 3), (0, 9, 2), (0, 7, 1), (5, 32 * 9 * 35, 3)]:
                # the composite modulus needs up to 12 traversals; cap its precision
                if (m, N, d) == (5, 32 * 9 * 35, 3) and j > (4 if quick else 6):
                    continue
                grid.append((j, m, N, d, K))
    nbits_max = 0
    theta_ok = True
    for (j, m, N, d, K) in grid:
        xs, word, t, Mp = build_certificate(j, m, N, d, K)
        good = verify_certificate(j, m, N, d, xs)
        nbits = max(bitlen(x) for x in xs)
        nbits_max = max(nbits_max, nbits)
        # the bit-length bound Theta of Theorem E (floats for the bound only)
        Q = 1 << j
        m2, u3, qp = split_modulus(N)
        phi = (Q * math.log2(3)) % 1.0
        theta = m2 + math.log2(3 ** u3 * qp) + 6 * t * K + j + math.log2(1 / min(phi, 1 - phi)) + 10
        if nbits > theta:
            theta_ok = False
        check(f"j={j} K={K} N={N} d={d}: {len(xs)} witnesses ({t} traversal{'s' if t>1 else ''}), {nbits} bits",
              good, f"Theta={theta:.0f}")
    check("every certificate above respects the bit-length bound Theta of Theorem E", theta_ok)
    # the published small instances
    print("  explicit instances:")
    xs = [4123, 5817]
    check("(j,m)=(3,16): 4123 -> 6185, 5817 -> 4363 closes with gain 26985155/23983491",
          verify_certificate(3, 4, 16, 0, xs) and f(4123) == 6185 and f(5817) == 4363
          and 6185 * 4363 == 26985155 and 4123 * 5817 == 23983491)
    # the 2^n + 27 family at (j,m,K) = (3,16,2): partner is least x = 9 mod 16 in
    # the non-carrying part of cell(f(x_1))
    fam_ok = True
    for n in list(range(10, 40)) + [60, 100]:
        x1 = (1 << n) + 27
        y1 = f(x1)
        c2 = cell(8, y1)
        x2 = cell_bottom(8, c2)
        x2 += (9 - x2) % 16
        while cell(8, x2) == c2 and not verify_certificate(3, 4, 16, 0, [x1, x2]):
            x2 += 16
        if cell(8, x2) != c2:
            fam_ok = False
    check("family x_1 = 2^n + 27 (n = 10..39, 60, 100) with its mod-16 partner closes at (j,m)=(3,16)",
          fam_ok)


# ---------------------------------------------------------------------------
# (C) cost law
# ---------------------------------------------------------------------------

def check_cost_law():
    print("\n(C) admissibility and the cost of precision")
    table = []
    ok_equiv, ok_Q = True, True
    JMAX = 14
    # incremental powers of 3: E_K = bitlength(3^K) - 1
    Es = [0]
    p3 = 1
    for K in range(1, (1 << JMAX) + 1):
        p3 *= 3
        Es.append(bitlen(p3) - 1)
    for j in range(0, JMAX + 1):
        Q = 1 << j
        Lj = Es[Q]
        Kmin = None
        for K in range(1, Q + 1):
            sK = Es[K] * Q - K * Lj
            a = sK >= 0
            b = Fraction(Es[K], K) >= Fraction(Lj, Q)
            if a != b or sK > K:
                ok_equiv = False
            if a and Kmin is None:
                Kmin = K
        if Es[Q] * Q - Q * Lj != 0:
            ok_Q = False
        table.append((j, Kmin))
    check(f"admissible <=> floor(K b)/K >= floor(Q b)/Q, and s <= K, all K <= Q, j <= {JMAX}", ok_equiv)
    check(f"K = Q is admissible (s = 0) for every j <= {JMAX}", ok_Q)
    print(f"    K_min(2^j), j = 0..{JMAX}:", [Kmin for _, Kmin in table])
    check("K_min sequence begins 1,2,2,2,7,7,12,12,12,53,665",
          [Kmin for _, Kmin in table][:11] == [1, 2, 2, 2, 7, 7, 12, 12, 12, 53, 665])


# ---------------------------------------------------------------------------
# (M) modulus corollary for the single-orbit shadow
# ---------------------------------------------------------------------------

def mult_order(g, q):
    if q == 1:
        return 1
    assert math.gcd(g, q) == 1
    t, x = 1, g % q
    while x != 1:
        x = (x * g) % q
        t += 1
    return t


def check_modulus_corollary():
    print("\n(M) the shadow walk closes modulo every odd q (hence every modulus)")
    for q in [5, 7, 11, 13, 25, 35, 49, 3, 9, 27, 45, 63]:
        m2, u, qp = split_modulus(q)
        o = mult_order((9 * pow(8, -1, qp)) % qp, qp) if qp > 1 else 1
        a = o
        while 2 * a < u:
            a += o
        N = 3 * a + 8
        ok = True
        for w in range(1, 40, 2):
            x0 = (1 << N) * w - 5
            # impose x = -5 mod 3^u (and anything mod qp): CRT inside the 2-adic class
            if u:
                x = x0 + (1 << N) * (((-5 - x0) * pow(1 << N, -1, 3 ** u)) % 3 ** u)
            else:
                x = x0
            z = x
            for i in range(2 * a):
                e = v2(3 * z + 1)
                if e != (1 if i % 2 == 0 else 2):
                    ok = False
                z = f(z)
            if (z - x) % q != 0 or z <= x:
                ok = False
        check(f"q={q}: a={a} (ord_{qp}(9/8)={o}), f^(2a)(x) = x mod {q} on 20 shadows", ok)


# ---------------------------------------------------------------------------
# (S) multi-step corollary
# ---------------------------------------------------------------------------

def check_multistep(quick):
    print("\n(S) multi-step potentials")
    beta_p = math.log2(9 / 8)  # guidance only
    j, m = 2, 4
    for k in range(1, 7):
        # Dirichlet on k*beta': find a' with ||a' k beta'|| < 2^-(j+3)
        ap = None
        for cand in range(1, 1 << (j + 6)):
            frac = (cand * k * beta_p) % 1.0
            if min(frac, 1 - frac) < 2 ** (-(j + 3)):
                ap = cand
                break
        assert ap is not None
        a = k * ap
        N = 3 * a + max(m, 5) + j + 8
        # choose w so that LD_j closes: try odd w until it does (existence is
        # the content of Theorem B; the walk itself is exact)
        found = False
        for w in range(1, 2000, 2):
            x = (1 << N) * w - 5
            z, ok = x, True
            for i in range(2 * a):
                if v2(3 * z + 1) != (1 if i % 2 == 0 else 2):
                    ok = False
                    break
                z = f(z)
            if not ok:
                continue
            if LD(j, z) != LD(j, x):
                continue
            if (z - x) % (1 << m) or tau(z) != tau(x) or z <= x:
                continue
            if any(lam(dd, z) is not None or lam(dd, x) is not None for dd in (1, 2, 3)):
                continue
            found = True
            break
        check(f"Theorem B class, k={k}: 2a={2*a}-step walk (k | 2a) closes LD_{j}, mod 2^{m}, tau, detectors; gain > 1",
              found, f"a'={ap}, N={N}")
    # Theorem E class with k-step segments
    for k in (2, 3, 5):
        for j in ([0, 2, 4] if quick else [0, 2, 4, 6]):
            Q = 1 << j
            K0 = max(Q, 2)
            for (m, N, d) in [(4, 16, 0), (8, 9 * 256, 2)]:
                xs, word, t, Mp = build_certificate(j, m, N, d, K0, k=k)
                good = verify_certificate(j, m, N, d, xs, k=k)
                check(f"Theorem E class, k={k}, j={j}, N={N}, d={d}: {len(xs)} segments of {k} steps close with gain",
                      good, f"{max(bitlen(x) for x in xs)} bits")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--quick", action="store_true")
    args = ap.parse_args()
    check_rational_cycles()
    check_cost_law()
    check_theorem_F(args.quick)
    check_modulus_corollary()
    check_multistep(args.quick)
    print()
    if FAIL:
        print("FAILED:", FAIL)
        sys.exit(1)
    print("ALL PASS")


if __name__ == "__main__":
    main()
