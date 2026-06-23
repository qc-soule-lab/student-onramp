*AI-generated draft (Claude, Anthropic) — for review.*

# Probe p02a — work a notebook  (coding · step 1 · skills: jupyter_basics)

## Prompt (show to student)
You're in a JupyterLab notebook. (a) How do you **run** a cell? (b) What's the difference between a
**code** cell and a **markdown** cell? (c) Your variables suddenly seem "undefined" even though you
defined them earlier — what does **restarting the kernel** do, and when would you reach for it?

## Answer key
- (a) **Shift+Enter** (run + advance) or Ctrl/Cmd+Enter (run in place); the toolbar ▶ runs too.
- (b) A **code** cell executes Python and shows output; a **markdown** cell renders text/headings/links (no execution).
- (c) **Restart kernel** clears all in-memory state (variables, imports) and starts a fresh Python process — reach for it when state is stale/confused (after editing an import, or to confirm the notebook runs top-to-bottom cleanly).

Key idea: the kernel holds your session's memory; cells share it in *run* order, not top-to-bottom order — restarting gives a clean slate.

## Hint ladder
- **R1:** What keystroke runs the current cell? And what holds your variables between cells?
- **R2:** Cells share one running Python session (the "kernel"); think about what a code cell does vs. a text/markdown cell, and what would happen to your variables if that session were reset. The intro_to_jupyterlab chapter covers it.
- **R3 (reveal):** the key answer above.

## Scoring (→ rubric §3)
- `correct`: runs a cell (Shift+Enter/▶) **and** distinguishes code vs markdown **and** explains restart-kernel = fresh state.
- `partial`: gets running plus *one* of (cell types / kernel restart), not both.
- `wrong`: can't run a cell or explain the kernel.
**Anchor (Constitution III):** any part (run keystroke / cell types / kernel meaning) named for the student before they produced it was revealed — score per the after-reveal rule, depth 2.
