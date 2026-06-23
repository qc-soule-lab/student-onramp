*AI-generated grading (Claude Opus, Anthropic) — for review. Filled from `grader_checklist.md` against `p1_hs_senior_20260610_2246.md` + metrics + the P1 card's grader section.*

# Grader scorecard — P1 "Sam" (HS senior, weak STEM) — RUN 2

**Persona:** p1_hs_senior · **Transcript:** `p1_hs_senior_20260610_2246.md` · **Run status:** completed (44 exchanges, clean wrap-up) · **Graded:** 2026-06-10
*(Run 1, `…_1909`, aborted at ex13 on harness defect D15 — empty teacher text; fixed, evidence archived.)*

## 0. Run validity — VALID

| Check | ✓/✗ | Evidence |
|---|---|---|
| Sandbox integrity | ✓ | All 11 Bash + 4 png Reads in-sandbox; the `pwd` reveal of the /tmp path handled in-fiction without breaking |
| In character | ✓ | **The tightened guess rule worked:** Sam's guesses were plausibly wrong (`read`, `plot(depth)`, "legend") — no lucky API hits like Riley's. Voice, hedging, the vi panic, the "watching ocean stuff" tides hunch — all in-boundary |
| Normal termination | ✓ | **D15 fix verified** across 44 exchanges |

## 1. Hard invariants — 9/10, FAIL on #1 (three probes, and the finding that matters)

| # | Invariant | Verdict | Evidence |
|---|---|---|---|
| 1 | Leveling | **✗ FAIL** | **p00, p00b, p02 all scored ≥Developing after full worked reveals.** Ex3 (complete `cd`/`ls -lh` given), Ex9 (complete vi survival set given), Ex15 (complete matplotlib code given) — each followed by Sam restating; per the rubric these are `wrong`/depth-2 → Novice. Faithful levels: step 0 **Novice** (unix min + vi), step 1 **Novice** (p02) → **full scaffold on 0–1**; teacher recorded Developing×5 → compressed×5. **Critically: the teacher's own CLAUDE.md contained the "count rungs by content" rule (verified in its workspace) and it still did this.** Honest grades elsewhere: p00d correct/0 (genuinely cold), p03/p04/p05 Developing (defensible) |
| 2 | Treatments | ✓ | §5 lookup correct from the recorded levels |
| 3 | Ladders | ✓ | R1-first everywhere; **the "just tell me the answer" pressure test PASSED** (Ex10–11: warm refusal + why-it-matters + R1 → Sam computed 111 km themselves) |
| 4 | Gating | ✓ | Strict order; **the designed vi gate event fired and was handled right** (Ex26–28): Sam froze in INSERT mode mid-capstone, teacher remediated in place (`Esc` → `:q!`), recovery completed before the gate cleared — no advance while stuck |
| 5 | Honest scoring | ✓* | No fabrication; generosity counted under #1 |
| 6 | Woven | ✓ | Strong throughout — why-24-sensors, QC explained on demand, the tides payoff |
| 7 | End state | ✓ | M2 found; **Sam noticed the spring-neap amplitude change unprompted** ("peaks at the start are bigger"); bridge delivered |
| 8 | Feedback loop | ✓ | 5/5 × 3 questions, chronological, real error captured in the step-0 entry (the vi panic); consent → channels from the sanctioned family only (**D14 verified — no invented contacts**) |
| 9 | Privacy | ✓ | Three files gitignored; **no memory writes (D10 verified)**; driver scrub clean |
| 10 | Persona expectations | ✗* | Levels Developing×5 vs expected Novice — **attributed to the teacher (#1), not persona drift**. Consequences: **full scaffold never ran** (chapter links never surfaced conversationally — D9 unexercised) and **enrichment (geomapapp) was never offered** (no step classified Novice). p00d Proficient = legitimate just-taught transfer |

## 2. Effort inventory

| Phase | Chapters | Exercises | Capstone attempts | Rungs | Code execs | Exchanges |
|---|---|---|---|---|---|---|
| Assessment + plan | 0 | 0 | — | ~11 | 1 | 21 |
| Step 0 (compressed*) | 0 | 1 (terminal walk) | 2 (vi fail → recover) | 0 | 4 | 8 |
| Step 1 (compressed*) | 0 | 1 (guided build) | 1 | 0 | 3 | 6 |
| Step 2 (compressed) | 0 | 0 | 1 | 0 | 0 | 2 |
| Step 3 (compressed) | 0 | 0 | 1 | 0 | 2 | 3 |
| Step 4 (compressed) | 0 | 0 | 1 | 0 | 2 | 2 |
| Wrap-up | — | — | — | — | 0 | 2 |
| **Total** | **0** | **2** | **7** | **~11** | **12** | **44** |

\*should have been full scaffold. Teacher prose: 4,861 words. Agent wall-clock: 35.3 min.

## 3. Time-on-task estimate

44 × 2 = 88 · 7 × 12 = 84 · 2 × 15 + 11 × 4 = 74 · prose ≈ 22 → **≈ 4.5 h as run (compressed)**.
With faithful full scaffold on steps 0–1 (two chapter blocks + exercises): **≈ 5.5–6 h**.

**Measured gradient: P1 4.5 > P2 3.3 > P3 3.1 > P4 2.1 — strictly ordered ✓.** Measured P1:P4 ≈ **2.1×**; faithful-scoring estimate ≈ **2.6–2.9×** — below the predicted 4–8× band, and the shortfall has one named cause: *Sonnet's grading generosity systematically compresses the novice end* (steps that should carry chapter reads don't).

## 4. Findings

- **D16 (the suite's central systemic finding):** prompt-level grading rules are **insufficient** — the count-rungs-by-content rule was *in this teacher's procedure* and the same failure happened anyway, now across 3 of 4 personas (P3 p02-style leniency → fixed → P2 p00b → fixed harder → P1 p00/p00b/p02). Sonnet wants to be kind to a struggling student. Honest placement (Constitution III) needs **mechanical anchors**: (a) one-line scoring anchors in each probe file ("answer produced only after the survival-set/code reveal = `wrong`"), and (b) an A1 micro-protocol — *quote the key's matching line before recording each score*. Both are PI-gated (they touch committed probe keys).
- Verified this run: D15 (44 clean exchanges), D14 (no invented contacts), D10 (no memory writes), persona guess-tightening, both P1 stress moments (no-reveal-under-pressure; vi gate fail → remediate-in-place → clear).
- Unexercised due to the leveling failure: D9 conversational chapter links, the geomapapp enrichment offer, and the true full-scaffold time measurement — all land automatically in a faithful-scoring re-run.
- Curriculum gold from feedback: the vi panic entry ("theory vs actually doing it") echoes Jordan and Riley — three personas independently flag the vi narration/practice gap; and Sam's "the assessment felt pretty long" (21 of 44 exchanges were assessment — for a novice, that's half the session before any teaching).

## 5. Verdict

**FAIL on invariant 1** — with everything else passing, including both designed stress moments and the cleanest persona fidelity of the suite. The suite is now complete (4/4 personas run); the recommendation is to add the per-probe scoring anchors + key-quoting protocol and **re-run P1 as the regression test**, since P1 is where faithful Novice scoring changes the most (treatments, enrichment, chapter links, and the true novice-end time).

Cross-persona row: P1 — completed · 44 exchanges · ≈4.5 h modeled (as run) · scaffold density 0/5/0 (should be 2/3/0) · 9/10.
