import os 
import math
import numpy as np
import statistics
from scipy.interpolate import UnivariateSpline

# NOTE: Assumes Bag object and that splines are fit to data points 



#Output: Tuple of error arrays, one array for each time interval specified in error_interval
#Implements: https://towardsdatascience.com/ways-to-evaluate-regression-models-77a3ff45ba70
def meanSquareError(spline1, spline2, total_time, time_step, error_interval):
    """
        error_interval - (seconds) specify how long the time interval for error analysis should be
            e.g: error_interval = 5 seconds determines mean squared error every 5 seconds
    """
    error_summary = []
    elns_in_interval = error_interval/time_step

    interval_cntr = elns_in_interval #specifies how many time array elements we need to go through for the given error interval
    interval_sum = 0
    timestamps_array = np.linspace(0, total_time, (math.floor(total_time/time_step)))

    for timestamp in timestamps_array: #Goes through each time stamp
        if(interval_cntr>=0): #Creates error intervals
            interval_sum += np.square(np.subtract(spline1(timestamp), spline2(timestamp)))
            interval_cntr -=1
        else:
            error_arr = [round(timestamp - error_interval,3)," to ",round(timestamp, 3), " seconds:", round(interval_sum/elns_in_interval, 5)]
            error_summary.append(error_arr)
            interval_sum = 0
            interval_cntr = elns_in_interval
    
    return error_summary
    



