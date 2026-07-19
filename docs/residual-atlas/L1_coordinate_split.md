# L1: Coordinate-C split

**Status:** Bookkeeping formalization. Not mathematical progress beyond
IEF19. Intended for immediate use so L2 and L3 do not share an “or.”

**Logical role:** classification only.

**Dependencies:** IEF16, IEF17, IEF19 (`docs/repunit/integral_escape_frontier.md`).

## 1. Setup

Let \(\mathcal R\) be the IEF17 residual: non-cyclic itineraries in the
\(3/4\)-block terminal language satisfying coordinates A--E of
`RESIDUAL_ATLAS.md`.

Coordinate C asserts

\[
\operatorname{dio}(w)=1
\quad\text{or}\quad
\limsup_{L\to\infty} S_L/L > 0.
\]

Write

\[
\overline s(w)=\limsup_{L\to\infty}\frac{S_L}{L}.
\]

## 2. Definitions

\[
\mathcal R_+
=
\{w\in\mathcal R:\overline s(w)>0\},
\]

\[
\mathcal R_1
=
\{w\in\mathcal R:\overline s(w)=0\}.
\]

## 3. Partition lemma (L1)

> **L1.** The sets \(\mathcal R_+\) and \(\mathcal R_1\) are disjoint, their
> union is \(\mathcal R\), and every \(w\in\mathcal R_1\) satisfies
> \(\operatorname{dio}(w)=1\).

**Proof.** Disjointness is immediate from the definitions. If
\(w\in\mathcal R\), then either \(\overline s(w)>0\), hence
\(w\in\mathcal R_+\), or \(\overline s(w)=0\), hence \(w\in\mathcal R_1\).
In the latter case coordinate C and \(\overline s(w)=0\) force
\(\operatorname{dio}(w)=1\). \(\square\)

**Remark.** Membership in \(\mathcal R_+\) does not forbid
\(\operatorname{dio}(w)=1\). The positive-limsup branch may still be
highly repetitive; L3 must allow that overlap.

## 4. Residual after L1

\[
\mathcal R=\mathcal R_1\,\dot\cup\,\mathcal R_+.
\]

No itinerary is removed. Proof obligations for L2 and L3 are now separate:

| Subclass | Proposed next attack | Must not assume |
|---|---|---|
| \(\mathcal R_1\) | L2 recurrence tax | positive linear excursions |
| \(\mathcal R_+\) | L3 excursion localization | \(\operatorname{dio}(w)=1\) |

## 5. Ledger note

This statement is definitional given IEF19. It may be cited inside the
side project without a new claim-ledger row unless a downstream note needs
an explicit ID. If promoted, suggest claim ID `ATL1` with status
“Proved here” and source this file, dependency IEF19.
