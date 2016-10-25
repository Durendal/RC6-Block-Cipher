import math
import sys

from helpers import ROR, ROL
from block import Block
from key import Key

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

	orgi = [A, B, C, D]

	w = 32
	b = 32
	r = 20
	modulo  = 1 << w			 # 2^w
	lgw	 = int(math.log(w, 2))# Logarithm of w, base 2

	return (A, B, C, D, w, r, b, modulo, lgw, orgi)

def encryptBlock(sentence, k):
	"""
		Encrypt sentence with key s
	"""
	s = k.getKey()
	A, B, C, D, w, r, b, modulo, lgw, orgi = setup(sentence)  
	B = (B + s[0]) % modulo
	D = (D + s[1]) % modulo 
	for i in range(1, r + 1): 
		t = ROL((B * (2 * B + 1)) % modulo, lgw, b)
		u = ROL((D * (2 * D + 1)) % modulo, lgw, b)
		A = (ROL(A^t, u % w, b) + s[2 * i]) % modulo 
		C = (ROL(C^u, t % w, b) + s[2 * i + 1]) % modulo
		(A, B, C, D)  =  (B, C, D, A)
	A = (A + s[2 * r + 2]) % modulo 
	C = (C + s[2 * r + 3]) % modulo

	cipher = [A, B, C, D]

	return (orgi, cipher)
	
def decryptBlock(esentence,k):
	"""
		Decrypt esentence with key s
	"""
	s = k.getKey()
	A, B, C, D, w, r, b, modulo, lgw, cipher = setup(esentence)  

	C = (C - s[2 * r + 3]) % modulo
	A = (A - s[2 * r + 2]) % modulo
	for j in range(1, r + 1):
		i = r + 1 - j
		(A, B, C, D) = (D, A, B, C)
		u = ROL((D * (2 * D + 1)) % modulo, lgw, b) 
		t = ROL((B * (2 * B + 1)) % modulo, lgw, b)
		C = (ROR((C - s[2 * i + 1]) % modulo, t % w, b) ^ u)  
		A = (ROR((A - s[2 * i]) % modulo, u % w, b) ^ t) 
	D = (D - s[1]) % modulo 
	B = (B - s[0]) % modulo

	orgi = [A, B, C, D]

	return (cipher, orgi)

def encrypt(sentence, s):
	blocks = []
	encryptedData = ""

	#count = 1
	for i in range(0, len(sentence), 16):
		if len(sentence[i:]) < 16:
			sentence += " " * (16 - len(sentence[i:]))

		_, cipher = encryptBlock(sentence[i:i+16], Key(s))
		blocks.append(Block(registers=cipher))

		#print "Encrypting Block %d\r" % count
		encryptedData += "%s" % blocks[-1].getString()
		#count += 1

	#print "Message encrypted"
	return (blocks, encryptedData)

def decrypt(esentence, s):
	blocks = []
	decryptedData = ""

	#count = 1
	for i in range(0, len(esentence), 16):
		if len(esentence[i:]) < 16:
			esentence += " " * (16 - len(esentence[i:]))

		_, orgi = decryptBlock(esentence[i:i+16], Key(s))

		#print "Decrypting Block %d\r" % count
		blocks.append(Block(registers=orgi))
		decryptedData += "%s" % blocks[-1].getString()
		#count += 1

	return (blocks, decryptedData)
