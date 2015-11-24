

'''
Reza Adhitya Saputra
Computer Science Department - University of Waterloo
radhitya@uwaterloo.ca
'''

# rootfinding methods

import sys
import numpy as np
import math
import matplotlib.pyplot as plt

plt.ion()

# default parameters
default_tol = 0.000001
default_n_max = 1000

# function f(x) we want to find its roots
def my_func(x):
    return x - math.cos (x)
    #return x**3 - x - 2.0
    
# phi(x) = x
# this function is the input for the bisection method
def phi(x):
    return math.cos(x)    
    #return x**3 -  2.0
    
# 1st derivative
    # this function is the input for newton method
def dfdx(x):
    return math.sin(x) + 1.0    
    #return 3.0 * x**2 - 1
  
'''  
Secant method
f       function f(x)
x0      1st initial guess
x1      2nd initial guess
'''
def secant(f, x0, x1, tolerance = default_tol, n_max = default_n_max) :
    err = sys.float_info.max
    x_history = [x0, x1]
    x = 0
    for i in range(0, n_max):     
        x_1 = x_history[-1]
        x_2 = x_history[-2]
        x = x_1 - f(x_1) * ((x_1 - x_2) / ( f(x_1) - f(x_2) )) 
        x_history.append(x)   
        err = np.abs(x - x_1)
        
        if err < tolerance :
            return x, x_history
    
    return x, x_history
    
    
'''  
Newton method
f       function f(x)
deriv   1-order derivation of f(x)
x0      initial guess
'''
def newton(f, deriv, x0, tolerance = default_tol, n_max = default_n_max) :
    err = sys.float_info.max
    x = x0
    x_history = [x0]
    for i in range(0, n_max):                
        x = x0 - ( f(x0) / deriv(x0) )
        x_history.append(x)  
        err = np.abs(x - x0)
        
        if err < tolerance:
            return x, x_history        
        
        x0 = x
        
    return x, x_history

'''  
Fixed-point method
p       function p(x) = x
x0      initial guess
'''
def fixed_point(p, x0, tolerance = default_tol, n_max = default_n_max) :
    err = sys.float_info.max
    x = x0
    x_history = [x0]
    for i in range(0, n_max):
        x = p(x0)
        x_history.append(x)  
        err = np.abs(x - x0)
        
        if err < tolerance:
            return x, x_history        
        
        x0 = x
    
    return x, x_history
        
    
'''  
Bisection method
f       function f(x)
as      lower limit
b       upper limit
'''
def bisection(f, a, b, tolerance = default_tol, n_max = default_n_max):   
    c = 0
    for i in range(0, n_max) :    
        c = (a + b) / 2.0
        fc = f(c)        
        if np.abs(fc) < tolerance or np.abs(b - a) < tolerance :
            return c
        elif f(a) * fc > 0 :
            a = c
        else :
            b = c
    
    return c

'''          
Visualization for fixed-point iterations
'''
def plot_fixed_point_method(p, a, b, x_history):    
    x_all = np.arange(a, b, 0.01)
    y_all = np.zeros(len(x_all))
    for i in range(0, len(x_all)):
        y_all[i] = p(x_all[i])
    plt.plot(x_all, y_all, color='blue')    

    y_x_history = np.zeros(len(x_history))
    for i in range(0, len(x_history)) :
        y_x_history[i] = p(x_history[i])    
    
    # draw lines
    for i in range(0, len(y_x_history) - 1) :
        cur_y = y_x_history[i]        
        cur_x = x_history[i]
        next_y = y_x_history[i + 1]        
        next_x = x_history[i + 1]
        
        #if i == 0:
        #    # draw a line from (x0, 0) to (x0, yo) 
        #    plt.plot([cur_x, cur_x], [0.0, cur_y], 'k-', lw=0.5)
            
        # draw a line from phi(x_n) to x_n = y_n
        plt.plot([cur_x, cur_y], [cur_y, cur_y], 'k-', lw=0.5)
        
        # draw a line from x_n = y_n to phi(x_{n+1})
        plt.plot([cur_y, next_x], [cur_y, next_y], 'k-', lw=0.5)
        
    plt.plot([0, 1], [0, 1], 'k-', lw=0.5)
    plt.plot(x_history, y_x_history, 'ro')
    
    plt.show()
    
'''
Main function
'''
if __name__ == "__main__":
    #root = bisection(my_func, 0.0, 1.0)
    #print '(bisection) the root is ', root
    
    root, x_history = fixed_point(phi, 0.5)
    print '(fixed-point) the root is ', root    
    plot_fixed_point_method(phi, 0.0, 1.0, x_history)
    
    #root, x_history = newton(my_func, dfdx, 0.5)
    #print '(newton) the root is ', root    
    
    #root, x_history = secant(my_func, 0.4, 0.6)
    #print '(secant) the root is ', root   
            
