# 02730341

import matplotlib.pyplot as plt
import math

#define the function, set a to 3 (4th digit of my CID)
a = 3
def Series(N):
    #initialize the sum S to 0
    S = 0
    #loop over all j
    for j in range(-N, N + 1):
        #initialize subSum to 0
        subSum = 0

        #loop over k
        for k in range(-j, j):
            #skip if k == 0
            if k == 0:
                continue
            #add to subsum
            subSum += (-1) ** j * math.sin(a*k) / (k ** a)

        subSum /= (100 - a ** 2)
        #add subsum to S
        S += subSum
    
    return S

#initialize arrays x and y
x = []
y = []

#loop over N, add N and Series(N) to x and y
for N in range(1, 21):
    x.append(N)
    y.append(Series(N))

#plot y against x
plt.scatter(x=x, y=y)
plt.xlim(0, 21)
plt.show()