# Analysis Plan: Onramp v1 — Integrated Vertical Slice ("From the map to the tidal signal")

*AI-generated draft (Claude, Anthropic) — for review. All parameters and figures are derived from version-controlled scripts and data.*

**Spec**: `specs/001-coding-onramp-v1/spec.md` (clarify complete 2026-06-05)
**Created**: 2026-06-07
**Status**: Draft

## Summary

Build the artifacts that let a student clone this repo, launch Claude (Sonnet), and be assessed → personalized → guided along the confirmed 4-step slice (locate Axial → why it's there → get the data → see the M2 tide in bottom pressure). This is a **curriculum-build plan**, not a data-analysis plan: the "pipeline" produces structured content (YAML journey/skill-map, rubric, probe bank with keys + hint ladders, chapter lookup, templates) plus three small pre-staged datasets, all wired together by a deterministic `CLAUDE.md` runtime procedure. Acceptance = the full slice runs **on Sonnet** for ≥2 fixture profiles (Constitution I).

## Analysis Environment

**Language/Version**: Python 3.13 (Hub conda python; project managed with **uv** per lab standard)
**Key packages (student runtime)**: numpy, pandas, matplotlib, xarray, netcdf4 — exactly the slice's woven-coding stack; **no geo deps** (plate boundary pre-converted to CSV)
**Dev/build extras**: pytest (dev group), pyshp (staging only — shapefile→CSV conversion)
**Environment file**: `pyproject.toml` — to be created (modeled on `claude-config/pyproject.student.example.toml`, trimmed to the slice stack)

## Compute Environment

- [x] Shared server (OOI JupyterHub; students inherit lab `~/.claude` + ethical-check)
- **Data scale**: tiny — committed datasets total <10 MB (bathy subset ~2–5 MB, BOTPT 336 rows, boundary CSV ~30 KB)
- **Timeline pressure**: Alexa's onboarding is the driver; no hard date
- **Known bottlenecks**: none at runtime (offline-friendly by design); GMRT fetch happens ONCE at staging, not per-student

## Constitution Check

- [x] **I Build-Opus/Run-Sonnet** — every runtime operation in this plan is lookup / grade-against-key / follow-ladder / fill-template; Sonnet acceptance protocol is a planned artifact
- [x] **II Privacy** — generated `journey_plan.md` / `progress.md` / profiles gitignored (already in repo `.gitignore`)
- [x] **III Honest assessment** — rubric thresholds + answer keys; hint-ladder depth feeds level
- [x] **IV Attribution** — ethical-check passed 2026-06-07 for all three data sources (GMRT: Ryan et al. 2009 + version; OOI: NSF/OOI acknowledgment; MGDS Bobbitt: verbatim citation, CC BY-NC-SA preserved); `data/PROVENANCE.md` is a required artifact; book referenced by URL, never vendored
- [x] **V Inspectable** — plan derivation = skill-map diff + rubric lookup; every assignment traceable
- [x] **VI Socratic-by-structure** — hint ladders + question banks are explicit build artifacts
- [x] **VII Woven** — `journey.yml` schema REQUIRES each step to bind domain concept(s) + coding skill(s) + chapter(s); a step with free-floating coding fails `test_structure.py`

**Issues to resolve**: none — Phase-0 questions resolved in `research.md` (bathymetry source, dataset window, shapefile handling, validation method).

## Project Structure

```text
CLAUDE.md                       # runtime procedure — drives the student session (THE product)
README.md                       # student-facing quickstart (exists; will gain run instructions)
pyproject.toml                  # uv env: slice stack + pytest dev group
journey/
├── journey.yml                 # 4 steps: domain tags + skills + chapters + capstone per step
└── readings.md                 # 0a/0b/0c links: OOI Data Labs 1/2/3, tidal Nugget, spreading
skill_maps/
└── slice_v1.yml                # target competencies (domain + coding), chapter-tagged
assessment/
├── rubric.md                   # 3-level thresholds (probe score + hint depth) → treatment lookup
├── probes/                     # one .md per probe: prompt, answer key, 3-rung hint ladder, scoring
└── question_banks/             # per-concept Socratic guiding questions (teaching/remediation)
content/
└── skill_to_chapter.yml        # coding skill → book chapter path/URL + assignment
data/
├── axial_bathymetry_gmrt.nc    # staged: GMRT subset, Axial region
├── axial_botpt_2015-01-17.csv  # staged: 336 hourly rows, NaN-free, M2-verified
├── plate_boundary.csv          # staged: MGDS shp → plain lon/lat segments CSV
└── PROVENANCE.md               # source, license, citation, regeneration recipe per file
scripts/
└── stage_data.py               # PI-run once: GMRT fetch + BOTPT window extract + shp→CSV
templates/
├── journey_plan.template.md    # fill-in-the-blanks personalized plan (AI-disclosure label baked in)
└── progress.template.md        # step/skill tracker
validation/
├── fixtures/
│   ├── profile_novice.md       # scripted answers: near-beginner (full scaffold path)
│   └── profile_intermediate.md # scripted answers: partial skills (mixed skip/compress)
└── sonnet_acceptance_protocol.md  # how to run + score the acceptance passes
tests/
├── test_data_integrity.py      # BOTPT window NaN-free + M2 peak via FFT; bathy grid loads; boundary CSV parses
├── test_structure.py           # YAMLs parse; skills↔probes↔chapters cross-refs all resolve; every step woven
└── test_links.py               # book chapter paths exist in the mirror
```

**Structure notes**: no `data/raw→processed` split — staged files ARE the immutable inputs (regenerable via `stage_data.py`; raw sources live in `~/my_data` / GMRT / MGDS, never modified).

## Build Pipeline

### Stage A — Data staging (`scripts/stage_data.py`)
- **Input**: GMRT GridServer API (Axial bbox, ~100 m res) · `~/my_data/axial/axial_botpt/axial_mj03f_bpH.csv` · MGDS shapefile
- **Processing**: fetch/subset; extract 2015-01-17→01-31 window (assert 336 rows, 0 NaN); shp → lon/lat CSV
- **Output**: the four `data/` files incl. `PROVENANCE.md`

### Stage B — Structured content
- **Input**: spec slice table; book mirror TOC; resource-evaluation KEEP/ADAPT set; roadmap links
- **Output**: `journey/journey.yml`, `skill_maps/slice_v1.yml`, `content/skill_to_chapter.yml`, `journey/readings.md`
- Book→chapter mapping already drafted (lab memory, 2026-06-03 overnight agent) — transcribe + verify against mirror

### Stage C — Assessment layer
- **Input**: skill map (B); rubric rules from spec (3-level + hint-depth)
- **Output**: `assessment/rubric.md`, `probes/` (≥1 probe per skill incl. domain triage Qs; meters-per-degree probe from the exemplar roadmap), `question_banks/`
- Probe sources: book `assignments/` (adapt, attribute) + bespoke (bathy plot, BOTPT resample)

### Stage D — Runtime procedure + templates
- **Input**: all of B + C
- **Output**: `CLAUDE.md` (numbered assess→personalize→guide→track procedure), both templates, README run section

### Stage E — Validation
- **Input**: everything
- **Output**: `tests/` (pytest), `validation/fixtures/`, `sonnet_acceptance_protocol.md`; then 2 live Sonnet acceptance runs

## Script/Notebook Plan

| Artifact | Purpose | Inputs | Outputs |
|---|---|---|---|
| `scripts/stage_data.py` | One-shot data staging w/ integrity asserts | GMRT API, local BOTPT CSV, MGDS shp | `data/*` + PROVENANCE |
| `tests/test_data_integrity.py` | Guard staged data (NaN-free, M2 present, files load) | `data/*` | pass/fail |
| `tests/test_structure.py` | Guard content wiring (cross-refs, woven invariant) | YAMLs, probes | pass/fail |
| `tests/test_links.py` | Guard book links vs mirror | `skill_to_chapter.yml` | pass/fail |
| `CLAUDE.md` | Deterministic runtime procedure | all content artifacts | student session behavior |

(Students write their own exercise code during the slice; the repo ships no student-facing analysis scripts — by design, Constitution VII.)

## Dependencies

```text
A (data)  B (content)        ← independent, parallel
    \        ↓
     \    C (assessment)     ← needs skill map
      \      ↓
       → D (CLAUDE.md + templates)  ← needs A paths + B + C
             ↓
          E (tests, fixtures, Sonnet acceptance runs)
```

**Parallel opportunities**: A ∥ B; within C, probes per skill are independent; within E, the three test modules are independent.

## Open Questions

All Phase-0 questions resolved — see `research.md`. Remaining (non-blocking, revisit at tasks):
- [ ] Whether step-2 conceptual content needs its own probe or rides on triage only (default: triage only, one retrieval question)

## Notes

- Dataset window empirically verified 2026-06-05 (FFT: M2 12.48 h dominant; 22 NaNs lurk Jan 15–16 *outside* the chosen window) — see research.md.
- Next: `/speckit.tasks` to break stages A–E into ordered tasks.
