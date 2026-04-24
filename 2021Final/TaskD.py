# 02730341

import math
import matplotlib.pyplot as plt

def Series(N):
    a = 3
    P = 0

    for i in range(1, N + 1):
        subSum = 0
        for k in range(1, i + 1):
            subSum += (a + 10) ** (k - 3)
        
        P += subSum / math.factorial(i - 1)
    
    return P

P_s = []
N_s = [_ for _ in range(1, 51)]

for N in N_s:
    P_s.append(Series(N))

plt.plot(N_s, P_s)
plt.show()