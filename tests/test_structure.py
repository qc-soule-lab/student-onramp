"""Structure & wiring guards for the v1 slice.

Enforces the contracts the runtime (CLAUDE.md) depends on, so a Sonnet session
can't hit a dangling reference or a non-woven step:
  - YAML parses; the slice has steps + a progression rule
  - the gate chain is a single linear unlock path covering every step once
  - Constitution VII: every step with coding has domain concepts AND chapters
  - cross-refs resolve: probes exist (+ have keys/ladders), chapters & readings resolve
Known-pending sources (not yet sourced) are tracked explicitly, not silently failed.
"""
from pathlib import Path
import re
import pytest
import yaml

ROOT = Path(__file__).resolve().parent.parent

# Sources deliberately not yet wired (see journey/readings.md "Pending / to source").
# vi is NOT pending: the book has no vi chapter, so vi is sourced externally as the
# reading `vi_ref` (Wikibooks, CC BY-SA) — skill_to_chapter.yml is book-only by design.
PENDING_CHAPTERS = set()              # no pending book chapters
PENDING_READINGS = {"tidal_nugget"}   # need a CC-licensed seafloor-tide reading


def _load(rel):
    return yaml.safe_load((ROOT / rel).read_text())


def _sourced_reading_keys(text):
    """Reading keys that are actually sourced: a `key` appearing on a line that also
    carries a URL. A key mentioned only in the TBD "Pending / to source" table (no
    link) is NOT sourced — that's what PENDING_READINGS tracks."""
    keys = set()
    for line in text.splitlines():
        if "http" in line:
            keys.update(re.findall(r"`([a-z0-9_]+)`", line))
    return keys


@pytest.fixture(scope="module")
def journey():
    return _load("journey/journey.yml")["slice"]


@pytest.fixture(scope="module")
def skill_map():
    return _load("skill_maps/slice_v1.yml")


@pytest.fixture(scope="module")
def chapters():
    return _load("content/skill_to_chapter.yml")["chapters"]


@pytest.fixture(scope="module")
def readings_text():
    return (ROOT / "journey/readings.md").read_text()


# --- basic shape -----------------------------------------------------------

def test_journey_parses_and_has_steps(journey):
    assert journey["steps"], "no steps in journey.yml"
    assert "progression" in journey and journey["progression"]["start_unlocked"]


# --- gate chain: single linear unlock path, every step once ---------------

def test_gate_chain_is_single_linear_path(journey):
    steps = {s["n"]: s for s in journey["steps"]}
    start = journey["progression"]["start_unlocked"]
    assert len(start) == 1, f"expect exactly one start-unlocked module, got {start}"
    cur, seen = start[0], []
    while True:
        assert cur in steps, f"unlock points at missing step {cur!r}"
        assert cur not in seen, f"cycle in gate chain at step {cur}"
        seen.append(cur)
        nxt = steps[cur]["gate"]["unlocks"]
        if nxt == "end":
            break
        cur = nxt
    assert set(seen) == set(steps), (
        f"gate chain {seen} does not cover all steps {sorted(steps)} exactly once"
    )


# --- Constitution VII: coding is woven, never free-floating ---------------

def test_every_coding_step_is_woven(journey):
    for s in journey["steps"]:
        if s.get("coding_skills"):
            assert s.get("domain", {}).get("concepts"), (
                f"step {s['n']} teaches coding with no domain concept (Constitution VII)"
            )
            assert s.get("chapters"), (
                f"step {s['n']} teaches coding with no book chapter (Constitution VII)"
            )


# --- cross-refs: probes exist and are well-formed -------------------------

def _referenced_probes(journey, skill_map):
    ids = set()
    for s in journey["steps"]:
        ids.update(s.get("probes", []))
    for group in ("domain", "coding"):
        for comp in skill_map.get(group, []):
            ids.update(comp.get("probes", []))
    return ids


def test_referenced_probes_exist_and_have_sections(journey, skill_map):
    required = ["## Prompt", "## Answer key", "## Hint ladder", "## Scoring"]
    for pid in sorted(_referenced_probes(journey, skill_map)):
        f = ROOT / "assessment/probes" / f"{pid}.md"
        assert f.exists(), f"probe referenced but missing: {pid}.md"
        txt = f.read_text()
        for sec in required:
            assert sec in txt, f"{pid}.md missing section {sec!r}"
        for rung in ("R1", "R2", "R3"):
            assert rung in txt, f"{pid}.md missing hint-ladder rung {rung}"


def test_every_competency_has_a_probe(skill_map):
    for group in ("domain", "coding"):
        for comp in skill_map.get(group, []):
            assert comp.get("probes"), f"competency {comp['id']} has no probe"


# --- cross-refs: chapters & readings resolve (or are tracked-pending) ------

def test_chapters_resolve_or_pending(journey, skill_map, chapters):
    keys = set()
    for s in journey["steps"]:
        keys.update(s.get("chapters", []))
    for comp in skill_map.get("coding", []):
        if comp.get("chapter"):
            keys.add(comp["chapter"])
    for k in sorted(keys):
        assert k in chapters or k in PENDING_CHAPTERS, (
            f"chapter key {k!r} not in skill_to_chapter.yml and not tracked-pending"
        )


def test_readings_resolve_or_pending(journey, skill_map, readings_text):
    keys = set()
    for s in journey["steps"]:
        keys.update(s.get("readings", []))
        keys.update(s.get("enrichment", []))
    for comp in skill_map.get("coding", []):       # e.g. vi_basics -> reading: vi_ref
        if comp.get("reading"):
            keys.add(comp["reading"])
    for k in sorted(keys):
        assert f"`{k}`" in readings_text or k in PENDING_READINGS, (
            f"reading/enrichment key {k!r} not defined in readings.md and not tracked-pending"
        )


@pytest.mark.xfail(reason="tidal_nugget still awaiting a CC-licensed link", strict=False)
def test_pending_sources_resolved(readings_text):
    """Canary: XPASSes once every pending reading carries a real URL — the cue to
    drop it from PENDING_READINGS. vi_ref already graduated (it has a link)."""
    sourced = _sourced_reading_keys(readings_text)
    assert all(k in sourced for k in PENDING_READINGS), (
        f"still unsourced: {sorted(PENDING_READINGS - sourced)}"
    )


# --- privacy + templates: generated student files stay local --------------

def test_local_student_files_gitignored():
    """Constitution II — every generated per-student file must be gitignored."""
    gi = (ROOT / ".gitignore").read_text()
    for f in ("journey_plan.md", "progress.md", "feedback.md", "misconceptions.md"):
        assert f in gi, f"{f} must be gitignored (Constitution II — student data stays local)"


def test_generated_artifact_templates_exist():
    for t in ("journey_plan", "progress", "feedback", "misconceptions"):
        assert (ROOT / "templates" / f"{t}.template.md").exists(), f"missing template: {t}.template.md"


# --- Theme 1: step 0 builds terminal comfort ------------------------------

def test_step0_shell_warmup_wired(journey):
    step0 = next(s for s in journey["steps"] if s["n"] == 0)
    assert step0.get("warmup"), "step 0 must name a shell warm-up (Theme 1: Unix comfort)"
    assert (ROOT / "content" / f"{step0['warmup']}.md").exists(), "shell_warmup content file missing"
    assert (ROOT / "content" / "terminal_survival_card.md").exists(), "terminal survival card missing"
