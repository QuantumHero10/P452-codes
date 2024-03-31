
# Solve the linear system to find the coefficients
def solve_linear_system(A, b):
    n = len(b)
    x = [0] * n
    for i in range(n):
        factor = A[i][i]
        for j in range(i, n):
            A[i][j] /= factor
        b[i] /= factor
        for j in range(i+1, n):
            factor = A[j][i]
            for k in range(i, n):
                A[j][k] -= A[i][k] * factor
            b[j] -= b[i] * factor
    for i in range(n-1, -1, -1):
        x[i] = b[i]
        for j in range(i+1, n):
            x[i] -= A[i][j] * x[j]
    return x

def main(A,y_data):
    # Compute the transpose of the design matrices
    A_transpose = [[row[i] for row in A] for i in range(len(A[0]))]

    # Compute A^T * A
    A_transpose_X_cubic = [[sum(A_transpose[i][k] * A_transpose[j][k] for k in range(len(A_transpose[0]))) 
                                for j in range(len(A_transpose))] 
                                for i in range(len(A_transpose))]

    # Compute A^T * y
    A_transpose_y = [sum(A_transpose[i][j] * y_data[j] for j in range(len(A_transpose[0]))) 
                        for i in range(len(A_transpose))]
    
    return solve_linear_system(A_transpose_X_cubic, A_transpose_y)
    



