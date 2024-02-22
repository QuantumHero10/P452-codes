# Verlet method

def main(x0,v0,a,tn,dt):
    x1 = x0 + (v0*dt) + (a(x0)*dt*dt/2)
    xnm1 = float(x0)
    xn = float(x1)
    X = []
    X.append(xn)
    for i in range (1,tn/dt):
        xnp1 = (2*xn) - xnm1 + (a(xn)*dt*dt)
        xnm1 = float(xn)
        xn = float(xnp1)
        X.append(xn)
    return X