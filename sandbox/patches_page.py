"""Sandbox: the pictures for the explainer page "Patches and melting". Usage:

    python sandbox/patches_page.py OUT.json

Writes, for five states of the same 96 dots, each dot's place on the unrolled tube (24 along, 4 around, where it
started), what it is now, and its four links. Three states are saved end states of T61's stage 1 (read on 11
October); the tube is built; the melt is the tube after 300 sweeps of the thermal chain at g = 12. Pictures, not
evidence.
"""
import json
import sys
from collections import Counter
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "sandbox"))
from graphity.cqg import NO_CAP, hamiltonian, run_chain, torus, total_squares      # noqa: E402
from graphity.dimension import local_dimension                                  # noqa: E402
from patchwork_census import look                                               # noqa: E402
from read_flat_kind import pieces                                               # noqa: E402

LENGTH, AROUND = 24, 4


def squares_at(adj):
    """Squares through each dot."""
    nbr = [set(int(x) for x in row) for row in adj]
    out = np.zeros(adj.shape[0], dtype=np.int64)
    for u in range(adj.shape[0]):
        for a in nbr[u]:
            for c in nbr[u]:
                if a < c:
                    out[u] += len((nbr[a] & nbr[c]) - {u})
    return out


def kinds(adj):
    """Per dot: 'curled' (d = 1), 'flaw' (not on exactly four squares, or d = 3), or 'six', 'eight', 'wide' for a
    dot in good fabric by how far it sees a sheet."""
    d = local_dimension(adj)
    sq = squares_at(adj)
    first, _over = look(adj)
    out = []
    for v in range(adj.shape[0]):
        if d[v] == 1 and sq[v] == 5:
            out.append("curled")
        elif sq[v] != 4 or d[v] != 2:
            out.append("flaw")
        else:
            out.append("six" if first[v] <= 3 else ("eight" if first[v] == 4 else "wide"))
    return out


def state(name, adj, lam, note):
    n = adj.shape[0]
    links = []
    for u in range(n):
        xu, yu = divmod(u, AROUND)
        for v in adj[u]:
            xv, yv = divmod(int(v), AROUND)
            dx = (xv - xu + LENGTH // 2) % LENGTH - LENGTH // 2
            dy = (yv - yu + AROUND // 2) % AROUND - AROUND // 2
            links.append([xu, yu, dx, dy])
    k = kinds(adj)
    return dict(name=name, note=note, kinds=k, counts=dict(Counter(k)), links=links,
                squares_per_dot=round(float(total_squares(adj)) / n, 3), energy=round(float(hamiltonian(adj, lam)), 1),
                pieces=[int(p.shape[0]) for p in pieces(adj)],
                far_links=round(float(np.mean([abs(l[2]) > 3 for l in links])), 3))


def saved(name, stores, rep):
    return np.load(ROOT / "results" / (name + "_adj") / ("N96_C%d_rep%d.npz" % (stores, rep)))["adj"]


def main(out):
    tube, part = torus(LENGTH, AROUND, NO_CAP)
    side = np.flatnonzero(part == 0).astype(np.int64)
    melt = tube.copy()
    run_chain(melt, side, 1.0 / 12.0, 299, 1, 20261011, 1.25, NO_CAP)
    warm = tube.copy()
    run_chain(warm, side, 1.0 / 3.2, 1999, 1, 20261012, 1.25, NO_CAP)
    states = [
        state("tube", tube, 1.25, "built"),
        state("clean", saved("t61_lam125_n96", 96, 0), 1.25, "T61 stage 1, lambda 1.25, one store per dot, replica 0"),
        state("patchwork", saved("t61_lam140_n96", 24, 10), 1.40, "T61 stage 1, lambda 1.40, a quarter store per dot, replica 10"),
        state("wide", saved("t61_lam140_n96", 96, 6), 1.40, "T61 stage 1, lambda 1.40, one store per dot, replica 6"),
        state("warm", warm, 1.25, "the tube after 2,000 sweeps at g = 3.2"),
        state("melt", melt, 1.25, "the tube after 300 sweeps at g = 12"),
    ]
    Path(out).write_text(json.dumps(states), encoding="utf-8")
    for s in states:
        print("%-9s squares per dot %.3f | energy %6.1f | pieces %s | links reaching more than 3 along: %.0f %% | %s"
              % (s["name"], s["squares_per_dot"], s["energy"], s["pieces"], 100 * s["far_links"], s["counts"]))


if __name__ == "__main__":
    main(sys.argv[1])
