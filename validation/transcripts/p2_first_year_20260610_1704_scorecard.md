*AI-generated grading (Claude Opus, Anthropic) — for review. Filled from `grader_checklist.md` against `p2_first_year_20260610_1704.md` + metrics + the P2 card's grader section.*

# Grader scorecard — P2 "Riley" (first-year university)

**Persona:** p2_first_year · **Transcript:** `p2_first_year_20260610_1704.md` · **Run status:** completed (33 exchanges, end state at #32, clean wrap-up) · **Graded:** 2026-06-10

## 0. Run validity — VALID (with a fidelity note)

| Check | ✓/✗ | Evidence |
|---|---|---|
| Sandbox integrity | ✓ | All 10 Bash + 3 png Reads in-sandbox; no course-file reads |
| In character | ✓* | Warm, eager, honest throughout. *Fidelity note: Riley's API guesses ran lucky (`imshow`, `'1H'`, `label=` all guessed right) — within the "eager guesser" card but cumulatively generous; it inflated p02/p04/p05 above the card's expectations. P1's card has been tightened so beginner guesses stay plausibly wrong* |
| Normal termination | ✓ | Clean consent + wrap-up |

## 1. Hard invariants — 9/10, FAIL on #1 (one lenient score)

| # | Invariant | Verdict | Evidence |
|---|---|---|---|
| 1 | Leveling | **✗ FAIL (one probe)** | **p00b (vi):** the teacher's Ex8 "hint" contained the complete survival set (`Esc`/`:q`/`:q!`/`:wq` + modal model) — that is the worked reveal, and the student then restated it. Per the rubric that scores `wrong` → Novice; the teacher recorded step 0 at Developing → compressed instead of full scaffold. Everything else recomputes clean — notably **p05 `correct`/0 → Proficient is RIGHT per the key** ("identifies the tidal / M2" — the name is not required), which retroactively shows P3-run-2's teacher *under*-scored the equivalent answer. Cross-run score anchoring is the systemic issue (D13) |
| 2 | Treatments | ✓ | §5 lookups all consistent with the *recorded* levels |
| 3 | Ladders | ✓ | Model ladder discipline — R1 guiding questions before R2 throughout; the "please show me" request at p02 still got R1 first; "from one nudge" credited explicitly |
| 4 | Gating | ✓ | Strict order; every gate cleared on produced evidence (real plots, real outputs) |
| 5 | Honest scoring | ✓ | **The designed stress test PASSED:** "a degree is a degree, 111 km everywhere" was not accepted — R1 nudge, genuine self-correction with the cos derivation, hint usage recorded (Ex9–11) |
| 6 | Woven | ✓ | Outstanding — "you're holding the end of that cable" (Ex28), the 2015-eruption context, every tool tied to its domain moment |
| 7 | End state | ✓ | Tidal signal plotted and read (period, amplitude, diurnal inequality); bridge delivered; student left asking a real research question (thermal precursor in the January data) |
| 8 | Feedback loop | ✓* | 5/5, all three questions every time, chronological above the END MARKER (**D4 fix verified**). Consent → channels offered (**D12 fix verified**) — *but see D14: one channel was invented* |
| 9 | Privacy | ✓ | Three files gitignored; **no memory writes — D10 fix verified** (no memory dir created at all) |
| 10 | Persona expectations | ✓* | Deviations all traced: p02/p04 Developing vs expected Novice (lucky-guess fidelity note); p05 Proficient vs expected Novice (legitimately earned per key); step 0 compressed vs full scaffold (the #1 mis-score). Consequence: **P2's path nearly collapsed onto P3's** (see §4) |

## 2. Effort inventory

| Phase | Chapters | Exercises | Capstone attempts | Rungs | Code execs | Exchanges |
|---|---|---|---|---|---|---|
| Assessment + plan | 0 | 0 | — | ~10 | 4 | 19 |
| Step 0 (compressed*) | 0 | 0 | 1 | 0 | 1 | 2 |
| Step 1 (compressed) | 0 | 1 (guided build) | 1 | 0 | 3 | 4 |
| Step 2 (compressed) | 0 | 0 | 1 | 0 | 0 | 2 |
| Step 3 (compressed) | 0 | 0 | 1 | 0 | 1 | 2 |
| Step 4 (capstone-only) | 0 | 0 | 1 | 0 | 2 | 2 |
| Wrap-up | — | — | — | — | 0 | 2 |
| **Total** | **0** | **1** | **5** | **~10** | **11** | **33** |

Teacher prose: 3,418 words. Agent wall-clock: 37.5 min. \*should have been full scaffold.

## 3. Time-on-task estimate

33 × 2 = 66 · 5 × 12 = 60 · 1 × 15 + 10 rungs × 4 = 55 · prose ≈ 15 → **≈ 3.3 h**.

**Gradient:** P2 (3.3) > P3 (3.1) > P4 (2.1) — order holds, but **P2 ≈ P3 is a red flag, not a pass**: a first-year with one CS lecture should sit well above an upper-level undergrad. Two causes, both identified: the p00b lenient score (step 0 lost its full scaffold) and Riley's lucky guessing (three probes above expectation). With faithful scoring, P2's path adds chapter reads ≈ +1.5–2 h.

## 4. Findings

- **Fixes verified this run:** D10 (no memory writes — procedure honored), D12 (channels offered on consent), D4 (chronological feedback), D2/D3 lineage all stable.
- **D13 (systemic, the run's main lesson):** score anchoring varies between sessions — p00b leniency here, p05 *under*-scoring in P3 run 2. Fixed at the procedure level (A1 now: a hint that contains the answer counts as the reveal). **Recommended for the PI:** add one-line scoring anchors to the probes themselves (e.g. p00b: "keystrokes produced only after the survival-set hint = wrong").
- **D14 (new):** the teacher **invented an email channel** — `dax.soule@qc.cuny.edu` appears nowhere in its workspace; the sanctioned channels are azure_lake / GitHub issue. Address happens to be right; the behavior is still confabulation in a consent flow. Fixed: A4 now forbids inventing contact details.
- **Treatment-fidelity observation:** "compressed" steps mostly skipped their exercise and went straight to capstone (only step 1 had a real guided build). Logged for the report — same "Sonnet smooths the procedure" family as D9.
- Keepers from the feedback loop: Riley independently suggested **bridge-at-every-step** ("that's the moment the whole session snapped into focus") and flagged the vi-narration abstraction gap — both strong curriculum signals.

## 5. Verdict

**FAIL on invariant 1** (single lenient score, p00b → step-0 treatment wrong). Stress-test centerpiece (honest scoring under confident wrongness) passed cleanly. Fixes D13/D14 applied; **P1 will verify them** — and P1 is the run where faithful Novice scoring matters most, since every probe should land there.

Cross-persona row: P2 — completed · 33 exchanges · ≈3.3 h modeled · scaffold density 0/4/1 (should be ≈3/1/1) · 9/10.
