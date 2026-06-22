*AI-generated draft (Claude, Anthropic) — for review. Copy-paste tester instructions for a human acceptance run (T036, novice fixture). Maintained alongside `sonnet_acceptance_protocol.md`; swap the script table for `fixtures/profile_intermediate.md` to make the intermediate version.*

# Onramp test instructions — novice profile

Hi! You're the first human tester of the lab's new onboarding course. The course runs as a
guided conversation with Claude inside a copy of the course repository, on your JupyterHub seat.

**The big idea:** you'll play the role of a near-beginner student. We're testing the *course* —
whether it assesses fairly, teaches at the right level, and refuses to cut corners — not testing
you. Some of your scripted answers are wrong **on purpose**; that's the test working.

**Time:** plan for about half a day total. **You do not need to do it in one sitting** — stopping
and resuming is itself something we're testing (see step 6).

---

## 1. Setup (~15 min, JupyterLab terminal)

```bash
cd ~                                    # clone into your home folder, not wherever you happen to be
git clone -b 001-coding-onramp-v1 https://github.com/qc-soule-lab/student-onramp.git
cd student-onramp
uv sync
claude
```

Inside Claude, type `/model claude-sonnet-4-6` (important — this exact model is what we're
validating; if your seat doesn't offer it, stop and tell Dax). Then type:

```
assess me
```

When it asks your name: give your first name or say you'd rather stay anonymous — either is
fine, and everything personal stays in your local copy (never uploaded, never committed).

## 2. The assessment — answer from this script, verbatim

Claude will ask ~9 questions. **Answer each with the scripted line below, even when it's
wrong.** If Claude offers a hint, give the "after hint" line. Don't improvise better answers —
the wrong ones are load-bearing.

| When it asks about… | Say first | If it gives you a hint, then say |
|---|---|---|
| terminal commands to find a file | "I'm not sure… type the folder name?" | "oh — `cd data`, `ls`?" |
| peeking at the top of a CSV | "Um… double-click it? I don't know a terminal command for that." | first hint: "something like… 'top'?" · after it shows you: "oh — `head plate_boundary.csv`." |
| a "No such file or directory" error | "Maybe the file got deleted somehow?" | "oh — I'm just in the wrong folder, so `cd` there first and try again?" |
| the vi editor | "Honestly I don't know how to get out of vi." | (after it shows you) "`:q!`, got it." |
| kilometers per degree | "Maybe ~100 km? Not sure about longitude." | "shorter near the pole?" |
| matplotlib / plotting code | "`plt.plot(depth)`? I don't know about a colorbar." | (let it walk you through the ladder) |
| why there's a volcano at Axial | "There's a volcano… because it's the ocean?" | (let it walk you through) |
| xarray / opening a data file | "Open it with pandas `read_csv`?" | (let it walk you through) |
| pandas / resample | "I've never used pandas." | (let it walk you through) |

## 3. During the course itself — be a beginner, honestly

After the assessment, Claude builds you a learning plan (it should be "full scaffold"
everywhere) and walks you through 5 steps. From here on, **work normally but stay in
character as a beginner**: do what it asks, run the commands and code it gives you, ask when
you don't understand, and don't volunteer knowledge a beginner wouldn't have.

**One scripted moment remains.** At the **step-0 capstone**, it will have you open
`plate_boundary.csv` in vi. Get stuck on purpose: press `i`, type a few junk characters, then
tell Claude something like *"I think I broke it — it won't let me out."* Follow its rescue
instructions exactly. (It should walk you out and have you redo it — it must NOT wave you
through.)

If it offers an optional "see it visually first" link (GeoMapApp): your choice, either way is fine.

## 4. The feedback questions — answer as YOURSELF

After every step, Claude asks three quick questions (difficulty / friction / keep-or-cut).
**These are NOT scripted — give your genuine reactions.** This is the most valuable thing you
produce: real human friction notes.

## 5. Take notes outside the conversation too

Keep a scratch note (paper is fine) of: anything confusing or broken, anywhere you waited too
long, anywhere it felt condescending or too fast, the actual clock time you spend reading each
chapter, and the moment (if any) you'd have quit if this weren't a favor to Dax.

## 6. Stopping and resuming

Stop whenever you like — just close the terminal. To resume (even days later): open a terminal,
`cd student-onramp`, run `claude`, and type `continue`. It should greet you, tell you exactly
where you left off, and **never re-ask an assessment question it already asked**. If it does
re-ask one, note it — that's a bug we want to know about.

## 7. When you finish

At the end, Claude will ask whether you're willing to share your feedback file with Dax —
please say yes and follow its instructions. Then also send Dax:

1. The conversation transcript: type `/export` in Claude and send the file it produces.
2. From your `student-onramp` folder: `feedback.md`, `journey_plan.md`, `progress.md`
   (these exist only on your seat — nothing is shared unless you send it).
3. Your scratch notes from step 5, photos fine.

## 8. If something breaks

Note what you typed and what happened (screenshot if easy), then either ask Claude to continue
or stop and resume later. Breakage is a finding, not a failure — don't troubleshoot for more
than a couple of minutes. Questions any time: dax.soule@qc.cuny.edu.

Thank you, Rose — you're the first real human through this, and your friction notes will shape
it for every student after you.
