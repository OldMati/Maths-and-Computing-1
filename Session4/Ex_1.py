import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

def CombineRes(resistors, bool):
    totalResistance = 0
    if bool:
        for r in resistors:
            totalResistance += r
        return totalResistance
    else:
        for r in resistors:
            totalResistance += 1 / r
        return 1 / totalResistance
    
    
res = [150, 200, 350, 400, 550]

print('R Total: ', CombineRes(res, False))

VoltageDivider = lambda E, R1, R2: E * R2 / (R1 + R2)


## task 2

def OpPoint(ES, RS, EL, RL):

    i = np.linspace(-1, 10, 100)
    VS = ES - i * RS
    VL = EL - i * RL

    ax.plot(i, VS, label='Source')
    ax.plot(i, VL, label='Load')
    ax.legend()
    plt.show()

def OpPoint2(ES, RS, EL, RL):
    """
    Plots the Thevenin lines for a source (ES, RS)
    and a load (EL, RL), and shows their operating point.

    ES, RS = Thevenin voltage and resistance of the source
    EL, RL = Thevenin voltage and resistance of the load
    """

    # Source Thevenin line:  V = ES - RS * I
    IS_max = ES / RS                   # short-circuit current of the source
    I_S = np.linspace(0, IS_max, 200)
    V_S = ES - RS * I_S

    # Load Thevenin line:  V = EL - RL * I
    IL_max = EL / RL                   # short-circuit current of the load
    I_L = np.linspace(0, IL_max, 200)
    V_L = EL - RL * I_L

    # --- Compute intersection (operating point) ---
    # Solve:
    #   ES - RS*I = EL - RL*I
    # → I*(RS - RL) = ES - EL
    if RS == RL:
        I_op = None   # parallel or coincident lines
    else:
        I_op = (ES - EL) / (RS - RL)
        V_op = ES - RS * I_op

    # --- Plot ---
    fig, ax = plt.subplots()

    ax.plot(I_S, V_S, label="Source Thevenin line")
    ax.plot(I_L, V_L, label="Load Thevenin line")

    # Plot operating point if valid
    if I_op is not None and I_op >= 0:
        ax.plot(V_op, I_op, 'ro', label=f"Operating point\nV={V_op:.2f}, I={I_op:.2f}")

    ax.set_ylabel("Voltage V  [V]")
    ax.set_xlabel("Current I  [A]")
    ax.set_title("Thevenin Source–Load Operating Point")
    ax.grid(True)
    ax.legend()

    plt.show()

OpPoint(10, 10, -15, 1)



