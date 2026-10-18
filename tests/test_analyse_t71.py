"""The T71 runner and analyzer together on a tiny cell (scratch output; nothing in results/)."""
import csv
import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import analyse_t71 as A            # noqa: E402
import run_layer_feed as R         # noqa: E402


def _run(tmp_path, name, **over):
    cfg = dict(name=name, section="T71", written="2026-10-18", lambdas=[1.25], sizes=[6], rates=[0.0625],
               gate="a * N_slab", leak=0.0, n_sweeps=60, replicas=2, seed=71, move_set="layer",
               feed_stops_at_split=True, max_width=8, log_every=1)
    cfg.update(over)
    path = tmp_path / (name + ".json")
    path.write_text(json.dumps(cfg))
    R.main(str(path), str(tmp_path))
    return list(csv.DictReader(open(tmp_path / (name + ".csv"), newline="")))


def test_the_runner_conserves_energy_and_the_analyzer_reads_the_gate_and_the_release(tmp_path):
    rows = _run(tmp_path, "t71_test_a")
    assert all(abs(float(r["residual"])) < 1e-9 for r in rows)
    assert (tmp_path / "t71_test_a.meta.json").exists()
    cells = A.read_cells(rows)
    assert len(cells) == 1
    (cell,) = cells.values()
    assert cell["n"] == 2
    for rep in cell["replicas"]:
        assert rep["first_split"] >= 32                        # the pool of 72 points reaches 144 at 2a / r = 32 sweeps
        assert rep["release"] == pytest.approx(144.0)           # a N_slab, credited at the split
        assert rep["word"] in ("OSCILLATES", "OPENS AND STAYS") and not rep["spent_first"]
    assert cell["median_release"] == pytest.approx(144.0)


def test_a_gate_the_stores_never_reach_reads_never_splits(tmp_path):
    rows = _run(tmp_path, "t71_test_b", gate="100 * N_slab", n_sweeps=20, move_set="model")
    (cell,) = A.read_cells(rows).values()
    assert cell["majority"] == "NEVER SPLITS" and cell["words"] == {"NEVER SPLITS": 2}
    assert cell["median_first_split"] is None
    assert all(int(r["broken"]) == 0 for r in rows)


def test_the_runner_refuses_to_overwrite(tmp_path):
    _run(tmp_path, "t71_test_c", n_sweeps=5)
    with pytest.raises(FileExistsError):
        _run(tmp_path, "t71_test_c", n_sweeps=5)
