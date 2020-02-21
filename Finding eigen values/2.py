import numpy as np;
import math;
np.set_printoptions(suppress=True)
m = input();
E = 0.1
matA=np.empty((m,m))
for i in range(0,m):
    for j in range(0,m):
        matA[i][j]=input()
print matA
print "###########################################"
while True:
    flag =0
    maX = matA[0][1]
    maxi = 0
    maxJ = 1
    for i in range(0,m):
        for j in range(0,m):
            if i != j:
                if matA[i][j]>=maX:
                    maX = matA[i][j]
                    maxi = j
                    maxJ = i
    mat1 = np.zeros((m,m))
    for i in range(0,m):
        for j in range(0,m):
            if i == j:
                mat1[i][j]=1
    r = -1.0*matA[maxi][maxJ]
    s = (matA[maxi][maxi]-matA[maxJ][maxJ])/2
    t = math.sqrt(r*r + s*s)
    cosT = math.sqrt((t+math.fabs(s))/(2*t))
    if cosT != 1:
        J = 2*t*cosT
        sinT = math.fabs(r)/J
    else:
        sinT = 0
    mat1[maxi][maxi] = cosT
    mat1[maxJ][maxJ] = cosT
    mat1[maxi][maxJ] = sinT
    mat1[maxJ][maxi] = -1*sinT
    print mat1
    matA = np.dot(mat1.transpose(),matA)
    matA = np.dot(matA,mat1)
    print matA
    for i in range(0,m):
        for j in range(0,m):
            if i != j:
                if -1*E <= matA[i][j] <= E:
                    flag = flag + 1
    flag2 = 0
    for i in range(0,m):
        for j in range(0,m):
            if -1*E <= matA[i][j] <= E:
                flag2 = flag2 + 1
    if flag == (m*m)-m:
        break
    print "---------------------------------------------"
print "###########################################"
print "matrix:"
print matA
