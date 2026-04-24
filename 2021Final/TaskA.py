# 02730341

#cid = [0, 2, 7, 3, 0, 3, 4, 1]

cid = [0, 1, 8, 5, 6, 6, 6, 6]

# define matrices A and B
A = [[] for _ in range(8)]
B = [[] for _ in range(8)]

# filling matrix A
for i in range(8):
    A[i] = [cid[i]] + [0] * 6 + [cid[7 - i]]

# filling first and last rows of matrix B
B[0] = cid[:]
B[-1] = cid[::-1]

# filling the middle rows of matrix B
for i in range(1, 7):
    B[i] = [0 for _ in range(8)]


# create matrix D of size 8x8
D = [[0 for _ in range(8)] for _ in range(8)]

# define the matrices E = A + B and F = A - B
E = [[0 for _ in range(8)] for _ in range(8)]
F = [[0 for _ in range(8)] for _ in range(8)]

# evaluate the sum and differences of matrices
for row in range(len(A)):
    for column in range(len(A[0])):
        E[row][column] = A[row][column] + B[row][column]
        F[row][column] = A[row][column] - B[row][column]

# evaluate the product of matrices
for row in range(len(D)):
    for column in range(len(D[0])):
        for k in range(8):
            D[row][column] += E[row][k] * F[k][column]

for row in D:
    print(row)
