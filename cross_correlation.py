# -*- coding: utf-8 -*-
"""
cross correlation

inspired from: https://www.youtube.com/watch?v=RO8s1TrElEw
"""

import numpy as np
import matplotlib.pyplot as plt


def GetDelay(s1, s2):
    corrs = []
    for delay in range(-N + 1, N): 
        sum_val = 0
        
        if(delay >= 0):      
            i_array = range(delay, N)
            j_array = range(N - delay)
        else:
            j_array = range(-delay, N)
            i_array = range(0, N + delay)
        
        for ctr in range(N - np.abs(delay)):
            i = i_array[ctr]
            j = j_array[ctr]
            sum_val += s1[i] * s2[j]
            
        corrs.append(sum_val)
        
    delay = np.argmax(np.absolute(corrs)) - N + 1
    
    return delay



s1 = np.array([0.1, 0.2, -0.1, 4.1, -2.0, 1.5, 0.0])
s2 = np.array([0.1, 4.0, -2.2, 1.6,  0.1, 0.1, 0.2])
N = len(s1)
    
delay1 = GetDelay(s1, s2)
delay2 = GetDelay(s2, s1)

plt.clf()
plt.plot(np.arange(len(s1)), s1)
plt.plot(np.arange(len(s2)), s2)
plt.show()

