from sympy import *
import numpy as np
import scipy as sc
from itertools import product
###############################################################################
#                   FOR LINEAR EQUATIONS ONLY
###############################################################################
x = Symbol('x') #x is our variable

#####################################################
f =  (0*x**4)+ (1*x**3) + (0*x**2) + (0*x) + (0)                     #any linear function
#####################################################
#df/dx = f'(x)
fd = f.diff(x,Real=true)        #using sympy to differentiate

#d^2 f/ dx^2 = f''(x)
fdd = fd.diff(x,Real=true)   #using sympy to differentiate again

roots_X = solveset(f,x)      #find the roots of the function f

criticalPts_X = np.asarray(list(solveset(fd,x)))    #the roots of f'(x) give us the x coords of our max, min or point of inflection
criticalPts_X = np.append(criticalPts_X,list(solveset(fdd,x)))

#lists for storing the XY coords of max, min, poi and the concavity of critical points
maxima_XY = []
minima_XY = []
poi_XY = []
concavity = []

for cp in range(0,len(criticalPts_X)):      #cycle through the critical points
    #criticalPts_X = np.append(solveset(fdd,x))       #append poi s
    corres_Y = f.subs(x,criticalPts_X[cp])      #f(criticalPt) = y
    concavity.append(fdd.subs(x,criticalPts_X[cp])) #f''(criticalPt), the sign of this tells us if it is positive or negative

    if concavity[cp] < 0:
        maxima_XY.append(tuple((criticalPts_X[cp], corres_Y)))
    elif concavity[cp] > 0:
        minima_XY.append(tuple((criticalPts_X[cp], corres_Y)))
    else:#must be equal to 0
         poi_XY.append(tuple((criticalPts_X[cp], f.subs(x,criticalPts_X[cp]))))

print("maximum: \n", maxima_XY,\
      "\nminimum: \n", minima_XY,\
      "\nPoint of Inflection: \n", poi_XY)
