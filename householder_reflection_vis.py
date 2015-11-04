'''
Householder Reflections
'''

import numpy as np
import matplotlib.pylab as plt

x = np.random.rand(2) - 0.5

e = np.zeros(len(x))
e[0] = 1.0

fx_plus = np.linalg.norm(x, 2) * e
fx_neg = -1.0 * np.linalg.norm(x, 2) * e

u_1 = cmp(x[0], 0) * np.linalg.norm(x, 2) * e + x
u_2 = -cmp(x[0], 0) * np.linalg.norm(x, 2) * e - x

u_1 = u_1.reshape(len(u_1), 1)
u_2 = u_2.reshape(len(u_2), 1)

u_1_norm = u_1 / np.linalg.norm(u_1, 2)
u_2_norm = u_2 / np.linalg.norm(u_2, 2)

u_1_t = u_1.reshape((1, len(u_1_norm))) 
u_2_t = u_2.reshape((1, len(u_1_norm))) 

#I = np.eye(len(u_1), len(u_1))
##
#F_1 = I - 2.0 * np.dot(u_1_norm, u_1_t) 
#F_2 = I - 2.0 * np.dot(u_2_norm, u_2_t) 
##
#Fx_1 = np.dot(F_1, x) 
#Fx_2 = np.dot(F_2, x)

uutx_1 = -2.0 * np.dot(u_1_norm, np.dot(u_1_t, x))
uutx_2 = -2.0 * np.dot(u_1_norm, np.dot(u_2_t, x))

plt.clf()
plt.plot([-1, 1], [0, 0], color='gray')
plt.plot([0, 0], [-1, 1], color='gray')
circle = plt.Circle((0,0), np.linalg.norm(x, 2))
circle.set_edgecolor( 'gray' )
circle.set_facecolor( 'none' )
fig = plt.gcf()
fig.gca().add_artist(circle)

plt.plot([0.0, x[0]], [0.0, x[1]], color='red', label='x')


plt.plot([0.0, u_1[0]], [0.0, u_1[1]], color='green', label = 'sign(x1)||x||e + x')
plt.plot([0.0, u_2[0]], [0.0, u_2[1]], color='blue', label = '-sign(x1)||x||e - x')

#plt.plot([0.0, u_1_norm[0]], [0.0, u_1_norm[1]], color='green', linewidth=2)
#plt.plot([0.0, u_2_norm[0]], [0.0, u_2_norm[1]], color='blue', linewidth=2)

plt.plot([0.0, fx_plus[0]], [0.0, fx_plus[1]], color='green', linewidth=3, linestyle='dashed', label='Fx = ||x||e')
plt.plot([0.0, fx_neg[0]], [0.0, fx_neg[1]], color='blue', linewidth=3, linestyle='dashed', label='-Fx = -||x||e')

#plt.plot([0, uutx_1[0]], [0, uutx_1[1]], color='orange', linewidth=2, label='-2 u u^T x')
#plt.plot([0, uutx_2[0]], [0, uutx_2[1]], color='purple', linewidth=2, label='-2 u u^T x')

#plt.plot([x[0], x[0] + uutx_1[0]], [x[1], x[1] + uutx_1[1]], color='orange', linewidth=2, label='-2 u u^T x')
#plt.plot([x[0], x[0] + uutx_2[0]], [x[1], x[1] + uutx_2[1]], color='orange', linewidth=2, label='-2 u u^T x')

plt.legend(loc='upper right', shadow=False)
plt.axes().set_aspect('equal', 'datalim')
plt.show()