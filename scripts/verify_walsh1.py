# scripts/verify_walsh1.py

"""Spectral and residue structure of a finite actual-orbit escape set.

Reproduces section 6 of docs/no-go/macro_step_lundberg.md.

Definitions used throughout (these fix the ambiguity in earlier drafts of
the note, where two tables reported different values for mu(E_a) under
unstated conventions):

  Domain      D_B = { 2j + 1 : 0 <= j < 2^B }, indexed by j, B = 14.
  Escape set  E_{a,B,T} = { x0 in D_B : some iterate at time 0 <= k <= T
                           reaches a value >= 2^a * x0 }, T = STEP_CAP.
  Measure     mu_D = |E_{a,B,T}| / |D_B|.
  Transform   Ahat(eta) = (1/|D_B|) * sum_j 1_{E_{a,B,T}}(2j+1)
                          * (-1)^{<eta, j>},
              the Walsh-Hadamard transform in the j coordinate, so that
              Ahat(0) = mu_D.

The normalization gives |Ahat(eta)| <= Ahat(0) = mu_D for every eta.
LUN2 concerns homogeneous multipliers and does not prove mu_D <= 2^-a
for this actual-orbit event. The number 2^-a is reported only as a
reference, not as a probability or spectral bound.

The script reports max |Ahat(eta)| over eta != 0 against three yardsticks:
the reference 2^-a, the observed measure mu_D, and a heuristic scale for
a random subset of D_B of the same density. It also reports residue-class
densities and checks the FUEL1 containment and resulting finite Walsh
lower bound exactly. These finite observations do not establish an
unconditional asymptotic spectral or equidistribution claim.
"""

import math

DOMAIN_BITS = 14
STEP_CAP = 4000


def f(x):
    y = 3 * x + 1
    v = (y & -y).bit_length() - 1
    return y >> v, v


def escapes(x0, a, cap=STEP_CAP):
    """1 if an iterate at time 0 <= k <= cap reaches 2^a * x0, else 0."""
    x = x0
    threshold = x0 << a
    for _ in range(cap):
        if x >= threshold:
            return 1
        if x == 1:
            return 0
        x, _ = f(x)
    return 1 if x >= threshold else 0


def fwht(vec):
    """In-place-style fast Walsh-Hadamard transform, unnormalized."""
    a = list(vec)
    n = len(a)
    h = 1
    while h < n:
        for i in range(0, n, h * 2):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j] = x + y
                a[j + h] = x - y
        h *= 2
    return a


def random_subset_baseline(mu, n):
    """Heuristic max |Ahat(eta)| scale for a random subset of density mu.

    A nonzero coefficient for independent Bernoulli(mu) membership has
    standard deviation sqrt(mu(1-mu)/n). The Gaussian extreme-value
    heuristic multiplies this by sqrt(2 ln n); this is not a bound.
    """
    return math.sqrt(mu * (1 - mu) / n) * math.sqrt(2 * math.log(n))


def report(a, n_bits=DOMAIN_BITS):
    n = 1 << n_bits
    ind = [escapes(2 * j + 1, a) for j in range(n)]
    coef = fwht(ind)

    mu = coef[0] / n
    reference = 2.0 ** -a
    peak_eta = max(range(1, n), key=lambda k: abs(coef[k]))
    peak = abs(coef[peak_eta]) / n
    baseline = random_subset_baseline(mu, n)

    modulus = 1 << (a + 2)
    total = [0] * modulus
    hits = [0] * modulus
    for j in range(n):
        r = (2 * j + 1) % modulus
        total[r] += 1
        hits[r] += ind[j]
    # Relative finite escape density in each odd residue class, normalized
    # so that perfect equidistribution would give 1.0 in every class.
    rel = [(r, hits[r] / total[r] / mu) for r in range(1, modulus, 2)]
    rel.sort(key=lambda t: -t[1])
    empty = sum(1 for _, d in rel if d == 0.0)

    return {
        "a": a,
        "mu": mu,
        "mu_over_reference": mu / reference,
        "peak": peak,
        "peak_eta": peak_eta,
        "peak_over_reference": peak / reference,
        "peak_over_mu": peak / mu,
        "baseline": baseline,
        "peak_over_baseline": peak / baseline,
        "richest": rel[:3],
        "empty": empty,
        "classes": modulus // 2,
    }


def check_FUEL1(amax=5, n_bits=DOMAIN_BITS, cap=STEP_CAP):
    """Check fuel-cylinder containment and the finite Walsh lower bound.

    For integer a, certify the burn length s by 3^s >= 2^(s+a) in exact
    arithmetic. The forced cylinder has t=s+1 bits in x but only s free
    bits in j=(x-1)/2. Require B >= s and cap >= s so the finite domain
    resolves the cylinder and the escape window includes the forced burn.
    """
    n = 1 << n_bits
    print("FUEL1: tau(x) >= t_a  ==>  x in E_{a,B,T}")
    for a in range(1, amax + 1):
        s = 0
        while 3 ** s < 2 ** (s + a):
            s += 1
        assert 3 ** s >= 2 ** (s + a)
        assert 3 ** (s - 1) < 2 ** (s - 1 + a)
        if n_bits < s or cap < s:
            raise ValueError(f"FUEL1 at a={a} requires n_bits >= {s} "
                             f"and cap >= {s}")
        t = s + 1
        modulus = 1 << t
        ind = [escapes(2 * j + 1, a, cap) for j in range(n)]
        members = [j for j in range(n)
                   if (2 * j + 1) % modulus == modulus - 1]
        assert len(members) == n // (1 << s)
        bad = [2 * j + 1 for j in members if not ind[j]]
        if bad:
            raise AssertionError(f"FUEL1 violated at a={a}: {bad[:5]}")
        coef = fwht(ind)
        # The fixed parity bit contributes no free Walsh coordinate.
        denominator = (1 << (t - 1)) - 1
        assert max(abs(c) for c in coef[1:]) * denominator >= n - coef[0]
        mu = coef[0] / n
        forced = (1 - mu) / denominator
        baseline = random_subset_baseline(mu, n)
        print(f"  a={a} t_a={t:>2}: {len(members):>5} members checked, "
              f"0 counterexamples | forced max|A| >= {forced:.5f}, "
              f"heuristic random baseline {baseline:.5f}")
    print("  FUEL1 containment and finite Walsh inequality PASS (exact arithmetic)\n")


def main(amax=5):
    check_FUEL1(amax)
    rows = [report(a) for a in range(1, amax + 1)]

    print(f"Domain: {1 << DOMAIN_BITS} odd integers 2j+1, j < 2^{DOMAIN_BITS};"
          f" step cap {STEP_CAP}\n")

    print("Finite measure and spectrum (2^-a is a reference, not a proved bound)")
    print(f"{'a':>2} {'mu_D':>9} {'2^-a':>8} {'mu/2^-a':>9} "
          f"{'max|A|':>9} {'/2^-a':>7} {'/mu':>7}")
    for r in rows:
        print(f"{r['a']:>2} {r['mu']:>9.4f} {2.0 ** -r['a']:>8.4f} "
              f"{r['mu_over_reference']:>9.3f} {r['peak']:>9.4f} "
              f"{r['peak_over_reference']:>7.3f} {r['peak_over_mu']:>7.3f}")

    print("\nComparison against a heuristic random-subset scale at the same density")
    print(f"{'a':>2} {'max|A|':>9} {'random':>9} {'ratio':>7} {'argmax eta':>11}")
    for r in rows:
        print(f"{r['a']:>2} {r['peak']:>9.4f} {r['baseline']:>9.5f} "
              f"{r['peak_over_baseline']:>7.2f} {r['peak_eta']:>11d}")

    print("\nFinite residue structure mod 2^(a+2), normalized by observed mu_D")
    print(f"{'a':>2} {'richest classes (residue, rel. density)':>46} "
          f"{'empty':>12}")
    for r in rows:
        rich = ", ".join(f"({res}, {d:.2f})" for res, d in r["richest"])
        print(f"{r['a']:>2} {rich:>46} {r['empty']:>5}/{r['classes']:<6}")

    print("\nFinite observations:")
    print(f"  * max |Ahat(eta)| / mu_D ranges from "
          f"{min(r['peak_over_mu'] for r in rows):.2f} to "
          f"{max(r['peak_over_mu'] for r in rows):.2f} in this sample.")
    print(f"    Observed peaks exceed the heuristic random-subset scale by "
          f"{min(r['peak_over_baseline'] for r in rows):.2f}-"
          f"{max(r['peak_over_baseline'] for r in rows):.2f} times.")
    print(f"  * Observed maximizing frequencies: "
          f"{sorted({r['peak_eta'] for r in rows})}.")
    last = rows[-1]
    residue, density = last['richest'][0]
    print(f"  * At a={last['a']}, residue {residue} is richest at "
          f"{density:.2f}x the mean; {last['empty']} of {last['classes']} "
          "odd classes have no observed escape.")
    print("  * These finite data exhibit residue structure. They do not prove")
    print("    an unconditional asymptotic refutation of DISC1 or WALSH1.")


if __name__ == "__main__":
    main()
