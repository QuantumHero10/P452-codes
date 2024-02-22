import mylibrary.rk4c as rk4c
import matplotlib.pyplot as plt

def main(x0,y0,xn,dx,a,b,ci,dydx,dzdx,T):
    ch=ci
    print("Initial guess slope = ",ci)
    rk4c.couple(ci,y0,x0,xn,dx,dydx,dzdx)
    y=float(rk4c.couple(ci,y0,x0,xn,dx,dydx,dzdx)-b)
    while abs(y)>10**-4:
        if (y)<b:
            ch=ch+5.0
        else:
            ch=ch-5.0
        c = ci + ((ch-ci)*(b-float(rk4c.couple(ci,y0,x0,xn,dx,dydx,dzdx))))/(float(rk4c.couple(ch,y0,x0,xn,dx,dydx,dzdx))-float(rk4c.couple(ci,y0,x0,xn,dx,dydx,dzdx)))
        y=float(rk4c.couple(c,y0,x0,xn,dx,dydx,dzdx)-b)
    rk4c.couple(ch,y0,x0,xn,dx,dydx,dzdx)
    rk4c.couple(c,y0,x0,xn,dx,dydx,dzdx)
    print("Final value of slope = ",c)
    yn=T
    #(rk4c.main(c,a,yn,x0,xn,dx*0.001,dydx,dzdx))
    plt.title("x vs T for different guess values")
    plt.axhline(y = a, color = 'black')
    plt.axhline(y = b, color = 'black')
    plt.axhline(y = T, color = 'black')
    plt.show()
    return (rk4c.main(c,a,yn,x0,xn,dx*0.001,dydx,dzdx))