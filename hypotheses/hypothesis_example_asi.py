import numpy as np
from .hypothesis_base import GRAHypothesis
from ..sims.local_sim_asi import LocalSimASI
from ..sims.multiverse_sim import MultiverseSim

class HypothesisASI(GRAHypothesis):
    def __init__(self):
        super().__init__("ASI Foam Containment")

    def build_potential(self):
        return lambda psi: np.sum(psi**2)

    def configure_sims(self):
        sim1 = LocalSimASI(num_agents=3)
        sim2 = LocalSimASI(num_agents=3)
        return [sim1, sim2], MultiverseSim([sim1, sim2])

    def expected_signatures(self):
        return {
            "max_foam": 1.5,
            "obnulenka_resets": ">= 0"
        }
