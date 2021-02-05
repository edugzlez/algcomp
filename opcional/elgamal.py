import numpy as np

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

class ElGamal:

    def __init__(self, p, g = None, a = None):

        if g is None:
            g = np.random.randint(1, p)
        
        if a is None:
            a = np.random.randint(1, p)

        self.p = p
        self.g = g
        self.a = a

        self.K = pow(g, a, p)


    def public_key(self):
        return (self.g, self.p, self.K)

    def private_key(self):
        return (self.a, self.p)


def cifrate_num(m, key, b = None):
    g, p, K = key
    if b is None:
        b = np.random.randint(2, p)
    
    y_1 = pow(g, b, p)
    
    return (pow(g, b, p), pow(K, b, p)*m % p)

def cifrate_text(text, key):
    return list(map(lambda char: cifrate_num(ord(char), key), text))

def uncifrate_num(y_tuple, key):
    a, p = key
    y1, y2 = y_tuple

    return pow(y1, p-1-a, p)*y2 % p

def uncifrate(list_tuples, key):
    return "".join(map(lambda tup: chr(uncifrate_num(tup, key)), list_tuples))

gamal = ElGamal(52673)