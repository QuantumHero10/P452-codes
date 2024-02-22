import numpy as np
# Matrix multiplication library file
def main(M,N):
    dimension1 = np.shape(M)
    m1,m2=dimension1
    dimension2 = np.shape(N)
    n1,n2=dimension2
    P=[]
    #if statement to check if 2 matrices can be multiplied or not
    if m2 != n1:
        print('The two input matrices cannot be multiplied.\n')
        return
    for i in range (0,m1):
        row=[]
        for j in range (0,n2):
            c=0.0
            s=0.0
            for k in range (0,m2):
                c=M[i,k]*N[k,j]
                s=s+c
            row.append(s)
        P.append(row)
    Q=np.matrix(P)
    return Q
