"""The T76 reader on synthetic rows (every registered word, the overlap of CONSTANT with FALLING, and the translation to
w), the config writer (eight cells, seeds one per cell, couplings required), and the runner and the settling helper
end to end on tiny configs written to a temporary folder."""
import csv
import json
import sys
from pathlib import Path

import numpy as np
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import analyse_t76 as A            # noqa: E402
import make_t76_configs as M       # noqa: E402
import run_t76 as R                # noqa: E402
import settle_t76 as S             # noqa: E402

N0, N_SETTLE = 256, 200


def replica(rho_eq, growth, rho_of_n, n_grow=40, noise=0.0, seed=0):
    """Readings for one replica: a start, N_SETTLE settling readings at rho_eq, then n_grow growth readings with N
    rising evenly to growth * N0 and rho = rho_of_n(N)."""
    rng = np.random.default_rng(seed)
    rows = [dict(fair_sweep=0, phase="start", N=N0, rho=0.0)]
    rows += [dict(fair_sweep=t, phase="settle", N=N0, rho=rho_eq) for t in range(1, N_SETTLE + 1)]
    for k in range(1, n_grow + 1):
        n = int(round(N0 + (growth - 1) * N0 * k / n_grow))
        rows.append(dict(fair_sweep=N_SETTLE + k, phase="grow", N=n,
                         rho=rho_of_n(n) * (1 + noise * rng.uniform(-1, 1))))
    return rows


def cell(**kw):
    return [A.replica_reading(replica(**kw, seed=s)) for s in range(16)]


def test_rho_eq_reads_the_last_hundred_settling_sweeps():
    rows = replica(0.01, 2, lambda n: 0.01)
    for r in rows:
        if r["phase"] == "settle" and r["fair_sweep"] <= 100:
            r["rho"] = 1.0                            # the first hundred are not read
    assert A.rho_eq(rows) == pytest.approx(0.01)
    with pytest.raises(ValueError):
        A.rho_eq(rows, window=201)


def test_constant():
    rd = cell(rho_eq=0.01, growth=8, rho_of_n=lambda n: 0.01, noise=0.05)
    word, counts, also = A.cell_verdict(rd)
    assert word == "CONSTANT" and counts["CONSTANT"] == 16 and not also
    w = A.w_of(rd)
    assert abs(w["p"]) < 0.05 and w["w"] == pytest.approx(-1 - w["p"])


def test_falling_and_its_w():
    rd = cell(rho_eq=0.01, growth=8, rho_of_n=lambda n: 0.01 * (n / N0) ** -1.0)
    word, counts, _ = A.cell_verdict(rd)
    assert word == "FALLING" and counts["FALLING"] == 16 and counts["CONSTANT"] == 0
    w = A.w_of(rd)
    assert w["p"] == pytest.approx(-1.0, abs=1e-9) and w["w"] == pytest.approx(0.0, abs=1e-9)


def test_rising():
    rd = cell(rho_eq=0.01, growth=4, rho_of_n=lambda n: 0.01 * (n / N0) ** 0.5)
    assert A.cell_verdict(rd)[0] == "RISING"
    assert A.w_of(rd)["w"] == pytest.approx(-1.5, abs=1e-9)


def test_stalls():
    rd = cell(rho_eq=0.1, growth=1.5, rho_of_n=lambda n: 0.1)
    word, counts, _ = A.cell_verdict(rd)
    assert word == "STALLS" and counts["STALLS"] == 16
    assert not any(r["constant"] or r["falling"] or r["rising"] for r in rd)


def test_no_growth_at_all_stalls():
    rd = cell(rho_eq=0.1, growth=1.0, rho_of_n=lambda n: 0.1)
    assert A.cell_verdict(rd)[0] == "STALLS"
    assert all(r["n_half"] == 0 and np.isnan(r["p"]) for r in rd)


def test_mixed():
    rd = (cell(rho_eq=0.01, growth=8, rho_of_n=lambda n: 0.01)[:8]
          + cell(rho_eq=0.1, growth=1.5, rho_of_n=lambda n: 0.1)[:8])
    word, counts, _ = A.cell_verdict(rd)
    assert word == "MIXED" and counts["CONSTANT"] == 8 and counts["STALLS"] == 8


def test_constant_at_a_lower_level_also_falling():
    """A step down in the first half, steady after: both CONSTANT and FALLING; the registered order gives CONSTANT
    and the reader says FALLING was met too."""
    rd = cell(rho_eq=0.01, growth=8, rho_of_n=lambda n: 0.005 if n > 2 * N0 else 0.01)
    word, counts, also = A.cell_verdict(rd)
    assert word == "CONSTANT" and also == ["FALLING"] and counts["FALLING"] == 16


def test_a_single_second_half_reading_is_not_constant():
    """Growth that reaches the stop in one fair sweep leaves one reading in the second half: not CONSTANT (MIN_HALF),
    though it can still be FALLING, and p cannot be fitted."""
    rd = cell(rho_eq=0.01, growth=8, rho_of_n=lambda n: 0.002, n_grow=1)
    word, counts, _ = A.cell_verdict(rd)
    assert counts["CONSTANT"] == 0 and word == "FALLING"
    assert all(r["n_half"] == 1 and np.isnan(r["p"]) for r in rd)


def test_second_half_is_by_points_added():
    rows = replica(0.01, 3, lambda n: 0.01)
    half = A.second_half(rows, N0, 3 * N0)
    assert half and min(r["N"] for r in half) >= 2 * N0
    assert all(r["N"] - N0 >= N0 for r in half)


def test_power_fit_ignores_zeros_and_needs_two_sizes():
    assert A.power_fit([100, 200, 400], [0.0, 0.1, 0.05]) == pytest.approx(-1.0)
    assert np.isnan(A.power_fit([100, 100], [0.1, 0.2]))


# --------------------------------------------------------------------------------------------- configs and runs

def test_make_configs(tmp_path):
    with pytest.raises(ValueError):
        M.main([1.0, 2.0, 3.0, 3.0], tmp_path)
    written = M.main([1.2, 1.5, 2.0, 3.0], tmp_path)
    assert len(written) == 32                          # Amendment 2: 2 sizes x 4 couplings x 4 values of q
    cfgs = [json.loads(p.read_text()) for p in written]
    assert [c["seed"] for c in cfgs] == list(range(20267601, 20267633))
    assert [c["L"] for c in cfgs] == [16] * 16 + [24] * 16
    assert all(c["replicas"] == 16 and c["n_settle"] == 200 and c["n_growth"] == 4000 and c["cap_factor"] == 8
               and c["lambda"] == 1.25 and c["reach"] == 3 and c["n_ref"] == 96 for c in cfgs)
    assert [c["rho_target"] for c in cfgs[:16:4]] == [0.003, 0.01, 0.03, 0.1]
    assert [c["q"] for c in cfgs[:4]] == [1 / 16, 1 / 64, 1 / 256, 1 / 1024]
    assert len({c["name"] for c in cfgs}) == 32
    assert not any(c["L"] == 32 for c in cfgs)
    before = written[0].read_text()
    M.main([1.2, 1.5, 2.0, 3.0], tmp_path)            # refuses to rewrite
    assert written[0].read_text() == before


def tiny_config(tmp_path, name="t76_tiny"):
    cfg = dict(name=name, section="T76", L=8, **{"lambda": 1.25}, g=2.5, replicas=2, n_settle=6, n_growth=5,
               cap_factor=8, n_ref=96, reach=3, seed=20267699)
    p = tmp_path / (name + ".json")
    p.write_text(json.dumps(cfg))
    return p


def test_runner_end_to_end(tmp_path):
    out = tmp_path / "results"
    path = tiny_config(tmp_path)
    R.main(path, out)
    rows = list(csv.DictReader(open(out / "t76_tiny.csv", newline="")))
    meta = json.loads((out / "t76_tiny.meta.json").read_text())
    assert meta["config"]["seed"] == 20267699 and len(meta["finals"]) == 2
    assert {r["replica"] for r in rows} == {"0", "1"}
    assert [r["phase"] for r in rows if r["replica"] == "0"][:8] == ["start"] + ["settle"] * 6 + ["grow"]
    with pytest.raises(FileExistsError):              # append-only
        R.main(path, out)
    cells = A.read_rows([out / "t76_tiny.csv"])
    rd = [A.replica_reading(recs, window=3) for recs in cells[(2.5, 8)].values()]
    assert all(r["N_stop"] >= r["N0"] == 64 for r in rd)
    again = tmp_path / "again"                        # the same config reproduces its rows
    R.main(path, again)
    assert (again / "t76_tiny.csv").read_text() == (out / "t76_tiny.csv").read_text()


def test_settling_helper_end_to_end(tmp_path):
    cfg = dict(name="t76_settle_tiny", section="T76-settle", L=8, **{"lambda": 1.25}, couplings=[2.0, 4.0],
               replicas=2, n_settle=10, window=5, n_ref=96, seed=20267698)
    p = tmp_path / "s.json"
    p.write_text(json.dumps(cfg))
    S.main(p, tmp_path)
    rows = list(csv.DictReader(open(tmp_path / "t76_settle_tiny.csv", newline="")))
    assert len(rows) == 4 and {r["g"] for r in rows} == {"2.0", "4.0"}
    assert all(float(r["rho_eq"]) >= 0 for r in rows)
    meta = json.loads((tmp_path / "t76_settle_tiny.meta.json").read_text())
    assert [s["g"] for s in meta["summary"]] == [2.0, 4.0]
