"""Stage the small Axial time-series slices the v1 onramp capstones use.

Maintainer script (NOT run by students): reads the lab's OOI sources, cuts a
~2-week Jan-2015 window, and writes two small, in-repo teaching files:

  data/axial_botpt_2015-01.parquet  — Step 4 (pandas): observed BOTPT bottom
      pressure at MJ03F. Uses OOI's `botsflu_meanpres` (the OBSERVED mean
      seafloor pressure, which RETAINS the tide) — NOT `botsflu_meandepth`,
      which is OOI's de-tided seafloor-uplift product (tide filtered out).
  data/axial_tmpsf_2015-01.nc       — Step 3 (xarray): TMPSF thermistor array,
      temperature(time, sensor) — a real gridded dataset to inspect.

Sources live only on the JupyterHub (OOI kdata + lab parquet caches); students
get the small derived slices committed here. See data/PROVENANCE.md.
"""
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


if __name__ == "__main__":
    stage_botpt()
    stage_tmpsf()
