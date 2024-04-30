import numpy as np
def power_iteration(A, num_iterations=1000, tol=1e-6):
    """Power iteration method to find the largest eigenvalue and its corresponding eigenvector."""
    n = A.shape[0]
    # Initialize a random vector
    v = np.random.rand(n)
    # Iterate
    for _ in range(num_iterations):
        Av = np.dot(A, v)
        v_new = Av / np.linalg.norm(Av)  # Normalize the vector
        # Check for convergence
        if np.linalg.norm(v_new - v) < tol:
            break
        v = v_new
    # Compute the eigenvalue
    eigenvalue = np.dot(v, np.dot(A, v)) / np.dot(v, v)
    return eigenvalue, v

def main(matrix, num_iterations, tol=1e-6):
    """Compute the eigenvalues and eigenvectors of a matrix."""
    # Initialize arrays to store eigenvalues and eigenvectors
    eigenvalues = []
    eigenvectors = []
    # Iterate over each column
    for i in range(matrix.shape[1]):
        # Construct a matrix for power iteration
        if i > 0:
            A = matrix - eigenvalues[i-1] * np.eye(matrix.shape[0])
        else:
            A = matrix
        # Apply power iteration method
        eigenvalue, eigenvector = power_iteration(A, num_iterations, tol)
        # Store the eigenvalue and eigenvector
        eigenvalues.append(eigenvalue)
        eigenvectors.append(eigenvector)
    return np.array(eigenvalues), np.array(eigenvectors)
