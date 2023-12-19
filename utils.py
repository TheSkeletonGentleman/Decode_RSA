"""
Authors:    Nikolic Stefan, Rouiller Cyril, Lapaire Sabrina, Marty Hugo
Project:    Decode RSA
Date:       14.12.2023
File:       fonctions_utiles.py
Summary:    Quelques fonctions utiles pour le projet
"""

import random
import math

# Find p and q knowing n
def find_p_q(n):
    if n % 2 == 0:
        #print("Les nombres clef premiers sont : 2 et ", int(n/2))
        return 2, int(n/2)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            #if miller_rabin(i, 10) and miller_rabin(int(n/i), 10):
            #    print("Les nombres clef premiers sont : ", i, " et ", int(n/i))
            return i, int(n/i)
    return 0

# Find d knowing n and e
def find_d(n, e):
    d = invmod(e, phi(n))
    #print(d)
    return d

# Return the number of numbers coprime with n
def phi(n):
    p, q = find_p_q(n)
    return (p-1) * (q-1)

# Int to string
def decodemsg(M):
    return M.to_bytes((M.bit_length() + 7) // 8, "little").decode("utf-8")

# String to int
def encode_msg(m):
    m.encode('utf-8')
    tmp = bytes(m, 'utf-8')
    str = int.from_bytes(tmp, "little")
    return str

# Return num power exponent modulo mod
def exponentiation(b, exp, m):
    res = 1
    while exp > 1:
        if exp & 1: # & means an AND bit per bit with 1 : determine if exp is odd (same as % 2 == 0) 
            res = (res * b) % m
        b = b ** 2 % m
        exp >>= 1 # shift bit to the right by one, it's like divide by 2
    return (b * res) % m

# Determine if a number is prime after 'k' tests
def miller_rabin(n,k):
    r, s = 0, n - 1

    while s % 2 == 0:
        r += 1
        s //= 2  #floor division 
        
    for i in range(k):
        a = random.randint(2,n - 1)
        res = exponentiation(a,s,n)
        if res == 1 or res == n-1:
            continue
        for j in range(r - 1):
            res = pow(res, 2, n)
            if res == n - 1:
                break
        else:
            return False
    return True

# give the inverse modular of a number
def invmod(x, p):
    return pow(x, -1, p)