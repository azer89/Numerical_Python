"""
radhitya@uwaterloo.ca

SVD Demo

This code is adapted from Jeff Orchard's demo during UWaterloo CS770 (Fall 2015)

"""


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D # without this, the 3d plot will not work


"""
RotationMatrix(tx, ty, tz)
tx, ty and tz are the rotation angles about the x-, y- and z-axes, respectively
(in radians). The output is a 3x3 rotation matrix.
"""
def RotationMatrix(t0, t1, t2):    
    M = np.zeros([3,3])
    M = np.array([[1., 0, 0],[0, np.cos(t0), -np.sin(t0)],[0, np.sin(t0), np.cos(t0)]])
    M = np.dot(np.array([[np.cos(t1), 0, np.sin(t1)],[0, 1., 0],[-np.sin(t1), 0, np.cos(t1)]]), M)
    M = np.dot(np.array([[np.cos(t2), -np.sin(t2), 0],[np.sin(t2), np.cos(t2), 0],[0, 0, 1.]]), M)
    return M


"""
A test function to check if a matrix is orthogonal
input:
    M: the input matrix
    n: number of columns
"""
def IsOrthogonal(M):
    n_rows, n_cols = M.shape
    MTM_error = abs( np.eye(n_cols) - np.dot(M.T, M) )
    max_error = max(MTM_error.flatten())    
    if max_error>1e-12:
        print "TEST FAILED: Matrix is not orthogonal"
    else:
        print "TEST SUCCESS: Matrix is orthogonal"
        

sigma0  = 1.5                       # standard deviation along x-axis
sigma1  = 0.1                       # standard deviation along y-axis
sigma2  = 0.5                       # standard deviation along z-axis
mu      = np.array([0.0, 0.0, 0.0]) # centroid of the cluster
N       = 1000                      # number of points
M       = np.diag([sigma0, sigma1, sigma2])
points1 = np.random.normal(0.0, 1.0, size=[N, 3])
points1 = np.dot(points1, M)
points2 = np.dot(points1, RotationMatrix(30.0 / 180.0 * np.pi, 0, 0).T) + mu


fig = plt.figure(1)
fig.clf()
ax = fig.add_subplot(111, projection="3d")
#ax.scatter(points1[:,0], points1[:,1], points1[:,2], color="red")
ax.scatter(points2[:,0], points2[:,1], points2[:,2])
plt.xlabel("x")
plt.ylabel("y")
ax.set_zlabel("z")
minbound = -3
maxbound = 3
ax.auto_scale_xyz(*[[minbound, maxbound]]*3)
ax.axis("scaled")


U, S, V = np.linalg.svd(points2, full_matrices=0)
print "\n The shapes of U, S, V:"
print np.shape(U)
print np.shape(S)
print np.shape(V)


# Let's look what V holds
SV = np.dot( np.diag(np.sqrt(S)), V )
print "\nSV:"
print SV


c = ["red", "green", "yellow"]
for i in range(len(S)):
    plt.plot([0, SV[i,0]], [0, SV[i,1]], [0, SV[i,2]], c[i])
ax.auto_scale_xyz(*[[minbound, maxbound]]*3)


# Are U and V orthogonal
print "\nIs U orthogonal ?"
IsOrthogonal(U)
print "\nIs V orthogonal ?"
IsOrthogonal(V)








