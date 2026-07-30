*AI-generated draft (Claude, Anthropic) — for review.*

# JupyterLab survival card

Keep this open for Steps 1–4 — a handful of habits save most of the pain new notebook users hit.

| Need | Do this |
|---|---|
| Make a new notebook | In the JupyterLab **file browser**, first open your `student-onramp` folder, *then* New → Notebook — so the notebook lives **inside the repo** and relative paths like `data/…` just work |
| Pick the right kernel | Top-right kernel name → choose **`ooi`** (the base/Python-3 kernel lacks `xarray` and `netCDF4`, so `import xarray` fails there) |
| Run a cell | **Shift+Enter** (run + go to next) · **Ctrl+Enter** (run, stay) |
| Save | **Ctrl+S** (or Cmd+S) — notebooks don't autosave reliably |
| See a plot | put the figure-making code in **one cell**; a figure only renders in the cell that created it — if you add to `ax` later, re-display with `fig` on the last line |
| Cell stuck on `[*]` / kernel hung | don't wait — **Kernel → Restart Kernel**, then re-run your cells from the top |
| `No module named xarray` (or netCDF4) | wrong kernel — switch to **`ooi`** (see above) and re-run |
| `FileNotFoundError` on `data/…` | the notebook isn't in the repo folder — check with `import os; os.getcwd()`; move/remake the notebook inside `student-onramp` |

Rule of thumb: **repo-folder notebook + `ooi` kernel + Ctrl+S**, and when in doubt, restart the
kernel and run top-to-bottom.
