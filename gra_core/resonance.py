import numpy as np
from .algebra import GRAState

def resonance_step(state: GRAState, grad_U: np.ndarray, eta: float = 0.01) -> GRAState:
    """
    dPsi/dt = R(Psi, nabla U)
    Perform one resonance update step (gradient descent in ontological potential).
    """
    new_psi = state.psi - eta * grad_U
    new_state = GRAState(new_psi, level=state.level, meta=state.meta.copy())
    return new_state
