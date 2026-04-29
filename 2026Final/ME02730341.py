import pandas as pd
import time
import numpy as np
import matplotlib.pyplot as plt
import random as rn


##################### TASK 1 #####################

def MatMat(A, B):
    # store the size of the matrices
    M = len(A)
    N = len(A[0])

    # create the matrix C
    C = np.zeros((M, 1))

    # loop over all i
    for i in range(M):

        # loop over all k
        for k in range(N):
            # update C[i]
            C[i] += A[i][k] * B[i][k]
    
    # return the matrix C
    return C
    
A = [[1, 0, -1], [0, 1, -2], [2, 1, 1]]
B = [[-1, 0, 1], [0, 1, 2], [2, 1, 2]]

C = MatMat(A, B)

print('The transpose of the matrix C: ', C.T)



##################### TASK 2 #####################


# read the data into a data frame
df = pd.read_csv("2026Final/Financial.csv")

# create a new column and convert from GBp to USD
df['LSE (USD)'] = df['LSE (GBp)'] * 1.35 / 100

# calculate the averages by taking the total sum and dividing by the number of entries
avg_LSE = df['LSE (USD)'].sum() / len(df['LSE (USD)'])
avg_NYSE = df['NYSE (USD)'].sum() / len(df['NYSE (USD)'])

# print out the averages
print('Average prices of LSE and NYSE: ', avg_LSE, avg_NYSE)


# rename the first column
new_col = ['ID']
new_col.extend(df.columns[1:])
df.columns = new_col

# define subplots (to also plot graphs for the other tasks)
fig, ax = plt.subplots(2, 2)

# plot the markets
ax[0][0].plot(df['Date'], df['LSE (USD)'], c='b')
ax[0][0].plot(df['Date'], df['NYSE (USD)'], c='r')

# store the number of rows
no_of_entries = len(df)

# plot the averages
ax[0][0].plot(df['Date'], [avg_LSE for _ in range(no_of_entries)], c='gray')
ax[0][0].plot(df['Date'], [avg_NYSE for _ in range(no_of_entries)], c='black')

#plt.show()

# count the number of days where LSE has higher price than NYSE
count = df[df['LSE (USD)'] > df['NYSE (USD)']]['ID'].count()
print('the number of days where LSE has higher price than NYSE: ', count)


##################### TASK 3 #####################

def Func1(N):
    for i in range(N):
        for j in range(N):
            a = 1
    return

def Func2(N):
    for i in range(N):
        a = 1
    return
    
def Func3(N):
    for i in range(N):
        for j in range(N//2):
            a = 1
    return

# create a Funcs array storing the functions
Funcs = [Func1, Func2, Func3]

# create a 2D array storing the computational costs of the functions,
# where F_time[0] refers to Func1 etc
F_time = [[] for _ in range(3)]

# create the array N
N = [10 ** i for i in [1, 2, 3, 4]]

# loop over all n in N
for n in N:
    # loop over all functions
    for i in range(3):

        # store the start time
        start = time.perf_counter()

        # call the function
        Funcs[i](n)

        # store the end time
        end = time.perf_counter()

        # calculate the time difference and add to the array storing the computational times
        t = end - start
        F_time[i].append(t)

ax[0][1].plot(N, F_time[0], c='b')     # plot the first func in blue
ax[0][1].plot(N, F_time[1], c='r')     # the second in red
ax[0][1].plot(N, F_time[2], c='g')     # the third in green

#plt.show()


##################### TASK 4 #####################

# define N
N = 10

# plot the square
square_x = [0, 100, 100, 0, 0]
square_y = [0, 0, 100, 100, 0]

ax[1][1].plot(square_x, square_y, c='r')

# define t from 0 to 2 pi
t = np.arange(0, 2 * np.pi + 0.1, 0.1)

# loop N times
for n in range(N):  
    # define random x and y, centres of the circle, inside the square
    x = rn.random() * 100
    y = rn.random() * 100

    # find the max radius
    max_x = min(100 - x, x)
    max_y = min(100 - y, y)
    max_radius = min(max_x, max_y)

    # calculate the x and y coordinates of the points and store them
    y_arr = y + np.sin(t) * max_radius
    x_arr = x + np.cos(t) * max_radius

    # plot the circle
    ax[1][1].plot(x_arr, y_arr, c='b')

##################### TASK 5 #####################

def Cantor(N, a, b):
    # base case, return if no more segments to draw
    if N == 0:
        return

    # define the length of the line
    length = b - a

    # plot the line
    x = [a, b]
    y = [N, N]
    ax[1][0].plot(x, y, c='b')

    # recurse left side
    Cantor(N - 1, a, a + length / 3)

    # recurse right side
    Cantor(N - 1, b - length / 3, b)


Cantor(4, 8, 12)


plt.show()


##################### TASK 6 #####################
    

class Complex:
    def __init__(self, a=0, b=0):
        self.re = a
        self.im = b

    def Amplitude(self):
        return np.sqrt(self.re ** 2 + self.im ** 2)

z1 = Complex(3, 5)
z2 = Complex(3, -5)

print('Amplitudes of z1 and z2: ', z1.Amplitude(), z2.Amplitude())