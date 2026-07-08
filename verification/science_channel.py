import matplotlib.pyplot as plt
import os

def plot_metrics(results, output_dir="output"):
    os.makedirs(output_dir, exist_ok=True)

    plt.figure(figsize=(10, 5))
    plt.plot(results["foam_history"], label="Foam (Contradictions)", color="red")
    plt.plot(results["stability_history"], label="Stability", color="blue")
    plt.axhline(y=1.5, color='k', linestyle='--', label="Obnulenka Threshold")
    plt.title(f"Verification Metrics: {results['hypothesis']}")
    plt.xlabel("Simulation Step")
    plt.ylabel("Metric Value")
    plt.legend()
    plt.grid(True)

    filepath = os.path.join(output_dir, f"{results['hypothesis'].replace(' ', '_')}_metrics.png")
    plt.savefig(filepath)
    plt.close()
    return filepath
