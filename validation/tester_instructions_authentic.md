*Drafted with Claude (Anthropic) for Dr. Soule's lab — reviewed by Dax Soule.*

# Onramp test instructions — third run (the real one)

Hi Alexa! You're the third tester of the lab's new onboarding course — and unlike the first
two, **you have no script**. Rose and Neftali played scripted roles; your job is to take the
course as yourself, honestly. You're the first genuinely real student through it.

**The big idea:** the course starts with a short assessment and then builds a personalized
path — skipping what you already know, teaching what you don't. We're testing whether it reads
a *real person* correctly. So the only rule is: **be honest**. "I don't know" is a perfectly
good answer; guessing is fine too (say it's a guess). Don't study or look anything up first —
the course meeting you exactly where you are is the whole experiment.

**Time:** depends on where it places you — anywhere from 2 hours to most of a day. **You do
not need to do it in one sitting** — stopping and resuming is itself a feature we're testing
(see section 5).

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

## 2. The assessment and the course — just be you

Answer the assessment questions with whatever you actually know. Then work the course it
builds for you: read what it asks you to read, run what it asks you to run, ask it questions
when you're confused (really — push back, ask "why," tell it when it's going too fast or too
slow; how it handles that is part of the test).

If you get stuck somewhere, stay stuck honestly and let it help you — don't rescue yourself
with Google. If it offers an optional extra (like a map-viewer link), take it or skip it as
you genuinely prefer.

## 3. The feedback questions

After every step it asks three quick questions (difficulty / friction / keep-or-cut). Answer
honestly — these notes are the most valuable thing you produce.

## 4. Take notes outside the conversation too

Keep a scratch note (paper is fine) of: anything confusing or broken, anywhere you waited too
long, anywhere it felt condescending or too fast or too slow, roughly how long each reading
actually took you, and the moment (if any) you'd have quit if this weren't a favor to Dax.

## 5. Stopping and resuming

Stop whenever you like — just close the terminal. To resume (even days later): open a
terminal, `cd student-onramp`, run `claude`, and type `resume`. It should greet you, tell
you exactly where you left off, and never re-ask an assessment question it already asked. If
it does re-ask one, note it — that's a bug we want to know about.

## 6. When you finish

At the end, Claude will ask whether you're willing to share your feedback file with Dax —
please say yes and follow its instructions. Then also send Dax:

1. The conversation transcript: type `/export` in Claude and send the file it produces.
2. From your `student-onramp` folder: `feedback.md`, `journey_plan.md`, `progress.md`
   (these exist only on your seat — nothing is shared unless you send it).
3. Your scratch notes from section 4, photos fine.

## 7. If something breaks

Note what you typed and what happened (screenshot if easy), then either ask Claude to continue
or stop and resume later. Breakage is a finding, not a failure — don't troubleshoot for more
than a couple of minutes. Questions any time: dax.soule@qc.cuny.edu.

Thank you, Alexa — Rose and Neftali tested the machinery; you're testing the real thing.
