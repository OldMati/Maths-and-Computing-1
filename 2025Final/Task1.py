import numpy as np
import matplotlib.pyplot as plt

CID = [0, 2, 7, 3, 0, 3, 4, 1]

# define helper function that returns the nth number in fibonacci sequence
def fibo(n, memo):
    # if already calculated fibo(n), return it
    if n in memo:
        return memo[n]
    # base case
    if n <= 1:
        return 1
    # if not already calculated nor base case, calculate recursively
    return fibo(n - 1, memo) + fibo(n - 2, memo)


# define function Diag
def Diag(n):
    # create the matrix A, fill with zeros
    A = np.zeros((n, n))

    # loop over rows in A
    for i in range(len(A)):
        # fill one diagonal with fibonacci numbers
        A[i][i] = fibo(i, {})
        # fill the other diagonal with the CID numbers
        A[i][-1 - i] = CID[i % 8]

    # return the matrix
    return A


def Series(n):
    # define the sum S as 0
    S = 0
    # create the matrix A
    A = Diag(n)

    # loop over c
    for c in range(n):
        # create the minor by removing first row and (c + 1)th column
        M_0_c = np.delete(np.delete(A, 0, axis=0), c, axis=1)

        # add the product to the sum
        S += fibo(c, {}) * np.linalg.det(M_0_c)

    # return the sum    
    return S

# define array S to store the Series(i) for all i in CID
S = []
# loop over i in CID
for i in CID:
    # compute Series(i) and append to the array
    S.append(Series(i))

# plot S against CID
plt.plot(CID, S)
plt.show()