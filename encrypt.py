#!/usr/bin/env python
import sys

from rc6.block import Block
from rc6.ops import encrypt

def enc():
	"""
		Prompt user for input and key, encrypt, and display results
	"""
	print "ENCRYPTION: "

	key = raw_input("Enter Key: ")
		 
	sentence = raw_input("Enter Sentence: ")
	print "User Key: %s" % key[:16]
	blocks, text = encrypt(sentence, key)
	print "%d Blocks" % len(blocks)
	print "\nInput String: %s" % sentence 
	print "Length of Input String: %d" % len(sentence)
	
	print "\nEncrypted String list: ", text
	for blk in blocks:
		print blk.getRegisters()
	print "Encrypted String: %s" % text
	print "Length of Encrypted String: %d" % len(text)

	with open("encrypted.txt","wb") as f:
	   f.write(text);
	
def cenc():
	"""
		Encrypt command line input with command line key and output results
	"""
	if(len(sys.argv)) < 3:
		print "Usage: python %s <key> <string> [filename]" % (sys.argv[0])
		sys.exit(0)

	key = sys.argv[1]				   
	sentence = sys.argv[2]

	blocks, text = encrypt(sentence, key)
	print "%d Blocks" % len(blocks)		
	print "\nEncrypted String list: "
	for blk in blocks:
		print blk.getRegisters()

	print "Encrypted String: %s" % text
	fileName = "encrypted.txt" if len(sys.argv) < 4 else sys.argv[3]

	with open(fileName, "w") as f:
	   f.write(text);

# Determine which mode to run in based on the number of command line arguments
def main():
	cenc() if len(sys.argv) > 1 else enc()

if __name__ == "__main__":
	main()
