# AGENT_HANDOFF_NEXT — load this first in a new chat

Status: **live spine cut = Gap SD-K-block-8-17 remainder**
(Cor SD-K-block-8-17-early closes density \(9/1024\) of \(k\), plus
\(n=81\)).
Date stamp: 2026-07-19 (EOD).
Do not reopen residual-atlas L5 / E_mix unless user explicitly asks.
Do not ledger-promote SD1/EC1/SD-L1 until a full human proof closes the gate.

---

## 0. One-line mission

Extend Cor SD-K-block-8-17-early. Closed progressions:
\(k\equiv3,171\pmod{256}\), \(k\equiv323\pmod{512}\),
\(k\equiv579\pmod{1024}\). Next: \(k\equiv11\pmod{64}\) and the
remaining \(67\bmod256\) slices (\(s\equiv0,4\pmod8\)).

---

## 1. Programme position

- Master: `docs/no-go/avenue_a_comparison_dynamics.md`
- Finite: `--check-block8-mod17`

---

## 2. What changed (this stamp)

- **Thm 171mod256:** \(\Delta_2+\Delta_3+\Delta_4=2+2+13=17\).
- **Thm 323mod512:** \(2+13+13=28\) (odd-\(s\) half of \(67\bmod256\)).
- **Thm 579mod1024:** \(2+13+4=19\) (\(s\equiv2\pmod4\) of \(67\bmod256\)).
- **Cor early:** density \(9/1024\) among \(k\), plus \(n=81\).

---

## 3. DO NEXT

1. \(k\equiv11\pmod{64}\) early blocks (cum \(6\) after four on
   \(11\bmod256\); need deeper).
2. \(k\equiv67\pmod{256}\) with \(s\equiv0\) or \(4\pmod8\) (variable
   high \(h_4\)).
3. \(k\equiv59\pmod{64}\) (cum \(-21\) after three).
4. EB-17 on unstructured remainder.

### Anti-patterns
- Prefer explicit block dictionaries over equidistribution EB.
- No ledger promotion; no git commit unless asked.

---

## 4. Success criteria

- [ ] Gap SD-K-block-8-17 for all \(n=64k+17\);
- [ ] or block-8 / 911-6-strong / survivor-6;
- [ ] or alternate \(K_\downarrow=n^{O(1)}\).

---

## 5. Key files

| Path | Role |
|---|---|
| `docs/no-go/avenue_a_comparison_dynamics.md` | early-block theorems |
| `scripts/verify_repunit_storage_dominance.py` | `--check-block8-mod17` |
