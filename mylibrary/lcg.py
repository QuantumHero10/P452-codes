import matplotlib.pyplot as plt
#function for LCG
def main(a,m,n):
    x=10
    ylist=[]
    for i in range (n):
        x=(a*x)%m
        ylist.append(x/m)
    return ylist
