import numpy as np

def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a

def shor(n):
    while True:
        a = int(np.random.choice(range(2, n-1)))
        f0 = gcd(a, n)
        if f0 != 1:
            return f0
        else:
            r = find_period(a, n)
            if r % 2 == 0 and pow(a, r//2, n) != -1:
                x = pow(a, r//2, n)
                f1 = gcd(x+1, n)
                f2 = gcd(x-1, n)
                return f1 if f1%n == 0 else f2

def extended_euclides(a: int, b: int):
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        (q, a), b = divmod(b, a), a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return x0, y0, b 
    
def mod_inverse(n, p):
    s, t, r = extended_euclides(n, p)
    return s % p

def discrete_logarithm(alpha, beta, p): # alpha ^ x = beta (mod p)
    m = int(np.ceil(p**0.5))

    table = {0: 1}
    for j in range(1, m):
        table[j] = (table[j-1]*alpha) % p

    alpha_m = pow(alpha, -m, p)
    y = beta

    for i in range(m):
        j = next(filter(lambda tup: tup[1] == y, zip(table.keys(), table.values())), (None, None))[0]
        if j is not None:
            return i*m+j
        else:
            y = y*alpha_m % p

    return None


def find_period(a, p):
    a_ = mod_inverse(a, p)
    return discrete_logarithm(a, a_, p)+1