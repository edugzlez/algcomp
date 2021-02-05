import numpy as np

"""
    Encontrar el periodo de una función
"""
def find_period(a, p):
    a_ = mod_inverse(a, p)
    return discrete_logarithm(a, a_, p)+1

"""
    Algoritmo de Shor
"""
def shor(n):
    while True:
        a = int(np.random.choice(range(2, n-1)))
        f0 = gcd(a, n)
        if f0 != 1:
            return (f0, n//f0)
        else:
            r = find_period(a, n)
            if r % 2 == 0 and pow(a, r//2, n) != -1:
                x = pow(a, r//2)
                f1 = gcd(x+1, n)
                f2 = gcd(x-1, n)
                return (f1, f2)