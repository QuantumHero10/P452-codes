import matplotlib.pyplot as plt

def couple(z0,y0,x0,xn,dx,dydx,dzdx):#Coupled RK4 with plot
    X=[]
    Y=[]
    Z=[]
    ct=1
    while x0 < xn :
        Z.append(z0)
        Y.append(y0)
        X.append(x0)
        k1z=dx*dzdx(z0,y0,x0)
        k1y=dx*dydx(z0,y0,x0)
        k2z=dx*dzdx(z0+k1z/2,y0+k1y/2,x0+dx/2)
        k2y=dx*dydx(z0+k1z/2,y0+k1y/2,x0+dx/2)
        k3z=dx*dzdx(z0+k2z/2,y0+k2y/2,x0+dx/2)
        k3y=dx*dydx(z0+k2z/2,y0+k2y/2,x0+dx/2)
        k4z=dx*dzdx(z0+k3z,y0+k3y,x0+dx)
        k4y=dx*dydx(z0+k3z,y0+k3y,x0+dx)
        z0+= (k1z + 2*k2z + 2*k3z + k4z)/6
        y0+= (k1y + 2*k2y + 2*k3y + k4y)/6
        x0+=dx
        ct+=1
    plt.plot(X,Y,'.',markersize=2.0)
    plt.xlabel("x (m)")
    plt.ylabel("T (K)")
    return y0

def main(z0,y0,yn,x0,xn,dx,dydx,dzdx):#Coupled RK4 without plot for later use in code
    X=[]
    Y=[]
    Z=[]
    ct=1
    while x0 < xn :
        Z.append(z0)
        Y.append(y0)
        X.append(x0)
        k1z=dx*dzdx(z0,y0,x0)
        k1y=dx*dydx(z0,y0,x0)
        k2z=dx*dzdx(z0+k1z/2,y0+k1y/2,x0+dx/2)
        k2y=dx*dydx(z0+k1z/2,y0+k1y/2,x0+dx/2)
        k3z=dx*dzdx(z0+k2z/2,y0+k2y/2,x0+dx/2)
        k3y=dx*dydx(z0+k2z/2,y0+k2y/2,x0+dx/2)
        k4z=dx*dzdx(z0+k3z,y0+k3y,x0+dx)
        k4y=dx*dydx(z0+k3z,y0+k3y,x0+dx)
        z0+= (k1z + 2*k2z + 2*k3z + k4z)/6
        y0+= (k1y + 2*k2y + 2*k3y + k4y)/6
        x0+=dx
        ct+=1
        if abs(y0-yn)<=10**-3:
            return x0-dx
