import numpy as np
import csv

def printarray(M): #Function to print a array
  for i in range (len(M)):
    for j in range (len(M[0])):
      if M[i][j]==0:
        M[i][j]=abs(M[i][j])
      print(float(M[i][j]),end='\t\t')
    print("\n")
  print("\n") 

def input(path): #To read input matrix
  i=0
  j=0
  M=[]
  with open(path) as x:
    cr=csv.reader(x)
    next(cr)
    for line in cr:
      row=[]
      for n in line:
        row.append(float(n))
      M.append(row)
  return (np.array(M))

def matrix_transpose(A):
    n=len(A)
    M=np.array(A)
    for i in range(n):
        for j in range (n):
            M[i][j]=A[j][i]
    return M

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

def mod(R):
    n=len(R)
    sum=0
    for i in range (0,n):
        sum+=(R[i]**2)
    return np.sqrt(sum)

def vector_addition(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ValueError("Vectors must be of the same length.")
    
    result = [vector1[i] + vector2[i] for i in range(len(vector1))]
    return np.array(result)

def scalar_multiplication(scalar, vector):
    result = [scalar * element for element in vector]
    return np.array(result)

def conjugate_gradient(A,B): # Matrix Inverse function using Conjugate method
    n=len(B)
    X=np.array([0.0 for _ in range(n)])
    R=vector_addition(B,scalar_multiplication(-1,matrix_vector_multiplication(A,X)))
    D=np.array(R)
    c=1
    resi=[]
    resi.append(vector_vector_multiplication(R,R))
    while vector_vector_multiplication(R,R) >= 10**-6 :
        Alpha=vector_vector_multiplication(R,R)/(vector_vector_multiplication(D,matrix_vector_multiplication(A,D)))
        XP1 = vector_addition(X,scalar_multiplication(Alpha,D))
        RP1 = vector_addition(R,scalar_multiplication(-Alpha,matrix_vector_multiplication(A,D)))
        Beta = vector_vector_multiplication(RP1,RP1)/vector_vector_multiplication(R,R)
        DP1 = vector_addition(np.array(RP1),scalar_multiplication(Beta,D))
        X=np.array(XP1)
        R=np.array(RP1)
        D=np.array(DP1)
        c+=1
        #print(c)
        #print(Alpha)
        #print(Beta)
        resi.append(vector_vector_multiplication(R,R))
    return X,resi,c

def matrix_inverter(A):
    n=len(A)
    B=np.array([[1 if i == j else 0 for j in range(n)] for i in range(n)])
    A_inverse=[]
    R=[]
    print("\nThe input matrix A : \n")
    printarray(A)
    for i in range (0,n):
        X,R,c=conjugate_gradient(A,B[i])
        A_inverse.append(X)
        if i==0:
           R1=np.array(R)
    A_inverse=matrix_transpose(A_inverse)
    
    return A_inverse,np.array(R1)
