#!/usr/bin/env python3
"""
verify_failure_density.py
=========================

Exact verification of the quantitative no-go theorem (manuscript Theorem G,
`docs/no-go/failure_density.md`): how often a depth-m local potential

    Phi_g(x) = log_2 x + g(x mod 2^m)

must fail to be nonincreasing along the accelerated map f.  Write
theta = 1/log_2 3 and c = 1 - H(theta), H the binary entropy, so
c = 0.0493...  The theorem says that the minimal failure density delta_m
(infimum over g of the lower density, among odd integers, of
{x : Phi_g(f(x)) > Phi_g(x)}) satisfies

    2^{-cm} / (16 (m+2)^5)  <=  delta_m  <=  4 * 2^{-cm}      (m >= 12),

the lower bound coming from the shadows of all expanding periodic parity
words of length m+1, the upper bound from an explicit "lookahead" potential.

What is checked here (no floating point in any assertion; log_2 3 is
carried as a formal symbol L and inequalities aL + b > 0 with rational a, b
are decided by comparing powers of 2 and 3):

(T)  Terras bijection: odd residues mod 2^n <-> parity words of length n
     with first letter O, for n <= 14.
(I)  The lookahead identity.  With h(r) = sum_{l<m} (1-(l+1)/m) gamma(p_l),
     gamma(O) = L-1, gamma(E) = -1:  gamma(p_0) + h(T x) - h(x)
     = (1/m) sum_{l<m} gamma(p_l) = (k L - m)/m for every residue x mod
     2^{m+1}, m <= 12 (symbolic identity, exact rationals).
(U)  Exact failure density of the lookahead potential: the set
     {odd x : some T^i(x), i < e(x), has more than theta*m odd letters in
     its m-window} has density sum_i 2^{-i} P(...) computed exactly, and it
     is <= 4 * 2^{-cm} for 8 <= m <= 40 (the last comparison uses the exact
     value of c to 60 digits).  Also, by direct exact evaluation on odd
     x < 2^17 for m = 6, 8, 10: every failure of Phi_g lies in that set or
     in the explicit finite exceptional set.
(Lw) Lower bound.  For each m <= 13 and every expanding cyclic parity word w
     of length m+1 (3^k > 2^{m+1}): its rational cycle from Lemma
     (rational cycles) has the right word; the class A_i = {x = y_i mod
     2^{m+e_i}} realises the edge (valuation and image residue checked on
     the three smallest members); the summed gain K L - P is positive
     (exactly); and the windows of length m+1 chosen for distinct cyclic
     words are distinct.  The resulting bound LB_m = sum_w 2^{-(m+e_max-1)}
     is computed exactly and compared with 2^{-cm}/(16(m+2)^5).
(D)  Detector locality: beta_d(s) <= 2d + ord_d s and T_s = t_d (mod
     2^{beta_d(s)+1}) for d <= 6, s <= 40, so lambda_d is decided by x mod 2^m
     off the class of t_d (checked directly at m = 12, d = 1, 2).
(A)  Adversarial check.  For m = 6, 8 and several explicit g (zero, the
     lookahead potential, the fuel potential truncated to depth m, random
     rationals), the exact density of fully-failing edge classes is >= LB_m.

Run:  python3 scripts/verify_failure_density.py
"""

import random
import sys
from decimal import Decimal, getcontext
from fractions import Fraction
from itertools import product

getcontext().prec = 80
FAIL = []


def check(name, cond, detail=""):
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ""))
    if not cond:
        FAIL.append(name)


# ---------------------------------------------------------------------------
# arithmetic with the formal symbol L = log_2 3:  values are pairs (a, b) = aL + b
# ---------------------------------------------------------------------------

def v2(n):
    if isinstance(n, Fraction):
        n = n.numerator
    return (n & -n).bit_length() - 1


def T(x):
    return x // 2 if x % 2 == 0 else (3 * x + 1) // 2


def f(x):
    y = 3 * x + 1
    return y >> v2(y)


def e_of(x):
    return v2(3 * x + 1)


def parity_word(x, n):
    w = []
    for _ in range(n):
        w.append(x % 2)
        x = T(x)
    return tuple(w)


def sym_positive(a, b):
    """Decide a*L + b > 0 exactly for rational a, b (L = log_2 3)."""
    a, b = Fraction(a), Fraction(b)
    if a == 0:
        return b > 0
    # a L > -b  <=>  L > -b/a (a>0)  or  L < -b/a (a<0);  L > p/q <=> 3^q > 2^p
    r = -b / a
    p, q = r.numerator, r.denominator  # q > 0
    if p < 0:
        gt = True  # L > negative number
    else:
        gt = 3 ** q > 2 ** p
    return gt if a > 0 else (not gt)


def gamma(p):
    return (Fraction(1), Fraction(-1)) if p == 1 else (Fraction(0), Fraction(-1))


def add(u, v):
    return (u[0] + v[0], u[1] + v[1])


def scale(c, u):
    return (c * u[0], c * u[1])


# ---------------------------------------------------------------------------
# (T) Terras bijection
# ---------------------------------------------------------------------------

def check_terras():
    print("\n(T) Terras bijection between odd residues mod 2^n and parity words")
    ok = True
    for n in range(1, 15):
        seen = set()
        for r in range(1, 1 << n, 2):
            w = parity_word(r, n)
            if w[0] != 1 or w in seen:
                ok = False
            seen.add(w)
        if len(seen) != 1 << (n - 1):
            ok = False
    check("odd residues mod 2^n <-> words of length n starting with O, n <= 14", ok)


# ---------------------------------------------------------------------------
# (I) lookahead identity
# ---------------------------------------------------------------------------

def h_sym(r, m):
    w = parity_word(r, m)
    tot = (Fraction(0), Fraction(0))
    for l, p in enumerate(w):
        tot = add(tot, scale(Fraction(m - l - 1, m), gamma(p)))
    return tot


def check_identity():
    print("\n(I) the lookahead identity gamma(p_0) + h(Tx) - h(x) = (kL - m)/m")
    for m in range(1, 13):
        ok = True
        for x in range(0, 1 << (m + 1)):
            w = parity_word(x, m)
            k = sum(w)
            lhs = add(gamma(w[0]), add(h_sym(T(x) % (1 << m), m), scale(Fraction(-1), h_sym(x % (1 << m), m))))
            rhs = (Fraction(k, m), Fraction(-m, m))
            if lhs != rhs:
                ok = False
                break
        check(f"m={m}: identity on all residues mod 2^{m+1}", ok)


# ---------------------------------------------------------------------------
# (U) upper bound: exact density of the lookahead failure set
# ---------------------------------------------------------------------------

def binom_tail_strict(n, a_num, a_den):
    """P(Bin(n,1/2) > a) with a = a_num/a_den exactly, as a Fraction."""
    from math import comb
    return Fraction(sum(comb(n, k) for k in range(n + 1) if k * a_den > a_num), 2 ** n)


def expanding_threshold(P):
    """least k with 3^k > 2^P."""
    k = 0
    while 3 ** k <= 2 ** P:
        k += 1
    return k


def c_decimal():
    th = 1 / (Decimal(3).ln() / Decimal(2).ln())
    H = -(th * th.ln() + (1 - th) * (1 - th).ln()) / Decimal(2).ln()
    return 1 - H, th


def check_upper():
    print("\n(U) the lookahead potential fails on density <= 4 * 2^{-cm}")
    c, th = c_decimal()
    print(f"    theta = {th:.12f}, c = 1 - H(theta) = {c:.12f}")
    ok_all = True
    rows = []
    for m in range(8, 41):
        # windows with k L > m  <=>  k >= expanding_threshold(m)
        k0 = expanding_threshold(m)
        from math import comb
        # dens(G_0) = P(1 + Bin(m-1) >= k0),  dens(G_i) = 2^-i P(Bin(m-1) >= k0), i>=1
        pm1 = Fraction(sum(comb(m - 1, k) for k in range(m) if k >= k0), 2 ** (m - 1))
        p0 = Fraction(sum(comb(m - 1, k) for k in range(m) if 1 + k >= k0), 2 ** (m - 1))
        dens = p0 + pm1  # sum_{i>=1} 2^-i = 1
        bound = 4 * Decimal(2) ** (-c * m)
        ok = Decimal(dens.numerator) / Decimal(dens.denominator) <= bound
        ok_all &= ok
        rows.append((m, dens, bound))
    check("exact density of the lookahead failure set <= 4 * 2^{-cm}, 8 <= m <= 40", ok_all)
    for m, dens, bound in rows[::8]:
        print(f"    m={m:2d}: density = 2^{float(Decimal(dens.numerator).ln() / Decimal(2).ln() - Decimal(dens.denominator).ln() / Decimal(2).ln()):7.3f}"
              f"   4*2^(-cm) = 2^{float((bound).ln() / Decimal(2).ln()):7.3f}")
    # direct check on integers: every failure of Phi_g (g = lookahead) is in the
    # predicted set or in the finite exceptional set
    for m in (6, 8, 10):
        k0 = expanding_threshold(m)
        bad = 0
        exceptional = 0
        for x in range(3, 1 << 17, 2):
            # Phi(f x) - Phi(x) = log2(f(x)/x) + h(fx) - h(x) > 0 ?
            d = add(h_sym(f(x) % (1 << m), m), scale(Fraction(-1), h_sym(x % (1 << m), m)))
            # exact decision of log2(f(x)/x) + aL + b > 0 :  f(x) * 3^a * 2^b > x
            a, b = d
            q = (a.denominator * b.denominator) // __import__("math").gcd(a.denominator, b.denominator)
            aq, bq = int(a * q), int(b * q)
            lhs, rhs = f(x) ** q, x ** q
            if aq >= 0:
                lhs *= 3 ** aq
            else:
                rhs *= 3 ** (-aq)
            if bq >= 0:
                lhs *= 2 ** bq
            else:
                rhs *= 2 ** (-bq)
            fails = lhs > rhs
            if not fails:
                continue
            # predicted: some T^i x, i < e(x), has >= k0 odd letters in its window
            pred = False
            y = x
            for i in range(e_of(x)):
                if sum(parity_word(y, m)) >= k0:
                    pred = True
                    break
                y = T(y)
            if pred:
                bad += 1  # counted, fine
            else:
                exceptional += 1
                # must be explained by a small odd T^i x with the eps term
                y, expl = x, False
                for i in range(e_of(x)):
                    if y % 2 == 1:
                        k = sum(parity_word(y, m))
                        # (m - kL)/m < eps(y) = log2(1 + 1/(3y))  <=>  (1+1/(3y))^m * 3^k > 2^m  exactly
                        if (3 * y + 1) ** m * 3 ** k > 2 ** m * (3 * y) ** m:
                            expl = True
                    y = T(y)
                if not expl:
                    FAIL.append(f"unexplained failure m={m} x={x}")
        check(f"m={m}: all failures of the lookahead potential for odd x < 2^17 are predicted",
              not any(s.startswith(f"unexplained failure m={m}") for s in FAIL),
              f"{bad} in the window set, {exceptional} in the finite exceptional set")


# ---------------------------------------------------------------------------
# (Lw) lower bound: shadows of expanding cyclic words
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
        assert v2(t) == e
        ys.append(t / 2 ** e)
    assert ys[-1] == ys[0]
    return ys[:-1]


def word_to_valuations(w):
    """w a binary tuple starting with 1 (O). Returns the valuation word."""
    P = len(w)
    es = []
    i = 0
    while i < P:
        assert w[i] == 1
        j = i + 1
        while j < P and w[j] == 0:
            j += 1
        es.append(j - i)
        i = j
    return es


def canonical_rotation(w):
    return min(w[i:] + w[:i] for i in range(len(w)))


def check_lower(mmax=13):
    print("\n(Lw) lower bound from expanding cyclic words")
    c, th = c_decimal()
    table = []
    for m in range(3, mmax + 1):
        P = m + 1
        k0 = expanding_threshold(P)
        seen = set()
        windows = set()
        LB = Fraction(0)
        n_words = 0
        ok = True
        for w in product((0, 1), repeat=P):
            if sum(w) < k0:
                continue
            cw = canonical_rotation(w)
            if cw in seen:
                continue
            seen.add(cw)
            # representative starting with O
            i0 = cw.index(1)
            w0 = cw[i0:] + cw[:i0]
            es = word_to_valuations(w0)
            K, E = len(es), sum(es)
            assert E == P and K == sum(w0)
            ys = rational_cycle(tuple(es))
            # parity word of y_1 is w0^infty
            y1 = ys[0]
            # 2-adic parity: compute via residue mod 2^(2P+4)
            M = 2 * P + 4
            r = (y1.numerator * pow(y1.denominator, -1, 1 << M)) % (1 << M)
            if parity_word(r, 2 * P) != w0 + w0:
                ok = False
            # positive summed gain: K L - P > 0
            if not sym_positive(K, -P):
                ok = False
            # edge classes
            for i, e in enumerate(es):
                yi = ys[i]
                mod = 1 << (m + e)
                ri = (yi.numerator * pow(yi.denominator, -1, mod)) % mod
                nxt = ys[(i + 1) % K]
                rn = (nxt.numerator * pow(nxt.denominator, -1, 1 << m)) % (1 << m)
                for t in range(3):
                    x = ri + t * mod
                    if x <= 1:
                        continue
                    if e_of(x) != e or f(x) % (1 << m) != rn:
                        ok = False
            emax = max(es)
            LB += Fraction(1, 2 ** (m + emax - 1))
            # the window of length P used for disjointness: a rotation of cw
            windows.add(cw)
            n_words += 1
        if len(windows) != n_words:
            ok = False
        bound = Decimal(2) ** (-c * m) / (16 * (m + 2) ** 5)
        lb_dec = Decimal(LB.numerator) / Decimal(LB.denominator)
        table.append((m, n_words, LB, lb_dec, bound))
        check(f"m={m}: {n_words} expanding cyclic words of length {P}; cycles, edge classes, gains, distinct windows",
              ok)
    ok_bound = all(lb >= bd for (m, n, LB, lb, bd) in table if m >= 12)
    check("LB_m >= 2^{-cm}/(16(m+2)^5) for 12 <= m <= %d" % mmax, ok_bound)
    print("    m   #words   LB_m (exact)                 log2 LB_m    log2 of stated bound")
    for (m, n, LB, lb, bd) in table:
        print(f"    {m:2d}  {n:7d}   {LB.numerator}/{LB.denominator:<22d} {float(lb.ln()/Decimal(2).ln()):8.3f}    {float(bd.ln()/Decimal(2).ln()):8.3f}")
    return table


# ---------------------------------------------------------------------------
# (A) adversarial check: explicit potentials fail on at least LB_m
# ---------------------------------------------------------------------------

def failing_measure(g, m, ecap):
    """Exact density (among odd integers) of the union of edge classes
    x = r mod 2^{m+e} (e <= ecap) on which g(f(x) mod 2^m) - g(x mod 2^m)
    + (L - e) >= 0, i.e. the constraint fails for every member."""
    tot = Fraction(0)
    for e in range(1, ecap + 1):
        mod = 1 << (m + e)
        for r in range(1, mod, 2):
            if e_of(r) != e:
                continue
            u, v = r % (1 << m), f(r) % (1 << m)
            d = add(g[v], scale(Fraction(-1), g[u]))
            d = add(d, (Fraction(1), Fraction(-e)))
            # fails for all members iff d >= 0, i.e. not (d < 0)
            if not sym_positive(-d[0], -d[1]):
                tot += Fraction(1, 1 << (m + e - 1))
    return tot


def check_adversarial(table):
    print("\n(A) explicit potentials against the lower bound")
    random.seed(1)
    LBs = {m: LB for (m, n, LB, lb, bd) in table}
    for m in (6, 8):
        odd = list(range(1, 1 << m, 2))
        pots = {
            "g = 0": {r: (Fraction(0), Fraction(0)) for r in odd},
            "lookahead": {r: h_sym(r, m) for r in odd},
            "fuel c*tau": {r: (Fraction(min(v2(r + 1), m)), Fraction(-min(v2(r + 1), m))) for r in odd},
        }
        for t in range(3):
            pots[f"random {t}"] = {r: (Fraction(random.randint(-8, 8), 4), Fraction(random.randint(-8, 8), 4)) for r in odd}
        for name, g in pots.items():
            mu = failing_measure(g, m, ecap=m + 4)
            check(f"m={m}, {name:10s}: failing-class density {float(mu):.5f} >= LB_m = {float(LBs[m]):.5f}", mu >= LBs[m])


# ---------------------------------------------------------------------------
# (D) detector locality (Lemma (local) of manuscript Section 8)
# ---------------------------------------------------------------------------

def w_d(d, M):
    num = 2 ** (M + 2 * d) - 2 ** (2 * d + 1) + 3 ** d
    assert num % 3 ** d == 0
    return num // 3 ** d


def check_detector_locality():
    print("\n(D) detector templates satisfy beta_d(s) <= 2d + ord_d s and T_s = t_d mod 2^(beta+1)")
    ok = True
    for d in range(1, 7):
        o = 2 * 3 ** (d - 1)
        for s in range(1, 41):
            Ts = w_d(d, 1 + o * s)
            beta = Ts.bit_length()
            mod = 1 << (beta + 1)
            td = (1 - (2 ** (2 * d + 1)) * pow(3 ** d, -1, mod)) % mod
            if not (beta <= 2 * d + o * s and Ts % mod == td):
                ok = False
    check("d <= 6, s <= 40: bit length bound and congruence to the 2-adic limit t_d", ok)
    # consequence: lambda_d(x) is determined by x mod 2^m unless x = t_d mod 2^m  (m = 12, d = 1, 2)
    def lam(d, x, smax=12):
        o = 2 * 3 ** (d - 1)
        best = 0
        for s in range(1, smax + 1):
            Tt = w_d(d, 1 + o * s)
            if x % (1 << (Tt.bit_length() + 1)) == Tt % (1 << (Tt.bit_length() + 1)):
                best = s
        return best
    m = 12
    ok2 = True
    for d in (1, 2):
        td = (1 - (2 ** (2 * d + 1)) * pow(3 ** d, -1, 1 << m)) % (1 << m)
        for r in range(1, 1 << m, 2):
            if r == td:
                continue
            vals = {lam(d, r + t * (1 << m)) for t in range(0, 64)}
            if len(vals) != 1:
                ok2 = False
    check("m=12, d=1,2: lambda_d constant on every odd class mod 2^12 other than that of t_d (64 lifts each)", ok2)


def main():
    check_detector_locality()
    check_terras()
    check_identity()
    check_upper()
    table = check_lower()
    check_adversarial(table)
    print()
    if FAIL:
        print("FAILED:", FAIL[:10])
        sys.exit(1)
    print("ALL PASS")


if __name__ == "__main__":
    main()
