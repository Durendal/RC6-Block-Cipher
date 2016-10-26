#rotate right input x, by n bits
def ROR(x, n, bits = 32):
    mask = (1 << n) - 1
    mask_bits = x & mask

    return (x >> n) | (mask_bits << (bits - n))

#rotate left input x, by n bits
def ROL(x, n, bits = 32):
    return ROR(x, bits - n, bits)

#convert input sentence into blocks of binary
#creates 4 blocks of binary each of 32 bits.
def blockConverter(sentence):
    encoded = []
    res = ""
    for i in range(0,len(sentence)):
        if (i % 4 == 0) and (i != 0):
            encoded.append(res)
            res = ""

        temp = bin(ord(sentence[i]))[2:]

        if len(temp) < 8:
            temp = "0" * (8 - len(temp)) + temp
        res += temp
    encoded.append(res)

    return encoded

#converts 4 blocks array of long int into string
def deBlocker(registers):
    s = ""
    for ele in registers:
        temp = bin(ele)[2:]
        if len(temp) <32:
            temp = "0" * ( 32 - len(temp) ) + temp
        for i in range(0,4):
            s += chr(int(temp[i * 8:(i + 1) * 8], 2))


    return s