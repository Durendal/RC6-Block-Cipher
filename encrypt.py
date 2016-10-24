import sys

from rc6.ops import encrypt
from rc6.helpers import deBlocker
from rc6.key import Key

# Determine which mode to run in based on the number of command line arguments
def main():
	cenc() if len(sys.argv) > 1 else enc()

def encData(sentence, key):
	
	s = Key(key)
	print "UserKey: %s" % s.getKeyStr()

	if len(sentence) < 16:
		sentence += " " * ( 16 - len(sentence) )
	
	sentence = sentence[:16]
	
	orgi,cipher = encrypt(sentence, s.getKey())
	esentence = deBlocker(cipher)

	return (orgi, cipher, esentence)

def enc():
	
	print "ENCRYPTION: "

	key = raw_input("Enter Key(0-16 characters): ")
		 
	sentence = raw_input("Enter Sentence(0-16 characters): ")

	orgi, cipher, esentence = encData(sentence, key)
	
	print "\nInput String: %s" % sentence 
	print "Original String list: ",orgi
	print "Length of Input String: %d" % len(sentence)
	
	print "\nEncrypted String list: ",cipher
	print "Encrypted String: %s" % esentence
	print "Length of Encrypted String: %d" % len(esentence)

	f = open("encrypted.txt","w")
	f.write(esentence);
	f.close()

def cenc():

	if(len(sys.argv)) < 3:
		print "Usage: python cenc.py <key> <string>"
		sys.exit(0)

	key		 = sys.argv[1]				   
	sentence = sys.argv[2]

	orgi, cipher, esentence = encData(sentence, key)
		
	print "\nEncrypted String list: ",cipher
	print "Encrypted String: %s" % esentence
	
	f = open("encrypted.txt","w")
	f.write(esentence);
	f.close()

if __name__ == "__main__":
	main()
