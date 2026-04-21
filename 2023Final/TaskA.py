import math
import matplotlib.pyplot as plt

def series(N):
    S = 0

    for j in range(N + 3):
        sub_sum = 0
        for k in range(2, 10 * j + 1, 2):
            sub_sum += (-1) ** j * (j ** k) / (math.factorial(k))
        S += sub_sum / math.factorial(j)
    return S


for N in [0, 2, 7, 3, 0, 3, 4, 1]:
    plt.scatter(N, series(N))

plt.show()