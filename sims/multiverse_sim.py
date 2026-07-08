import numpy as np
from .base_sim import BaseSim
from ..gra_core.algebra import GRAState
from ..gra_core.metrics import foam_metric
from ..gra_core.obnulenka import obnulenka

class MultiverseSim(BaseSim):
    """Aggregates multiple local sims into a higher-level GRA state."""
    def __init__(self, local_sims):
        self.local_sims = local_sims
        super().__init__([], {"type": "multiverse"})
        self.multiverse_state = None

    def step(self):
        for sim in self.local_sims:
            sim.step()
            sim.measure()

        if not self.local_sims:
            return

        states_to_combine = [sim.states[0] for sim in self.local_sims if sim.states]
        if not states_to_combine:
            return

        # Align shapes for GRA combination
        min_len = min(len(s.psi) for s in states_to_combine)
        states_to_combine = [GRAState(s.psi[:min_len], s.level, s.meta) for s in states_to_combine]

        combined = states_to_combine[0]
        for s in states_to_combine[1:]:
            combined = combined.combine(s)  # GRA (x) GRA

        self.multiverse_state = combined

    def measure(self):
        if self.multiverse_state:
            observables = {"level": self.multiverse_state.level}
            self.multiverse_state.foam = foam_metric(self.multiverse_state, observables)
            self.multiverse_state.stability = np.sum(self.multiverse_state.psi**2)

    def apply_obnulenka(self, threshold=1.0):
        if self.multiverse_state:
            self.multiverse_state = obnulenka(self.multiverse_state, self.multiverse_state.foam, threshold)
