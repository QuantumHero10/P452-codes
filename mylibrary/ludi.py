# LUD matrix inverter

import numpy as np
import csv

def inverse_matrix(M):
    n = len(M)
    identity = [[0.0] * n for _ in range(n)]
    for i in range(n):
        identity[i][i] = 1.0

    n = len(M)
    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]

# LU decomposition
    
    for i in range(n):
        L[i][i] = 1.0
        for j in range(i, n):
            sum_val = sum(L[i][k] * U[k][j] for k in range(i))
            U[i][j] = M[i][j] - sum_val

        for j in range(i + 1, n):
            sum_val = sum(L[j][k] * U[k][i] for k in range(i))
            L[j][i] = (M[j][i] - sum_val) / U[i][i]

    MI = []
    for i in range(n):
        b = identity[i]
        n = len(L)
        y = [0.0] * n

# Forward substitution
        
        for i in range(n):
            y[i] = b[i] - sum(L[i][j] * y[j] for j in range(i))
        n = len(U)
        x = [0.0] * n

# Backward substitution
        
        for i in range(n - 1, -1, -1):
            x[i] = (y[i] - sum(U[i][j] * x[j] for j in range(i + 1, n))) / U[i][i]
        
        MI.append(x) # Inverse matrix

    return MI

def input(path): #To read augmented M
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

def main(p):
   A=input(p)
   return inverse_matrix(A)