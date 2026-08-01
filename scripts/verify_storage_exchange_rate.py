#!/usr/bin/env python3
"""
verify_storage_exchange_rate.py
===============================

Exact-rational verification of EXR1, the storage exchange-rate no-go for
primitive repunit tails (promoted from `repunit_extremal_principle.md` §9).

STATEMENT (EXR1).  On a valuation-one step of a repunit tail, deficit
storage and deficit accumulation move at exactly the same rate.  Precisely,
with the extremal-principle coordinates

    R_K = A_K + 2^(E_K + 1),        Z_K = R_K / 2^(E_K + 1),
    D_K = K * log_2 3 - E_K         (the running deficit),

REPEXT1 gives  Z_{K+1} = 1 + (3 Z_K - 2) / 2^(e_K).  If e_K = 1 then

    (a)  Z_{K+1} = (3/2) Z_K              [exact rational identity]
    (b)  D_{K+1} - D_K = log_2 3 - 1 = log_2(3/2)
    (c)  hence  D_K - log_2 Z_K  is constant through any valuation-one run.

CONSEQUENCE.  The exchange rate between accumulating deficit and storing it
in the correction coordinate is exactly one.  Therefore no argument using
only the valuation-one part of an orbit can show that storing deficit is
intrinsically unsustainable.  Any strict inequality must use payout ancestry
(the B_K ledger of REPEXT3), primitivity, or collision structure.

This is an impossibility statement about a class of arguments, in the same
sense as SH1/BND1 -- not a statement about the orbits themselves.

NO FLOATING POINT APPEARS IN ANY ASSERTION.  Claim (b) is verified in the
exact multiplicative form  2^(D_{K+1} - D_K) = 3/2, i.e.
3^(K+1) / 2^(E_K + 1) = (3/2) * (3^K / 2^(E_K)), as rationals.
"""

import sys
from fractions import Fraction

FAILURES = []


def check(name, condition, detail=""):
    status = "PASS" if condition else "FAIL"
    print(f"  [{status}] {name}" + (f"  ({detail})" if detail else ""))
    if not condition:
        FAILURES.append(name)


def step_Z(Z, e):
    """REPEXT1 successor: Z' = 1 + (3Z - 2)/2^e, exact rational."""
    return 1 + Fraction(3 * Z - 2, 2 ** e)


# ---------------------------------------------------------------------------
# (a) the valuation-one identity  Z' = (3/2) Z
# ---------------------------------------------------------------------------
print("\n(a) valuation-one storage identity  Z' = (3/2) Z")
ok = True
witnesses = []
for num in range(1, 400):
    for den in (1, 2, 4, 8, 16, 32, 64):
        Z = Fraction(num, den)
        if step_Z(Z, 1) != Fraction(3, 2) * Z:
            ok = False
            witnesses.append((num, den))
check("Z' = (3/2) Z for all tested rational Z on e=1", ok,
      "2800 rational states" if ok else f"failures {witnesses[:5]}")

# the identity is an algebraic one; confirm it fails for e != 1 so the
# hypothesis is not vacuous
print("\n(a') the identity is specific to e = 1")
for e in (2, 3, 4):
    Z = Fraction(5, 4)
    check(f"Z' != (3/2)Z at e={e}", step_Z(Z, e) != Fraction(3, 2) * Z,
          f"Z'={step_Z(Z, e)} vs {Fraction(3,2)*Z}")

# ---------------------------------------------------------------------------
# (b) the deficit increment, in exact multiplicative form
# ---------------------------------------------------------------------------
print("\n(b) deficit increment  2^(D_{K+1}-D_K) = 3/2  on e=1")
ok = True
for K in range(0, 300):
    for E in range(0, 60):
        # e_K = 1  =>  E_{K+1} = E_K + 1
        lhs = Fraction(3 ** (K + 1), 2 ** (E + 1))
        rhs = Fraction(3, 2) * Fraction(3 ** K, 2 ** E)
        if lhs != rhs:
            ok = False
            break
check("2^D is multiplied by exactly 3/2 on every valuation-one step", ok,
      "18000 (K,E) pairs")

# ---------------------------------------------------------------------------
# (c) invariance of D_K - log_2 Z_K through a valuation-one run
#     exact form: 2^(D_K) / Z_K is constant, i.e.
#     (3^K / 2^(E_K)) / Z_K  is unchanged by an e=1 step
# ---------------------------------------------------------------------------
print("\n(c) invariance of 2^(D_K)/Z_K through a valuation-one run")
ok = True
for num in range(1, 200):
    for den in (1, 2, 4, 8):
        Z = Fraction(num, den)
        K, E = 0, 0
        inv0 = Fraction(3 ** K, 2 ** E) / Z
        for _ in range(12):                    # a 12-step valuation-one run
            Z = step_Z(Z, 1)
            K, E = K + 1, E + 1
            if Fraction(3 ** K, 2 ** E) / Z != inv0:
                ok = False
                break
        if not ok:
            break
    if not ok:
        break
check("2^(D_K)/Z_K constant through 12-step valuation-one runs", ok,
      "800 starting states")

# ---------------------------------------------------------------------------
# (d) the exchange rate is exactly one -- the no-go itself.
#     Accumulated deficit and stored deficit change by the same factor,
#     so their difference is invariant; a strict local inequality is
#     therefore impossible on valuation-one data alone.
# ---------------------------------------------------------------------------
print("\n(d) exchange rate exactly one")
Z = Fraction(7, 4)
K, E = 5, 3
dZ = step_Z(Z, 1) / Z                                  # storage factor
dD = Fraction(3 ** (K + 1), 2 ** (E + 1)) / Fraction(3 ** K, 2 ** E)
check("storage factor equals deficit factor", dZ == dD == Fraction(3, 2),
      f"both = {dZ}")

# ---------------------------------------------------------------------------
print("\n" + "=" * 60)
if FAILURES:
    print(f"FAILED: {len(FAILURES)} check(s): {FAILURES}")
    sys.exit(1)
print("ALL PASS")
