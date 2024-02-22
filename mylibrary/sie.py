# Semi implicit euler

def main(x0,v0,t0,tn,dt,f,g):
    xn = float(x0)
    vn = float(v0)
    X = []
    V = []
    X.append(xn)
    V.append(vn)
    for i in range (0,tn/dt):
        vnp1 = vn + (g((t0+(dt*i)),xn)*dt)
        xnp1 = xn + (f((t0+(dt*i)),vnp1)*dt)
        vn = float(vnp1)
        xn = float(xnp1)
        X.append(xn)
        V.append(vn)
    return X,V