# Multiverse Hierarchy

## Levels of Simulation
The architecture is strictly hierarchical:
1. **Local Sims**: Represent specific domains (e.g., economics in `LocalSimBank`, ethics in `LocalSimASI`). They operate on low-dimensional state vectors.
2. **Multiverse Sim**: Aggregates local sims. It uses the GRA `combine()` method to project local states into a higher-level ontological state.
3. **Meta-Level (Future)**: The multiverse state itself can be fed into an even higher-level sim, creating a fractal hierarchy of reality.

## Extending the Hierarchy
To add a new level:
1. Create a new sim class inheriting from `BaseSim`.
2. Implement `step()` to define local dynamics.
3. Implement `measure()` to calculate local foam.
4. Add it to a `MultiverseSim` instance to be aggregated.
