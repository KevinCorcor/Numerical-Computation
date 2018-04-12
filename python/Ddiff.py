import numpy as np
from sympy import *


def DDiff(xs,fxs):
    ''' newtons divided difference'''
    k = 1
    while k < len(fxs[0]):
        n = k
        count = 0 # for counting how many calculations have been made on that trial
        while n < len(fxs):
            if(count < len(fxs[0])-k): #optimisation
               # import ipdb; ipdb.set_trace()
                fxs[n][k] = Rational((fxs[n+1][k-1]-fxs[n-1][k-1]) ,(xs[n+k][0]-xs[n-k][0]))
                n += 2
                count += 1
            else:
                break #no need to make any more calculations for this trial
        k += 1
    return (fxs , np.diag(fxs)) # return the upper diagonal


x_in = np.asarray([[1],[2],[4]],Rational)     #seems to work regardless of input values
xs = np.asarray(np.zeros((2*len(x_in)-1,1)),Rational)
xs[::2] = x_in[:]                                    #add spacing

fx_in = np.asarray([[0],[1],[2]],Rational)
fxs = np.asarray(np.zeros((2*len(fx_in)-1,len(fx_in))),Rational)
fxs[::2,0][:] = fx_in[:].T                              #add spacing

#CALCULATE POLYNOMIAL AND SIMPLIFY
def poly(xs,diag):
    xs = xs[~np.all(xs == 0, axis=1)] # remove zero rows

    x = Symbol('x')
    f = diag[0]

    for d in range(1,len(diag)):
        c=d-1
        r=1
        while c>=0:
            r = r*(x-xs[c])                    #any linear function
            c = c-1
        #print(r)
        f = f + diag[d]*r
    f=simplify(f)
    return f
