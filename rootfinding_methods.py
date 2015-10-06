# rootfinding_methods
# rewritten from: https://gist.github.com/swvist/3775568

import sys
import numpy as np
import math
import matplotlib.pyplot as plt

# function f(x)
def my_func(x):    
    return x**3 - x - 2.0
    
# phi(x) = 0
def phi(x):
    return x**3 -  2.0

# 1st derivative
def dfdx(x):
    return 3.0 * x**2 - 1
    
# fixed-point method
def fixed_point(g, x0, tolerance = 0.000001, n_max = 1000) :
    err = sys.float_info.max
    for i in range(0, n_max):
        x = g(x0)
        print x
        err = np.abs(x - x0)
        
        if err < tolerance :
            return x        
        
        x0 = x
        
    
# bisection method
def bisection(f, a, b, tolerance = 0.000001, n_max = 1000):
    for i in range(0, n_max) :    
        c = (a + b) / 2.0
        fc = f(c)
        if np.abs(fc) or np.abs(b - a) < tolerance  :
            return c
        elif f(a) * fc > 0 :
            a = c
        else :
            b = c
            
if __name__ == "__main__":   
    root = bisection(my_func,1,2)
    print '(bisection) the root is ', root
    
    root = fixed_point(phi, 0.5)
    print '(fixed-point) the root is ', root
            
