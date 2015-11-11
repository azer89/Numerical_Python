'''

radhitya@uwaterloo.ca

a matrix version of jacobi method

'''

import numpy as np


'''
Function to perform backward substitution
'''
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

'''

A = D - L - U

D x_{n+1} = b + (L + U) x_{n}
'''
def JacobiSolve(A, f, u0, maxIter, tol):
    
    # create a diagonal matrix D 
    D_vec = np.diag(A)
    D = np.zeros(np.shape(A))
    for i in range(len(D_vec)):
        D[i, i] = D_vec[i] 
    
    # create lower-triangular matrix
    L = -np.tril(A) + D

    # create upper-triangular matrix          
    U = -np.triu(A) + D
    
    # calculate L + U once
    LplusU = L + U
    
    x_new = u0.copy()
    for iter in range(maxIter): 
        #x_prev = x_new.copy()
        
        # b + (L + U) x_{n}
        right_side = f + np.dot(LplusU, x_new)
        
        # calculate x_{n+1} using backward substitution 
        x_new = backsub(D, right_side)
        
        Ax = np.dot(A, x_new)               
        residual = np.linalg.norm(f - Ax)
        if residual < tol:
            print "stopped after ", iter, " iterations"
            break
    
    # return the solution
    return x_new
    

if __name__ == "__main__":
    A = np.array([[ 10.0, -1.0,  2.0,  0.0], 
                  [ -1.0, 11.0, -1.0,  3.0], 
                  [  2.0, -1.0, 10.0, -1.0],
                  [  0.0,  3.0, -1.0,  8.0]])
                  
    f = np.array([6.0, 25.0, -11.0, 15.0])
    
    u0 = np.zeros(len(f))
    u = JacobiSolve(A, f, u0, 100, 1e-10)
              
              
