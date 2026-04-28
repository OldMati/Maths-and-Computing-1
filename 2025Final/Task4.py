import matplotlib.pyplot as plt
import numpy as np

# define the class
class Force():
    
    # define the constructor
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    # define the resultant function
    def Resultant(self, force):
        # create the result Force object
        result = Force()

        # add the x and y components to the resultant force
        result.x = self.x + force.x
        result.y = self.y + force.y

        # return the resultant force
        return result

# define the array t from 0 to 2 pi
t = np.arange(0, 2 * np.pi, 0.1)

# define the forces F1 and F2
F1 = Force()
F2 = Force()

# define the array to store the x and y components of all the forces, for plotting
F1_x = []
F1_y = []
F2_x = []
F2_y = []
Res_x = []
Res_y = []

# loop over t
for time in t:

    # set the x and y components of the forces F1 and F2
    F1.x = 5 * np.sin(time) + 5
    F1.y = 2 * np.cos(time) + 5

    F2.x = 4 * np.cos(time) - 3
    F2.y = 8 * np.sin(time) - 3

    # calculate the resultant force
    Res = F1.Resultant(F1)

    # store the components in the arrays
    F1_x.append(F1.x)
    F1_y.append(F1.y)
    
    F2_x.append(F2.x)
    F2_y.append(F2.y)

    Res_x.append(Res.x)
    Res_y.append(Res.y)

#plot the loci
plt.plot(F1_x, F1_y, c='b')
plt.plot(F2_x, F2_y, c='r')
plt.plot(Res_x, Res_y, c='g')

plt.show()

