import math
from .Primes import generate_prime


class PublicKey(object):

    @classmethod
    def from_n(cls, n):
        return cls(n)

    def __init__(self, n):
        self.n = n
        self.n_sq = n * n
        self.g = n + 1

    def __repr__(self):
        return '<PublicKey: %s>' % self.n


def invmod(a, p, maxiter=1000000):
    """The multiplicitive inverse of a in the integers modulo p:
         a * b == 1 mod p
       Returns b.
       (http://code.activestate.com/recipes/576737-inverse-modulo-p/)"""
    if a == 0:
        raise ValueError('0 has no inverse mod %d' % p)
    r = a
    d = 1
    for i in range(min(p, maxiter)):
        d = ((p // r + 1) * d) % p
        r = (d * a) % p
        if r == 1:
            break
    else:
        raise ValueError('%d has no inverse mod %d' % (a, p))
    return d


def encrypt(pub, plain):
    while True:
        r = generate_prime(int(round(math.log(pub.n, 2))))
        if r > 0 and r < pub.n:
            break

    x = pow(r, pub.n, pub.n_sq)

    cipher = (pow(pub.g, plain, pub.n_sq) * x) % pub.n_sq
    return cipher


def enc_add(pub, a, b):
    """Add one encrypted integer to another"""
    return a * b % pub.n_sq


def secure_addition(result_local, result_prev, n=None):
    if not n:
        raise ValueError("Empty secure addition key")

    pk = PublicKey.from_n(n)

    if result_prev is None:
        pt = 0
        ct1 = encrypt(pk, pt)
    else:
        ct1 = result_prev

    enc_local = encrypt(pk, result_local)

    ct_added = enc_add(pk, ct1, enc_local)

    return ct_added
