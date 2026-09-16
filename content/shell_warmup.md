*AI-generated draft (Claude, Anthropic) — for review.*

# Step 0 shell warm-up — practiced, not graded

Build terminal *comfort* before the capstone. Walk the student through this in their real
JupyterLab terminal, one line at a time — they type it, see the result, you confirm, then move on.
This is **practice, not assessment**: nothing is scored, and any rung can be repeated until it's
easy. Offer the full drill to Novice/Developing students; a **Proficient** student can blitz it in
under a minute and go straight to the capstone. Either way, the **tab check and the three
navigation drills below are the gate** — the capstone has *every* student demonstrate them, so a
mentor's later "cd into the probes folder, now back up to content" just works.

Each task: *what to try → what they should see.*

## Which tab am I in? — do this first
Two JupyterLab terminal tabs, side by side: this one (running Claude) and a plain shell. If the
student has only one tab, have them open the shell now: **File → New → Terminal**. Then:
1. **Point at each tab and name it.** Which is Claude, which is the shell, and what is the tell?
   → The shell's prompt ends in `$`; Claude's input line starts with `>` inside its frame.
2. **Type `pwd` in each tab.** → The shell prints a path. Claude answers in words. That contrast is
   the test they can run any time they are unsure.
3. **Mis-route on purpose.** Type `hello` at the `$` prompt → `command not found` (the shell tried
   to run `hello` as a program). That is what a sentence sent to the wrong tab looks like. The
   reverse, a command typed at `>`, is a message to Claude: nothing runs.
Everything below is typed in the **shell tab**; every prediction and report comes back **here**.
If a command shows up in this tab during the drill, do not run it: point at the `$` tab and wait.

## Orient
1. **Where am I?** `pwd` → prints the current directory path.
2. **What's here?** `ls` → lists names; then `ls -lh` → adds human-readable sizes + permissions.

## Navigation drills — the Step-0 gate (walk these until they're automatic)
The floor everything else stands on. **Tab-complete every path segment** — start a name, press
**Tab**; when it won't finish (an ambiguous prefix), press **Tab twice** to list the choices, then
type one more letter. Repeat any rung until it's second nature.

**A. Up and down the tree.**
- **Down** into a child: `cd ~/student-onramp`, then `cd da`**⇥** (Tab finishes `data/`) → `pwd` to confirm.
- **Down two levels:** from home, `cd ~/student-onramp/as`**⇥**`/pr`**⇥** → `assessment/probes/` → `pwd`.
- **Up:** `cd ..` (up one) → `pwd`; `cd ../..` (up two) → `pwd`. `..` means "the parent of where I am."
- **Ambiguity on the way:** `cd ~/student-onramp/s`**⇥** won't complete — three dirs start with `s`
  (`scripts`, `skill_maps`, `specs`); press **Tab twice** to see them, then `sk`**⇥** → `skill_maps/`.

**B. The tilde `~` — home from anywhere.**
- `~` *is* your home directory. From anywhere deep in the tree, `cd ~` (or just bare `cd`) jumps
  straight home → `pwd` shows your home path.
- Reach a target from *anywhere* with an absolute `~` path: wherever you're standing,
  `cd ~/student-onramp/da`**⇥** lands in `data/`. (Contrast: `cd data` only works when `data` is a
  child of where you already are.)

**C. Identify the pathway (predict → `pwd`).**
- Before you press Enter on a `cd`, **say the full path you expect to land in.** Then run it and
  `pwd` to check your prediction. (This is the predict → do → report habit, applied to moving around.)
- **Absolute vs relative:** an **absolute** path starts at `/` or `~` and works from anywhere; a
  **relative** path (`data`, `../content`) is read from where you currently stand. `pwd` always
  reports the absolute truth — reach for it whenever you're unsure where you are.

## The rest of the survival kit
3. **History.** Press **↑** to recall the last command, edit it, re-run — instead of retyping.
4. **Peek without opening.** `head plate_boundary.csv` → first ~10 lines (header + rows);
   `head -n 3 plate_boundary.csv` → just 3. (`cat` dumps the *whole* file — fine only for tiny ones.)
5. **A scratch-file round-trip.** `mkdir scratch` → `touch scratch/notes.txt` → `ls scratch`
   (see it) → `rm scratch/notes.txt && rmdir scratch` (clean up).
6. **Read an error on purpose.** `cat nope.csv` → `No such file or directory`. That's the shell
   saying *"not here, from where you are"* — not "gone." Orienting with `pwd`/`ls` is the fix.

## Part 2 — handy extras (practiced, optional; never required to pass)
Not part of the gate — offer these as the student is ready, or as a later reach-for. They're the
commands that make real data work faster. Same *try → what you should see*; clean up anything you make.

- **Page a big file — `less`.** `less data/plate_boundary.csv` → scroll with **Space**/**b**, quit
  with **`q`**. Unlike `cat`, it doesn't dump the whole file — and **`q`** always gets you back out.
- **Count lines — `wc -l`.** `wc -l data/plate_boundary.csv` → the number of rows (header included).
- **Search inside a file — `grep`.** `head` the file, pick a word you see, then
  `grep -i <word> data/plate_boundary.csv` → every line containing it. `grep -n …` adds line numbers;
  `grep -c …` just counts the matches.
- **Combine commands — the pipe `|`.** Send one command's output straight into the next:
  `ls data | wc -l` → how many files are in `data/`. Read `|` as "…and feed that into…".
- **Save output to a file — `>` and `>>`.** `ls data > files.txt` writes the listing to a file
  (**overwrites**); `echo done >> files.txt` **appends** a line; `cat files.txt` to see it;
  `rm files.txt` to clean up. `>` clobbers, `>>` adds.
- **Many files at once — wildcards `*` `?`.** `ls data/*.nc` → all netCDF files; `ls data/axial_*`
  → everything starting `axial_`. `*` = any run of characters, `?` = exactly one.
- **Copy / move / rename — `cp` / `mv`.** `cp data/plate_boundary.csv pb_copy.csv` (copy) →
  `mv pb_copy.csv pb_renamed.csv` (**`mv` both moves *and* renames**) → `rm pb_renamed.csv` (clean up).
- **Ask a command for help — `man` / `--help`.** Forgot a flag? `ls --help` prints quick usage;
  `man ls` opens the full manual (**`q`** to quit). The answer is usually one keystroke away.

When the tab check and the three navigation drills feel routine, the student is ready for the
step-0 capstone — which has them name the two tabs and their tell, *demonstrate* all three
navigation musts (go down and back up, make a `~` jump, and predict a path), then `head` the file
and make a clean vi exit, sending every command to the shell tab.

Keep `content/terminal_survival_card.md` open alongside this — the same commands as a cheat sheet.
