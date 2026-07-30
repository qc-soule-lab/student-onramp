"""Guards the Step-0-preflight server-size check (scripts/check_server_ram.py)."""

import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location(
    "check_server_ram", Path(__file__).resolve().parent.parent / "scripts" / "check_server_ram.py"
)
csr = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(csr)

GB = 2**30


def test_small_profiles_fail_and_say_respawn():
    for gb in (2, 4, 8):
        ok, msg = csr.verdict(gb * GB)
        assert ok is False
        assert "LARGE" in msg and "16 GB" in msg  # tells them where to go


def test_large_and_bigger_pass():
    for gb in (12, 16, 32):
        ok, _ = csr.verdict(gb * GB)
        assert ok is True


def test_uncapped_passes():
    assert csr.verdict(None)[0] is True  # 'max' / no cgroup limit


def test_cutoff_is_below_large():
    assert csr.MIN_GB < csr.LARGE_GB


def test_read_limit_parses(tmp_path):
    numeric = tmp_path / "memory.max"
    numeric.write_text("17179869184\n")  # 16 GiB
    assert csr.read_limit_bytes((str(numeric),)) == 17179869184

    unlimited = tmp_path / "memory.max.unl"
    unlimited.write_text("max\n")  # cgroup-v2 unlimited
    assert csr.read_limit_bytes((str(unlimited),)) is None

    sentinel = tmp_path / "memory.limit_in_bytes"
    sentinel.write_text("9223372036854771712\n")  # cgroup-v1 unlimited sentinel
    assert csr.read_limit_bytes((str(sentinel),)) is None

    assert csr.read_limit_bytes(("/no/such/path",)) is None
