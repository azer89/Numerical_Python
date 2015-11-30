
"""
scipy.optimize.minimize
"""

import numpy as np
import scipy.optimize as optimize

def f(c):
    return np.sqrt(c[0]**2 + c[1]**2 + c[2]**2)

result = optimize.minimize(f, [0.0, 0.0, 0.0])
sol = result.x
print(sol)