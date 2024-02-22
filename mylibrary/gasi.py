# Gauss siedel matrix inverter

import numpy as np
import csv
def gauss_seidel_inverse(M, epsilon=1e-10, max_iterations=1000):
    n = len(M)
    identity = [[0.0] * n for _ in range(n)]
    for i in range(n):
        identity[i][i] = 1.0

    x = [[0.0] * n for _ in range(n)]
    for i in range(n):
        x[i][i] = 1.0

    for _ in range(max_iterations):
        x_old = [row[:] for row in x]

        for i in range(n):
            sig_fw = sum(M[i][j] * x[j][k] for j in range(i) for k in range(n))
            sig_bw = sum(M[i][j] * x_old[j][k] for j in range(i + 1, n) for k in range(n))
            x[i][i] = (1 / M[i][i]) * (identity[i][i] - sig_fw - sig_bw)

        # Check for convergence
        max_diff = max(abs(x[i][j] - x_old[i][j]) for i in range(n) for j in range(n))
        if max_diff < epsilon:
            break

    return x

# Example usage:
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
   return gauss_seidel_inverse(A)
