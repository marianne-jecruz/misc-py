import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline

from msqe import *

# rng = np.random.default_rng()
# x = np.linspace(-3, 3, 50)
# y = np.exp(-x**2) + 0.1 * rng.standard_normal(50)
# plt.plot(x, y, 'ro', ms=5)

def func(x, a, b, c):
    return a * np.exp(-b * x) + c

xdata = np.linspace(0, 4, 50)
y = func(xdata, 2.5, 1.3, 0.5)
rng = np.random.default_rng()
y0_noise = 0.2 * rng.normal(size=xdata.size)
y1_noise = rng.normal(size=xdata.size)
ydata0 = y + y0_noise
ydata1 = y + y1_noise
plt.plot(xdata, ydata0, 'b-', label='data')
plt.plot(xdata, ydata1, 'g', label='data')

y0_spl = UnivariateSpline(xdata, ydata0)
y1_spl = UnivariateSpline(xdata, ydata1)

#plt.show()