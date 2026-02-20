import matplotlib.pyplot as plt
import math

PI = math.pi

V = 1.5
r = 0.1
rl, hl, Vl, Al = [], [], [], []

while r <= 1.5:
    v = 0
    h = 2 * r - 0.05
    while v < V:
        h += 0.05
        v = PI * r ** 2 * (h - 2 * r) + 4 / 3 * PI * r ** 3

    A = 2 * PI * r * (h - 2 * r) + 4 * PI * r ** 2
    Al += [A]
    Vl += [V]
    hl += [h]
    rl += [r]
    r += 0.05

#print(A1)
print(f'Min area: {min(Al)}, index: {Al.index(min(Al))}')
print(f'Min height: {min(hl)}, index: {hl.index(min(hl))}')
print(f'Min radius: {min(rl)}, index: {rl.index(min(rl))}')

plt.plot(rl, Al)
plt.xlabel('Radius, m')
plt.ylabel('Surface area, m^2')
plt.title('Surface area vs radius')
plt.show()