import sys

from helpers import ROR, ROL
from block import Block

def setup(sentence):
    """
        Perform basic setup that applies to both encrypt and decrypt methods
    """
    blok = Block(sentence)
    encoded = blok.getRegisters()
    enlength = len(encoded)
    A = long(encoded[0],2)
    B = long(encoded[1],2)
    C = long(encoded[2],2)
    D = long(encoded[3],2)

    orgi = prologue(A, B, C, D)

    w = 32
    b = 32
    r = 20
    modulo = 2**w
    lgw = 5

    return (A, B, C, D, r, b, modulo, lgw, orgi)

def prologue(A, B, C, D):

    orgi = []
    orgi.append(A)
    orgi.append(B)
    orgi.append(C)
    orgi.append(D)

    return orgi

def encrypt(sentence,s):
    """
        Encrypt sentence with key s
    """
    A, B, C, D, r, b, modulo, lgw, orgi = setup(sentence)  
    B = (B + s[0]) % modulo
    D = (D + s[1]) % modulo 
    for i in range(1, r + 1):
        t_temp = (B * (2 * B + 1)) % modulo 
        t = ROL(t_temp, lgw, b)
        u_temp = (D * (2 * D + 1)) % modulo
        u = ROL(u_temp, lgw, b)
        tmod= t % 32
        umod= u % 32
        A = (ROL(A^t, umod, b) + s[2 * i]) % modulo 
        C = (ROL(C^u, tmod, b) + s[2 * i + 1]) % modulo
        (A, B, C, D)  =  (B, C, D, A)
    A = (A + s[2 * r + 2]) % modulo 
    C = (C + s[2 * r + 3]) % modulo

    cipher = prologue(A, B, C, D)

    return (orgi, cipher)
    
def decrypt(esentence,s):
    """
        Decrypt esentence with key s
    """
    A, B, C, D, r, b, modulo, lgw, cipher = setup(esentence)  

    C = (C - s[2 * r + 3]) % modulo
    A = (A - s[2 * r + 2]) % modulo
    for j in range(1, r + 1):
        i = r + 1 - j
        (A, B, C, D) = (D, A, B, C)
        u_temp = (D * (2 * D + 1)) % modulo
        u = ROL(u_temp, lgw, b)
        t_temp = (B * (2 * B + 1)) % modulo 
        t = ROL(t_temp, lgw, b)
        tmod= t % 32
        umod= u % 32
        C = (ROR((C - s[2 * i + 1]) % modulo, tmod, b) ^ u)  
        A = (ROR((A - s[2 * i]) % modulo, umod, b) ^ t) 
    D = (D - s[1]) % modulo 
    B = (B - s[0]) % modulo

    orgi = prologue(A, B, C, D)

    return (cipher, orgi)
