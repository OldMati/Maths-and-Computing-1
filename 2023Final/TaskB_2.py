import numpy as np

mat = np.loadtxt('2023Final/Matrix.txt', dtype=float).reshape(7, 7)

C = np.zeros((8, 8))
C[1:, 1:] = mat


for column in range(1, 8):
    C[0, column] = max(C[1:, column])

for row in range(1, 8):
    C[row, 0] = min(C[row, 1:])

def Diagonals(mat):
    diag_sum = 0
    antidiag_sum = 0
    n = len(mat)
    for i in range(n):
        diag_sum += mat[i, i]
        antidiag_sum += mat[i, n - 1 - i]
    
    return (diag_sum, antidiag_sum)

S = 0

for r in range(8):
    for c in range(8):
        minor = np.delete(np.delete(C, r, axis=0), c, axis=1)
        S += np.linalg.det(minor)

print(S)



D = np.zeros((8, 8))

D[:4,:4] = C[:4,:4].T
D[4:,:4] = C[4:,:4].T
D[:4,4:] = C[:4,4:].T
D[4:,4:] = C[4:,4:].T

print(C)

print(D)