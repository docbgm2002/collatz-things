# Repunit Bad-Automaton Notes

**Building on:** `repunit_tail_attack.md`, `stopping_time_density.md`
**Status:** Exploratory. This records a attempted residue-class route and what it rules out.

---

## 1. The idea

For a fixed valuation pattern

$$
e=(e_0,\ldots,e_{K-1}),\qquad E=\sum e_i,
$$

the shortcut map determines a unique odd residue class

$$
x\equiv r(e)\pmod {2^E}
$$

with that exact valuation pattern.

For the repunit

$$
a_n=\frac{3^n-1}{2},
$$

membership in this class is equivalent to

$$
3^n\equiv 2r(e)+1\pmod {2^{E+1}}.
$$

Thus the first natural hope was:

> maybe the low-valuation bad patterns mostly miss the cyclic curve `3^n mod 2^m`.

If true, the density theorem could be sharpened for the explicit repunit family.

---

## 2. What the experiment shows

`explore_repunit_bad_automaton.py` enumerates low-total valuation patterns with

$$
E\le \lfloor K\log_2 3\rfloor
$$

and tests whether their residue class intersects the repunit curve.

For small `K`, the bad classes do **not** disappear. A substantial fraction remain compatible:

```text
K= 9:  2002 bad patterns,   715 curve-compatible
K=10:  3003 bad patterns,  1001 curve-compatible
K=11: 12376 bad patterns,  4368 curve-compatible
K=12: 50388 bad patterns, 18564 curve-compatible
```

Adding the exact first-payout condition

$$
v_2(3a_n+1)=1+v_2(n+1)
$$

does not reduce these counts. If a full valuation pattern intersects the repunit curve, its first valuation is already consistent.

So the proof will not be a one-step forbidden-residue argument.

---

## 3. Interpretation

The residue-class approach still gives a useful reframing:

* low-valuation patterns are explicit residue classes;
* the repunit family is an explicit cyclic subgroup/coset modulo powers of two;
* the missing theorem is a **long-range non-shadowing** statement, not local incompatibility.

In other words, individual bad strings often intersect the repunit curve. What we need to prove is that the actual repunit index `n` cannot keep selecting compatible bad strings through a window as long as `3n`.

The next possible refinement is to avoid counting patterns independently and instead build a nested automaton over the index `n`: after each valuation constraint, track the surviving residue classes of `n` modulo the current power of two. If those surviving classes thin out faster than the allowed window grows, that could become a proof.

---

## 4. Verification

Run:

```bash
python3 explore_repunit_bad_automaton.py
```

This is exploratory only. It proves no new theorem; its value is identifying that the naive curve-intersection obstruction is too weak.
