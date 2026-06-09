*AI-generated draft (Claude, Anthropic) — for review.*

# Probe p00 — reach the data  (coding · step 0 · skills: unix_basics)

## Prompt (show to student)
The staged bathymetry grid lives in `~/data/`. From the JupyterLab **terminal**, show the
commands you'd use to: (1) move into that directory, (2) confirm the file
`axial_bathymetry_gmrt.nc` is there, and (3) see how big it is.

## Answer key
```bash
cd ~/data            # move into the data directory
ls -lh               # list contents with human-readable sizes (or: ls -lh axial_bathymetry_gmrt.nc)
pwd                  # (optional) confirm where you are
```
Key idea: `cd` changes directory, `ls` lists what's there, and `-lh` shows human-readable
file sizes — the shell is how you find and inspect the data before any code touches it.

## Hint ladder
- **R1:** Which command moves you into a directory? Which one lists what's inside it?
- **R2:** `cd ~/data` moves in; `ls` lists files; add `-lh` (`ls -lh`) to see sizes in KB/MB.
- **R3 (reveal):** the snippet above.

## Scoring (→ rubric §3)
- `correct`: navigates (`cd`) **and** lists (`ls`) **and** reads the size (`-lh`/`du`).
- `partial`: navigates and lists but can't confirm the size, or lists without `cd`.
- `wrong`: can't reach or list the directory.
