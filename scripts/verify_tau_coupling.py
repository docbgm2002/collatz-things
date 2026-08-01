#!/usr/bin/env python3
"""
verify_tau_coupling.py
======================

Machine verification of TAU1: the tau-component of the quantized-log
coordinate imposes NO independent constraint, so the coupling identified as
the residual gap in `sufficiency_reduction.md` §6 dissolves.

For odd x write tau(x) = v_2(x+1) (the count of trailing 1-bits) and
e(x) = v_2(3x+1).

  (T1)  tau(x) >= 2  <=>  e(x) = 1,   and   tau(x) = 1  <=>  e(x) >= 2.
        (x = 3 mod 4 gives 3x+1 = 2 mod 4; x = 1 mod 4 gives 4 | 3x+1.)

  (T2)  BURN IDENTITY.  If e(x) = 1 then tau(f(x)) = tau(x) - 1.
        (x = 2^t - 1 + 2^{t+1}k gives f(x) + 1 = 3 * 2^{t-1} * (1+2k).)

  (T3)  If e(x) >= 2 then tau(x) = 1 and tau(f(x)) is unconstrained: every
        value is attained.

CONSEQUENCE (TAU1).  Along any orbit the tau-word is DETERMINED by the
e-word together with a free choice at each e >= 2 step.  Maximal runs of
e = 1 have length exactly tau - 1 (this is RUNLEN2, already in the ledger),
and each payout resets tau freely.  Therefore, for a cyclic e-word:

    the tau-closure of the cycle is satisfiable  <=>  the e-word contains
    at least one step with e >= 2,

and that is automatic, since sum(e_i) = floor(K log_2 3) >= K + 1 for K >= 2.

So tau is not an independent coordinate to be matched; it is a function of
the e-word and the payout choices.

NO FLOATING POINT APPEARS IN ANY ASSERTION.
"""

import json
import os
import sys
from collections import Counter

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


def tau(x):
    return v2(x + 1)


def f(x):
    y = 3 * x + 1
    e = v2(y)
    return y // 2 ** e, e


LIMIT = 200001

# ---------------------------------------------------------------------------
print("\n(T1) e and tau are rigidly linked")
bad = 0
for x in range(1, LIMIT, 2):
    e = f(x)[1]
    t = tau(x)
    if (t >= 2) != (e == 1):
        bad += 1
check("tau(x) >= 2  <=>  e(x) = 1", bad == 0, f"{LIMIT//2} odd x, {bad} violations")

# ---------------------------------------------------------------------------
print("\n(T2) burn identity on e = 1 steps")
bad = n = 0
for x in range(1, LIMIT, 2):
    y, e = f(x)
    if e == 1:
        n += 1
        if tau(y) != tau(x) - 1:
            bad += 1
check("e = 1  =>  tau(f(x)) = tau(x) - 1", bad == 0, f"{n} steps, {bad} violations")

# ---------------------------------------------------------------------------
print("\n(T3) payouts reset tau freely -- CONSTRUCTIVE")
# A scan over a bounded range is the WRONG test: high tau is exponentially
# rare, so absences are sampling artefacts (an earlier draft of this check
# "failed" at t=16 for exactly that reason).  The claim is existential, so
# solve for x directly:  want 3x+1 = 2^e * y with y = 2^t - 1 (mod 2^{t+1}).
def realise(t):
    for e in (2, 3, 4, 5):
        for k in range(0, 4000):
            y = (1 << t) - 1 + ((1 << (t + 1)) * k)
            n = (1 << e) * y
            if (n - 1) % 3:
                continue
            x = (n - 1) // 3
            if x <= 0 or x % 2 == 0:
                continue
            yy, ee = f(x)
            if ee == e and ee >= 2 and tau(yy) == t:
                return x, e
    return None

sols = {t: realise(t) for t in range(1, 31)}
check("for every t in 1..30 there is x with e >= 2 and tau(f(x)) = t",
      all(v is not None for v in sols.values()),
      f"e.g. t=5 -> x={sols[5][0]}, t=12 -> x={sols[12][0]}")
# and confirm the scan's apparent gap is only sparsity
c = Counter()
for x in range(1, LIMIT, 2):
    y, e = f(x)
    if e >= 2:
        c[tau(y)] += 1
check("scan density halves with t (so scan gaps are sampling artefacts)",
      all(c[t] >= c[t + 1] for t in range(1, 12)),
      f"counts t=1..8: {[c[t] for t in range(1, 9)]}")

# ---------------------------------------------------------------------------
print("\n(RUNLEN2) maximal e = 1 runs have length exactly tau - 1")
bad = eps = 0
for x0 in range(3, 60001, 2):
    if tau(x0) < 2:
        continue
    L, y = 0, x0
    while tau(y) >= 2:
        y, e = f(y)
        L += 1
        if e != 1:
            bad += 1
    eps += 1
    if L != tau(x0) - 1:
        bad += 1
check("run length = tau - 1, all steps e = 1", bad == 0, f"{eps} runs")

# ---------------------------------------------------------------------------
print("\n(TAU1) the closure condition is automatic")
bad = 0
for K in range(2, 400):
    E = (3 ** K).bit_length() - 1
    if E < K + 1:
        bad += 1
check("sum(e_i) = floor(K log_2 3) >= K+1 for K >= 2, so some e_i >= 2",
      bad == 0, "K = 2..399")

# ---------------------------------------------------------------------------
print("\n(C) the mined certificates obey the tau structure")
HERE = os.path.dirname(os.path.abspath(__file__))
CERTS = json.load(open(os.path.join(HERE, "certificates_quantized_log_remined.json")))
for js in sorted(CERTS, key=int):
    W = CERTS[js]["witnesses"]
    K = CERTS[js]["K"]
    ok_burn = ok_close = True
    for i, x in enumerate(W):
        y, e = f(x)
        if e == 1 and tau(y) != tau(x) - 1:
            ok_burn = False
        if tau(y) != tau(W[(i + 1) % K]):
            ok_close = False
    check(f"j={js}: burn identity holds on every e=1 edge", ok_burn)
    check(f"j={js}: tau closes at every junction", ok_close)

# ---------------------------------------------------------------------------
print("\n(W) the WALK1 travel path is itself a burn")
check("residues 15,7,11,1 have tau 4,3,2,1",
      [tau(r) for r in (15, 7, 11, 1)] == [4, 3, 2, 1])
check("residues 1 and 9 are payout residues (tau=1, e>=2)",
      tau(1) == 1 and tau(9) == 1 and f(1)[1] >= 2 and f(9)[1] >= 2)

print("\n(X) WHAT STILL REMAINS FOR SUFF1")
print("""      Uniformity of the counting bound.  Each witness needs
        (class mod 2^M)  INTERSECT  (sub-interval of its cell),
      with M = max(m, tau_max + 1) <= max(m, K+1).  Existence for a SINGLE
      edge is the elementary count of sec. 4 of sufficiency_reduction.md.
      The composition requires one height to serve all K edges at once.
      Their cells differ by bounded factors, so this is plausible -- but it
      is NOT written out, and SUFF1 remains OPEN.""")

print("\n" + "=" * 64)
if FAILURES:
    print(f"FAILED: {len(FAILURES)} check(s)")
    for x in FAILURES:
        print("   -", x)
    sys.exit(1)
print("ALL PASS")
