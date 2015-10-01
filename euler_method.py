'''
This code is rewritten from http://www.nervouscomputer.com/hfs/pdf/introtns/Getting-to-know-Python.pdf
'''

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

# right hand side of the ODE
def f(x, y) :
    return y + 1 # x doesn't matter since dy/dx is linear

# initial condition
y0 = 0

# time step
h = 0.01

# solve from 0 to time T
T = 10

# list of discretized time (visualization purpose only) 
x = np.linspace(0, T, int(T/h) + 1)

# solution
y = np.zeros(len(x)) 

y[0] = y0;

for i in xrange(1, len(x)) :
    y[i] = y[i - 1] + f(x[i - 1], y[i - 1]) * h
    
plt.figure()

plt.plot(x, y, color='red')
plt.show()
    


