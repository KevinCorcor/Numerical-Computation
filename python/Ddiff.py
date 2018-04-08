import numpy as np
from sympy import Rational


def DDiff(x,fx):
    ''' newtons divided difference'''
    k = 1
    while k < len(fx[0]):
        n = k
        count = 0
        while n < len(fx):
            if(count < len(fx[0])-k):
               # import ipdb; ipdb.set_trace()
                fx[n][k] = Rational((fx[n+1][k-1]-fx[n-1][k-1]) ,(x[n+k][0]-x[n-k][0]))
                n += 2
                count += 1
            else:
                n = len(fx)
        k += 1
    return np.diag(fx)

x_in = np.asarray([[3],[4],[5],[6]],Rational)     #seems to work regardless of input values
x = np.asarray(np.zeros((2*len(x_in)-1,1)),Rational)
x[::2] = x_in[:]

fx_in = np.asarray([[180],[235],[318],[435]],Rational)
fx = np.asarray(np.zeros((2*len(fx_in)-1,len(fx_in))),Rational)
fx[::2,0][:] = fx_in[:].T
