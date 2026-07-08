import matplotlib.pyplot as plt
import numpy as np
import os

def visualize_field(field_data, output_dir="output"):
    os.makedirs(output_dir, exist_ok=True)
    plt.figure(figsize=(6, 6))
    plt.imshow(field_data, cmap="viridis")
    plt.title("Multiverse State Field (Ontological Landscape)")
    plt.colorbar(label="Psi amplitude")
    filepath = os.path.join(output_dir, "multiverse_field.png")
    plt.savefig(filepath)
    plt.close()
    return filepath
