import time
from tracemalloc import start


def fib_rec(n):
    if n < 2:
        return n
    else:
        return fib_rec(n-1) + fib_rec(n-2)


def fib_it(n):
    res = n
    a, b = 0, 1
    for k in range(2, n+1):
        res = a + b
        a, b = b, res
    return res



# Teste Tempo de execucao

n = 11
start = time.time()
print(fib_rec(n))
print('Recursive: {} segundos '.format(time.time() - start))
start = time.time()
print(fib_it(n))
print('Iterative: {} segundos '.format(time.time() - start)) 
