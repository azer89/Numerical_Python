
"""
scipy.optimize.minimize
"""

import numpy as np
import scipy.optimize as optimize

def f1(c):
    return np.sqrt(c[0]**2 + c[1]**2 + c[2]**2)
    

def f2(x):
    return np.linalg.norm(x[0]) + np.linalg.norm(x[1])

'''
result = optimize.minimize(f1, [0.0, 0.0, 0.0])
sol = result.x
print(sol)
'''

result = optimize.minimize(f2, [[0.0, 0.0], [0.0, 0.0]])
sol = result.x
print(sol)

