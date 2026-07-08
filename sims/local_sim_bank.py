import numpy as np
from .base_sim import BaseSim
from ..gra_core.metrics import foam_metric

class LocalSimBank(BaseSim):
    """Simple model of a bank / payment system."""
    def __init__(self, num_accounts=10):
        initial_states = [np.random.randn(5) for _ in range(num_accounts)]
        super().__init__(initial_states, {"type": "bank"})

    def step(self):
        for state in self.states:
            transactions = np.random.randn(len(state.psi)) * 0.1
            state.psi += transactions

    def measure(self):
        for state in self.states:
            observables = {
                "balance_mean": np.mean(state.psi), 
                "balance_var": np.var(state.psi)
            }
            state.foam = foam_metric(state, observables)
            state.stability = np.sum(state.psi**2)
