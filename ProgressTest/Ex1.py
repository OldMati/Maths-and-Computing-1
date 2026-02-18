import numpy as np

sum = 0
for i in range(0, 1052):
    if i % 2 == 1 and (i < 500 or i > 600):
        sum += i

print('sum: ', sum)

a = {'a':'A'}
b = {'b':'B'}
a = [b,a]

#print(a, type(a))

count = 0

a = False
b = 10
c = 200
while not a and b <= c:
    count += 1
    b = b + 3

print('count: ', count)
