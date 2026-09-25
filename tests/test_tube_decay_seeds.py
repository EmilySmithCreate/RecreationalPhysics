"""T37: counting seeds reads the graph and draws no random numbers, so a run with it is the run without it."""
import csv
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import run_tube_decay  # noqa: E402


def _run(tmp_path, name, extra):
    cfg = {"name": name, "sides": [[24, 4]], "g": 1.5, "replicas": 2, "n_sweeps": 30000, "block": 5,
           "stop_at": 0.98, "settle": 100, "settle_max": 400, "seed": 7, "lambda": 1.25}
    cfg.update(extra)
    path = tmp_path / (name + ".json")
    path.write_text(json.dumps(cfg))
    run_tube_decay.main(str(path), str(tmp_path))
    return list(csv.DictReader(open(tmp_path / (name + ".csv"), newline="")))


def test_seed_count_does_not_change_the_chain(tmp_path):
    a = _run(tmp_path, "plain", {})
    b = _run(tmp_path, "counted", {"count_patches_every": 50, "patch_min": 8})
    for ra, rb in zip(a, b):
        for key in ("waiting", "phi_final", "released", "sweeps"):
            assert ra[key] == rb[key]
        if float(rb["reached"]) >= 0.5:
            assert int(rb["seeds"]) >= 1


def test_saving_waiting_tubes_does_not_change_the_chain(tmp_path):
    """T38: a tube still waiting at a named sweep is saved; the chain is the chain without it."""
    a = _run(tmp_path, "plain2", {})
    b = _run(tmp_path, "saved", {"save_waiting_at": [300, 600]})
    for ra, rb in zip(a, b):
        for key in ("waiting", "phi_final", "released", "sweeps"):
            assert ra[key] == rb[key]
    saved = sorted(p.name for p in (tmp_path / "saved_waiting").glob("*.npz")) if (tmp_path / "saved_waiting").exists() else []
    for rb in b:
        w = int(rb["waiting"]) if rb["waiting"] else 10 ** 9
        for s in (300, 600):
            assert (("N96_rep%s_sweep%d.npz" % (rb["replica"], s)) in saved) == (w > s)
