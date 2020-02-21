import numpy as np
from numpy import linalg as LA
def qrFunction(matA,n):
    QA = np.zeros((n, n, n))
    Q = np.zeros((n, n, n))
    QA[0] = matA
    for n in range(0, dim - 1):
        e = np.zeros((dim - n, dim - n))
        f = np.zeros((dim - n, dim - n))
        for i in range(n, dim):
            for j in range(n, dim):
                e[i - n][j - n] = QA[n][i][j]
        a = LA.norm((e.transpose())[0])
        e1 = np.zeros((1, dim - n))
        e1[0][0] = 1
        u = (e.transpose())[0] - e1 * a
        v = u / LA.norm(u)
        matb = np.dot(np.transpose(v), v)
        I = np.zeros((dim - n, dim - n))
        for i in range(0, dim - n):
            I[i][i] = 1
        f = I - 2 * matb
        for i in range(n, dim):
            for j in range(n, dim):
                Q[n][i][j] = f[i - n][j - n]
        for i in range(0, n):
            for j in range(0, n):
                if (i == j):
                    Q[n][i][j] = 1
        QA[n + 1] = np.dot(Q[n], QA[n])

    r = QA[dim - 1]
    q = np.transpose(Q[0])
    for i in range(1, n + 1):
        q = np.dot(q, np.transpose(Q[i]))
    z = np.array([q,r])
    return z
dim = input()
n = dim
matA = np.zeros((n,n))
for i in range (0,n):
    numbers = map(float, raw_input().split())
    for j in range(0,n):
        matA[i][j]= numbers[j]


u = np.zeros((n,n))
v = np.zeros((n,n))
for i in range(0,n):
    u[i][i] = 1
    v[i][i] = 1
s = np.transpose(matA)
for i in range(0,500):
    z = qrFunction(np.transpose(s),n)
    s = z[1]
    q = z[0]
    u = np.dot(u,q)
    z = qrFunction(np.transpose(s), n)
    s = z[1]
    q = z[0]
    v = np.dot(v, q)
ss = np.zeros((1,n))
for i in range(0,n):
    ss[0][i] = s[i][i]
s = np.zeros((n,n))
for i in range(0,len(ss[0])):
    ssn = ss[0][i]
    s[i][i] = abs(ssn)
    if (ssn<0):
        for j in range(0,n):
            u[j][i] = -1*u[j][i]
for j in range(0, dim):
    for i in u[j]:
        print"{0:.9f}".format(i, end = " "),
    print ("\n")
for j in range(0, dim):
    for i in s[j]:
        print"{0:.9f}".format(i, end = " "),
    print ("\n")
for j in range(0, dim):
    for i in v[j]:
        print"{0:.9f}".format(i, end = " "),
    print ("\n")

