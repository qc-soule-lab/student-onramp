"""Server-size preflight for the onramp — is the student on the Large (16 GB) profile?

Students pick their JupyterHub server profile at spawn and forget; on a Small profile the
data steps (xarray open + matplotlib) OOM-restart the kernel — the recurring hang a real
student hit (feedback H5). This reads the container's cgroup memory limit and tells the
student to respawn on Large if they're under the cutoff.

Large = 16 GB (lab profile); cutoff = 12 GB (comfortably below 16, above any smaller profile).
Assumes the Hub sets a per-server cgroup mem limit (KubeSpawner mem_limit) — the usual case;
an unconstrained/dev container reads a huge limit and passes.

  uv run python scripts/check_server_ram.py   # exit 0 = OK, 1 = respawn on Large
"""

from __future__ import annotations

import sys
from pathlib import Path

CGROUP_V2 = "/sys/fs/cgroup/memory.max"
CGROUP_V1 = "/sys/fs/cgroup/memory/memory.limit_in_bytes"
LARGE_GB = 16
MIN_GB = 12.0  # below this => not on Large
_UNCAPPED = 2**62  # cgroup "unlimited" sentinels sit at ~2**63


def read_limit_bytes(paths: tuple[str, ...] = (CGROUP_V2, CGROUP_V1)) -> int | None:
    """Container memory limit in bytes, or None if there's no explicit cap ('max'/unlimited)."""
    for p in paths:
        try:
            v = Path(p).read_text().strip()
        except OSError:
            continue
        if v.isdigit():
            b = int(v)
            return None if b >= _UNCAPPED else b
        return None  # cgroup-v2 "max" (unlimited)
    return None


def verdict(limit_bytes: int | None) -> tuple[bool, str]:
    """(ok, message) for a given cgroup limit. ok=False means: respawn on Large."""
    if limit_bytes is None:
        return True, "No per-server memory cap detected — proceeding."
    gb = limit_bytes / 2**30
    if gb >= 64:
        return True, f"Server memory ~{gb:.0f} GB (no small-profile cap) — good to go."
    if gb >= MIN_GB:
        return True, f"Server memory ~{gb:.0f} GB — Large profile, good to go."
    return False, (
        f"⚠ This server has only ~{gb:.1f} GB of memory — that's a SMALL profile.\n"
        f"The data steps (xarray/matplotlib) will hang or crash the kernel here.\n"
        f"Fix it before we start: save your work, then File → Hub Control Panel → "
        f"Stop My Server, and respawn on the LARGE ({LARGE_GB} GB) profile.\n"
        f"Then relaunch Claude here and say 'continue'."
    )


def main() -> None:
    ok, msg = verdict(read_limit_bytes())
    print(msg)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
