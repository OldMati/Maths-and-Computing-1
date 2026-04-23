# 02730341

a = 3
def ExpSeq(n):
    if n == 0:
        return 1
    return ExpSeq(n - 1) * (10 - a)

for i in range(1, 11):
    print(f'ExpSeq({i}) = {ExpSeq(i)}')