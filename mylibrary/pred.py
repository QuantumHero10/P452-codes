# Predictor corrector method

import math

def main(x0,y0,xn,h,f):
    y1=0
    y2=0
    while x0 < xn :
        x1=float(x0)
        y1=float(y0)
        y2 = y0 + h*f(x0,y0)
        x0 = x0 + h
        y0 = y1 + h*((f(x0,y2)+f(x1,y1))/2)
    print(y0)

"""
def f(x,y):
    return (math.sin(x)+x**2)

x0=0
y0=-1
xn=1
h=0.01
main(x0,y0,xn,h)
"""