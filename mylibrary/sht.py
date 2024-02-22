# Shooting method

import matplotlib.pyplot as plt
import mylibrary.plotfunc as fplot
import math
def dzdx(z,y,x):
    return (2*y)

def dydx(z,y,x):
    return (z)

def ff(x):
    return (0.157*math.exp(math.sqrt(2)*x)) + (1.043*math.exp(-math.sqrt(2)*x))

def couple(z0,y0,x0,xn,dx):
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
    return y0

def main(x0,y0,xn,dx,a,b,ci):
    ch=ci
    couple(ci,y0,x0,xn,dx)
    y=float(couple(ci,y0,x0,xn,dx)-b)
    while abs(y)>10**-4:
        if (y)<b:
            ch=ch+0.5
        else:
            ch=ch-0.5
        c = ci + ((ch-ci)*(b-float(couple(ci,y0,x0,xn,dx))))/(float(couple(ch,y0,x0,xn,dx))-float(couple(ci,y0,x0,xn,dx)))
        y=float(couple(c,y0,x0,xn,dx)-b)
    #fplot.main(ff,x0,xn)
    couple(ch,y0,x0,xn,dx)
    couple(c,y0,x0,xn,dx)
    #print(c)
    plt.axhline(y = 0.9, color = 'black')
    plt.axhline(y = 0.5614, color = 'black')
    plt.axhline(y = 1.2455, color = 'black')
    plt.axvline(x = 1.0, color = 'black')
    plt.axvline(x = 0.0, color = 'black')
    plt.show()
    return (y+b)