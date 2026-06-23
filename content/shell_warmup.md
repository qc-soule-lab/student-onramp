*AI-generated draft (Claude, Anthropic) — for review.*

# Step 0 shell warm-up — practiced, not graded

Build terminal *comfort* before the capstone. Walk the student through this short sequence in
their real JupyterLab terminal, one line at a time — they type it, see the result, you confirm,
then move on. This is **practice, not assessment**: nothing is scored, and any rung can be
repeated until it feels easy. Offer it to Novice/Developing students; a Proficient student can
blitz it in under a minute.

Each task: *what to try → what they should see.*

1. **Where am I?** `pwd` → prints the current directory path.
2. **What's here?** `ls` → lists names; then `ls -lh` → adds human-readable sizes + permissions.
3. **Move around.** `cd ~/student-onramp` (course home) → `cd data` (into the data folder) →
   `cd ..` (back up one) → `cd -` (jump to the previous directory). Run `pwd` after each to confirm.
4. **Tab-completion — the big time-saver.** Type `cd ~/student-onramp/da` and press **Tab**; the
   shell finishes `data/`. Start the grid's filename and press **Tab** again. Tab early, tab often.
5. **History.** Press **↑** to recall the last command, edit it, re-run — instead of retyping.
6. **Peek without opening.** `head plate_boundary.csv` → first ~10 lines (header + rows);
   `head -n 3 plate_boundary.csv` → just 3. (`cat` dumps the *whole* file — fine only for tiny ones.)
7. **A scratch-file round-trip.** `mkdir scratch` → `touch scratch/notes.txt` → `ls scratch`
   (see it) → `rm scratch/notes.txt && rmdir scratch` (clean up).
8. **Read an error on purpose.** `cat nope.csv` → `No such file or directory`. That's the shell
   saying *"not here, from where you are"* — not "gone." Orienting with `pwd`/`ls` is the fix.

When these feel routine, the student is ready for the step-0 capstone — which now *uses* them:
navigate with tab-completion, `head` the file, then open it in vi and exit cleanly.

Keep `content/terminal_survival_card.md` open alongside this — the same commands as a cheat sheet.
