import numpy as np

class GRAState:
    def __init__(self, psi, level=0, meta=None):
        self.psi = np.array(psi, dtype=float)
        self.level = level
        self.meta = meta or {}
        self.foam = 0.0
        self.stability = 0.0

    def combine(self, other: "GRAState") -> "GRAState":
        """
        GRA (x) GRA = sqrt(GRA)-style combination:
        returns a new state with compressed 'ontological weight'.
        """
        if self.psi.shape != other.psi.shape:
            raise ValueError("States must have the same shape to combine.")

        # Non-linear transform: average with compression
        psi_new = (self.psi + other.psi) / 2.0
        psi_new = np.tanh(psi_new)  # Dimensionality/norm reduction

        new_level = max(self.level, other.level) + 1
        return GRAState(psi_new, level=new_level, meta={"combined": True})
