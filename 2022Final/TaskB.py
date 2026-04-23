# CID: 02730341

import numpy as np
import matplotlib.pyplot as plt

# load the file into the matrix of size 600 x 600
A = np.loadtxt('2022Final/Matrix.txt', dtype=float).reshape(600, 600)

# initialize the AV and Det matrices
AV = np.zeros((60, 60))
Det = np.zeros((60, 60))

# loop over all i and j, where A[i, j] is the top-left
# entry of the 10 x 10 sub-matrix
for i in range(0, 600, 10):
    for j in range(0, 600, 10):
        # define the corresponding coordinates for the AV and Det matrices
        i_p, j_p = i // 10, j // 10

        # store the submatrix starting at [i, j]
        subMatrix = A[i:i + 10, j:j + 10]

        # set the Average of the corresponding entry in AV as the 
        # sum of the submatrix divided by 100
        AV[i_p, j_p] = subMatrix.sum() / 100

        # set Det(i_p, j_p) as the determinant of the submatrix
        Det[i_p, j_p] = np.linalg.det(subMatrix)

        if Det[i_p, j_p] != 0:
            # substitute the original submatrix with its transpose:
            A[i:i + 10, j:j + 10] = subMatrix.T


# save matrix AV into Averages.txt
with open('2022Final/Averages.txt', 'w') as f:
    # resize AV into a temporary matrix AV_temp with 3600 rows and 1 column
    AV_temp = AV.reshape(3600, 1)
    # iterate over all rows in AV_temp and write the first (only) element into the file
    for entry in AV_temp:
        f.write(str(entry[0]) + '\n')


# save matrix Det into Determinants.txt
with open('2022Final/Determinants.txt', 'w') as f:
    # resize Det_temp into a temporary matrix Det_temp with 3600 rows and 1 column
    Det_temp = Det.reshape(3600, 1)
    # iterate over all rows in Det_temp and write the first (only) element into the file
    for entry in Det_temp:
        f.write(str(entry[0].round()) + '\n')


plt.imshow(A)
plt.show()

