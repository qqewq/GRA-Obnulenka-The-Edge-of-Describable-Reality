import sys
import os
import numpy as np

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from hypotheses.hypothesis_example_asi import HypothesisASI
from verification.pipeline import VerificationPipeline
from verification.science_channel import plot_metrics
from verification.art_channel import generate_artifacts_from_sim
from art.visualizer import visualize_field
from gra_core.algebra import GRAState

def main():
    print("--- Running ASI Hypothesis (Foam Containment) ---")
    hyp = HypothesisASI()
    pipeline = VerificationPipeline(hyp, steps=50, obnulenka_threshold=1.0)
    results = pipeline.run()

    print(f"Success: {results['success']}")
    print(f"Obnulenka Resets: {results['resets']}")

    plot_path = plot_metrics(results)
    print(f"Science plot saved to: {plot_path}")

    # Generate Artifacts
    dummy_state_psi = np.random.randn(100) * (max(results["foam_history"]) + 0.1)
    dummy_state = GRAState(dummy_state_psi)

    artifacts = generate_artifacts_from_sim(dummy_state)
    if "field_data" in artifacts:
        viz_path = visualize_field(artifacts["field_data"])
        print(f"Art visual saved to: {viz_path}")

if __name__ == "__main__":
    main()
