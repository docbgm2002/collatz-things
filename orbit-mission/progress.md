Original prompt: Build a more usable game simulation for Collatz: click Play, understand what the mathematics does, try different formulas, and replay the history of formulas and contributions.

## Design and scope

- Orbit Mission is a browser game about integer rules. Space is an explicitly labelled metaphor, not a model of gravity or galaxies.
- Players can watch, step, rewind, predict the next move, change a rule, save/replay runs, compare runs, and export evidence.
- Exact BigInt arithmetic; finite runs end at 1, a detected repeated value, or an explicit resource limit. Reaching 1 is the game's stop convention.
- Code lives in a companion folder on Niyi/orbit-mission, based on current upstream main (the correction PR is now merged).
- No backend, accounts, paid service, or external assets are needed.

## Progress

- Initialized isolated worktree and fetched upstream before building.
- Exact engine and unit checks delegated; history/provenance documentation delegated.

## Verification

- All 14 exact-arithmetic/evidence unit tests pass.
- Ran the develop-web-game Playwright client after each meaningful gameplay revision; inspected both its canvas screenshots and full desktop/mobile screenshots.
- Independent browser checks cover play/pause, previous/next, restart, prediction scores, autoplay home/cycle completion, odd steps, invalid configurations, unresolved limits, persistence, comparison, export/import, tamper rejection, help, fullscreen, history, and 320/375px layouts.
- Final browser regression run: 21/21 checks pass, zero browser errors. This includes monotonic outward movement, Same predictions, and an exact 60-digit input on a 320px screen.
- Found and fixed straight-line movement that briefly moved inward on an increasing-number step. Polar interpolation now preserves radial direction, with a browser regression check.
- Found and fixed clipped playback controls at 320px. Controls wrap without page or panel overflow.
- Bounded large-integer readouts retain an expandable exact value; calculations and exports remain exact.

## Next steps

- Gather feedback on whether first-time players can explain the even/odd rule and distinguish home, cycle, and unresolved outcomes.
- Shared experiment storage, authenticated contribution attribution, and research-grade certificates remain future work. Flight histories remain local browser records; research milestones are curated Git snapshots.
- Local preview is served with `python3 orbit-mission/serve.py --port 8767`; this is not a deployed public service.

## Project history follow-up

- User reported that Project history did not show the latest PR. The original list was a fixed selection of commits.
- Pulled upstream main at 8b5d769 (merged Orbit Mission PR #5) before creating Niyi/live-project-history.
- Added a public GitHub PR feed with status labels, a manual refresh, and one-minute throttling for automatic tab-open checks. No credentials or saved flight data are sent.
- Kept research milestones separate; added the actual UI merge and retained the mathematical baseline. App release is now 0.1.1.
- Bundled a timestamped fallback containing PR #6; unsuccessful refreshes retain data with an explicit error and source timestamp.
- Verification: 25 unit checks, 21 gameplay browser checks, and 10 focused history browser checks pass. The game client still plays correctly; desktop and 320/375px history screenshots were inspected.
- Confirmed an actual successful public GitHub refresh in the local in-app browser: PR #6 open and PR #5 merged. An independent integration review found no actionable issues.
