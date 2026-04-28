import matplotlib.pyplot as plt
import numpy as np
import random as rn


# plot the square on the figure
square_x = [-3, 3, 3, -3, -3]
square_y = [-3, -3, 3, 3, -3]
plt.plot(square_x, square_y, c='black')

# plot the circle
circle_t = np.arange(0, 2*np.pi + 1, 0.1)
circle_x = np.cos(circle_t)
circle_y = np.sin(circle_t)
plt.plot(circle_x, circle_y, c='black')


# define the initial coordinates of the ant
x, y = 3, 3

# loop while it is outside the circle
while x ** 2 + y ** 2 > 1:
    # define dx and dy
    dx = rn.random() * 0.4 - 0.2
    dy = rn.random() * 0.4 - 0.2

    # store the previous position
    x_prev = x
    y_prev = y

    # move the ant by dx and dy
    x = x + dx
    y = y + dy

    # plot the step
    plt.plot([x_prev, x], [y_prev, y], c='b')

    # bounce back if it left the square
    if abs(x) > 3 or abs(y) > 3:
        # return to previous coordinates, no need for plotting
        x = x_prev
        y = y_prev

plt.show()
