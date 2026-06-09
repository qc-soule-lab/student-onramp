*AI-generated draft (Claude, Anthropic) — for review. Scoring thresholds and treatment rules below are a fixed lookup, not runtime judgment (Constitution I).*

# Assessment Rubric — v1 slice

The runtime never "decides how good a student is" by feel. It **scores each probe against its answer key**, **records how far down the hint ladder** the student needed, maps that to a **level**, and looks up the **treatment** for each slice step. Pure table — runs identically on Sonnet.

## 1. Per-probe scoring (against the answer key in each probe file)

Each probe is scored on its own key:

| Score | Meaning |
|---|---|
| `correct` | Reached the key answer essentially unaided. |
| `partial` | Right idea, incomplete/imprecise; or correct only after mid-ladder hints. |
| `wrong` | Did not reach the key, or only after the full worked reveal. |

## 2. Hint-ladder depth (Constitution VI — walked-to-answer ≠ knew-it)

Every probe ships a 3-rung ladder: **R1 guiding question → R2 concrete hint → R3 worked reveal.** Record the deepest rung used:

| Rung reached | Depth |
|---|---|
| Answered before R1 / at R1 | `0` (unaided) |
| Needed R2 | `1` |
| Needed R3 (the reveal) | `2` |

## 3. Probe → level

Combine score + depth:

| Score \ Depth | 0 (unaided) | 1 (hint) | 2 (reveal) |
|---|---|---|---|
| `correct` | **Proficient** | Developing | Developing |
| `partial` | Developing | Developing | **Novice** |
| `wrong` | Novice | Novice | **Novice** |

## 4. Skill → level (when a skill has multiple probes)

Take the **lower** of the probe levels (honest placement — Constitution III). A skill with no probe attempted defaults to **Novice** (scaffold rather than assume).

## 5. Level → per-step treatment (the personalization lookup)

For each slice step, the student's level on that step's skill(s) selects the treatment:

| Level | Treatment | What the student does |
|---|---|---|
| **Novice** | **Full scaffold** | Read the mapped book chapter, work the guided exercise with hint ladders available, then the capstone. |
| **Developing** | **Compressed** | Skip the chapter read; do the exercise; hints available on demand; then the capstone. |
| **Proficient** | **Capstone only** | Skip the teaching; go straight to the step's capstone task to confirm. |

A step whose level is mixed across its skills uses the **lowest** skill level (teach to the weakest needed skill).

## 6. Determinism

Same probe answers + same ladder depth → same levels → same treatments → same journey (Constitution V). No randomness, no "vibe."
