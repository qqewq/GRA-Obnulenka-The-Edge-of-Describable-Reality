import numpy as np
from ..gra_core.resonance import resonance_step
from ..gra_core.potential import gradient_potential

class VerificationPipeline:
    def __init__(self, hypothesis, steps=100, eta=0.05, obnulenka_threshold=1.5):
        self.hypothesis = hypothesis
        self.steps = steps
        self.eta = eta
        self.obnulenka_threshold = obnulenka_threshold
        self.results = {
            "hypothesis": hypothesis.name,
            "foam_history": [],
            "stability_history": [],
            "resets": 0,
            "success": False
        }

    def run(self):
        local_sims, multiverse_sim = self.hypothesis.configure_sims()

        for t in range(self.steps):
            # 1. Run local sims under GRA-Obnulenka dynamics
            for sim in local_sims:
                sim.step()
                for i, state in enumerate(sim.states):
                    grad = gradient_potential(state.psi)
                    sim.states[i] = resonance_step(state, grad, self.eta)
                sim.measure()

            # 2. Run multiverse sim
            multiverse_sim.step()
            if multiverse_sim.multiverse_state:
                grad = gradient_potential(multiverse_sim.multiverse_state.psi)
                multiverse_sim.multiverse_state = resonance_step(
                    multiverse_sim.multiverse_state, grad, self.eta
                )
            multiverse_sim.measure()

            # 3. Apply Obnulenka at multiverse level
            multiverse_sim.apply_obnulenka(self.obnulenka_threshold)
            if multiverse_sim.multiverse_state and multiverse_sim.multiverse_state.meta.get("obnulenka_triggered"):
                self.results["resets"] += 1
                multiverse_sim.multiverse_state.meta["obnulenka_triggered"] = False

            # 4. Measure verification metrics
            if multiverse_sim.multiverse_state:
                self.results["foam_history"].append(multiverse_sim.multiverse_state.foam)
                self.results["stability_history"].append(multiverse_sim.multiverse_state.stability)
            else:
                self.results["foam_history"].append(0)
                self.results["stability_history"].append(0)

        self._evaluate_success()
        return self.results

    def _evaluate_success(self):
        sigs = self.hypothesis.expected_signatures()
        max_foam = max(self.results["foam_history"]) if self.results["foam_history"] else 0

        if max_foam < sigs.get("max_foam", float('inf')):
            self.results["success"] = True
