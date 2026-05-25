#!/usr/bin/env python3
"""
Verification for "Recharge No-Go and the Tight Mersenne Burn Ledger".

Two things are checked, both with exact integer / rational arithmetic where the
claim is an identity, and with reported floating-point figures only for the
logarithmic ledger quantities:

  PART 1 (negative result).  No potential of the form
        P(x) = log2(x) + g(v2(x+1))
  with g ANY function can be a global Collatz supermartingale. The rail-7 / burn
  side forces g to climb with slope >= log2(3/2) ~ 0.585 per unit of trailing-one
  fuel; the recharge side (landing on a Mersenne number 2^m - 1) permits g to
  climb with slope -> 0. The two constraints are inconsistent over tau in [3,7].

  PART 2 (tight cumulative ledger, even Mersenne spine).  For M_n = 2^n - 1 the
  burn phase has the exact closed form x_j = 3^j * 2^(n-j) - 1 with tau = n - j,
  each step is the affine map x -> (3x+1)/2, and the critical potential
        Phi(x) = log2(x) + log2(3/2) * tau(x)
  increases by EXACTLY  sum log2(1 + 1/(3 x_j)),  a total bounded by log2(10/9)
  for every n. Hence the burn's fuel price is exactly log2(3/2), approached from
  above. The single post-burn escape step is computed exactly. The closed-form
  phase does NOT bring the value below x0 (the peak is ~ (3/2)^(n-1) * x0): that
  residual descent is the open part and is not claimed here.

No external dependencies.
"""
import math
from fractions import Fraction as Fr

LOG2_3_2 = math.log2(1.5)          # 0.5849625007...
LOG2_10_9 = math.log2(10 / 9)      # 0.1520030934...  (= sup_n S_n, attained at n=2)


def v2(n):
    return (n & -n).bit_length() - 1 if n else 10 ** 9


def tau(x):
    """Trailing-one fuel of an odd x: number of trailing 1 bits = v2(x+1)."""
    return v2(x + 1)


def f(x):
    """Odd-step (shortcut) map on odd x: (3x+1)/2^v2(3x+1)."""
    t = 3 * x + 1
    return t >> v2(t)


# ---------------------------------------------------------------------------
# PART 2a: exact burn closed form for the Mersenne spine
# ---------------------------------------------------------------------------
def check_burn_closed_form(N=200):
    """M_n = 2^n - 1 burns as x_j = 3^j 2^(n-j) - 1 (j = 0..n-1):
       tau(x_j) = n - j, each interior step has v2(3x+1)=1, and the exact
       per-step ratio is x_{j+1}/x_j = 3/2 + 1/(2 x_j)."""
    for n in range(2, N + 1):
        x = 2 ** n - 1
        for j in range(n):                       # j = 0 .. n-1
            assert x == 3 ** j * 2 ** (n - j) - 1, (n, j)
            assert tau(x) == n - j, (n, j, tau(x))
            if j < n - 1:                        # still on the burn
                assert v2(3 * x + 1) == 1, (n, j)
                nxt = f(x)
                assert Fr(nxt, x) == Fr(3, 2) + Fr(1, 2 * x), (n, j)
                assert nxt == (3 * x + 1) // 2
                x = nxt
    print(f"Part 2a: PASS  burn closed form x_j=3^j 2^(n-j)-1, tau=n-j, "
          f"ratio=3/2+1/(2x)  (n=2..{N})")


# ---------------------------------------------------------------------------
# PART 2b: tight cumulative ledger  S_n  and critical fuel price  c*(n)
# ---------------------------------------------------------------------------
def check_tight_ledger():
    """Over the whole burn, log2(peak/x0) = (n-1) log2(3/2) + S_n where
       S_n = sum_{j=0}^{n-2} log2(1 + 1/(3 x_j))   (the exact Phi increment),
       with 0 < S_n <= log2(10/9), S_n decreasing in n, and the fuel price
       c*(n) = log2(peak/x0)/(n-1) decreasing to log2(3/2).
       S_n is summed term-by-term with log1p to stay accurate when the
       per-step correction drops below float resolution."""
    ln2 = math.log(2)
    print("Part 2b: tight ledger")
    print(f"   {'n':>4} {'(n-1)log2 3/2':>14} {'S_n':>14} "
          f"{'log2(peak/x0)':>14} {'c*(n)':>10}")
    prev_S = None
    prev_c = None
    for n in [2, 3, 5, 9, 17, 33, 65, 129, 257, 513]:
        # exact per-step Phi increments log2(1 + 1/(3 x_j)), x_j = 3^j 2^(n-j)-1
        Sn = 0.0
        for j in range(n - 1):                   # j = 0 .. n-2
            xj = 3 ** j * 2 ** (n - j) - 1
            Sn += math.log1p(1.0 / (3 * xj)) / ln2
        lg = (n - 1) * LOG2_3_2 + Sn
        cstar = lg / (n - 1)
        assert Sn >= 0.0, (n, Sn)
        assert Sn <= LOG2_10_9 + 1e-12, (n, Sn)
        assert cstar > LOG2_3_2 - 1e-12, (n, cstar)
        if prev_S is not None:
            assert Sn <= prev_S + 1e-15, (n, Sn, prev_S)
            assert cstar <= prev_c + 1e-15, (n, cstar, prev_c)
        prev_S, prev_c = Sn, cstar
        print(f"   {n:4d} {(n-1)*LOG2_3_2:14.4f} {Sn:14.8f} {lg:14.4f} {cstar:10.6f}")
    print(f"   sup_n S_n = log2(10/9) = {LOG2_10_9:.5f} (attained at n=2); "
          f"c*(n) -> log2(3/2) = {LOG2_3_2:.6f}")
    print("   PASS  S_n in (0, log2(10/9)], c* decreasing to log2(3/2)")


# ---------------------------------------------------------------------------
# PART 2c: the single post-burn escape step (exact)
# ---------------------------------------------------------------------------
def check_escape_step():
    """From the peak x_{n-1} = 2*3^(n-1)-1:
         3*peak+1 = 2(3^n - 1), so f(peak) = (3^n - 1) / 2^{v2(3^n-1)}.
       Odd n (the 'even spine', k even): v2(3^n-1)=1, f(peak)=(3^n-1)/2, tau=1.
       The peak is ~ (3/2)^(n-1) * x0, so the closed-form phase does NOT
       descend below x0 -- that residual is open and not claimed."""
    print("Part 2c: escape step")
    for n in [5, 9, 17, 33, 65]:                 # odd n = even spine
        peak = 2 * 3 ** (n - 1) - 1
        assert 3 * peak + 1 == 2 * (3 ** n - 1)
        vv = v2(3 ** n - 1)
        pred = (3 ** n - 1) // (2 ** vv)
        assert f(peak) == pred, (n, f(peak), pred)
        if n % 2 == 1:
            assert vv == 1 and pred == (3 ** n - 1) // 2
            assert tau(pred) == 1, (n, tau(pred))
        ratio = peak / (2 ** n - 1) if n < 60 else float('inf')
        print(f"   n={n:3d}: f(peak)=(3^n-1)/2^{vv} exact; tau_after={tau(pred)}; "
              f"peak/x0 ~ {ratio:.3e} >> 1 (no closed-form descent)")
    print("   PASS  escape image exact; residual descent below x0 left open")


# ---------------------------------------------------------------------------
# PART 1a: burn side of the no-go -- required g-slope >= log2(3/2)
# ---------------------------------------------------------------------------
def check_burn_slope():
    """Any odd x with tau(x)=t>=2 has v2(3x+1)=1, so f(x)=(3x+1)/2, with
       tau(f(x)) = t-1 and log2(f/x) > log2(3/2). Hence a monotone g must
       satisfy g(t) - g(t-1) >= log2(3/2) at every level t>=2."""
    worst = 10.0
    for t in range(2, 40):
        for m in range(1, 50, 2):                # x = 2^t * m - 1, m odd
            x = (1 << t) * m - 1
            assert v2(3 * x + 1) == 1
            fx = f(x)
            assert tau(fx) == t - 1, (t, m, tau(fx))
            d = math.log2(fx / x)
            assert d > LOG2_3_2 - 1e-12, (t, m, d)
            worst = min(worst, d)
    print(f"Part 1a: PASS  burn forces g-slope >= log2(3/2)={LOG2_3_2:.4f}; "
          f"min observed step dlog={worst:.4f} (-> log2(3/2) from above)")


# ---------------------------------------------------------------------------
# PART 1b: recharge side -- allowed g-slope -> 0
# ---------------------------------------------------------------------------
def check_recharge_slope():
    """Recharge family x_m = (2^(m+2) - 5)/3 (odd m) maps in one step to the
       Mersenne number 2^m - 1, with value dropping by -> log2(3/4) while tau
       jumps to m. The allowed g-slope (-dlog)/dtau -> 0 as m grows."""
    prev = 10.0
    print("Part 1b: recharge family x_m=(2^(m+2)-5)/3 -> 2^m-1")
    for m in range(7, 100, 2):
        assert (2 ** (m + 2) - 5) % 3 == 0, m
        xm = (2 ** (m + 2) - 5) // 3
        fx = f(xm)
        assert fx == 2 ** m - 1, (m, fx)
        dlog = math.log2(Fr(fx, xm))             # exact ratio -> float, stable
        dt = tau(fx) - tau(xm)
        slope = (-dlog) / dt
        assert slope < prev, (m, slope, prev)    # strictly decreasing
        prev = slope
        if m <= 31:
            print(f"   m={m:3d}: x={xm} (tau{tau(xm)}) -> 2^{m}-1 (tau{tau(fx)})  "
                  f"dlog={dlog:+.3f} dtau={dt:+d}  allowed g-slope <= {slope:.4f}")
    assert prev < 0.005, prev
    print(f"   PASS  allowed g-slope strictly decreasing, < {prev:.4f} by m=99 (-> 0)")


# ---------------------------------------------------------------------------
# PART 1c: the explicit contradiction over tau in [3,7]
# ---------------------------------------------------------------------------
def check_nogo_contradiction():
    """Burn forces g increasing with slope >= log2(3/2) on every unit step, so
       g(7)-g(3) >= 4 log2(3/2). The recharge 169 -> 127 = 2^7-1 forces
       g(7)-g(1) <= -log2(127/169); monotonicity (g(3)>=g(1)) then gives
       g(7)-g(3) <= g(7)-g(1). The two bounds are inconsistent."""
    lower = 4 * LOG2_3_2                          # from burn on [3,7]
    fx = f(169)
    assert fx == 127 == 2 ** 7 - 1
    upper = -math.log2(127 / 169)                 # >= g(7)-g(1) >= g(7)-g(3)
    print("Part 1c: no-go contradiction on tau in [3,7]")
    print(f"   burn  => g(7)-g(3) >= 4*log2(3/2)   = {lower:.4f}")
    print(f"   169->127=2^7-1 (+ monotone g) => g(7)-g(3) <= {upper:.4f}")
    assert lower > upper, (lower, upper)
    print(f"   {lower:.4f} > {upper:.4f}: PASS  no g(v2(x+1)) can be a "
          f"global supermartingale")


if __name__ == "__main__":
    print("=== PART 1: recharge no-go (no scalar trailing-one potential works) ===")
    check_burn_slope()
    check_recharge_slope()
    check_nogo_contradiction()
    print("\n=== PART 2: tight cumulative ledger for the Mersenne spine ===")
    check_burn_closed_form()
    check_tight_ledger()
    check_escape_step()
    print("\nAll checks passed.")
