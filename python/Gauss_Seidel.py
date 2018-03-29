import numpy as np

A = np.asmatrix([[3,-1,1],[-1,3,-1],[1,-1,3]])
B = np.asmatrix([[0],[0],[100]])

def GS3x3(A,B):
    x = np.asmatrix(np.zeros(len(A),1))
    #xk = np.asmatrix(np.zeros((len(x),1)))
    RE = 1

    #precision specified in loop - not very specific
    while RE >= 0.009:
        xk = x.copy()
        x[0] = (B[0] - (A[0,1] * x[1]) - (A[0,2] * x[2])) / A[0,0]
        x[1] = (B[1] - (A[1,0] * x[0]) - (A[1,2] * x[2])) / A[1,1]
        x[2] = (B[2] - (A[2,0] * x[0]) - (A[2,1] * x[1])) / A[2,2]
        RE = (np.linalg.norm(x - xk,np.inf)) / (np.linalg.norm(x,np.inf) + 0)
        #x = xk.copy()

        print(x[0],"\t",x[1],"\t",x[2],"\t",RE)

def GS(A,B):
    x = np.asmatrix(np.zeros((len(A),1)))
    #xk = np.asmatrix(np.zeros((len(x),1)))
    RE = 1
    trial_no = 1
    print("trial          x1          x2          x3          ...")

    while RE > 0.0009:
        xk = x.copy()
        for i  in range(0, len(x)):
            x[i] = (B[i] + eqn(A[i], x,i)) / A[i,i]

        RE = (np.linalg.norm(x - xk,np.inf)) / (np.linalg.norm(x,np.inf) + 0)
        #x = xk.copy()

        print(str(trial_no)+"\t"+str(x.T)+"\t"+str(RE))
        trial_no +=1
    print("trial          x1          x2          x3          ...")

    return x

def GSrec(A,B):
    x = np.asmatrix(np.zeros((len(A),10)))
    #xk = np.asmatrix(np.zeros((len(x),1)))
    RE = 1
    trial_no = 1
    print("trial          x1          x2          x3          ...")
    t=0
    while t < 10:
        if t>0: x[:,t] = x[:,t-1].copy()
        for i  in range(0, len(x)):
            x[i,t] = (B[i] + eqn(A[i], x[:,t],i)) / A[i,i]

        RE = (np.linalg.norm(x[:,t] - x[:,t-1],np.inf)) / (np.linalg.norm(x[:,t],np.inf) + 0)
        #x = xk.copy()

        print(str(trial_no)+"\t"+str(x[:,t].T)+"\t"+str(RE))
        t += 1
        trial_no +=1
    print("trial          x1          x2          x3          ...")

    return x.T

def GSrel(A,B):
    x = np.asmatrix(np.zeros((len(A),11)))
    #xk = np.asmatrix(np.zeros((len(x),1)))
    RE = 1
    trial_no = 1
    print("trial          x1          x2          x3          ...")
    t=0
    w=1
    while t < 11:
        if t>0: x[:,t] = x[:,t-1].copy()
        for i  in range(0, len(x)):
            x[i,t] = (B[i] + eqn(A[i], x[:,t],i)) / A[i,i]
            if(t>0): x[i,t] = w*x[i,t] + (1-w)*x[i,t-1]

        RE = (np.linalg.norm(x[:,t] - x[:,t-1],np.inf)) / (np.linalg.norm(x[:,t],np.inf) + 0)
        #x = xk.copy()

        print(str(trial_no)+"\t"+str(x[:,t].T)+"\t"+str(RE))
        t += 1
        trial_no +=1
    print("trial          x1          x2          x3          ...")

    return x.T

def GSrelimp(A,B):
    iterations = 17
    x = np.asmatrix(np.zeros((len(A),iterations),np.float64),np.float64)
    print("trial          x1          x2          x3          ...")
    k=10
    t=0
    w=1
    while t < iterations:
        if t>0:
            x[:,t] = x[:,t-1].copy()
        for i in range(0, len(x)):
            x[i,t] = (B[i] + eqn(A[i], x[:,t],i)) / A[i,i]
            if(t>0):
                x[i,t] = w*x[i,t] + (1-w)*x[i,t-1]

        RE = (np.linalg.norm(x[:,t] - x[:,t-1],np.inf)) / (np.linalg.norm(x[:,t],np.inf) + 0)

        print(str(t+1)+"\t"+str(x[:,t].T)+"\t"+str(RE)+" \t"+str(w))
        t += 1

        if t == k+1: #in order to get the same result as in the example in T.Dowling's notes
            deltab = np.linalg.norm(x[:,t-1]-x[:,t-2],2)
            deltas= np.linalg.norm(x[:,t-2]-x[:,t-3],2)
            w = (2 / (1 + np.sqrt(1-(deltab / deltas))))

    print("trial          x1          x2          x3          ...")
    return (x.T,w)

def eqn(w,x,I):

    w = -1 * w
    res = np.multiply(w.T,x)
    res[I] = 0
    sum = np.sum(res)
    return sum
