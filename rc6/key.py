from helpers import ROL
from block import Block

class Key(object):
	"""
		Key is a data structure representing the encryption key for RC6 encryption algorithm
	"""
	def __init__(self, key = " "):
		"""
			Take a ASCII string as key and generate a key from it.
		"""
		if key and len(key) < 16:
			key += " " * ( 16 - len(key) )
		
		key = key[:16]
		self.setKeyStr(key)
		self._key = self.generateKey()


	#generate key s[0... 2r+3] from self._keyStr
	def generateKey(self):
		"""
			Generate key from keyStr
		"""
		r = 20
		modulo = 2**32
		s = (2 * r + 4) * [0]
		s[0] = 0xB7E15163

		for i in range(1, 2 * r + 4):
			s[i] = (s[i - 1] + 0x9E3779B9) % (modulo)
		blok = Block(self._keyStr)
		encoded = blok.getRegisters()
		enlength = len(encoded)
		l = enlength * [0]
		
		for i in range(1, enlength + 1):
			l[enlength - i] = long(encoded[i - 1], 2)
		
		v = 3 * max(enlength, 2 * r + 4)
		A=B=i=j=0
		
		for index in range(0, v):
			
			A = s[i] = ROL((s[i] + A + B) % modulo, 3, 32)
			B = l[j] = ROL((l[j] + A + B) % modulo, (A + B) % 32, 32) 
			i = (i + 1) % (2 * r + 4)
			j = (j + 1) % enlength
		
		return s

	def setKeyStr(self, key):
		"""
			Set self._keyStr to key
		"""
		self._keyStr = key

	def getKeyStr(self):
		"""
			Return the ASCII Key string
		"""
		return self._keyStr

	def getKey(self):
		"""
			Return the generated key
		"""
		return self._key
