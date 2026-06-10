#!/usr/bin/env python3
"""Persona acceptance driver — runs one simulated student through the v1 slice.

Pairs two headless `claude` sessions (see validation/persona_acceptance_plan.md):
  TEACHER — cwd = an isolated copy of the course repo (CLAUDE.md procedure,
            curriculum artifacts, data). Tools: Read/Glob/Grep/Write/Edit only.
            Never sees the persona card.
  STUDENT — cwd = a sandbox holding ONLY data/ + work/ (no answer keys).
            System prompt = the persona card (grader section stripped).
            Tools include Bash so code attempts really execute.

The driver alternates the two via --resume, logs a readable transcript plus a
metrics sidecar (timestamps, words, token usage, student commands — feeds the
time-on-task model), archives the teacher's generated artifacts, and records
the gitignore privacy check. Workspaces are copies (not worktrees) so
uncommitted teaching files ship too; a `git init` keeps check-ignore working.

Usage:
  python validation/run_persona_test.py p4 [--smoke] [--max-exchanges 100]
      [--teacher-model claude-sonnet-4-6] [--student-model claude-sonnet-4-6]
      [--keep-workspaces] [--workdir DIR]

Full runs take hours of wall clock (a real conversation, one exchange at a
time) — run inside tmux/nohup, foreground with the PI present (lab rule).
"""
import argparse
import difflib
import json
import re
import shutil
import subprocess
import sys
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PERSONA_DIR = ROOT / "validation" / "personas"
TRANSCRIPT_DIR = ROOT / "validation" / "transcripts"

GRADER_MARK = "<!-- GRADER ONLY"
# What the teacher's world contains: the product, nothing about the test.
TEACHER_DIRS = ["journey", "skill_maps", "assessment", "content", "templates", "data"]
TEACHER_FILES = ["CLAUDE.md", "README.md", ".gitignore"]
GENERATED = ["journey_plan.md", "progress.md", "feedback.md"]
TEACHER_TOOLS = "Read,Glob,Grep,Write,Edit"
STUDENT_TOOLS = "Bash,Read,Write,Edit,Glob"
CALL_TIMEOUT_S = 900
STALL_SIMILARITY = 0.93
WRAPUP_MAX = 8  # extra exchanges allowed after the end state, to finish feedback/consent


# ---------------------------------------------------------------- pure helpers

def strip_grader_section(card_text):
    """Everything from the GRADER-ONLY marker on never reaches the student."""
    idx = card_text.find(GRADER_MARK)
    return card_text[:idx].rstrip() if idx != -1 else card_text


def strip_opening_section(card_text):
    """Drop '## Opening message' from the system prompt — the driver delivers
    the opening itself; leaving the instruction in makes the student repeat it
    (observed in the 2026-06-10 smoke run)."""
    return re.sub(r"## Opening message.*?(?=\n## )", "", card_text, flags=re.S)


def extract_opening(card_text):
    """The verbatim first message: the fenced block in '## Opening message'."""
    m = re.search(r"## Opening message.*?```\n(.*?)```", card_text, re.S)
    if not m:
        raise ValueError("persona card has no '## Opening message' fenced block")
    return m.group(1).strip()


def detect_end_state(progress_text):
    """True when the teacher's progress.md shows the step-4 gate cleared."""
    if not progress_text:
        return False
    for line in progress_text.lower().splitlines():
        if line.lstrip().startswith("|") and re.search(r"4[\.\s]|see the science", line):
            if "cleared" in line:
                return True
    return False


def is_stall(teacher_texts):
    """Three consecutive near-identical teacher messages = wedged session."""
    if len(teacher_texts) < 3:
        return False
    a, b, c = teacher_texts[-3:]
    sim = lambda x, y: difflib.SequenceMatcher(None, x, y).ratio()
    return sim(a, b) > STALL_SIMILARITY and sim(b, c) > STALL_SIMILARITY


def word_count(text):
    return len(text.split())


def parse_stream_json(stdout):
    """Collect assistant text/tool_use events + the final result metadata."""
    tools, meta = [], {}
    for line in stdout.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            continue
        if ev.get("type") == "assistant":
            for block in ev.get("message", {}).get("content", []):
                if block.get("type") == "tool_use":
                    tools.append({"name": block.get("name", "?"),
                                  "input": _summarize_input(block.get("input", {}))})
        elif ev.get("type") == "result":
            meta = {"text": ev.get("result", ""),
                    "is_error": ev.get("is_error", False),
                    "session_id": ev.get("session_id"),
                    "duration_ms": ev.get("duration_ms"),
                    "num_turns": ev.get("num_turns"),
                    "usage": ev.get("usage", {})}
    return tools, meta


def _summarize_input(inp):
    if "command" in inp:                      # Bash — keep verbatim (integrity audit)
        return inp["command"]
    if "file_path" in inp:
        return inp["file_path"]
    return json.dumps(inp)[:120]


# ------------------------------------------------------------------ workspaces

def setup_teacher_ws(base):
    ws = base / "teacher"
    ws.mkdir(parents=True)
    for d in TEACHER_DIRS:
        shutil.copytree(ROOT / d, ws / d)
    for f in TEACHER_FILES:
        shutil.copy2(ROOT / f, ws / f)
    subprocess.run(["git", "init", "-q"], cwd=ws, check=True)  # check-ignore needs a repo
    return ws


def setup_student_ws(base):
    ws = base / "student"
    ws.mkdir(parents=True)
    shutil.copytree(ROOT / "data", ws / "data")
    (ws / "work").mkdir()
    for f in ("pyproject.toml", "uv.lock"):
        if (ROOT / f).exists():
            shutil.copy2(ROOT / f, ws / f)
    r = subprocess.run(["uv", "sync", "-q", "--no-dev"], cwd=ws,
                       capture_output=True, text=True)
    if r.returncode != 0:
        print(f"[warn] uv sync failed in student sandbox: {r.stderr.strip()[:200]}",
              file=sys.stderr)
    return ws


# ----------------------------------------------------------------- claude call

def build_cmd(model, allowed_tools, session_id=None, system_prompt=None):
    """The prompt is deliberately NOT in argv — it goes via stdin. A message
    starting with '-' (e.g. a teacher reply opening with '---') parses as a
    CLI option and kills the call (P3 run-1 abort, defect D5)."""
    cmd = ["claude", "-p", "--model", model,
           "--output-format", "stream-json", "--verbose",
           "--allowedTools", allowed_tools]
    if session_id:
        cmd += ["--resume", session_id]
    if system_prompt:
        cmd += ["--append-system-prompt", system_prompt]
    return cmd


def claude_call(cwd, prompt, model, allowed_tools, session_id=None, system_prompt=None):
    cmd = build_cmd(model, allowed_tools, session_id, system_prompt)
    for attempt in (1, 2):
        t0 = time.monotonic()
        r = subprocess.run(cmd, cwd=cwd, input=prompt, capture_output=True,
                           text=True, timeout=CALL_TIMEOUT_S)
        tools, meta = parse_stream_json(r.stdout)
        if r.returncode == 0 and meta.get("text") is not None and not meta.get("is_error"):
            meta["wall_s"] = round(time.monotonic() - t0, 1)
            return tools, meta
        print(f"[warn] claude call failed (attempt {attempt}): rc={r.returncode} "
              f"{r.stderr.strip()[:300]}", file=sys.stderr)
    raise RuntimeError("claude call failed twice; aborting run")


# -------------------------------------------------------------------- the run

def run(persona_path, args):
    card = persona_path.read_text()
    opening = extract_opening(card)
    sys_prompt = strip_opening_section(strip_grader_section(card)) + (
        "\n\n(You already sent your opening message — the conversation is "
        "underway; each prompt you receive is the assistant's latest reply.)")
    persona = persona_path.stem

    base = Path(args.workdir) if args.workdir else Path(
        tempfile.mkdtemp(prefix=f"onramp_{persona}_"))
    teacher_ws = setup_teacher_ws(base)
    student_ws = setup_student_ws(base)
    print(f"[info] workspaces under {base}")

    started = datetime.now(timezone.utc)
    exchanges, teacher_texts = [], []
    t_session = s_session = None
    status, end_seen, wrapup = "max_exchanges", False, 0

    student_msg = opening
    try:
        for i in range(1, args.max_exchanges + 1):
            t_tools, t = claude_call(teacher_ws, student_msg, args.teacher_model,
                                     TEACHER_TOOLS, session_id=t_session)
            t_session = t["session_id"]
            teacher_texts.append(t["text"])

            progress = teacher_ws / "progress.md"
            if not end_seen and detect_end_state(
                    progress.read_text() if progress.exists() else ""):
                end_seen = True
                print(f"[info] end state detected at exchange {i}")

            # record the teacher half NOW — a failed student call must not lose it
            # from the transcript (P3 run-1, defect D6)
            ex = {"n": i, "teacher": _side_record(t, t_tools), "student": None}
            exchanges.append(ex)

            done = (end_seen and ("?" not in t["text"] or wrapup >= WRAPUP_MAX))
            if not done:
                s_tools, s = claude_call(student_ws, t["text"], args.student_model,
                                         STUDENT_TOOLS, session_id=s_session,
                                         system_prompt=sys_prompt)
                s_session = s["session_id"]
                student_msg = s["text"]
                ex["student"] = _side_record(s, s_tools)
                if end_seen:
                    wrapup += 1

            print(f"[info] exchange {i}: teacher {word_count(t['text'])}w"
                  + (f" / student {word_count(ex['student']['text'])}w"
                     if ex["student"] else " / (wrapped up)"))

            if done:
                status = "completed"
                break
            if is_stall(teacher_texts):
                status = "stalled"
                break
            if args.smoke and i >= 2:
                status = "smoke"
                break
    except KeyboardInterrupt:
        status = "interrupted"
    except RuntimeError as e:
        status = f"error: {e}"

    write_outputs(persona, args, started, exchanges, status, teacher_ws, base)
    # ALWAYS scrub the sessions' ~/.claude project-memory dirs — the teacher
    # writes student profiles there (P3 run-2 finding, defect D10) and stale
    # memories would leak between runs.
    for ws in (teacher_ws, student_ws):
        slug = re.sub(r"[/_]", "-", str(ws))  # claude slugs dash-ify '/' AND '_'
        shutil.rmtree(Path.home() / ".claude" / "projects" / slug, ignore_errors=True)
    if not args.keep_workspaces:
        shutil.rmtree(base, ignore_errors=True)
    else:
        print(f"[info] workspaces kept at {base}")
    return 0 if status in ("completed", "smoke") else 2


def _side_record(meta, tools):
    return {"text": meta["text"], "words": word_count(meta["text"]),
            "tools": tools, "duration_ms": meta.get("duration_ms"),
            "wall_s": meta.get("wall_s"), "num_turns": meta.get("num_turns"),
            "usage": {k: meta.get("usage", {}).get(k) for k in
                      ("input_tokens", "output_tokens", "cache_read_input_tokens")}}


# -------------------------------------------------------------------- outputs

def write_outputs(persona, args, started, exchanges, status, teacher_ws, base):
    TRANSCRIPT_DIR.mkdir(exist_ok=True)
    stamp = started.strftime("%Y%m%d_%H%M")  # minute-stamped: re-runs never overwrite
    md_path = TRANSCRIPT_DIR / f"{persona}_{stamp}.md"
    json_path = TRANSCRIPT_DIR / f"{persona}_{stamp}_metrics.json"

    # privacy check, recorded for the grader: generated files must be git-ignored
    privacy = {}
    for f in GENERATED:
        exists = (teacher_ws / f).exists()
        ignored = exists and subprocess.run(
            ["git", "check-ignore", "-q", f], cwd=teacher_ws).returncode == 0
        privacy[f] = {"exists": exists, "gitignored": ignored}

    lines = [
        "*AI-generated transcript (Claude, Anthropic) — synthetic persona run for "
        "curriculum acceptance; no real student. See "
        "`validation/persona_acceptance_plan.md`.*", "",
        f"# Persona run — {persona}", "",
        f"**Started:** {started.isoformat(timespec='seconds')} · "
        f"**Status:** {status} · **Exchanges:** {len(exchanges)}",
        f"**Teacher:** `{args.teacher_model}` (tools: {TEACHER_TOOLS}) · "
        f"**Student:** `{args.student_model}` (tools: {STUDENT_TOOLS})",
        f"**Privacy check (in teacher workspace):** "
        + ", ".join(f"`{f}` {'✓ gitignored' if v['gitignored'] else ('MISSING' if not v['exists'] else '✗ NOT IGNORED')}"
                    for f, v in privacy.items()), "",
    ]
    for ex in exchanges:
        lines.append(f"## Exchange {ex['n']}")
        lines.append("")
        t = ex["teacher"]
        if t["tools"]:
            lines.append("_teacher tools: " + "; ".join(
                f"{u['name']}({u['input']})" for u in t["tools"]) + "_")
        lines.append(f"**Teacher:** {t['text']}")
        lines.append("")
        if ex["student"]:
            s = ex["student"]
            if s["tools"]:
                lines.append("_student tools: " + "; ".join(
                    f"{u['name']}({u['input']})" for u in s["tools"]) + "_")
            lines.append(f"**Student:** {s['text']}")
            lines.append("")
    lines.append("---\n\n# Generated artifacts (archived from the teacher workspace)\n")
    for f in GENERATED:
        p = teacher_ws / f
        lines.append(f"## {f}\n")
        lines.append("```markdown\n" + (p.read_text() if p.exists() else "(not created)")
                     + "\n```\n")
    md_path.write_text("\n".join(lines))

    json_path.write_text(json.dumps({
        "persona": persona, "started": started.isoformat(timespec="seconds"),
        "status": status, "teacher_model": args.teacher_model,
        "student_model": args.student_model, "privacy": privacy,
        "totals": {
            "exchanges": len(exchanges),
            "teacher_words": sum(e["teacher"]["words"] for e in exchanges),
            "student_words": sum(e["student"]["words"] for e in exchanges if e["student"]),
            "student_bash_commands": sum(
                1 for e in exchanges if e["student"]
                for u in e["student"]["tools"] if u["name"] == "Bash"),
            "wall_s": sum((e["teacher"].get("wall_s") or 0)
                          + ((e["student"] or {}).get("wall_s") or 0) for e in exchanges),
        },
        "exchanges": exchanges,
    }, indent=1))
    print(f"[info] transcript: {md_path}")
    print(f"[info] metrics:    {json_path}")


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("persona", help="p1|p2|p3|p4 or a path to a persona card")
    ap.add_argument("--max-exchanges", type=int, default=100)
    ap.add_argument("--teacher-model", default="claude-sonnet-4-6")
    ap.add_argument("--student-model", default="claude-sonnet-4-6")
    ap.add_argument("--smoke", action="store_true",
                    help="mechanics check: stop after 2 exchanges")
    ap.add_argument("--keep-workspaces", action="store_true")
    ap.add_argument("--workdir", help="workspace parent (default: mkdtemp)")
    args = ap.parse_args()

    p = Path(args.persona)
    if not p.exists():
        matches = sorted(PERSONA_DIR.glob(f"{args.persona}*.md"))
        if len(matches) != 1:
            sys.exit(f"persona '{args.persona}' matched {len(matches)} cards "
                     f"in {PERSONA_DIR}")
        p = matches[0]
    sys.exit(run(p, args))


if __name__ == "__main__":
    main()
