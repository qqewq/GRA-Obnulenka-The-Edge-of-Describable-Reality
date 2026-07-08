import numpy as np
from ..gra_core.algebra import GRAState
from ..gra_core.obnulenka import obnulenka

class BaseSim:
    def __init__(self, states, params=None):
        self.states = [GRAState(s) if not isinstance(s, GRAState) else s for s in states]
        self.params = params or {}
        self.history = []

    def step(self):
        raise NotImplementedError("Subclasses must implement step()")

    def measure(self):
        raise NotImplementedError("Subclasses must implement measure()")

    def apply_obnulenka(self, threshold=0.5):
        for i, state in enumerate(self.states):
            self.states[i] = obnulenka(state, state.foam, threshold)
