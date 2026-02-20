import numpy as np


def diagonal(mat):
    sum = 0
    for i in range(len(mat)):
        sum += mat[i, i]
    
    return sum

def transpose(mat):
    (a, b) = mat.shape
    res = np.zeros((b, a))
    for x in range(a):
        for y in range(b):
            res[y, x] = mat[x, y]

    return res

mat = np.zeros((5, 5))

for i in range(len(mat)):
    for j in range(len(mat[0])):
        if i == j or i == 4 - j:
            mat[i,j] = 1
        
print(mat)



R = np.random.randint(1, 100, size=(10, 5))

print(R)
R = transpose(R)
print(R)


