# scripts/verify_walsh1.py

"""Spectral and residue structure of the escape set E_a.

Reproduces section 6 of docs/no-go/macro_step_lundberg.md.

Definitions used throughout (these fix the ambiguity in earlier drafts of
the note, where two tables reported different values for mu(E_a) under
unstated conventions):

  Domain      D = { 2j + 1 : 0 <= j < 2^14 }, indexed by j.
  Escape set  E_a = { x0 in D : the accelerated odd orbit of x0 ever
                      reaches a value >= 2^a * x0 }.
  Measure     mu(E_a) = |E_a| / |D|.
  Transform   Ahat(eta) = (1/|D|) * sum_j 1_{E_a}(2j+1) * (-1)^{<eta, j>},
              the Walsh-Hadamard transform in the j coordinate, so that
              Ahat(0) = mu(E_a).

Two consequences of this normalization are worth stating because the note
previously leaned on the second without noticing the first:

  (i)  |Ahat(eta)| <= Ahat(0) = mu(E_a) for every eta, trivially.
  (ii) By LUN2, mu(E_a) <= 2^-a.  Hence |Ahat(eta)| <= 2^-a holds for all
       eta with no work at all.  Any spectral claim of the form
       |Ahat(eta)| <= C * 2^-a is therefore vacuous unless C is small
       enough to beat mu(E_a)/2^-a, which is ~0.74-0.87 here.

The script reports max |Ahat(eta)| over eta != 0 against three yardsticks:
the Haar bound 2^-a, the observed measure mu(E_a), and the size expected of
a uniformly random subset of D of the same density.  It also reports the
distribution of E_a across residue classes mod 2^(a+2), normalized by the
observed measure rather than by 2^-a.
"""

import math

DOMAIN_BITS = 14
STEP_CAP = 4000


def f(x):
    y = 3 * x + 1
    v = (y & -y).bit_length() - 1
    return y >> v, v


def escapes(x0, a, cap=STEP_CAP):
    """1 if the orbit of x0 ever reaches 2^a * x0, else 0."""
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
    """Expected max |Ahat(eta)| for a uniformly random subset of density mu.

    Each coefficient is a mean of n centered Bernoulli(mu) terms, so has
    standard deviation sqrt(mu(1-mu)/n); the max over n-1 of them sits near
    sqrt(2 ln n) standard deviations.
    """
    return math.sqrt(mu * (1 - mu) / n) * math.sqrt(2 * math.log(n))


def report(a, n_bits=DOMAIN_BITS):
    n = 1 << n_bits
    ind = [escapes(2 * j + 1, a) for j in range(n)]
    coef = fwht(ind)

    mu = coef[0] / n
    haar = 2.0 ** -a
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
    # relative density of E_a in each odd residue class, normalized so that
    # a perfectly equidistributed E_a would give 1.0 in every class
    rel = [(r, hits[r] / total[r] / mu) for r in range(1, modulus, 2)]
    rel.sort(key=lambda t: -t[1])
    empty = sum(1 for _, d in rel if d == 0.0)

    return {
        "a": a,
        "mu": mu,
        "mu_over_haar": mu / haar,
        "peak": peak,
        "peak_eta": peak_eta,
        "peak_over_haar": peak / haar,
        "peak_over_mu": peak / mu,
        "baseline": baseline,
        "peak_over_baseline": peak / baseline,
        "richest": rel[:3],
        "empty": empty,
        "classes": modulus // 2,
    }


def check_FUEL1(amax=5, n_bits=DOMAIN_BITS):
    """tau(x) >= ceil(a/alpha)+1 forces x into E_a, with no exceptions.

    Also prints the Walsh lower bound this containment forces, against the
    random-subset baseline.  The forced bound is independent of the domain
    size while the baseline decays like N^{-1/2}, so for each fixed a the
    forced bound dominates once N is large enough.
    """
    alpha = math.log2(3) - 1
    n = 1 << n_bits
    print("FUEL1: tau(x) >= t_a  ==>  x in E_a")
    for a in range(1, amax + 1):
        t = math.ceil(a / alpha) + 1
        modulus = 1 << t
        members = [2 * j + 1 for j in range(n)
                   if (2 * j + 1) % modulus == modulus - 1]
        bad = [x for x in members if not escapes(x, a)]
        if bad:
            raise AssertionError(f"FUEL1 violated at a={a}: {bad[:5]}")
        mu = sum(escapes(2 * j + 1, a) for j in range(n)) / n
        forced = (1 - mu) / (modulus - 1)
        baseline = random_subset_baseline(mu, n)
        print(f"  a={a} t_a={t:>2}: {len(members):>5} members checked, "
              f"0 counterexamples | forced max|A| >= {forced:.5f}, "
              f"random baseline {baseline:.5f}")
    print("  FUEL1 PASS\n")


def main(amax=5):
    check_FUEL1(amax)
    rows = [report(a) for a in range(1, amax + 1)]

    print(f"Domain: {1 << DOMAIN_BITS} odd integers 2j+1, j < 2^{DOMAIN_BITS};"
          f" step cap {STEP_CAP}\n")

    print("Measure and spectrum")
    print(f"{'a':>2} {'mu(E_a)':>9} {'2^-a':>8} {'mu/2^-a':>9} "
          f"{'max|A|':>9} {'/2^-a':>7} {'/mu':>7}")
    for r in rows:
        print(f"{r['a']:>2} {r['mu']:>9.4f} {2.0 ** -r['a']:>8.4f} "
              f"{r['mu_over_haar']:>9.3f} {r['peak']:>9.4f} "
              f"{r['peak_over_haar']:>7.3f} {r['peak_over_mu']:>7.3f}")

    print("\nComparison against a random subset of the same density")
    print(f"{'a':>2} {'max|A|':>9} {'random':>9} {'ratio':>7} {'argmax eta':>11}")
    for r in rows:
        print(f"{r['a']:>2} {r['peak']:>9.4f} {r['baseline']:>9.5f} "
              f"{r['peak_over_baseline']:>7.2f} {r['peak_eta']:>11d}")

    print("\nResidue structure mod 2^(a+2), normalized by observed mu(E_a)")
    print(f"{'a':>2} {'richest classes (residue, rel. density)':>46} "
          f"{'empty':>12}")
    for r in rows:
        rich = ", ".join(f"({res}, {d:.2f})" for res, d in r["richest"])
        print(f"{r['a']:>2} {rich:>46} {r['empty']:>5}/{r['classes']:<6}")

    print("\nFindings:")
    print("  * max |Ahat(eta)| tracks mu(E_a) at ratio ~0.50-0.56, and the")
    print("    ratio does NOT decay with a.  A white-noise set would instead")
    print("    scale like sqrt(mu/|D|); the observed peak exceeds that")
    print("    baseline by a factor of 2.5-13.")
    print("  * The argmax sits at the lowest frequencies (eta in {1, 3, 4}),")
    print("    i.e. at the bottom bits of x0 -- macroscopic structure, not")
    print("    high-frequency noise.")
    print("  * E_a concentrates on the residue 2^(a+2) - 1, the maximal")
    print("    trailing-one (fuel-rich) class, at ~12x the mean density by")
    print("    a = 5, while 15 of 64 odd classes are empty.")
    print("  * This is the residue-freezing of docs/no-go/no_local_potential.md")
    print("    reappearing in the escape set.  DISC1 as originally stated is")
    print("    contradicted by this data, not merely unproven.")


if __name__ == "__main__":
    main()
