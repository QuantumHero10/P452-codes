# Backward Euler

import matplotlib.pyplot as plt
import math
import nr as nr

def main(x0,y0,xn,h,f):
    X=[]
    Y=[]
    ct=1   
    y1=float(y0)
    while x0 < xn :
        X.append(x0)
        Y.append(y0)
        y1=f(x0+h,y1)
        y0= f(x0+h,y0)
        x0+= h
    print(y0)
    plt.scatter(X,Y)
    #plt.show()


"""
def f(x,y):
    return y+(h*(math.sin(x)+x**2))

x0=0
y0=-1
xn=1
h=0.01
main(x0,y0,xn,h)
"""