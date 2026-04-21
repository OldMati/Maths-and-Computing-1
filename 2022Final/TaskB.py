


mat = [[] for _ in range(600)]

with open('2022Final/Matrix.txt') as f:
    count = 0
    for line in f.readlines():
        mat[count // 600].append(int(line.rstrip()))
        count += 1
        

for line in mat[:20]:
    print(line[:20])