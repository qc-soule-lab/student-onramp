*AI-generated draft (Claude, Anthropic) — for review.*

# Resource Evaluation — exemplar roadmap vs. the v1 vertical slice

Evaluates the lab's prior curriculum **exemplar** (see lab memory `reference_onramp_resource_roadmap.md` — an example, not a mandate) against the proposed v1 slice **"From the map to the tidal signal"** (steps: 1 locate Axial · 2 why it's there · 3 get the data · 4 see the tidal signal). Verdicts: **KEEP** (serves a slice step ~as-is) · **ADAPT** (use, but weave coding / change delivery) · **CUT** (not needed for *this* slice — defer to breadth or another slice) · **ADD** (gap the exemplar doesn't cover).

## By module

| Module | Verdict | Rationale / how it maps |
|---|---|---|
| Intro to Earth's Topography (Axial Caldera profile, max depth) | **ADAPT** | Step 1. Keep the concept + Axial deliverable, but *make the profile in Python/matplotlib* (woven), not a handout-only activity. |
| Rules for Contouring (Axial contour map) | **CUT** | Step 1 only needs locate + depth/profile; full contouring is breadth → defer (Advanced Mapping). |
| Latitude & Longitude (meters-per-degree at Axial) | **ADAPT** | Step 1. The meters-per-degree task is a great quick probe — deliver it as a tiny Python computation. |
| Advanced Mapping (ASHES profile) | **CUT** | Marked "coming soon"; breadth. Defer. |
| Seafloor Spreading (explain Axial's tectonic context) | **KEEP** | Step 2 (conceptual, Socratic). Light. |
| Plate Tectonics & Sea Floor (OOI Data Lab 3) | **KEEP** | Step 2. Link the interactive lab as-is. |
| Sea Floor Changes / volcanic setting (Lab 4 — bottom-pressure since 2015) | **ADAPT** | Step 4-adjacent. Strong deliverable; do it *with the data in pandas*, not just the Data Explorer GUI. |
| Eruption Impacts on Elevation (Nugget) | **CUT** | Overlaps Lab 4; defer to breadth. |
| Sound & Light in the Ocean | **CUT (this slice)** | Acoustics/optics → relevant to a *bravoseis/scaleworm* slice, not the thermal/tidal one. KEEP it for a future slice. |
| Collecting Oceanographic Data (OOI Data Lab 1 — instruments at ASHES) | **KEEP** | Steps 2–3. How OOI gathers the data; what's at ASHES. |
| Working with Oceanographic Data (OOI Data Lab 2 — reading graphs/maps) | **KEEP** | Step 3 bridge into the data + coding. |
| Life on a Hydrothermal Vent (Axial food web) | **CUT (this slice)** | Fauna/biology → the *scaleworm* slice. KEEP for that later. |
| **Tidal Fluctuation of Diffuse Vent Fluid Flow (Nugget — Mushroom Vent)** | **KEEP — this *is* step 4** | The capstone of the slice; the phenomenon we reveal in data. |
| Linux | **ADAPT** | Woven, just-in-time: only enough to run Jupyter/notebooks for steps 1/3 — not a standalone Linux course. |
| Python course (EdX/Rutgers, pandas/numpy) | **ADAPT → book** | Drop the time-limited EdX dependency; weave the equivalent via the book chapters just-in-time. |
| Python Notebooks from OOI | **KEEP** | Steps 3–4: working with OOI data in Python — the coding spine of the slice. |
| Ocean Waves (Data Lab 6) | **CUT** | Explicitly less-connected; not in slice. |

## ADD (gaps the exemplar doesn't cover, needed for v1)

- **Pre-staged sample dataset** for steps 3–4 — the exemplar assumes the live OOI Data Explorer/portal; the onramp needs a small bundled/stable dataset so it's reliable + offline on Sonnet.
- **Just-in-time coding weave** — the exemplar isolates Python as a final objective; v1 must attach a small coding exercise to each domain step (Constitution VII).
- **Agentic assessment layer** — hint ladders, rubric, scaffolding-depth→level. The exemplar has deliverables but no adaptive assess-and-personalize loop.
- **Tidal-signal coding exercise** — the Nugget shows the phenomenon; ADD the pandas resample/plot exercise that *produces* it.

## Net v1 content set

Steps map to: **(1)** Topography + Lat/Long, adapted to Python plotting of Axial bathymetry + meters-per-degree · **(2)** Seafloor Spreading + Data Lab 3 + Data Lab 1 (conceptual, link the interactive labs) · **(3)** Data Lab 2 + OOI Python Notebooks (pull/read the pre-staged Axial data) · **(4)** Tidal Diffuse-Flow Nugget + Data Lab 4 deliverable, done in pandas (reveal the tidal signal). Coding (Linux/Python/pandas/xarray/matplotlib) woven via the book, just-in-time. Sound&Light, Life-on-a-Vent, Contouring, Ocean Waves → deferred to breadth or sibling slices.
