# CID: 02730341
import math
import matplotlib.pyplot as plt

a = 3
def Series(N):
    # define sum, set equal to 0
    S = 0
    # loop over all j
    for j in range(-N, N + 1):
        # define subSum, set to 0
        subSum = 0
        
        # loop over all k
        for k in range(-j, j):
            # skip if k is 0
            if k == 0:
                continue
            # increase subSum
            subSum += (-1) ** j * math.sin(a * k) / (k ** a)
        
        #add the subsum to S
        S += subSum / (100 - a ** 2)

    return S 

# initialize the array containing integers 1 to 20
x_s = [_ for _ in range(1, 21)]

# compute Series(X) for each x in the array above
y_s = [Series(x) for x in x_s]

# plot Series(x) against x and show the figure
plt.plot(x_s, y_s)
plt.show()

