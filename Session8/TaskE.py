import numpy as np
import pandas as pd

with open('Session8/MatA.csv', 'r') as f:
    df = pd.read_csv(f)

A = df.to_numpy()

with open('Session8/MatB.csv', 'r') as f:
    df = pd.read_csv(f)

B = df.to_numpy()

def mat_sum(mat_1, mat_2):
    return mat_1 + mat_2

D = 0.5 * (A + A.transpose()) + 0.5 * (A - A.transpose())
print(D)

def matrix_multiplication(mat_1, mat_2):
    (a, b) = mat_1.shape
    (c, d) = mat_2.shape

    if b != c:
        return False
    
    res = np.zeros((a, d))

    for i in range(a):
        for j in range(d):
            sum = 0
            for k in range(b):
                sum += mat_1[i, k] * mat_2[k, j]
            res[i, j] = sum
    
    return res

C = matrix_multiplication(A, B)
E = matrix_multiplication(B, A)

print(C - E)