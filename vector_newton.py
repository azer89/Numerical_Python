

'''
Vector Newton - Finding the solution of a linear system of equations

Reza Adhitya Saputra
Computer Science Department - University of Waterloo
radhitya@uwaterloo.ca
'''

import numpy as np

'''
vector-valued f(x), where x is a vector
'''
def my_f(x):
    x_1 = x[0]
    x_2 = x[1]
    x_3 = x[2]
    
    fx = np.zeros(len(x))
    fx[0] = x_1**2.0 + x_2**2.0 - x_3 - 1.0
    fx[1] = x_1 + x_2 * x_3
    fx[2] = np.exp(x_1) - 0.5
    
    return fx

'''
The jacobian matrix of f(x), x should be a vector
'''
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
    
'''
vector newton

note that the last parameter is tolerance
'''
def VectorNewtonsMethod(fcn, Jacobian, x_orig, xtol = 10e-7):
    x_history = [x_orig]   # a list containing the appoximate solutions
    x_0 = x_orig
    
    # the loop is only 20 times
    for i in range(0, 20):           
        j_matrix = Jacobian(x_0)    # ontain the jacobian matrix
        min_fx = -fcn(x_0)          # obtain -f(x)
        delta_x = np.linalg.solve(j_matrix, min_fx) # solve J . delta_x = -fx
        
        x_next = x_0 + delta_x      # obtain x_{n+1} = x_{n} + delta_x
        x_history.append(x_next)    # store x values

        d = np.linalg.norm(x_next - x_0)    # get the euclidean distance   
        if d < xtol :
            # the distance is less than the tolerance
            print "SUCCESS"
            return x_history        
        
        # update
        x_0 = x_next
    
    # stop after 20 iterations
    # it's sad, since we are not close enough to the solution
    print "FAILED"
    return x_history

'''
These below are bunch of initial values,
uncomment one of them
'''
#x_0 = np.array([0.4, 0.0, 0.9])    # FAILED
x_0 = np.array([0.0, 1.0, 0.0])    # SUCCESS
#x_0 = np.array([-0.69, 1.07, 0.64]) # SUCCESS, this is really close to the solution

# calculate the solution
x_history = VectorNewtonsMethod(my_f, my_Jacobian, x_0)
xstar = x_history[-1] # the solution is the last element of the list

print "the solution is :", xstar

