# Specification: Coding-First Agentic Onramp (v1)

*AI-generated draft (Claude, Anthropic) — for review.*

**Directory**: `specs/001-coding-onramp-v1`
**Created**: 2026-06-02
**Status**: Draft
**Input**: "v1 coding-first agentic onramp: assess a new student's data-science readiness and build a personalized learning plan routed through the Abernathey book"

## Goal / Problem

New lab students arrive with widely varying data-science/coding backgrounds. We need a **self-serve, Claude-driven** experience that (1) accurately gauges a new student's readiness against the skills the lab's work requires, and (2) produces a **personalized, paced learning plan** that closes their specific gaps by routing them through the lab's *Earth & Environmental Data Science* book — so they reach "ready to contribute" efficiently, without a human hand-building a curriculum for each person.

**v1 covers the coding / data-science pillar only.** Math and physics are explicitly out of scope (Phase 2).

## Users

- **Primary**: a new student (e.g. Alexa) running Claude on **Sonnet** in this repo on the Hub.
- **Secondary**: PI/collaborators (authors/reviewers of the skill-map, rubric, and probe bank).

## Inputs

### Skill-map (the target)
- **What**: one generic, book-chapter-tagged **coding-readiness map** (`skill_maps/coding_readiness.yml`): skill areas (e.g. Python fundamentals, functions/classes & packaging, numpy + matplotlib, pandas, git/environment, data access) each with a target proficiency and the book chapters that teach it.
- **Source**: lab-authored; derived from the book's TOC (each book "Part" ≈ a skill area).

### Content backbone (the curriculum)
- **What**: the *Earth & Environmental Data Science* book — `qc-soule-lab/earth-env-data-science-book` (CC BY-SA 4.0), referenced by chapter URL/path, **not vendored**. Its `assignments/` supply hands-on probes and exercises.

### Student responses (gathered at runtime)
- Conversational triage answers + attempts at a few hands-on coding probes drawn from a **probe bank** (`probes/`) that has an **answer key / evaluation rubric per probe**.

## Approach / Behavior

1. **Triage (conversational)**: Claude asks a short, friendly set of questions to set a rough level per skill area (what have you built? used numpy/pandas/git?).
2. **Hands-on probes (Socratic)**: for each skill area, Claude presents 1–2 short tasks from the probe bank (write/fix/predict code). The student attempts them; when they stall, Claude offers **Socratic guidance via the probe's hint ladder** (guiding question → hint → bigger hint → reveal) rather than the answer. Claude **grades against the probe's answer key**, and **records how far down the hint ladder the student needed to go** — that scaffolding depth feeds the level (Constitution III + VI).
3. **Score & level**: Claude applies the **rubric thresholds** (`assessment_rubric.md`) to assign a level per skill area — consistently, by rule.
4. **Gap diff**: compare assessed level vs. the skill-map target → ordered list of gaps.
5. **Plan generation**: fill `learning_plan.template.md` — for each gap, look up the mapped book chapters + assignments via the **skill→chapter lookup** and emit an ordered, paced plan (e.g. "Week 1: Python fundamentals → ch. …, do assignment …").
6. **Progress tracking + Socratic teaching**: write `progress.md`; on later sessions ("continue"), Claude reads progress, optionally re-probes, and advances or remediates. Throughout teaching/remediation Claude is **Socratic by default** (Constitution VI) — it works the student through concepts and stuck points by *asking*, drawing on per-concept **guiding-question banks**, and explains directly only after genuine engagement.

**Why this design**: per Constitution Principle I, every step is a *lookup / grade-against-key / follow-the-hint-ladder / fill-template* operation, so it runs reliably on **Sonnet**. Claude is not asked to invent a curriculum, judge ability open-endedly, or improvise Socratic pedagogy — the questions, hints, and reveals are pre-authored ladders it follows.

## Required Artifacts (what implementation must produce)

- `CLAUDE.md` — the agent's **step-by-step runtime procedure** (deterministic, numbered) for the flow above.
- `skill_maps/coding_readiness.yml` — skill areas, targets, chapter tags.
- `assessment_rubric.md` — explicit scoring thresholds + leveling rules.
- `probes/` — probe bank, each probe with prompt + **answer key / grading criteria** + a **hint ladder** (guiding question → hint → bigger hint → worked reveal) for Socratic scaffolding, with scaffolding-depth → level mapping.
- **Per-concept guiding-question banks** — pre-authored Socratic questions/hints for teaching & remediation (so the agent leads by asking, on Sonnet, without improvising).
- `skill_to_chapter.yml` (or equivalent lookup) — skill → book chapter URL/path + assignment.
- `learning_plan.template.md` — fill-in-the-blanks plan template.

## Expected Outputs (per student, private)

- `learning_plan.md` — the personalized, ordered, paced plan (with AI-disclosure label).
- `progress.md` — completion/state tracker.
- Both **gitignored** — generated into the student's own clone, never committed.

## Validation Approach

- **Runs on Sonnet**: the entire flow completes and yields a sensible plan when executed on `claude-sonnet-4-6` (not just Opus). Headline acceptance gate.
- **Grading fidelity**: probe grading matches the answer keys on fixture answers (correct / partial / wrong) → expected levels.
- **Determinism**: same assessment inputs → same gap diff → same plan ordering.
- **Plan sanity**: every assigned module maps to a real book chapter that exists in the mirror; no gap left unaddressed; ordering respects prerequisites.
- **Tone**: assessment dialogue reads as welcoming and honest (spot-check), never flattering or harsh.
- **Socratic behavior**: the agent **asks before telling** — it offers hint-ladder guiding questions before answers, and records scaffolding depth into the level. Spot-check that it follows the ladder rather than dumping the solution.

## Completion Criteria

- [ ] Skill-map, rubric, probe bank (with keys **+ hint ladders**), per-concept guiding-question banks, chapter lookup, and plan template authored
- [ ] `CLAUDE.md` runtime procedure drives the full assess→diff→plan→track loop
- [ ] A test run **on Sonnet** produces a correct, sensible personalized plan for ≥2 fixture student profiles (e.g. "near-beginner", "intermediate")
- [ ] Generated artifacts are gitignored (privacy verified)
- [ ] All book-chapter links resolve against the current mirror (`master`)
- [ ] `ethical-check` clean (attribution, privacy, AI-disclosure, no fabricated scoring)

## Assumptions & Limitations

**Assumptions**:
- Students run inside the lab Claude environment on the Hub (have `~/.claude` config + `ethical-check`).
- The book mirror is complete and current (`master`), and its chapter paths are stable.
- A single generic coding-readiness target is adequate for v1 (skills are shared across lab projects).

**Limitations / out of scope (v1)**:
- **No math or physics pillars** (Phase 2).
- **No per-project skill-maps** (scaleworm vs bravoseis tailoring) — Phase 2.
- No PI cross-student progress dashboard — Phase 3.
- Not a graded course; it's a readiness ramp, not a certification.

## Notes

- Built SpecKit-native; this spec derives from the design locked 2026-06-02 (see lab memory `project_student_onramp.md`).
- Next: `/speckit.clarify` for residual ambiguity, then `/speckit.plan` → `/speckit.tasks` → `/speckit.implement`.
- Build/author on **Opus**; validate the student path on **Sonnet** before shipping.
