
"""
Reza Adhitya Saputra
radhitya@uwaterloo.ca


Eigenvalues and Eigenvectors DEMO

"""

import numpy as np

# This code is adapted from Jeff Orchard's demo during UWaterloo CS770 (Fall 2015)

"""
The power iteration to find
the largest eigenvalue (magnitude)
"""
def PowerIteration(M, n_iter=100):
    v = np.random.rand(4)
    v = v / np.linalg.norm(v)
    for k in range(n_iter):
        w = np.dot(M, v)
        v = w / np.linalg.norm(w)
        l = np.dot(v.T, np.dot(M, v)) # raleigh quotient
    return l, v

if __name__ == "__main__":
    
    # Real symmetric matrix
    N = 4
    A = np.random.rand(N, N) - 0.5
    A = A + A.T
    
    
    """ DEMO 1 """   
    # Eigen decomposition (L: Eigenvalues. V: Eigenvectors)
    L, V = np.linalg.eig(A)
            
    # Raleigh quotient
    # if x is an eigenvector then r(x) is an eigenvalue
    
    # eigenvalue 1
    x0 = V[:,0]
    r0 = np.dot(x0.T, np.dot(A, x0)) / np.dot(x0.T, x0)
    
    # eigenvalue 2
    x1 = V[:,1]
    r1 = np.dot(x1.T, np.dot(A, x1)) / np.dot(x1.T, x1)
    
    # eigenvalue 3
    x2 = V[:,2]
    r2 = np.dot(x2.T, np.dot(A, x2)) / np.dot(x2.T, x2)
    
    # eigenvalue 4
    x3 = V[:,3]
    r3 = np.dot(x3.T, np.dot(A, x3)) / np.dot(x3.T, x3)

    """ DEMO 2 """ 
    # biggest magnitude 
    l_big, v_big = PowerIteration(A)
    print "Power Iteration"
    print "eigenvalue: ", l_big, "    eigenvector: ", v_big  
    
    # smallest magnitude
    l_small, v_small = PowerIteration(np.linalg.inv(A))
    l_small = 1.0/l_small
    print "Power Iteration"
    print "eigenvalue: ", l_small, "    eigenvector: ", v_small  
    
    """ DEMO 3 """
    mu = 0.7
    B = A - mu * np.eye(4)
    L_B, V_B = np.linalg.eig(B) # the eigenvalues are shifted by mu
    
    """ DEMO 4 """
    # QR Iteration
    Ak = A.copy()
    Q = np.eye(N)
    n_iter = 1000
    for i in range(n_iter):
        q, r = np.linalg.qr(Ak)
        Ak = np.dot(r, q)
        Q = np.dot(Q, q)
        
    print "(QR) E-values:\n", np.round(np.diag(Ak), 10)
    print "(QR) E-vectors:\n", np.round(Q, 10)
        
    
    
    
    
    
    