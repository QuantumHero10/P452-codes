# Poisson's equation solver

import numpy as np
import matplotlib.pyplot as plt
def main(Lx,Ly,nx,ny,u):
    dx, dy = Lx / (nx + 1), Ly / (ny + 1)

    # Create grid
    x = np.linspace(0, Lx, nx)
    y = np.linspace(0, Ly, ny)
    u1 = u.copy()

    # Solve Poisson's equation
    for it in range(1000):  # Number of iterations
        for i in range(1, nx-1):
            for j in range(1, ny-1):
                u1[i, j] = (u[i + 1, j] + u[i - 1, j] + u[i, j + 1] + u[i, j - 1] - dx*dy * x[i] * np.exp(y[j])) / 4
        u=u1.copy()
    
    # Display the solution in a table
    print("Solution Table:")
    print(u1)

    # Display the solution in a 3D plot
    X, Y = np.meshgrid(x, y)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, u.T, cmap='inferno')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('u(x, y)')
    ax.set_title('Solution of Poisson\'s Equation')
    plt.show()