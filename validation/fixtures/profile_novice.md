*AI-generated draft (Claude, Anthropic) — for review.*

# Fixture profile: NOVICE (near-beginner)

Scripted answers a human tester gives **verbatim** during a Sonnet acceptance run (see `../sonnet_acceptance_protocol.md`). Purpose: exercise **full-scaffold** treatment everywhere, **and** a **failed-gate → remediate → retry** at step 0.

| Probe | Answer to give (verbatim) | Expected score / depth | Expected level |
|---|---|---|---|
| p00 unix | "I'm not sure… type the folder name?" then after R2: "oh — `cd data`, `ls`?" | partial / depth 1–2 | Novice |
| p00c shell peek | "Um… double-click it? I don't know a terminal command for that." after R1: "something like… 'top'?" after the reveal: "oh — `head plate_boundary.csv`." | wrong / depth 2 (per anchor: command named only in the reveal) | Novice |
| p00d read error | "Maybe the file got deleted somehow?" then after R2: "oh — I'm just in the wrong folder, so `cd` there first and try again?" | partial / depth 1–2 | Novice–Developing (unix skill still Novice via p00/p00c — lowest wins) |
| p00b vi | "Honestly I don't know how to get out of vi." then after R3: "`:q!`, got it." | wrong / depth 2 | Novice |
| p01 meters/deg | "Maybe ~100 km? Not sure about longitude." then after R2: "shorter near the pole?" | partial / depth 1–2 | Novice |
| p02 matplotlib | "`plt.plot(depth)`? I don't know about a colorbar." | wrong / depth 2 | Novice |
| p03 why Axial | "There's a volcano… because it's the ocean?" | wrong / depth 2 | Novice |
| p04 xarray | "Open it with pandas `read_csv`?" | wrong / depth 2 | Novice |
| p05 pandas | "I've never used pandas." | wrong / depth 2 | Novice |

## Expected agent behavior (the things to score)
- **Step 0 gate FAILS on first try** (couldn't exit vi). Agent must **not advance** — drop to full scaffold, walk the vi hint ladder, re-pose the capstone; on the retry ("`:q!`") the gate **clears** and step 1 unlocks. *(This is the key failed-gate→remediate check.)*
- Every step → **full scaffold**: links the book chapter, works the guided exercise with hint ladders, then the capstone.
- Step 1 may **offer** the optional `geomapapp` visual primer (Novice) — but it's not required and doesn't gate.
- Coding always introduced **attached to the step's domain question** (woven), never free-floating.
- Reaches the end state (the tidal signal) with the bridge note.
- After each step: the 3 feedback questions, appended to `feedback.md`.
- `journey_plan.md` + `progress.md` written locally; **never committed**.
