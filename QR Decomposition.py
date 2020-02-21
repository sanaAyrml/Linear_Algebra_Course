import numpy as np;
from numpy import linalg as LA;
dim = input()
n = dim
matA = np.zeros((n,n))
QA = np.zeros((n,n,n))
Q = np.zeros((n,n,n))
for i in range (0,n):
    numbers = map(float, raw_input().split())
    for j in range(0,n):
        matA[i][j]= numbers[j]
QA[0]= matA
for n in range(0,dim-1):
    e = np.zeros((dim-n,dim-n))
    f = np.zeros((dim-n, dim-n))
    for i in range(n, dim):
        for j in range(n,dim):
            e[i-n][j-n] = QA[n][i][j]
    a = LA.norm((e.transpose())[0])
    e1 = np.zeros((1,dim-n))
    e1[0][0] = 1
    u = (e.transpose())[0] - e1*a
    v = u/ LA.norm(u)
    # print np.transpose(v)
    matb = np.dot(np.transpose(v),v)
    I = np.zeros((dim-n,dim-n))
    for i in range (0,dim-n):
        I[i][i] = 1
    f = I - 2*matb
    for i in range(n, dim):
        for j in range(n,dim):
            Q[n][i][j] = f[i-n][j-n]
    for i in range(0, n):
        for j in range(0,n):
            if(i == j):
               Q[n][i][j] = 1
    # print Q[n]
    QA[n+1] = np.dot(Q[n],QA[n])
    # print QA[n+1]

r = QA[dim-1]
q = np.transpose(Q[0])
for i in range(1,n+1):
    q = np.dot(q,np.transpose(Q[i]))
# print np.dot(q,r)
for j in range(0, dim):
    for i in q[j]:
        print"{0:.9f}".format(i, end = " "),
    print ("\n")
for j in range(0, dim):
    for i in r[j]:
        print"{0:.9f}".format(i, end = " "),
    print ("\n")

