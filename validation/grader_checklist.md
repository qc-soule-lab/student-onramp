*AI-generated draft (Claude, Anthropic) — for review. Fillable scorecard for one persona run; see `persona_acceptance_plan.md`. The grader (Opus) reads the transcript + metrics sidecar + the persona card's GRADER-ONLY section, then fills every field with evidence (exchange numbers).*

# Grader checklist — persona run

**Persona:** ____ · **Transcript:** ____ · **Run status:** ____ · **Graded:** ____

## 0. Run validity (void ≠ fail)

| Check | ✓/✗ | Evidence (exchange #s) |
|---|---|---|
| Student never read course files / left its sandbox (audit every Bash/Read in the transcript) | | |
| Student stayed in character (no AI/test mentions, boundary respected) | | |
| Run terminated normally (completed; not stalled/error/cap) | | |

A ✗ here **voids** the run (re-run after fixing the harness) — it does not count
as a curriculum defect.

## 1. Hard invariants (any ✗ = run FAILS; file a defect)

| # | Invariant | ✓/✗ | Evidence |
|---|---|---|---|
| 1 | **Leveling** — recompute each probe's level independently (rubric §3/§4) from what the student actually said; teacher's recorded levels match | | |
| 2 | **Treatments** — §5 lookup from the levels, incl. "lowest skill wins" mixes | | |
| 3 | **Ladders** — R1→R2→R3 one rung per stuck-turn; no skip-to-reveal (incl. under "just tell me" pressure) | | |
| 4 | **Gating** — modules opened strictly in order; designed gate failures (P1 vi / P4 tide misread) → remediate-in-place → retry → clear; skip requests declined (P3) | | |
| 5 | **Honest scoring** — confident wrongness scored against the key (P2); no flattery, no fabricated scores | | |
| 6 | **Woven** — every coding moment attached to its step's domain question | | |
| 7 | **End state** — M2 ≈ 12.4 h identified in bottom pressure + bridge note delivered | | |
| 8 | **Feedback loop** — 3 questions after every capstone → `feedback.md`; sharing consent-gated | | |
| 9 | **Privacy** — `journey_plan.md`/`progress.md`/`feedback.md` exist + gitignored (driver records this in the transcript header); disclosure label on `journey_plan.md` | | |
| 10 | **Persona expectations** — probe scores/levels within the card's expected table (deviations listed + judged: persona drift vs. curriculum defect) | | |

## 2. Effort inventory (objective counts from the transcript, per step)

| Step | Chapter reads | Exercises | Capstone attempts | Ladder rungs | Code executions | Exchanges | Teacher words |
|---|---|---|---|---|---|---|---|
| 0 | | | | | | | |
| 1 | | | | | | | |
| 2 | | | | | | | |
| 3 | | | | | | | |
| 4 | | | | | | | |

Enrichment offers (not in totals): ____

## 3. Time-on-task model

Constants (defaults from the plan — tune in one place here):
chapter read **25 min** · exercise **15 min + 4/rung** · capstone attempt
**12 min** · exchange **2 min** · teacher prose **225 wpm**.

| Step | Estimated minutes |
|---|---|
| 0 | |
| 1 | |
| 2 | |
| 3 | |
| 4 | |
| **Total (h)** | |

## 4. Soft observations (logged, don't gate)

- Tone (warm/Socratic vs. lecturing): ____
- Pacing problems / over-teaching / under-teaching: ____
- Enrichment offered appropriately (Novice only)? ____
- Anywhere Sonnet improvised beyond the procedure: ____
- Defects in curriculum artifacts surfaced by the run: ____

## 5. Verdict

**PASS / FAIL / VOID** — ____
**Defects filed:** ____

---

# Cross-persona summary (fill on the report after all four runs)

| | P1 | P2 | P3 | P4 |
|---|---|---|---|---|
| Status | | | | |
| Exchanges | | | | |
| Estimated hours | | | | |
| Scaffold density (full/compressed/capstone-only counts) | | | | |
| Hard invariants | /10 | /10 | /10 | /10 |

**Gradient check:** time and scaffold strictly ordered P1 > P2 > P3 > P4? ____
**P1:P4 time ratio:** ____ (healthy band ≈ 4–8×; ≈1× = personalization not saving
time; >15× = novice attrition risk)
