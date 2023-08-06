import numpy as np
from numba import jit


@jit(nopython=True)
def combine_taggers(decs, omegas):
    # events with omega > 0.5 do not contribute with information in combinations
    for t, omega in enumerate(omegas):
        ignore = omega > 0.5
        omegas[t][ignore] = 0.5
        decs[t][ignore] = 0

    # Tagger combination algorithm
    NT = len(omegas)
    p_b    = np.array([np.prod((1 + decs[i]) / 2 - decs[i] * (1 - omegas[i])) for i in range(NT)])
    p_bbar = np.array([np.prod((1 - decs[i]) / 2 + decs[i] * (1 - omegas[i])) for i in range(NT)])

    P_b = p_b / (p_b + p_bbar)

    dec_minus = P_b > 1 - P_b
    dec_plus  = P_b < 1 - P_b

    d_combined = np.zeros(len(decs))
    d_combined[dec_minus] = -1
    d_combined[dec_plus]  = +1

    omega_combined = 0.5 * np.ones(len(decs))
    omega_combined[dec_minus] = 1 - P_b[dec_minus]
    omega_combined[dec_plus]  = P_b[dec_plus]

    return d_combined, omega_combined
