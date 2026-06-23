*AI-generated draft (Claude, Anthropic) — for review.*

# Probe p00b — open a file in vi  (coding · step 0 · skills: vi_basics)

## Prompt (show to student)
From the terminal, open `plate_boundary.csv` in **vi**, read its header line, then leave
the editor **without changing the file**. Walk me through the keystrokes — including how
you'd quit, and how you'd quit if you'd accidentally typed something.

## Answer key
```text
vi plate_boundary.csv     # open the file
                          # (read the first line — the CSV header)
Esc                       # make sure you're in normal/command mode
:q                        # quit (file unchanged)
:q!                       # quit DISCARDING any accidental edits
:wq                       # (for contrast) save AND quit
```
Key idea: vi starts in **normal mode** (keys are commands, not text). `i` enters insert
mode to type; **`Esc`** returns to normal mode; `:q` quits, `:q!` quits without saving,
`:wq` saves and quits. Knowing how to *get out* is the survival skill.

## Hint ladder
- **R1:** How do you open a file in vi from the shell — and once inside, how do you get back out?
- **R2:** One command opens a file in vi. The catch is *leaving*: vi starts in command mode (keystrokes are commands, not text), and the quits are colon-commands — one quits normally, one quits throwing away changes, one saves first. The `vi_ref` reading lists the survival set — which keys?
- **R3 (reveal):** the snippet above.

## Scoring (→ rubric §3)
- `correct`: opens with `vi`, reads the header, **and** exits deliberately (`:q`/`:q!`),
  distinguishing save vs. discard.
- `partial`: opens the file but is unsure how to exit / can't tell `:q` from `:wq` from `:q!`.
- `wrong`: can't open the file in vi.
**Anchor (Constitution III):** keystrokes produced only after the survival set (`Esc`/`:q`/`:q!`/`:wq`) was shown score `wrong`, depth 2 — restating the reveal is not knowing it.
