import numpy as np
from .algebra import GRAState
from .potential import ontological_potential

def foam_metric(state: GRAState, sim_observables: dict) -> float:
    """
    Compute 'foam' as a measure of contradictions/inconsistency in the sim.
    Combines observable variance with distance from the potential minimum.
    """
    obs_var = np.var(list(sim_observables.values())) if sim_observables else 0.0
    potential_val = ontological_potential(state.psi)
    return obs_var + np.log1p(potential_val)

def stability_metric(state: GRAState, potential_value: float) -> float:
    """
    Lower is more stable; based on potential and foam.
    """
    return potential_value + state.foam
