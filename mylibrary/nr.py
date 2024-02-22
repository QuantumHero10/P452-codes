# Newton-Raphson method

def main(f,d,x):
    ct=0
    print("NEWTON-RAPHSON")
    print("--------------")
    print("Initial guess for newton raphson=",x)
    print("Iterations:")
    while abs(f(x))>10**-6:
        ct+=1
        x= x - f(x)/d(x)
        print(x)
    print("No. of Iterations:",ct)
    print("The required root is:",x)
    return

