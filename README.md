# GRA-Obnulenka: The Edge of Describable Reality

> "This repo implements a self-verifying multiverse of simulations:  
> GRA-Obnulenka generates hypotheses and tests them using its own resonance and reset dynamics --  
> in science and in art."

## Overview
This repository formalizes the **GRA-Obnulenka** (General Resonance Architecture with Obnulenka resets) framework. It provides a complete, runnable pipeline to define scientific hypotheses, simulate them across a hierarchy of "sims" (local and multiverse), and verify them using GRA's own algebraic and reset dynamics.

## Installation
```bash
pip install -r requirements.txt
```

## Running Experiments
To run the physics phase-transition hypothesis:
```bash
python experiments/run_example_physics.py
```

To run the ASI foam-containment hypothesis:
```bash
python experiments/run_example_asi.py
```

Results (plots and artifacts) will be saved in the `output/` directory.

## Defining a New Hypothesis
1. Create a new class in `hypotheses/` inheriting from `GRAHypothesis`.
2. Implement `build_potential()`, `configure_sims()`, and `expected_signatures()`.
3. Create a runner script in `experiments/` using the `VerificationPipeline`.

## Architecture
- `gra_core/`: The mathematical engine (Algebra, Potential, Resonance, Obnulenka, Metrics).
- `sims/`: The simulation hierarchy (Local Bank, Local ASI, Multiverse).
- `hypotheses/`: Definitions of testable theories.
- `verification/`: The closed-loop pipeline, science plots, and art generation.
- `art/`: Visual and sonic mappings of the multiverse state.
