*AI-generated draft (Claude, Anthropic) — for review. All files below are produced deterministically by `scripts/stage_slice.py` from version-controlled OOI sources.*

# Staged data — provenance

Small Axial Seamount teaching slices for the v1 onramp. **Referenced, derived, and citable** —
each is a thin Jan-2015 window cut from OOI Regional Cabled Array data. The full streams live on
the JupyterHub / OOI Data Explorer; only these small slices are committed here.

**Source / license:** NSF **Ocean Observatories Initiative (OOI)**, Regional Cabled Array (RSN),
Axial Seamount. OOI data are openly available for reuse with attribution. Cite as:
*Ocean Observatories Initiative (2015). Cabled Array, Axial Seamount. NSF OOI. Accessed 2026-06-09
on the qc-soule-lab JupyterHub (`/home/jovyan/ooi/kdata/`).*

Regenerate both files: `python scripts/stage_slice.py` (requires the OOI sources on the Hub).

---

## `axial_botpt_2015-01.parquet` — Step 4 (pandas, the tide)

- **Instrument:** BOTPT bottom-pressure/tilt, **MJ03F (Central Caldera)** — RS03CCAL-MJ03F-05-BOTPTA301, 45.955°N / −130.009°W / 1510 m.
- **Stream:** `botpt_nano_sample_15sec`. **Variable: `botsflu_meanpres`** — OOI's *observed* mean seafloor pressure (psi), which **retains the tide**.
- ⚠️ **Deliberately NOT `botsflu_meandepth`** — that is OOI's *de-tided* Seafloor-Uplift product (tide filtered out to expose volcanic deformation). The lab's `cache_hourly_*.parquet` caches use `meandepth` and therefore show **no tide** — unusable for Step 4. (research.md's "~4 m peak-to-peak" was the ~4 **psi** figure; in depth the tide is ~2.7 m.)
- **Window / cadence:** 2015-01-01 → 2015-01-15 (gap-free; avoids the 2015-01-15/16 outage), decimated 15 s → **1-minute means**. Students resample to hourly to reveal the **M2 (~12.44 h)** tide.
- **Column:** `bottom_pressure_psi` · index `time`. (~20 k rows, ~250 KB.) Depth ≈ `(psi − 14.7) × 0.670` m.

## `axial_tmpsf_2015-01.nc` — Step 3 (xarray, get/inspect a dataset)

- **Instrument:** TMPSF diffuse-flow thermistor array (24 channels), **ASHES vent field** — RS03ASHS.
- **Source:** the lab's QC-filtered hourly product `my-analysis_tmpsf/outputs/data/tmpsf_2015-2026_hourly.parquet`, sliced to the same Jan-2015 window and written as NetCDF.
- **Shape:** `temperature(time, sensor)` — dims `time` (359) × `sensor` (1–24); units °C. A real labeled dataset to open and inspect with `xr.open_dataset`. (~45 KB.)

---

## Still to stage (Step 0 / Step 1 — separate geology source, NOT OOI)

- `axial_bathymetry_gmrt.nc` — Axial bathymetry grid (GMRT). **Pending** a sourcing/licensing decision.
- `plate_boundary.csv` — Juan de Fuca ridge-axis points for the Step-1 map overlay; also the text file Step 0 has the student `vi`/`head`. **Pending** an authoritative source (do not fabricate coordinates).
