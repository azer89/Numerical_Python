"""
bezier interpolation
"""

import numpy as np
import matplotlib.pyplot as plt

#fix: http://stackoverflow.com/questions/25157838/drawing-half-arc-of-bezier-curve
#def DeCasteljau(poly, p0, p1, p2, p3, subdivide_limit = 0.5):
def DeCasteljau(poly, p0, p1, p2, p3, depth = 0):    
    #dist = np.linalg.norm(p0 - p3)

    if(depth >= 3):
    #if(dist <= subdivide_limit):
        poly.append(p0)  
    
    else:
        x0 = p0[0]
        y0 = p0[1]
        
        x1 = p1[0]
        y1 = p1[1]
        
        x2 = p2[0]
        y2 = p2[1] 
        
        x3 = p3[0]
        y3 = p3[1]        
        
        """
        # http://stackoverflow.com/questions/11302937/finding-y-given-x-on-a-cubic-bezier-curve
        newX = p0[0] + (p3[0] - p0[0]) * 0.5    
        oneMinX = 1 - newX        
        newY = oneMinX**3.0 * y0 + 3.0 * oneMinX**2.0 * newX * y1 + 3.0 * oneMinX * newX**2.0 * y2 + newX**3.0 * y3        
        """
        
        splitParam = 0.5;	# split into two equal lengths
        
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
        DeCasteljau(poly, np.array([x0123,  y0123]), np.array([x123, y123]), np.array([x23, y23]),   np.array([x3, y3]), depth + 1)
        
        
def CurveToBezier(p0, p1, p2, p3, t_smooth_factor = 0.5):
    
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
    
    cp0 = np.array([xm1 + (xc2 - xm1) * t_smooth_factor + p1[0] - xm1, ym1 + (yc2 - ym1) * t_smooth_factor + p1[1] - ym1])
    cp1 = np.array([xm2 + (xc2 - xm2) * t_smooth_factor + p2[0] - xm2, ym2 + (yc2 - ym2) * t_smooth_factor + p2[1] - ym2])

    return cp0, cp1
    

if __name__ == "__main__":
    
    N = 5
    y_data = np.random.rand(N) * 10
    x_data = np.arange(0, N, 1)
    
    initial_data = []
    # combine into 2d array
    for i in range(N):
        initial_data.append(np.array([float(x_data[i]), float(y_data[i])]))
    
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
        
        DeCasteljau(interpolated_data, pt1, cp0, cp1, pt2)
        
    plt.figure(2)
    plt.clf()
    for i in interpolated_data:
        plt.plot(i[0], i[1],'o', color="magenta", markersize=7)
    for i in range(len(interpolated_data) - 1):    
        plt.plot([interpolated_data[i][0], interpolated_data[i+1][0]], [interpolated_data[i][1], interpolated_data[i+1][1]], 'k-', lw=0.5)
    for i in interpolated_data:
        plt.plot([i[0], i[0]], [0, i[1]], 'k-', lw=0.5)
    plt.show()