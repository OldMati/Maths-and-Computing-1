

def GCD(a, b):

    # a > b
    if b > a:
        a, b = b, a

    r = a % b

    if r == 0:
        return b
    else:
        return GCD(b, r)


def LCM(a, b):
    return abs(a * b) / GCD(a, b)

def AddFractions(N, D):
    Nt = 0
    Dt = 1
    for n in range(len(N)):
        Dt *= D[n]

    for n in range(len(N)):
        Nt += N[n] * Dt // D[n]
    #check if have common divisor:

    r = GCD(Nt, Dt)

    if r != 1:
        Dt = Dt // r
        Nt = Nt // r

    return Nt, Dt