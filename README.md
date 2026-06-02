*AI-generated draft (Claude, Anthropic) — for review.*

# student-onramp

An agentic, Claude-driven onboarding curriculum for new **qc-soule-lab** students. A student clones this repo, launches Claude, and Claude assesses their data-science / coding readiness and builds a **personalized, paced learning plan** that routes them through the lab's mirror of the *Earth & Environmental Data Science* book (Abernathey et al., CC BY-SA 4.0).

**Status:** scaffolding / spec phase (SpecKit). **v1 = coding-first** (math + physics are Phase 2).

## How a student uses it (target experience)
1. Clone this repo, launch `claude`, and say *"Assess me and build my plan."*
2. Claude runs a short **hybrid assessment** — a conversational triage, then a few hands-on coding probes.
3. Claude writes a personalized **`learning_plan.md`** + **`progress.md`** into *your own clone* — kept private (gitignored), never pushed.
4. Work through it; on later sessions say *"continue"* and Claude advances or remediates.

## Design notes
- **Built on Opus, run on Sonnet.** Students run this on Sonnet seats, so the intelligence lives in explicit *structure* — skill-map, scoring rubric, a probe bank with answer keys, a skill→chapter lookup, and a plan template — rather than runtime model cleverness. Acceptance = it works **run on Sonnet**, not just Opus.
- **Content backbone:** the book mirror `qc-soule-lab/earth-env-data-science-book` is *referenced* (linked), not duplicated — preserving CC BY-SA 4.0 attribution. Each book "Part" maps to a skill area; its `assignments/` become hands-on probes + exercises.
- **Privacy:** a student's assessment results and plan stay local to their clone (see `.gitignore`); skill gaps are sensitive.

## Build flow (SpecKit)
`/speckit.constitution` → `/speckit.specify` → `/speckit.clarify` → `/speckit.plan` → `/speckit.tasks` → `/speckit.implement`
