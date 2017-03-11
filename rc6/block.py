import binascii

from helpers import blockConverter, deBlocker
class Block(object):

	def __init__(self, sentence = None, registers = None):
		self._registers = []
		self._sentence = ""
		if sentence:
			if len(sentence) > 16:
				sentence = sentence[:16]
			else:
				sentence += " " * (16 - len(sentence))
			self._sentence = sentence
			self._registers = blockConverter(self._sentence)

		elif registers and type(registers) == list:
			self._registers = registers
			self._sentence = deBlocker(self._registers)
			
		self._size = len(self._sentence)
		self._numRegs = len(self._registers)

	def __str__(self):
		return self._sentence

	def __repr__(self):
		return "Block: <%s>" % (self._sentence)

	def getString(self):
		return self._sentence

	def getStringBase64(self):
		return binascii.b2a_base64(self._sentence)

	def getRegisters(self):
		return self._registers

	def getNumRegs(self):
		return self._numRegs