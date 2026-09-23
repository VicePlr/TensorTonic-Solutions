import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    A = np.asarray(A)
    m, n = A.shape
    return np.asarray([[A[i][j] for i in range(m)] for j in range(n)])
    pass
