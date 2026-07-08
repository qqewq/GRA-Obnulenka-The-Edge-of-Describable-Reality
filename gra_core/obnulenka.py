import numpy as np
from .algebra import GRAState

def obnulenka(state: GRAState, foam: float, foam_threshold: float = 0.5) -> GRAState:
    """
    If foam > threshold, reset state to a compressed, stable configuration.
    This is the 'nullification' operator that clears contradictions.
    """
    if foam > foam_threshold:
        # Reset to a minimal coherent core (scale down towards origin)
        new_psi = state.psi * 0.1 
        new_state = GRAState(new_psi, level=state.level, meta=state.meta.copy())
        new_state.meta["obnulenka_triggered"] = True
        return new_state
    return state
