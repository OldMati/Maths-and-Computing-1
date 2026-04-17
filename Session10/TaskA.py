import matplotlib.pyplot as plt

data = []
with open('Session10/Data.csv', 'r') as f:
    for line in f.readlines()[1:]:
        temp_data = line.rstrip().split(',')
        data.append((temp_data[0], temp_data[1], temp_data[2]))


data = sorted(data, key= lambda x: x[2], reverse=True)
print(data)

occurences = [(data[0][2], 1, [data[0][0]])]
print(f'OCCURENCES: {occurences}')

for line in data[1:]: 
    print(f'OCCURENCES: {occurences} for {line}')
    if occurences[-1][0] == line[2]:
        old_tuple = occurences[-1]
        old_tuple[2].append(line[0])
        new_tuple = (old_tuple[0], old_tuple[1] + 1, old_tuple[2])
        occurences[-1] = new_tuple
    else:
        occurences.append((line[2], 1, [line[0]]))

for occ in occurences:
    print(occ[0], occ[1])

x = [line[0] for line in occurences[::-1]]
y = [line[1] for line in occurences[::-1]]

plt.plot(x, y)
plt.title('Occurences vs marks')
plt.xlabel('Marks')
plt.ylabel('Occurences')
plt.xticks(range(0, 105, 5))
plt.show()
