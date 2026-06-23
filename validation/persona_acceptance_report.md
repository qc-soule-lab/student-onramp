*AI-generated report (Claude Opus, Anthropic) — for review. Synthesis of the four persona acceptance runs (plan: `persona_acceptance_plan.md`; evidence: `transcripts/` — each run has a transcript, metrics sidecar, and graded scorecard).*

# Persona acceptance report — v1 slice, 2026-06-11

## Headline

**All four personas completed the slice on Sonnet, every hard invariant now passes, and the
time-on-task gradient is strictly ordered.** Six runs were needed for the four passes (one
harness abort, one grading-regression re-run); every defect found was fixed and re-verified in a
later run. The suite caught **16 defects** — 5 curriculum, 6 procedure, 5 harness — including
one systemic finding that changes how this curriculum should encode honesty requirements.

## Final results

| | P1 Sam (HS senior) | P2 Riley (1st-year) | P3 Jordan (upper UG) | P4 Alex (grad) |
|---|---|---|---|---|
| Verdict | **PASS 10/10** (run 3) | 9/10¹ | 9/10² (run 2) | **PASS 10/10** |
| Exchanges | 61 | 33 | 27 | 24 |
| **Modeled time** | **≈ 8.2 h** | ≈ 3.3 h¹ | ≈ 3.1 h | ≈ 2.1 h |
| Scaffold density (full/compr/capstone) | 2/3/0 | 0/4/1¹ | 1/3/1 | 0/0/5 |
| Designed stress moment | no-reveal-under-pressure ✓ · vi gate fail→remediate ✓ | confident-wrong not accepted ✓ | skip-ahead declined ✓ | Proficient gate failed on evidence ✓ |

¹ P2 ran before the scoring anchors; its one lenient score (p00b) cost step 0 its full scaffold — under anchored scoring P2 ≈ 4.3 h with density 1/3/1 or 3/1/1.
² P3's failure was the memory-write privacy defect (D10), fixed and verified in P2 and both P1 runs.

**Time gradient: 8.2 > 3.3 > 3.1 > 2.1 h — strictly ordered; P1:P4 ≈ 3.9×** (≈ 2.5× between
anchored-P2 and P3 — those two personas genuinely sit close together; the curriculum
discriminates them by *which* steps scaffold, more than by total hours).
Constants used: chapter 25 min · exercise 15 + 4/rung · capstone attempt 12 · exchange 2 ·
prose 225 wpm — **PI calibration pending (open question 3)**.

## The systemic finding (D16)

Sonnet grades a struggling student generously: 3 of 4 personas initially drew inflated scores,
each time by classifying an answer-containing hint as a mid-ladder rung. Two rounds of
general-instruction fixes in CLAUDE.md did **not** stop it — the P1 run-2 teacher had the
"count rungs by content" rule in its own procedure and still did it. What worked:
**one-line scoring anchors inside each probe's key** ("keystrokes produced only after the
survival set was shown score `wrong`") plus an A1 rule to quote the key's line before scoring.
The anchored P1 re-run recorded five `wrong`/Novice scores for a likeable, struggling student —
under maximal kindness pressure.

> **Design principle for this curriculum:** Constitution-III honesty requirements must live in
> the artifact being applied (the answer key), not in general procedure instructions.

## What the runs proved (each verified in ≥1 run after its fix)

- **Gates judge evidence, not level** — failed a Proficient student's rushed "~24 h diurnal"
  capstone (P4) and a Novice's vi panic (P1); both remediated in place, never advanced.
- **Ladder discipline** — R1-first everywhere, incl. under explicit "just tell me" pressure.
- **Lock enforcement** — skip-ahead request declined with the progression explained (P3).
- **Honest scoring under social pressure** — confident wrongness walked back via R1, hint
  recorded (P2); generous scoring eliminated by anchors (P1 run 3).
- **Privacy** — three gitignored files only; the memory-write leak (D10) fixed at procedure +
  harness level; consent-gated sharing through sanctioned channels only (after D14 banned a
  confabulated email).
- **Woven coding** — every tool introduced at its domain moment in every run; full scaffold
  surfaces chapter/reading links with attribution (D9, verified P1 run 3).
- **Feedback loop** — 3 questions after every capstone, chronological entries (D4 END-MARKER
  fix), real errors captured.
- **Resume bookkeeping (new)** — P1 run 3's teacher wrote the Assessment table probe-by-probe
  and tracked chapter/exercise/capstone per step: a mid-assessment quit now loses nothing.
  **The interrupt/resume conversation test (Scenario R) has NOT yet run.**

## Defect ledger (all fixed unless noted)

| # | Type | Finding → fix |
|---|---|---|
| D1 | curriculum | step-2 capstone was verbatim p03 → differentiated (applied framing) |
| D2 | curriculum | step-1 "overlay" needed a clip hint → added |
| D3 | procedure | meta-questions ignored ("why vi?") → answer briefly, then continue |
| D4 | curriculum | feedback entries mis-ordered → unique ⟂ END MARKER anchor |
| D5 | harness | prompt as argv broke on leading `---` → stdin |
| D6 | harness | failed exchange lost teacher text → record before student call |
| D7 | procedure | key applied leniently (unlabeled colorbar = correct) → grade-literally rule |
| D8 | harness | probes say `~/data`, sandbox differs → card path-mapping |
| D9 | procedure | full scaffold skipped chapter links → links required, with attribution |
| D10 | procedure | **student profile written to `~/.claude` memory** → three-files-only rule + driver scrub |
| D11 | procedure | "I don't know" scored without R1 → ladder before scoring |
| D12 | procedure | consent without share channels → concrete options required |
| D13 | procedure | score-anchor variance across sessions → rungs-by-content rule |
| D14 | procedure | **confabulated email in consent flow** → sanctioned channels only |
| D15 | harness | empty teacher text killed resumed session → normalize + nudge |
| D16 | systemic | general rules don't stop grading generosity → **per-probe key anchors** |

## Curriculum signals from the synthetic students (for the next revision)

1. **vi practice gap** — all three sub-grad personas flagged narrated-vi vs doing-vi
   ("theory vs actually doing it"). Consider a sacrificial `test.csv` live drill on real seats.
2. **p00d is a weak discriminator** — three personas aced it cold; the error message
   self-explains. Consider a harder error (e.g. permission denied, or a misleading path).
3. **Assessment length for novices** — Sam: 24 of 61 exchanges before any teaching ("the
   assessment felt pretty long"). Option: split assessment per-tier (probe step-N skills just
   before step N) — also fits the multi-session reality.
4. **Bridge-at-every-step** — Riley's suggestion ("that's the moment the whole session snapped
   into focus"); cheap: one bridge sentence per step in journey.yml.
5. **Predict-before-run** — Sam's suggestion for plots; strong pedagogy, one line in A3.
6. **Enrichment never fired** — geomapapp wasn't offered to either Novice-leveled student run;
   surface it in A2's plan presentation (the only soft miss left).

## Open questions for the PI

1. **Rubric §2 depth semantics** — "answered at R1" = depth 0 makes an R1-assisted recovery
   Proficient-eligible; teachers interpreted it three different ways before the anchors. Intended?
2. **Time bands** — first real numbers are in (8.2 / ~4 / 3.1 / 2.1 h). Set acceptance bands, or
   adjust constants first? (12-min capstone overstates conceptual step 2; chapter minutes unmeasured.)
3. **P2 anchored re-run?** — P2/P3 are the only runs whose grading predates the anchors. Optional;
   the anchors' effectiveness is already proven on P1, the harder case.

## Remaining before v1 sign-off

1. **Scenario R** — the interrupt/resume conversation test (driver flags ready; recipe in the plan).
2. **Human fixture runs** (T036/T037 per `sonnet_acceptance_protocol.md`) — the constitution's
   final acceptance gate; the persona suite is the automated pre-check, not the replacement.
3. Commit the anchored probes + P1 artifacts + this report (uncommitted, pytest green).
