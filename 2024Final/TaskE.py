# 02730341

import matplotlib.pyplot as plt
import random as rn
import math

# define target y and room width
y_target = 50
room_width = 5

# define the x and y arrays of the room
room_x = [0, 0, room_width, room_width]
room_y = [y_target, 0, 0, y_target]

# plot the room
plt.plot(room_x, room_y, c='b')

# set the limits of the x and y axis
plt.xlim(-5, 10)
plt.ylim(-10, 60)

# turn on the gridlines
plt.grid()

# define theta
theta = float(input('Theta: '))

# initiate arrays x and y
x, y = rn.random() * 5, 0

# initiate the count of the bounces
count = 0

# define the step dy
dy = 1 * math.sin(theta)
dx = 1 * math.cos(theta)

# define direction (1 or -1)
direction = 1

# loop while the ball has not escaped the room
while y < y_target:

    # save the previous coordinates
    y_prev = y
    x_prev = x

    # increment x
    x += dx * direction

    # what fraction of the step the ball moves
    fraction_of_step = 1

    # if ball went through the wall
    if x >= 5 or x <= 0:

        #update counter
        count += 1

        # reverse direction
        direction *= -1

        # check which side it escaped, find what fraction of the step it can do,
        # update x
        if x >= 5:
            fraction_of_step = (5 - x_prev) / dx
            x = 5
        else:
            fraction_of_step = (x_prev) / dx
            x = 0
        
    # increment y with the fraction of the step
    y += dy * fraction_of_step

    plt.plot([x_prev, x], [y_prev, y], c='black')


print('The number of bounces: ', count)
plt.show()


