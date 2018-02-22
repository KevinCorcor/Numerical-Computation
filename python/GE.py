def RREF(M):
    if not M:
        return
    lead = 0
    rowCount = len(M)
    columnCount = len(M[0])
    for r in range(rowCount):      #cycle through the rows
        if lead >= columnCount:     #if the current lead is greater than the number of cols
            return                  #exit
        i = r                       #set i to the value of r
        while M[i][lead] == 0:      #
            i += 1
            if i == rowCount:
                i = r
                lead += 1
                if columnCount == lead:
                    return
        M[i],M[r] = M[r],M[i]
        lv = M[r][lead]
        M[r] = [ mrx / float(lv) for mrx in M[r]]
        for i in range(rowCount):
            if i != r:
                lv = M[i][lead]
                M[i] = [ iv - lv*rv for rv,iv in zip(M[r],M[i])]
        lead += 1
    print(M)


Ab = [[-3,6,-4,-3],[9,-8,24,65],[-12,24,-26,-42]]

# RREF( Ab )

import numpy as np

def linearsolver(A,b): #https://stackoverflow.com/questions/31957096/gaussian-elimination-with-pivoting-in-python
    n= len(A)
    M = A

    i = 0
    for x in M:                                           #augment A to b
        x.append(b[i])
        i += 1
    #partial pivoting
    for k in range(n):                          #consider a specific row
        for i in range(k+1,n):                        #partial pivoting - consider all the rows under this specified row 'k'
            if abs(M[i][k]) > abs(M[k][k]):                #if the abs of the current diagonal element 'kk' is less than any cell below it swap those rows
                M[k], M[i] = M[i],M[k]                            # the swap
            else:                                                 # I think this is actually quite similar to bubble sort
                pass
        #forward elimintation
        for j in range(k+1,n):                                #now consider each cell under that diagonal again
            print(M)
            q = float(M[j][k]) / M[k][k]                      #divide the current row  by the diagonal
            for m in range(k, n+1):                             #now for the current row go through all the non zero entries(columns)
                M[j][m] -=  q * M[k][m]                         #for each cell in that row subtract the ratio q(previously calculated)*the diagonl rows corresponding cell which will ensure a zero under the diagonal :D
    x = [0 for i in range(n)]                                   #set of zeroes

    #Back Substitution
    for i in range(n-1,-1,-1):#starting from the last row work your way back substituting values in
        x[i] = float(M[i][n])/M[i][i]              ##on a row divide a b value by its a value
        for j in range(i-1,-1,-1):                  #Since we now know the value of the last variable let the rest of the matrix know
            M[j][n] -= M[j][i]*x[i]                 #propagate this result back the matrix and

    print(x)
    # x[n-1] =float(M[n-1][n])/M[n-1][n-1]                        #solve for the last row
    #
    # for i in range (n-1,-1,-1):                                 #start,stop, step:
    #     z = 0
    #     for j in range(i+1,n):
    #         z = z  + float(M[i][j])*x[j]
    #         x[i] = float(M[i][n] - z)/M[i][i]
    # #print (x)

A = [[-3,6,-4],[9,-8,24],[-12,24,-26]]
b = [-3, 65, -42]

linearsolver(A,b)
