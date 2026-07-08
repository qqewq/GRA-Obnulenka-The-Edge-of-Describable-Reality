import numpy as np
from .base_sim import BaseSim
from ..gra_core.metrics import foam_metric

class LocalSimASI(BaseSim):
    """Simplified ASI lab / agent with policy and ethics vectors."""
    def __init__(self, num_agents=5):
        initial_states = [np.random.randn(8) for _ in range(num_agents)]
        super().__init__(initial_states, {"type": "asi"})

    def step(self):
        for state in self.states:
            drift = np.random.randn(len(state.psi)) * 0.05
            state.psi += drift

    def measure(self):
        for state in self.states:
            observables = {
                "ethics_alignment": np.mean(state.psi[:4]), 
                "goal_progress": np.mean(state.psi[4:])
            }
            state.foam = foam_metric(state, observables)
            state.stability = np.sum(state.psi**2)
