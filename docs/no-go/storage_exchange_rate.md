# The Storage Exchange Rate: a No-Go for Local Deficit Arguments

**Building on:** `docs/repunit/repunit_extremal_principle.md` (REPEXT1-3)
**Status:** Proved here. This is an impossibility statement about a *class of
arguments*, in the same sense as SH1 and BND1 — not a statement about the
orbits themselves. Machine-checked in exact rational arithmetic by
`scripts/verify_storage_exchange_rate.py`.
**Ledger:** EXR1
**License:** CC-BY 4.0

---

## 1. Why this is stated separately

`repunit_extremal_principle.md` §9 records the observation that, on a
valuation-one step, "deficit storage is not locally more expensive than
deficit accumulation: the exchange rate is exactly one." That sentence is the
sharpest thing in the extremal programme and it was sitting unlabelled at the
bottom of a 609-line exploratory note. It is a no-go, it has the same logical
shape as the no-go theorems in the manuscript, and it should be cited as one.

Its practical function is to kill a whole family of proof attempts before they
are attempted: any argument that hopes to derive a contradiction from a long
valuation-one run, using only the data of that run, is doomed.

---

## 2. Coordinates

Fix an odd exponent \(n\) and follow the repunit tail \(x_K=f^{(K)}(a_n)\)
in the exact normal form of `repunit_normal_form_notes.md`:

\[
x_K=\frac{3^{\,n+K}+A_K}{2^{E_K+1}},
\qquad
e_K=v_2(3x_K+1),
\qquad
E_{K+1}=E_K+e_K .
\]

Following REPEXT1, set

\[
R_K=A_K+2^{E_K+1},
\qquad
Z_K=\frac{R_K}{2^{E_K+1}},
\qquad
D_K=K\log_23-E_K .
\]

\(D_K\) is the running **deficit** (the shortfall of accumulated halvings
against neutral growth); \(Z_K\) is the **storage coordinate**, carrying the
correction that the tail has accumulated. The raw surplus is \(S_K=-D_K\).

REPEXT1 gives the exact successor law

\[
Z_{K+1}=1+\frac{3Z_K-2}{2^{e_K}} .
\tag{2.1}
\]

---

## 3. The theorem

**Theorem (EXR1).** Suppose \(e_K=1\). Then

1. \(Z_{K+1}=\tfrac32 Z_K\);
2. \(D_{K+1}-D_K=\log_23-1=\log_2\tfrac32\);
3. consequently \(D_K-\log_2Z_K\) is invariant, and remains invariant
   throughout any maximal valuation-one run.

*Proof.* (a) Substituting \(e_K=1\) into (2.1),

\[
Z_{K+1}=1+\frac{3Z_K-2}{2}=\frac{2+3Z_K-2}{2}=\frac32 Z_K .
\]

(b) \(e_K=1\) means \(E_{K+1}=E_K+1\), so

\[
D_{K+1}-D_K=(K+1)\log_23-(E_K+1)-K\log_23+E_K=\log_23-1 .
\]

(c) By (a), \(\log_2Z_{K+1}-\log_2Z_K=\log_2\tfrac32\), which is exactly the
increment in (b). The difference \(D_K-\log_2Z_K\) is therefore unchanged by
the step, and by induction through the whole run. \(\blacksquare\)

Both increments equal \(\log_2\frac32\). **The exchange rate between
accumulating deficit and storing it is exactly one.**

---

## 4. What this excludes

**Corollary (the no-go).** No argument that uses only the valuation-one
portion of a repunit tail — its length, its position, its storage coordinate,
or any function of the run's own data — can establish that deficit storage is
unsustainable, or derive a strict inequality bounding the attainable deficit.

*Proof.* Any such argument would have to produce a quantity that strictly
degrades along the run. By Theorem (c), the natural candidate
\(D_K-\log_2Z_K\) is exactly conserved, and \(D_K\) and \(\log_2 Z_K\)
individually move at identical rates. A strict inequality would have to come
from data the run does not contain. \(\blacksquare\)

This is why the low-prefix construction of
`docs/repunit/repunit_low_prefix_obstruction.md` is so effective as an
obstruction: it produces arbitrarily long valuation-one runs, and by EXR1
nothing local can be charged against them.

It also explains, retrospectively, why the fixed 256-block floor and the
variable-window recovery proposal both failed. Both were local arguments over
valuation data. EXR1 says the failure was structural, not a matter of tuning
the window.

---

## 5. Where a strict inequality must come from

Theorem (c) leaves exactly three sources of strictness, all of them
*historical* rather than local:

1. **Payout ancestry.** The ledger \(B_K\) of REPEXT3,
   \(B_K=\tfrac12+\sum_{j<K,\ e_j>1}w_j\) with
   \(w_j=(1-2^{1-e_j})2^{-D_{j+1}}\). Only the \(e_j>1\) steps enter, and
   they are precisely the steps EXR1 does not cover.
2. **Primitivity.** The assumption that the tail has not merged into a
   smaller exponent's tail is not visible in the local data.
3. **Collision structure.** The shell arithmetic of REPEXT4-5 and GAPMRG1.

The open target stated at the end of `repunit_extremal_principle.md` (the
primitive ancestry-amortization theorem) is correctly aimed: it charges the
present stored correction to the earlier payouts that created it. EXR1 is the
proof that this historical framing is not merely convenient but *necessary*.

**Warning retained from the source note.** A correct statement must not assert
that current surplus and current deficit are both large, since \(S_K=-D_K\).
The conclusion of any successor theorem must be a bound on \(D_K\), a descent,
or a merge.

---

## 6. Verification

`scripts/verify_storage_exchange_rate.py` checks, in exact rational
arithmetic with no floating point in any assertion:

- (a) \(Z'=\tfrac32Z\) on \(e=1\) over 2800 rational states;
- (a') the identity genuinely fails for \(e=2,3,4\), so the hypothesis is not
  vacuous;
- (b) the deficit increment in exact multiplicative form
  \(2^{D_{K+1}-D_K}=3/2\) over 18000 \((K,E)\) pairs;
- (c) invariance of \(2^{D_K}/Z_K\) through 12-step valuation-one runs from
  800 starting states;
- (d) equality of the storage factor and the deficit factor.

```bash
python3 scripts/verify_storage_exchange_rate.py   # ALL PASS
```

---

## 7. Ledger row

| ID | Claim | Status | Source | Verification |
|---|---|---|---|---|
| EXR1 | On a valuation-one step of a repunit tail the storage coordinate and the running deficit both scale by exactly \(3/2\); hence \(D_K-\log_2 Z_K\) is invariant through any valuation-one run, and no argument using only valuation-one data can show that deficit storage is unsustainable | Proved here (impossibility for a class of arguments) | `docs/no-go/storage_exchange_rate.md` | `scripts/verify_storage_exchange_rate.py`; depends on REPEXT1-2 |
