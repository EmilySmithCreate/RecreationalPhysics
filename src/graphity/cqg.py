"""2D combinatorial quantum gravity (CQG): Monte Carlo on incompressible graphs.

Model, as we read it from the sources (keys in REFERENCES.bib):

* Configuration space: 4-regular graphs on N vertices in which short cycles
  (triangles, squares, pentagons) share at most one edge ("incompressible" /
  hard-core condition) [T22 Sec. "Combinatorial quantum gravity"; T24 Eq. (1)].
* Energy: total Ollivier-Ricci curvature. On these graphs the edge curvature
  is  kappa = T/2D - [1-(2+T+S)/2D]_+ - [1-(2+T+S+P)/2D]_+  [T22 Eq. (2)].
* Simplification used in the published simulations: bipartite graphs only
  (no triangles or pentagons can occur) [T24, text below Eq. (4); KTB19
  Sec. 3.1.1], and no edge carrying more than 2D-2 = 2 squares [KTB19
  Sec. 3.1.1, as we read it].
* Weight exp(-H/g) with g the coupling, playing the role of temperature
  [T24 Eq. (1)].

ASSUMPTION Q1 (energy, derived by us from [T22 Eq. (2)] with D = 2, T = P = 0):
    kappa(e) = -(2 - S_e)_+ / 2,
    H = -4 sum_i sum_{j~i} kappa(ij) = 4 sum_e (2 - S_e)_+
      = 16 (N - S) + 4 sum_e (S_e - 2)_+ .
  With the cap S_e <= 2 the last term vanishes and H = 16 (N - S), which
  matches the published global term [T24 Eq. (4)] and the mean-field action
  8ND(D-1)(1 - phi) of [KTB19 Eq. (35)] at D = 2. Checks: random graph
  (S ~ 0) gives H = 16N; the square-lattice torus (S = N) gives H = 0.

ASSUMPTION Q2 (hard-core rule, derived by us): in a bipartite graph two
  distinct squares can share two edges only if the edges are adjacent, which
  makes a K_{2,3}. So "incompressible" is equivalent to "no two vertices have
  more than two common neighbours". Not yet checked against the excluded
  subgraphs drawn in [KTB19 Fig. 2].

ASSUMPTION Q3 (why the cap matters): without the cap the 4-cube Q4 (= 4x4
  torus) has S/N = 1.5 and S_e = 3; by Q1 its energy is 0, degenerate with the
  flat torus. Imposing S_e <= 2 removes it, and then S <= N with equality for
  the torus. The soft (uncapped) version of the model is parked.

ASSUMPTION Q4 (move): bipartite edge switch (u1,v1),(u2,v2) -> (u1,v2),(u2,v1).
  [KTB19 Sec. 4] says "edge switches"; details not given there. Proposal is
  symmetric (two edges chosen uniformly; the reverse move picks the two new
  edges with the same probability), moves leading outside the configuration
  space are rejected, so Metropolis acceptance satisfies detailed balance
  [NB99]. Ergodicity inside the constrained space is NOT established (O2).
  Connectedness is not enforced.

ASSUMPTION Q5 (start state): an lx x ly periodic square lattice, both sides
  even and >= 6, melted by running at infinite temperature. Ours.
"""
import numpy as np
from numba import njit

CAP = 2            # max squares per edge, 2D - 2 with D = 2   (Q3)
MAX_CODEGREE = 2   # no K_{2,3}                                  (Q2)
ENERGY_PER_SQUARE = 16.0   # H = 16 (N - S)                      (Q1)


def torus(lx: int, ly: int = None):
    """Adjacency (N,4) and bipartition (0/1 per vertex) of the lx x ly torus.

    torus(L) is the L x L torus. Both sides must be even, so that the lattice is
    bipartite, and >= 6: a side of 4 closes a 4-cycle around the torus, which puts
    three squares on half the edges and breaks the cap (checked by brute force:
    4 x 6 has S = 1.25 N). The 4 x 4 case is the 4-cube of Q3.
    """
    if ly is None:
        ly = lx
    if lx % 2 or ly % 2 or min(lx, ly) < 6:
        raise ValueError("both sides must be even and >= 6 (a side of 4 wraps into extra "
                         "squares; the 4x4 torus is the 4-cube, see Q3)")
    n = lx * ly
    adj = np.empty((n, 4), dtype=np.int64)
    part = np.empty(n, dtype=np.int64)
    for x in range(lx):
        for y in range(ly):
            i = x * ly + y
            adj[i] = [((x + 1) % lx) * ly + y, ((x - 1) % lx) * ly + y,
                      x * ly + (y + 1) % ly, x * ly + (y - 1) % ly]
            part[i] = (x + y) % 2
    return adj, part


@njit(cache=True)
def has_edge(adj, a, b):
    for k in range(4):
        if adj[a, k] == b:
            return True
    return False


@njit(cache=True)
def squares_on_edge(adj, u, v):
    """Number of 4-cycles u - v - a - b - u containing the edge (u, v)."""
    count = 0
    for i in range(4):
        a = adj[v, i]
        if a < 0 or a == u:
            continue
        for j in range(4):
            b = adj[u, j]
            if b < 0 or b == v:
                continue
            if has_edge(adj, a, b):
                count += 1
    return count


@njit(cache=True)
def codegree(adj, x, y):
    c = 0
    for i in range(4):
        a = adj[x, i]
        if a >= 0 and has_edge(adj, y, a):
            c += 1
    return c


@njit(cache=True)
def total_squares(adj):
    s = 0
    for u in range(adj.shape[0]):
        for k in range(4):
            v = adj[u, k]
            if v > u:
                s += squares_on_edge(adj, u, v)
    return s // 4          # every square is seen from each of its 4 edges


@njit(cache=True)
def is_valid(adj):
    """4-regular, simple, codegree <= 2 everywhere, squares per edge <= CAP."""
    n = adj.shape[0]
    for u in range(n):
        for k in range(4):
            v = adj[u, k]
            if v < 0 or v == u or not has_edge(adj, v, u):
                return False
            for m in range(k + 1, 4):
                if adj[u, m] == v:
                    return False
            if squares_on_edge(adj, u, v) > CAP:
                return False
            for m in range(4):          # pairs at distance two through v
                w = adj[v, m]
                if w != u and codegree(adj, u, w) > MAX_CODEGREE:
                    return False
    return True


@njit(cache=True)
def _replace(adj, u, old, new):
    for k in range(4):
        if adj[u, k] == old:
            adj[u, k] = new
            return


@njit(cache=True)
def _new_edge_ok(adj, p, q):
    """Constraints that adding edge (p, q) could have broken."""
    for k in range(4):
        x = adj[q, k]
        if x != p and codegree(adj, p, x) > MAX_CODEGREE:
            return False
        y = adj[p, k]
        if y != q and codegree(adj, q, y) > MAX_CODEGREE:
            return False
    if squares_on_edge(adj, p, q) > CAP:
        return False
    for i in range(4):                  # other edges of every square through (p, q)
        a = adj[q, i]
        if a == p:
            continue
        for j in range(4):
            b = adj[p, j]
            if b == q:
                continue
            if has_edge(adj, a, b):
                if (squares_on_edge(adj, q, a) > CAP or squares_on_edge(adj, a, b) > CAP
                        or squares_on_edge(adj, b, p) > CAP):
                    return False
    return True


@njit(cache=True)
def run_chain(adj, side_u, inv_g, n_equil, n_meas, seed):
    """Metropolis chain at coupling g = 1 / inv_g. Modifies adj in place.

    side_u : array of the vertices in one half of the bipartition.
    Returns (squares after each measurement sweep, acceptance rate).
    One sweep = 2N attempted switches (one per edge).
    """
    np.random.seed(seed)
    n = adj.shape[0]
    nu = side_u.shape[0]
    s = total_squares(adj)
    out = np.zeros(n_meas, dtype=np.int64)
    attempted = 0
    accepted = 0
    for sweep in range(n_equil + n_meas):
        for _ in range(2 * n):
            attempted += 1
            u1 = side_u[np.random.randint(0, nu)]
            v1 = adj[u1, np.random.randint(0, 4)]
            u2 = side_u[np.random.randint(0, nu)]
            v2 = adj[u2, np.random.randint(0, 4)]
            if u1 == u2 or v1 == v2 or has_edge(adj, u1, v2) or has_edge(adj, u2, v1):
                continue
            lost = squares_on_edge(adj, u1, v1)
            _replace(adj, u1, v1, -1)
            _replace(adj, v1, u1, -1)
            lost += squares_on_edge(adj, u2, v2)
            _replace(adj, u2, v2, -1)
            _replace(adj, v2, u2, -1)
            _replace(adj, u1, -1, v2)
            _replace(adj, v2, -1, u1)
            gained = squares_on_edge(adj, u1, v2)
            _replace(adj, u2, -1, v1)
            _replace(adj, v1, -1, u2)
            gained += squares_on_edge(adj, u2, v1)
            d_s = gained - lost
            ok = _new_edge_ok(adj, u1, v2) and _new_edge_ok(adj, u2, v1)
            if ok:
                d_h = -ENERGY_PER_SQUARE * d_s
                if d_h > 0.0 and np.random.random() >= np.exp(-inv_g * d_h):
                    ok = False
            if ok:
                s += d_s
                accepted += 1
            else:
                _replace(adj, u1, v2, v1)
                _replace(adj, v1, u2, u1)
                _replace(adj, u2, v1, v2)
                _replace(adj, v2, u1, u2)
        if sweep >= n_equil:
            out[sweep - n_equil] = s
    return out, accepted / max(attempted, 1)
