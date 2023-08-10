import os 
import numpy as np
import statistics
from scipy.interpolate import UnivariateSpline

# NOTE: Assumes Bag object and that splines are fit to data points 

#Output: Tuple of error arrays 
def meanSquareError(spline1, spline2, total_time, time_interval, error_interval):

    timestamps_array = np.linspace(0, total_time, (total_time/time_interval))
    
    for timestamps in timestamps_array:
    
