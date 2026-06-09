"""Verify every book-chapter path in skill_to_chapter.yml resolves in the mirror.

Fetches the book repo tree ONCE (via `gh api`) and checks membership — no per-path
hammering. Skips cleanly when gh/network is unavailable (e.g. offline CI), so this
never blocks structure validation; it's a freshness guard, not a hard gate.
"""
from pathlib import Path
import json
import shutil
import subprocess
import pytest
import yaml

ROOT = Path(__file__).resolve().parent.parent
S2C = yaml.safe_load((ROOT / "content/skill_to_chapter.yml").read_text())
BOOK = S2C["book"]
CHAPTERS = S2C["chapters"]


def _chapter_paths():
    paths = set()
    for ch in CHAPTERS.values():
        if ch.get("path"):
            paths.add(ch["path"])
        if ch.get("assignment"):
            paths.add(ch["assignment"])
        for p in ch.get("also", []):
            paths.add(p)
    return paths


@pytest.fixture(scope="module")
def mirror_paths():
    if shutil.which("gh") is None:
        pytest.skip("gh CLI not available — skipping book-link freshness check")
    repo, branch = BOOK["repo"], BOOK["branch"]
    try:
        out = subprocess.run(
            ["gh", "api", f"/repos/{repo}/git/trees/{branch}?recursive=1"],
            capture_output=True, text=True, timeout=30,
        )
    except (subprocess.TimeoutExpired, OSError):
        pytest.skip("could not reach GitHub — skipping book-link freshness check")
    if out.returncode != 0:
        pytest.skip(f"gh api failed ({out.returncode}) — skipping book-link check")
    tree = json.loads(out.stdout).get("tree", [])
    return {node["path"] for node in tree}


def test_all_chapter_paths_resolve(mirror_paths):
    missing = sorted(p for p in _chapter_paths() if p not in mirror_paths)
    assert not missing, f"book paths not found in {BOOK['repo']}@{BOOK['branch']}: {missing}"
