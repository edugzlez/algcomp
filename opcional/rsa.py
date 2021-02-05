import numpy as np


"""
    Cifrar número a partir de una clave
"""
def cifrate_num(number, key):
    n, e = key
    return pow(number, e, n)

"""
    Cifrar texto a partir de una clave
"""
def cifrate_text(text, key):
    return "".join(map(lambda char: chr(cifrate_num(ord(char), key)), text))


"""
    Generación de claves
"""
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
