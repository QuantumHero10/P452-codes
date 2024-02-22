# Gauss-Jordon matrix inverter

import numpy as np
import csv
def swap(M,N,n):
  x=n
  y=M[n,n]
  m=len(M)
  for i in range (m):
    for j in range (n,(n+1)):
      k=M[i,j]
      if k**2 >= y**2:
        y=k
        x=i
  if x<n:
    return
  s=np.matrix(M[x])
  M[x]=M[n]
  M[n]=s
  r=np.matrix(N[x])
  N[x]=N[n]
  N[n]=r

def gauss_jordan_inverter(M,N): #main code 
  L=M
  n=len(L)
  M=np.matrix(L)
  n=len(M)-1
  c=0.0
  c1=0.0
  for i in range (0,n+1):
    if M[i,i]==0:
      swap(M,N,i)
    c1=float(M[i,i])
    M[i]=M[i]/c1
    N[i]=N[i]/c1
    for j in range (i+1,n+1):
      c=float((M[j,i])/(M[i,i]))
      M[j]=M[j]-(c*M[i])
      N[j]=N[j]-(c*N[i])

  for i in range (0,n):
    k=n-i
    for j in range (0,k):
      l=k-j-1
      c=float((M[l,k])/(M[k,k]))
      M[l]=M[l]-(c*M[k])
      N[l]=N[l]-(c*N[k])
  return N

def input(path):
  i=0
  j=0
  M=[]
  with open(path) as x:
    cr=csv.reader(x)
    next(cr)
    for line in cr:
      row=[]
      for n in line:
        row.append(float(n))
      M.append(row)
  return (np.matrix(M))

def identity(n):
  s=0.0
  P=[]
  for i in range (0,n):
    row=[]
    for j in range (0,n):
      if i==j:
        s=float(1)
      else:
        s=float(0)
      row.append(s)
    P.append(row)
  return P

def main(A):
  #A=input(p)
  A=np.matrix(A)
  C=np.matrix(A)
  m=len(A)
  I = np.matrix(identity(m))
  B=gauss_jordan_inverter(A,I)
  return B
