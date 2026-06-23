*AI-generated draft (Claude, Anthropic) — for review.*

# Probe p01 — meters per degree  (domain · step 1 · skills: latitude_longitude, earth_topography)

## Prompt (show to student)
Axial Seamount is near **46°N, 130°W**.
(a) Roughly how many kilometers is **1° of latitude**?
(b) At 46°N, is **1° of longitude** longer, shorter, or the same in km as 1° of latitude — and why?

## Answer key
- (a) **~111 km** per degree of latitude (Earth's circumference ≈ 40,000 km ÷ 360°).
- (b) **Shorter.** Meridians converge toward the poles, so 1° of longitude ≈ `111 × cos(latitude)` km ≈ `111 × cos(46°)` ≈ **77 km**.

## Hint ladder (walk one rung at a time — never skip to R3)
- **R1 (guiding question):** Earth's circumference is ~40,000 km. How many degrees take you all the way around? What does that make one degree?
- **R2 (hint):** Latitude lines stay parallel (so a degree of latitude is ~constant length), but meridians converge toward the poles — so a degree of longitude shrinks as you go north. One trig function captures "full length at the equator, zero at the pole" — which one scales the longitude distance?
- **R3 (reveal):** 1° lat = 40000/360 ≈ **111 km**. 1° lon at 46°N = 111 × cos(46°) ≈ **77 km** → shorter.

## Scoring (→ rubric §3)
- `correct`: both (a) ≈ 111 km **and** (b) shorter with the convergence/cos reason.
- `partial`: (a) right but (b) missing the reason; or (b) direction right without (a)/cos.
- `wrong`: neither.
**Anchor (Constitution III):** if 40,000/360 was handed over before they computed it, or cos(lat) before they reasoned the convergence, those parts were revealed — score per the after-reveal rule, not by the restatement.
