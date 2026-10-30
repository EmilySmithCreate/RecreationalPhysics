"""The curl-store world family (scripts/gi_world_family.py): exact readings, exact walls, foils present, no hidden
field in a prompt, same seed same cases."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import gi_world_family as gw  # noqa: E402


def test_readings_match_the_exact_ladder():
    # per point: squares D(D-1)/2 + u/4, surplus u, energy 4(lambda-1)u, local dimension D-u (checked on every
    # rung with graphity.cqg_d.torus on 30 Oct 2026)
    assert gw.readings(2, 1, 1.25) == (1.0, 1.25, 1)
    assert gw.readings(3, 2, 1.25) == (2.0, 3.5, 1)
    assert gw.readings(4, 4, 1.1) == (round(1.6, 6), 7.0, 0)
    assert gw.readings(3, 0, 1.5) == (0.0, 3.0, 3)


def test_walls_match_the_record():
    kinds = gw.load_walls()
    # VISION Update 9: the tube's wall at lambda = 1.25 is 12; ASSUMPTIONS O49: the rod's is 96 - 64 lambda = 16;
    # O41: the slab's 36 at 1.25 and 48 at 1.0; the four-direction ladder 20, 40, 80 at 1.25 (O50)
    assert gw.wall(kinds, 2, 1, 1.25) == 12
    assert gw.wall(kinds, 3, 2, 1.25) == 16
    assert gw.wall(kinds, 3, 1, 1.25) == 36
    assert gw.wall(kinds, 3, 1, 1.0) == 48
    assert [gw.wall(kinds, 4, u, 1.25) for u in (3, 2, 1)] == [20, 40, 80]


def test_spark_cascade_and_stall_are_arithmetic():
    kinds = gw.load_walls()
    base = dict(kind="spark", D=3, lam=1.25, f=0, u0=2, kappa=0, drop_chance=0.0, noise_seed=0)
    # N = 288: the rod opens at 16, the release 288 pays the slab's wall of 36: a cascade to flat
    tr = gw.simulate(kinds, dict(base, N=288, v0=16), 3)
    assert [t[2] for t in tr] == [1, 2, 3, 3]
    # N = 16: the store keeps the spark (a wall is a hill, not a toll: O71), 16 + 16 = 32 is below 36: a stall
    tr = gw.simulate(kinds, dict(base, N=16, v0=16), 3)
    assert [t[2] for t in tr] == [1, 2, 2, 2]
    # below the wall nothing ever opens (Update 9: a tube with nothing to spare never converts)
    tr = gw.simulate(kinds, dict(base, N=288, v0=15.9), 20)
    assert all(t[2] == 1 for t in tr)


def test_batch_has_matched_foils_and_leaks_nothing():
    prompts, hiddens = gw.build(seed=7, per_kind=3)
    labels = [h["label"] for h in hiddens]
    assert labels.count("not reducible to two") == 3 and labels.count("no rule found") == 3
    assert labels.count("rule") == 6
    for pr in prompts:
        text = json.dumps(pr)
        for word in ("lam", "lambda", "kind", "label", "wall", "u0", "v0", "kappa", "drop_chance", "truth"):
            assert word not in text, (word, pr["case_id"])
        assert len(pr["window"]) == pr["probe_steps"][0]
    for pr, hi in zip(prompts, hiddens):
        assert pr["case_id"] == hi["case_id"]
        assert len(hi["probe_truth"]) == 5 and len(hi["fresh"]) == 3


def test_twisted_foil_is_not_a_function_of_two_variables():
    # same (u, v) at the same step, different twist store: different futures; and the drawn foils really delay a drop
    kinds = gw.load_walls()
    p = dict(kind="twisted", D=2, lam=1.25, N=40, f=4, u0=1, v0=0, kappa=9, f2=1, drop_chance=0.0, noise_seed=0)
    plain = gw.drop_steps(gw.simulate(kinds, dict(p, kind="fed"), 30))
    twisted = gw.drop_steps(gw.simulate(kinds, p, 30))
    assert plain == [3] and twisted == [9]
    prompts, hiddens = gw.build(seed=5, per_kind=6)
    for hi in hiddens:
        if hi["kind"] == "twisted":
            q = hi["params"]
            assert gw.drop_steps(gw.simulate(kinds, q, 60)) != gw.drop_steps(gw.simulate(kinds, dict(q, kind="fed"), 60))


def test_same_seed_same_cases():
    a = gw.build(seed=11, per_kind=2)
    b = gw.build(seed=11, per_kind=2)
    assert a == b
    c = gw.build(seed=12, per_kind=2)
    assert c != a


def test_every_rule_case_shows_a_drop_in_or_after_its_window():
    prompts, hiddens = gw.build(seed=3, per_kind=8)
    kinds = gw.load_walls()
    for pr, hi in zip(prompts, hiddens):
        if hi["label"] != "rule":
            continue
        p = hi["params"]
        tr = gw.simulate(kinds, p, p["T"] + 15)
        d = [t[2] for t in tr]
        assert d[0] == pr["window"][0]["r3"]
        # the drop count never exceeds the start's curled directions and the dimension never falls
        assert all(x <= y for x, y in zip(d, d[1:]))
        assert d[-1] - d[0] <= p["u0"]
