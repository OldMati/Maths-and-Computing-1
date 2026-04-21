import matplotlib.pyplot as plt
import random as rn


x, y = 0, 0

y_target = 100
steps_count = 0

y_s = [0]
x_s = [0]

plt.ion()
plt.plot(y_s, y_s)
plt.ylim(-5, 110)
plt.xlim(-5, 110)
plt.draw()

while y < y_target:
    dy = int(rn.random() * 9 + 1)
    print(f'random dy: {dy}')
    dx = dy

    x_s.extend([x + dx, x + dx])
    y_s.extend([y, y + dy])
    y += dy
    x += dx
    plt.plot(x_s, y_s)
    steps_count += 1

#horizontal distance:
D = x
#steps needed to win: steps_count
input()
