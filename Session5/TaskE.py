import time
import matplotlib.pyplot as plt

def fibo_mem(n, mem):
    if n < 3:
        return 1
    else:
        if n in mem:
            return mem[n]
        else:
            mem[n] = fibo_mem(n - 1, mem) + fibo_mem(n - 2, mem)
            return mem[n]
    
def fibo(n):
    if n < 3:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)
    
ns = []
t_sim = []
t_mem = []

for i in range(1, 36):
    ns.append(i)

for n in ns:
    ### simple
    t_before = time.perf_counter()
    fibo(n)
    t_after = time.perf_counter()
    t = t_after - t_before
    t_sim += [t]


    ### with memorization
    t_before = time.perf_counter()
    fibo_mem(n, {})
    t_after = time.perf_counter()
    t = t_after - t_before
    t_mem += [t]

plt.plot(ns, t_sim)
plt.plot(ns, t_mem)
plt.title('Simple vs memorized fibonacci recursive function')
plt.show()





    