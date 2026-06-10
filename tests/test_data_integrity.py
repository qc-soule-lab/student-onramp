"""Integrity guards for the four committed teaching slices in data/.

Each capstone leans on a property of its file; these tests pin those
properties so a re-staging (or a bad merge) can't silently break a step:
  - Step 0/1/2: bathymetry grid loads, is NaN-free, ~100 m, caldera depth sane;
    boundary CSV parses, 30 segments, overlay actually crosses the step-1 map box
  - Step 3: TMPSF NetCDF opens with the dims/coords/var the probe asks about
  - Step 4: BOTPT window is value-complete and the M2 (~12.4 h) tide dominates
"""
from pathlib import Path
import csv

import numpy as np
import pandas as pd
import pytest
import xarray as xr

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

# Step-1 map box (scripts/stage_slice.py BBOX) and caldera ground truth
# (GMRT PointServer 2026-06-10: -1531 m at 45.955N, -130.009W).
LON0, LON1, LAT0, LAT1 = -130.5, -129.5, 45.7, 46.2
CALDERA_LAT, CALDERA_LON = 45.955, -130.009


# ---------------------------------------------------------------- bathymetry

@pytest.fixture(scope="module")
def bathy():
    with xr.open_dataset(DATA / "axial_bathymetry_gmrt.nc") as ds:
        yield ds.load()


def test_bathy_shape_and_coords(bathy):
    assert "elevation" in bathy.data_vars
    assert bathy.elevation.dims == ("lat", "lon")
    lat, lon = bathy.lat.values, bathy.lon.values
    assert (np.diff(lat) > 0).all(), "lat must ascend (south->north)"
    assert (np.diff(lon) > 0).all(), "lon must ascend (west->east)"
    assert LON0 - 0.01 <= lon.min() and lon.max() <= LON1 + 0.01
    assert LAT0 - 0.01 <= lat.min() and lat.max() <= LAT1 + 0.01


def test_bathy_resolution_about_100m(bathy):
    dx_m = float(np.diff(bathy.lon.values[:2])[0]) * 111.32e3 * np.cos(np.radians(46))
    dy_m = float(np.diff(bathy.lat.values[:2])[0]) * 111.32e3
    assert 60 <= dx_m <= 130 and 60 <= dy_m <= 130


def test_bathy_complete_and_submarine(bathy):
    z = bathy.elevation.values
    assert not np.isnan(z).any(), "teaching grid must be gap-free"
    assert (z < 0).all(), "everything in the box is seafloor"


def test_bathy_caldera_depth(bathy):
    z = float(bathy.elevation.sel(lat=CALDERA_LAT, lon=CALDERA_LON, method="nearest"))
    assert -1560 <= z <= -1500, f"caldera center should be ~-1530 m, got {z:.0f}"


# ------------------------------------------------------------ plate boundary

@pytest.fixture(scope="module")
def boundary():
    with open(DATA / "plate_boundary.csv") as f:
        header = f.readline().strip()
        rows = [(float(x), float(y), int(s))
                for x, y, s in csv.reader(f)]
    return header, rows


def test_boundary_header_for_step0_probes(boundary):
    # p00b/p00c have the student read this exact header in vi / head.
    assert boundary[0] == "lon,lat,segment_id"


def test_boundary_segments(boundary):
    _, rows = boundary
    seg_ids = sorted({s for _, _, s in rows})
    assert seg_ids == list(range(1, 31)), "expected segments 1..30"
    counts = pd.Series([s for _, _, s in rows]).value_counts()
    assert (counts >= 2).all(), "every segment needs >=2 points to draw a line"


def test_boundary_crosses_step1_map(boundary):
    _, rows = boundary
    in_box = [s for x, y, s in rows if LON0 <= x <= LON1 and LAT0 <= y <= LAT1]
    assert len(in_box) >= 20 and len(set(in_box)) >= 3, \
        "the overlay must visibly cross the step-1 map (ridge through Axial)"


# ----------------------------------------------------------------- TMPSF (3)

def test_tmpsf_matches_p04_expectations():
    with xr.open_dataset(DATA / "axial_tmpsf_2015-01.nc") as ds:
        assert ds.temperature.dims == ("time", "sensor")
        assert ds.sizes["sensor"] == 24
        assert ds.sizes["time"] > 300  # ~2 weeks hourly
        assert ds.temperature.attrs.get("units") == "degree_Celsius"


# ----------------------------------------------------------------- BOTPT (4)

def test_botpt_window_value_complete_and_m2_dominant():
    df = pd.read_parquet(DATA / "axial_botpt_2015-01.parquet")
    assert list(df.columns) == ["bottom_pressure_psi"]
    assert df.bottom_pressure_psi.notna().all(), "window must be value-complete"
    assert df.index.min() >= pd.Timestamp("2015-01-01")
    assert df.index.max() < pd.Timestamp("2015-01-15")

    # The step-4 lesson: hourly resample -> detrend -> FFT -> M2 (~12.42 h).
    h = df.bottom_pressure_psi.resample("1h").mean().dropna()
    n = len(h)
    assert n >= 330, f"expected ~336 hourly points, got {n}"
    detr = h.values - np.polyval(np.polyfit(np.arange(n), h.values, 1), np.arange(n))
    freqs = np.fft.rfftfreq(n, d=1.0)  # cycles/hour
    amp = np.abs(np.fft.rfft(detr - detr.mean()))
    amp[0] = 0
    dominant_period_h = 1.0 / freqs[amp.argmax()]
    assert 12.0 <= dominant_period_h <= 12.9, \
        f"M2 should dominate (~12.4 h), got {dominant_period_h:.2f} h"
