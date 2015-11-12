'''

radhitya@uwaterloo.ca

Jacobi iterative method
'''

import numpy as np

def JacobiIteration(A, f, x0, maxIter = 100, tol = 1e-10):
    x_new = x0.copy() 
        
    row, col = np.shape(A)
    
    for iter in range(maxIter): 
        
        x_copy = x_new.copy()
        for i in range(row):     
            substract_val = 0        
            for j in range(col):
                if i != j:
                    substract_val += A[i, j] * x_new[j]
            x_copy[i] = (f[i] - substract_val) / A[i][i]
        x_new = x_copy.copy()
        
        
        # if the residual is below threshold, we stop
        Ax = np.dot(A, x_new)               
        residual = np.linalg.norm(f - Ax)
        if residual < tol:
            print "stopped after ", iter, " iterations"
            break
        
    return x_new

if __name__ == "__main__":
    # example from wikipedia
    A = np.array([[ 10.0, -1.0,  2.0,  0.0], 
                  [ -1.0, 11.0, -1.0,  3.0], 
                  [  2.0, -1.0, 10.0, -1.0],
                  [  0.0,  3.0, -1.0,  8.0]])
                  
    f = np.array([6.0, 25.0, -11.0, 15.0])
    
    
    x0 = np.zeros(len(f))
    x = JacobiIteration(A, f, x0)    
    
    print "the solution is:"
    print x