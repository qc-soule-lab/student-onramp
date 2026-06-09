*AI-generated draft (Claude, Anthropic) — for review.*

# Probe p04 — open and inspect a dataset  (coding · step 3 · skill: xarray_intro)

## Prompt (show to student)
You have a NetCDF file `data/axial_tmpsf_2015-01.nc` (the Axial TMPSF thermistor array). Using **xarray**, how do you open it and find out what **variables, dimensions, and coordinates** it contains?

## Answer key
```python
import xarray as xr
ds = xr.open_dataset("data/axial_tmpsf_2015-01.nc")
ds                       # rich repr shows dims, coords, data_vars at a glance
ds.dims, ds.coords, ds.data_vars   # dims: time (359), sensor (24); var: temperature
da = ds["temperature"]   # index by name to pull one variable as a DataArray
```
Key idea: `open_dataset` returns a labeled `Dataset`; displaying it (or `.dims/.coords/.data_vars`) reveals structure; index with `ds["name"]` to select.

## Hint ladder
- **R1:** Which library opens NetCDF and gives you *labeled* dimensions? What's the function to open a dataset?
- **R2:** `xr.open_dataset(path)` → a Dataset. Just display it (or use `.dims`, `.coords`, `.data_vars`); grab a variable with `ds['varname']`.
- **R3 (reveal):** the snippet above.

## Scoring (→ rubric §3)
- `correct`: `open_dataset` **and** inspects dims/coords/variables (and/or selects one).
- `partial`: opens the file but unsure how to inspect or select.
- `wrong`: can't open/inspect.
