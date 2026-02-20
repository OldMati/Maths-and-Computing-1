import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-2.0, 5.9, 0.1)

y = np.sin(x)

x = np.linspace(-2.0, 5.8, 100)
y = np.sinh(x)

a = np.arange(-5, -1.5, 0.5)
b = np.arange(-1.95, 3, 0.05)
c = np.arange(3, 5.5, 0.5)

x = np.concatenate((a, b, c))
y = np.exp(-x ** 2 / 4)

plt.plot(x, y)
plt.show()