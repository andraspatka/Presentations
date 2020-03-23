import  matplotlib.pyplot as plt
import numpy as np

import scipy

x = np.linspace(0, 2 * np.pi, 1000)

y = np.cos(x)
y2 = np.cos(2 * x)
y3 = (y + y2) / 2

plt.plot(x, y)
plt.plot(x, y2)
plt.plot(x, y3)

plt.show()