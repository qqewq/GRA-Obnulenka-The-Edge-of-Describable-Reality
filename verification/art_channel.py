import numpy as np
import os

def generate_artifacts_from_sim(multiverse_state, output_dir="output"):
    os.makedirs(output_dir, exist_ok=True)
    artifacts = {}

    if multiverse_state is None:
        return artifacts

    # Map internal sim states to a 2D field image
    psi = multiverse_state.psi
    size = int(np.ceil(np.sqrt(len(psi))))
    field = np.zeros((size, size))
    field[:len(psi)] = psi[:size*size]

    artifacts["field_data"] = field
    return artifacts
