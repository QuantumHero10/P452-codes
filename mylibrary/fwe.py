# Forward Euler

import matplotlib.pyplot as plt
import math

def main(x0,y0,xn,h,f):
    X=[]
    Y=[]
    ct=1
    while x0 < xn :
        X.append(x0)
        Y.append(y0)
        y0+= h*f(x0,y0)
        x0+= h
        ct+=1
    print(y0)
    plt.scatter(X,Y)
    #plt.show()

"""
def f(x,y):
    return (math.sin(x)+x**2)

x0=0
y0=-1
xn=1
h=0.01
main(x0,y0,xn,h)
"""
