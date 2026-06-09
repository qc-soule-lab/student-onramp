*AI-generated draft (Claude, Anthropic) — for review.*

# Workflow plan — finish onramp v1 with an agent team

**Created**: 2026-06-09 · **Status**: draft, ready to run *with PI present*
**Branch**: `001-coding-onramp-v1` (skeleton uncommitted)

## Goal
Take the walkable demo skeleton to a **Sonnet-accepted v1**: stage the data, deepen the assessment, lock in the test harness, and pass two fixture-profile acceptance runs — fanned out across a small agent team, integrated behind a structure gate.

## ⚠ Execution constraint (read before running)
The lab guardrail (memory `feedback_background_agents.md`, 2026-06-05) **denies *background* agents Write/Bash**. A multi-agent workflow left running unattended therefore **cannot write files**. Two safe ways to run this:
1. **Foreground-orchestrated (recommended):** run the workflow while the PI's session is active so the main (foreground) agent persists each agent's returned content to disk. Agents *produce* content; the orchestrator *writes* it.
2. **Confirm the setting first:** if background Write/Bash has since been re-enabled, the workflow can write directly. Verify before relying on it.
Either way: **no auto-commit/push** (lab rule = pytest-green + PI review first); build on the branch, leave for review.

## Overnight progress already landed (reduces this plan's scope)
Done foreground 2026-06-09 (uncommitted, for review): `tests/test_structure.py`, `tests/test_links.py`, `validation/fixtures/profile_novice.md`, `validation/fixtures/profile_intermediate.md`, `validation/sonnet_acceptance_protocol.md`, `pyproject.toml`, README run section. Step-0 probes (`p00`,`p00b`) already authored by PI. **So the workflow's remaining scope is Stage A + assessment depth + running acceptance + sourcing 2 TBD readings.**

## Remaining work → agent fan-out

| Agent | Scope | Tasks | Notes / inputs |
|---|---|---|---|
| **A · Data staging** | `scripts/stage_data.py` + `data/axial_bathymetry_gmrt.nc`, `data/axial_botpt_2015-01-17.csv`, `data/plate_boundary.csv` + `data/PROVENANCE.md` | T006–T010 | **Needs network (GMRT) + `~/my_data` BOTPT CSV + MGDS shp + PI confirm of the Jan-17→31 window.** Not offline-safe → this agent needs Bash + net; best run with PI present. |
| **B · Assessment depth** | `assessment/question_banks/` (one per domain/coding concept) + probe-coverage audit | T022–T023 | Pure authoring from `skill_maps/slice_v1.yml` + existing probes. Self-contained. |
| **C · Source TBD readings** | resolve `tidal_nugget` + `vi_basics` to CC-licensed/openly-usable links; wire into `readings.md`/`skill_to_chapter.yml` | (new) | **Each is an external resource → ethical-check + fetch first.** Link-only, never vendored. |
| **D · Data integrity test** | `tests/test_data_integrity.py` (BOTPT 336 rows, 0 NaN, M2 via FFT; bathy loads; boundary parses) | T011 | Depends on Agent A's outputs existing. |

**Integration gate:** `python -m pytest tests/ -q` green (structure + links + data integrity) **and** `test_structure.py` woven + single-gate-chain invariants hold.

**QC / adversarial pass (one reviewer agent):** audit against the constitution — woven invariant (no free-floating coding), honest scoring (keys present, no fabrication), attribution + AI-disclosure on all prose, **Sonnet-runnability** (every runtime step is lookup/grade/fill, no Opus-only judgment). Report defects → fix list.

**Final acceptance (PI / interactive, not automatable):** two live runs per `validation/sonnet_acceptance_protocol.md` — `profile_novice` (full scaffold, walks a failed-gate→remediate) and `profile_intermediate` (skips/compresses) — both reach the end state.

## Dependency shape
```
B (question_banks) ─┐
C (TBD readings)   ─┼─→ structure gate (pytest) ─→ QC pass ─→ Sonnet acceptance (PI)
A (data) ─→ D (integrity test) ─┘
```
A∥B∥C independent; D needs A. Modest fan-out (~4 build agents + 1 reviewer), low compute (well under the 24-worker cap; content authoring, not multiprocessing).

## Ready-to-run sketch (when PI present)
```
Workflow({ script: <build from this plan> })
  phase('Build')   → parallel: A(data), B(question_banks), C(readings)   [schema-returned content; orchestrator writes]
  phase('Tests')   → D(data integrity) after A; then run pytest
  phase('QC')      → reviewer agent, adversarial constitution audit
  phase('Report')  → defect list + acceptance-run checklist for the PI
```

## Acceptance (from spec.md)
pytest green · woven verified · artifacts gitignored · book links resolve · ethical-check clean · 2 Sonnet runs reach the end state with correct skip/scaffold/gate behavior.
