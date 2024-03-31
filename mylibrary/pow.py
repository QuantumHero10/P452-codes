import numpy as np

def matrix_vector_multiplication(matrix, vector):
    if len(matrix[0]) != len(vector):
        raise ValueError("Number of columns in the matrix must be equal to the length of the vector.")
    
    result = [0 for _ in range(len(matrix))]
    
    for i in range(len(matrix)):
        for j in range(len(vector)):
            result[i] += matrix[i][j] * vector[j]
    
    return np.array(result)

def vector_matrix_multiplication(vector, matrix):
    if len(vector) != len(matrix):
        raise ValueError("Length of row vector must be equal to the number of rows in the matrix.")
    
    result = [0 for _ in range(len(matrix))]

    for i in range(len(matrix)):
        for j in range(len(vector)):
            result[i] += matrix[j][i] * vector[j]

    return np.array(result)

def vector_vector_multiplication(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ValueError("Vectors must be of the same length.")
    
    result = 0

    for i in range(len(vector1)):
        result += vector1[i] * vector2[i]

    return result


def main(A): # Main method also contains power method algorithm
    A=np.array(A)
    n=len(A)
    V=np.array([1.0 for _ in range(n)])
    AV=matrix_vector_multiplication(A,V)
    VAV=vector_vector_multiplication(V,AV)
    VV=vector_vector_multiplication(V,V)
    Lambda=VAV/VV
    Lambda1=0
    c=1
    while abs(Lambda-Lambda1)>=10**-6:
        V=np.array(AV)
        AV=matrix_vector_multiplication(A,V)
        VAV=vector_vector_multiplication(V,AV)
        VV=vector_vector_multiplication(V,V)
        Lambda1=float(Lambda)
        Lambda=VAV/VV
        c+=1
    print("\nNo. of iterations :",c)
    
    
    print("\nThe dominant eigenvalue using Power method is :",Lambda)
    return Lambda
