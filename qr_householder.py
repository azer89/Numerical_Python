
'''
QR Decomposition using Householder reflection

radhitya@uwaterloo.ca
'''

import numpy as np


# In[]:
'''
Function to calculate QR decomposition

parameter: 
    A: an MxN matrix where N <= M

return:
    Q: an orthogonal matrix whose size is MxM
    R: an upper-triangular matrix whose size is MxN        
'''
def myQR(A):
    M, N = np.shape(A)
    
    # This will be reduced to upper-triangular matrx
    R = A.copy()    
    
    # Q = I x Q_{1} x Q_{2} x Q_{3} x ...
    Q = np.eye(M, M)
    
    for k in range(0, N):
        
        # vector x
        x = R[k:M,k].copy()
        
        # e = {1, 0, 0, ...}
        e = np.zeros(len(x))
        e[0] = 1.0
        
        # the sign is implemented using cmp()
        #u = -cmp(x[0], 0) * np.linalg.norm(x, 2) * e - x
        u = cmp(x[0], 0) * np.linalg.norm(x, 2) * e + x
        
        # make it a unit vector
        u = u / np.linalg.norm(u, 2)
        
        # the transpose of u
        u_t = u.reshape((1, len(u))) 
        
        # should reshape into a 2-d array, I don't know why
        u = u.reshape(len(u), 1) 

        # calculate Q_{k} = I - 2 u u^T        
        I = np.eye(len(u), len(u))
        F = I - 2.0 * np.dot(u, u_t) 
        Q_k = np.eye(M, M)        
        Q_k[k:M, k:M] = F
        
        # Q = I x Q_{1} x Q_{2} x Q_{3} x ... 
        Q = np.dot(Q, Q_k)      
        
        for j in range(k, N):        
            utA = np.dot(u.T, R[k:M, j])
            R[k:M, j] = R[k:M, j] - 2.0 * np.dot(u, utA) 
        
    return Q, R

# In[]: these tests were written by Jeff Orchard (jorchard@uwaterloo.ca)
'''
A function that contains tests to check whether A = QR

params:
    A: an MxN matrix where N <= M
    Q: an orthogonal matrix whose size is MxM
    R: an upper-triangular matrix whose size is MxN 
'''
def testQR(A, Q, R):
    M, N = np.shape(A)    
    
    tests_passed = True
    
    # Is Q orthogonal?
    QTQ_error = abs( np.eye(M) - np.dot(Q.T, Q) )
    max_error = max(QTQ_error.flatten())
    if max_error>1e-12:
        print 'TEST FAILED: Q is not orthogonal'
        tests_passed = False
    
    # Is R upper-triangular?
    idx = np.tril_indices(M,k=-1,m=N)   # gives indices of sub-diagonal elements of MxN matrix
    for jk in zip(idx[0],idx[1]):       # loop through those elements...
        if abs(R[jk[0],jk[1]])>1.e-12:  # and check that they are all close to zero.
            print 'TEST FAILED: R is not upper-triangular'
            tests_passed = False
            break
    
    # Is Q*R equal to A?
    A_QR_error = abs( A - np.dot(Q, R) )
    max_error = max(A_QR_error.flatten())
    if max_error>1e-12:
        print 'TEST FAILED: Q*R is not equal to A'
        tests_passed = False
    
    # Summary
    if tests_passed:
        print 'Congratulations! Your myQR code seems to work.'
    else:
        print '!*!*! Back to the drawing board. Some of the tests failed. !*!*!'

# In[]:
if __name__ == "__main__":
    A = np.random.rand(100,5)
    Q, R = myQR(A)
    testQR(A, Q, R)



    