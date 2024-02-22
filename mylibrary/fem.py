# Finite element method

import numpy as np
import matplotlib.pyplot as plt

def finite_element_method(N, T, L, alpha):
    # Parameters
    dt = T / N
    dx = L / N
    
    # Initialize mesh
    x = np.linspace(0, L, N+1)
    
    # Initialize solution array
    u = np.zeros(N+1)
    
    # Initial condition
    u[0] = 100.0
    
    # Time-stepping loop
    for n in range(0, N):
        # Finite element method update
        for i in range(1, N):
            u[i] = u[i] + alpha * dt / dx**2 * (u[i+1] - 2*u[i] + u[i-1])
        
        # Boundary condition
        u[N] = 0.0
    
    return x, u

def main(N, T, L, alpha):
    x, u = finite_element_method(N, T, L, alpha)
    # Plot the result
    plt.plot(x, u, label='Temperature')
    plt.title('Finite Element Method for Heat Conduction')
    plt.xlabel('Position')
    plt.ylabel('Temperature')
    plt.legend()
    plt.show()
    return u
