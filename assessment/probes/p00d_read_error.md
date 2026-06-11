*AI-generated draft (Claude, Anthropic) — for review.*

# Probe p00d — read a shell error and recover  (coding · step 0 · skills: unix_basics)

## Prompt (show to student)
You run `cat plate_boundary.csv` and the terminal answers:
```
cat: plate_boundary.csv: No such file or directory
```
You know the file exists in the project. **What does this error mean, and what's your next move?**

## Answer key
The shell looked for that name **in your current directory** and didn't find it — almost always
because you're in the *wrong directory* (or mistyped the name), **not** because the file is gone.
Recover by orienting and pointing at the right place:
```bash
pwd                       # where am I right now?
ls                        # what's actually in this directory?
cd ~/data                 # move to where the file lives (or give the full/relative path to cat)
cat ~/data/plate_boundary.csv
```
Key idea: commands run **relative to where you are**. "No such file or directory" means the path
doesn't resolve from here — fix your location or the path; tab-completion avoids typos.

## Hint ladder
- **R1:** The shell can't find a file you know exists. Given that commands run relative to *where you currently are*, what's the most likely reason?
- **R2:** It's looking in your current directory. Check `pwd` and `ls` to see where you are and what's here; the file is probably in another directory — `cd` there, or give `cat` the full/relative path.
- **R3 (reveal):** the snippet above.

## Scoring (→ rubric §3)
- `correct`: reads it as a *wrong-directory / wrong-path* problem (not "file deleted/corrupt") **and** recovers via `pwd`/`ls`/`cd` or the correct path.
- `partial`: right idea but vague on recovery, or only fixes it by trial-and-error guessing.
- `wrong`: misreads the error (thinks the file is gone/broken) or is stuck.
**Anchor (Constitution III):** if you told them it's a wrong-directory/path problem before they said it, that was the reveal — a restated diagnosis scores `wrong`, depth 2.
