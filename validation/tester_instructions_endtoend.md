*Drafted with Claude (Anthropic) for Dr. Soule's lab — reviewed by Dax Soule.*

# Onboarding test instructions — the full pipeline

Hi Makayla! You're testing something none of the other testers have touched: **the entire
onboarding pipeline, end to end** — the guided environment setup AND the science course that
follows it. You're our most experienced student, which makes you perfect for this: you'll
notice things a newcomer would silently suffer through.

**Your mission has two parts, in order. Throughout both: you have no script — be yourself,
answer honestly, and write down every rough edge.**

**Time:** Part A maybe 30–60 min (much of your environment already exists — that's part of the
test); Part B 2 hours to half a day depending on where it places you. Multiple sittings are
fine everywhere.

## Part A — the guided environment setup (the "orientation")

Even though your environment is already set up, run the guided orientation as if you were new.
**What we're testing:** does the guide handle a partially-configured seat gracefully — verifying
what exists instead of breaking on it — and do every step's instructions match what your screen
actually shows?

1. In a JupyterHub terminal:
   ```bash
   cd ~ && git clone https://github.com/qc-soule-lab/onboard-makayla-joseph.git
   cd onboard-makayla-joseph
   claude
   ```
   (If the clone says the folder already exists, `cd` into it and run `git pull` instead.)
2. Type exactly: **`Onboard me — read ORIENTATION.md and walk me through it one step at a time.`**
3. Follow it honestly. Where something already exists on your seat (your thesis repo, your
   Azure credential, SpecKit), let the guide discover that and watch what it does — smooth
   verification = pass; confusion, re-installation, or anything scary-looking = a finding.
   **Exception:** if it wants to overwrite your existing Azure credential file
   (`~/.azure/scaleworm-makayla.env`), stop it and note that — your current SAS works and
   should be left alone.
4. **Note the clock time** each step takes and anywhere the instructions don't match reality
   (wrong menu names, missing commands, steps that assume things you don't have).
5. The orientation ends by handing you into the science course — that handoff working smoothly
   is itself under test. Follow it straight into Part B.

## Part B — the onramp course, as yourself

### Before you start — one short email (important!)
Email Dax 3–5 honest lines on where you'd place yourself: terminal comfort? Python
(matplotlib/pandas/xarray)? vi? Marine geology background? This is sealed ground truth — we
compare where the course *places* you against where you *said* you were. Send it before
starting.

### The run
The orientation's last step gives you the commands (clone the course, `uv sync`, `claude`,
`/model claude-sonnet-4-6`, then `assess me`). From there:

- **Answer the assessment with what you actually know.** "I don't know" is a great answer;
  don't look things up. Given your experience, the course should *skip a lot for you* — if it
  teaches you things you plainly already know, that's a finding (note it, play along).
- Work the course honestly: run what it asks, push back when it's too slow or too fast, stay
  stuck honestly if you get stuck.
- After every step it asks three quick feedback questions — answer as yourself; you can also
  flag anything mid-activity at any moment, and it should log it without losing your place.
- Stop whenever you like; resume with `claude` + `continue` in the course folder. It should
  greet you, say exactly where you left off, and never re-ask an answered question.

## When you finish

Say yes when it asks to share your feedback with Dax, then send him:
1. Transcripts from BOTH parts (`/export` in each Claude session).
2. From the course folder: `feedback.md`, `journey_plan.md`, `progress.md`.
3. Your Part-A notes — step timings and every mismatch between instructions and reality.

## If something breaks

Note what you typed and what happened (screenshot if easy), then continue or resume later.
Breakage is a finding, not a failure — don't troubleshoot more than a couple of minutes.
Questions any time: dax.soule@qc.cuny.edu.

Thank you, Makayla — the others tested the course; you're testing the whole front door.
