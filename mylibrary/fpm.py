def main(g,x):
    x1=g(x)
    eps=10**-4
    c=1
    while abs(x1-x)>eps:
        x=float(x1)
        x1=g(x1)
        c+=1
    print("No. of iterations = ",c)
    return x1