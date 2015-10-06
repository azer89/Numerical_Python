# rootfinding_methods
# rewritten from: https://gist.github.com/swvist/3775568

import numpy as np
import math
import matplotlib.pyplot as plt

# function f(x) x^3 - x - 2
def my_func(x):    
    return x**3 - x - 2.0

# 1st derivative df(x)/dx = 3x^2 - 1
def dfdx(x):
    return 3.0 * x**2 - 1
    
# bisection method
def bisection(f, a, b, tolerance = 0.000001, n_max = 100):
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
    print 'the root is ', root
            
