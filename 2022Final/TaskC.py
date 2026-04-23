# CID: 02730341

import matplotlib.pyplot as plt
import random as rn
import numpy as np
import math


# helper function that returns if the ant hits or crosses an obstacle
def hits_an_obstacle(x, y):
    #check if it hits the low wall
    if y < 0:
        return True

    # check if hits the first circle
    if (x + 2) ** 2 + (y - 1) ** 2 <= 0.4 ** 2:
        return True
    
    # check if hits the second circle
    if (x + 1) ** 2 + (y - 2) ** 2 <= 0.4 ** 2:
        return True
    
    # check if outside of the upper and lower lines:
    if not (y - x < 4 and y - x > 2):
        return True
    
    # doesnt hit an obstacle
    return False
    

# initialize the x and y lists
x = [-3]
y = [0]

# initialize the counter of steps
count = 0

# define the obstacles for plotting
# upper: y = x + 4; upper = [x[], y[]]
upper_line = [[-4, 0], [0, 4]]
# lower: y = x + 2; lower = [x[], y[]]
lower_line = [[-2, 0], [0, 2]]

# circles:

# parameter values from 0 to 2π
t = np.linspace(0, 2*np.pi, 500)
# Circle 1: centre (-2, 1), radius 0.4
x1 = -2 + 0.4 * np.cos(t)
y1 =  1 + 0.4 * np.sin(t)

# Circle 2: centre (-1, 2), radius 0.4
x2 = -1 + 0.4 * np.cos(t)
y2 =  2 + 0.4 * np.sin(t)

# set up the figure
plt.ion()
plt.plot(x1, y1)
plt.plot(x2, y2)
plt.plot(upper_line[0], upper_line[1])
plt.plot(lower_line[0], lower_line[1])
plt.xlim(-4, 1)
plt.ylim(-1, 5)
plt.draw()

while count < 1000:
    # increase the counter by 1
    count += 1

    # set dx and dy as random values between -0.3 and 0.3
    dx = (rn.random() - 0.5) * 0.6
    dy = (rn.random() - 0.5) * 0.6

    # define the curreny x and y
    x_cur = x[-1] + dx
    y_cur = y[-1] + dy
    
    # add the current position to the x and y arrays
    x.append(x_cur)
    y.append(y_cur)

    # check if it hits an obstacle:
    if hits_an_obstacle(x_cur, y_cur):
        # bounce it back to the last position
        x.append(x[-2])
        y.append(y[-2])
    
    # plot the current position of the ant
    plt.plot(x, y)

    # check if it escaped through the exit:
    if x[-1] > 0:
        print('The ant escaped')
        break
    

# the ant has done 1000 steps and is exhausted
if count == 1000:
    print('The ant is exhausted.')
input()