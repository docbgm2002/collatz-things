# Self-Review Log — no-go program proofs (2026-07-02)

Adversarial pass over the three items previously flagged for review. This
does not replace an external read; it records what was checked, what
held, and the two minor items found. Complemented by the independent
certificate check below.

## 1. Tower Theorem T1(d) — the no-carry claim

Re-derived skeptically. The identity
(2^(M-1)-1)/3^d = B_d * sum_{i<s} 2^(ord*i) is exact algebra; the
carry-free claim rests on 0 <= B_d < 2^ord, which makes the right side a
base-2^ord number all of whose digits equal B_d — airtight. Blocks must
be zero-padded to ord bits (the verifier's zfill does this). The "+1"
and the 2^(2d+1) shift cannot interact (lowest set bit of the shifted
word is at position >= 2d+1 >= 3). **Verdict: sound.**
*Minor:* the abstract's gloss "exactly periodic binary word" refers to
the repeated-block region; w_d itself is (trailing 1) + (shift) +
(periodic region). T1(d)'s formal statement is already precise; no
change required, but a referee may ask — the gloss could say
"periodic-block normal form".

## 2. Theorem T2 / Theorem C — the subsequence argument

Checked: burn constraint quantifiers (t0 = max(m+1,5) covers residue
freeze at t-1 >= m and mod-16 blindness at t-1 >= 4); inequality
directions on both burn and cap; the telescoped cap bound
log2(w_L/w_0) < L log2(4/3) from per-step ratios in (3/4,1);
coordinate finiteness of w_L(M) uniformly over the progression
(residue freeze threshold M-1 >= m; tau = 1; detector bounds via D.3
with nu = 2i+1, threshold M > 2i+2, i in S, i != L guaranteed by
L = max(S)+1); the pigeonhole over an infinite progression with finitely
many thresholds; and that growth (1) holds at every integer M > t0, so
contradiction on any infinite subsequence suffices. Smallest-template
cases in Lemma D.2 (w_1(3) = 9, w_2(7) = 225) are handled directly, with
B(e) covering M >= 5. **Verdict: sound.**

## 3. Corridor Rate Theorem 1b — measure-change bookkeeping

Re-derived dP/dQ = M(u)^n u^(-E_n); on the window
E_n in [mu n - dK/2, mu n + dK/2] with u < 1 the bound
u^(-E_n) >= u^(-mu n) u^(dK/2) is the right direction;
M(u)^n u^(-mu n) = e^(-n I(mu)) because u is chosen as the Legendre
optimizer (tilted mean = mu); the final jump is untilted and
independent; below-line and within-budget hold on the event.
**Verdict: sound.**
*Minor:* the buffer's forced e=1 prefix shifts E_n accounting by at most
b = O(1); this sits inside the dK/2 window slack but should be tracked
explicitly in a journal version (one sentence).

## 4. Independent certificate check (new)

`scripts/verify_nogo_certificate.py`: the no-go constraint system on any finite
coordinate window is a difference-constraint system; infeasibility is
equivalent to a directed cycle of value-ratio product > 1 in the
coordinate graph of observed real steps. Bellman–Ford over odd
x <= 10^6, with exact Fraction confirmation of any candidate cycle:

- NLP1 window (mod 16, tau): INFEASIBLE via a length-2 cycle,
  witnesses 57 -> 43 and 27 -> 41, product 1763/1539 > 1. This is a
  complete two-line proof of Theorem A for m <= 4, using no designed
  family. The pair separates mod 32, confirming that the families'
  role is uniformity in m.
- NLP2 window (mod 16, tau, lambda_1 <= 10): INFEASIBLE via a length-5
  cycle with witnesses [27, 41, 31, 15, 7] — the mined cycle passes
  through 41 = x'_5 -> 31 = 2^5 - 1, i.e. the search rediscovered the
  recharge mechanism unprompted.

Logical status: this check uses no lemma from the notes and would have
refuted the theorems had a valid correction existed on the tested
windows. It cannot, by construction, verify the unbounded-coordinate
content of the theorems; that is exactly the part carried by the
burn/recharge families and the tower.

## Remaining for external review

Unchanged: manual read of the annotated bibliographies and Wirsching
chs. 2–3 (BIBLIOGRAPHY_PASS.md); human adversarial read, especially of
the two *Minor* items above; author block.
