import sys
import os
import numpy as np

# Setup path to import from root
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from hypotheses.hypothesis_example_physics import HypothesisPhysics
from verification.pipeline import VerificationPipeline
from verification.science_channel import plot_metrics
from verification.art_channel import generate_artifacts_from_sim
from art.visualizer import visualize_field
from gra_core.algebra import GRAState

def main():
    print("--- Running Physics Hypothesis (Double-Well Phase Transition) ---")
    hyp = HypothesisPhysics()
    pipeline = VerificationPipeline(hyp, steps=50)
    results = pipeline.run()

    print(f"Success: {results['success']}")
    print(f"Obnulenka Resets: {results['resets']}")

    plot_path = plot_metrics(results)
    print(f"Science plot saved to: {plot_path}")

    # Generate Artifacts
    dummy_state_psi = np.random.randn(100) * (results["foam_history"][-1] + 0.1)
    dummy_state = GRAState(dummy_state_psi)

    artifacts = generate_artifacts_from_sim(dummy_state)
    if "field_data" in artifacts:
        viz_path = visualize_field(artifacts["field_data"])
        print(f"Art visual saved to: {viz_path}")

if __name__ == "__main__":
    main()
