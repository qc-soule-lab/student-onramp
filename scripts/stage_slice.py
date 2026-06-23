"""Stage the small Axial data slices the v1 onramp capstones use.

Maintainer script (NOT run by students): reads the lab's sources, cuts small
teaching slices, and writes them into the repo:

  data/axial_botpt_2015-01.parquet  — Step 4 (pandas): observed BOTPT bottom
      pressure at MJ03F. Uses OOI's `botsflu_meanpres` (the OBSERVED mean
      seafloor pressure, which RETAINS the tide) — NOT `botsflu_meandepth`,
      which is OOI's de-tided seafloor-uplift product (tide filtered out).
  data/axial_tmpsf_2015-01.nc       — Step 3 (xarray): TMPSF thermistor array,
      temperature(time, sensor) — a real gridded dataset to inspect.
  data/axial_bathymetry_gmrt.nc     — Steps 0–2 (matplotlib): GMRT bathymetry
      subset around Axial, decoded from the GridServer's legacy GMT-grd layout
      into a clean elevation(lat, lon) grid. Needs network (one-shot fetch).
  data/plate_boundary.csv           — Steps 0–2: Bobbitt/MGDS Juan de Fuca
      plate boundary as plain lon,lat,segment_id (no geo deps for students).
      Needs `uv run --group staging` (pyshp).

OOI sources live only on the JupyterHub (kdata + lab parquet caches); students
get the small derived slices committed here. See data/PROVENANCE.md.

Usage: python scripts/stage_slice.py [botpt tmpsf bathy boundary]  (default: all)
"""
import sys
from pathlib import Path
import numpy as np
import pandas as pd
import xarray as xr

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data"
OUT.mkdir(exist_ok=True)

# Gap-free 2-week window (avoids the 2015-01-15/16 BOTPT data gap).
START, END = "2015-01-01", "2015-01-15"   # [START, END)

BOTPT_NC = ("/home/jovyan/ooi/kdata/RS03CCAL-MJ03F-05-BOTPTA301-streamed-"
            "botpt_nano_sample_15sec/deployment0001_RS03CCAL-MJ03F-05-BOTPTA301-"
            "streamed-botpt_nano_sample_15sec_20140829T205945-20200830T235945.nc")
TMPSF_PARQUET = ("/home/jovyan/repos/specKitScience/my-analysis_tmpsf/"
                 "outputs/data/tmpsf_2015-2026_hourly.parquet")

# Step 0–2 map box: caldera + both rift zones + ridge context (research.md).
BBOX = {"minlongitude": -130.5, "maxlongitude": -129.5,
        "minlatitude": 45.7, "maxlatitude": 46.2}
GMRT_URL = ("https://www.gmrt.org/services/GridServer?"
            + "&".join(f"{k}={v}" for k, v in BBOX.items())
            + "&format=netcdf&resolution=high&layer=topo")
BOBBITT_SHP = ("/home/jovyan/my_data/axial/axial_bathy/MGDS_Download/"
               "JdF_Bobbitt/JdF_plate_boundary.shp")
# Caldera center ground truth (GMRT PointServer, 2026-06-10): -1531 m.
CALDERA = (45.955, -130.009)


def stage_botpt():
    ds = xr.open_dataset(BOTPT_NC, decode_timedelta=True)
    t = ds["time"].values
    i0 = int(np.searchsorted(t, np.datetime64(f"{START}T00:00:00")))
    i1 = int(np.searchsorted(t, np.datetime64(f"{END}T00:00:00")))
    sub = ds.isel(obs=slice(i0, i1))
    s = pd.Series(sub["botsflu_meanpres"].values,
                  index=pd.to_datetime(sub["time"].values), name="bottom_pressure_psi")
    ds.close()
    # 15-s firehose -> 1-minute means: small file, but students still must
    # resample to hourly to reveal the tide (the Step-4 lesson).
    s = s.resample("1min").mean().dropna()
    s.index.name = "time"
    df = s.to_frame()
    p = OUT / "axial_botpt_2015-01.parquet"
    df.to_parquet(p)
    # diagnostics
    h = s.resample("1h").mean().dropna()
    n = len(h); det = h.values - np.polyval(np.polyfit(np.arange(n), h.values, 1), np.arange(n))
    fr = np.fft.rfftfreq(n, 1.0); amp = np.abs(np.fft.rfft(det - det.mean())); amp[0] = 0
    print(f"[BOTPT] {p.name}: {len(df)} rows @1min, {df.isna().sum().item()} NaN, "
          f"p2p={s.max()-s.min():.3f} psi, dom_period={1/fr[amp.argmax()]:.2f} h, "
          f"{p.stat().st_size/1024:.0f} KB")


def stage_tmpsf():
    df = pd.read_parquet(TMPSF_PARQUET).loc[START:END].iloc[:-1]  # [START, END)
    cols = sorted(c for c in df.columns if c.startswith("temperature"))
    arr = df[cols].to_numpy(dtype="float32")
    da = xr.DataArray(
        arr, dims=("time", "sensor"),
        coords={"time": df.index.values, "sensor": np.arange(1, len(cols) + 1)},
        name="temperature",
        attrs={"units": "degree_Celsius",
               "long_name": "TMPSF thermistor temperature",
               "description": "OOI RS03ASHS TMPSF array (24 thermistors), hourly QC-filtered"},
    )
    ds = da.to_dataset()
    ds["sensor"].attrs["long_name"] = "thermistor channel (1-24)"
    ds.attrs["title"] = "Axial Seamount TMPSF thermistor array — Jan 2015 teaching slice"
    p = OUT / "axial_tmpsf_2015-01.nc"
    ds.to_netcdf(p)
    print(f"[TMPSF] {p.name}: dims={dict(ds.sizes)}, "
          f"vars={list(ds.data_vars)}, {p.stat().st_size/1024:.0f} KB")


def stage_bathy():
    import tempfile
    import urllib.request

    # One-shot fetch. GridServer returns legacy GMT-v2 grd NetCDF (flat z +
    # x_range/y_range/spacing/dimension sidecars); the synthesis version is
    # only exposed in the download filename (Content-Disposition).
    with urllib.request.urlopen(GMRT_URL, timeout=300) as resp:
        disp = resp.headers.get("Content-Disposition", "")
        raw = resp.read()
    version = "unknown"
    if "filename=GMRT" in disp:
        version = disp.split("filename=")[1].split("topo")[0].rstrip("_")
    with tempfile.NamedTemporaryFile(suffix=".grd") as tmp:
        tmp.write(raw)
        tmp.flush()
        grd = xr.open_dataset(tmp.name)
        nx, ny = (int(v) for v in grd["dimension"].values)
        x0, x1 = grd["x_range"].values
        y0, y1 = grd["y_range"].values
        # grd z is row-major from the NW corner (top row = max lat) — verified
        # against GMRT PointServer 2026-06-10 (NW blob -869 m, SW -2576 m).
        z = grd["z"].values.reshape(ny, nx)
        grd.close()

    lon = np.linspace(x0, x1, nx)
    lat = np.linspace(y1, y0, ny)
    da = xr.DataArray(z[::-1].astype("float32"), dims=("lat", "lon"),
                      coords={"lat": lat[::-1], "lon": lon}, name="elevation")
    # The GridServer cut leaves a couple of NaN rows on the box edge (observed:
    # bottom 2 rows, 2026-06-10) — trim NaN edges; interior must stay complete.
    while np.isnan(da.values[0]).any():
        da = da.isel(lat=slice(1, None))
    while np.isnan(da.values[-1]).any():
        da = da.isel(lat=slice(None, -1))
    while np.isnan(da.values[:, 0]).any():
        da = da.isel(lon=slice(1, None))
    while np.isnan(da.values[:, -1]).any():
        da = da.isel(lon=slice(None, -1))
    # ~42 m native -> ~85 m teaching grid (research.md target ~100 m, 2-5 MB).
    da = da.coarsen(lat=2, lon=2, boundary="trim").mean()

    assert not np.isnan(da.values).any(), "GMRT subset contains NaN"
    caldera = float(da.sel(lat=CALDERA[0], lon=CALDERA[1], method="nearest"))
    assert -1560 <= caldera <= -1500, f"caldera depth off: {caldera:.0f} m"

    da.attrs.update(units="m", positive="up",
                    long_name="seafloor elevation (negative = below sea level)")
    da["lat"].attrs.update(units="degrees_north", long_name="latitude")
    da["lon"].attrs.update(units="degrees_east", long_name="longitude")
    ds = da.to_dataset()
    ds.attrs.update(
        title="Axial Seamount bathymetry — GMRT synthesis teaching subset",
        source=GMRT_URL, gmrt_version=version,
        references=("Ryan, W.B.F., et al. (2009), Global Multi-Resolution "
                    "Topography synthesis, Geochem. Geophys. Geosyst., 10, "
                    "Q03014, doi:10.1029/2008GC002332"),
        history="fetched + decoded + 2x2 mean-coarsened by scripts/stage_slice.py",
    )
    p = OUT / "axial_bathymetry_gmrt.nc"
    ds.to_netcdf(p, encoding={"elevation": {"zlib": True, "complevel": 4}})
    dx_m = float(np.diff(ds["lon"][:2])[0]) * 111.32e3 * np.cos(np.radians(46))
    print(f"[BATHY] {p.name}: {version}, {dict(ds.sizes)}, ~{dx_m:.0f} m nodes, "
          f"caldera={caldera:.0f} m, z=[{float(da.min()):.0f},{float(da.max()):.0f}], "
          f"{p.stat().st_size/1024:.0f} KB")


def stage_boundary():
    import shapefile  # pyshp — staging dep only

    r = shapefile.Reader(BOBBITT_SHP)
    rows, seg_id = [], 0
    for shp in r.shapes():
        offsets = list(shp.parts) + [len(shp.points)]
        for k in range(len(shp.parts)):
            pts = shp.points[offsets[k]:offsets[k + 1]]
            # 29/30 features carry a corrupt single-point "continuation marker"
            # part — drop sub-2-point parts (see data/PROVENANCE.md caveat).
            if len(pts) < 2:
                continue
            seg_id += 1
            rows.extend((x, y, seg_id) for x, y in pts)

    assert seg_id == 30, f"expected 30 boundary segments, got {seg_id}"
    lons, lats = [r_[0] for r_ in rows], [r_[1] for r_ in rows]
    assert -137 < min(lons) and max(lons) < -124 and 40 < min(lats) and max(lats) < 58
    in_map = sum(1 for x, y, _ in rows
                 if BBOX["minlongitude"] <= x <= BBOX["maxlongitude"]
                 and BBOX["minlatitude"] <= y <= BBOX["maxlatitude"])
    assert in_map >= 20, f"only {in_map} boundary points fall in the step-1 map box"

    p = OUT / "plate_boundary.csv"
    with open(p, "w") as f:
        f.write("lon,lat,segment_id\n")
        f.writelines(f"{x:.5f},{y:.5f},{s}\n" for x, y, s in rows)
    print(f"[BOUNDARY] {p.name}: {seg_id} segments, {len(rows)} points "
          f"({in_map} in the step-1 map box), {p.stat().st_size/1024:.0f} KB")


STAGES = {"botpt": stage_botpt, "tmpsf": stage_tmpsf,
          "bathy": stage_bathy, "boundary": stage_boundary}

if __name__ == "__main__":
    names = sys.argv[1:] or list(STAGES)
    for name in names:
        STAGES[name]()
