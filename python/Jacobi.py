import numpy as np

A = np.asmatrix([[10,-1,2,0],[-1,11,-1,3],[2,-1,10,-1],[0,3,-1,8]])
B = np.asmatrix([[6],[25],[-11],[15]])

def Jacobi3x3(A,B):
    x = np.asmatrix(np.zeros(len(A),1))
    xk = np.asmatrix(np.zeros((len(x),1)))
    RE = 1

    #precision specified in loop - not very specific
    while RE >= 0.0009:
        xk[0] = (B[0] - (A[0,1] * x[1]) - (A[0,2] * x[2])) / A[0,0]
        xk[1] = (B[1] - (A[1,0] * x[0]) - (A[1,2] * x[2])) / A[1,1]
        xk[2] = (B[2] - (A[2,0] * x[0]) - (A[2,1] * x[1])) / A[2,2]
        RE = (np.linalg.norm(xk - x,np.inf)) / (np.linalg.norm(xk,np.inf) + 0)
        x = xk.copy()

        print(x[0],"\t",x[1],"\t",x[2],"\t",RE)

def Jacobi(A,B):
    x = np.asmatrix(np.zeros((len(A),1)))
    xk = np.asmatrix(np.zeros((len(x),1)))
    RE = 1
    trial_no = 1
    print("trial          x1          x2          x3          ...")

    while RE > 0.0009:
        for i  in range(0, len(x)):
            xk[i] = (B[i] + EQN(A[i], x,i)) / A[i,i]

        RE = (np.linalg.norm(xk - x,np.inf)) / (np.linalg.norm(xk,np.inf) + 0)
        x = xk.copy()

        print(str(trial_no)+"\t"+str(x.T)+"\t"+str(RE))
        trial_no +=1
    print("trial          x1          x2          x3          ...")

    return x



def eqn(w,x,I):

    w = -1 * w
    res = np.multiply(w.T,x)
    res[I] = 0
    sum = np.sum(res)
    return sum
