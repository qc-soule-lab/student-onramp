*AI-generated draft (Claude, Anthropic) — for review.*

# Probe p02b — python fundamentals  (coding · step 1 · skills: python_fundamentals)

## Prompt (show to student)
Given `depths = [2200, 1850, 1490, 1320]` (seafloor depths in metres):
(a) How do you get the **first** value? the **last**? the **first two**?
(b) Write a one-line call that returns **how many** values are in the list.
(c) In `import numpy as np`, what does `as np` do?

## Answer key
- (a) `depths[0]` (first), `depths[-1]` (last), `depths[:2]` (first two) — zero-based indexing; negatives count from the end; slices are half-open.
- (b) `len(depths)` → 4.
- (c) imports the `numpy` module under the shorter **alias** `np`, so you call `np.<func>` instead of `numpy.<func>`.

Key idea: indexing/slicing pull elements out of a sequence (0-based, half-open slices); `len()` is a built-in; `import … as` gives a module a local alias.

## Hint ladder
- **R1:** Which index is the *first* element in Python — 0 or 1? And how might you count the items without counting by hand?
- **R2:** Python indexes from 0 and counts from the end with negatives; a slice `a:b` stops *before* `b`. There's a one-word built-in that returns a length, and `import x as y` is just renaming. The python_fundamentals chapter has all three.
- **R3 (reveal):** the key answer above.

## Scoring (→ rubric §3)
- `correct`: indexing (first/last/slice) **and** `len()` **and** the alias meaning.
- `partial`: indexing right but misses `len()` or the alias (or vice versa).
- `wrong`: can't index or count the list.
**Anchor (Constitution III):** any element (an index form, `len()`, the alias meaning) spelled out before the student produced it was revealed — score per the after-reveal rule, depth 2.
