import numpy as np

def ontological_potential(psi: np.ndarray, A0: float = 1.0) -> float:
    """
    Compute U(psi, -A0).
    Double-well symmetry-breaking potential: U = (|psi|^2 - A0^2)^2
    """
    norm_sq = np.sum(psi**2)
    return (norm_sq - A0**2)**2

def gradient_potential(psi: np.ndarray, A0: float = 1.0) -> np.ndarray:
    """Gradient of the double-well potential (nabla U)."""
    norm_sq = np.sum(psi**2)
    return 4 * (norm_sq - A0**2) * psi

def hessian_potential(psi: np.ndarray, A0: float = 1.0) -> np.ndarray:
    """Second derivative (d2U / dpsi2) for symmetry breaking analysis."""
    norm_sq = np.sum(psi**2)
    dim = len(psi)
    H = 4 * (norm_sq - A0**2) * np.eye(dim) + 8 * np.outer(psi, psi)
    return H
