import numpy as np
import matplotlib.pylab as plt 
from scipy.integrate import odeint

Ts = 5.0
k  = -0.2

def func(T, t):
    return [k * ( T[0] - Ts)]
    
t = np.arange(0, 10, 0.01)

t0 = 20.0

sol = odeint(func, t0, t)
plt.plot(t, sol, color='blue')
plt.show()

 