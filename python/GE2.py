import numpy as np
a= [[-3,6,-4],[9,-8,24],[-12,24,-26]]
n = len(a)
for k in range(0,n-1):
    for i in range(k+1,n):
        a[i][k] = a[i][k]/a[k][k]
        for j in range(k+1,n):
            a[i][j]  -= np.dot(a[i][k],a[k][j])
            print(a)
