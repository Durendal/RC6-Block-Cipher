#!/usr/bin/env python
import binascii
import string
import base64
import sys

from rc6.ops import decrypt
from rc6.key import Key

# From http://stackoverflow.com/a/31566605/3718401 Thanks skyler!
def isASCII(s):
	return all(c in string.printable for c in s)

def decData(key, fileName = "encrypted.txt"):
	"""
		Decrypt the input string with the input key
	"""
	s = Key(key)
	print "\n\nUserKey: %s" % s.getKeyStr()

	try:
		with open(fileName, "rb") as f:
		   esentence = ''.join(f.readlines())
	except:
		print "Encrypted input not found in %s" % fileName
		sys.exit(0)
	print "Encrypted text %s: %s" % ("base64" if isASCII(esentence) else "Binary", esentence)
	if isASCII(esentence):
		esentence = binascii.a2b_base64(esentence)
	return decrypt(esentence, key)
	

def dec():
	"""
		Prompt user for input and key, decrypt, and display results
	"""
	print "DECRYPTION: "

	key = raw_input("Enter Key: ")
						 
	blocks, text = decData(key)
	print "%d Blocks" % len(blocks)
	print "\nDecrypted String list: "
	for blk in blocks:
		print blk.getRegisters()

	print "Decrypted String: %s " % text 
	print "Length of Decrypted String: %d" % len(text)
	
def cdec():
	"""
		Decrypt command line input with command line key and output results
	"""
	if len(sys.argv) < 2:
		print "Usage: python %s <key> [filename]" % (sys.argv[0])
		sys.exit(0)

	fileName = sys.argv[2] if len(sys.argv) > 2 else "encrypted.txt"
	key = sys.argv[1]

	blocks, text = decData(key, fileName)
	print "%d Blocks" % len(blocks)
	print "\nDecrypted String list: "
	for blk in blocks:
		print blk.getRegisters()

	print "Decrypted String: %s" % text
	
# Determine which mode to run in based on the number of command line arguments
def main():
	cdec() if len(sys.argv) > 1 else dec()
	
if __name__ == "__main__":
	main()
