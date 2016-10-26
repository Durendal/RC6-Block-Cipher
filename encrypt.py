#!/usr/bin/env python
import binascii
import base64
import sys

from rc6.block import Block
from rc6.ops import encrypt

def encData(sentence, key):
	print "\n\nUser Key: %s" % key[:16]
	blocks, text = encrypt(sentence, key)
	print "%d Blocks" % len(blocks)
	print "\nInput String: %s" % sentence 
	print "Length of Input String: %d" % len(sentence)
	
	print "\nEncrypted String list: ", text
	for blk in blocks:
		print blk.getRegisters()
	print "Encrypted String %s: %s" % (("base64", binascii.b2a_base64(text)) if "--armor" in sys.argv else ("Binary", text))
	print "Length of Encrypted String: %d" % len(text)

	return text

def enc():
	"""
		Prompt user for input and key, encrypt, and display results
	"""
	print "ENCRYPTION: "

	key = raw_input("Enter Key: ")
		 
	sentence = raw_input("Enter Sentence: ")
	text = encData(sentence, key)

	with open("encrypted.txt","wb") as f:
	   f.write(text);
	
def cenc():
	"""
		Encrypt command line input with command line key and output results
	"""
	if(len(sys.argv)) < 3:
		print "Usage: python %s <key> <string> [filename] [--armor]" % (sys.argv[0])
		sys.exit(0)

	key = sys.argv[1]				   
	sentence = sys.argv[2]

	text = encData(sentence, key)
	fileName = "encrypted.txt" if len(sys.argv) < 4 else sys.argv[3]
	if fileName == "--armor":
		fileName = "encrypted.txt"
	if "--armor" in sys.argv:
		text = base64.b64encode(text)
	print text
	with open(fileName, "wb") as f:
	   f.write(text);

# Determine which mode to run in based on the number of command line arguments
def main():
	cenc() if len(sys.argv) > 1 else enc()

if __name__ == "__main__":
	main()
