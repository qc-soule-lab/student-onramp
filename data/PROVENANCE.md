*AI-generated draft (Claude, Anthropic) — for review. All files below are produced deterministically by `scripts/stage_slice.py` from documented sources.*

# Staged data — provenance

Small Axial Seamount teaching slices for the v1 onramp. **Referenced, derived, and citable.**
Only these small derived files are committed; the full sources live with their providers
(OOI / GMRT / MGDS) or on the lab JupyterHub.

**OOI files (BOTPT, TMPSF):** NSF **Ocean Observatories Initiative (OOI)**, Regional Cabled
Array (RSN), Axial Seamount. OOI data are openly available for reuse with attribution. Cite as:
*Ocean Observatories Initiative (2015). Cabled Array, Axial Seamount. NSF OOI. Accessed 2026-06-09
on the qc-soule-lab JupyterHub (`/home/jovyan/ooi/kdata/`).*

Regenerate: `uv run --group staging python scripts/stage_slice.py [botpt tmpsf bathy boundary]`
(OOI sources need the Hub; `bathy` needs network; `boundary` needs the MGDS download on the Hub).
Integrity is pinned by `tests/test_data_integrity.py`.

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

## `axial_bathymetry_gmrt.nc` — Steps 0–2 (matplotlib, the map)

- **Source:** **GMRT synthesis** (Global Multi-Resolution Topography), GridServer API one-shot
  fetch, **GMRTv4_5_0** (version from the download filename, stamped in the file's
  `gmrt_version` attribute). Request: Axial box lon −130.5…−129.5, lat 45.7…46.2,
  `resolution=high`, `layer=topo` (exact URL in the file's `source` attribute). Fetched 2026-06-10.
- **License / citation:** GMRT grids are freely redistributable with citation. Cite:
  *Ryan, W.B.F., et al. (2009), Global Multi-Resolution Topography synthesis, Geochem. Geophys.
  Geosyst., 10, Q03014, doi:10.1029/2008GC002332* — plus the version string GMRTv4_5_0.
  (Ethical-check passed 2026-06-07, re-confirmed 2026-06-10.)
- **Processing:** GridServer's legacy GMT-grd layout decoded to a clean CF-style
  `elevation(lat, lon)` grid (m, negative = below sea level; lat/lon ascending); NaN box-edge
  rows trimmed; 2×2 mean-coarsened from ~42 m native to **~85 m** nodes (654×910, ~1.4 MB).
- **Verification:** orientation + values ground-truthed against GMRT PointServer 2026-06-10
  (caldera center 45.955°N/−130.009°W = −1531 m; staged grid reads −1529 m).

## `plate_boundary.csv` — Steps 0–2 (the vi/head target + map overlay)

- **Source:** Juan de Fuca plate-boundary shapefile, **Bobbitt / MGDS dataset 17123**, from the
  lab's documented download (`~/my_data/axial/axial_bathy/MGDS_Download/JdF_Bobbitt/`,
  retrieved 2026-05-21; see its `PROVENANCE.txt`). Converted shp → plain CSV
  (`lon,lat,segment_id`, WGS84 assumed per source docs) so students need **no geo deps**.
- **License — ⚠ this file is CC BY-NC-SA 3.0 US** (unlike the rest of the repo):
  attribution + noncommercial + **ShareAlike carries to this derived CSV**. Educational lab
  use is within the NC clause. License: <https://creativecommons.org/licenses/by-nc-sa/3.0/us/>
- **Citation (verbatim, required by MGDS terms):** *Bobbitt, A., Juan de Fuca plate boundary,
  Marine Geoscience Data System, dataset 17123, <https://www.marine-geo.org/tools/datasets/17123>.*
- **Processing caveat:** 29 of 30 source features carry a corrupt single-point "continuation
  marker" part that breaks naive shapefile readers (geopandas/pyogrio recover only 1 feature).
  The converter drops sub-2-point parts and recovers **all 30 segments (281 points; 4 segments
  cross the step-1 map box, incl. the caldera ring)**.
