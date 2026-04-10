
# TASK A
def minor(A, i, j):
    B = [row[::] for row in (A[:i] + A[i + 1:])]
    for k in range(len(B)):
        B[k].pop(j)
    return B
        

def det(A):
    #print('DET: ', A, len(A))
    if len(A) == 1:
        return A[0][0]
    if len(A) == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]
    
    total = 0
    for i in range(len(A[0])):
        total += A[0][i] * (-1) ** i * det(minor(A, 0, i))
    
    return total

# TASK B

def adj(A):
    B = [[None for element in row] for row in A]
    #print('ADJ: ', B)
    for i in range(len(B)):
        for j in range(len(B[0])):
            B[j][i] = det(minor(A, i, j)) * (-1) ** (i + j)
    return B

def inv(A):
    B = adj(A)
    det_A = det(A)
    if det_A == 0:
        return None
    for i in range(len(A)):
        for j in range(len(A[0])):
            B[i][j] /= det_A
    return B
    
# TASK C

def multiply_matrices(A, B):
    a, b = len(A), len(A[0])
    c, d = len(B), len(B[0])
    if b != c:
        return False
    
    C = [[0 for _ in range(d)] for _ in range(a)]
    
    for i in range(a):
        for j in range(d):
            for k in range(b):
                C[i][j] += A[i][k] * B[k][j]
    
    return C

def solve_sys_lin_eq(A, b):
    A_inv = inv(A)
    if A_inv is None:
        return 'No unique solution'
    return multiply_matrices(A_inv, b)


#TASK D

def gauss_elimination(A, b):
    A = [row[:] for row in A]
    b = b[:]

    for i in range(len(A) - 1):
        for j in range(i + 1, len(A)):
            pivot = -A[j][i] / A[i][i]
            for k in range(i, len(A)):
                A[j][k] += A[i][k] * pivot
            b[j] += b[i] * pivot

    x = [None for _ in range(len(A))]
    for i in range(len(A) - 1, -1, -1):
        for j in range(i + 1, len(A)):
            b[i] -= x[j] * A[i][j]
        x[i] = b[i] / A[i][i]

    return x
    

A = [[1, 1], [1, 1]] ## det == 0
B = [[1, 2], [3, 4]] ## det == -2

C = [[1, 2, 3], [4, 5, 3], [1, 2, 1]] ## det == 6
b = [0, 1, 2]

D = [[8, -2, 1, 3], [1, -5, 2, 1], [-1, 2, 7, 2], [2, -1, 3, 8]]
e = [9, -7, -1, 5]
print(gauss_elimination(D, e))

