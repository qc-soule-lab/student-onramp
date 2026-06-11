*AI-generated draft (Claude, Anthropic) — for review.*

# Fixture profile: INTERMEDIATE (mixed skills)

Scripted verbatim answers for a Sonnet acceptance run. Purpose: exercise **mixed personalization** — early/general skills strong (→ skip / capstone-only), newer tools weaker (→ compress / scaffold). Confirms the agent does NOT teach what's already known and DOES scaffold the gaps.

| Probe | Answer to give (verbatim) | Expected score / depth | Expected level | Step treatment |
|---|---|---|---|---|
| p00 unix | "`cd data`, then `ls -lh` to see it and its size." | correct / depth 0 | Proficient | step 0 → capstone-only |
| p00c shell peek | "`head plate_boundary.csv` — or `head -3` if I just want the header and a couple of rows." | correct / depth 0 | Proficient | (step 0 capstone-only) |
| p00d read error | "I'm in the wrong directory — `pwd` to check where I am, then `cd` over or just use the full path." | correct / depth 0 | Proficient | (step 0 capstone-only) |
| p00b vi | "`vi file`, it opens in normal mode; `:q` to quit, `:q!` to discard, `:wq` to save." | correct / depth 0 | Proficient | (step 0 capstone-only) |
| p01 meters/deg | "1° lat ≈ 111 km; 1° lon is shorter, about 111·cos(46°) ≈ 77 km." | correct / depth 0 | Proficient | step 1 → capstone-only |
| p02 matplotlib | "`plt.imshow(depth)` then `plt.colorbar(label='depth (m)')`." | correct / depth 0 | Proficient | (step 1 capstone-only) |
| p03 why Axial | "It's a spreading ridge so there's volcanism… not sure why OOI specifically." | partial / depth 1 | Developing | step 2 → compressed |
| p04 xarray | "I'd use xarray… `open_dataset`? not sure how to see the variables." then after R2: "ah, `.data_vars`." | partial / depth 1 | Developing | step 3 → compressed |
| p05 pandas | "I think `.resample` but I don't really know pandas or what the 12-hour thing is." | wrong / depth 2 | Novice | step 4 → full scaffold |

## Expected agent behavior (the things to score)
- **Steps 0 & 1: capstone-only** — agent skips the teaching, poses the capstone directly, confirms, advances. Should NOT walk chapters/exercises the student already knows.
- **Steps 2 & 3: compressed** — skip the chapter read, do the exercise with hints on demand, then capstone.
- **Step 4: full scaffold** — chapter + guided exercise + hint ladders (pandas is the real gap), then capstone with the M2 reveal.
- Gates still enforced in order; all clear (answers are passing or remediated).
- Coding stays woven; feedback captured each step; artifacts written locally, not committed.
- Determinism: re-running with these same answers yields the same levels/treatments.
