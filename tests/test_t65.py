"""T65: the sealed runner's start from a slab with a hand-opened patch (2026-10-15)."""
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from exact_t54_patch import patch, tie_table                     # noqa: E402
from run_sealed_curled_d import start_of                          # noqa: E402
from graphity.cqg_d import is_valid, torus                        # noqa: E402
from graphity.sealed_tie_d import energy_table_d                  # noqa: E402
from graphity.dimension import local_dimension_d                  # noqa: E402


def test_patch_start_matches_exact_t54_and_is_valid():
    cfg = {"patch": {"L": 8, "k": 3}}
    adj, part, label = start_of(cfg)
    adj0, _ = torus([4, 8, 8])
    ref, _ = patch(adj0, 8, 3)
    assert (adj == ref).all() and label == "4 8 8 patch 3"
    assert is_valid(adj)
    lam = 1.25
    ftab = tie_table("all_at_the_last", lam)
    # the slab holds 3a per point under the tie; the patch state lies above it by T54's exact dH(3) at L = 8
    e_slab = energy_table_d(adj0, lam, ftab)
    assert abs(e_slab / adj0.shape[0] - 3 * 4 * (lam - 1)) < 1e-9
    # T54's exact quadratic under the tie: dH(k) = (176 - 112 lam) k - 48 (lam - 1) k^2, which is 24 at k = 1 and
    # exactly 0 at k = 3 for lam = 1.25 (O118)
    assert abs(energy_table_d(adj, lam, ftab) - e_slab) < 1e-9
    adj1, _, _ = start_of({"patch": {"L": 8, "k": 1}})
    assert abs(energy_table_d(adj1, lam, ftab) - e_slab - 24.0) < 1e-9


def test_full_patch_is_flat_space():
    adj, part, _ = start_of({"patch": {"L": 8, "k": 8}})
    d = local_dimension_d(adj)
    assert (d == 3).all()
    assert abs(energy_table_d(adj, 1.25, tie_table("all_at_the_last", 1.25))) < 1e-9


def test_patch_absent_leaves_the_runner_as_it_was():
    adj, part, label = start_of({"dims": [4, 6, 6]})
    ref, _ = torus([4, 6, 6])
    assert (adj == ref).all() and label == "4 6 6"
