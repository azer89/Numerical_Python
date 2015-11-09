'''

radhitya@uwaterloo.ca

a matrix version of gauss-seidel method

'''
import numpy as np

def forwardsub(L, b):
    row, col = np.shape(L)
    y = b.copy()

    # first row
    y[0] = y[0] / L[0][0]
    
    for i in range(1, col):   # iterate rows
        for j in range(0, i): # iterate columns
            y[i] = y[i] - L[i][j] * y[j]
        y[i] = y[i] / L[i][i]
    
    return y

def GSsolve(A, f, u0, maxIter, tol):
    D_vec = np.diag(A)
    D = np.zeros(np.shape(A))
    for i in range(len(D_vec)):
        D[i, i] = D_vec[i] 
    
    L = np.tril(A) - D        
    U = np.triu(A) - D
    
    L = -L
    U = -U     
    
    DminL = D - L
    
    x_new = u0.copy()
    for iter in range(maxIter): 
        x_prev = x_new.copy()
        right_side = f + np.dot(U, x_new)
        x_new = forwardsub(DminL, right_side)
        d = np.linalg.norm(x_prev - x_new)
        if d < tol:
            print "stopped after ", iter, " iterations"
            break
        
    return x_new
    
if __name__ == "__main__":
    A = np.array([[ 10.0, -1.0,  2.0,  0.0], 
                  [ -1.0, 11.0, -1.0,  3.0], 
                  [  2.0, -1.0, 10.0, -1.0],
                  [  0.0,  3.0, -1.0,  8.0]])
                  
    f = np.array([6.0, 25.0, -11.0, 15.0])
    
    u0 = np.zeros(len(f))
    u = GSsolve(A, f, u0, 100, 1e-10)
              

    
    
    
