"""
bezier interpolation
"""

import numpy as np
import matplotlib.pyplot as plt


"""
def PointInterpolation(poly, pt1, pt2, f = 0.5, subLimit = 0.1):
	if(np.linalg.norm(pt1 - pt2) <= subLimit):
		poly.append(pt1)
	else:
		newPt = pt1 + (pt2 - pt1) * f
		PointInterpolation(poly, pt1, newPt, f, subLimit)
		PointInterpolation(poly, newPt, pt2, f, subLimit)
"""


"""
def DeCasteljauMidPoint(p0, p1, p2, p3):
    splitParam = 0.5;	# split into two equal lengths

    x0 = p0[0]
    y0 = p0[1]
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1] 
    x3 = p3[0]
    y3 = p3[1]

    x01 = (x1 - x0) * splitParam + x0
    x12 = (x2 - x1) * splitParam + x1
    x23 = (x3 - x2) * splitParam + x2
    
    y01 = (y1 - y0) * splitParam + y0
    y12 = (y2 - y1) * splitParam + y1
    y23 = (y3 - y2) * splitParam + y2		

    x012 = (x12 - x01) * splitParam + x01
    x123 = (x23 - x12) * splitParam + x12
    
    y012 = (y12 - y01) * splitParam + y01
    y123 = (y23 - y12) * splitParam + y12

    x0123 = (x123 - x012) * splitParam + x012
    y0123 = (y123 - y012) * splitParam + y012

    return np.array([x0123, y0123])
"""


#def DeCasteljau(poly, p0, p1, p2, p3, subdivide_limit = 0.5):
def DeCasteljau(poly, p0, p1, p2, p3, depth = 0):    
    dist = np.linalg.norm(pt0 - pt3) 
    #print pt0, " ", pt3, " ", dist
    print pt0, " ", pt3    
    if(depth > 5):
    #if(dist <= subdivide_limit):
        #print "stop"
        poly.append(p0)  
    
    else:
        splitParam = 0.5;	# split into two equal lengths
        
        x0 = p0[0]
        y0 = p0[1]
        x1 = p1[0]
        y1 = p1[1]
        x2 = p2[0]
        y2 = p2[1] 
        x3 = p3[0]
        y3 = p3[1]
        
        x01 = (x1 - x0) * splitParam + x0
        x12 = (x2 - x1) * splitParam + x1
        x23 = (x3 - x2) * splitParam + x2
        
        y01 = (y1 - y0) * splitParam + y0
        y12 = (y2 - y1) * splitParam + y1
        y23 = (y3 - y2) * splitParam + y2		
        
        x012 = (x12 - x01) * splitParam + x01
        x123 = (x23 - x12) * splitParam + x12
        
        y012 = (y12 - y01) * splitParam + y01
        y123 = (y23 - y12) * splitParam + y12
        
        x0123 = (x123 - x012) * splitParam + x012
        y0123 = (y123 - y012) * splitParam + y012
        
        DeCasteljau(poly, np.array([x0, y0]),        np.array([x01, y01]),   np.array([x012, y012]), np.array([x0123, y0123]), depth + 1)
        DeCasteljau(poly, np.array([x0123,  y0123]), np.array([x123, y123]), np.array([x23, y23]),   np.array([x3, y3]),       depth + 1)

def CurveToBezier(p0, p1, p2, p3, t_smooth_factor = 0.1):

    xc1 = (p0[0] + p1[0]) / 2.0	
    yc1 = (p0[1] + p1[1]) / 2.0
    
    xc2 = (p1[0] + p2[0]) / 2.0		
    yc2 = (p1[1] + p2[1]) / 2.0
    
    xc3 = (p2[0] + p3[0]) / 2.0		
    yc3 = (p2[1] + p3[1]) / 2.0
    
    len1 = np.sqrt((p1[0] - p0[0]) * (p1[0] - p0[0]) + (p1[1] - p0[1]) * (p1[1] - p0[1]))
    len2 = np.sqrt((p2[0] - p1[0]) * (p2[0] - p1[0]) + (p2[1] - p1[1]) * (p2[1] - p1[1]))
    len3 = np.sqrt((p3[0] - p2[0]) * (p3[0] - p2[0]) + (p3[1] - p2[1]) * (p3[1] - p2[1]))
    
    k1 = len1 / (len1 + len2)
    k2 = len2 / (len2 + len3)
    
    xm1 = xc1 + (xc2 - xc1) * k1	
    ym1 = yc1 + (yc2 - yc1) * k1
    
    xm2 = xc2 + (xc3 - xc2) * k2	
    ym2 = yc2 + (yc3 - yc2) * k2
    
    # Resulting control points. Here t_smooth_factor should be in range [0...1]
    cp0 = np.array([0, 0])    
    cp1 = np.array([0, 0])    
    
    cp0[0] = xm1 + (xc2 - xm1) * t_smooth_factor + p1[0] - xm1
    cp0[1] = ym1 + (yc2 - ym1) * t_smooth_factor + p1[1] - ym1
    
    cp1[0] = xm2 + (xc2 - xm2) * t_smooth_factor + p2[0] - xm2
    cp1[1] = ym2 + (yc2 - ym2) * t_smooth_factor + p2[1] - ym2
    
    return cp0, cp1


N = 5
y_data = np.random.rand(N) * 10
x_data = np.arange(0, N, 1)

initial_data = []
# combine into 2d array
for i in range(N):
    initial_data.append(np.array([x_data[i], y_data[i]]))

# draw initial data
plt.figure(1)
plt.clf()
# draw points
for i in range(N):
    plt.plot(initial_data[i][0], initial_data[i][1],'o', color="magenta", markersize=7)
# draw lines
for i in range(N-1):    
    plt.plot([initial_data[i][0], initial_data[i+1][0]], [initial_data[i][1], initial_data[i+1][1]], 'k-', lw=0.5)
plt.show()

plt.figure(2)
plt.clf()
interpolated_data = []
for i in range(N-1):
    pt0 = np.array([i - 1, initial_data[i][1]])
    if(i > 0):
        pt0 = initial_data[i-1]
    
    pt1 = initial_data[i]
    pt2 = initial_data[i+1]
    
    pt3 = np.array([i + 2, initial_data[i+1][1]])
    if(i < N-2):
        pt3 = initial_data[i+2] 
        
    cp0, cp1 = CurveToBezier(pt0, pt1, pt2, pt3)
    
    plt.plot([pt1[0], cp0[0]], [pt1[1], cp0[1]], 'k-', lw=0.5)
    plt.plot([cp0[0], cp1[0]], [cp0[1], cp0[1]], 'k-', lw=0.5)
    plt.plot([pt2[0], cp1[0]], [pt2[1], cp1[1]], 'k-', lw=0.5)
        
    #new_segments = []
    #DeCasteljau(new_segments, pt0, pt1, pt2, pt3)
        
    """
    plt.plot(cp0[0], cp0[1],'o', color="green", markersize=10-i)
    plt.plot(cp1[0], cp1[1],'o', color="green", markersize=10-i)
    
    
    plt.plot(pt0[0], pt0[1],'o', color="red", markersize=10-i)
    plt.plot(pt1[0], pt1[1],'o', color="red", markersize=10-i)
    plt.plot(pt2[0], pt2[1],'o', color="red", markersize=10-i)
    plt.plot(pt3[0], pt3[1],'o', color="red", markersize=10-i)
    """
    
    
plt.show()
    
    #cp0, cp1 = CurveToBezier(pt0, pt1, pt2, pt3)
    
    #print np.linalg.norm(pt0 - pt3)
    
    #new_segments = []
    #DeCasteljau(new_segments, pt0, pt1, pt2, pt3)
    #print len(new_segments)    
    #interpolated_data.append(new_segments)



#a = np.linalg.norm(np.array([0, 1, 1.5]))

#data = []
#N = 10 # number of initial data
#for i in range(N):
    