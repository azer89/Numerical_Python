# rootfinding_methods
# rewritten from: https://gist.github.com/swvist/3775568

import sys
import numpy as np
import math
import matplotlib.pyplot as plt

# function f(x)
def my_func(x):
    return x - math.cos (x)
    #return x**3 - x - 2.0
    
# phi(x) = x
def phi(x):
    return math.cos(x)    
    #return x**3 -  2.0

# 1st derivative
def dfdx(x):
    return math.sin(x) + 1.0    
    #return 3.0 * x**2 - 1
    
# fixed-point method
def fixed_point(p, x0, tolerance = 0.000001, n_max = 1000) :
    err = sys.float_info.max
    x_history = []
    for i in range(0, n_max):
        x = p(x0)
        x_history.append(x)        
        #print x
        err = np.abs(x - x0)
        
        if err < tolerance or i == n_max - 1:
            return x, x_history        
        
        x0 = x
        
    
# bisection method
def bisection(f, a, b, tolerance = 0.000001, n_max = 1000):
    
    for i in range(0, n_max) :    
        c = (a + b) / 2.0
        fc = f(c)
        
        #print fc
        if np.abs(fc) < tolerance or np.abs(b - a) < tolerance  or i == n_max - 1:
            return c
        elif f(a) * fc > 0 :
            a = c
        else :
            b = c

# visualization
def plot_phi_func(p, a, b, x_history):    
    x_all = np.arange(a, b, 0.01)
    y_all = np.zeros(len(x_all))
    for i in range(0, len(x_all)):
        y_all[i] = p(x_all[i])
    plt.plot(x_all, y_all, color='blue')
    

    y_x_history = np.zeros(len(x_history))
    for i in range(0, len(x_history)) :
        y_x_history[i] = p(x_history[i])
    plt.plot(x_history, y_x_history, 'ro')
    
    
    plt.show()
    
            
if __name__ == "__main__":   
    root = bisection(my_func, 0.0, 1.0)
    print '(bisection) the root is ', root
    
    root, x_history = fixed_point(phi, 0.5)
    print '(fixed-point) the root is ', root
    
    plot_phi_func(phi, 0.0, 1.0, x_history)
            
