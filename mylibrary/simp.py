def main(f,a,b,n):
    h=(b-a)/n
    ct=1
    sum=f(a)+f(b)
    x=a+h
    while x<b :
        if ct % 2 == 0:
            w=2
        else:
            w=4
        sum+=w*f(x)
        x+=h
        ct+=1
    return sum*h/3
