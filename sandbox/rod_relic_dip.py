"""Sandbox look, 15 October 2026 (rule 16; one line in LOG). The owner's question: is the rod (4 x 4 x L, one
open direction) the three-direction equivalent of paper 1's tube, and in particular does its opening leave a
stuck relic as the tube leaves a column? Read from saved end states (T48 rod and slab cells; T53 rod cells at the
coldest baths; T48's two-direction control as a check that the method finds the 2D column stuck): every piece of
points still below the flat rung, its size, its energy, and whether every single move touching it costs energy
at the run's lambda (STUCK) or some move goes downhill. Exact per graph; which graphs are read is ours.

    python3 sandbox/rod_relic_dip.py results/t48_local_2d_lam125_w4_adj results/t48_local_3d_two_lam125_w4_adj ...
"""
import glob, os, sys
import numpy as np
from numba import njit
sys.path.insert(0, "scripts")
from exact_exits_d import _has, _replace, _locally_valid, s_and_x, _squares_on  # noqa: E402
from graphity.dimension import local_dimension_d, piece_labels  # noqa: E402


@njit
def _local_sx(adj, pts, mask, sat):
    """(S, X) over the edges with both ends within one step of pts; mask is a scratch array of zeros."""
    n, deg = adj.shape
    w = np.empty(4 + 4 * deg, dtype=np.int64)
    m = 0
    for i in range(4):
        p = pts[i]
        if mask[p] == 0:
            mask[p] = 1; w[m] = p; m += 1
        for k in range(deg):
            q = adj[p, k]
            if q >= 0 and mask[q] == 0:
                mask[q] = 1; w[m] = q; m += 1
    s4 = 0; x = 0
    for i in range(m):
        u = w[i]
        for k in range(deg):
            v = adj[u, k]
            if v > u and mask[v] == 1:
                se = _squares_on(adj, u, v)
                s4 += se
                if se > sat:
                    x += se - sat
    for i in range(m):
        mask[w[i]] = 0
    return s4, x


@njit
def moves_touching(adj, side_u, u1_list, inpiece, sat, lam):
    """Over switches with u1 in u1_list and u2 any other side-0 point: the cheapest cost among moves with at least
    one of the four points in the piece or one step from it (inpiece == 1 or 2), and the cheapest with a point in
    the piece itself (inpiece == 1). Returns (min_near, min_in, count_near)."""
    n, deg = adj.shape
    mask = np.zeros(n, dtype=np.int64)
    pts = np.empty(4, dtype=np.int64)
    best_near = 1e9; best_in = 1e9; cnt = 0
    for ii in range(u1_list.shape[0]):
        u1 = u1_list[ii]
        for jj in range(side_u.shape[0]):
            u2 = side_u[jj]
            if u2 == u1:
                continue
            for a in range(deg):
                v1 = adj[u1, a]
                for b in range(deg):
                    v2 = adj[u2, b]
                    if v1 == v2 or _has(adj, u1, v2) or _has(adj, u2, v1):
                        continue
                    pts[0] = u1; pts[1] = u2; pts[2] = v1; pts[3] = v2
                    near = 0; inside = 0
                    for t in range(4):
                        if inpiece[pts[t]] >= 1:
                            near = 1
                        if inpiece[pts[t]] == 1:
                            inside = 1
                    if near == 0:
                        continue
                    s0, x0 = _local_sx(adj, pts, mask, sat)
                    adj[u1, a] = v2
                    adj[u2, b] = v1
                    _replace(adj, v1, u1, u2)
                    _replace(adj, v2, u2, u1)
                    if _locally_valid(adj, pts):
                        s1, x1 = _local_sx(adj, pts, mask, sat)
                        cost = -16.0 * (s1 - s0) / 4.0 + 4.0 * lam * (x1 - x0)
                        if not (s1 == s0 and x1 == x0):
                            cnt += 1
                            if cost < best_near:
                                best_near = cost
                            if inside == 1 and cost < best_in:
                                best_in = cost
                    adj[u1, a] = v1
                    adj[u2, b] = v2
                    _replace(adj, v1, u2, u1)
                    _replace(adj, v2, u1, u2)
    return best_near, best_in, cnt


def check_local_is_exact(adj, side, sat, trials=200, seed=0):
    rng = np.random.default_rng(seed)
    n, deg = adj.shape
    side_u = np.flatnonzero(side == 0)
    mask = np.zeros(n, dtype=np.int64)
    pts = np.empty(4, dtype=np.int64)
    done = 0
    while done < trials:
        u1, u2 = rng.choice(side_u, 2, replace=False)
        a, b = rng.integers(deg), rng.integers(deg)
        v1, v2 = adj[u1, a], adj[u2, b]
        if v1 == v2 or _has(adj, u1, v2) or _has(adj, u2, v1):
            continue
        pts[:] = (u1, u2, v1, v2)
        g0 = s_and_x(adj, sat); l0 = _local_sx(adj, pts, mask, sat)
        adj[u1, a] = v2; adj[u2, b] = v1; _replace(adj, v1, u1, u2); _replace(adj, v2, u2, u1)
        ok = _locally_valid(adj, pts)
        if ok:
            g1 = s_and_x(adj, sat); l1 = _local_sx(adj, pts, mask, sat)
            assert 4 * (g1[0] - g0[0]) == l1[0] - l0[0] and g1[1] - g0[1] == l1[1] - l0[1], "local dS/dX differs from global"
            done += 1
        adj[u1, a] = v1; adj[u2, b] = v2; _replace(adj, v1, u2, u1); _replace(adj, v2, u1, u2)


def point_energy(adj, sat, lam):
    n, deg = adj.shape
    e = np.zeros(n)
    for u in range(n):
        for k in range(deg):
            v = adj[u, k]
            se = _squares_on(adj, u, v)
            e[u] += 0.5 * (4.0 * (sat - se) + 4.0 * lam * max(se - sat, 0))
    return e


def main(dirs):
    print("dir rep lam | d-census (d=0..D+) | pieces below flat: size energy(1-step) min_cost_near min_cost_in verdict")
    for d in dirs:
        files = sorted(glob.glob(os.path.join(d, "*.npz")))
        for f in files:
            z = np.load(f)
            adj = z["adj"].astype(np.int64); side = z["part"].astype(np.int64); lam = float(z["lam"])
            n, deg = adj.shape; D = deg // 2; sat = 2 * D - 2
            if f == files[0]:
                check_local_is_exact(adj.copy(), side, sat)
            dd = local_dimension_d(adj)
            census = [int((dd == k).sum()) for k in range(D)] + [int((dd >= D).sum())]
            below = (dd < D - 1) if D == 3 else (dd < D)   # 3D: still on the rod rung or lower; 2D: still curled
            labels = piece_labels(adj, below) if below.any() else None
            e = point_energy(adj, sat, lam)
            side_u = np.flatnonzero(side == 0).astype(np.int64)
            out = []
            if labels is not None:
                for lab in np.unique(labels[labels >= 0]):
                    P = np.flatnonzero(labels == lab)
                    inpiece = np.zeros(n, dtype=np.int64)
                    inpiece[P] = 1
                    nb = np.unique(adj[P].ravel()); nb = nb[inpiece[nb] == 0]; inpiece[nb] = 2
                    u1 = np.array([p for p in np.flatnonzero(inpiece >= 1) if side[p] == 0], dtype=np.int64)
                    near, inside, cnt = moves_touching(adj.copy(), side_u, u1, inpiece, sat, lam)
                    e_piece = float(e[inpiece >= 1].sum())
                    verdict = "STUCK" if inside > 0 else "FALLS"
                    out.append(f"{len(P)}:{e_piece:.0f}:{near:+.1f}:{inside:+.1f}:{verdict}")
            print(os.path.basename(d), os.path.basename(f)[:-4], lam, "|", census, "|", " ".join(out) if out else "none", flush=True)


if __name__ == "__main__":
    main(sys.argv[1:])
