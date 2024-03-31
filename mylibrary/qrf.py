import numpy as np
import math

def matrix_matrix_multiplication(A,B):
    # Check if the matrices are compatible for multiplication
    if len(A[0]) != len(B):
        raise ValueError("Number of columns in A must be equal to the number of rows in B")

    # Initialize the resultant matrix with zeros
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    # Perform matrix multiplication
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return np.array(result)

def vector_vector_multiplication(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ValueError("Vectors must be of the same length.")
    
    result = 0

    for i in range(len(vector1)):
        result += vector1[i] * vector2[i]

    return result

def matrix_transpose(A):
    n=len(A)
    M=np.array(A)
    for i in range(n):
        for j in range (n):
            M[i][j]=A[j][i]
    return M

def check_upper(A):
    n=len(A)
    for i in range(n):
        for j in range(i-1):
            if abs(A[i][j])>=10**-6:
                return 1
    return 0

def qmatrix(A):
    m, n = A.shape
    Q = np.zeros((m, n))
    R = np.zeros((n, n))

    for j in range(n):
        v = A[:, j]
        for i in range(j):
            R[i, j] = vector_vector_multiplication(Q[:, i], A[:, j])
            v = v - R[i, j] * Q[:, i]
        R[j, j] = np.sqrt(vector_vector_multiplication(v,v))
        Q[:, j] = v / R[j, j]

    return Q

def main(A):
    A=np.array(A)
    n=len(A)
    while (check_upper(A)==1):
        Q=qmatrix(A)
        Ak=matrix_matrix_multiplication(matrix_transpose(Q),matrix_matrix_multiplication(A,Q))
        A=np.array(Ak)
    
    print("\nThe eigenvalues of the given matrix using QR factorisation method(Gram Schmidt orthogonalisation) are:\n")
    for i in range(n):
        print("Eigenvalue",(i+1),":",A[i][i])
    
    return
    
