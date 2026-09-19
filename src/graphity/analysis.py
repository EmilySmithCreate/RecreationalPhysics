"""Observables and error bars.

Specific heat from energy fluctuations, C = beta^2 (<E^2> - <E>^2)
[K08, Eq. (41); CP12, Sec. IV C]. [K08, Fig. 5] plots C / N^2 with bootstrap
error bars; we do the same. Successive sweeps are correlated, so we bootstrap
over blocks of sweeps rather than single sweeps [NB99, ch. 3].
"""
import numpy as np


def specific_heat(energies: np.ndarray, beta: float) -> float:
    return beta**2 * energies.var()


def block_bootstrap(energies, beta, n_blocks=20, n_boot=500, seed=0):
    """Return (mean_E, err_E, C, err_C) using a block bootstrap."""
    rng = np.random.default_rng(seed)
    usable = len(energies) - len(energies) % n_blocks
    blocks = energies[:usable].reshape(n_blocks, -1)
    means, heats = [], []
    for _ in range(n_boot):
        sample = blocks[rng.integers(0, n_blocks, n_blocks)].ravel()
        means.append(sample.mean())
        heats.append(specific_heat(sample, beta))
    return (energies.mean(), float(np.std(means)),
            specific_heat(energies, beta), float(np.std(heats)))


def random_menu_energy_bound(k: int, r: float, l_max: int, g_b: float = 1.0) -> float:
    """Upper bound on the TOTAL ordering energy available inside a random menu.

    A uniform random k-regular graph has, in expectation and for large N,
    (k-1)^L / (2L) cycles of length L, independent of N (ASSUMPTION C1).
    A subgraph cannot contain more cycles than the menu, so the energy it can
    gain is at most  sum over energy-lowering L of |w(L)| (k-1)^L / (2L).
    Divide by N for the bound per node: it falls like 1/N (ASSUMPTION C2).

    The bound is loose (a 3-regular subgraph cannot use every menu cycle) and
    is an expectation, not a worst case.
    """
    from .energy import cycle_weights
    w = cycle_weights(r, l_max, g_b)
    return float(sum(-w[L] * (k - 1) ** L / (2 * L) for L in range(3, l_max + 1) if w[L] < 0))
