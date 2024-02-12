def main(f,x0,y0,xn,h):
    X=[]
    Y=[]
    ct=1
    while x0 < xn :
        X.append(x0)
        Y.append(y0)
        k1 = h*f(x0,y0)
        k2 = h*f(x0+h/2,y0+k1/2)
        k3 = h*f(x0+h/2,y0+k2/2)
        k4 = h*f(x0+h,y0+k3)
        y0+= (k1 + 2*k2 + 2*k3 + k4)/6
        x0+= h
        ct+=1
    return y0
