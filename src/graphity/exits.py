"""Counting every exit from the curled torus, and every fall-back into it (PREREGISTRATION T22).

WHY. Eq. (2) of the curled-torus paper predicts the time to the *first* exit from the perfect 4 x L torus.
Near lambda = 1 the measured waits run longer than that, and one reading is that some exits fall back into
the torus instead of growing into a front. Checking it needs every exit seen, including one that heals within
a sweep, so this counts move by move rather than sweep by sweep.

THE MOVE. The kernel's own (cqg.run_chain): two points of side 0 each swap one partner, Metropolis at coupling
g, the hard-core rule enforced by `is_valid`. Energies are recomputed in full at every accepted candidate,
which is simple and exact (the arrangements here have N <= 96).

WHAT IS COUNTED. The torus state is S = 5N/4 and X = N exactly (moves that keep both, which exist, leave it a
torus). An **exit** is an accepted move out of that state; a **fall-back** an accepted move back into it. The run
stops when the conversion fraction (5N/4 - S) / (N/4) first reaches `stop_fraction` (the change has gone
through), or after `max_sweeps`. Returns (exits, fallbacks, attempts to the first exit, attempts to the end,
went_through).
"""
import numpy as np
from numba import njit

from graphity.cqg import _switch, has_edge, is_valid, surplus, total_squares


@njit(cache=True)
def _energy(adj, lam):
    return 16.0 * (adj.shape[0] - total_squares(adj)) + 4.0 * lam * surplus(adj)


@njit(cache=True)
def run_until_through(adj, side_u, g, lam, cap, max_sweeps, seed, stop_fraction):
    np.random.seed(seed)
    n = adj.shape[0]
    nu = side_u.shape[0]
    s_tube = 5 * n // 4
    x_tube = n
    s_stop = s_tube - stop_fraction * (n / 4.0)
    s = total_squares(adj)
    x = surplus(adj)
    h = 16.0 * (n - s) + 4.0 * lam * x
    in_tube = s == s_tube and x == x_tube
    exits = 0
    fallbacks = 0
    first_exit = -1
    attempt = 0
    trial = adj.copy()
    for _ in range(max_sweeps * 2 * n):
        attempt += 1
        u1 = side_u[np.random.randint(0, nu)]
        u2 = side_u[np.random.randint(0, nu)]
        v1 = adj[u1, np.random.randint(0, 4)]
        v2 = adj[u2, np.random.randint(0, 4)]
        if u1 == u2 or v1 == v2 or has_edge(adj, u1, v2) or has_edge(adj, u2, v1):
            continue
        trial[:] = adj
        _switch(trial, u1, v1, u2, v2)
        if not is_valid(trial, cap):
            continue
        s_new = total_squares(trial)
        x_new = surplus(trial)
        h_new = 16.0 * (n - s_new) + 4.0 * lam * x_new
        d_h = h_new - h
        if d_h > 0 and np.random.random() >= np.exp(-d_h / g):
            continue
        adj[:] = trial
        s, x, h = s_new, x_new, h_new
        now_tube = s == s_tube and x == x_tube
        if in_tube and not now_tube:
            exits += 1
            if first_exit < 0:
                first_exit = attempt
        elif now_tube and not in_tube:
            fallbacks += 1
        in_tube = now_tube
        if s <= s_stop:
            return exits, fallbacks, first_exit, attempt, True
    return exits, fallbacks, first_exit, attempt, False
