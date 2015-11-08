'''

radhitya@uwaterloo.ca

Gauss-Seidel iterative method
'''

import numpy as np

'''
 
def GSstep(A, u0, f):
    
    #Usage: u = GSstep(A, u0, f)
    #Performs one Gauss-Seidel iteration on
    #A u = f using the guess u0.
    
    u = u0.copy()  # placeholder code
     
    return u
 


def GSsolve(A, f, u0, maxIter, tol):
    
    #u = GSsolve(A, f, u0, maxIter, tol)
    #Iteratively solves A u = f using Gauss-Seidel iteration,
    #starting with the initial guess u0. The matrix A must be
    #NxN, and f must be an N-vector. The iteration stops
    #either after maxIter iterations, or when the 2-norm of
    #the residual is less than tol.    
    
    u = u0.copy()  # placeholder code
     
    return u
    
'''

# example from wikipedia
A = np.array([[ 10.0, -1.0,  2.0,  0.0], 
              [ -1.0, 11.0, -1.0,  3.0], 
              [  2.0, -1.0, 10.0, -1.0],
              [  0.0,  3.0, -1.0,  8.0]])
              
f = np.array([6.0, 25.0, -11.0, 15.0])

x_new = np.zeros(len(f)) 

max_iter = 100

row, col = np.shape(A)

for iter in range(max_iter): 
    x_prev = x_new.copy()
    for i in range(row):     
        substract_val = 0        
        for j in range(col):
            if i != j:
                substract_val += A[i, j] * x_new[j]
        x_new[i] = (f[i] - substract_val) / A[i][i]
    d = np.linalg.norm(x_prev - x_new)
    if d < 1e-10:
        break
    
q,r = np.linalg.qr(A)

# calculate the solution
qtb = np.dot(q.T, f)
x_array = np.linalg.solve(r, qtb)