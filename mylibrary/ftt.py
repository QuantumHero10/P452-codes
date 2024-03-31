import numpy as np

def mean(A):
    A=np.array(A)
    n=len(A)
    sum=0.0
    for i in range(n):
        sum+=A[i]/n
    return sum

def variance(A):
    A=np.array(A)
    n=len(A)
    variance=0.0
    mean_A=mean(A)
    for i in range(n):
        variance+=((A[i]-mean_A)**2)/(n-1)
    return variance

def F_value(A,B):
    return variance(A)/variance(B)

def t_value(A,B):
    return (mean(A)-mean(B))/np.sqrt((variance(A)/len(A))+(variance(B)/len(B)))


def main(A,B):
    A=np.array(A)
    B=np.array(B)
    return F_value(A,B),t_value(A,B)

