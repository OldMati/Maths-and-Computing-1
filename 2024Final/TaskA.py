# 02730341

import numpy as np

# define funciton
def MakeMatrix(n):
    # initiate the matrix A
    A = np.zeros((n, n))

    # loop over all columns
    for i in range(n):
        # fill the diagonals with the column number
        A[i, i] = i + 1
        A[n - 1 - i, i] = i + 1

    return A

def Series(N):
    # initiate the sum as 0
    S = 0

    # loop over all n
    for n in range(2, N + 1):
        # create matrix A_n
        A = MakeMatrix(n)
        print(A)
        # update the sum by adding the determinant of A_n
        S += np.linalg.det(A)
    
    return S

cid = [0, 2, 7, 3, 0, 3, 4, 1]

for i in cid:
    print(f'Series({i}) = {Series(i)}')