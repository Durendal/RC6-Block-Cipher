import math

#rotate right input x, by n bits
def ROR(x, n, bits = 32):
    mask = (2L**n) - 1
    mask_bits = x & mask

    return (x >> n) | (mask_bits << (bits - n))

#rotate left input x, by n bits
def ROL(x, n, bits = 32):
    return ROR(x, bits - n,bits)



