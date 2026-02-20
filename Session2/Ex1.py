import math


noOfTeeth = [20, 24, 25, 30, 35, 36, 40, 45, 48, 50, 55, 60, 70, 80, 100]

catalogNo = []


for number in noOfTeeth:
    catalogNo += [f'GA1-{number}', f'GB1-{number}']

bores = [8, 10, 10, 12, 10, 12, 10, 12, 10, 15, 12, 15, 12, 15, 12, 15, 12, 15, 12, 15, 15, 20, 15, 20, 20, 25, 20, 25, 20, 25]
noToBores = {}

for i in range(len(bores)):
     noToBores[catalogNo[i]] = bores[i]
    
target = 15
count = 0

for i in noToBores.values():
     if i == target:
          count += 1

#print(f'There are {count} gears with bore {target}')



#P6

N = int(input('Input N: '))
primes = 0
count = 0

for i in range(2, N + 1):
    prime = True

    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            prime = False
            continue

    if prime == True:
        count += 1

print(f'Primes up to {N}: {count}')