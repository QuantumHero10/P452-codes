# Velocity verlet method

def main(x0,v0,a,tn,dt):
    xn = float(x0)
    vn = float(v0)
    V = []
    V.append(xn)
    for i in range (0,tn/dt):
        vthdt = xn + (vn*dt) + (a(xn)*dt/2)
        xnp1 = xn + (vthdt*dt)
        vnp1 = vn + ((a(xn)+a(xnp1))/2)
        vn = float(vnp1)
        xn = float(xnp1)
        V.append(vn)
    return V