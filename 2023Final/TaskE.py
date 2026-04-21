import math
import matplotlib.pyplot as plt
import numpy as np

class Trigonometry():
    def __init__(self, x, unit):
        
        # sequence of numbers
        self.x = x
        #True if x in radians, False otherwise
        self.unit = unit

    def cos(self):
        result = []
        radian = self.unit
        for angle in self.x:
            if not radian:
                angle = math.radians(angle)
            result.append(math.cos(angle))
        self.cosines = result
        return result

PI = math.pi
print("PI::", PI)
d_ang = PI * 2 / 100
xr = Trigonometry(x=np.arange(0, 2 * PI + d_ang, d_ang), unit=True)

xd = Trigonometry(x=np.arange(0, 361, 3.6), unit=False)

xr.cos()
xd.cos()

fig, ax = plt.subplots(2, 1)


ax[0].plot(xr.x, xr.cosines)
ax[1].plot(xd.x, xd.cosines)
plt.show()
input()
