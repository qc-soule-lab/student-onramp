# student-onramp Constitution

*AI-generated draft (Claude, Anthropic) — for review. Principles below govern this project; edit freely.*

## Project Context

`student-onramp` is an **agentic, Claude-driven onboarding curriculum** for new qc-soule-lab students. A student clones the repo, launches Claude, Claude assesses where they are, and guides them along a **domain spine with coding woven through** — toward being ready to contribute to a lab project. Intended users: new lab students (e.g. Alexa); PI/collaborators author and review.

**Curriculum taxonomy (PI-defined):** a domain spine — **0a** initial earth-science background (topography, lat/long, seafloor spreading, sound & light) → **0b** OOI & Axial Seamount familiarity (collecting ocean data, plate tectonics/seafloor, seafloor change in a volcanic setting) → **0c** hydrothermal systems & fauna (life on a vent, tidal diffuse-flow) → **project** — with the **"working with data" coding skills (Linux, Python, oceanographic data) woven in just-in-time** along the way (Principle VII), drawing on the *Earth & Environmental Data Science* book (Abernathey et al., CC BY-SA 4.0) as the coding reference.

**v1 = one integrated vertical slice** through this spine (a thin but complete path that touches the domain tiers with coding woven in, end-to-end), proving the model before breadth is added. Full tier breadth, per-project skill-maps, and math/physics depth are later phases.

## Core Principles

### I. Build on Opus, Run on Sonnet (non-negotiable)

Students run this on **Sonnet** (Standard seats); it is authored on Opus. Therefore the intelligence must live in **explicit structure, not runtime model cleverness**: a skill-map, a scoring rubric with thresholds, a probe bank with answer keys, a skill→chapter lookup, and fill-in templates. The runtime job must reduce to "follow a defined procedure, grade against keys, look up mappings, fill templates." **Acceptance is measured run on Sonnet, not Opus.** Any feature that only works because Opus is clever is a defect.

### II. Student Privacy

A student's assessment results, skill gaps, personalized plan, and captured **misconceptions** are **sensitive and stay local to their own clone** — generated artifacts (`journey_plan.md`, `progress.md`, `feedback.md`, `misconceptions.md`, profiles) are gitignored and never committed to the shared repo. No student's results are shared without their consent. Misconception notes (the actual wrong answers — invaluable for evolving the curriculum) follow the same rule: captured locally, shared only with consent, and aggregated **anonymously** into `validation/misconception_ledger.md`.

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

### VII. Computing is Woven, Not Terminal

Coding is **never taught in isolation or saved for the end.** It is introduced **just-in-time, in service of the science** — the student learns a tool at the moment a domain question demands it (matplotlib to *see* the bathymetry, xarray to *pull* the OOI data, pandas to *expose* the tidal signal in diffuse vent flow). The book is a **reference drawn on chapter-by-chapter as topics demand**, not a course completed front-to-back. Every coding skill enters attached to a concrete domain motivation. The curriculum is a **domain spine (earth science → OOI/Axial → vents & fauna → project) with coding woven through**, not a sequence of pillars that ends in coding.

## Technical Environment

- Python via **uv**; runs inside the lab Claude Code environment on the OOI JupyterHub (students inherit `~/.claude` config + the `ethical-check` skill).
- Content backbone: the org mirror `qc-soule-lab/earth-env-data-science-book` (referenced by URL/path, not vendored).
- Built SpecKit-native (`.specify/` + `/speckit.*`); changes via branch + PR.

## Content Sources

- **Earth & Environmental Data Science book** — `qc-soule-lab/earth-env-data-science-book` (CC BY-SA 4.0). Carries the coding/data-science curriculum; its `assignments/` provide ready-made hands-on probes and exercises.

## Project Notes

- **v1 = one integrated vertical slice** (domain spine, coding woven — Principle VII); full tier breadth, math + physics pillars, and per-project skill-maps = Phase 2; optional PI progress dashboard = Phase 3.
- Governance follows the lab norms (branch + PR, pytest before commit, `ethical-check` before introducing resources or shipping prose).

---
**Version**: 0.1.0 (draft) · **Ratified**: 2026-06-02 (pending PI review)
