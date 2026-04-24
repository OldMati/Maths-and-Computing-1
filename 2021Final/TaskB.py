# 02730341

import matplotlib.pyplot as plt
import math
import random as rn

sigma = 0.1 + 3 / 20

def f(x):
    return math.exp(-1 * (x - 0.5) ** 2 / (sigma ** 2))

N = 10000
plt.xlim(0, 1)
plt.ylim(0, 1)

outside = 0
inside = 0

for _ in range(N):
    x = rn.random()
    y = rn.random()

    if y > f(x):
        plt.scatter(x, y, c='blue', s=1)
        outside += 1
    else:
        plt.scatter(x, y, c='red', s=1)
        inside += 1

plt.show()
ratio = inside / outside
print('The ratio of the two areas is: ', ratio)