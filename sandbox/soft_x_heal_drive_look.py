"""Sandbox look (rule 16: can kill, never crown), 27 October 2026: under the owner's soft rule, does the healing of the
south cap's anticurl drive the north rod open? Words declared here before anything ran.

Why: `soft_x_stuck_look.py` (same day) found her nearest buildable X (rod 4 x 4 x L, south half melted to S = 3N; OBEYS
the hard rule at the start) NOT STUCK at every lambda and mu0, every downhill switch in the melted south or across the
middle, none in the curled north. Healing the south raises S above 3N; the penalty mu0 (S - 3N)^2 / N then pushes S back
down, and the north can lower S only by losing curl, which is opening. So the penalty couples the two halves.

Run: `soft_d.run_chain` from that X (L = 16, melt seeds 1, 2, 3), her energy at lambda = 1.25 mapped exactly onto the toy
(O164 addendum): lambda' = 2 - 1/lambda = 1.2, coupling g / lambda, penalty mu0 / (N lambda); her g in {1.0, 1.5}; mu0 in
{1, 16, 256}; 10,000 chain sweeps (one sweep = 2N attempted switches; the chain clock, stated). Named points. One replica
per (seed, g, mu0).

Read at the end: the north half's local dimension census (d = 1 still rod, 2 one direction open, 3 both open, > 3
broken), S - 3N, the south half's anticurl against its start. Words per run: BOTH OPEN (at least 90 % of north points
at d = 3), ONE OPEN (at least 90 % at d >= 2 and not BOTH OPEN), STAYS (at least 90 % at d = 1), MIXED otherwise; flag
DAMAGED if any point anywhere has d > 3; south HEALED if its anticurl fell to 10 % of its start or less.

Her prediction (A4, 27 October 17:41 UTC, verbatim "soft runs make the space open with the twin daughters"), read here as
BOTH OPEN (the reading is ours; she stated it for the soft runs, not for this look). Ours: the south HEALS everywhere;
the north STAYS at mu0 = 1 and 16 (a fully healed south raises S by its anticurl over 4, about 64 at L = 16, a penalty of
16 mu0, small against the rod's walls), and at mu0 = 256 the north moves and the run is DAMAGED.
"""
import sys
import time
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "sandbox"))
from graphity import cqg_d, soft_d  # noqa: E402
from graphity.dimension import local_dimension_d  # noqa: E402
from soft_x_stuck_look import melt_south  # noqa: E402

OUT = ROOT / "sandbox" / "out" / "soft_x_stuck"


def south_uncurl(adj, south):
    unc = 0
    for u in np.flatnonzero(south):
        for v in adj[u]:
            if u < v and south[v]:
                unc += max(4 - int(cqg_d.squares_on_edge(adj, int(u), int(v))), 0)
    return unc


def main():
    lam, L = 1.25, 16
    lp = 2 - 1 / lam
    lines = []
    for seed in (1, 2, 3):
        for g in (1.0, 1.5):
            for mu0 in (1.0, 16.0, 256.0):
                adj, part = cqg_d.torus((4, 4, L))
                n = adj.shape[0]
                south = (np.arange(n) % L) >= L // 2
                side = np.flatnonzero(part == 0).astype(np.int64)
                melt_south(adj, side, south, 3 * n, seed, 50_000_000)
                unc0 = south_uncurl(adj, south)
                t0 = time.time()
                s, x, acc = soft_d.run_chain(adj, side, lam / g, 0, 10_000, 100 + seed, lp, mu0 / (n * lam))
                d = local_dimension_d(adj)
                north = d[~south]
                share = {k: float(np.mean(north == k)) for k in (1, 2, 3)}
                broken = int((d > 3).sum())
                if share[3] >= 0.9:
                    word = "BOTH OPEN"
                elif share[2] + share[3] >= 0.9:
                    word = "ONE OPEN"
                elif share[1] >= 0.9:
                    word = "STAYS"
                else:
                    word = "MIXED"
                unc1 = south_uncurl(adj, south)
                lines.append(
                    f"seed {seed}, g {g}, mu0 {mu0:5.0f}: {word}{', DAMAGED' if broken else ''}; north d=1 {share[1]:.2f}, "
                    f"d=2 {share[2]:.2f}, d=3 {share[3]:.2f}; points with d > 3: {broken}; S - 3N {int(s[-1]) - 3 * n:+d} "
                    f"(min {int(s.min()) - 3 * n:+d}, max {int(s.max()) - 3 * n:+d}); south anticurl {unc0} -> {unc1}"
                    f"{' HEALED' if unc1 <= 0.1 * unc0 else ''}; acceptance {acc:.4f}; {time.time() - t0:.0f} s")
                print(lines[-1], flush=True)
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "soft_x_heal_drive.txt").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
