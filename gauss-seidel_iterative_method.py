'''

radhitya@uwaterloo.ca

Gauss-Seidel iterative method
'''

import numpy as np

# In[]
 
def GSstep(A, u0, f):
    '''
    Usage: u = GSstep(A, u0, f)
    Performs one Gauss-Seidel iteration on
    A u = f using the guess u0.
    '''
    u = u0.copy()  # placeholder code
     
    return u
 
# In[]

def GSsolve(A, f, u0, maxIter, tol):
    '''
    u = GSsolve(A, f, u0, maxIter, tol)
    Iteratively solves A u = f using Gauss-Seidel iteration,
    starting with the initial guess u0. The matrix A must be
    NxN, and f must be an N-vector. The iteration stops
    either after maxIter iterations, or when the 2-norm of
    the residual is less than tol.    
    '''
    u = u0.copy()  # placeholder code
     
    return u