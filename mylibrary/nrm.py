# Newton-Raphson multivariable

def matrix_multiply(A, B):
    """Multiply two matrices."""
    rows_A, cols_A = len(A), len(A[0])
    cols_B = len(B[0])
    result = [[0] * cols_B for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result

def vector_addition(a, b):
    """Add two vectors element-wise."""
    return [ai + bi for ai, bi in zip(a, b)]

def scalar_multiply(scalar, vector):
    """Multiply a scalar by a vector."""
    return [scalar * vi for vi in vector]

def transpose(matrix):
    """Transpose a matrix."""
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def newton_raphson_system(F, J, x0, tol=1e-6, max_iter=100):
    """
    Newton-Raphson method for solving a system of nonlinear equations.

    Parameters:
    - F: Function representing the system of equations (returns a vector).
    - J: Function representing the Jacobian matrix of the system.
    - x0: Initial guess for the solution.
    - tol: Tolerance for convergence.
    - max_iter: Maximum number of iterations.

    Returns:
    - x: Solution vector.
    - iterations: Number of iterations performed.
    """

    x = x0.copy()
    iterations = 0

    while iterations < max_iter:
        F_val = F(x)
        J_val = J(x)

        # Solve J_val * delta_x = -F_val
        delta_x = solve_system(J_val, scalar_multiply(-1, F_val))

        x = vector_addition(x, delta_x)

        # Check for convergence
        if max(abs(dx) for dx in delta_x) < tol:
            break

        iterations += 1

    return x, iterations

def solve_system(A, b):
    """Solve a system of linear equations Ax = b."""
    n = len(A)
    augmented_matrix = [row + [bi] for row, bi in zip(A, b)]

    # Gaussian elimination
    for i in range(n):
        # Make the diagonal element 1
        factor = 1.0 / augmented_matrix[i][i]
        augmented_matrix[i] = scalar_multiply(factor, augmented_matrix[i])

        # Eliminate other elements in the column
        for j in range(i + 1, n):
            factor = augmented_matrix[j][i]
            augmented_matrix[j] = vector_addition(augmented_matrix[j], scalar_multiply(-factor, augmented_matrix[i]))

    # Back-substitution
    x = [row[-1] for row in augmented_matrix]
    for i in range(n - 1, 0, -1):
        for j in range(i):
            factor = augmented_matrix[j][i]
            augmented_matrix[j] = vector_addition(augmented_matrix[j], scalar_multiply(-factor, augmented_matrix[i]))

    return [row[-1] for row in augmented_matrix]

# Example: Solve a system of nonlinear equations
def system_of_equations(x):
    # Define the system of equations
    f1 = x[0]**2 + x[1]**2 - 1
    f2 = x[0] - x[1]

    return [f1, f2]

def jacobian_matrix(x):
    # Define the Jacobian matrix of the system
    df1_dx0 = 2 * x[0]
    df1_dx1 = 2 * x[1]
    df2_dx0 = 1
    df2_dx1 = -1

    return [[df1_dx0, df1_dx1], [df2_dx0, df2_dx1]]

# Initial guess
initial_guess = [1.0, 0.0]

# Solve the system using Newton-Raphson method
solution, iterations = newton_raphson_system(system_of_equations, jacobian_matrix, initial_guess)

print("Solution:", solution)
print("Iterations:", iterations)
