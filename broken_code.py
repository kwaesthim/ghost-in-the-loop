import numpy as np

def glitch_qubit():
    # Incomplete transformation
    state = np.array([0.6, 0.9])  # Not normalized
    h_gate = hadamard()
    return np.matmul(h_gate, state)  # Dimensional mismatch?

def hadamard():
    return np.array([[1, 1], [1, -1]])  # Missing normalization
