"""Sandbox look (exploratory; rule 16), 26 October 2026: is the push look's "breakage" anticurl? Usage:

    python sandbox/breakage_anticurl_look.py

The owner's question of 26 October: "the wrong way around is a anticurl to its curl and they always come in pairs. so
maybe 'breakage' is actually more opening?" With six links a flat link carries four squares; curl on a link is a square
above four (S_e > 4), anticurl a square below (S_e < 4) (VISION Update 105). A broken point has d > 3 (more pairs of
links closing no square than flat space has). This reads the saved end states of `pair_tie_push_look.py` (no new run)
and reports, per cell: the total curl and anticurl (summed over links, in squares), how much of the anticurl sits on
links touching a broken point, how much of the remaining curl sits within one link of a broken point, and the energy
ledger: the main term 16 (3N - S) and the curling term 4 lambda X at the start and the end.
"""
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from graphity.cqg_d import squares_on_edge, torus      # noqa: E402
from graphity.dimension import local_dimension_d       # noqa: E402

OUT = ROOT / "sandbox" / "out" / "pair_tie_push"


def link_squares(adj):
    n, deg = adj.shape
    links = [(u, int(v)) for u in range(n) for v in adj[u] if u < v]
    return links, np.array([squares_on_edge(adj, u, v) for u, v in links])


def read(adj):
    links, s = link_squares(adj)
    d = local_dimension_d(adj)
    broken = d > 3
    curl = np.clip(s - 4, 0, None)
    anti = np.clip(4 - s, 0, None)
    touch_b = np.array([broken[u] or broken[v] for u, v in links])
    near = broken.copy()
    for v in np.flatnonzero(broken):
        near[adj[v]] = True
    near_b = np.array([near[u] or near[v] for u, v in links])
    return dict(curl=int(curl.sum()), anti=int(anti.sum()), anti_on_broken=int(anti[touch_b].sum()),
                curl_near_broken=int(curl[near_b].sum()), broken=int(broken.sum()), S=int(s.sum()) // 4)


def main():
    rod, _ = torus([4, 4, 18])
    r0 = read(rod)
    print(f"start (the rod): curl {r0['curl']}, anticurl {r0['anti']}, squares {r0['S']} (flat would have {3 * 288})")
    for path in sorted(OUT.glob("push_rod_*_adj")):
        rows = []
        for f in sorted(path.glob("*.npz")):
            z = np.load(f)
            r = read(z["adj"])
            r["lam"] = float(z["lam"])
            rows.append(r)
        lam = rows[0]["lam"]
        parts = [f"curl {r['curl']:4d} anti {r['anti']:4d} (on broken {r['anti_on_broken']:4d}) broken {r['broken']:3d} "
                 f"curl near broken {r['curl_near_broken']:4d}" for r in rows]
        print(f"{path.name[9:-4]:18s} " + " | ".join(parts))


if __name__ == "__main__":
    main()
