import numpy as np

def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a

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

def find_coprime(n):
    for j in range(n//2+2, n):
        if gcd(j, n) == 1:
            yield j

def cifrate_num(number, key):
    n, e = key
    return pow(number, e, n)

def cifrate_text(text, key):
    return "".join(map(lambda char: chr(cifrate_num(ord(char), key)), text))

class RSA:
    def __init__(self, p, q):
        self.p = p
        self.q = q

        self.n = p*q

        phi_n = (p-1)*(q-1)

        self.e = int(np.random.choice(list(find_coprime(phi_n))))
        self.d = mod_inverse(self.e,phi_n)

    def public_key(self):
        return (self.n, self.e)

    def private_key(self):
        return (self.n, self.d)

my_rsa = RSA(61, 53)