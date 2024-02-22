import matplotlib.pyplot as plt

def main(f1,f2,x0,y0,t,tn,dt):
    X=[]
    Y=[]
    T=[]
    ct=1
    while t < tn :
        X.append(x0)
        Y.append(y0)
        T.append(t)
        k1x=dt*f1(x0,y0,t)
        k1y=dt*f2(x0,y0,t)
        k2x=dt*f1(x0+k1x/2,y0+k1y/2,t+dt/2)
        k2y=dt*f2(x0+k1x/2,y0+k1y/2,t+dt/2)
        k3x=dt*f1(x0+k2x/2,y0+k2y/2,t+dt/2)
        k3y=dt*f2(x0+k2x/2,y0+k2y/2,t+dt/2)
        k4x=dt*f1(x0+k3x,y0+k3y,t+dt)
        k4y=dt*f2(x0+k3x,y0+k3y,t+dt)
        x0+= (k1x + 2*k2x + 2*k3x + k4x)/6
        y0+= (k1y + 2*k2y + 2*k3y + k4y)/6
        t+=dt
        ct+=1
    plt.plot(X,Y)
    plt.ylabel("Y")
    plt.xlabel("X")
    plt.show()
    return x0

