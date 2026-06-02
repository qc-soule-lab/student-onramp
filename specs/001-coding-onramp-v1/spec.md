# Specification: Integrated Vertical Slice (v1)

*AI-generated draft (Claude, Anthropic) — for review.*

**Directory**: `specs/001-coding-onramp-v1`
**Created**: 2026-06-02
**Status**: Draft (revised — v1 reframed from "coding pillar" to "integrated vertical slice")
**Input**: "agentic onramp that assesses a new student and guides them along a domain spine with coding woven in just-in-time"

## Goal / Problem

New lab students arrive with widely varying backgrounds — some without oceanography/earth science, most without much coding. We need a **self-serve, Claude-driven** experience that meets a student where they are and walks them along the lab's **domain spine with coding woven in just-in-time** (Constitution VII), toward being ready to contribute.

**v1 = one *integrated vertical slice*** through that spine: a thin but **complete** path that touches the domain tiers (0a→0b→0c) with coding introduced exactly when the science needs it, ending at the doorstep of a real lab project. This proves the integrated, assess-driven, woven model end-to-end before breadth is added.

## Users

- **Primary**: a new student (e.g. Alexa) running Claude on **Sonnet** in this repo on the Hub.
- **Secondary**: PI/collaborators (author/review the slice, skill-map, rubric, probes).

## The v1 Vertical Slice (proposed — "From the map to the tidal signal")

A single coherent journey from *"where/what is Axial"* to *"see a real signal in vent data,"* coding woven throughout:

| Step | Domain (spine) | Coding woven in (just-in-time) |
|---|---|---|
| 1. **Locate it** | lat/long + Earth's topography (0a) | Python + matplotlib to plot Axial's location & bathymetry; Jupyter/Linux to run it |
| 2. **Why it's there** | plate tectonics / seafloor + OOI observatory (0b) | *(conceptual — Socratic Q&A, light reading)* |
| 3. **Get the data** | how OOI collects ocean data (0b) | xarray + data access to load a real Axial dataset |
| 4. **See the science** | tidal fluctuation of diffuse vent flow (0c) | pandas time-series (resample/plot) to reveal the tidal periodicity |

**End state:** the student has touched 0a/0b/0c concepts *and* learned Jupyter/Python/matplotlib/xarray/pandas — each in service of a real question — landing at the doorstep of the thermal / diffuse-flow projects (tmpsf, magma2vents). *(Slice is swappable; this is the proposed v1 golden path.)*

## Inputs

- **Slice definition** (`slice/` or `journey.yml`) — the ordered steps above, each tagging its **domain concept(s)** + **coding skill(s)** + the **book chapter(s)** that teach the coding.
- **Skill-map** (`skill_maps/slice_v1.yml`) — the target competencies for *this slice* (the domain familiarity + coding skills it requires), book-chapter-tagged.
- **Content backbone** — the book mirror `qc-soule-lab/earth-env-data-science-book` (CC BY-SA 4.0), referenced not vendored, for the coding; light domain readings/links for 0a–0c concepts.
- **Pre-staged dataset** — a small, bundled (or stable-URL) Axial vent-temperature sample so step 3–4 are **reliable and offline-friendly** (no dependence on a live data portal at runtime).
- **Student responses** — triage answers + attempts at hands-on probes (domain *and* coding), graded against keys.

## Approach / Behavior

1. **Assess (hybrid, Socratic)**: Claude runs a friendly conversational triage across the slice's domain familiarity *and* coding skills, then a few **hands-on probes** from the probe bank. Struggling students get **Socratic hint-ladder** guidance; grading is **against answer keys**, and scaffolding depth feeds the level (Constitution III + VI).
2. **Personalize the journey**: diff assessed level vs. the slice's skill-map → decide, per step, what to **skip** (already known), **compress**, or **scaffold heavily**. The *path* is the fixed golden slice; the *depth/pace* is personalized.
3. **Guide the slice, coding woven in**: walk the student step-by-step; at each step introduce the needed coding tool **at the moment the science demands it**, pulling the relevant book chapter as reference. Socratic by default (Constitution VII + VI).
4. **Track progress**: write/update `progress.md`; on "continue," resume from the last step, re-probe if needed, advance or remediate.

Per Constitution I, every operation is a *lookup / grade-against-key / follow-the-hint-ladder / fill-template* step — so it runs reliably **on Sonnet**, not just Opus.

## Required Artifacts

- `CLAUDE.md` — deterministic, numbered **runtime procedure** for assess → personalize → guide-the-slice → track.
- `journey.yml` (slice definition) — ordered steps, each tagging domain concept(s) + coding skill(s) + book chapter(s).
- `skill_maps/slice_v1.yml` — slice target competencies (domain + coding), chapter-tagged.
- `assessment_rubric.md` — scoring thresholds + leveling rules.
- `probes/` — probe bank for **both domain and coding** skills in the slice; each probe has prompt + **answer key** + **hint ladder** (guiding Q → hint → reveal) with scaffolding-depth → level mapping.
- per-concept **guiding-question banks** for Socratic teaching/remediation.
- `skill_to_chapter.yml` — coding skill → book chapter URL/path + assignment.
- light **domain readings/links** for the 0a–0c concepts in the slice.
- pre-staged **sample dataset** for steps 3–4.
- `journey_plan.template.md` — fill-in-the-blanks personalized journey + `progress.md` template.

## Expected Outputs (per student, private)

- `journey_plan.md` — the personalized walk through the slice (with AI-disclosure label).
- `progress.md` — step/skill completion tracker.
- Both **gitignored** — generated into the student's own clone, never committed.

## Validation Approach

- **Runs on Sonnet, end-to-end**: a student can complete the whole slice (assess → all 4 steps → reach the end state) on `claude-sonnet-4-6`. Headline acceptance gate.
- **Grading fidelity**: probe grading matches answer keys on fixture answers (correct/partial/wrong → expected levels).
- **Personalization**: a strong fixture profile correctly **skips** known steps; a near-beginner gets **full scaffolding** — both reach the end state.
- **Integration check**: every coding skill is introduced *attached to* a domain step (none taught free-floating) — verifies Constitution VII.
- **Determinism**: same assessment inputs → same personalization decisions.
- **Socratic**: agent asks before telling; follows hint ladders; records scaffolding depth.
- **Reliability**: steps 3–4 work against the pre-staged dataset with no live-portal dependency.

## Completion Criteria

- [ ] Slice (`journey.yml`), skill-map, rubric, probe bank (keys + hint ladders), guiding-question banks, chapter lookup, domain readings, sample dataset, and templates authored
- [ ] `CLAUDE.md` runtime procedure drives assess → personalize → guide-slice → track
- [ ] A run **on Sonnet** completes the full slice for ≥2 fixture profiles (near-beginner, intermediate), each reaching the end state with appropriate skip/scaffold behavior
- [ ] Coding skills verified **woven** (each attached to a domain step), not terminal
- [ ] Generated artifacts gitignored (privacy verified)
- [ ] Book-chapter links resolve against the current mirror (`master`)
- [ ] `ethical-check` clean (attribution, privacy, AI-disclosure, no fabricated scoring)

## Assumptions & Limitations

**Assumptions**:
- Students run inside the lab Claude environment on the Hub (`~/.claude` config + `ethical-check`).
- The book mirror is complete/current (`master`); chapter paths stable.
- One vertical slice adequately proves the model for v1.

**Out of scope (later phases)**:
- **Breadth** — the full set of paths across all of 0a/0b/0c (v1 is ONE slice).
- **Per-project skill-maps** (scaleworm vs bravoseis tailoring).
- **Math & physics depth** as standalone pillars.
- PI cross-student progress dashboard.
- Not a graded course; a readiness ramp, not certification.

## Notes

- Reframed 2026-06-02 per PI directive: *coding is integrated across the curriculum, not terminal* → v1 became an integrated vertical slice (was "coding-first pillar"). See lab memory `project_student_onramp.md` for the full taxonomy + decisions.
- Proposed slice is swappable — confirm/adjust the golden path before `/speckit.plan`.
- Next: `/speckit.clarify` → `/speckit.plan` → `/speckit.tasks` → `/speckit.implement`. Author on **Opus**; validate on **Sonnet**.
