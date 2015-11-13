'''

radhitya@uwaterloo.ca

a matrix version of gauss-seidel method

'''
import numpy as np

'''
Function to perform forward substitution
'''
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

'''
A single step of Gauss-Seidel method

parameters:
    A     : a square matrix
    u0    : the initial guess
    f     : the right hand side matrix, Ax = f
    
optional parameters:
    DminL : a lower-triangular (D - L) matrix, where A = D - L - U
    U     : an upper triangular matrix without the diagonal, where A = D - L - U
return:
    x_new : the approximate solution of x
'''
def GSstep(A, u0, f, DminL=None, U=None):
    
    # the user can feed the precomputed (D - L) and U to speed up computation
    if DminL is None or U is None:
        # create a diagonal matrix D    
        D_vec = np.diag(A)
        D = np.zeros(np.shape(A))
        for i in range(len(D_vec)):
            D[i, i] = D_vec[i] 
        
        # create lower-triangular matrix
        L = -np.tril(A) + D 
    
        # create upper-triangular matrix        
        U = -np.triu(A) + D
        
        # calculate D - L once
        DminL = D - L

    # b + U x_{n}
    right_side = f + np.dot(U, u0)
    
    # calculate x_{n+1} using forward substitution        
    return forwardsub(DminL, right_side)
        
'''
Solve a linear system with
    (D - L) x_{n+1} = (b + U x_{n})

where
    A = D - L - U

'''
def GSsolve(A, f, u0, maxIter = 100, tol = 1e-10):
    
    # precompute A = D - L - U (optional)
    # create a diagonal matrix D    
    D_vec = np.diag(A)
    D = np.zeros(np.shape(A))
    for i in range(len(D_vec)):
        D[i, i] = D_vec[i]     
    # create lower-triangular matrix
    L = -np.tril(A) + D 
    # create upper-triangular matrix        
    U = -np.triu(A) + D    
    # calculate D - L once
    DminL = D - L
    
    x_new = u0.copy()
    
    for iter in range(maxIter): 
        # perform a single step        
        x_new = GSstep(A, x_new, f, DminL, U) 
        
        # if the residual is below threshold, we stop        
        Ax = np.dot(A, x_new)               
        residual = np.linalg.norm(f - Ax)
        if residual < tol:
            print "stopped after ", iter, " iterations"
            break
    
    # return the solution        
    return x_new

'''
Main function
'''
if __name__ == "__main__":
    A = np.array([[ 10.0, -1.0,  2.0,  0.0], 
                  [ -1.0, 11.0, -1.0,  3.0], 
                  [  2.0, -1.0, 10.0, -1.0],
                  [  0.0,  3.0, -1.0,  8.0]])
                  
    f = np.array([6.0, 25.0, -11.0, 15.0])
    
    u0 = np.zeros(len(f))
    u = GSsolve(A, f, u0)
              

    
    
    
