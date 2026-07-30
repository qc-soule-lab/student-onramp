*AI-generated draft (Claude, Anthropic) — for review.*

# student-onramp

An agentic, Claude-driven onboarding curriculum for new **qc-soule-lab** students. A student clones this repo, launches Claude, and Claude assesses where they are and guides them along a **domain spine with coding woven in just-in-time** — toward being ready to contribute to a lab project.

**Status:** v1 **integrated vertical slice** built and demo-walkable; skeleton in review (data staging + Sonnet acceptance pending). The slice — *"From the map to the tidal signal"* — is 5 **gated modules** (0 reach the data → 1 locate Axial → 2 why it's there → 3 get the data → 4 see the seafloor tide), each binding a domain question to the coding tool it needs.

## How a student uses it
0. **Spawn the Large (16 GB) server** at the JupyterHub login/spawn page before you begin — the data steps hang or crash the kernel on a Small profile. (The onramp double-checks this on start and will tell you to respawn if you're on Small.)
1. Clone this repo, launch `claude` in it, and say *"Assess me and walk me through it one step at a time."*
2. Claude runs a short **hybrid, Socratic assessment** — conversational triage + a few hands-on probes (domain *and* coding), graded against answer keys.
3. Claude writes a personalized, paced **`journey_plan.md`** + **`progress.md`** into *your own clone* — private (gitignored), never pushed.
4. Modules **unlock progressively** as you clear each one's capstone; after each activity Claude asks for quick **feedback** (so the curriculum improves between students).
5. On later sessions say *"continue"* to resume; *"demo mode"* (for the PI) narrates the pedagogy without assessing or writing files.

## Design notes
- **Built on Opus, run on Sonnet.** Students run this on Sonnet seats, so the intelligence lives in explicit *structure* — skill-map, scoring rubric, a probe bank with answer keys, a skill→chapter lookup, and a plan template — rather than runtime model cleverness. Acceptance = it works **run on Sonnet**, not just Opus.
- **Content backbone:** the book mirror `qc-soule-lab/earth-env-data-science-book` is *referenced* (linked), not duplicated — preserving CC BY-SA 4.0 attribution. Each book "Part" maps to a skill area; its `assignments/` become hands-on probes + exercises.
- **Privacy:** a student's assessment results and plan stay local to their clone (see `.gitignore`); skill gaps are sensitive.

## Run it
```bash
uv sync                 # student runtime: numpy/pandas/matplotlib/xarray/netcdf4 (+ dev: pytest)
claude                  # launch IN this repo so CLAUDE.md auto-loads
#   then: "Assess me and walk me through it one step at a time."
#   or (PI review): "demo mode"
uv run pytest           # structure + link guards (data-integrity test arrives with Stage A)
```

## Build flow (SpecKit)
`/speckit.constitution` → `/speckit.specify` → `/speckit.clarify` → `/speckit.plan` → `/speckit.tasks` → `/speckit.implement`
Current: spec/plan/tasks done; quick-demo skeleton implemented on `001-coding-onramp-v1`. Remaining build → `specs/001-coding-onramp-v1/workflow_plan.md`.
