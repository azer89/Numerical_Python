
# heun's method vs euler method

from __future__ import division
import numpy as np
import math
import matplotlib.pyplot as plt

# right hand side of the ODE
def f(x, y) :
    return y * (1 - y) 
    #return y + 1 # x doesn't matter since dy/dx is linear

# initial condition
y0 = 0.01

# time step
h = 0.5

# solve from 0 to time T
T = 15

# list of discretized time (visualization purpose only) 
x = np.arange(0, T, 0.5)
#x = np.linspace(0, T, T * 2)

# heun's method
y_h = np.zeros(len(x)) 
y_h[0] = y0;
for i in xrange(1, len(x)) :
    k1 = h * f(x[i - 1], y_h[i - 1])
    k2 = h * f(x[i], y_h[i - 1] + k1)
    y_h[i] = y_h[i - 1] + (k1 + k2) / 2

# euler's method    
y_e = np.zeros(len(x)) 
y_e[0] = y0;
for i in xrange(1, len(x)) :
    y_e[i] = y_e[i - 1] + f(x[i - 1], y_e[i - 1]) * h
    
plt.figure()



plt.plot(x, y_h, color='blue')
plt.plot(x, y_e, color='red')
plt.show()
    
