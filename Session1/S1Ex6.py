import matplotlib.pyplot as plt
import math
PI = math.pi


r = 0.1
Vf = 0.85
Vo = 1.6
Al = []
rl = []
hfl = []
hol = []
Wl = []

while r < 1:
    hf = Vf / (PI * r ** 2)
    ho = Vo / (PI * r ** 2)
    h = ho + hf
    #A = PI * r ** 2 * 3 + 2 * PI * r * h
    Af = 2 * PI * r ** 2 + 2 * PI * r * hf
    Ao = 2 * PI * r ** 2 + 2 * PI * r * ho
    W = Af * 0.001 * 7500 + Ao * 0.002 * 2700
    Wl += [W]
    #Al += [A]
    rl += [r]
    hfl += [hf]
    hol += [ho]
    r += 0.01

print(rl)
print(Wl)

print(f'MIN Weight: {min(Wl)}, radius: {rl[Wl.index(min(Wl))]}')
plt.plot(rl, Wl)
plt.show()
