from helpers import blockConverter, ROL
class Key(object):

	def __init__(self, key = None):
		if key and len(key) <16:
			key += " "*(16-len(key))
		
		key = key[:16] if key else None
		
		self._key		= None
		self.setKeyStr(key)

		if self._keyStr:
			self._key 	= self.generateKey()


	#generate key s[0... 2r+3] from self._keyStr
	def generateKey(self):
		if not self._keyStr:
			return None

		r 		=12
		b 		=len(self._keyStr)
		modulo 	= 2**32
		s 		=(2*r+4)*[0]
		s[0]	=0xB7E15163

		for i in range(1,2*r+4):
			s[i]=(s[i-1]+0x9E3779B9)%(modulo)
		
		encoded = blockConverter(self._keyStr)
		#print encoded
		
		enlength= len(encoded)
		l 		= enlength*[0]
		
		for i in range(1,enlength+1):
			l[enlength-i]=long(encoded[i-1],2)
		
		v = 3*max(enlength,2*r+4)
		A=B=i=j=0
		
		for index in range(0,v):
			A = s[i] = ROL((s[i] + A + B)%modulo,3,32)
			B = l[j] = ROL((l[j] + A + B)%modulo,(A+B)%32,32) 
			i = (i + 1) % (2*r + 4)
			j = (j + 1) % enlength
		
		return s

	def setKeyStr(self, key):
		self._keyStr = key

	def getKeyStr(self):
		return self._keyStr

	def getKey(self):

		return self._key
