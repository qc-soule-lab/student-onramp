*AI-generated draft (Claude, Anthropic) — for review.*

# Probe p05 — find the tide  (coding · step 4 · skills: pandas_timeseries, resample_plot)

## Prompt (show to student)
You have a DataFrame `df` with a **datetime index** and a column `bp` (bottom pressure, hourly).
(a) How do you compute an hourly (or daily) **mean** with pandas `resample`?
(b) The data carries a **~12.4-hour oscillation**. How would you make it visible, and what *is* that signal?

## Answer key
- (a) `df['bp'].resample('1h').mean()` (already hourly) or `df['bp'].resample('1D').mean()` for daily — requires a `DatetimeIndex`.
- (b) **Plot a few days at hourly resolution** (`df['bp'].plot()`): you'll see ~two highs and two lows per day — the **M2 lunar semidiurnal tide** (~12.42 h). An FFT/periodogram of the detrended series confirms the dominant ~12.4 h peak.
- **Insight:** resampling to `'1D'` would *average the tide away* (Nyquist) — to *see* it you must keep sub-daily resolution.

## Hint ladder
- **R1:** `.resample()` acts on a datetime index — what frequency string is hourly? daily? And if you average to daily, what happens to a 12-hour wiggle?
- **R2:** `df['bp'].resample('1h').mean()`. To reveal a ~12 h cycle, plot a few days hourly and look for two highs/lows per day — that's a tide. `'1D'` erases it.
- **R3 (reveal):** the full key above, naming the **M2** tide.

## Scoring (→ rubric §3)
- `correct`: correct `resample` syntax **and** identifies the tidal / M2 ~12.4 h signal (bonus: the don't-daily-average insight).
- `partial`: resample right but doesn't name the tide, or names the tide without the syntax.
- `wrong`: neither.
