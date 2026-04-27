# 02730341

import matplotlib.pyplot as plt



def Squares(n, L):
    # define the arrays x and y containing the x and y 
    # coordinates of the points of the square
    x = [0, 0, L, L, 0]
    y = [0, L, L, 0, 0]

    # define the color to red if there is at least one more rectangle to draw,
    # blue otherwise
    color = 'r' if n > 1 else 'b'

    # plot the squre
    plt.plot(x, y, c=color)

    # return if this was the last square to draw, else recurse
    if n == 1:
        return
    else:
        Squares(n - 1, L / 1.1)

    # show the figure
    plt.show()

