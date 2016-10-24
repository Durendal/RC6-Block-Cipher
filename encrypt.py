import sys

from rc6.ops import encrypt
from rc6.helpers import generateKey, deBlocker

def main():
    cenc() if len(sys.argv) > 1 else enc()

def enc():
    print "ENCRYPTION: "

    key =raw_input("Enter Key(0-16 characters): ")
    if len(key) <16:
        key += " "*(16-len(key))
    key = key[:16]
                         
    print "UserKey: %s" % key 
    s = generateKey(key)

    sentence =raw_input("Enter Sentence(0-16 characters): ")
    if len(sentence) <16:
        sentence += " "*(16-len(sentence))
    sentence = sentence[:16]
    
    orgi,cipher = encrypt(sentence,s)
    esentence = deBlocker(cipher)
    
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

    key = sys.argv[1]
    if len(key) <16:
        key += " "*(16-len(key))
    key = key[:16]
                         
    s = generateKey(key)
    sentence = sys.argv[2]
    if len(sentence) <16:
        sentence += " "*(16-len(sentence))
    sentence = sentence[:16]
    
    orgi,cipher = encrypt(sentence,s)
    esentence = deBlocker(cipher)
    
    
    print "\nEncrypted String list: ",cipher
    print "Encrypted String: %s" % esentence
    f = open("encrypted.txt","w")
    f.write(esentence);
    f.close()


if __name__ == "__main__":
    main()
