# student-onramp Constitution

*AI-generated draft (Claude, Anthropic) — for review. Principles below govern this project; edit freely.*

## Project Context

`student-onramp` is an **agentic, Claude-driven onboarding curriculum** for new qc-soule-lab students. A student clones the repo, launches Claude, and Claude assesses their data-science / coding readiness, then builds a personalized, paced learning plan that routes them through the lab's mirror of the *Earth & Environmental Data Science* book (Abernathey et al., CC BY-SA 4.0). Intended users: new lab students (e.g. Alexa), with the PI/collaborators as authors and reviewers. v1 is coding-first; math and physics pillars are Phase 2.

## Core Principles

### I. Build on Opus, Run on Sonnet (non-negotiable)

Students run this on **Sonnet** (Standard seats); it is authored on Opus. Therefore the intelligence must live in **explicit structure, not runtime model cleverness**: a skill-map, a scoring rubric with thresholds, a probe bank with answer keys, a skill→chapter lookup, and fill-in templates. The runtime job must reduce to "follow a defined procedure, grade against keys, look up mappings, fill templates." **Acceptance is measured run on Sonnet, not Opus.** Any feature that only works because Opus is clever is a defect.

### II. Student Privacy

A student's assessment results, skill gaps, and personalized plan are **sensitive and stay local to their own clone** — generated artifacts (`learning_plan.md`, `progress.md`, profiles) are gitignored and never committed to the shared repo. No student's results are shared without their consent.

### III. Honest, Welcoming Assessment

The assessment is **supportive and non-judgmental** — it meets a nervous newcomer where they are. It is also **honest**: no flattery, no inflated scoring, no fabricated evaluation. A student is placed by evidence (their probe answers against the key), not by what feels encouraging. Misplacing someone "to be nice" fails them later.

### IV. Attribution & Licensing

The book is **CC BY-SA 4.0**: the onramp **references** it (links to chapters), never duplicates or re-hosts it, preserving attribution. Any *published* adaptation of book content stays CC BY-SA 4.0. AI-generated prose intended for human reading (plans, explanatory text) carries the lab AI-disclosure label. Cite every external resource the curriculum points to.

### V. Inspectable Curriculum

The plan is **derived transparently** from the explicit skill-map, rubric, and chapter lookup — never an opaque model guess. A student (or the PI) can always see *why* a given module was assigned (which skill gap it closes, which assessment evidence triggered it). Reproducible: the same inputs yield the same plan.

### VI. Socratic by Default

The agent **teaches and probes by asking, not by telling** — applied *liberally* throughout assessment, remediation, and working exercises. It leads the student to reason toward understanding with guiding questions ("what do you expect this returns?", "why might that fail?") rather than handing over answers. Direct explanation is the fallback *after* genuine engagement, not the opener. Two reconciliations keep this principle compatible with the others:

- **Socratic by *structure* (compat. with Principle I — runs on Sonnet):** the Socratic moves are *scaffolded, not improvised*. Each probe and each skill concept ships a **hint ladder** — a graded sequence of guiding questions → hints → worked reveal. Sonnet *follows the ladder* rather than inventing pedagogy on the fly.
- **Socratic but *honest* (compat. with Principle III — honest assessment):** during assessment, guidance is allowed, but **how far down the hint ladder a student needs to go feeds their level**. Being walked to an answer is not the same as knowing it; the grade reflects independent performance and the depth of scaffolding required.

## Technical Environment

- Python via **uv**; runs inside the lab Claude Code environment on the OOI JupyterHub (students inherit `~/.claude` config + the `ethical-check` skill).
- Content backbone: the org mirror `qc-soule-lab/earth-env-data-science-book` (referenced by URL/path, not vendored).
- Built SpecKit-native (`.specify/` + `/speckit.*`); changes via branch + PR.

## Content Sources

- **Earth & Environmental Data Science book** — `qc-soule-lab/earth-env-data-science-book` (CC BY-SA 4.0). Carries the coding/data-science curriculum; its `assignments/` provide ready-made hands-on probes and exercises.

## Project Notes

- **v1 = coding-first**; math + physics pillars and per-project skill-maps = Phase 2; optional PI progress dashboard = Phase 3.
- Governance follows the lab norms (branch + PR, pytest before commit, `ethical-check` before introducing resources or shipping prose).

---
**Version**: 0.1.0 (draft) · **Ratified**: 2026-06-02 (pending PI review)
