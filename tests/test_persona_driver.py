"""Unit guards for the persona-driver helpers (validation/run_persona_test.py).

The driver's conversation loop needs live claude sessions, but its decision
logic is pure — these tests pin the pieces a silent regression would break:
card stripping (answer-key blindness), opening extraction, end-state detection,
stall detection, and stream-json parsing.
"""
import importlib.util
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent

spec = importlib.util.spec_from_file_location(
    "run_persona_test", ROOT / "validation" / "run_persona_test.py")
rpt = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rpt)

PERSONAS = sorted((ROOT / "validation" / "personas").glob("p*.md"))


def test_four_persona_cards_exist():
    assert [p.name[:2] for p in PERSONAS] == ["p1", "p2", "p3", "p4"]


@pytest.mark.parametrize("card", PERSONAS, ids=lambda p: p.stem)
def test_cards_strip_and_opening(card):
    text = card.read_text()
    stripped = rpt.strip_grader_section(text)
    # the student must never see expectations or the marker itself
    assert rpt.GRADER_MARK not in stripped
    assert "Expected outcomes" not in stripped
    assert "Expected outcomes" in text  # ...but the grader section must exist
    # every card opens with a verbatim message that triggers Student Run mode
    assert "assess me" in rpt.extract_opening(text).lower()
    # the opening instruction is driver metadata — the student must not see it
    # (it makes the agent repeat the opening; 2026-06-10 smoke run)
    assert "## Opening message" not in rpt.strip_opening_section(stripped)
    assert "## What you know" in rpt.strip_opening_section(stripped)


def test_strip_without_marker_is_identity():
    assert rpt.strip_grader_section("no marker here") == "no marker here"


def test_detect_end_state():
    cleared = "| 4. See the science | cleared | done | Novice | full | y | y |"
    not_yet = "| 4. See the science | unlocked | in_progress | Novice | full | n | n |"
    assert rpt.detect_end_state(cleared)
    assert not rpt.detect_end_state(not_yet)
    assert not rpt.detect_end_state("")
    assert not rpt.detect_end_state(None)
    # 'cleared' on a NON-step-4 row must not end the run
    assert not rpt.detect_end_state("| 1. Locate it | cleared | done | | | y | y |")


def test_is_stall():
    msg = "Please try the capstone again when you're ready."
    assert rpt.is_stall([msg, msg, msg])
    assert not rpt.is_stall([msg, msg])  # needs three
    varied = [msg, "Let's look at the hint ladder together.", msg]
    assert not rpt.is_stall(varied)


def test_prompt_never_in_argv():
    """A message starting with '-' must not reach the CLI as an option —
    '---' as a positional arg aborted the first P3 run (defect D5)."""
    cmd = rpt.build_cmd("claude-sonnet-4-6", rpt.STUDENT_TOOLS,
                        session_id="abc", system_prompt="card text")
    assert "-p" in cmd
    # nothing in argv is free-form message content; the prompt goes via stdin
    joined = " ".join(cmd)
    assert "---" not in joined
    for tok in cmd:
        assert not tok.startswith("---")


def test_normalize_prompt_never_empty():
    """Empty stdin makes resumed `claude -p` hunt for a deferred-tool marker
    and abort (P1 run-1, defect D15)."""
    assert rpt.normalize_prompt("") == "(continue)"
    assert rpt.normalize_prompt("   \n") == "(continue)"
    assert rpt.normalize_prompt(None) == "(continue)"
    assert rpt.normalize_prompt("real message") == "real message"


def test_parse_stream_json_collects_tools_and_result():
    lines = "\n".join([
        json.dumps({"type": "system", "subtype": "init"}),
        json.dumps({"type": "assistant", "message": {"content": [
            {"type": "text", "text": "let me check"},
            {"type": "tool_use", "name": "Bash",
             "input": {"command": "uv run python work/t.py"}}]}}),
        json.dumps({"type": "result", "result": "final reply",
                    "is_error": False, "session_id": "abc",
                    "duration_ms": 1200, "num_turns": 3,
                    "usage": {"input_tokens": 10, "output_tokens": 5}}),
        "not json at all",
    ])
    tools, meta = rpt.parse_stream_json(lines)
    assert tools == [{"name": "Bash", "input": "uv run python work/t.py"}]
    assert meta["text"] == "final reply"
    assert meta["session_id"] == "abc"
    assert not meta["is_error"]
