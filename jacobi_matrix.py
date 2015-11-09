'''

radhitya@uwaterloo.ca

a matrix version of jacobi method

'''

import numpy as np

def backsub(U, b):
    row, col = np.shape(U)
    y = b.copy()

    # last row
    y[col - 1] = y[col - 1] / U[col - 1][col - 1]
    
    for i in range(col - 2, -1, -1):
        for j in range(col - 1, i, -1):
            y[i] = y[i] - U[i][j] * y[j]
        y[i] = y[i] / U[i][i]
    
    return y
    
def JacobiSolve(A, f, u0, maxIter, tol):
    D_vec = np.diag(A)
    D = np.zeros(np.shape(A))
    for i in range(len(D_vec)):
        D[i, i] = D_vec[i] 
    
    L = np.tril(A) - D        
    U = np.triu(A) - D
    
    L = -L
    U = -U 
    
    LplusU = L + U
    
    x_new = u0.copy()
    for iter in range(maxIter): 
        x_prev = x_new.copy()
        right_side = f + np.dot(LplusU, x_new)
        x_new = backsub(D, right_side)
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
    u = JacobiSolve(A, f, u0, 100, 1e-10)
              
              
