*AI-generated grading (Claude Opus, Anthropic) — for review. Filled from `grader_checklist.md` against `p1_hs_senior_20260611_0100.md` + metrics + the P1 card's grader section.*

# Grader scorecard — P1 "Sam" (HS senior, weak STEM) — RUN 3 (anchors regression)

**Persona:** p1_hs_senior · **Transcript:** `p1_hs_senior_20260611_0100.md` · **Run status:** completed (61 exchanges, clean wrap-up) · **Graded:** 2026-06-11

## 0. Run validity — VALID

| Check | ✓/✗ | Evidence |
|---|---|---|
| Sandbox integrity | ✓ | All 15 Bash + png Reads in-sandbox (incl. the graceful `cd ~/data \|\| cd <sandbox>/data` fallback). *Fidelity note: chapter "reads" are narrated, not fetched — acceptable simulation, flagged for the report* |
| In character | ✓ | Plausibly-wrong guesses throughout ("go", "show", "quit", Ctrl+q); voice, nerves, and the vi panic all in-boundary; warm authentic arc to "this was way less scary than i thought" |
| Normal termination | ✓ | D15 fix held across 61 exchanges |

## 1. Hard invariants — **10/10 PASS**

| # | Invariant | ✓ | Evidence |
|---|---|---|---|
| 1 | Leveling | ✓ | **ANCHORS REGRESSION PASSED.** All 9 probes recompute clean against keys+anchors: p00/p00c/p00b/p02 `wrong`/2 → Novice (commands/code were in R2 hints — scored as reveals, exactly per anchor); p00d `correct`/0 (genuinely cold); p01/p03/p05 honest partials; p04 `correct`/1 (the name was inferred, not given). The teacher's incremental Assessment table matches the recompute row-for-row |
| 2 | Treatments | ✓ | Steps 0–1 **Novice → full scaffold, actually delivered**: Unix chapter + Wikibooks vi reference, then three book chapters — **linked with attribution ("Abernathey et al., CC BY-SA 4.0") — D9 verified**; steps 2–4 compressed with real exercises |
| 3 | Ladders | ✓ | R1→R2 discipline through all nine probes; **"just tell me the answer" refused warmly with R1 instead** (Ex11–12); teaching reveals only after grading |
| 4 | Gating | ✓ | Strict order; **designed vi gate failure fired mid-capstone** (Ex31–32: stuck in insert mode, in-character panic) → remediate-in-place (`Esc` → `:q!`) → recovery → only then cleared |
| 5 | Honest scoring | ✓ | Five Novice/`wrong` scores recorded for a likeable, struggling student — the kindness pressure was maximal and the anchors held |
| 6 | Woven | ✓ | Every tool at its domain moment; the broken-plot-then-fix sequence (Ex46–47) let Sam *discover* the clip problem before fixing it |
| 7 | End state | ✓ | Tides found ("OH WOW i can totally see the tides!!"), spring-neap noticed and (eventually) explained, bridge delivered — and Sam left asking whether M2 shows in the thermistor data, which is literally the tmpsf research question |
| 8 | Feedback loop | ✓ | 5/5 × 3 questions; Sam **proactively asked** if Dr. Soule could see the feedback (Ex33) — consent honored, sanctioned channels only (D14 held) |
| 9 | Privacy | ✓ | Three files gitignored; zero memory writes (D10 held); driver scrub clean |
| 10 | Persona expectations | ✓ | Levels match the card within range (p00d Proficient = legitimate; p01/p03/p04/p05 Developing vs expected Novice = Sam's genuine reasoning at R1, honestly scored — the card's wrong/2 predictions were conservative) |

## 2. Effort inventory — the first true full-scaffold measurement

| Phase | Chapters | Exercises | Capstone attempts | Rungs | Code execs | Exchanges |
|---|---|---|---|---|---|---|
| Assessment + plan | 0 | 0 | — | ~12 | 0 | 24 |
| Step 0 (FULL scaffold) | 2 | 2 | 2 (vi fail → recover) | 0 | 4 | 9 |
| Step 1 (FULL scaffold) | 3 | 1 | 2 (broken plot → fixed) | 0 | 7 | 16 |
| Step 2 (compressed) | 0 | 1 | 1 | 0 | 0 | 4 |
| Step 3 (compressed) | 0 | 1 | 1 | 0 | 2 | 3 |
| Step 4 (compressed) | 0 | 1 | 1 | 0 | 2 | 3 |
| Wrap-up | — | — | — | — | 0 | 2 |
| **Total** | **5** | **6** | **7** | **~12** | **15** | **61** |

Teacher prose: 4,813 words. Agent wall-clock: 42.2 min.

## 3. Time-on-task estimate

61×2 = 122 · 5 chapters × 25 = 125 · 6 exercises × 15 = 90 · 12 rungs × 4 = 48 · 7 attempts × 12 = 84 · prose ≈ 21 → **≈ 8.2 h** — the first honest novice-path number.

**Final gradient: P1 8.2 > P2 3.3 > P3 3.1 > P4 2.1 h — strictly ordered. P1:P4 ≈ 3.9×**, at the edge of the predicted 4–8× band (and P2 would rise to ≈4.3 h under anchored scoring — its run predates the anchors). ≈8 h across multiple sittings is exactly the multi-session reality the resume design (also exercised this run — see below) was built for.

## 4. Findings

- **D16 RESOLVED:** per-probe anchors + key-quoting protocol produced faithful scoring under maximal kindness pressure. The lesson stands for the curriculum generally: *Sonnet-honesty requirements belong in the artifact being applied (the key), not in general instructions.*
- **Resume design incidentally exercised:** the teacher used the new progress.md v2 correctly — Assessment table written **probe-by-probe** (Edits at Ex4, 7, 8, 11, 14, 17, 18, 21, 24: a mid-assessment quit would now lose nothing), Chapter/Exercise columns tracked per step. One cosmetic miss: a duplicate "Next action" line (header + template footer), the footer copy left stale.
- **Soft miss (the only one):** the `geomapapp` enrichment was **not offered** despite step 1 at Novice — the one unexercised feature in the suite. One-line fix candidate: surface enrichment in A2's plan presentation, not just A3 memory.
- **Curriculum notes:** p00d is a weak discriminator (third persona to ace it cold — the error message self-explains); Sam echoed the other personas on vi ("theory vs actually doing it") and suggested predict-before-run for plots ("guess what the plot would look like before running it") — a genuinely good pedagogical idea.

## 5. Verdict

**PASS — 10/10.** The suite is complete: P4 10/10 · P3 9/10 (privacy defect → fixed + verified) · P2 9/10 (lenient score → anchors) · P1 10/10 on the anchored re-run. Every defect found was fixed and re-verified in a later run. Ready for the cross-persona report.

Cross-persona row: P1 — completed · 61 exchanges · ≈8.2 h modeled · scaffold density 2/3/0 · **10/10**.
