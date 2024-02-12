import numpy as np
import mylibrary.mm as mm
import matplotlib.pyplot as plt

def main(L,T,Nx,Nt,g,C):
    # Grid spacings
    dx = L / Nx
    dt = T / Nt

    # Crank-Nicolson parameter
    alpha = dt / (dx**2)

    x_values = np.linspace(0, L, Nx+1)
    t_values = np.linspace(0, T, Nt+1)

    # Initialize solution matrix
    u=[]
    for i in range(Nx + 1):
        row=[]
        for j in range(Nt + 1):
            row.append(0.0)
        u.append(row)

    u=np.matrix(u)
    #Initial condition
    for i in range (Nx+1):
        u[i,0]=g(x_values[i])
    D=[]
    for i in range(Nx + 1):
        row=[]
        for j in range(1):
            row.append(0.0)
        D.append(row)
    D=np.matrix(D)
    for j in range (Nt):
        for i in range (Nx+1):
            D[i]=u[i,j]
        E=mm.main(C,D)
        for i in range (Nx+1):
            u[i,j+1]=E[i]
    print("Solution Table:")
    print(u)

    # contour plot
    X, T = np.meshgrid(x_values, t_values)
    plt.contourf(X, T, u.T, cmap='coolwarm')
    plt.colorbar()
    plt.xlabel('x')
    plt.ylabel('t')
    plt.title('Solution of the Heat Equation (Crank-Nicolson)')
    plt.show()