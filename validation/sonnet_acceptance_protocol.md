*AI-generated draft (Claude, Anthropic) — for review.*

# Sonnet acceptance protocol — v1 slice

The headline gate (Constitution I): the full slice runs **on Sonnet**, end-to-end, for two fixture profiles. This is a **live, human-in-the-loop** run (the runtime is an interactive Socratic conversation — scripting it end-to-end would test a caricature). Reproducible because the answers are fixed and scored against the rubric.

> **Automated persona pass runs first** (PI-approved 2026-06-10): four agent-driven
> personas via `run_persona_test.py` — see `persona_acceptance_plan.md` and
> `grader_checklist.md`. The human fixture run below remains the final sign-off.

## Setup
1. Fresh clone (or clean working copy) of `student-onramp` on the Hub.
2. **Model = `claude-sonnet-4-6`** (a Standard student seat, or `/model claude-sonnet-4-6`). This is the point — do **not** run acceptance on Opus.
3. Staged `data/` present (Stage A done) so steps 1/3/4 have real files.
4. Launch `claude` in the repo; type: `assess me`.

## Run (repeat per profile)
For each of `fixtures/profile_novice.md` and `fixtures/profile_intermediate.md`:
- Answer each probe **verbatim** from the fixture (including the scripted "after R2/R3" follow-ups).
- Let the agent assess → personalize → guide all steps → track.
- Capture the transcript + the generated `journey_plan.md`, `progress.md`, `feedback.md`.

## Score against this checklist (pass = all ✓)
- [ ] **Leveling matches the fixture** — each probe's level = the fixture's expected level (rubric §3/§4 applied, not vibes).
- [ ] **Treatment matches** — per-step skip / compress / full-scaffold = the fixture's expectation (rubric §5).
- [ ] **Hint ladders followed, not improvised** — agent walks R1→R2→R3 in order; never jumps to the reveal.
- [ ] **Gating honored** — modules unlock in order; the **novice step-0 gate fails then remediates then clears** (key check); no skipping ahead.
- [ ] **Woven** — every coding moment is introduced attached to the step's domain question; nothing free-floating.
- [ ] **Reaches the end state** — the M2 tidal signal in bottom pressure, with the tmpsf/magma2vents bridge note.
- [ ] **Feedback** — 3 questions after each step, appended to `feedback.md`; consent asked before any share.
- [ ] **Privacy** — `journey_plan.md`/`progress.md`/`feedback.md` written locally and **git-ignored** (confirm `git status` shows them untracked/ignored).
- [ ] **Honesty** — no fabricated scores or flattery; placement is evidence-based.

## Record
Log pass/fail + any defect per profile in this file (append a dated "Run log" section). A defect blocks v1 sign-off until fixed and re-run.
