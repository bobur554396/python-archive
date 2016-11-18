import numpy as np
import copy

a = np.arange(60).reshape(3,4,5)

print a[1:2:]

c = copy.deepcopy(a)

print c

import matplotlib.pyplot as plt

x = np.arange(0., 5., 0.2)
plt.plot(x, x**4, 'r', x, x*90, 'bs', x**3, 'g^')
plt.show()