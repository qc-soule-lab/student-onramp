*Drafted with Claude (Anthropic) for Dr. Soule's lab — reviewed by Dax Soule.*

# Onramp test instructions — the stop-and-go run

Hi Michelle! You're the fourth tester of the lab's new onboarding course, and yours is the most
realistic mission of all: **take the course as yourself, but in deliberately scattered
sittings** — the way a real student with classes, a job, and a life actually would.

**The big idea:** the course saves your progress and is supposed to pick up exactly where you
left off, even weeks later, never re-asking what it already asked. Other testers are allowed
to stop and resume; your job is to **stress it**: stop at awkward moments, walk away for days,
come back, and tell us whether the pickup felt seamless or clumsy. Beyond that — just be
honest. "I don't know" is a perfectly good answer; don't study or google anything first.

**Time:** 2 hours to most of a day of total work, depending on where it places you — spread
over **at least three sittings on at least three different days** (more is better).

## 0. Before you start — one short email (important!)

Before you run anything, email Dax 3–5 honest lines about where you'd place yourself:

- Terminal/command line: never used / some / comfortable?
- Python: none / a course / use it regularly? (matplotlib? pandas? xarray?)
- The vi editor: ever used it?
- Marine geology / plate tectonics: how much background?

This is sealed ground truth — afterward we compare where the course *placed* you against where
you *said* you were.

## 1. Setup (about 15 min, JupyterLab terminal)

```
git clone -b 001-coding-onramp-v1 https://github.com/qc-soule-lab/student-onramp.git
cd student-onramp
uv sync
claude
```

Inside Claude, type `/model claude-sonnet-4-6` (important — if your seat doesn't offer it,
stop and tell Dax). Then type:

```
assess me
```

When it asks your name: first name or anonymous, your choice — everything personal stays in
your local copy (never uploaded, never committed).

## 2. The stop-and-go protocol

**Sitting 1 — quit mid-assessment.** Start the assessment and answer honestly… then, when
you're roughly halfway through the questions (4 or 5 in), **just close the terminal**. Mid-flow,
no goodbye, even though it feels rude. That's the test.

**Wait at least one day.**

**Sitting 2 — resume, then quit mid-step.** Open a terminal, `cd student-onramp`, run
`claude`, type `resume`. *Before you scroll on, jot down:* did it greet you and say exactly
where you left off? Did it resume at the right question — **without re-asking anything you
already answered**? Then keep working normally. Once you're in the middle of a course step —
ideally after it's taught you something but **before** you've done that step's final task —
close the terminal again, mid-flow.

**Wait at least two days** (longer is even better — the course should offer you an optional
refresher if you've been gone a while; note whether it does, and whether it felt optional).

**Sitting 3 (and beyond) — resume and finish.** Same drill: `continue`, jot down whether the
pickup was accurate, then work to the end. Split further if life intervenes — every extra
stop is extra data.

**At every resume, note:** Did it know where you were? Did it repeat anything? Did it lose
anything (something you did that it forgot)? Did the re-entry feel welcoming or disorienting?

## 3. During the course — just be you

Work the course honestly: read what it assigns, run what it asks, push back, ask "why," tell
it when it's too fast or too slow. If you get stuck, stay stuck honestly and let it help you —
no Google. Optional extras (like a map-viewer link): take or skip as you genuinely prefer.

After every step it asks three quick feedback questions (difficulty / friction / keep-or-cut)
— answer honestly. These notes, plus your resume notes, are the most valuable thing you produce.

## 4. Scratch notes outside the conversation

Keep a running note (paper is fine): the awkward-stop moments and what happened at each
resume; anything confusing or broken; how long each reading actually took; anywhere it felt
condescending or rushed; the moment (if any) you'd have quit if this weren't a favor to Dax.

## 5. When you finish

At the end, it asks whether you'll share your feedback file with Dax — please say yes and
follow its instructions. Then also send Dax:

1. The conversation transcript: type `/export` in Claude and send the file it produces.
2. From your `student-onramp` folder: `feedback.md`, `journey_plan.md`, `progress.md`.
3. Your scratch notes — especially the resume notes — photos fine.

## 6. If something breaks

Note what you typed and what happened (screenshot if easy), then continue or stop and resume
later — for you, even a crash is on-mission. Don't troubleshoot more than a couple of minutes.
Questions any time: dax.soule@qc.cuny.edu.

Thank you, Michelle — nobody finishes a course like this in one sitting in real life. You're
testing the version of it that real life gets.
