
marks = []
with open('Session3/Marks.txt', 'r') as f:
    for mark in f.readlines():
        marks += [int(mark.rstrip())]

print(marks)
sum = 0
for mark in marks:
    sum += mark

avg = sum / len(marks)
print(f'Sum: {sum}, avg: {avg:.3f}')