 
#defining the matrix
mat_A = [[None] * 7 for _ in range(7)]

#reading the data into the matrix
with open('2023Final/Matrix.txt') as f:
    #defining the count, starting at 0
    cnt = 0
    for el in f.readlines():
        #defining the row and column of the element
        row, column = divmod(cnt, 7)
        #updating the matrix with the new element
        mat_A[row][column] = float(el.rstrip())
        cnt += 1

#copy matrix A into C and add the new row and column
mat_C = [[-float('inf')] * 8]
for row in mat_A:
    new_row = row[:]
    new_row.insert(0, float('inf'))
    mat_C.append(new_row)

mat_C[0][0] = 0

#assigning maxes to the first row
for i in range(1, len(mat_C[0])):
    #set max to -inf
    max_in_column = mat_C[0][i]
    for j in range(1, len(mat_C)):
        # if more than max, update
        max_in_column = max(max_in_column, mat_C[j][i])
    #assign max to the first element in the column
    mat_C[0][i] = max_in_column


#assigning mins to the first column
for i in range(1, len(mat_C)):
    min_in_column = mat_C[i][0]
    for j in range(1, len(mat_C[0])):
        min_in_column = min(min_in_column, mat_C[i][j])
    mat_C[i][0] = min_in_column



############### 1) ###############
def diagonals(mat):
    #define # of rows and columns, must be equal for the input to be valid
    n = len(mat)
    m = len(mat[0])
    if n != m:
        return False
    
    #start the sums to 0
    diag_sum = 0
    antidiag_sum = 0

    for i in range(len(mat)):
        #add the element on the diagonal to the diagonal sum
        diag_sum += mat[i][i]
        
        #add the element on the antidiagonal to the other sum
        antidiag_sum += mat[n - 1 - i][i]
    
    return (diag_sum, antidiag_sum)

mat_D = [[5, 0, -2], [0, 0, 0], [-2, 0, 5]]
#print(diagonals(mat_D))


############### 2) ###############

#function to find the minor of x_i_j in a matrix A
def minor(A, i, j):
    #copy matrix A into new matrix B, except the ith row
    B = [row[::] for row in (A[:i] + A[i + 1:])]

    #remove jth element from each row
    for k in range(len(B)):
        B[k].pop(j)
    return B
        
#function to find the determinant of a given matrix A
def det(A):
    #base cases
    if len(A) == 1:
        return A[0][0]
    if len(A) == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]
    
    #recursively calculating the determinant
    total = 0
    for i in range(len(A[0])):
        total += A[0][i] * (-1) ** i * det(minor(A, 0, i))
    
    return total

#initialize the sum S of the determinants of matrices as 0
S = 0
#calculate S
for i in range(len(mat_C)):
    for j in range(len(mat_C[0])):
       S += det(minor(mat_C, i, j))

print('#################### S:', S)
#two-dimensional temp array containing the quadrants of C
'''E = [
    [[[[0] * 4 for _ in range(4)]] * 2] * 2
]
print('len(E):', len(E))
print('len(E[0]):', len(E[0]))
for row_quad in [0, 1]:
    for col_quad in [0, 1]:
        for row in E[row_quad][col_quad]:
            print(row)
        print(row_quad, col_quad)


for i in range(8):
    for j in range(8):
        quadrant = (i // 4, j // 4)
        row = i % 4
        column = j % 4'''
