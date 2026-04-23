# 02730341

import numpy as np
import matplotlib.pyplot as pl

x = np.arange(-2*np.pi,2*np.pi,0.01)
y = np.sin(x)
xm = np.arange(-2*np.pi, -1*np.pi, 0.01) + (np.arange(np.pi, 2*np.pi, 0.01))
ym = np.sin(xm)
pl.scatter(x,y,Linewidth=10,c='b')
pl.scatter(xm,ym,Linewidth=1,c='r')
pl.grid()
pl.legend(['y','ym'])