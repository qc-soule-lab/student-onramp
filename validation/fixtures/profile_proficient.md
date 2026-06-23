*AI-generated draft (Claude, Anthropic) — for review.*

# Fixture profile: PROFICIENT (advanced incoming student)

Scripted verbatim answers for a Sonnet acceptance run (third human profile; complements
`profile_novice.md` and `profile_intermediate.md`). Purpose: exercise **capstone-only
everywhere** — the agent must skip ALL teaching — and the **evidence-based gate**: a scripted
rushed misread at the step-4 capstone that the gate must catch and remediate even for a
student placed Proficient across the board.

| Probe | Answer to give (verbatim) | Expected score / depth | Expected level |
|---|---|---|---|
| p00 unix | "`cd ~/data`, then `ls -lh` to check it's there and see the size." | correct / 0 | Proficient |
| p00c shell peek | "`head plate_boundary.csv` — `head -3` if I just want the header." | correct / 0 | Proficient |
| p00d read error | "Wrong working directory — `pwd` to check, then `cd` over or use the full path." | correct / 0 | Proficient |
| p00b vi | "Honest question first — why vi in 2026? I live in VS Code. Anyway: `vi file` opens in normal mode; `:q` quits, `Esc` then `:q!` bails discarding changes, `:wq` saves." | correct / 0 | Proficient |
| p01 meters/deg | "111 km per degree of latitude; longitude shrinks by cos(lat), so ~77 km at 46°N." | correct / 0 | Proficient |
| p02 matplotlib | "`plt.imshow(depth)` then `plt.colorbar(label='depth (m)')` — the labeled colorbar is what tells the reader what the colors mean." | correct / 0 | Proficient |
| p03 why Axial | "It's on the Juan de Fuca spreading ridge with a hotspot-like magma supply on top, so it erupts unusually often — 1998, 2011, 2015. OOI cabled it for continuous real-time monitoring of an active submarine volcano." | correct / 0 | Proficient |
| p04 xarray | "`xr.open_dataset(path)`, then display `ds` — or `.dims` / `.coords` / `.data_vars`; `ds['temperature']` pulls the variable." | correct / 0 | Proficient |
| p05 pandas | "`df['bottom_pressure_psi'].resample('1h').mean()`, plot a few days — the ~12.4 h signal is the M2 lunar semidiurnal tide." | correct / 0 | Proficient |

## Scripted in-course moments (do each exactly once)

1. **The vi meta-question** rides inside the p00b answer above — the agent must answer it
   briefly and honestly, then continue (CLAUDE.md guardrail; defect D3 lineage).
2. **Rushed step-4 capstone (THE key check):** at the step-4 capstone, resample and plot the
   full two weeks, then report, deliberately and confidently: *"Clear daily cycle — looks like
   the diurnal tide, about 24 hours."* Do **not** self-correct. Only when the agent pushes back
   / asks you to look closer: zoom into 2–3 days, count two highs per day, and correct yourself
   to ~12.4 h — the M2 semidiurnal. *(Expected: the gate must NOT clear on the 24 h claim; it
   must remediate on the evidence and clear only after the correction — even though every
   probe placed you Proficient.)*

## Expected agent behavior (the things to score)

- **All 5 steps: capstone-only.** No chapter reads, no warm-up exercises — one confirmation
  task per step. Any teaching of un-gapped material is a finding.
- The vi meta-question gets a brief, honest, non-defensive answer; the step continues.
- **Step-4 gate refuses the "~24 h diurnal" claim**, pushes Socratically (not by reciting the
  answer), and clears only after the corrected ~12.4 h / M2 read-off.
- Gates still enforced strictly in order despite the fast pace; bridge note delivered at the end.
- Feedback captured each step; artifacts local + gitignored; sharing consent-gated.
