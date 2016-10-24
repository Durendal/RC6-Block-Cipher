import sys

from rc6.ops import decrypt
from rc6.helpers import deBlocker
from rc6.key import Key

# Determine which mode to run in based on the number of command line arguments
def main():
	cdec() if len(sys.argv) > 1 else dec()
	
def decData(key):

	s = Key(key)
	print "UserKey: %s" % s.getKeyStr() 
	f = open("encrypted.txt","r")

	if not f:
		print "Encrypted input not found in encrypted.txt"
		sys.exit(0)
	
	else:
		esentence   = f.readline()
	
	cipher,orgi	 = decrypt(esentence, s.getKey())
	sentence		= deBlocker(orgi)

	return (cipher, orgi, esentence, sentence)

def dec():

	print "DECRYPTION: "

	key =raw_input("Enter Key(0-16 characters): ")
						 
	cipher, orgi, esentence, sentence = decData(key)
	
	print "\nEncrypted String list: ",cipher
	print "Encrypted String: %s" % esentence
	print "Length of Encrypted String: %d" % len(esentence)

	print "\nDecrypted String list: ", orgi
	print "Decrypted String: %s " % sentence 
	print "Length of Decrypted String: %d" % len(sentence)
	
def cdec():

	if(len(sys.argv)) < 2:
		print "Usage: python cenc.py <key> optional(filename)"
		sys.exit(0)

	key = sys.argv[1]
	
	cipher, orgi, esentence, sentence = decData(key)

	print "\nDecrypted String list: ",orgi
	print "Decrypted String: %s" % sentence 
	


if __name__ == "__main__":
	main()
