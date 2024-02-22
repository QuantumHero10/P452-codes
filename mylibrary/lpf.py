# Leapfrog method

import numpy as np
import matplotlib.pyplot as plt

def main(f, y0, v0, t0, T, h):
    # Number of time steps
    Nt = int((T - t0) / h)

    # Initialize arrays to store results
    T = np.linspace(t0, T, Nt + 1)
    Y = np.zeros_like(T)
    V = np.zeros_like(T)
    
    # Initial conditions
    Y[0] = y0
    V[0] = v0

    # Leapfrog algorithm
    for i in range(Nt):
        tn = T[i]
        yn = Y[i]
        vn = V[i]

        # Update velocity at the half-step
        vh = vn + 0.5 * h * f(tn, yn)

        # Update position and velocity
        Y[i + 1] = yn + h * vh
        V[i + 1] = vh + 0.5 * h * f(tn + h, Y[i + 1])
    
    plt.plot(T, Y, label='Leapfrog')
    plt.xlabel('Time')
    plt.ylabel('y(t)')
    plt.legend()
    plt.show()

    return T, Y

