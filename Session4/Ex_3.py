import matplotlib.pyplot as plt
import numpy as np
import math as mt

fig, ax = plt.subplots()

def Signals(T, Vpp, VDC, Stype):
    t = np.linspace(0, 4 * T, 400)
    Vrpp = Vpp / 2

    if Stype == 1:
        V = VDC + np.sin(t * 2 * mt.pi / T) * Vrpp
    elif Stype == 2:
        V = VDC - Vrpp + Vpp * np.where(t % T < T / 2, 0, 1)
    elif Stype == 3:
        V = VDC + Vpp / T * (t % T)
    elif Stype == 4:
        V = VDC - Vrpp + 4 * Vpp / T * (t % T / 2) * np.where(t % T < T / 2, 1, -1) + 2 * Vpp * np.where(t % T < T / 2, 0, 1)

    ax.plot(t, V)
    ax.set_title('Voltage against time')
    ax.set_xlabel('Time')
    ax.set_ylabel('Voltage')
    ax.set_ylim(0, 12)
    plt.show()

Signals(10, 4, 9, 4)
    
