import numpy as np
def f(x):
    return np.sqrt(1+x**4)
def legend_poly(n, x):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return ((2 * n - 1) * x * legend_poly(n - 1, x) - (n - 1) *legend_poly(n - 2, x)) / n

def legend_roots(n):
    # Initial approximation of roots using Chebyshev nodes
    x = np.cos(np.pi * (4 * np.arange(1, n + 1) - 1) / (4 * n + 2))
    # Improved approximation using Newton's method
    for i in range(5): # Iterate for refinement (adjust the number ofiterations as needed)
        x -= legend_poly(n, x) / legend_poly_deriv(n, x)

    return x

def legend_poly_deriv(n, x):
    return n / (x**2 - 1) * (x * legend_poly(n, x) -legend_poly(n - 1, x))

def main(f,a, b, n):
# Compute Legendre roots and weights
    roots = legend_roots(n)
    weights = 2 / ((1 - roots**2) * legend_poly_deriv(n, roots)**2)

# Map the roots to the interval [a, b]
    mapped_roots = 0.5 * (b - a) * roots + 0.5 * (a + b)

    # Perform the Gaussian quadrature integration
    result = np.sum(weights * f(mapped_roots))
    return ( 0.5 * (b - a) * result)
