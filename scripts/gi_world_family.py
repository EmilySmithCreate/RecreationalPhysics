"""The curl-store world family for the GeneralizedIntelligence plans (docs/design/gi/world_family_curl_store.md).

    PYTHONPATH="src;scripts" python scripts/gi_world_family.py --seed 1234 --per-kind 6 --out out/gi_world [--private]

A two-state world built from exact facts of this record: the curling ladder (per point, squares D(D-1)/2 + u/4,
surplus u, energy 4(lambda-1)u, local dimension D-u; checked on every rung 30 Oct 2026) and its single-move walls
(docs/figures/ladder_kinds.json, scripts/exact_ladder_d.py). State (u, v): u curled directions left, v the store.
Three readings, each a function of u alone, so v shows only through when the drops happen.

Kinds: fed (a feed f per step), spark (f = 0, one store at the start), twisted (foil: a hidden twist store y fills
at its own rate, an opening needs y >= kappa as well as v >= wall, and y resets at each opening; y is not a function
of (u, v), so the drops cannot be predicted from two state variables), noisy (foil: drop steps at random, no wall).
The twisted draw is kept only if the twist condition actually delays at least one drop against the untwisted rule.

Output: <out>/cases.json with each case's prompt half (what a model may see) and, unless --private, its hidden half
beside it; with --private the hidden halves go to <out>/hidden.json so the public file can be shared. Deterministic
in the seed. Nothing here is a run of the hypothesis; it is a resource for the sister repository's plans.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LADDER = ROOT / "docs" / "figures" / "ladder_kinds.json"

KINDS = ("fed", "spark", "twisted", "noisy")
LABELS = {"fed": "rule", "spark": "rule", "twisted": "not reducible to two", "noisy": "no rule found"}
LAMBDAS = (1.1, 1.25, 1.5)
PROBE_OFFSETS = (1, 3, 5, 10, 15)
FRESH_SETS = 3


def make_rng(seed: int, kind: str, index: int) -> random.Random:
    key = f"{seed}|gi|{kind}|{index}".encode()
    return random.Random(int.from_bytes(hashlib.sha256(key).digest()[:8], "big"))


def load_walls(path: Path = LADDER) -> dict[tuple[int, int], list[tuple[int, int]]]:
    """(D, curled) -> the list of single-move kinds (dS, dX) of that rung, from the exact listing."""
    rows = json.loads(path.read_text(encoding="utf-8"))
    return {(r["D"], r["curled"]): [(k["dS"], k["dX"]) for k in r["kinds"]] for r in rows}


def wall(kinds: dict, D: int, u: int, lam: float) -> float:
    """The cheapest single move out of the rung with u curled directions: min over kinds of -16 dS + 4 lam dX."""
    return min(-16 * ds + 4 * lam * dx for ds, dx in kinds[(D, u)])


def readings(D: int, u: int, lam: float) -> tuple[float, float, int]:
    a = 4 * (lam - 1)
    return round(a * u, 6), round(D * (D - 1) / 2 + u / 4, 6), D - u


def simulate(kinds: dict, p: dict, steps: int) -> list[tuple[float, float, int]]:
    """Readings at steps 0..steps under the hidden rule of the kind."""
    D, lam, N, f, u, v = p["D"], p["lam"], p["N"], p["f"], p["u0"], float(p["v0"])
    a = 4 * (lam - 1)
    out = [readings(D, u, lam)]
    y = 0.0                      # the twist store (twisted kind only); 0 and never binding otherwise
    rng = random.Random(p.get("noise_seed", 0))
    for _ in range(steps):
        v += f
        y += p.get("f2", 0)
        if p["kind"] == "noisy":
            if u > 0 and rng.random() < p["drop_chance"]:
                u -= 1
        else:
            twisted_ok = p["kind"] != "twisted" or y >= p["kappa"]
            if u > 0 and twisted_ok and v >= wall(kinds, D, u, lam):
                u -= 1
                v += a * N
                y = 0.0
        out.append(readings(D, u, lam))
    return out


def drop_steps(trace: list[tuple[float, float, int]]) -> list[int]:
    return [t for t in range(1, len(trace)) if trace[t][2] != trace[t - 1][2]]


def draw_params(rng: random.Random, kind: str, kinds: dict) -> dict:
    """One world. The window T is chosen so that at least one drop falls inside it and, for rule kinds, the rule
    still has something to show after it (a later drop, or a plateau that an extrapolation of the drops gets wrong)."""
    D = rng.choice((2, 3, 4))
    lam = rng.choice(LAMBDAS)
    N = 4 * rng.randint(8, 64)
    u0 = rng.randint(1, D)
    p = dict(kind=kind, D=D, lam=lam, N=N, u0=u0, kappa=0, f2=0, drop_chance=0.0, noise_seed=0)
    if kind == "spark":
        p["f"] = 0
        # a spark between the first wall and well above it, so cascades and stalls both occur
        w1 = wall(kinds, D, u0, lam)
        p["v0"] = max(0.0, w1 + rng.choice((-4, 0, 4, 12, 40)))
    else:
        p["f"] = rng.randint(1, 6)
        p["v0"] = rng.randint(0, 8)
    if kind == "twisted":
        p["f2"] = 1
        p["kappa"] = rng.randint(3, 12)
        plain = drop_steps(simulate(kinds, dict(p, kind="fed"), 60))
        while drop_steps(simulate(kinds, p, 60)) == plain:
            p["kappa"] += 4           # until the twist store actually delays a drop
    if kind == "noisy":
        p["drop_chance"] = rng.choice((0.05, 0.1, 0.2))
        p["noise_seed"] = rng.randint(1, 10 ** 6)
    trace = simulate(kinds, p, 60)
    drops = drop_steps(trace)
    if drops:
        T = drops[0] + rng.randint(1, 4)
    else:
        T = rng.randint(6, 12)
    p["T"] = T
    return p


def fresh_params(rng: random.Random, p: dict) -> dict:
    q = dict(p)
    q["N"] = 4 * rng.randint(8, 64)
    if p["kind"] == "spark":
        q["v0"] = max(0.0, p["v0"] + rng.choice((-8, 0, 8)))
    else:
        q["f"] = rng.randint(1, 6)
        q["v0"] = rng.randint(0, 8)
    if p["kind"] == "noisy":
        q["noise_seed"] = rng.randint(1, 10 ** 6)
    return q


def make_case(seed: int, kind: str, index: int, kinds: dict) -> tuple[dict, dict]:
    rng = make_rng(seed, kind, index)
    p = draw_params(rng, kind, kinds)
    T = p["T"]
    trace = simulate(kinds, p, T + PROBE_OFFSETS[-1])
    case_id = f"gi-{seed}-{kind}-{index:03d}"
    prompt = {
        "case_id": case_id,
        "family": "D" if LABELS[kind] == "rule" else "N",
        "stated_numbers": {"N": p["N"], "feed": p["f"]},
        "window": [{"t": t, "r1": trace[t][0], "r2": trace[t][1], "r3": trace[t][2]} for t in range(T + 1)],
        "probe_steps": [T + k for k in PROBE_OFFSETS],
        "task": ("Recover a rule for two state variables and a map to the three readings; predict r1, r2, r3 at "
                 "the probe steps on fresh parameters; or answer 'not reducible to two' or 'no rule found'."),
    }
    fresh = [fresh_params(rng, p) for _ in range(FRESH_SETS)]
    hidden = {
        "case_id": case_id,
        "kind": kind,
        "label": LABELS[kind],
        "params": p,
        "walls": {str(u): round(wall(kinds, p["D"], u, p["lam"]), 6) for u in range(1, p["D"] + 1)},
        "release_per_direction": round(4 * (p["lam"] - 1) * p["N"], 6),
        "probe_truth": [trace[T + k] for k in PROBE_OFFSETS],
        "fresh": [{"params": q, "probe_truth": [simulate(kinds, q, q["T"] + PROBE_OFFSETS[-1])[q["T"] + k]
                                               for k in PROBE_OFFSETS]} for q in fresh],
        "rule": ("v = v + f; if u > 0 and v >= wall(u) { u = u - 1; v = v + 4 (lambda - 1) N }; "
                 "r1 = 4 (lambda - 1) u; r2 = D (D - 1) / 2 + u / 4; r3 = D - u"),
    }
    return prompt, hidden


def build(seed: int, per_kind: int, kinds: dict | None = None) -> tuple[list[dict], list[dict]]:
    kinds = kinds or load_walls()
    prompts, hiddens = [], []
    for kind in KINDS:
        for i in range(per_kind):
            pr, hi = make_case(seed, kind, i, kinds)
            prompts.append(pr)
            hiddens.append(hi)
    return prompts, hiddens


def main(argv: list[str] | None = None) -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=1234)
    ap.add_argument("--per-kind", type=int, default=6)
    ap.add_argument("--out", default="out/gi_world")
    ap.add_argument("--private", action="store_true", help="write hidden halves to a separate file")
    args = ap.parse_args(argv)
    prompts, hiddens = build(args.seed, args.per_kind)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    if args.private:
        (out / "cases.json").write_text(json.dumps({"seed": args.seed, "cases": prompts}, indent=1) + "\n",
                                        encoding="utf-8", newline="\n")
        (out / "hidden.json").write_text(json.dumps({"seed": args.seed, "hidden": hiddens}, indent=1) + "\n",
                                         encoding="utf-8", newline="\n")
    else:
        cases = [{"prompt": pr, "hidden": hi} for pr, hi in zip(prompts, hiddens)]
        (out / "cases.json").write_text(json.dumps({"seed": args.seed, "cases": cases}, indent=1) + "\n",
                                        encoding="utf-8", newline="\n")
    counts = {k: sum(1 for h in hiddens if h["kind"] == k) for k in KINDS}
    print(f"wrote {len(prompts)} cases to {out}: {counts}")


if __name__ == "__main__":
    main()
