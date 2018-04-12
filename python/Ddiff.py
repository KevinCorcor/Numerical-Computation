import numpy as np
from sympy import Rational


def DDiff(x,fx):
    ''' newtons divided difference'''
    k = 1
    while k < len(fx[0]):
        n = k
        count = 0 # for counting how many calculations have been made on that trial
        while n < len(fx):
            if(count < len(fx[0])-k): #optimisation
               # import ipdb; ipdb.set_trace()
                fx[n][k] = Rational((fx[n+1][k-1]-fx[n-1][k-1]) ,(x[n+k][0]-x[n-k][0]))
                n += 2
                count += 1
            else:
                break #no need to make any more calculations for this trial
        k += 1
    return (fx , np.diag(fx)) # return the upper diagonal


x_in = np.asarray([[1],[2],[4]],Rational)     #seems to work regardless of input values
x = np.asarray(np.zeros((2*len(x_in)-1,1)),Rational)
x[::2] = x_in[:]                                    #add spacing

fx_in = np.asarray([[0],[1],[2]],Rational)
fx = np.asarray(np.zeros((2*len(fx_in)-1,len(fx_in))),Rational)
fx[::2,0][:] = fx_in[:].T                              #add spacing

#CALCULATE POLYNOMIAL AND SIMPLIFY
def poly(diag):
    x = Symbol('x')
    f = diag[0]

    for d in range(len(diag)-1,0,-1):
        c=d
        r=1
        while c>0:
            r = r*(x-c)                    #any linear function

            c = c-1
        print(r)
        f = f + diag[d]*r
    f=simplify(f)
    return f
