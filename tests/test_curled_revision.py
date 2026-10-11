"""Independent controls for the retrospective paper certificates and thermometer."""
import importlib.util
from pathlib import Path

import numpy as np
import pytest

from graphity.cqg import NO_CAP, torus
from graphity.sealed import demon_temperature
from scripts.analyse_curled_revision import binomial_interval, neutral_closure


def geometry_reader():
    path = Path(__file__).resolve().parents[1] / "docs/papers/curled_torus/reviewer_checks_2026-10-09.py"
    spec = importlib.util.spec_from_file_location("curled_reviewer", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.independent_geometry


def test_topology_certificate_distinguishes_flat_curled_and_disconnected():
    geometry = geometry_reader()
    flat, _ = torus(6, 6, NO_CAP)
    curled, _ = torus(4, 16, NO_CAP)
    g = geometry(flat)
    assert (g["S"], g["components"], g["closed_surface"], g["orientable"], g["chi"]) == (36, 1, True, True, 0)
    g = geometry(curled)
    assert g["S"] == 80 and not g["closed_surface"]
    g = geometry(np.vstack([flat, flat+36]))
    assert g["closed_surface"] and g["orientable"] and g["chi"] == 0
    assert g["components"] == 2  # chi and local surface tests alone do not give one torus


def test_smaller_neutral_basin_does_not_inherit_full_hazard_invariance():
    records = neutral_closure(32)
    assert len(records) == 3
    assert sorted(r["symmetries"] for r in records) == [32, 64, 64]
    assert len({r["census"] for r in records}) > 1
    assert all(r["minimum"] == 12 for r in records)


def test_integer_demon_thermometer_matches_geometric_distribution():
    g = 3.5
    levels = np.arange(300)
    weights = np.exp(-levels/g)
    mean = np.dot(levels, weights)/weights.sum()
    assert mean == pytest.approx(3.023777192733274)
    assert demon_temperature([mean], step=1) == pytest.approx(g)
    assert demon_temperature([0.5], step=1) == pytest.approx(1/np.log(3))


def test_small_sample_success_intervals_do_not_claim_certainty():
    assert binomial_interval(8, 8) == pytest.approx((0.6305833524471807, 1))
    assert binomial_interval(0, 8) == pytest.approx((0, 0.3694166475528192))
