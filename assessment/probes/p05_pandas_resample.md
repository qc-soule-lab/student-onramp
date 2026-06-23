*AI-generated draft (Claude, Anthropic) — for review.*

# Probe p05 — find the tide  (coding · step 4 · skills: pandas_timeseries, resample_plot)

## Prompt (show to student)
You load `data/axial_botpt_2015-01.parquet` (`df = pd.read_parquet(...)`) — a **datetime index** and a column `bottom_pressure_psi` (1-minute samples).
(a) How do you compute an hourly (or daily) **mean** with pandas `resample`?
(b) The data carries a **~12.4-hour oscillation**. How would you make it visible, and what *is* that signal?

## Answer key
- (a) `df['bottom_pressure_psi'].resample('1h').mean()` (or `'1D'` for daily) — requires a `DatetimeIndex` (this file has one).
- (b) **Plot a few days at hourly resolution** (`df['bottom_pressure_psi'].resample('1h').mean().plot()`): you'll see ~two highs and two lows per day — the **M2 lunar semidiurnal tide** (~12.42 h, ~4 psi peak-to-peak here). An FFT/periodogram of the detrended series confirms the dominant ~12.4 h peak.
- **Insight:** resampling to `'1D'` would *average the tide away* (Nyquist) — to *see* it you must keep sub-daily resolution.

## Hint ladder
- **R1:** `.resample()` acts on a datetime index — what frequency string is hourly? daily? And if you average to daily, what happens to a 12-hour wiggle?
- **R2:** pandas has a method that re-bins a datetime-indexed series to a new frequency (you give it a frequency string — hourly vs daily — then aggregate, e.g. a mean). To *see* a ~12 h wiggle you must keep sub-daily resolution and plot a few days; averaging to daily erases it. What's the method, and which frequency keeps the tide visible?
- **R3 (reveal):** the full key above, naming the **M2** tide.

## Scoring (→ rubric §3)
- `correct`: correct `resample` syntax **and** identifies the tidal / M2 ~12.4 h signal (bonus: the don't-daily-average insight).
- `partial`: resample right but doesn't name the tide, or names the tide without the syntax.
- `wrong`: neither.
**Anchor (Constitution III):** the resample syntax or the tide identification produced only after R2/R3 spelled them out scores per the after-reveal rule — an unaided tidal ID with hinted syntax is `partial`, not `correct`.

**Intro-tool fast-path:** pandas is taught *after* the assessment — if the student says they've **never used pandas**, record **Novice** (full scaffold) and skip the ladder; only run the task + ladder if they've used it before.
