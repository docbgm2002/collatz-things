# SH1-GEN: the Shadow No-Go for General Piecewise-Affine Integer Maps

**Building on:** `docs/no-go/shadow_certificate.md` (SH1)
**Status:** Proved here. Machine-checked in `scripts/verify_general_shadow.py`
(exact integer and rational arithmetic, 17 expanding cycles across 11 maps).
The theorem is conditional on the existence of an expanding rational cycle;
that hypothesis is non-vacuous in both directions.
**Ledger:** SHG1
**License:** CC-BY 4.0

---

## 1. What was tested and what came back

SH1 is stated for the \(3x{+}1\) map. Its `General principle` paragraph
already observes that nothing is special about the cycle \(-5\mapsto-7\)
*within that map*. The question here is one level up:

> Does the SH1 proof use anything about **3 and 2**, or only about the frame?

The answer is that it uses only the frame. Replacing \((3,2)\) by \((a,c)\)
throughout, every step of Lemma S and Theorem SH1 survives, and the only
place the specific pair mattered is a side condition on the **length**
coordinate, made precise in §4 below.

This matters because it moves the result out of Collatz. The object
\(T(x)=(ax+b)/c^{v_c(ax+b)}\) is a piecewise-affine integer map — in program
verification, a single-path linear-constraint loop — and \(\log_c x+g(\cdot)\)
is a **ranking function**. SH1-GEN is a ranking-function non-existence
theorem with a constructive certificate.

---

## 2. The map

Let \(c\) be prime, \(a\ge1\) with \(\gcd(a,c)=1\), and \(b\) with
\(\gcd(b,c)=1\). On integers coprime to \(c\) define

\[
T(x)=\frac{ax+b}{c^{\,v_c(ax+b)}} .
\]

\((a,b,c)=(3,1,2)\) is the accelerated odd Collatz map \(f\).

**Definitions.** A \(K\)-cycle \(\{y_1,\dots,y_K\}\) of \(T\) has *total
valuation* \(E=\sum_i v_c(ay_i+b)\) and *multiplier* \(a^K/c^E\). It is
**expanding** if \(c^E<a^K\). A coordinate is **\(c\)-adically local** if it
is determined by \(x \bmod c^{m}\) for some fixed \(m\) — this covers residues,
valuations, trailing-digit runs, and any finite suffix detector.

---

## 3. Theorem SH1-GEN

**Theorem.** Suppose \(T\) has an expanding \(K\)-cycle with total valuation
\(E\). Let \(m\ge0\) and let \(g\) be **any** real-valued function of
\(c\)-adically local data at depth \(m\). Then

\[
\Phi(x)=\log_c x+g(\text{local data})
\]

is not nonincreasing along \(T\) on positive integers coprime to \(c\).

*Proof.* Let \(y_1\) be a cycle member with valuation word
\((e_1,\dots,e_K)\). Fix \(N\ge m+E+1\) and take any positive
\(X\equiv y_1 \pmod{c^{N}}\).

**(a) The shadow reproduces the itinerary.** \(v_c(aX+b)\) is determined by
\(X \bmod c^{\,e_1+1}\), and \(N>e_1\), so \(v_c(aX+b)=e_1\) and
\(T(X)\equiv y_2 \pmod{c^{\,N-e_1}}\). Inductively, after \(i\) steps
\(T^i(X)\equiv y_{i+1} \pmod{c^{\,N-E_i}}\) with \(E_i=e_1+\cdots+e_i\), and
each valuation agrees with the cycle's, since \(N-E_i>0\) throughout.

**(b) Coordinates close.** At \(i=K\), \(T^K(X)\equiv y_1\equiv X
\pmod{c^{\,N-E}}\), and \(N-E\ge m\). So \(X\) and \(T^K(X)\) agree on every
\(c\)-adically local coordinate at depth \(m\): same residue, same valuation
word, same suffix detectors.

**(c) The value gains.** Unrolling the affine steps,

\[
c^{E}\,T^K(X)=a^K X+\beta,
\qquad
\beta=b\sum_{i=1}^{K}a^{K-i}c^{\,E_{i-1}}>0 ,
\]

so \(T^K(X)/X=a^K/c^E+\beta/(c^E X)>a^K/c^E>1\).

**(d) Contradiction.** If \(\Phi\) were nonincreasing, the \(K\) constraints
along \(X\to T(X)\to\cdots\to T^K(X)\) sum. By (b) the \(g\)-terms telescope
to zero, leaving

\[
0\ \le\ -\log_c\frac{T^K(X)}{X}\ <\ -\log_c\frac{a^K}{c^E}\ <\ 0 .
\]

\(\blacksquare\)

The Collatz instance is \((a,b,c)=(3,1,2)\), \(K=2\), \(E=3\), cycle
\(-5\mapsto-7\), multiplier \(9/8\), smallest witness
\(1275\mapsto1913\mapsto1435\) — exactly SH1.

---

## 4. The length coordinate, and where \((a,c)\) finally matters

SH1 also covers \(\mathrm{len}(x)\), the bit length. That step is the one
place the specific pair enters, and generalizing it produces a clean
dichotomy.

**Proposition.** The conclusion of SH1-GEN extends to corrections that
additionally read \(\mathrm{len}_c(x)\) **if and only if**

\[
\frac{a^K}{c^{E}}<c .
\]

*Reason.* \(\mathrm{len}_c\) closes iff \(X\) and \(T^K(X)\approx(a^K/c^E)X\)
lie in the same window \([c^{L-1},c^{L})\). A window has multiplicative width
\(c\), so a multiplier \(\ge c\) forces a carry out of the window for every
\(X\); a multiplier \(<c\) admits positions near the bottom of the window
where both fall inside, and the shadow parameter can be chosen to land there
(in SH1 this is precisely the role of \(w=2^{k-1}+1\)).

**Verified, 17/17 with no exceptions**, including the one case where the
condition fails: \((a,b,c)=(5,3,2)\) has two expanding cycles, at \(-1\) with
multiplier \(5/2>2\) (length does **not** close) and at \(-3\) with
multiplier \(5/4<2\) (length **does** close). Same map, both sides of the
dichotomy.

So \((3,2)\) was never doing work beyond supplying a multiplier \(9/8<2\).

---

## 5. Non-vacuity in both directions

The hypothesis is a real hypothesis:

- **Satisfied**, with genuinely multi-step cycles: \((7,3,2)\) has a
  \(K=5\) cycle at \(\{-43,-65,-113,-149,-197\}\), \(E=14\), multiplier
  \(16807/16384\); \((4,1,3)\) has \(K=4\) at \(\{-11,-19,-25,-43\}\);
  \((3,1,5)\) has \(K=6\); \((3,1,2)\) has the \(K=7\) cycle at \(-17\).
- **Not satisfied** in the searched range for \((7,1,2)\), \((11,1,2)\),
  \((5,1,3)\), \((7,1,3)\), \((11,1,3)\), \((7,1,5)\), \((4,1,5)\). This is a
  **statement about the search range only** and is not a proof of
  nonexistence. Locating the exact boundary — for which \((a,b,c)\) an
  expanding cycle exists — is open and is the natural next question.

---

## 6. Reading

For a piecewise-affine integer loop, an expanding rational cycle is a
**certificate factory against ranking functions**: it produces, for every
depth \(m\), an explicit positive integer witnessing that no ranking function
of the form \(\log_c x + g(\text{local data at depth } m)\) can exist. The
certificate is finite, exactly checkable, and constructed rather than
searched for.

What survives SH1-GEN is what survived SH1, transposed: corrections reading
information from the **top** of the number (leading digits, the fractional
part of \(\log_c x\)) and multi-step potentials. In the Collatz instance the
cost of pushing into the first of those is governed by the continued fraction
of \(\log_23\) (QLG1); the general statement should read \(\log_c a\).

---

## 7. Verification

`scripts/verify_general_shadow.py` — exact integer and rational arithmetic,
no floating point in any assertion:

- (0) the general frame reproduces the published SH1 witness
  \(1275\mapsto1913\mapsto1435\) with \(8f^2(x)=9x+5\);
- (a)-(c) itinerary reproduction, suffix closure mod \(c^{N-E}\), and exact
  value gain, over 17 expanding cycles across 11 maps;
- (e) the length dichotomy \(\mathrm{len}_c\) closes \(\iff a^K/c^E<c\),
  17/17 including the negative case;
- (6) non-vacuity of the hypothesis.

`scripts/explore_general_shadow2.py` is the exploratory search that found the
cycles.

```bash
python3 scripts/verify_general_shadow.py      # ALL PASS
```

---

## 8. Ledger row

| ID | Claim | Status | Source | Verification |
|---|---|---|---|---|
| SHG1 | For \(T(x)=(ax+b)/c^{v_c(ax+b)}\) with \(\gcd(a,c)=\gcd(b,c)=1\), \(c\) prime: if \(T\) has an expanding rational cycle (\(c^E<a^K\)) then no potential \(\log_c x+g(c\text{-adically local data})\) is nonincreasing; the \(\mathrm{len}_c\) coordinate is covered iff \(a^K/c^E<c\). SH1 is the \((3,1,2)\) instance | Proved here | `docs/no-go/general_shadow.md` | `scripts/verify_general_shadow.py`; 17 cycles across 11 maps; hypothesis non-vacuous both ways |
