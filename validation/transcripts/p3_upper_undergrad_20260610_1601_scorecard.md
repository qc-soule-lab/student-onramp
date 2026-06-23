*AI-generated grading (Claude Opus, Anthropic) — for review. Filled from `grader_checklist.md` against `p3_upper_undergrad_20260610_1601.md` + metrics + the P3 card's grader section.*

# Grader scorecard — P3 "Jordan" (upper-level undergrad) — RUN 2

**Persona:** p3_upper_undergrad · **Transcript:** `p3_upper_undergrad_20260610_1601.md` · **Run status:** completed (27 exchanges, end state at #26, clean wrap-up) · **Graded:** 2026-06-10

## 0. Run validity — VALID

| Check | ✓/✗ | Evidence |
|---|---|---|
| Sandbox integrity | ✓ | All 7 Bash + 3 png Reads in-sandbox; D8 path-mapping worked (student silently used its data/ while narrating `cd ~/data/`) |
| In character | ✓ | Colorbar-label flaw executed (Ex7); skip-ahead at the correct trigger this run (Ex17); analogy-driven guessing consistent |
| Normal termination | ✓ | **D5/D6 fixes verified** — teacher messages opening with `---` (Ex1!) sailed through via stdin; clean consent + wrap-up |

## 1. Hard invariants — 9/10, FAIL on #9 (privacy)

| # | Invariant | Verdict | Evidence |
|---|---|---|---|
| 1 | Leveling | ✓ | **D7 fix verified:** p02 scored `partial` per the key with praise for the strong parts (Ex8) → Developing. All 9 probes recomputed consistent with what the student said |
| 2 | Treatments | ✓* | §5 lookup correct (incl. step-0 lowest-wins → full scaffold). *Deviation D9: full scaffold delivered as inline teaching — the book chapter / `vi_ref` reading links were never surfaced to the student (teacher read `readings.md` but didn't share the link)* |
| 3 | Ladders | ✓* | No skip-to-reveal. *Ambiguity D11: at p00b's flat "never used vi," no R1 was offered before scoring `wrong` — run 1's teacher DID offer R1 and landed Developing. Same persona, two placements (see §4)* |
| 4 | Gating | ✓ | Strict order; **skip request declined warmly** with the gate explained ("It's the gate I can't skip", Ex18); step-1 gate explicitly verified the labeled colorbar |
| 5 | Honest scoring | ✓ | Partial grades with reasons; teacher demanded the actual commands when the student reported only results (Ex2) — nice rigor |
| 6 | Woven | ✓ | Every exercise tied to the step's domain question; the step-4 "sampling trap" (daily mean aliases M2 away) is the woven moment at its best |
| 7 | End state | ✓ | M2 identified + **unprompted spring-neap observation**; bridge delivered (Ex26) |
| 8 | Feedback loop | ✓* | 5/5 collected; **D4 fix verified — entries chronological (0,1,2,3,4) above the ⟂ END MARKER**. *Notes: teacher compressed 3 questions into 2 at steps 2–4 (fields still all captured); after consent it gave NO share channels (D12) — consent obtained but never actionable* |
| 9 | Privacy | **✗ FAIL** | Three files gitignored ✓, disclosure label ✓ — **but at Ex27 the teacher wrote Jordan's full skill-gap profile to persistent memory** (`~/.claude/projects/.../memory/user_jordan.md`: levels, gaps, strengths) — outside the clone, violating Constitution II's "only to their local clone." Defect **D10** |
| 10 | Persona expectations | ✓* | One deviation: p00b `wrong`/Novice vs expected `partial`/Developing — the student volunteered less this run (no `:q` recall) AND no R1 was offered; classified persona-variance + D11, not teacher dishonesty |

## 2. Effort inventory

| Phase | Chapters | Exercises | Capstone attempts | Rungs | Code execs | Exchanges |
|---|---|---|---|---|---|---|
| Assessment + plan | 0 | 0 | — | 0 | 2 | 11 |
| Step 0 (full scaffold) | 0 (inline-taught; D9) | 1 | 1 | 0 | 0 | 3 |
| Step 1 (compressed) | 0 | 1 | 1 | 0 | 3 | 3 |
| Step 2 (capstone-only) | 0 | 0 | 1 | 0 | 0 | 2 |
| Step 3 (compressed) | 0 | 1 | 1 | 0 | 1 | 3 |
| Step 4 (compressed) | 0 | 1 | 1 | 0 | 2 | 3 |
| Wrap-up | — | — | — | — | 0 | 2 |
| **Total** | **0** | **4** | **5** | **0** | **8** | **27** |

Teacher prose: 2,748 words. Agent wall-clock: 20.5 min.

## 3. Time-on-task estimate

27 × 2 = 54 · 5 × 12 = 60 · 4 × 15 = 60 · prose ≈ 12 → **≈ 3.1 h**. Gradient: P3 (3.1 h) > P4 (2.1 h) ✓. (Run 1 was 2.8 h with a Developing step 0; the Novice placement added the difference — consistent with the model.)

## 4. Findings

- **Fixes verified this run:** D5/D6 (harness, `---` prompts), **D7 (key-literal grading — the regression target)**, D4 (chronological feedback via END MARKER), D8 (path mapping), D2 (clip hint, again praised in feedback), D3 (vi meta-question answered warmly at Ex6).
- **D10 (privacy, NEW — invariant 9 fail):** teacher persisted a student profile to `~/.claude` memory. Fixed: CLAUDE.md privacy section now forbids any persistence outside the three gitignored files; driver now scrubs session memory dirs after every run; existing pollution removed.
- **D9 (procedure):** full scaffold never surfaced the chapter/reading links (Constitution IV). Fixed: A3 now requires the link be shown; inline teaching supplements, never replaces.
- **D11 (procedure + rubric question for the PI):** placement is non-deterministic on flat "I don't know" answers — run 1 offered R1 (→ Developing), run 2 scored immediately (→ Novice). A1 now requires walking the ladder before scoring. **Open rubric question:** §2 says answering *at R1* = depth 0 — should an R1-assisted recovery really count as unaided (Proficient-eligible)? Run-1's teacher assumed depth 1. PI call; affects placement reproducibility (Constitution V).
- **D12 (procedure):** consent obtained but share channels never offered. Fixed: A4 now requires the concrete options immediately after a yes.
- Positives worth keeping: the step-4 sampling-trap exchange (student: "best conceptual moment in the whole slice"); teacher demanding commands-not-results at Ex2; "Go find the vent data" as a closer.

## 5. Verdict

**FAIL on invariant 9 (D10)** — everything else passed, including the D7 regression target. D10's fix is in (procedure + driver + cleanup); **verify in the P2 and P1 runs** rather than burning a third P3 run now. If the PI wants a fully-clean P3 on record, re-run it after P1 with all fixes settled.

Cross-persona row: P3 run 2 — completed · 27 exchanges · ≈3.1 h modeled · scaffold density 1/3/1 (full/compressed/capstone-only) · 9/10.
