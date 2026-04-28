import time
import matplotlib.pyplot as plt

# define iterative function
def factorial_iterative(n):
    # define result, set to 1
    res = 1

    # loop over all numbers between 2 and n, inclusive
    for num in range(2, n + 1):
        # multiply res by the number
        res *= num
    
    # return result
    return res

# define the recursive factorial function, assumes n is an integer not less than 0
def factorial_recursive(n):
    # base case, return 1 if n <= 1
    if n <= 1:
        return 1
    
    # recurse on n, return the product
    return n * factorial_recursive(n - 1)


# define array n
n = [5, 10, 20, 30, 50]

# define arrays to store the time taken by the functions to complete the tasks
time_recursive = []
time_iterative = []

# loop over all numbers in n
for num in n:
    # store the time before the function is executed
    start_iter = time.time()

    # call the function
    factorial_iterative(num)

    # store the time after the function is executed 
    end_iter = time.time()

    # compute the difference (time in seconds) and add to the array time_iterative
    diff = end_iter - start_iter
    time_iterative.append(diff)

    # repeat for the recursive functionstart_iter = time.time()
    start_iter = time.time()
    factorial_recursive(num)
    end_iter = time.time()
    diff = end_iter - start_iter
    time_recursive.append(diff)

# plot the results, iterative in red and recursive in blue
plt.title('Computational time of a recursive and an iterative function \nagainst input number for fibonacci sequence')
plt.plot(n, time_iterative, c='r')
plt.plot(n, time_recursive, c='b')
plt.ylabel('Time (S)')
plt.xlabel('Input number')
plt.show()