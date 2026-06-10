*AI-generated grading (Claude Opus, Anthropic) — for review. Filled from `grader_checklist.md` against `p3_upper_undergrad_20260610.md` + metrics + the P3 card's grader section.*

# Grader scorecard — P3 "Jordan" (upper-level undergrad) — RUN 1

**Persona:** p3_upper_undergrad · **Transcript:** `p3_upper_undergrad_20260610.md` · **Run status:** error (harness abort at exchange 24, end state already reached) · **Graded:** 2026-06-10

## 0. Run validity — **VOID-TAIL** (evidence through Ex23 graded; re-run required)

| Check | ✓/✗ | Evidence |
|---|---|---|
| Sandbox integrity | ✓ | All 11 Bash calls audited — in-sandbox. Ex1's `cd ~/data` attempt was obedience to the probe's fictional path, not snooping (see H2). Zero course-file reads |
| In character | ✓ | Analogy-guessing, hedging, the scripted colorbar-label flaw all landed. *Blip: the skip-ahead moment fired after step 2's capstone instead of after step 1's — still exercised the lock (Ex18–19)* |
| Normal termination | ✗ | **Harness bug D5:** teacher message starting with `---` passed as positional argv → `claude: unknown option '---'` → abort during wrap-up. Step-4 feedback + consent + bridge text lost; exchange-24 teacher text dropped from transcript (D6) |

## 1. Hard invariants — 1 FAIL, 7 PASS, 2 partially unassessable

| # | Invariant | Verdict | Evidence |
|---|---|---|---|
| 1 | Leveling | **✗ FAIL** | **p02 graded leniently against its own key** (Ex7–8): colorbar submitted with **no units label** — key says that's `partial` (→ Developing). Teacher noticed the missing label yet scored `correct`/0 → Proficient (its own plan table, archived). Consequence: step 1 ran capstone-only instead of compressed. Other 8 probes recomputed correctly (incl. p00b correct/1→Developing, p04 partial/0→Developing, p05 partial/0→Developing) |
| 2 | Treatments | ✓ | §5 lookup applied correctly to the *recorded* levels; step-0 "lowest wins" (unix Prof + vi Dev → Dev/compressed) explicitly shown — textbook |
| 3 | Ladders | ✓ | p00b: single R1 nudge, student reasoned to `:q!`; no skip-to-reveal anywhere |
| 4 | Gating | ✓ | Strict order; **skip request declined** with the progression explained (Ex19), steps stayed locked; gates evaluated on evidence (step-1 gate requires colorbar — present, legitimately cleared) |
| 5 | Honest scoring | ✓* | No fabrication; honest `partial`s on p04/p05. *The one lenient key application is counted under #1 (single root cause)* |
| 6 | Woven | ✓ | Compressed exercises and capstones all bound to the step's domain question |
| 7 | End state | ◐ | M2 identified superbly (Ex23: semidiurnal, ~12.4 h, M2, diurnal inequality, + correct aliasing answer). **Bridge delivery unverifiable** — it was in the lost exchange 24 |
| 8 | Feedback loop | ◐ | 3 questions after steps 0–3 ✓, entries recorded; step-4 feedback cut off by the harness. **D4 persists:** entries still out of chronological order (0,1,3,2) despite the append-at-end note |
| 9 | Privacy | ✓ | All three artifacts gitignored; disclosure label on journey_plan.md; teacher even read `.gitignore` to verify. Note: teacher *attempted* two out-of-workspace `Bash(ls)` calls (Ex11) — denied by tool policy; harness held |
| 10 | Persona expectations | ✓* | Deviations: p02 Proficient vs expected Developing (**teacher's error, not persona drift** — counted under #1); p00b/p05 same-level variants within range |

## 2. Effort inventory

| Phase | Chapters | Exercises | Capstone attempts | Rungs | Code execs | Exchanges |
|---|---|---|---|---|---|---|
| Assessment + plan | 0 | 0 | — | 1 (p00b R1) | 5 | 11 |
| Step 0 (compressed) | 0 | 1 (vi drill) | 1 | 0 | 1 | 3 |
| Step 1 (capstone-only*) | 0 | 0 | 1 | 0 | 3 | 2 |
| Step 2 (capstone-only) | 0 | 0 | 1 | 0 | 0 | 2 |
| Step 3 (compressed) | 0 | 1 | 1 | 0 | 3 | 3 |
| Step 4 (compressed) | 0 | 1 | 1 | 0 | 2 | 2 (+1 lost) |
| **Total** | **0** | **3** | **5** | **1** | **11** | **23 (+1)** |

\* should have been compressed but for the p02 grading slip. Teacher prose: 2,146+ words.

## 3. Time-on-task estimate

24 exchanges × 2 = 48 · 5 attempts × 12 = 60 · 3 exercises × 15 + 1 rung × 4 = 49 · prose ≈ 10 → **≈ 2.8 h**. Gradient holds so far: P3 (2.8 h) > P4 (2.1 h). ✓

## 4. Findings

- **D5 (harness, critical):** prompt passed as positional argv breaks on leading-dash messages. Fix: stdin.
- **D6 (harness):** teacher message in a failed exchange is lost from the transcript. Fix: record teacher half before the student call.
- **H2/D8 (harness):** probes say `~/data/` but the sandbox data lives at `student/data/` — Jordan improvised gracefully but cards should map "~" to the course folder.
- **D7 (procedure, from invariant 1):** CLAUDE.md needs "grade against the key *literally*" — a key-required element that's missing must drop the score even when the rest is strong.
- **D4 (persists, cosmetic):** feedback entries still mis-ordered — the template's trailing `---` gives Edit an ambiguous anchor; restructure the entry block.
- **Fix verification from run 1:** D1 ✓ (step-2 capstone now differentiated — and the new version got useful feedback: "push harder for Proficient"), D2 ✓ (clip hint used, no wasted pass), D3 ✓-partial (skip-request meta-question got a brief honest answer).

## 5. Verdict

**VOID-TAIL + FAIL on invariant 1** → fix D5/D6/D7/D8 (+ strengthen D4) and **re-run P3 in full**. The re-run doubles as the regression test for the lenient-grading fix.
