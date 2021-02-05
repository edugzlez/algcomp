import numpy as np


"""
    Generación de claves
"""
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

"""
    Cifrar un número m
"""
def cifrate_num(m, key, b = None):
    g, p, K = key
    if b is None:
        b = np.random.randint(2, p)
    
    y_1 = pow(g, b, p)
    
    return (pow(g, b, p), pow(K, b, p)*m % p)

"""
    Cifrar un texto. Devuelve tuplas.
"""
def cifrate_text(text, key):
    return list(map(lambda char: cifrate_num(ord(char), key), text))

"""
    Cifrar tuplas, devuelve números.
"""
def uncifrate_num(y_tuple, key):
    a, p = key
    y1, y2 = y_tuple

    return pow(y1, p-1-a, p)*y2 % p

"""
    Descifrar una lista de tuplas.
"""
def uncifrate(list_tuples, key):
    return "".join(map(lambda tup: chr(uncifrate_num(tup, key)), list_tuples))