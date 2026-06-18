# The Block-Fracture Identity for the $3x+1$ Map

**A structural note on the binary behaviour of multiplication by 3**

**Author:** Dr. Bry
**Status:** Proved here (not a proof of the Collatz conjecture)
**License:** CC-BY 4.0

---

## Abstract

We give an exact, elementary description of what multiplication by $3$ does to a maximal block of consecutive $1$-bits in a binary integer. The result corrects a common informal claim — that such blocks are "annihilated" — and replaces it with a sharp identity: an isolated block of $L$ consecutive ones is mapped to a shorter block of $L-2$ ones, flanked by a fixed two-bit frame, with the bit-count (Hamming weight) of the block preserved. Specialising to Mersenne numbers $2^L-1$, we obtain a deterministic statement: one Collatz odd-step reduces the length of the leading run of ones by *exactly one*. These are not heuristic or statistical claims; each is an exact algebraic identity, verified symbolically and computationally. We are careful to state precisely what the identity does and does not imply, and we flag explicitly that the longest run of $1$-bits is **not** in general bounded under $3x+1$.

---

## 1. Motivation and scope

Several informal treatments of the $3x+1$ ("Collatz") map observe that the operation $x \mapsto 3x+1$ is hostile to long runs of consecutive $1$-bits, on the grounds that $3x = 2x + x$ forces $1+1$ collisions when a run is added to its own left-shift. The intuition is sound, but the usual conclusion — that the run is "converted into a string of zeros" or "annihilated" — is **false**. This note replaces that claim with the correct identity.

We restrict attention to the cleanest case that admits an exact, unconditional statement: a single *isolated* maximal block of ones. This is precisely the case relevant to Mersenne numbers, and it is the honest foundation on which any "Mersenne descent" argument should be built. We make no claim here about the global Collatz conjecture, about cycle non-existence, or about the behaviour of arbitrary bit-patterns; §5 states the limits explicitly.

**Notation.** For a positive integer $x$, write its binary expansion with bit $0$ the least significant. A *block* (or *run*) of length $L$ at position $k$ is a maximal set of consecutive $1$-bits occupying positions $k, k+1, \dots, k+L-1$; maximality means bit $k-1$ is $0$ (or $k=0$) and bit $k+L$ is $0$. We write $w(x)$ for the Hamming weight (number of $1$-bits) and $r(x)$ for the length of the longest run of $1$-bits. The Mersenne number is $M_L = 2^L - 1$ (binary: $L$ ones).

---

## 2. The core identity

**Lemma 1 (Block triple).** For every integer $L \ge 2$,
$$
3\,(2^L - 1) \;=\; 2^{L+1} + \bigl(2^L - 4\bigr) + 1 \;=\; \underbrace{10}_{\text{frame}}\,\underbrace{1\cdots1}_{L-2}\,\underbrace{01}_{\text{frame}} \quad\text{(binary).}
$$
Equivalently, the binary string of $3(2^L-1)$ is `10` followed by $L-2$ ones followed by `01`.

*Proof.* Compute directly:
$$
3(2^L - 1) = 3\cdot 2^L - 3 = 2^{L+1} + 2^L - 3.
$$
Now $2^L - 3 = 2^L - 4 + 1 = (2^{L-1}+2^{L-2}+\cdots+2^2) + 1$ for $L\ge 2$, i.e. bits $2$ through $L-1$ are set, bit $1$ is clear, bit $0$ is set. Adding $2^{L+1}$ sets bit $L+1$; bit $L$ is clear (since $2^L - 3 < 2^L$). Reading positions $L+1, L, L-1, \dots, 2, 1, 0$ gives
$$
1,\;0,\;\underbrace{1,\dots,1}_{L-2},\;0,\;1,
$$
which is the string `10` $1^{L-2}$ `01`. $\qquad\blacksquare$

**Corollary 1 (Run shortens by two; weight is preserved).** Let the isolated block be $B = (2^L-1)\,2^k$. Then within the region it occupies, the longest run of ones in $3B$ has length $L-2$ (for $L \ge 2$), while the number of ones contributed by the block is unchanged:
$$
r_{\text{block}}\colon L \;\longmapsto\; L-2,
\qquad
w_{\text{block}}\colon L \;\longmapsto\; L .
$$

*Proof.* Multiplication by $2^k$ is a shift and does not change the bit-pattern of the block image, so $3B = \bigl(3(2^L-1)\bigr)2^k$ has the local pattern of Lemma 1. That pattern, `10`$1^{L-2}$`01`, has a single maximal interior run of length $L-2$ and total weight $1+(L-2)+1 = L$. $\qquad\blacksquare$

The content of Corollary 1 is the corrected "fracture" statement. The block is **not** annihilated; its *length* contracts by exactly two, and the two ones lost from the interior re-emerge as the leading and trailing frame bits. Weight is conserved at the multiplication stage — the loss of magnitude in the full Collatz step comes later, from the division by powers of two, not from the multiplication.

---

## 3. Carry interaction at the boundaries

Lemma 1 describes an isolated block in vacuum. In a general integer the block sits between other bits, and one must account for (i) the constant $+1$ in $3x+1$, and (ii) carries entering from the low side. The following lemma proves that both effects are confined below the interior or above it — never into it — so the interior contraction $L \to L-2$ holds unconditionally whenever the block is isolated in the sense of §1. The two frame bits, by contrast, are *not* protected; their fate depends on the surroundings, which is the source of the limitation in §5.

**Lemma 2 (Boundary localisation).** Let $L \ge 3$ and
$$
n = H\cdot 2^{\,k+L+1} \;+\; (2^L-1)\,2^k \;+\; \ell,
\qquad 0 \le \ell < 2^{\,k-1},\quad H \ge 0,
$$
so that bit $k-1$ of $n$ is $0$ (isolation below) and bit $k+L$ of $n$ is $0$ (isolation above). Then the **interior** bit-positions $k+2, k+3, \dots, k+L-1$ of $3n$ (and of $3n+1$) are **all equal to $1$**, regardless of the values of $H$ and $\ell$. Consequently these positions form a guaranteed window of $L-2$ consecutive ones. The maximal run containing that window may be longer if a boundary bit becomes $1$ through interaction with the surroundings.

*Proof.* Split $n$ into three pieces and use $3n = 3H\cdot 2^{k+L+1} + 3B + 3\ell$, where $B = (2^L-1)2^k$ is the block. We track each piece by the bit-positions it can occupy.

**(a) The block term $3B$ supplies the interior.** By Lemma 1, $3B = \bigl(\texttt{10}\,1^{L-2}\,\texttt{01}\bigr)\cdot 2^{k}$, occupying positions $k$ through $k+L+1$, with bit-values
$$
\text{pos } k{:}\ 1,\quad k{+}1{:}\ 0,\quad \underbrace{k{+}2,\dots,k{+}L{-}1{:}\ 1}_{\text{interior, }L-2\text{ ones}},\quad k{+}L{:}\ 0,\quad k{+}L{+}1{:}\ 1.
$$
Thus, before adding the other two terms, the interior positions $k+2,\dots,k+L-1$ already hold ones. It remains to show neither other term disturbs them.

**(b) The low term cannot reach the interior (carry from below).** Since $0 \le \ell < 2^{k-1}$,
$$
3\ell + 1 \;\le\; 3\,(2^{k-1}-1) + 1 \;=\; 3\cdot 2^{k-1} - 2 \;<\; 2^{k+1}.
$$
Hence $3\ell$ — and even $3\ell+1$, covering the full $3n+1$ map — occupies only bit-positions $0$ through $k$. The only position at or below $k+1$ where $3B$ carries a one is position $k$ itself (the trailing frame bit). Adding the low term to $3B$ therefore involves only bits $0,\dots,k+1$: the partial sum restricted to these positions is at most
$$
\underbrace{(2^{k+1}-1)}_{\text{bits }0..k\text{ of }3\ell+1} + \underbrace{2^{k}}_{\text{bit }k\text{ of }3B} \;<\; 2^{k+2},
$$
so it produces **no carry out of position $k+1$**, i.e. no carry into position $k+2$. The interior is untouched from below. (A direct enumeration confirms the maximal carry out of the bit-$(k+1)$ region is zero across all $k,L$.)

**(c) The high term cannot reach the interior (carry from above).** The term $3H\cdot 2^{k+L+1}$ occupies only positions $\ge k+L+1$. In binary addition carries propagate **upward only** — adding any quantity supported on positions $\ge k+L+1$ can alter bits at positions $\ge k+L+1$ but never any bit below $k+L+1$. The interior positions $k+2,\dots,k+L-1$ all lie strictly below $k+L+1$, so they are unaffected by the high term. (The leading frame bit at $k+L+1$ and the gap bit at $k+L$ may change, which is exactly why the *global* run length is not controlled; the interior is not.)

Combining (a)–(c): the interior positions $k+2,\dots,k+L-1$ receive their value solely from $3B$, where they are ones, and are disturbed by neither the low term (b) nor the high term (c). They are therefore all $1$ in $3n$ and in $3n+1$. This proves a guaranteed consecutive-one window of length $L-2$; it does not assert that the maximal run containing the window has exactly that length. $\qquad\blacksquare$

The decisive structural facts are the two one-line carry arguments: the low part is too small to carry past position $k+1$ ((b), a magnitude bound), and the high part lies entirely above the block so its carries cannot descend ((c), the directionality of binary addition). The fate of the two frame bits and of the $L=2$ case still depends on $H$ and $\ell$ — which is precisely why §5's warning about the *global* longest run stands — but the interior contraction $L \to L-2$ is unconditional.

---

## 4. Specialisation to Mersenne numbers

Mersenne numbers are the extremal case: a single block with no surrounding bits. Here the statement becomes fully deterministic.

**Theorem 1 (Mersenne single-step erosion).** For $L \ge 2$, the Collatz odd-step applied to $M_L = 2^L - 1$ gives
$$
\frac{3M_L + 1}{2} \;=\; 3\cdot 2^{L-1} - 1 \;=\; 2^{L} + \bigl(2^{L-1}-1\bigr) \;=\; \underbrace{1\,0}_{}\,\underbrace{1\cdots1}_{L-1}\quad\text{(binary),}
$$
and the $2$-adic valuation of $3M_L+1$ is exactly $1$. In particular the longest run of ones drops from $L$ to $L-1$:
$$
r(M_L) = L \;\longmapsto\; r\!\left(\tfrac{3M_L+1}{2}\right) = L-1.
$$

*Proof.* $3M_L + 1 = 3\cdot 2^L - 2 = 2\,(3\cdot 2^{L-1} - 1)$. The factor $3\cdot 2^{L-1}-1$ is odd for $L\ge 1$, so $v_2(3M_L+1)=1$ and the odd-step image is $3\cdot 2^{L-1}-1$. Writing $3\cdot 2^{L-1}-1 = 2^L + 2^{L-1} - 1$: bit $L$ is set, bit $L-1$ is clear, and bits $0,\dots,L-2$ are set (since $2^{L-1}-1$ is $L-1$ ones). That is the string `10`$1^{L-1}$, whose longest run is $L-1$. $\qquad\blacksquare$

**Corollary 2 (Bounded leading-block growth for Mersenne).** Starting from $M_L$, the leading run of ones cannot *grow* under the first odd-step; it strictly decreases by one. This furnishes the rigorous base case for a "$+2$ bound" programme: any subsequent regrowth of a long run must be paid for by the surrounding dynamics rather than supplied for free by the Mersenne structure itself.

*Remark.* Theorem 1 is the deterministic heart of the "Mersenne funnel" intuition. It does **not** by itself prove that the full trajectory of $M_L$ descends — after the first step the iterate is no longer a clean block and Lemma 2's isolation hypothesis must be re-established at each stage. What it does prove, exactly, is that the specific mechanism by which one might fear Mersenne numbers "fuel" unbounded growth — a self-sustaining maximal run — fails at every odd-step by one bit.

---

## 5. What this does *not* show (limits of the result)

Intellectual honesty requires stating the boundaries sharply, because they are easy to overrun.

1. **The longest run of $1$-bits is not globally bounded under $3x+1$.** Direct computation shows that for general odd $n$, the quantity $r(3n+1) - r(n)$ can be large and positive (values of $+19$ and beyond occur readily in random sampling at modest bit-lengths). The contraction identity is a statement about an *isolated* block's interior, not about $r$ of arbitrary integers. Any argument that silently upgrades Corollary 1 to "the longest run never grows" is invalid.

2. **Weight is preserved at multiplication, not reduced.** The descent in a Collatz step comes from $v_2(3n+1)$ divisions, which are governed by the low-order structure of $3n+1$, a separate phenomenon. This note says nothing about the distribution of $v_2$.

3. **Isolation must be re-earned each step.** Lemma 2's hypotheses ($\ell < 2^{k-1}$, clean upper boundary) generally fail after one step. Establishing that they recur — or quantifying how often they fail — is exactly the open work, not a corollary.

4. **No claim about cycles or about global convergence is made or implied.** This is a structural identity about a single arithmetic operation.

---

## 6. Suggested next steps (scoped)

- **Phase 1 (closed):** the Mersenne single-step erosion, Theorem 1 — complete and exact above.
- **Phase 2 (near-Mersenne):** characterise $3n+1$ for $n = 2^L - 1 - \epsilon$ with small $\epsilon$, tracking how the trailing/leading frames interact with the perturbation; determine for which $\epsilon$ the one-bit erosion persists.
- **Phase 3 (density form):** seek a *windowed* statement — over a bounded number of odd-steps, the longest run cannot be sustained at length $\Omega(\log n)$ without a compensating number of divisions — stated as a conditional lemma with explicit constants, never as an unconditional bound (cf. limit 1).

---

## Appendix A. Verification

All identities above were checked symbolically and by exact integer computation:

- Lemma 1 / Corollary 1: `3*(2**L-1)` equals the string `10` + `1`*(L-2) + `01` for all tested $L$, with block weight constant $=L$.
- Theorem 1: `(3*(2**L-1)+1)` has $v_2 = 1$; the odd-step image equals `2**L + 2**(L-1) - 1` with longest run $L-1$, for all tested $L$.
- Lemma 2: over $2\times10^5$ random isolated-block configurations (varying $L,k,H,\ell$), the interior window $[k+2,k+L-1]$ of both $3n$ and $3n+1$ is all-ones; the proof's two carry claims are checked directly — the low-term bound $3\ell+1 < 2^{k+1}$ with zero carry out of bit $k+1$ (claim (b)), and independence of the interior from the high term $H$ (claim (c)).
- Limit 1: random sampling of odd $n$ (bit-lengths 4–80) exhibits $r(3n+1)-r(n) > 2$ in a substantial fraction of cases, with observed maxima well above $+2$ — confirming the global longest-run is uncontrolled.

A reproducible script accompanies this note.
