
'''
Reza Adhitya Saputra
Computer Science Department - University of Waterloo
radhitya@uwaterloo.ca
'''

from __future__ import division
import numpy as np
import matplotlib.pylab as plt
plt.ion()

# In[] Parameters

tol           = 0.001
y0            = 0.01 
t_start       = 0.0
t_end         = 15.0
max_step      = 2.0
max_gamma     = 5.0
safety_factor = 0.8

# In[] The deivative function

def logistic(y, t):
    return y * (1 - y)

# In[] Adaptive ODE    

def ode12(de_fcn, tspan, y0, tol, h0 = 0.5):
    t_history = [tspan[0]]    
    y_history = [y0]
    
    t_end     = tspan[1]
    current_t = h0  # timestamp    
    current_h = h0  # current h = h_{opt}
    
    while(current_t < t_end) :         
        t_prev   = t_history[-1]
        y_prev   = y_history[-1]
        
        euler_step = current_h * de_fcn(y_prev, t_prev) 
        k1 = current_h * de_fcn( y_prev, t_prev, )
        k2 = current_h * de_fcn( y_prev + k1, current_t)        
        y_euler = y_prev + euler_step       # y_{n+1} euler
        y_heun  = y_prev + (k1 + k2) / 2.0  # y_{n+1} heun
        
        l_error = np.abs(y_euler - y_heun)              # l{n+1} 
        gamma = min(safety_factor * ((tol / l_error)**0.5), max_gamma)
        h_opt = min(current_h * gamma, max_step)        # cannot be larger than max_step                      
        
        if l_error < tol:
            # case 1: l{n+1} < tolerance
            y_history.append(y_heun)
            t_history.append(current_t)
            current_t = current_t + current_h        
        #else :
            # case 2: do nothing, repeat the loop   
        
        # always update h = h_{opt} whenever we get case 1 or case 2
        current_h = h_opt
        
    return y_history, t_history

# In[]   

y, t = ode12(logistic, [t_start, t_end], y0, tol)
  
# plot solution
plt.figure(1)
plt.clf()
plt.plot(t, y, color='blue'); 

# plot timestaps as vertical lines
for i in t:    
    plt.plot([i, i], [0.0, 1.0], 'k-', lw=0.5)

plt.show()


