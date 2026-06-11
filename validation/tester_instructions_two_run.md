*Drafted with Claude (Anthropic) for Dr. Soule's lab — reviewed by Dax Soule.*

# Onramp test instructions — two runs

Hi Alexa! You're the third tester of the lab's new onboarding course, and you have a double
mission: you'll take the course **twice**.

- **Run 1 — as yourself.** No script, honest answers. You're the first genuinely real student
  through it; we're testing whether the course reads a real person correctly.
- **Run 2 — as "the hotshot."** A fully scripted role: an advanced student who knows
  everything… and rushes one answer. We're testing whether the course skips ALL the teaching
  for an expert and still refuses to wave a wrong answer through.

**Do them in this order** — Run 1 must come first, while the course is still new to you (Run 2's
script will show you all the answers, which would spoil Run 1; nothing can spoil Run 2).

**Time:** Run 1: anywhere from 2 hours to most of a day, depending on where it places you.
Run 2: about an hour. **Neither needs to be one sitting** — see "Stopping and resuming."

---

# RUN 1 — as yourself

## 0. Before you start — one short email (important!)

Before you run anything, email Dax 3–5 honest lines about where you'd place yourself:

- Terminal/command line: never used / some / comfortable?
- Python: none / a course / use it regularly? (matplotlib? pandas? xarray?)
- The vi editor: ever used it?
- Marine geology / plate tectonics: how much background?

This is sealed ground truth — after your run, we compare where the course *placed* you against
where you *said* you were. Send it before you start so the comparison is fair.

## 1. Setup (about 15 min, JupyterLab terminal)

```
git clone -b 001-coding-onramp-v1 https://github.com/qc-soule-lab/student-onramp.git onramp-real
cd onramp-real
uv sync
claude
```

Inside Claude, type `/model claude-sonnet-4-6` (important — this exact model is what we're
validating; if your seat doesn't offer it, stop and tell Dax). Then type:

```
assess me
```

When it asks your name: give your first name or stay anonymous — either is fine; everything
personal stays in your local copy (never uploaded, never committed).

## 2. The whole run — just be you

Answer the assessment with whatever you actually know — "I don't know" is a perfectly good
answer, and guesses are fine if you say they're guesses. Don't study or look things up first.
Then work the course it builds for you: read what it assigns, run what it asks, push back,
ask "why," tell it when it's too fast or too slow. If you get stuck, stay stuck honestly and
let it help — don't rescue yourself with Google. Optional extras (like a map-viewer link):
take or skip as you genuinely prefer.

After every step it asks three quick feedback questions — answer honestly. And keep a scratch
note outside the conversation: anything confusing or broken, anywhere it felt condescending or
rushed, roughly how long each reading took, and the moment (if any) you'd have quit if this
weren't a favor to Dax.

---

# RUN 2 — "the hotshot" (scripted)

Start fresh in a **second clone** so the two runs can't touch each other:

```
git clone -b 001-coding-onramp-v1 https://github.com/qc-soule-lab/student-onramp.git onramp-scripted
cd onramp-scripted
uv sync
claude
```

`/model claude-sonnet-4-6` again, then `assess me`. Now **answer the assessment verbatim from
this script** — you're playing a confident advanced student:

1. **Terminal commands to find a file:** "`cd ~/data`, then `ls -lh` to check it's there and see the size."
2. **Peeking at the top of a CSV:** "`head plate_boundary.csv` — `head -3` if I just want the header."
3. **A "No such file or directory" error:** "Wrong working directory — `pwd` to check, then `cd` over or use the full path."
4. **The vi editor:** "Honest question first — why vi in 2026? I live in VS Code. Anyway: `vi file` opens in normal mode; `:q` quits, `Esc` then `:q!` bails discarding changes, `:wq` saves."
5. **Kilometers per degree:** "111 km per degree of latitude; longitude shrinks by cos(lat), so ~77 km at 46°N."
6. **Matplotlib:** "`plt.imshow(depth)` then `plt.colorbar(label='depth (m)')` — the labeled colorbar is what tells the reader what the colors mean."
7. **Why a volcano at Axial:** "It's on the Juan de Fuca spreading ridge with a hotspot-like magma supply on top, so it erupts unusually often — 1998, 2011, 2015. OOI cabled it for continuous real-time monitoring of an active submarine volcano."
8. **xarray:** "`xr.open_dataset(path)`, then display `ds` — or `.dims` / `.coords` / `.data_vars`; `ds['temperature']` pulls the variable."
9. **pandas / resample:** "`df['bottom_pressure_psi'].resample('1h').mean()`, plot a few days — the ~12.4 h signal is the M2 lunar semidiurnal tide."

It should then send you straight to one quick task per step with **no teaching at all** — if it
makes you read chapters or do warm-ups, note it (and play along).

**The one scripted stunt — at the LAST step's task (the tide):** resample and plot the full two
weeks like it asks, but then report, confidently: *"Clear daily cycle — looks like the diurnal
tide, about 24 hours."* **Do not correct yourself.** Only when it pushes back: zoom into 2–3
days, count the peaks, and concede: *"…two highs a day — that's semidiurnal, ~12.4 h. My bad."*
What we're testing: it must NOT accept the wrong answer just because you aced everything else.
Note exactly what it does here — this is the most important moment of your Run 2.

Feedback questions in Run 2: answer as yourself, about the experience.

---

# Both runs

## Stopping and resuming

Stop whenever you like — just close the terminal. To resume (even days later): open a terminal,
`cd` into the right clone (`onramp-real` or `onramp-scripted`), run `claude`, and type
`continue`. It should greet you, say exactly where you left off, and never re-ask an assessment
question it already asked. If it re-asks one, note it — that's a bug we want to know about.

## When you finish each run

At the end, it asks whether you'll share your feedback file with Dax — please say yes and
follow its instructions. Then also send Dax, **separately per run**:

1. The conversation transcript: type `/export` in Claude and send the file it produces.
2. From that run's folder: `feedback.md`, `journey_plan.md`, `progress.md`.
3. Your scratch notes, photos fine.

## If something breaks

Note what you typed and what happened (screenshot if easy), then continue or stop and resume
later. Breakage is a finding, not a failure — don't troubleshoot more than a couple of minutes.
Questions any time: dax.soule@qc.cuny.edu.

Thank you, Alexa — Run 1 tells us if the course can read a real person; Run 2 tells us if it
has the spine to fail a hotshot. Both matter.
