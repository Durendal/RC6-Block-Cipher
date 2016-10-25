import binascii

class Block(object):

	def __init__(self, sentence = None, registers = None):

		if sentence:
			if len(sentence) > 16:
				sentence = sentence[:16]
			else:
				sentence += " " * (16 - len(sentence))
			self._sentence = sentence
			self.blockConverter()

		elif registers and type(registers) == list:
			self._registers = registers
			self.deBlocker()

		self._size = len(self._sentence)
		self._numRegs = len(self._registers)

	#convert input sentence into blocks of binary
	#creates 4 blocks of binary each of 32 bits.
	def blockConverter(self):
	    encoded = []
	    res = ""
	    for i in range(0,len(self._sentence)):
	        if (i % 4 == 0) and (i != 0):
	            encoded.append(res)
	            res = ""

	        temp = bin(ord(self._sentence[i]))[2:]

	        if len(temp) <8:
	            temp = "0"*(8-len(temp)) + temp
	        res += temp
	    encoded.append(res)

	    self._registers = encoded

	    return encoded

	#converts 4 blocks array of long int into string
	def deBlocker(self):
	    s = ""
	    for ele in self._registers:
	        temp =bin(ele)[2:]
	        if len(temp) <32:
	            temp = "0"*(32-len(temp)) + temp
	        for i in range(0,4):
	            s+=chr(int(temp[i*8:(i+1)*8],2))
	    self._sentence = s

	    return s

	def getString(self):
		return self._sentence

	def getStringBase64(self):
		return binascii.b2a_base64(self._sentence)

	def getRegisters(self):
		return self._registers

	def getNumRegs(self):
		return self._numRegs