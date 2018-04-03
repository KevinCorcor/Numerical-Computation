import numpy as np

def GE_PP(A,b):
    n = len(A)
    A, b = np.asarray(A,dtype=np.float64),np.asarray(b,dtype=np.float64)
    Ab = np.asarray(np.c_[A, b],dtype=np.float64)
    #print(Ab)

    for k in range(n):                          #for each column of A in Ab
        #Partial Pivoting
        for i in range(k+1,n):                      #for each values in that column below the diagonal
            if abs(Ab[i][k]) > abs(Ab[k][k]):           #if one |value| is greater than another
                Ab[[k,i]]=Ab[[i,k]]                         #swap the rows containing those values
                print("this is a pivot \n",Ab)                                   #view the swap
            else:                                       #otherwise
                pass                                        #do nothing

        #Forward Elimination - Subtracting rows
        for j in range(k+1,n):                      #for each row under the diagonal of the kth column
            q = float(Ab[j][k]) / Ab[k][k]              #calculate the ratio to the value in the main diagonal
            for m in range(k, n+1):                     #for each each column in a Row j
                Ab[j][m] -=  q * Ab[k][m]                   #calculate Rj - q*Rk.  This will result in all zeros under the main diagonal

    # x = [0.0 for i in range(n)]                 #set of zeros
    x = np.zeros(n)


    #At this stage the matrix should be in row echelon form
        # this means all zeros below the main diagonal

    #Backwards Substitution - Solve for one variable and substite that back in to solve for another
    x[n-1] =float(Ab[n-1][n])/Ab[n-1][n-1]      #simply solve the last row, since there should be only one unknown
    for i in range (n-1,-1,-1):                 #start,stop, step - starting from the second last row work back up the rows
        z = 0.0                                     #let z=0 or reset to 0
        for j in range(i+1,n):                      #for each column in a Row j
            z = z  + float(Ab[i][j])*x[j]               #substitute answers from below(stored in x) into the equation of the current row
        x[i] = float(Ab[i][n] - z) / Ab[i][i]       #solve for this row, where there should now be only one unknown
    print(x)                                    #print off your solution vector



A = [[4,  1,  2,  -3,  5], [-3,  3, -1,   4, -2], [-1,  2,  5,   1,  3], [ 5,  4,  3,  -1,  2], [ 1, -2,  3,  -4,  5]]
b = [[-16], [20], [-4],[-10],[3]]

GE_PP(A,b)
