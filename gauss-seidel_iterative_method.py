'''

radhitya@uwaterloo.ca

Gauss-Seidel iterative method
'''

import numpy as np

def GaussSeidelIteration(A, f, x0):
    x_new = x0.copy()
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
        
    return x_new
    
if __name__ == "__main__":
    # example from wikipedia
    A = np.array([[ 10.0, -1.0,  2.0,  0.0], 
                  [ -1.0, 11.0, -1.0,  3.0], 
                  [  2.0, -1.0, 10.0, -1.0],
                  [  0.0,  3.0, -1.0,  8.0]])
                  
    f = np.array([6.0, 25.0, -11.0, 15.0])
    
    
    x0 = np.zeros(len(f))
    x = GaussSeidelIteration(A, f, x0)
    
    
    print "the solution is:"
    print x