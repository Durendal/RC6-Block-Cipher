#!/usr/bin/env python
import sys

from rc6.block import Block
from rc6.ops import encrypt
from rc6.key import Key

def encData(sentence, key):
	"""
		Encrypt the input string with the input key
	"""
	s = Key(key)
	print "UserKey: %s" % s.getKeyStr()

	if len(sentence) < 16:
		sentence += " " * ( 16 - len(sentence) )
	
	sentence = sentence[:16]
	
	orgi, cipher = encrypt(sentence, s.getKey())
	blok = Block(registers=cipher)
	esentence = blok.getString()

	return (orgi, cipher, esentence)

def enc():
	"""
		Prompt user for input and key, encrypt, and display results
	"""
	print "ENCRYPTION: "

	key = raw_input("Enter Key(0-16 characters): ")
		 
	sentence = raw_input("Enter Sentence(0-16 characters): ")

	orgi, cipher, esentence = encData(sentence, key)
	
	print "\nInput String: %s" % sentence 
	print "Original String list: ", orgi
	print "Length of Input String: %d" % len(sentence)
	
	print "\nEncrypted String list: ", cipher
	print "Encrypted String: %s" % esentence
	print "Length of Encrypted String: %d" % len(esentence)

	with open("encrypted.txt","w") as f:
	   f.write(esentence);
	
def cenc():
	"""
		Encrypt command line input with command line key and output results
	"""
	if(len(sys.argv)) < 3:
		print "Usage: python %s <key> <string> [filename]" % (sys.argv[0])
		sys.exit(0)

	key = sys.argv[1]				   
	sentence = sys.argv[2]

	orgi, cipher, esentence = encData(sentence, key)
		
	print "\nEncrypted String list: ", cipher
	print "Encrypted String: %s" % esentence
	fileName = "encrypted.txt" if len(sys.argv) < 4 else sys.argv[3]

	with open(fileName, "w") as f:
	   f.write(esentence);

# Determine which mode to run in based on the number of command line arguments
def main():
	cenc() if len(sys.argv) > 1 else enc()

if __name__ == "__main__":
	main()
