import numpy as np
import csv

def printmatrix(M):
    n = len(M)
    for i in range(n):
        for j in range(n):
            if M[i, j] == 0:
                M[i, j] = abs(M[i, j])
            print(float(M[i, j]), end='\t')
        print("\n")
    print("\n")

def input(path):
    i = 0
    j = 0
    M = []
    with open(path) as x:
        cr = csv.reader(x)
        next(cr)
        for line in cr:
            row = []
            for n in line:
                row.append(float(n))
            M.append(row)
    return np.matrix(M)

def dot_product(vec1, vec2):
    # Calculate the dot product of two vectors.
    return sum(x * y for x, y in zip(vec1, vec2))

def scalar_multiply(scalar, vec):
    # Multiply a scalar with a vector.
    return [scalar * x for x in vec]

def vector_add(vec1, vec2):
    # Add two vectors.
    return [x + y for x, y in zip(vec1, vec2)]

def conjugate_gradient(A, b, x=None, tol=10**(-6)):
    # Solve a system of linear equations Ax=b using the conjugate gradient method.
    n = len(b)
    if x is None:
        x = [1.0] * n
    r = [0] * n
    for i in range(n):
        for j in range(n):
            r[i] += A[i][j] * x[j]
        r[i] = b[i] - r[i]
    p = r[:]
    rold = dot_product(r, r)

    while rold>=10**-4:
        Ap = [0] * n
        for j in range(n):
            for k in range(n):
                Ap[j] += A[j][k] * p[k]
        alpha = rold / dot_product(p, Ap)
        for j in range(n):
            x[j] += alpha * p[j]
            r[j] -= alpha * Ap[j]
        rnew = dot_product(r, r)
        if rnew < tol:
            break
        beta = rnew / rold
        for j in range(n):
            p[j] = r[j] + beta * p[j]
        rold = rnew

    return x
