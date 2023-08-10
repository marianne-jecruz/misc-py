import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline

rng = np.random.default_rng()
x = np.linspace(-3, 3, 50)
y = np.exp(-x**2) + 0.1 * rng.standard_normal(50)
plt.plot(x, y, 'ro', ms=5)