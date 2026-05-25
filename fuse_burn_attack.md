# Fuse-Burn / Recharge Attack

**Status:** exact lemmas + exploratory proof programme; not a proof

This note records the strongest structural consequence found by combining the
Rail-7 work with the Block-Fracture perspective.

---

## 1. Exact fuse-burn lemma

For odd `x`, define

$$
\tau(x)=v_2(x+1),
$$

the length of the trailing block of `1` bits in the binary expansion of `x`.

If `L = \tau(x) \ge 2`, then

$$
x = 2^L m - 1
$$

for some odd `m`. The shortcut Collatz map gives

$$
f(x)=\frac{3x+1}{2^{v_2(3x+1)}}
     =3\cdot 2^{L-1}m-1.
$$

Since `L-1 >= 1`, the right-hand side is odd and

$$
\tau(f(x)) = L-1.
$$

Thus a trailing block of length `L >= 2` burns down by exactly one under each
shortcut odd-step. Iterating for `L-1` steps gives

$$
f^{L-1}(x)=2\cdot 3^{L-1}m-1,
$$

which has trailing-one fuel `1`.

This is the suffix version of the Block-Fracture principle: long blocks of ones
do not preserve themselves for free.

---

## 2. The global fuse map

The next shortcut step is the first point at which a large division may occur.
Let

$$
s = v_2(3^L m - 1).
$$

Then the full burn-plus-payout macro is

$$
2^L m - 1
\quad\longmapsto\quad
\operatorname{oddpart}(3^L m - 1)
=\frac{3^L m - 1}{2^s}.
$$

This formula also covers the case `L=1`, so it defines a global accelerated
map on odd integers:

$$
\Phi(2^L m - 1)=\operatorname{oddpart}(3^L m - 1).
$$

Each application of `\Phi` compresses one complete trailing-one fuse episode:
burn the suffix of ones down to length `1`, then take the payout division.

The macro descends in raw value exactly when

$$
\frac{3^L m - 1}{2^s} < 2^L m - 1.
$$

Asymptotically, this requires roughly

$$
s > L\log_2(3/2).
$$

So the hard case is not the burn. The burn is exact. The hard case is small
payout valuation `s`.

---

## 3. Exact recharge congruence

Suppose the burn-plus-payout output has new trailing-one fuel `K`:

$$
\tau\!\left(\frac{3^L m - 1}{2^s}\right) \ge K.
$$

This is equivalent to

$$
\frac{3^L m - 1}{2^s} \equiv -1 \pmod {2^K},
$$

hence

$$
3^L m - 1 \equiv -2^s \pmod {2^{K+s}},
$$

or

$$
m \equiv 3^{-L}(1-2^s) \pmod {2^{K+s}}.
$$

Because `3` is invertible modulo every power of `2`, this is a single residue
class modulo `2^{K+s}`.

**Recharge Cost Lemma candidate.** After a fuse of length `L` burns with payout
valuation `s`, creating a new fuse of length at least `K` forces the odd
cofactor `m` into one specific residue class modulo `2^{K+s}`.

This is the useful exact statement: long fuel can be created, but only through
a narrow low-bit alignment.

---

## 4. What this gives and what it does not

This does **not** prove Collatz. A single trajectory may keep hitting special
residue classes, and ruling that out is the real problem.

But it changes the shape of the attack:

1. Long-fuse growth is exactly accounted for by `L`.
2. The dangerous small-payout case is exactly accounted for by `s`.
3. Recharging new fuel of length `K` costs `K+s` low bits of congruence.

So a proof should try to show that an infinite ascent would require an infinite
sequence of increasingly restrictive congruences that are incompatible with the
same odd cofactor evolving through the burn maps.

---

## 5. Computational observations

The script `explore_fuse_burn.py` verifies the formulas above for all odd
`x <= 10^6`.

It also shows why one-step descent is too much to ask:

- for large `L`, most burn-plus-payout macros grow;
- the payout valuation `s` is distributed geometrically in samples;
- the next fuel length averages close to `2`, almost independent of `L`.

Under the global fuse map `\Phi`, the worst case from the earlier finite-window
test,

$$
x=626331,
$$

becomes a chain of `41` fuse episodes before falling below its start. Scanning
larger finite windows found longer chains (`61` episodes up to `10^7`), so a
fixed small episode bound is not plausible.

The promising fact is not immediate descent or bounded episode count. It is that
repeated growth requires repeated low-bit coincidences of the recharge
congruence above.

---

## 6. Next proof target

The next theorem to seek is a compatibility obstruction:

> No trajectory can realize an infinite sequence of burn-plus-payout growth
> macros whose recharge congruences keep restoring enough fuel to offset the
> accumulated growth.

Equivalently, prove that every sufficiently long chain of `\Phi`-growth macros
must contain a payout whose valuation is large enough to force descent, or must
merge into a smaller certified class.

In this form, the Collatz problem becomes:

> Show that every orbit of the accelerated fuse map `\Phi` eventually drops
> below its starting value.

This is not easier in a trivial sense, but it isolates the exact role of
Block-Fracture: all growth is now expressed as a sequence of fuse lengths `L`,
payout valuations `s`, and recharge congruences.
