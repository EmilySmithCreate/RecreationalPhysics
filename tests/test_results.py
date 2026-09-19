"""Checks on result writing (the append-only rule) and on the CQG sweep runner."""
import csv
import importlib.util
import json
from pathlib import Path

import numpy as np
import pytest

from graphity.cqg import run_chain, torus
from graphity.results import ResultWriter

ROOT = Path(__file__).resolve().parents[1]


def load_runner():
    """scripts/ is not a package, so load the runner by file path."""
    spec = importlib.util.spec_from_file_location("run_cqg_sweep", ROOT / "scripts" / "run_cqg_sweep.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def tiny_config(tmp_path, **extra):
    cfg = dict(name="tiny", sides=[6], couplings=[50, 5, 1], n_melt=50, n_equil=5,
               n_meas=40, replicas=1, seed=7, **extra)
    path = tmp_path / "tiny.json"
    path.write_text(json.dumps(cfg))
    return cfg, path


def read_rows(path):
    with path.open(newline="") as fh:
        return list(csv.DictReader(fh))


def test_writer_streams_rows_then_renames(tmp_path):
    with ResultWriter("run", {"note": "meta"}, tmp_path) as out:
        out.write(dict(a=1, b=2.5))
        assert not out.csv_path.exists()                      # not final until the run completes
        assert len(read_rows(out.partial_path)) == 1          # but already on disk
        out.write(dict(a=3, b=4.5))
    assert read_rows(tmp_path / "run.csv") == [dict(a="1", b="2.5"), dict(a="3", b="4.5")]
    assert json.loads((tmp_path / "run.meta.json").read_text()) == {"note": "meta"}
    assert not out.partial_path.exists()


def test_writer_refuses_to_overwrite(tmp_path):
    with ResultWriter("run", {}, tmp_path) as out:
        out.write(dict(a=1))
    before = (tmp_path / "run.csv").read_bytes()
    with pytest.raises(FileExistsError):
        ResultWriter("run", {}, tmp_path)
    assert (tmp_path / "run.csv").read_bytes() == before


def test_failed_run_leaves_only_a_partial_file(tmp_path):
    with pytest.raises(RuntimeError):
        with ResultWriter("run", {}, tmp_path) as out:
            out.write(dict(a=1))
            raise RuntimeError("simulated crash")
    assert not (tmp_path / "run.csv").exists()
    assert not (tmp_path / "run.meta.json").exists()
    assert len(read_rows(out.partial_path)) == 1              # finished rows survive the crash


def test_runner_reproduces_direct_chain_calls(tmp_path):
    """The runner adds bookkeeping only: same seeds, same numbers, to the last bit."""
    cfg, path = tiny_config(tmp_path)
    load_runner().main(path, tmp_path)
    rows = read_rows(tmp_path / "tiny.csv")
    assert [(r["leg"], float(r["g"])) for r in rows] == [
        ("cool", 50), ("cool", 5), ("cool", 1), ("heat", 5), ("heat", 50)]

    side, seed = 6, cfg["seed"] + 6                           # seed scheme of the runner, replica 0
    adj, part = torus(side)
    side_u = np.flatnonzero(part == 0)
    run_chain(adj, side_u, 0.0, cfg["n_melt"], 1, seed)
    for k, row in enumerate(rows, start=1):
        s, acc = run_chain(adj, side_u, 1.0 / float(row["g"]), cfg["n_equil"], cfg["n_meas"], seed + k)
        phi = s / side**2
        assert float(row["phi"]) == phi.mean()
        assert float(row["chi"]) == side**2 * phi.var()
        assert float(row["acceptance"]) == acc
        assert float(row["phi_err"]) >= 0 and float(row["chi_err"]) >= 0


def test_runner_refuses_a_second_run(tmp_path):
    _, path = tiny_config(tmp_path)
    runner = load_runner()
    runner.main(path, tmp_path)
    with pytest.raises(FileExistsError):
        runner.main(path, tmp_path)


def test_heating_leg_can_start_from_the_torus(tmp_path):
    _, path = tiny_config(tmp_path, heat_start="torus")
    load_runner().main(path, tmp_path)
    heat = [r for r in read_rows(tmp_path / "tiny.csv") if r["leg"] == "heat"]
    assert [float(r["g"]) for r in heat] == [1, 5, 50]        # coldest point included: it is a fresh start
    assert float(heat[0]["phi"]) > 0.9                        # still the torus at g = 1
    assert float(heat[-1]["phi"]) < 0.6                       # and it melts on the way up


def test_unknown_heat_start_is_rejected(tmp_path):
    _, path = tiny_config(tmp_path, heat_start="hexagons")
    with pytest.raises(ValueError):
        load_runner().main(path, tmp_path)
