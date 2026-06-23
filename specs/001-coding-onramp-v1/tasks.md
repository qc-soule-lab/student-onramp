# Tasks: Onramp v1 — Integrated Vertical Slice ("From the map to the tidal signal")

*AI-generated draft (Claude, Anthropic) — for review.*

**Spec**: `specs/001-coding-onramp-v1/spec.md`
**Plan**: `specs/001-coding-onramp-v1/plan.md`
**Generated**: 2026-06-09

## Format

```text
- [ ] T### Description with file path or specific action
```

- Task IDs are sequential (T001, T002, …); QC tasks labeled explicitly.
- This is a **curriculum-build**: most artifacts are structured content (YAML/MD) + a deterministic runtime procedure, not analysis scripts. Phases follow the plan's **Stages A–E**.
- Constitution gates apply throughout: **I** Sonnet-runnable (lookup/grade/fill, no Opus-only cleverness), **II** privacy (generated artifacts gitignored), **III** honest scoring, **IV** attribution (book linked not vendored), **V** inspectable, **VI** Socratic-by-structure (hint ladders), **VII** woven (every step binds domain + coding + chapter).

---

## Phase 0: Research — RESOLVED

**Purpose**: Confirm method decisions before build (all settled in `research.md`).

- [x] T001 Research resolved in `research.md`: bathymetry source (GMRT subset), tidal dataset + window (2015-01-17→31, 336 rows, M2-verified), plate-boundary handling (shp→CSV, no geo deps), Sonnet acceptance method (live fixture-scripted protocol), probe sourcing (book `assignments/` + bespoke).
- [ ] T002 Research (non-blocking, decide at build): does step-2 conceptual content need its own probe or ride on triage? **Default**: triage + one retrieval question (`p03_why_axial`).

**Checkpoint**: Method decisions documented; only the non-blocking T002 remains, with a default.

---

## Phase 1: Setup

**Purpose**: Environment + project skeleton ready.

- [ ] T003 Create `pyproject.toml` (uv) — student runtime stack: numpy, pandas, matplotlib, xarray, netcdf4; dev group: pytest; staging-only extra: pyshp. Model on `claude-config/pyproject.student.example.toml`, trimmed to the slice. **No geo deps** (boundary pre-converted to CSV).
- [ ] T004 Create directory structure per plan: `journey/`, `skill_maps/`, `assessment/probes/`, `assessment/question_banks/`, `content/`, `data/`, `scripts/`, `templates/`, `validation/fixtures/`, `tests/`.
- [ ] T005 QC: Verify `.gitignore` already excludes generated `journey_plan.md`, `progress.md`, `students/`, `*.profile.md` (Constitution II) — confirm, don't duplicate.

**Checkpoint**: `uv sync` succeeds; directories exist; privacy gitignore confirmed.

---

## Phase 2: Stage A — Data Staging  *(runs in parallel with Phase 3)*

**Purpose**: Three small, committed, offline-friendly datasets + provenance.

- [ ] T006 Implement `scripts/stage_data.py` — one-shot (PI-run): GMRT GridServer fetch (Axial bbox, ~100 m) → NetCDF; extract BOTPT window from `~/my_data/axial/axial_botpt/axial_mj03f_bpH.csv`; convert MGDS Bobbitt shapefile → lon/lat CSV. Include integrity asserts inline.
- [ ] T007 Stage `data/axial_bathymetry_gmrt.nc` (GMRT subset, ~2–5 MB).
- [ ] T008 Stage `data/axial_botpt_2015-01-17.csv` (assert exactly 336 hourly rows, **0 NaN**).
- [ ] T009 Stage `data/plate_boundary.csv` (lon, lat, segment_id).
- [ ] T010 Write `data/PROVENANCE.md` — per file: source, license, citation, regeneration recipe (GMRT: Ryan et al. 2009 + version string; OOI: NSF/OOI acknowledgment; MGDS Bobbitt: verbatim citation, CC BY-NC-SA preserved).
- [ ] T011 QC: `tests/test_data_integrity.py` — BOTPT window NaN-free + M2 (~12.4 h) dominant via FFT; bathy grid loads; boundary CSV parses.

**Checkpoint**: Four `data/` files present; `test_data_integrity.py` passes; provenance complete.

---

## Phase 3: Stage B — Structured Content  *(runs in parallel with Phase 2)*

**Purpose**: The slice + its skill/chapter wiring.

- [ ] T012 `journey/journey.yml` — 4 steps; each binds domain concept(s) + coding skill(s) + book chapter(s) + capstone; step 4 carries the tmpsf/magma2vents **bridge** note. (Woven invariant — Constitution VII.)
- [ ] T013 `skill_maps/slice_v1.yml` — target competencies (domain + coding), chapter-tagged, each linked to its probe(s).
- [ ] T014 `content/skill_to_chapter.yml` — coding skill → book chapter path/URL + assignment (transcribe the 2026-06-03 book→chapter mapping; verify against mirror `master`).
- [ ] T015 `journey/readings.md` — 0a/0b/0c links: OOI Data Labs 1/2/3, tidal Nugget, seafloor spreading (referenced, not vendored).

**Checkpoint**: YAMLs parse; every journey step has domain + coding + chapter; reading links listed.

---

## Phase 4: Stage C — Assessment Layer  *(needs Phase 3 skill-map)*

**Purpose**: Probes, rubric, and Socratic banks — the graded, Sonnet-safe core.

- [ ] T016 `assessment/rubric.md` — 3-level thresholds (Novice/Developing/Proficient) on probe score + hint-ladder depth; per-step treatment lookup (Novice→full scaffold, Developing→compressed, Proficient→capstone-only). Pure table.
- [ ] T017 Probe `assessment/probes/p01_meters_per_degree.md` (domain, step 1) — prompt + answer key + 3-rung hint ladder + scoring→level. *(adapt from exemplar roadmap)*
- [ ] T018 Probe `assessment/probes/p02_matplotlib_bathy.md` (coding, step 1) — bathymetry plot read-back. *(bespoke)*
- [ ] T019 Probe `assessment/probes/p03_why_axial.md` (domain, step 2) — retrieval/explanation. *(triage-linked; see T002)*
- [ ] T020 Probe `assessment/probes/p04_xarray_inspect.md` (coding, step 3) — load + inspect dims. *(adapt from book `assignments/`, attributed)*
- [ ] T021 Probe `assessment/probes/p05_pandas_resample.md` (coding, step 4) — resample + read off the ~12.4 h period. *(bespoke)*
- [ ] T022 `assessment/question_banks/` — per-concept Socratic guiding-question banks (teaching/remediation), one per domain/coding concept in the slice.
- [ ] T023 QC: every skill-map competency has ≥1 probe; each probe has key + hint ladder + scoring; probe↔skill↔chapter cross-refs all resolve.

**Checkpoint**: Each competency probed with a key + ladder; rubric maps scores→levels→treatment; cross-refs resolve.

---

## Phase 5: Stage D — Runtime Procedure + Templates  *(needs A paths + B + C)*

**Purpose**: The product — the deterministic procedure that drives a student session.

- [ ] T024 `CLAUDE.md` — numbered runtime procedure: **1 Assess** (hybrid Socratic triage + probes, grade vs keys) → **2 Personalize** (skill-map diff → per-step skip/compress/scaffold via rubric lookup) → **3 Guide the slice** (walk 4 steps, coding woven just-in-time, pull chapters, Socratic) → **4 Track** (`progress.md`, resume/re-probe). Every operation a lookup/grade/fill — Sonnet-safe.
- [ ] T025 `CLAUDE.md` **demo/walkthrough mode** (PI review affordance): on "demo mode", Claude *narrates* the pedagogy — shows triage questions, a sample probe + its hint ladder, and the skip/scaffold decision for a chosen level — **without** requiring real answers or writing private artifacts.
- [ ] T026 `templates/journey_plan.template.md` — fill-in-the-blanks personalized journey, **AI-disclosure label baked in** (Constitution IV).
- [ ] T027 `templates/progress.template.md` — step/skill completion tracker.
- [ ] T028 Update `README.md` with the student run section (launch → "assess me" → the slice; mention demo mode).
- [ ] T029 QC: every artifact the procedure references exists (no dangling path); procedure contains no step requiring Opus-only judgment (Constitution I self-audit).

**Checkpoint**: `CLAUDE.md` drives assess→personalize→guide→track; demo mode walkable; templates + README run section in place.

---

## Phase 6: Stage E — Validation  *(needs all)*

**Purpose**: Prove it runs on Sonnet, end-to-end, for two profiles.

- [ ] T030 `tests/test_structure.py` — YAMLs parse; skills↔probes↔chapters cross-refs resolve; **every journey step is woven** (domain + coding + chapter) — the Constitution VII guard.
- [ ] T031 `tests/test_links.py` — every `skill_to_chapter.yml` path exists in the book mirror (`master`).
- [ ] T032 `validation/fixtures/profile_novice.md` — scripted near-beginner answers (full-scaffold path).
- [ ] T033 `validation/fixtures/profile_intermediate.md` — scripted partial-skills answers (mixed skip/compress).
- [ ] T034 `validation/sonnet_acceptance_protocol.md` — how to run + score an acceptance pass (launch on `claude-sonnet-4-6`, answer from fixture, traverse 4 steps, score against checklist: correct leveling, ladders followed not improvised, coding attached to a domain step, artifacts generated + gitignored).
- [ ] T035 QC: `uv run pytest` — all green (data integrity + structure + links).
- [ ] T036 Sonnet acceptance run: `profile_novice` reaches the end state with full scaffolding.
- [ ] T037 Sonnet acceptance run: `profile_intermediate` correctly skips/compresses known steps, still reaches the end state.
- [ ] T038 QC: spec completion criteria all met; `ethical-check` clean (attribution, privacy, AI-disclosure, no fabricated scoring); book links resolve.

**Checkpoint**: pytest green; both Sonnet passes reach the end state with correct skip/scaffold behavior; ethical-check clean.

---

## Dependencies

```text
Phase 1 (Setup)
     ↓
   ┌─┴─────────────┐
Phase 2 (A: data) Phase 3 (B: content)     ← parallel
   └─┬─────────────┘
     ↓ (B feeds C)
Phase 4 (C: assessment)
     ↓ (A paths + B + C feed D)
Phase 5 (D: CLAUDE.md + templates)
     ↓
Phase 6 (E: tests, fixtures, Sonnet acceptance)
```

**Parallel opportunities**: A ∥ B; within C, probes per skill are independent; within E, the three test modules are independent. Otherwise sequential.

---

## Completion Criteria (from spec.md — all must hold)

- [ ] Slice, skill-map, rubric, probe bank (keys + hint ladders), question banks, chapter lookup, readings, sample data, templates authored
- [ ] `CLAUDE.md` drives assess → personalize → guide-slice → track (+ demo mode)
- [ ] A run **on Sonnet** completes the full slice for ≥2 fixture profiles (near-beginner, intermediate) with appropriate skip/scaffold
- [ ] Coding skills verified **woven** (each attached to a domain step) — `test_structure.py`
- [ ] Generated artifacts gitignored (privacy verified)
- [ ] Book-chapter links resolve against the mirror (`master`) — `test_links.py`
- [ ] `ethical-check` clean (attribution, privacy, AI-disclosure, no fabricated scoring)

---

## Notes

- **Suggested start**: T003–T005 (Setup), then split into the parallel **A (data, T006–T011)** and **B (content, T012–T015)** tracks.
- **Quickest path to a walkable demo** (your "demo mode" ask): T012 (journey) → T016 (rubric) → a couple of T017–T021 probes → T024–T025 (`CLAUDE.md` + demo mode). Data staging (A) and tests (E) can follow — demo mode narrates without needing real data.
- Commit after each phase; QC failures block progression. Author on Opus; **acceptance measured on Sonnet** (Constitution I).
- If a task reveals new requirements, add tasks rather than expanding scope silently.

---

## Build log — quick-demo skeleton (2026-06-09)

**Done (walkable demo path):** T012 `journey/journey.yml` · T013 `skill_maps/slice_v1.yml` · T014 `content/skill_to_chapter.yml` (paths verified vs mirror `master`) · T015 `journey/readings.md` · T016 `assessment/rubric.md` · T017–T021 all 5 probes · T024 `CLAUDE.md` procedure · T025 demo mode · T026–T027 templates. Cross-refs validated (probes/chapters/readings/enrichment all resolve).

**Not yet:** T003–T005 (pyproject/dirs done ad-hoc, no `uv` env) · T006–T011 (Stage A data staging) · T022 question_banks · T023 full probe-coverage QC · T028 README run section · T029 procedure self-audit · T030–T038 (tests, fixtures, Sonnet acceptance).

## New features added mid-build (fold into the plan)

- [ ] T039 **Per-activity feedback loop** — DONE in skeleton (`CLAUDE.md` A4 + `templates/feedback.template.md` + `feedback.md` gitignored). Remaining: cover in `test_structure.py`; add the consent/share step to the Sonnet protocol; decide collection channel (local+consent default vs azure_lake upload vs GitHub issue).
- [ ] T040 **Progressive gating** — DONE in skeleton (`journey.yml` per-step `gate.must`/`unlocks` + `progression`; `CLAUDE.md` A3 gate check + A5 lock tracking; `progress.template.md` gate column). Remaining: `test_structure.py` asserts a single linear unlock chain (1→2→3→4→end, no orphans/cycles); fixtures exercise a failed-gate→remediate path.
- [ ] T041 **Optional enrichment pointers** — DONE in skeleton (`journey.yml` step-1 `enrichment: [geomapapp]`; `readings.md` enrichment section; `CLAUDE.md` "optional, non-gating, Novice on-ramp"). GeoMapApp + SERC are **link-only** (ethical-check 2026-06-09: GeoMapApp = MGDS/Lamont free edu, same GMRT data; SERC = link-only, no content copied, terms unverified, dated 2012).
- [ ] T042 **Rutgers OOI Data Labs wired** — DONE (`readings.md` lab1–lab4 by reference; CC BY-NC-SA 4.0, citation + NSF OCE-1831625 recorded). Labs 5–8 = later breadth.
- [ ] T043 **Persona acceptance harness** (PI request 2026-06-10) — four agent-driven student personas (HS-senior/weak-STEM → first-year → upper-undergrad → incoming-grad) run the slice on Sonnet via paired headless sessions; Opus grader audits invariants + the cross-persona scaffold gradient + **modeled time-on-task per step (novice:advanced ratio)**. **Plan**: `validation/persona_acceptance_plan.md` (PI-approved 2026-06-10). **Built**: 4 persona cards (`validation/personas/`), driver (`validation/run_persona_test.py` + unit tests), `grader_checklist.md`; templates gained the missing Step-0 row. Remaining: run P4→P3→P2→P1, grade, write `persona_acceptance_report.md`. Complements, doesn't replace, the human fixture runs (T036–T037).
