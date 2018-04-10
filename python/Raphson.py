import numpy as np
from numpy import linalg as lanp
from sympy import * #probably don't need to import everything

x = np.asarray([Symbol('x0'),Symbol('x1'),Symbol('x2'),Symbol('x3'),Symbol('x4'),Symbol('x5'),Symbol('x6'),Symbol('x6'),Symbol('x6')]) #for 7 variables, not very convenient but hopefuly it will do

#FUNCTIONS FROM TOM'S NOTES - gives the same result
f = np.asarray([\
                    1.4*x[0] -x[1] - 0.6,  \
                    x[0]**2 - 1.6*x[0] - x[1] - 4.6         \
                ])

#CALCULATE THE JACOBIAN - the partial deivative of each funtion wrt(with respect to) each variable
#Note: the length(depth) of f should correspond to the number of variables, otherwords we have too much or too little equations and none of this will work anyway
#Note: len(f[0].atoms(Symbol)) will return the number of variables in 0th function
J = np.zeros((len(f),len(f)),object)                        #empty square array defined by the number of variable(again this should be the same as the number of functions)
for func in range(0,len(f)):                                 #cycle through all functions - func being an index for each function
 for var in range(0,len(f)):                                  #cycle through all the variables - var being an index for each variable
     J[func,var] = f[func].diff(x[var])                          #calcuate the partial dervitive of the curren function wrt(with respect to) the current variable

guess = np.asarray([5.0,5.0])              #initial guess - tedious to convert to matrix, easier to convert to matrix just when needed
iterations = 10

#begin the Newton Raphson algorithm for specified iterations
for n in range(0,iterations):                                 #for each iteration
    print("guess no. ",n,"\t",guess)                            #print our current Jguess

    #EVALUATE F(GUESS)
    fguess = np.asmatrix(np.zeros((f.shape)))                                #create an array to store the evaluation
    # the next line will only work properly if they are the same shape
    for func in range(0,len(f)):                                #as before - for each function
         ##here i am pairing variables with guess values, stooring them in an array and subbing that into the function
        fguess[0,func] = f[func].subs(set(zip(x[:],guess)))           #initialise the corresponding element in fguess.


    #EVALUATE J(GUESS)
    Jguess = np.asmatrix(np.zeros((J.shape)))
    for j in range(0,len(J)):
        for var in range(0,len(f)):
            Jguess[j,var] = J[j][var].subs(set(zip(x[:],guess)))

    #CALCULATE THE DELTAGUESS
    deltaG = lanp.inv(Jguess)*-fguess.T   #deltaguess = inverse(JacobianGuess) * -FunctionGuess. I had to convert to arrays here and transpose
    # print("Delta(",n,"): \n", deltaG)
    # print("J(",n,"):\n",Jguess)
    # print("f(",n,"):","\n",fguess)

    #ADD DELTAGUESS TO GUESS TO CREATE A NEW GUESS
    guess = np.asarray((np.asmatrix(guess).T+np.asmatrix(deltaG)).T)[0]     #update guess
