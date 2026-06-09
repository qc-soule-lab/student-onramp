# Research — Phase 0 decisions for the v1 slice plan

*AI-generated draft (Claude, Anthropic) — for review. All parameters and figures are derived from version-controlled scripts and data.*

**Created**: 2026-06-07 · companion to `plan.md`

## Bathymetry source for step 1

**Decision**: GMRT synthesis subset via the GridServer API (Axial region, ~100 m resolution, NetCDF, ~2–5 MB), fetched once by `stage_data.py` and committed.
**Rationale**: GMRT is built for programmatic access and free redistribution with citation (Ryan et al. 2009, G³, doi:10.1029/2008GC002332 + GMRT version string). Small enough to commit; offline at student runtime; ethical-check passed 2026-06-07.
**Alternatives considered**: (a) local MBARI AUV/ship grids (96–603 MB) — far too large to commit, higher-than-needed resolution, and redistribution terms for the local copies are undocumented; flagged as an optional Phase-2 enhancement *after* a license check. (b) GEBCO global subset — coarser than GMRT at Axial, no advantage.

## Tidal dataset + window for steps 3–4

**Decision**: 2015-01-17 → 2015-01-31 hourly window (336 rows) of `axial_mj03f_bpH.csv` (OOI RCA BOTPT, MJ03F), committed as CSV.
**Rationale**: verified 2026-06-05 — window is value-complete (0 NaN), 4.69 m peak-to-peak, FFT of the detrended window shows textbook spectrum (M2 12.48 h rel-amp 1.00; diurnal 24.07 h 0.51; S2 12.04 h 0.29). OOI data is open with acknowledgment.
**Alternatives considered**: (a) Jan 1–15 windows — contain 22 NaN values around Jan 15–16 (row-complete but NOT value-complete; the gotcha is asserted in `test_data_integrity.py`). (b) vent **temperature** data — REJECTED by PI decision 2026-06-05: local tmpsf/miso products are daily-mean/de-tided (Nyquist — cannot resolve a 12.4 h signal). Step 4 closes with the bridge: tidal loading also modulates diffuse vent flow.

## Plate-boundary overlay (steps 1–2)

**Decision**: convert the MGDS Bobbitt shapefile (dataset 17123, CC BY-NC-SA 3.0, provenance already on file) to a plain `plate_boundary.csv` (lon, lat, segment_id) during staging.
**Rationale**: keeps the student environment free of geo dependencies (no geopandas/shapely/cartopy install friction on the Hub); a CSV plotted with matplotlib is exactly the woven-coding level step 1 targets. ShareAlike + verbatim citation preserved in `data/PROVENANCE.md`.
**Alternatives considered**: shipping the shapefile + geopandas — heavier env, more failure modes, no pedagogical gain for this slice (cartopy is already a flagged BONUS via the book's mapping chapter).

## Sonnet acceptance method

**Decision**: live protocol runs, not scripted automation. `sonnet_acceptance_protocol.md` defines: launch on `claude-sonnet-4-6`, answer assessment from a fixture profile script verbatim, traverse all 4 steps, score against a checklist (correct leveling per rubric, hint-ladders followed not improvised, every coding moment attached to a domain step, artifacts generated + gitignored). Two passes: `profile_novice`, `profile_intermediate`.
**Rationale**: the runtime is an interactive Socratic conversation — scripting it end-to-end (e.g., `claude -p` pipelines) would test a caricature of the flow. Fixture-scripted *human-in-the-loop* runs are reproducible enough (same answers, same rubric) and verify the thing that matters: Sonnet following structure.
**Alternatives considered**: automated transcript replay — brittle, defers the hard part; partial automation may arrive in Phase 2 once the procedure is stable.

## Probe sourcing

**Decision**: adapt from the book's `assignments/` (CC BY-SA, attributed) + the exemplar roadmap's meters-per-degree exercise + two bespoke probes (bathymetry plot read-back; BOTPT resample/period read-off).
**Rationale**: reuses vetted exercises where they exist (resource-evaluation KEEP/ADAPT verdicts); bespoke only where the slice's woven moments have no book equivalent.
