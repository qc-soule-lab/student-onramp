*AI-generated draft (Claude, Anthropic) — for review.*

# Probe p02 — show the bathymetry  (coding · step 1 · skills: jupyter_basics, python_fundamentals, matplotlib_plot)

## Prompt (show to student)
You've loaded a 2-D NumPy array `depth` (rows = latitude, columns = longitude) of seafloor depths.
Write the matplotlib code to **display it as an image with a colorbar**, and say how you'd make clear *what the colors mean*.

## Answer key
```python
import matplotlib.pyplot as plt
plt.imshow(depth)                 # or plt.pcolormesh(lon, lat, depth) if you have coord arrays
plt.colorbar(label="depth (m)")   # the label tells the reader what the colors encode
plt.xlabel("longitude index"); plt.ylabel("latitude index")
plt.title("Axial bathymetry")
plt.show()
```
Key idea: `imshow`/`pcolormesh` renders the grid; `colorbar` + a units label communicate the depth scale.

## Hint ladder
- **R1:** What matplotlib function turns a 2-D array into an image? And what adds the scale bar on the side?
- **R2:** matplotlib has one function that renders a 2-D array as an image, and a separate call that adds the scale strip beside it (give it a label so the reader knows what the colors mean). Both are in the numpy_and_matplotlib chapter — what are they?
- **R3 (reveal):** the snippet above.

## Scoring (→ rubric §3)
- `correct`: `imshow`/`pcolormesh` **and** a `colorbar` **and** a units/label.
- `partial`: image shown but no colorbar, or colorbar with no label/units.
- `wrong`: can't produce the image.
**Anchor (Constitution III):** code assembled only after the full snippet (or `imshow`+`colorbar` named outright) was shown scores `wrong`, depth 2 — comprehension questions after a reveal are teaching, not assessment.
