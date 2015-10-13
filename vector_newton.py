# vector newton

import numpy as np

def my_f(x):
    fx = np.zeros(len(x))    
    
    x_1 = x[0]
    x_2 = x[1]
    x_3 = x[2]
    
    fx[0] = x_1**2.0 + x_2**2.0 - x_3 - 1.0
    fx[1] = x_1 + x_2 * x_3
    fx[2] = np.exp(x_1) - 0.5
    
    return fx
    
def my_Jacobian(x):
    x_1 = x[0]
    x_2 = x[1]
    x_3 = x[2]    
    
    j_matrix = np.zeros(shape=(3, 3))
    
    # first row
    j_matrix[0][0]  = 2.0 * x_1
    j_matrix[0][1]  = 2.0 * x_2
    j_matrix[0][2]  = -1.0
    
    # second row
    j_matrix[1][0]  = 1.0
    j_matrix[1][1]  = x_3
    j_matrix[1][2]  = x_2
    
    # third row
    j_matrix[2][0]  = np.exp(x_1)
    j_matrix[2][1]  = 0.0
    j_matrix[2][2]  = 0.0
    
    return j_matrix
    
def VectorNewtonsMethod(fcn, Jacobian, x_orig, xtol = 10e-7):
    x_history = [x_orig]    
    x_0 = x_orig
    for i in range(0, 20):    
        # solve J . delta_x = -fx
        j_matrix = Jacobian(x_0)
        min_fx = -fcn(x_0)
        delta_x = np.linalg.solve(j_matrix, min_fx)
        
        x_next = x_0 + delta_x
        x_history.append(x_next)

        d = np.linalg.norm(x_next - x_0)
        #print d        
        if d < xtol :
            print "SUCCESS"
            return x_history        
        
        x_0 = x_next
            
    print "FAILED"
    return x_history

x_0 = np.array([0.4, 0.0, 0.9])    # FAILED
#x_0 = np.array([0.0, 1.0, 0.0])    # SUCCESS
#x_0 = np.array([-0.69, 1.07, 0.64]) # this is really close to the solution
x_history = VectorNewtonsMethod(my_f, my_Jacobian, x_0)
print "the solution is :", x_history[-1]