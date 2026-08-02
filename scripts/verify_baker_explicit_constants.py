#!/usr/bin/env python3
"""Explicit-constants upgrade of the repo's Baker-gated thresholds (W9).

Every claim printed here is established in exact integer / rational
arithmetic.  Floats appear only in printing and in one explicitly labelled
cross-check (the derivative of the closed-form crossover in part D2, whose
inequality itself is evaluated exactly).

Contents
--------
A. Certified rational brackets for log 2 (self-contained series + tail).
B. The exact continued fraction of theta = log_2 3, computed by integer
   power comparisons only, with certified brackets for ||q theta||.
C. Rhin's explicit two-log bound specialised to theta, giving numeric
   (c_theta, mu) with  ||q theta|| >= c_theta * q^{-13.3}.
D. The Avenue A L=1 height/valuation gates (x*, M_{n+4}, y_n(s) for
   3-smooth s): the exact Diophantine window inequality, the exact
   window-empty index i_*(n), and the explicit crossover N_0 beyond which
   i_*(n) > 6n.  This replaces "standard lower bounds ... give ... for all
   large n" by a numeral.
E. BAKER1-3: the exact 2-adic reformulation v_2(3^m+7) = 2 + v_2(m-alpha)
   and the resulting *exact* prefix envelope, which needs no transcendence
   input at all inside any finite range.
F. The n=471 stress test.

Run:
    python3 scripts/verify_baker_explicit_constants.py
    python3 scripts/verify_baker_explicit_constants.py --nmax 4001
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from functools import lru_cache

FAILURES: list[str] = []


def check(label: str, ok: bool) -> None:
    status = "PASS" if ok else "FAIL"
    if not ok:
        FAILURES.append(label)
    print(f"  [{status}] {label}")


# ---------------------------------------------------------------------------
# A. certified rational bracket for ln 2
# ---------------------------------------------------------------------------

def ln2_bracket(terms: int = 200) -> tuple[Fraction, Fraction]:
    """Return (lo, hi) with lo <= ln 2 <= hi, exactly.

    ln 2 = sum_{k>=1} 1/(k 2^k).  The tail beyond N is at most
    (1/(N+1)) * sum_{k>N} 2^{-k} = 2^{-N}/(N+1).
    """
    total = Fraction(0)
    for k in range(1, terms + 1):
        total += Fraction(1, k * (1 << k))
    tail = Fraction(1, (terms + 1) * (1 << terms))
    return total, total + tail


LN2_LO, LN2_HI = ln2_bracket()


# ---------------------------------------------------------------------------
# B. exact continued fraction of theta = log_2 3
# ---------------------------------------------------------------------------

def cf_log(base: Fraction, arg: Fraction, count: int) -> list[int]:
    """Partial quotients of log_base(arg) for rationals base, arg > 1.

    Exact: each partial quotient is the largest k with base^k <= arg, which
    is decided by integer comparison.  Then
        log_base(arg) = k + 1/log_{arg/base^k}(base),
    and arg/base^k lies in [1, base), so the recursion is the CF algorithm.
    """
    out: list[int] = []
    for _ in range(count):
        k = 0
        power = Fraction(1)
        while power * base <= arg:
            power *= base
            k += 1
        out.append(k)
        rem = arg / power
        if rem == 1:
            break
        base, arg = rem, base
    return out


def convergents(quotients: list[int]) -> list[tuple[int, int]]:
    """Return [(p_k, q_k)] for the given partial quotients."""
    p_prev, q_prev = 1, 0
    p_cur, q_cur = quotients[0], 1
    out = [(p_cur, q_cur)]
    for a in quotients[1:]:
        p_prev, p_cur = p_cur, a * p_cur + p_prev
        q_prev, q_cur = q_cur, a * q_cur + q_prev
        out.append((p_cur, q_cur))
    return out


def log2_bracket_of_ratio(num: int, den: int) -> tuple[Fraction, Fraction]:
    """Exact (lo, hi) with lo <= log_2(num/den) <= hi.

    Uses (r-1)/r <= ln r <= r-1 for r >= 1 (and the reciprocal form for
    r <= 1), together with the certified bracket for ln 2.
    """
    r = Fraction(num, den)
    if r >= 1:
        ln_lo = (r - 1) / r
        ln_hi = r - 1
    else:
        s = 1 / r
        ln_hi = -(s - 1) / s
        ln_lo = -(s - 1)
    # dividing by ln 2 > 0: widen using the bracket, sign-aware
    lo = ln_lo / (LN2_LO if ln_lo < 0 else LN2_HI)
    hi = ln_hi / (LN2_HI if ln_hi < 0 else LN2_LO)
    return lo, hi


def theta_gap_brackets(quotients: list[int]) -> list[tuple[int, int, Fraction, Fraction]]:
    """For each convergent p/q of theta return (q, p, lo, hi) with
    lo <= |q*theta - p| <= hi, exactly.

    q*theta - p = log_2(3^q / 2^p).
    """
    out = []
    for p, q in convergents(quotients):
        if q == 0:
            continue
        lo, hi = log2_bracket_of_ratio(3 ** q, 2 ** p)
        a, b = abs(lo), abs(hi)
        if lo <= 0 <= hi:
            # bracket straddles zero -> useless; theta is irrational so this
            # only happens if the bracket is too wide.  Report it.
            out.append((q, p, Fraction(0), max(a, b)))
        else:
            out.append((q, p, min(a, b), max(a, b)))
    return out


class ThetaApproximation:
    """Best-approximation data for theta = log_2 3, certified."""

    def __init__(self, terms: int = 14) -> None:
        self.quotients = cf_log(Fraction(2), Fraction(3), terms)
        self.gaps = theta_gap_brackets(self.quotients)
        # strictly increasing denominators, dropping the degenerate q=1 twin
        seen: dict[int, tuple[Fraction, Fraction]] = {}
        for q, _p, lo, hi in self.gaps:
            if q not in seen or hi < seen[q][1]:
                seen[q] = (lo, hi)
        self.denoms = sorted(seen)
        self.lo = {q: seen[q][0] for q in self.denoms}
        self.hi = {q: seen[q][1] for q in self.denoms}
        self.qmax = self.denoms[-1]

    def min_gap_lower_bound(self, Q: int) -> Fraction:
        """A certified lower bound for min_{1<=q<=Q} ||q theta||.

        Best-approximation theorem (Hardy-Wright ch. 10): for q <= q_k the
        minimum of |q theta - p| over integers p is attained at the largest
        convergent denominator <= Q.  We return the certified lower bound of
        the bracket for that convergent.

        The map Q -> min_gap_lower_bound(Q) is non-increasing.
        """
        if Q < 1:
            raise ValueError("Q must be >= 1")
        if Q > self.qmax:
            raise ValueError(f"Q={Q} exceeds certified range q<= {self.qmax}")
        import bisect
        idx = bisect.bisect_right(self.denoms, Q) - 1
        return self.lo[self.denoms[idx]]


# ---------------------------------------------------------------------------
# C. Rhin's explicit two-log bound, specialised to theta
# ---------------------------------------------------------------------------
#
# Rhin (1987), the explicit proposition used by Simons-de Weger (2005) and by
# Simons (arXiv:2205.10582, Lemmas 10 and 12):
#
#     |u_0 + u_1 log 2 + u_2 log 3| >= H^{-13.3},   H = max(|u_1|,|u_2|) >= 2.
#
# Specialise with u_0 = 0, u_2 = -q, u_1 = p = nearest integer to q*theta.
# Then |p log 2 - q log 3| = (log 2) * ||q theta||, and since ||q theta||<=1/2
# we have p <= q*theta + 1/2 <= 1.585 q + 1/2 <= 2.085 q, so H <= RHIN_H_MULT*q.
# Hence  ||q theta|| >= (RHIN_H_MULT*q)^{-13.3} / log 2.
#
# We use exponent 13.3 with an absolute constant 1 (the *explicit* form).
# Rhin's inequality (8), as quoted by Lagarias-Soundararajan (Lemma 5.3 of
# arXiv:math/0509175), has the sharper exponent 7.616 but an unspecified
# positive constant C, so it cannot produce a numeral and is recorded in the
# audit note as "sharper but ineffective in the constant".

RHIN_EXP = Fraction(133, 10)          # 13.3
RHIN_H_MULT = Fraction(2085, 1000)    # H <= 2.085 q, valid for all q >= 1


def _ceil_cbrt(x: Fraction) -> int:
    """Least integer t with t^3 >= x, for x >= 0.  Exact."""
    a, b = x.numerator, x.denominator
    t = int(round(float(x) ** (1 / 3))) + 2
    while t > 0 and (t - 1) ** 3 * b >= a:
        t -= 1
    while t ** 3 * b < a:
        t += 1
    return max(t, 1)


def rhin_lower_bound(q: int) -> Fraction:
    """Certified lower bound for ||q theta|| from Rhin's explicit proposition.

    h = RHIN_H_MULT * q >= H, and h >= 1, so
        h^{13.3} = h^{13} * h^{0.3} <= h^{13} * h^{1/3} <= h^{13} * ceil(h^{1/3}).
    Hence  ||q theta|| >= H^{-13.3}/ln2 >= 1 / (h^{13} * ceil(h^{1/3}) * ln2).
    """
    h = RHIN_H_MULT * q
    assert h >= 1
    return Fraction(1) / (h ** 13 * _ceil_cbrt(h)) / LN2_HI


# ---------------------------------------------------------------------------
# D. Avenue A L=1 gates
# ---------------------------------------------------------------------------
#
# Lemma SD-L1-*-window (avenue_a_comparison_dynamics.md) states, for a hit
# x_i = target at index i >= 1 with x_j >= T = 2^n - 1 for all j < i,
#
#     L_i <= 2^{E_i} <= L_i (1 + 1/(3T))^i,      L_i = 3^i a_n / target.
#
# Taking log_2 and writing theta = log_2 3, a_n = (3^n-1)/2:
#
#     0 <= (E_i + A) - (i + B) theta - delta_n <= i * log_2(1 + 1/(3T))
#
# with target-dependent integers A, B and an exponentially small delta_n.
# Since E_i + A is an integer, a hit forces
#
#     || (i + B) theta ||  <=  |delta_n| + i * log_2(1 + 1/(3T))  =: Delta(n,i).
#
# The three targets of the repo:
#
#   x*(n)     = (2^{n+4}-5)/3 : A = n+5, B = n+1,
#               delta_n = log_2(1-3^{-n}) - log_2(1 - 5*2^{-(n+4)})
#   M_{n+4}   = 2^{n+4}-1     : A = n+5, B = n,
#               delta_n = log_2(1-3^{-n}) - log_2(1 - 2^{-(n+4)})
#   y_n(s)    = s*2^{n+2}-1, s = 2^a 3^b (3-smooth):
#               A = n+3+a, B = n-b,
#               delta_n = log_2(1-3^{-n}) - log_2(1 - 1/(s*2^{n+2}))
#
# For s not 3-smooth the term log_2 s is a third logarithm and Rhin does not
# apply; that row needs Matveev.  This is recorded in the audit note.


class Gate:
    """One L=1 comparison gate of Avenue A.

    label     : human name of the target
    b_off     : the Diophantine coefficient is q = i + n + b_off
    u2_num, u2_extra, u2_shift : the second logarithmic correction is
                exactly  log_2(1 - u2)  with  u2 = u2_num/(u2_extra*2^{n+u2_shift})
    note      : the repo lemma this row replaces
    """

    def __init__(self, label, b_off, u2_num, u2_extra, u2_shift, note):
        self.label = label
        self.b_off = b_off
        self.u2_num = u2_num
        self.u2_extra = u2_extra
        self.u2_shift = u2_shift
        self.note = note
        self._const: dict[int, Fraction] = {}

    def delta_upper(self, n: int, i: int) -> Fraction:
        """Certified upper bound for Delta(n,i) = |delta_n| + i log_2(1+1/(3T)).

        Strictly increasing in i.
        """
        base = self._const.get(n)
        if base is None:
            u1 = Fraction(1, 3 ** n)                # 3^{-n}
            t1 = u1 / (1 - u1)                      # |ln(1-u)| <= u/(1-u)
            u2 = Fraction(self.u2_num, self.u2_extra * (1 << (n + self.u2_shift)))
            assert u2 < 1
            t2 = u2 / (1 - u2)
            base = t1 + t2
            self._const[n] = base
        T = (1 << n) - 1
        return (base + Fraction(i, 3 * T)) / LN2_LO  # log(1+v) <= v


def _window_empty_at(gate: Gate, n: int, i: int,
                     theta: ThetaApproximation) -> bool:
    """True if the Diophantine window at index i is certifiably empty."""
    q = i + n + gate.b_off
    if q < 1:
        return False
    if q > theta.qmax:
        raise ValueError("certified CF range exhausted; raise --cf-terms")
    return theta.min_gap_lower_bound(q) > gate.delta_upper(n, i)


def gate_i_star(gate: Gate, n: int, theta: ThetaApproximation,
                i_cap: int) -> int:
    """Least i in [1, i_cap] whose Diophantine window can be nonempty.

    The predicate "window empty at i" is monotone decreasing in i, because
    min_{q<=i+B} ||q theta|| is non-increasing while Delta(n,i) is strictly
    increasing.  So a binary search is exact.

    Returns i_cap + 1 if the window is empty for every i <= i_cap.
    """
    if not _window_empty_at(gate, n, 1, theta):
        return 1
    if _window_empty_at(gate, n, i_cap, theta):
        return i_cap + 1
    lo, hi = 1, i_cap                # empty at lo, nonempty at hi
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if _window_empty_at(gate, n, mid, theta):
            lo = mid
        else:
            hi = mid
    return hi


def rhin_gate_bound(gate: Gate, n: int, i_cap: int) -> int:
    """Largest i0 <= i_cap such that Rhin's explicit bound alone proves the
    window empty for every i <= i0.  Same monotonicity, so binary search."""
    def ok(i: int) -> bool:
        q = i + n + gate.b_off
        if q < 1:
            return False
        return rhin_lower_bound(q) > gate.delta_upper(n, i)

    if not ok(1):
        return 0
    if ok(i_cap):
        return i_cap
    lo, hi = 1, i_cap
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if ok(mid):
            lo = mid
        else:
            hi = mid
    return lo


# ---------------------------------------------------------------------------
# E. BAKER1-3: the exact 2-adic reformulation
# ---------------------------------------------------------------------------

def alpha_mod(depth: int) -> int:
    """The unique alpha in Z_2 with 3^alpha = -7, returned mod 2^depth.

    Built bit by bit: 3^m mod 2^{V} depends only on m mod 2^{V-2}, so
    m -> 3^m extends continuously to Z_2, and -7 = 1 mod 8 lies in the image.
    """
    a = 0
    for j in range(depth):
        modulus = 1 << (j + 3)          # want 3^a = -7 mod 2^{j+3}
        if pow(3, a, modulus) != (-7) % modulus:
            a += 1 << j
        assert pow(3, a, modulus) == (-7) % modulus, (j, a)
    return a % (1 << depth) if depth else 0


def v2(x: int) -> int:
    if x == 0:
        raise ValueError("v2(0)")
    return (x & -x).bit_length() - 1


# ---------------------------------------------------------------------------
# accelerated map, for the n = 471 stress test
# ---------------------------------------------------------------------------

def f_odd(x: int) -> int:
    y = 3 * x + 1
    return y >> v2(y)


@lru_cache(maxsize=None)
def k_down(n: int) -> int:
    """Number of accelerated odd steps for a_n to fall below T = 2^n - 1."""
    T = (1 << n) - 1
    x = (3 ** n - 1) // 2
    k = 0
    while x >= T:
        x = f_odd(x)
        k += 1
    return k


# ---------------------------------------------------------------------------
# reporting
# ---------------------------------------------------------------------------

def part_a() -> None:
    print("\n== A. certified bracket for ln 2 ==")
    lo50, hi50 = ln2_bracket(50)
    check("coarse bracket (N=50) contains 0.69314718055994530942",
          lo50 < Fraction(69314718055994530942, 10 ** 20) < hi50)
    lo100, hi100 = ln2_bracket(100)
    check("brackets nest: [N=200] inside [N=100] inside [N=50]",
          lo50 <= lo100 <= LN2_LO < LN2_HI <= hi100 <= hi50)
    print(f"  ln2 bracket width = {float(LN2_HI - LN2_LO):.3e}")


def part_b(theta: ThetaApproximation) -> None:
    print("\n== B. exact continued fraction of theta = log_2 3 ==")
    print(f"  partial quotients: {theta.quotients}")
    print(f"  convergent denominators: {theta.denoms}")
    # sanity: the classical CF of log_2 3 starts [1;1,1,2,2,3,1,5,2,23,2,2,1,1,55,...]
    check("CF begins [1, 1, 1, 2, 2, 3, 1, 5, 2, 23]",
          theta.quotients[:10] == [1, 1, 1, 2, 2, 3, 1, 5, 2, 23])
    check("convergent 8/5 and 19/12 present (2^8<3^5, 2^19<3^12 checks)",
          (8, 5) in [(p, q) for p, q in convergents(theta.quotients)]
          and (19, 12) in [(p, q) for p, q in convergents(theta.quotients)])
    ok = True
    for q in theta.denoms:
        if not (0 < theta.lo[q] <= theta.hi[q]):
            ok = False
    check("every ||q theta|| bracket is strictly positive (irrationality)", ok)
    print("   q        lower bound on ||q theta||")
    for q in theta.denoms:
        print(f"   {q:<8d} {float(theta.lo[q]):.6e}")


def part_c(theta: ThetaApproximation) -> None:
    print("\n== C. Rhin's explicit bound specialised to theta ==")
    print("  Rhin (1987): |u0 + u1 log2 + u2 log3| >= H^-13.3, H = max(|u1|,|u2|)")
    print("  => ||q theta|| >= (2.085 q)^-13.3 / ln2   (we weaken 13.3 -> 14)")
    ok = True
    for q in theta.denoms:
        if q < 2:
            continue
        if not (rhin_lower_bound(q) <= theta.hi[q]):
            ok = False
            print(f"    inconsistency at q={q}")
    check("Rhin's bound is consistent with (weaker than) the exact CF gaps", ok)
    for q in (10, 100, 1000, 10 ** 4):
        print(f"   q={q:<7d} Rhin lower bound = {float(rhin_lower_bound(q)):.4e}")


GATES = (
    Gate("x*(n)   = (2^{n+4}-5)/3", 1, 5, 1, 4,
         "SD-L1-e2-preimage-Baker / -window-gap"),
    Gate("M_{n+4} = 2^{n+4}-1", 0, 1, 1, 4,
         "SD-L1-s4-Baker / -window-gap  (= y_n(4))"),
    Gate("y_n(3)  = 3*2^{n+2}-1", -1, 1, 3, 2,
         "SD-L1-s-Baker, s = 3 (3-smooth)"),
    Gate("y_n(6)  = 6*2^{n+2}-1", -1, 1, 3, 3,
         "SD-L1-s6 / SD-L1-s-fixed, s = 2*3 (3-smooth)"),
)

REPORT_N = (9, 11, 13, 15, 51, 101, 151, 159, 201, 471, 501, 1001, 2001)

RHIN_UNCAPPED = 10 ** 15


def part_d(theta: ThetaApproximation, nmax: int, kfactor: int) -> None:
    print("\n== D. Avenue A L=1 gates: exact i_*(n) and explicit crossover ==")
    print(f"  certificate-domain hypothesis: K_down(n) <= {kfactor} n")
    print("  A hit at index i forces  ||(i+n+b) theta|| <= Delta(n,i);")
    print("  'window empty' means that inequality is refuted in exact arithmetic.")
    for gate in GATES:
        print(f"\n  --- {gate.label}   [{gate.note}] ---")
        last_fail_cf = None
        last_fail_rhin = None
        rows = []
        n = 9
        nlast = 9
        while n <= nmax:
            cap = kfactor * n
            if n + gate.b_off + cap > theta.qmax:
                break
            istar = gate_i_star(gate, n, theta, cap)
            rhin_i0 = rhin_gate_bound(gate, n, cap)
            cf_ok = istar > cap
            rhin_ok = rhin_i0 >= cap
            if not cf_ok:
                last_fail_cf = n
            if not rhin_ok:
                last_fail_rhin = n
            if n in REPORT_N:
                rows.append((n, istar, cap, rhin_i0,
                             rhin_gate_bound(gate, n, RHIN_UNCAPPED),
                             k_down(n) if n <= 501 else None, cf_ok, rhin_ok))
            nlast = n
            n += 2
        n0_cf = (last_fail_cf + 2) if last_fail_cf is not None else 9
        n0_rhin = (last_fail_rhin + 2) if last_fail_rhin is not None else 9
        print(f"     n     i_*(exact CF)   {kfactor}n      K_down(n)"
              f"  Rhin i0 (uncapped)   CFok   Rhinok")
        for n_, istar, cap, _r0, runc, kd, a, b in rows:
            s = "inf" if istar > cap else str(istar)
            kds = "-" if kd is None else str(kd)
            print(f"   {n_:<6d} {s:<15s} {cap:<7d} {kds:<9s} {runc:<20d} "
                  f"{('yes' if a else 'NO'):<6s} {'yes' if b else 'NO'}")
        print(f"    exact-CF crossover   N0 = {n0_cf:<6d}"
              f" (window empty through {kfactor}n for every odd "
              f"{n0_cf} <= n <= {nlast})")
        print(f"    Rhin-only crossover  N0 = {n0_rhin}"
              f"   (theorem-only; valid for every odd n >= N0, no computation)")
        check(f"{gate.label}: exact-CF crossover N0 <= 2001 (inside scan range)",
              n0_cf <= 2001)
        check(f"{gate.label}: Rhin-only crossover N0 <= 2001", n0_rhin <= 2001)
        # the sharp pointwise statement: i_*(n) > K_down(n) for every odd n
        # n = 5 is the known exception (repo: i_*(5) = 11 < K_down(5) = 30,
        # discharged by direct orbit inspection, Lemma SD-L1-e2-preimage-small).
        pointwise_max = min(nmax, 501)
        bad = []
        for n_ in range(7, pointwise_max + 1, 2):
            kd = k_down(n_)
            if n_ + gate.b_off + kd > theta.qmax:
                continue
            if gate_i_star(gate, n_, theta, kd) <= kd:
                bad.append(n_)
        check(f"{gate.label}: i_*(n) > K_down(n) for every odd "
              f"7 <= n <= {pointwise_max}", not bad)
        if bad:
            print(f"    failures at n = {bad[:20]}")


def part_d2(kfactor: int) -> None:
    """The hand-provable closed-form crossover, checked numerically.

    For every gate above, i <= kfactor*n and q = i+n+b <= (kfactor+1)n+1 <= 8n
    (kfactor = 6, n >= 9).  Bounding Delta crudely,

        Delta(n,i) * ln2 <= 2*3^{-n} + 2*5*2^{-n-4} + 6n/(3(2^n-1))
                         <= 2^{-n} * (1 + 2.1 n)    for n >= 9
                         <= 2^{-n} * 3n            for n >= 9,

    while Rhin gives  ||q theta|| * ln2 >= (2.085 q)^{-13.3} >= (16.68 n)^{-13.3}.
    So the window is empty at every i <= 6n as soon as

        2^n  >  3n * (16.68 n)^{13.3}                                    (*)

    Taking log_2, (*) is  h(n) := n - log2(3n) - 13.3 log2(16.68 n) > 0, and
    h'(n) = 1 - 14.3/(n ln 2) > 0 for n >= 21, so (*) is monotone: once true it
    stays true.
    """
    import math
    print("\n== D2. the hand-provable closed-form crossover ==")
    print("  sufficient condition (*): 2^n > 3n * (16.68 n)^13.3")

    def star(n: int) -> bool:
        """(*) evaluated exactly: 2^n > 3n * (16.68 n)^13.3.

        Uses x^13.3 <= x^13 * ceil(x^{1/3}) for x >= 1, which only makes the
        right-hand side larger, so a True answer is a certified True.
        """
        x = Fraction(1668, 100) * n
        rhs = 3 * n * x ** 13 * _ceil_cbrt(x)
        return Fraction(1 << n) > rhs

    def h(n: float) -> float:
        return n - math.log2(3 * n) - 13.3 * math.log2(16.68 * n)

    n0 = next(n for n in range(9, 100000, 2) if star(n))
    print(f"  least odd n with (*) true (exact evaluation): {n0}")
    check("(*) is false at n = 157 and true at n = 161 (exact)",
          (not star(157)) and star(161))
    check("(*) is monotone: true at every odd 161 <= n <= 4001 (exact)",
          all(star(n) for n in range(161, 4002, 2)))
    check("h'(n) > 0 for n >= 21, so (*) stays true (float cross-check)",
          all(h(n + 2) > h(n) for n in range(21, 4001, 2)))
    check("closed-form crossover N0 = 161 <= 2001 (inside the scanned range)",
          n0 <= 2001)
    print(f"  => for every odd n >= {n0}, the L=1 Diophantine window is empty at")
    print(f"     every index i <= {kfactor}n, by Rhin's theorem alone.")
    # the growth law replacing "i_* >> 2^{n/mu}"
    print("  growth law: the same inequality with i free gives")
    print("     window empty for every i < c * 2^(n/14.3),  c > 1/2,")
    print("  the explicit form of the repo's 'i_* >> 2^{n/mu} for effective mu'.")


def part_e(nmax: int) -> None:
    print("\n== E. BAKER1-3: exact 2-adic reformulation and exact envelope ==")
    depth = 64
    a = alpha_mod(depth)
    print(f"  alpha mod 2^{depth} = {a}")
    print(f"  alpha mod 2^16 = {a % (1 << 16)}, v_2(alpha) = {v2(a)}")
    # Identity: for even m, v_2(3^m + 7) = 2 + v_2(m - alpha).
    ok = True
    for m in range(0, 4000, 2):
        lhs = v2(3 ** m + 7)
        d = (m - a) % (1 << depth)
        rhs = 2 + (v2(d) if d else depth)
        if lhs != min(rhs, depth):
            ok = False
            print(f"    mismatch at m={m}: {lhs} vs {rhs}")
            break
    check("v_2(3^m+7) = 2 + v_2(m - alpha) for all even m < 4000", ok)
    ok = all(v2(3 ** m + 7) == 1 for m in range(1, 500, 2))
    check("v_2(3^m+7) = 1 for all odd m < 500", ok)

    # BAKER1 equivalence and the exact envelope.
    # prefix (2,1^{K-1}) <=> v_2(3^{n+1}+7) >= K+3 <=> v_2(n+1-alpha) >= K+1.
    import math
    print("\n  Record ladder: least m with v_2(3^m+7) >= V is alpha mod 2^{V-2},")
    print("  so the least odd n admitting the prefix (2,1^{K-1}) is m_{K+3} - 1.")
    print("   K     least n       log2(n+1)   K - log2(n+1)")
    prev = -1
    ladder = []
    for V in range(4, depth + 2):
        m0 = a % (1 << (V - 2))
        if m0 <= prev:
            continue
        prev = m0
        K = V - 3
        # the true K at that n is the full valuation, computed below
        ladder.append((K, m0))
    shown = 0
    for K, m0 in ladder:
        if m0 < 2:
            continue
        d = (m0 - a) % (1 << depth)
        true_K = (v2(d) if d else depth) - 1
        lg = math.log2(m0)
        print(f"   {true_K:<5d} {m0 - 1:<13d} {lg:<11.2f} {true_K - lg:+.2f}")
        shown += 1
        if shown >= 14:
            break

    print("\n  exact envelope: max K over odd 3 <= n <= N, from the closed form")
    print("   N          max K (exact)   log2(N+1)   30 log2(N+1)+10")
    for N in (50, 500, 5001, 50001, 500001, 5000001):
        best_K, best_n = 0, None
        for K, m0 in ladder:
            if m0 - 1 <= N:
                d = (m0 - a) % (1 << depth)
                tk = (v2(d) if d else depth) - 1
                if tk > best_K:
                    best_K, best_n = tk, m0 - 1
        env = 30 * math.log2(N + 1) + 10
        print(f"   {N:<10d} {best_K:<15d} {math.log2(N+1):<11.2f} {env:<10.2f}"
              f" (attained at n={best_n})")
    # the sharp empirical envelope, exactly determined
    worst = max((tk - math.log2(m0)) for tk, m0 in
                (((v2((m0 - a) % (1 << depth)) if (m0 - a) % (1 << depth) else depth) - 1, m0)
                 for _K, m0 in ladder if m0 >= 2))
    print(f"\n  max over the whole ladder of  K - log2(n+1)  =  {worst:+.2f}")
    check("finite certificate: K <= log2(n+1) + 10 on the exact ladder "
          "to 2-adic depth 64 (n up to ~1.8e19)", worst <= 10)
    check("that is far inside the repo's empirical envelope 30 log2(n+1)+10",
          worst <= 30 * 1 + 10)
    # the theorem-free finite statement
    print("\n  The least m >= 0 with v_2(3^m+7) >= V is exactly alpha mod 2^{V-2}:")
    print("   V     least m        (so a prefix (2,1^{V-4}) needs n+1 >= this m)")
    for V in range(4, 26):
        print(f"   {V:<5d} {a % (1 << (V - 2))}")
    # Direct exhaustive confirmation, restricted to V whose witness is small.
    ok = True
    for V in range(4, 30):
        m0 = a % (1 << (V - 2))
        if m0 > 3000:
            continue
        if v2(3 ** m0 + 7) < V:
            ok = False
            break
        if any(v2(3 ** m + 7) >= V for m in range(0, m0)):
            ok = False
            break
    check("least m with v_2(3^m+7) >= V equals alpha mod 2^{V-2} "
          "(exhaustive where the witness is <= 3000)", ok)


def part_f(theta: ThetaApproximation) -> None:
    print("\n== F. n = 471 stress test ==")
    kd = k_down(471)
    print(f"  K_down(471) = {kd} accelerated odd steps (repo: 732)")
    check("K_down(471) = 732", kd == 732)
    check("K_down(471) <= 6*471", kd <= 6 * 471)
    for gate in GATES:
        cap = kd
        if 471 + gate.b_off + cap > theta.qmax:
            print(f"  {gate.label}: CF range too small for cap={cap}")
            continue
        istar = gate_i_star(gate, 471, theta, cap)
        check(f"n=471: {gate.label} window empty through K_down "
              f"(i_* > {cap})", istar > cap)
        r0 = rhin_gate_bound(gate, 471, cap)
        check(f"n=471: {gate.label} window empty through K_down by Rhin alone",
              r0 >= cap)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--nmax", type=int, default=2001)
    ap.add_argument("--cf-terms", type=int, default=13)
    ap.add_argument("--kfactor", type=int, default=6)
    args = ap.parse_args()

    print("== W9: explicit constants for the Baker-gated thresholds ==")
    theta = ThetaApproximation(args.cf_terms)
    part_a()
    part_b(theta)
    part_c(theta)
    part_d(theta, args.nmax, args.kfactor)
    part_d2(args.kfactor)
    part_e(args.nmax)
    part_f(theta)

    print()
    if FAILURES:
        print(f"FAILURES ({len(FAILURES)}):")
        for f in FAILURES:
            print(f"  - {f}")
        raise SystemExit(1)
    print("BAKER-EXPLICIT: PASS")


if __name__ == "__main__":
    main()
