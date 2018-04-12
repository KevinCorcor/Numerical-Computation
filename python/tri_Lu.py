import numpy as np
from numpy import linalg as la

#                [[d,e,.........],\
#                 [c,d,e,.......],\
#                 [0,c,d,e,.....],\
#                 [0,0,c,d,e,....]]

M = np.asmatrix([[3,5,0,0],\
                [1,4,6,0],\
                [0,5,7,3],\
                [0,0,3,8]],np.float64)
b = np.asmatrix([[13],\
                [27],\
                [43],\
                [41]],np.float64)
def tri_lu(M):
    #diagonals
    C = np.asmatrix(np.append(0,np.diag(M,-1))).T
    D = np.asmatrix(np.diag(M)).T
    E = np.asmatrix(np.append(np.diag(M,1),0)).T

    #the algo
    c = np.asmatrix(np.zeros(C.shape))
    d = np.asmatrix(np.zeros(D.shape))
    e = np.asmatrix(np.copy(E))

    d[0] = D[0]
    for i in range(1,len(D)):
        c[i] = C[i]/d[i-1]
        d[i] = (D[i] - (c[i] * E[i-1]))

    #create L
    L = np.asmatrix(np.identity(len(M)))
    for i in range(1,len(M)):
        L[i,i-1] = c[i]

    #create U
    U = np.asmatrix(np.triu(M))
    for i in range(0, len(M)):
        U[i,i] = d[i,0]

    return (L,U,c,d,e)

def tri_solve(L,U,c,d,e,b):
    #SOLVE Ly = b
    y = np.asmatrix(np.zeros(d.shape))
    y[0,0] = b[0,0]
    for k in range(1,len(L)):
        y[k,0] = b[k,0] - c[k] * y[k-1,0]

    #Solve Ux = y
    x = np.asmatrix(np.zeros(d.shape))
    x[len(L)-1] = y[len(L)-1]/d[len(L)-1]
    for n in range(len(L)-2, -1,-1):
        x[n,0] = (y[n,0] - e[n,0]*x[n+1,0])/d[n,0]

    return x
