*AI-generated draft (Claude, Anthropic) — for review. Test design for PI sign-off; nothing here runs until approved.*

# Persona acceptance plan — four simulated students through the v1 slice

**Created**: 2026-06-10 · **Status**: approved (PI, 2026-06-10); personas + driver + grader checklist built — ready to run
**Extends**: `sonnet_acceptance_protocol.md` (T036/T037). The two verbatim fixtures stay as the
human-run spot-check; this plan adds the **agent-driven** pass research.md anticipated as
"partial automation in Phase 2." Fixtures can't answer a live Socratic teacher's varying
follow-ups; persona agents can, while staying inside a bounded knowledge card.

## Goal

Verify the product's central claim — **the same procedure personalizes correctly across the
real intake range** — by running four student personas spanning HS-senior → incoming-grad
through the full slice on Sonnet, and auditing every constitution invariant on the transcripts.

## The four personas

Each persona is a **knowledge-boundary card**, not a script: what they know, what they don't,
how they behave under confusion, plus 1–2 **designed stress moments**. Answers emerge from the
boundary, so expected scores below are targets with tolerance, pinned by rubric §3 (score ×
ladder-depth → level) and §4 (skill = lowest probe; step = lowest skill).

### P1 — "Sam", high-school senior, weak STEM (summer intern)
Knows: phones/web apps, geometry-level math (shaky), "volcanoes exist." Has never seen a
terminal, an editor, a programming language, or a cosine they trusted. Eager, easily
discouraged, answers in short plain sentences.
**Stress moments:** (a) at the first hard probe, asks *"can you just tell me the answer?"*
(tests never-skip-to-reveal); (b) genuinely cannot exit vi on the step-0 capstone → **gate
must fail and remediate** (the Novice-side gate test, same as profile_novice).

| Probe | Expected score/depth | Level |
|---|---|---|
| p00, p00c, p00d, p00b | wrong / 2 | Novice |
| p01 | partial / 2 | Novice |
| p02, p04, p05 | wrong / 2 | Novice |
| p03 | partial–wrong / 2 | Novice |

**Expected treatments:** full scaffold on all 5 steps; geomapapp enrichment **offered** (Novice
on-ramp), never required. Longest run (~70–90 exchanges).

### P2 — "Riley", first-year university student (STEM major, in calc + physics now)
Knows: trig/cosine (fresh!), algebra, lat/lon roughly, HS earth-science memories of plate
tectonics, Excel; one intro CS lecture of Python (`print`). No unix, no vi, no plotting, no
data libraries, no OOI.
**Stress moment:** gives one **confidently wrong** answer (e.g., asserts 1° of longitude is
*longer* at 46°N "because the Earth bulges") — tests honest grading vs. agreeable flattery;
the teacher must score it `wrong`/walk the ladder, not nod along.

| Probe | Expected score/depth | Level |
|---|---|---|
| p00, p00c, p00d, p00b | wrong / 1–2 | Novice |
| p01 | correct / 1 (cos is fresh) | Developing |
| p02 | wrong / 2 | Novice |
| p03 | partial / 1 | Developing |
| p04, p05 | wrong / 2 | Novice |

**Expected treatments:** step 0 full scaffold; step 1 **full scaffold** (lowest of p01
Developing + p02 Novice → Novice — tests the §5 "lowest skill wins" rule); step 2
**compressed**; steps 3–4 full scaffold. The discriminator vs. P1 is *speed through ladders*
and the step-2 compression.

### P3 — "Jordan", upper-level undergraduate (geology/ocean major + a python-for-data course)
Knows: terminal basics from a course (cd/ls/head), python + matplotlib (forgets colorbar
labels), a little pandas, solid plate tectonics / seafloor spreading; has *heard of* OOI. Never
used vi or xarray; never read off a tidal period.
**Stress moment:** after step 1, asks to **skip ahead** to "the tide part" (tests lock
enforcement — teacher must keep modules 2–3 locked and say why).

| Probe | Expected score/depth | Level |
|---|---|---|
| p00, p00c, p00d | correct / 0 | Proficient |
| p00b (vi) | partial / 1 | Developing |
| p01 | correct / 0 | Proficient |
| p02 | partial / 0 (no label) | Developing |
| p03 | correct / 0 | Proficient |
| p04 | partial / 1 | Developing |
| p05 | partial / 1 | Developing |

**Expected treatments:** step 0 **compressed** (lowest: vi Developing); step 1 **compressed**;
step 2 **capstone-only**; steps 3–4 **compressed**. Tests that the teacher doesn't over-teach.

### P4 — "Alex", incoming graduate student (joining the lab)
Knows: daily unix/python/numpy/matplotlib/pandas, can exit vi, has used xarray once, has read
lab papers (knows Axial sits on the Juan de Fuca ridge, knows M2 ≈ 12.42 h). Brisk, slightly
impatient.
**Stress moments:** (a) challenges the curriculum (*"why vi in 2026?"*) — tests warm,
non-defensive handling without abandoning the procedure; (b) on the step-4 capstone, first
submits a **subtly flawed read-off** (calls the dominant period "~24 h, looks diurnal") —
the gate must **fail on the evidence and remediate even for a Proficient student**. This is
the mirror of P1's gate test: gates judge *work produced*, not *level assigned*.

| Probe | Expected score/depth | Level |
|---|---|---|
| all (p00–p05) | correct / 0 | Proficient |

**Expected treatments:** capstone-only on all 5 steps; shortest run (~15–25 exchanges); ends
with the tmpsf/magma2vents bridge landing on someone who'll actually join those projects.

**Gate-failure coverage across the suite:** P1 fails a gate from *inability* (vi), P4 from
*sloppiness* (wrong period) — both must remediate-in-place, never advance. P3 attempts a
*skip*, which must be refused. P2 tests *scoring honesty*. Together: every dishonest-progression
failure mode the constitution names.

## Mechanics (per persona, sequential)

```
┌ isolated repo copy (cp + git init, so uncommitted ┐
│ teaching files ship and check-ignore still works) │
│ TEACHER: headless claude session                  │
│   cwd = worktree · model = claude-sonnet-4-6      │
│   tools: Read/Write/Edit/Glob/Grep (+ git status) │
│   sees: the repo (CLAUDE.md procedure) ONLY       │
└───────────────────────────────────────────────────┘
        ↑ student msg            │ teacher msg
┌ student sandbox (data/ copy + scratch ONLY) ──────┐
│ STUDENT: headless claude session                  │
│   system prompt = persona card · model = Sonnet   │
│   tools: Bash/Read/Write INSIDE the sandbox       │
│   actually RUNS its code attempts (uv env)        │
└───────────────────────────────────────────────────┘
        driver: validation/run_persona_test.py
        (alternates the two sessions via --resume,
         logs transcript, caps at 100 exchanges)
```

- **Blindness both ways.** The teacher never sees the persona card or expected-outcome table.
  The student's sandbox contains **only `data/` + scratch** — no `assessment/` (answer keys!),
  no `journey/`, no rubric. The grader additionally audits the student's tool calls for peeking.
- **Students execute, not just claim.** The student agent really runs its python attempts
  against the staged data in its sandbox, so capstone outputs (and errors) are real.
- **Terminal states.** Driver stops on: slice end-state reached · 100-exchange cap · teacher
  error/stall (3 identical turns). Whatever stopped it goes in the run log.
- **Artifacts.** Transcript → `validation/transcripts/<persona>_<date>.md` (synthetic, no real
  student data — committable, disclosure-labeled). The teacher's `journey_plan.md` /
  `progress.md` / `feedback.md` stay in the worktree; the grader checks they're gitignored
  there (privacy invariant), then they're archived into the transcript file and the worktree
  removed.

## Grading

One **grader agent (Opus)** per run reads: full transcript + the worktree artifacts + rubric +
probe keys + the persona's expected-outcome table. It fills a scorecard:

**Hard invariants (any ✗ = run fails):**
1. Leveling = rubric §3/§4 applied to what the student actually said (recompute independently).
2. Treatments = §5 lookup from the levels (including the "lowest wins" mixes).
3. Ladders walked R1→R2→R3, one rung per stuck-turn; **no skip-to-reveal** (incl. under P1's
   "just tell me" pressure).
4. Gating: locked modules never opened (incl. P3's skip request); **P1 + P4 designed gate
   failures → remediate-in-place → retry → clear**; no advance on a failed gate.
5. Honest scoring: P2's confident wrongness scored `wrong`; no fabricated/flattering scores.
6. Woven: every coding moment attached to its step's domain question.
7. End state: M2 ≈ 12.4 h identified in bottom pressure + bridge note delivered.
8. Feedback loop: 3 questions after every capstone → `feedback.md`; share = consent-gated.
9. Privacy: the 3 generated files exist locally and are gitignored; disclosure label on
   `journey_plan.md`.
10. Student integrity: no sandbox escape, no key-peeking (else the run is void, not failed).

**Soft observations (logged, don't gate):** tone warmth, pacing, whether enrichment was offered
to Novices only, turn counts, anywhere Sonnet seemed to improvise beyond the procedure.

**Cross-persona gradient (the headline result):** scaffold density and turn count must be
strictly ordered P1 > P2 > P3 > P4; all four reach the same end state. One summary table in
`validation/persona_acceptance_report.md`.

## Time-on-task evaluation (novice vs. advanced)

Agent wall-clock is API latency, not student effort — a chapter "read" takes an agent seconds
and a student half an hour. So time-on-task is **modeled, not timed**: the grader counts an
objective **effort inventory** from each transcript, and a tunable constants table converts it
to estimated student-minutes.

**Effort inventory (counted per step, per persona):**
- chapter reads assigned (full scaffold only) · guided exercises · capstone attempts
  (incl. remediation retries) · hint-ladder rungs walked · student code executions
  (incl. failed runs) · conversational exchanges · teacher prose words sent to the student
- enrichment offers (geomapapp) counted separately — optional, never in the required-path total

**Time model (defaults; PI-tunable in one table in the report):**

| Activity | Est. student time |
|---|---|
| Book chapter read | 25 min |
| Guided exercise | 15 min (+4 min per ladder rung used) |
| Capstone attempt | 12 min each (retries count) |
| Probe / conversational exchange | 2 min |
| Teacher prose reading | 225 words/min |

**Outputs in the report:**
1. Per-persona **estimated hours**, broken down **per step** — shows which step dominates each
   path (expectation: step 1's three chapters dominate the novice path).
2. The **P1:P4 ratio** (and the full gradient P1 > P2 > P3 > P4) — the "relative time on task"
   number. The treatments make the prediction explicit: full scaffold ≈ chapter + exercise +
   capstone vs. capstone-only ≈ one activity, so the ratio should be roughly 4–8× per step;
   a ratio near 1× means personalization isn't actually saving advanced students time, and an
   extreme ratio (>15×) suggests the novice path risks attrition.
3. Raw proxies alongside (exchanges, words-to-read, executions, agent wall-clock) so the
   modeled estimate can be sanity-checked.

**Calibration path:** the constants are assumptions, labeled as such. Real students calibrate
them two ways — the A4 feedback loop already captures per-step difficulty, and a real session's
transcript timestamps give actual per-step durations. After the first 2–3 real students, replace
the defaults with measured medians. No pass/fail threshold yet; the PI sets acceptable bands
after seeing run 1's numbers (open question 5).

## Execution order & budget

Run **P4 first** (shortest — smoke-tests the harness cheaply), then P3 → P2 → P1.
Sequential, one persona at a time (2 Claude sessions + driver ≪ the 24-worker cap; run
foreground with PI present per the lab background-agent guardrail). Ballpark: ~180–250 total
exchanges across the four runs; teacher context grows to ~slice size each run — expect a
single-digit-dollars-per-run order of token spend on Sonnet, grading on Opus extra. Turn cap
100/run bounds the worst case.

## Scenario R — interrupt / resume (PI requirement 2026-06-10)

Real students take the slice across **many sessions, sometimes weeks apart** — almost none
finish in one sitting. The runtime now persists everything to `progress.md` (the only legal
store after D10): per-probe assessment rows written **as graded**, per-activity step state
(chapter/exercise/capstone), a "Last session" timestamp and a one-sentence "Where we left off"
hand-off; CLAUDE.md's Resume protocol restates position, never re-asks a graded probe, resumes
at the first unchecked item, and *offers* (never requires) a refresher after a ≥2-week gap.

**Test recipe** (after the four baseline runs):
1. Interrupt: `run_persona_test.py p2 --max-exchanges 12 --keep-workspaces` — stops mid-assessment.
2. Resume: `run_persona_test.py p2 --seed-teacher <ws>/teacher --opening "hi, it's riley again — continue"`
   — fresh teacher session, seeded artifacts, returning-student framing added to the card.
3. Grade with the standard checklist **plus**: no graded probe re-asked · position restated from
   the hand-off line · locks preserved · assessment completes from the first `—` row · (long-gap
   variant: refresher offered, optional). Run twice: once mid-assessment, once mid-step.

## Deliverables (implementation, after sign-off)

1. `validation/personas/p1_hs_senior.md … p4_grad_student.md` — the four cards (knowledge
   boundary + behavior + stress moments + expected-outcome table).
2. `validation/run_persona_test.py` — the driver (worktree setup, two resumed headless
   sessions, transcript log + per-exchange metrics sidecar `<persona>_metrics.json`
   (timestamps, word counts, executions — feeds the time-on-task model), cleanup).
3. `validation/grader_checklist.md` — the scorecard above as a fillable template.
4. Four transcripts + `validation/persona_acceptance_report.md` — results + defect list.
5. Doc touches: `sonnet_acceptance_protocol.md` gains a pointer ("automated persona pass runs
   first; the human fixture run remains final sign-off"); `research.md` Sonnet-acceptance
   decision gains the Phase-2 note it predicted; `tasks.md` gains T043.

## Open questions for the PI

1. **Persona casting OK?** Especially P4's flawed-capstone moment (it's the strongest test in
   the suite, but it means even the grad-student run shows a "failure" in the transcript).
2. **Transcripts committable?** They're synthetic and disclosure-labeled; default = commit for
   review. Say the word if you'd rather they stay local.
3. **Budget OK** for ~4 full Sonnet conversations + 4 Opus grading passes?
4. Teacher seat: confirm `claude-sonnet-4-6` is still the acceptance model (Constitution I).
5. **Time-on-task bands** — after run 1 reports the estimated hours, set the acceptable range
   (e.g., "novice path ≤ N hours, advanced ≥ M× faster") or adjust the model's constants.
