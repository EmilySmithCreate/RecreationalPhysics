"""A look (sandbox lane; the owner's objection of 30 October to T86: "why can't an amplitude start at the cube or diagonal
level?"). The wave rule (adopted this day) on light's network of the six-link space: the points of an L x L x L torus joined
by body-diagonal steps (eight per point; VISION Update 142, light travels through the body diagonals), each step's hopping
weight 1/l^2 with l the derived diagonal length of its cube (graphity.diagonals; sqrt 3 on flat space). A knot (T85's
one-switch knot, seed 20268501, charges (8, 8, 8)) curls six links; the curl's halo lengthens the edges round it with one
constant alpha (graphity.lengths.relax) and so the diagonals, which weakens the hopping there. That halo is the only thing
in this model that could confine an amplitude: it is the ingredient O169 said the two-dimensional toy lacked.

Measures (as T86): MODE, the largest share of any eigenspace of the weighted Laplacian on the object (the points within
two diagonal steps of the knot's four points); STAY, the probability on the object at t = (pi/2) l0^2 and pi l0^2 after
starting on the knot's points (l0^2 = 3, so the clock matches a unit-hopping lattice). Control: alpha = 0 (flat halo, the
same object), where MODE is exactly |object|/N by translation symmetry.

WRITTEN BEFORE COMPUTING (ours): at alpha = -0.5 (the value T84 and T85 ran) the halo changes diagonals by a few per cent
and nothing is confined: MODE and STAY within 20 % of the alpha = 0 control. Confinement, if it comes, comes with |alpha|
of order the stiffness, and the look scans alpha = -0.5, -1.5 (near the alpha* the gamma test pinned, O168), -3, -6: we
expect STAY to rise with |alpha| but MODE to stay below 0.5 through -3. If MODE >= 0.5 at -1.5, the gamma-pinned halo
confines, which would be a candidate carrier at her level with no new constant, and rule 13 would apply. Reported beside:
the largest diagonal lengthening at each alpha. Crowns nothing; the strict-lane test is designed from this.
"""
import sys
from itertools import product
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))
from graphity import diagonals, lengths              # noqa: E402
from graphity.cqg_d import torus                      # noqa: E402
from t85_gamma import make_knot                       # noqa: E402

L, SEED, ALPHAS, L0SQ = 12, 20268501, (0.0, -0.5, -1.5, -3.0, -6.0), 3.0
SIGNS = [np.array(s) for s in product((1, -1), repeat=3)]


def diagonal_laplacian(diag):
    dims = np.array(diag.shape)
    n = int(np.prod(dims))
    coords = np.array(np.unravel_index(np.arange(n), dims)).T
    idx = {tuple(c): i for i, c in enumerate(coords)}
    W = np.zeros((n, n))
    for p in range(n):
        for s in SIGNS:
            cube = tuple(np.mod(coords[p] + np.minimum(s, 0), dims))
            q = idx[tuple(np.mod(coords[p] + s, dims))]
            W[p, q] += 1.0 / diag[cube] ** 2
    return np.diag(W.sum(axis=1)) - W, coords, idx


def ball_steps(coords, idx, dims, anchors, steps):
    seen = {int(a) for a in anchors}
    edge = set(seen)
    for _ in range(steps):
        new = set()
        for p in edge:
            for s in SIGNS:
                new.add(idx[tuple(np.mod(coords[p] + s, dims))])
        edge = new - seen
        seen |= edge
    return sorted(seen)


def mode_and_stay(lap, start, obj, times):
    w, v = np.linalg.eigh(lap)
    best, i = 0.0, 0
    while i < len(w):
        j = i
        while j + 1 < len(w) and abs(w[j + 1] - w[i]) < 1e-9:
            j += 1
        sub = v[obj, i:j + 1]
        best = max(best, float(np.sum(sub * sub)) / (j + 1 - i))
        i = j + 1
    stays = []
    for t in times:
        tot = 0.0
        for s in start:
            psi = v @ (np.exp(-1j * w * t) * v[s, :])
            tot += float(np.sum(np.abs(psi[obj]) ** 2))
        stays.append(tot / len(start))
    return best, stays


if __name__ == "__main__":
    dims = (L, L, L)
    adj, part = torus(dims)
    n = adj.shape[0]
    coords = np.array(np.unravel_index(np.arange(n), dims)).T
    idx = {tuple(c): i for i, c in enumerate(coords)}
    rng = np.random.default_rng(SEED)
    quad = make_knot(adj, coords, idx, L, rng)
    f = lengths.curl_fields(adj, dims)
    print("knot points %s; family charges %s" % (quad, [float(x) for x in f.sum(axis=(1, 2, 3))]))
    times = [(np.pi / 2) * L0SQ, np.pi * L0SQ]
    for alpha in ALPHAS:
        delta, _ = lengths.relax(f, alpha)
        diag = diagonals.diagonal_lengths(delta)
        lap, coords, idx = diagonal_laplacian(diag)
        obj = ball_steps(coords, idx, np.array(dims), quad, 2)
        mode, stays = mode_and_stay(lap, list(quad), obj, times)
        print("alpha %5.2f: largest diagonal lengthening %+.3f (flat %.3f); object %d points (|obj|/N = %.3f); MODE %.3f; STAY(pi/2) %.3f, STAY(pi) %.3f" % (
            alpha, float(diag.max() - np.sqrt(3)), np.sqrt(3), len(obj), len(obj) / n, mode, stays[0], stays[1]))
    print("Crowns nothing.")


def mode_detail(lap, obj, inner):
    """(eigenvalue, degeneracy, share on obj, share on inner, inverse participation) of the eigenspace with the largest share on obj."""
    w, v = np.linalg.eigh(lap)
    best, i = None, 0
    while i < len(w):
        j = i
        while j + 1 < len(w) and abs(w[j + 1] - w[i]) < 1e-9:
            j += 1
        sub = v[obj, i:j + 1]
        share = float(np.sum(sub * sub)) / (j + 1 - i)
        if best is None or share > best[2]:
            inner_share = float(np.sum(v[inner, i:j + 1] ** 2)) / (j + 1 - i)
            ipr = float(np.sum(v[:, i] ** 4))
            best = (float(w[i]), j + 1 - i, share, inner_share, ipr)
        i = j + 1
    return best


def checks():
    """Controls written AFTER the first run above showed MODE 0.77 at alpha = -0.5 (so these are checks of a surprise, not
    predictions): (a) the best mode's eigenvalue and degeneracy, and the flat lattice's degeneracy at that level; (b) the same
    measure with a RANDOM lengthening field of the knot halo's rms and no knot; (c) the best mode's weight on the knot's four
    points and on the one-step ball, and its inverse participation (1/number of points it effectively lives on)."""
    dims = (L, L, L)
    adj, part = torus(dims)
    n = adj.shape[0]
    coords = np.array(np.unravel_index(np.arange(n), dims)).T
    idx = {tuple(c): i for i, c in enumerate(coords)}
    rng = np.random.default_rng(SEED)
    quad = make_knot(adj, coords, idx, L, rng)
    f = lengths.curl_fields(adj, dims)
    lap0, _, _ = diagonal_laplacian(diagonals.diagonal_lengths(np.zeros_like(f)))
    w0 = np.linalg.eigvalsh(lap0)
    levels, counts = np.unique(np.round(w0, 6), return_counts=True)
    print("(a) flat lattice: %d distinct levels among %d; the five most degenerate: %s" % (
        len(levels), n, sorted(zip(counts, levels), reverse=True)[:5]))
    obj = ball_steps(coords, idx, np.array(dims), quad, 2)
    inner = ball_steps(coords, idx, np.array(dims), quad, 1)
    for alpha in (-0.5, -1.5):
        delta, _ = lengths.relax(f, alpha)
        lap, _, _ = diagonal_laplacian(diagonals.diagonal_lengths(delta))
        ev, deg, share, inner_share, ipr = mode_detail(lap, obj, inner)
        near = levels[np.argmin(np.abs(levels - ev))]
        print("   alpha %.1f knot halo: best mode at eigenvalue %.4f (degeneracy %d; nearest flat level %.4f with degeneracy %d); share on 2-step ball %.3f, on 1-step ball %.3f, on the 4 knot points %.3f; lives on about %.0f points" % (
            alpha, ev, deg, near, counts[np.argmin(np.abs(levels - ev))], share, inner_share,
            float(np.sum(np.linalg.eigh(lap)[1][list(quad), np.argmin(np.abs(np.linalg.eigvalsh(lap) - ev))] ** 2)), 1 / ipr))
        rms = float(np.sqrt(np.mean(delta ** 2)))
        noise = rng.normal(0.0, rms, size=delta.shape)
        lapn, _, _ = diagonal_laplacian(diagonals.diagonal_lengths(noise))
        evn, degn, sharen, inner_n, iprn = mode_detail(lapn, obj, inner)
        print("   (b) random lengthening of the same rms (%.4f), no knot: best mode share on the same 2-step ball %.3f, 1-step %.3f, lives on about %.0f points" % (
            rms, sharen, inner_n, 1 / iprn))


if __name__ == "__main__":
    checks()
