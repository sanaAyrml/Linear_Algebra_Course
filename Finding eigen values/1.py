import numpy as np;
import math;
n = 3
matA = np.array([[-100,3,5],[7,6,5],[7,8,9]])
# for i in range(0,n):
#         for j in range(0,n):
#             matA[i][j]=input()
error = 0.00001
x0 = np.ones(n)
x1 = np.empty(n)
y = np.empty(n)
while True:
    y = np.dot(matA,x0)
    norm = max(y.min(), y.max(), key=abs)
    x1 = y/norm
    e = 0
    for i in range(0, n):
        e = e + (x1[i]-x0[i])*(x1[i]-x0[i])
    e = math.sqrt(e/n)
    print norm
    print x1
    print "------------------------------------------------------"
    x0 = x1
    if e < error:
        break;
l1 = norm
print "eigenvalue 1:"
print l1
print "eigenvector 1:"
print x1
print "#####################################################"
print np.dot(matA,x1)
print l1*x1
print "#####################################################"
lndM = np.zeros((n,n))
for i in range(0,n):
    lndM[i][i] = norm
matB = matA - lndM
x0 = np.ones(n)
x1 = np.empty(n)
y = np.empty(n)
while True:
    y = np.dot(matB,x0)
    norm = max(y.min(), y.max(), key=abs)
    x1 = y/norm
    e = 0
    for i in range(0, n):
        e = e + (x1[i]-x0[i])*(x1[i]-x0[i])
    e = math.sqrt(e/n)
    print norm
    print x1
    print "------------------------------------------------------"
    x0 = x1
    if e < error:
        break;
l2 = l1 + norm
print "eigenvalue 2:"
print l2
print "eigenvector 2:"
print x1
print "#####################################################"
print np.dot(matA,x1)
print l2*x1
print "#####################################################"



