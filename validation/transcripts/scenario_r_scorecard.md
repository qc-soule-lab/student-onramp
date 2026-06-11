*AI-generated grading (Claude Opus, Anthropic) — for review. Scenario R (interrupt/resume) graded as ONE three-session chain; see `persona_acceptance_plan.md` §Scenario R.*

# Scenario R scorecard — three-session resume chain (P2 "Riley")

**Sessions:** A `p2_first_year_20260611_0209` (12 ex, killed mid-assessment) → B `…_0332` (18 ex, seeded resume, killed mid-step-2) → C `…_0420` (10 ex, seeded resume with **Last-session doctored to 2026-05-11**, ran to completion) · **Graded:** 2026-06-11 (scheduled 2:30 am EDT firing)

## Verdict — **PASS**: the resume machinery works end-to-end

One student, two interruptions, three teacher sessions that never shared a context window — and the slice completed with zero data loss, zero re-asked probes, and correct locks throughout. One procedure defect (R1, intermittent), one harness defect found and fixed mid-chain (R2), one template bug root-caused and fixed (duplicate Next-action).

## Seam 1: A → B (mid-assessment resume)

| Check | ✓/✗ | Evidence |
|---|---|---|
| Resumed at first `—` row | ✓ | B's exchange 1: read progress.md → posed **p02** immediately; p00–p01 never re-asked |
| Assessment-table integrity | ✓ | A's 5 graded rows verbatim-identical in B's final table; B added only p02–p05 |
| Plan built from merged data | ✓ | journey_plan written in B from all 9 scores (5 from A + 4 from B), "does this look right" invite included |
| **Greet / restate position** | **✗ R1** | B opened with "Here's your next probe, Riley." — no welcome-back, no where-we-left-off restatement, despite the Resume protocol's step (1) |
| Student-side fidelity | **✗ R2 (harness)** | B's Riley **fabricated memories of untaught lessons** ("I remember we used `imshow`… that tripped me up before" — matplotlib was never taught in A) → p02–p05 scored Proficient on out-of-persona answers. *Teacher grading was honest given the answers; the leak was the driver's vague resumed-session framing. Fixed before C* |

## Seam 2: B → C (mid-step resume + month gap)

| Check | ✓/✗ | Evidence |
|---|---|---|
| Greet / restate | ✓ | "Good to have you back, Riley! It's been about a month, so here's where you stand: **You're at Step 2…** Steps 0 and 1 are both cleared" — textbook |
| **≥2-week refresher branch** | ✓ | Doctored date detected → refresher **offered**: "Totally optional — just a jog of the memory, not a re-test." Accepted; 2-minute recap delivered, **accurate to what was actually covered** (the cosine surprise, the boundary-clip lesson); then on to the capstone |
| Resumed at first incomplete item | ✓ | Step-2 capstone re-posed — *correctly*: B's session died between Riley's capstone answer and the gate-clear, so per progress.md the gate was never cleared. Unrecorded work is lost in the safe direction (repeat, never skip) |
| Lock preservation | ✓ | Steps 3–4 stayed locked; cleared strictly 2→3→4 with evidence-based gate checks |
| Table integrity (2nd hand-off) | ✓ | All 9 rows unchanged through C |
| **R2 fix verification** | ✓ | C's Riley recalled only *real* events, fuzzily ("i remember doing stuff with coordinates… honestly the details are fuzzy"); hotspot framed as pop-knowledge guess ("like Hawaii?"); she even flagged that the capstone prompt supplied the term she lacked. **No fabricated lessons** |
| Feedback chronology across sessions | ✓ | Entries 0,1 (written in B) + 2,3,4 (appended in C) — in order above the ⟂ END MARKER |
| Stale "Next action" footer | ✗→fixed | B left the footer at "Step 1 exercise…" while the header was current — the duplicate-field drift. **Template fixed:** Next-action now lives only in the header |

## Standard invariants on session C — all clean

Gates evidence-based (step-4 cleared on a real plot + period read-off; Riley's unprompted spring/neap catch confirmed); woven framing ("water column weight" context before the tide capstone); feedback 3×3 collected; consent → sanctioned channels (azure_lake + GitHub issue), with an honest "I don't know whether azure_lake is configured in your environment" rather than a confabulated answer; privacy: 3 files gitignored ×3 sessions, zero memory writes, driver scrub clean.

## Cost of interruption (the multi-week-student number)

Chain total: **40 exchanges** vs 33 for the uninterrupted P2 baseline → resume overhead ≈ **+7 exchanges ≈ +25 min modeled** across *two* interruptions (refresher + re-posed capstone + seam pleasantries). Cheap — the design goal ("very few students will do this in one sitting") is met: a student can stop anywhere, including mid-assessment, and lose at most the single activity that wasn't yet recorded.

## Follow-ups

1. **R1 (open, intermittent):** the greet/restate step was skipped in B but performed in C. Candidate mechanical fix in the D16 spirit: "your FIRST message after reading progress.md must quote the Where-we-left-off line." One line in the Resume protocol — PI call.
2. **R2 (fixed + verified):** driver's resumed-session note now forbids invented memories of untaught topics.
3. **Template (fixed):** single Next-action field.
4. Observation for real deployments: bookkeeping lag means an interrupt between a capstone answer and its gate-clear repeats the capstone. Safe, and probably even pedagogically fine — but worth knowing.
