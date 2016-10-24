#!/usr/bin/env python
import sys

from rc6.ops import decrypt
from rc6.helpers import deBlocker
from rc6.key import Key

def decData(key, fileName = "encrypted.txt"):
	"""
		Decrypt the input string with the input key
	"""
	s = Key(key)
	print "UserKey: %s" % s.getKeyStr()

	try:
		with open(fileName, "r") as f:
		   esentence = f.readline()
	except:
		print "Encrypted input not found in encrypted.txt"
		sys.exit(0)
	
	cipher, orgi = decrypt(esentence, s.getKey())
	sentence = deBlocker(orgi)

	return (cipher, orgi, esentence, sentence)

def dec():
	"""
		Prompt user for input and key, decrypt, and display results
	"""
	print "DECRYPTION: "

	key = raw_input("Enter Key(0-16 characters): ")
						 
	cipher, orgi, esentence, sentence = decData(key)
	
	print "\nEncrypted String list: ", cipher
	print "Encrypted String: %s" % esentence
	print "Length of Encrypted String: %d" % len(esentence)

	print "\nDecrypted String list: ", orgi
	print "Decrypted String: %s " % sentence 
	print "Length of Decrypted String: %d" % len(sentence)
	
def cdec():
	"""
		Decrypt command line input with command line key and output results
	"""
	if(len(sys.argv)) < 2:
		print "Usage: python %s <key> [filename]" % (sys.argv[0])
		sys.exit(0)
	fileName = sys.argv[2] if len(sys.argv) > 2 else "encryption.txt"
	key = sys.argv[1]
	
	cipher, orgi, esentence, sentence = decData(key)

	print "\nDecrypted String list: ", orgi
	print "Decrypted String: %s" % sentence 
	
# Determine which mode to run in based on the number of command line arguments
def main():
	cdec() if len(sys.argv) > 1 else dec()
	
if __name__ == "__main__":
	main()
