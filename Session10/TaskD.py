import random as rn
import matplotlib.pyplot as plt
import math

sqrt_2 = math.sqrt(2)
n = 0
N = 10 #define N
triangle = [[0, 1, 0, 0], [0, 0, 1, 0]]
points = [[],[]]
while n < N:
    x, y = rn.random(), rn.random()
    #y < 1 - x
    if x + y < 1:
        points[0].append(x)
        points[1].append(y)
        n += 1

plt.xlim(-0.2, 1.2)
plt.ylim(-0.2, 1.2)
plt.ion()

sc = plt.scatter(points[0], points[1])
plt.plot(triangle[0], triangle[1])

dt = (0.01)
print(points)
plt.pause(dt)

for _ in range(1000):
    for i in range(len(points[0])):
        step = (rn.random() - 0.5) / 50 / sqrt_2

        x_new = points[0][i] + step
        y_new = points[1][i] + step
        if x_new + y_new < 1 and x_new >= 0 and y_new >= 0:
            points[0][i] = x_new
            points[1][i] = y_new


    sc.set_offsets([(points[0][i], points[1][i]) for i in range(len(points[0]))])
    plt.draw()
    plt.pause(dt)

