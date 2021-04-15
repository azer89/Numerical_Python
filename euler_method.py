from __future__ import division
import numpy as np
import matplotlib.pyplot as plt


# right hand side of the ODE
def f(x, y) :
    # because the derivative of e^x is e^2
    return y;
    
# initial condition
y0 = 1

# time step
h = 0.1

# solve from 0 to time T
T = 5

# list of discretized time (visualization purpose only) 
x = np.linspace(0, T, int(T/h) + 1)

# Oiler solution
y = np.zeros(len(x))

# initial condition
y[0] = y0;

# let's compute oiler method
for i in range(1, len(x)):
    y[i] = y[i-1] + f(x[i-1],y[i-1])*h
  
# the true solution
y_true = np.exp(x)
    
plt.figure()
plt.plot(x,y,'b.-',x,y_true,'r-')
plt.legend(['Euler method','True e^x'])
plt.show()
    


