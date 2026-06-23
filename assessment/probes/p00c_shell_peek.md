*AI-generated draft (Claude, Anthropic) — for review.*

# Probe p00c — peek at a file from the shell  (coding · step 0 · skills: unix_basics)

## Prompt (show to student)
Before you load it in Python, you want a quick look at the **top** of
`plate_boundary.csv` — just the column header and the first couple of rows —
straight from the terminal, **without opening an editor**. What command would you use?

## Answer key
```bash
head plate_boundary.csv        # first ~10 lines — see the header + first rows
head -n 3 plate_boundary.csv   # or limit to the first 3 lines
cat plate_boundary.csv         # dumps the WHOLE file (fine for tiny text files, not a big one)
```
Key idea: `head` prints just the top of a file (great for checking a CSV's header without
loading it); `cat` prints the whole thing. For a big data file, reach for `head`, not `cat`.

## Hint ladder
- **R1:** Which command prints a file's contents to the screen? Is there one that shows only the first few lines?
- **R2:** Two commands print a file: one dumps the whole thing, the other shows only the top (and takes a flag to cap the number of lines). For a big CSV you want the top-only one so you don't flood the terminal. What are they named?
- **R3 (reveal):** the snippet above.

## Scoring (→ rubric §3)
- `correct`: uses `head` (or `head -n`) to view the top of the file — or `cat` while recognizing it's only sensible for a small file.
- `partial`: names `cat` but not `head`, or can't say how to limit the output on a large file.
- `wrong`: can't view the file without opening an editor.
**Anchor (Constitution III):** if `head`/`cat` were named for the student before they produced them, that was the reveal — a restated command scores `wrong`, depth 2.
