RC6-Block-Cipher
================

Implementation of RC6-w/r/b encryption and decryption in python.
Values for w/r/b are 32/20/128 with plans to allow customization to other values in future releases.

## Specification

* Block size : 4 * 32 bit Registers = 128 bits

* Key size : 128 bits

* Rounds: 20

* Word Size: 32 bits

## Features

* In cryptography, RC6 (Rivest Cipher 6) is a symmetric key block cipher derived from RC5. 

* It was designed by Ron Rivest, Matt Robshaw, Ray Sidney, and Yiqun Lisa Yin

* It was designed to meet the requirements of the Advanced Encryption Standard (AES) competition. 

* It is a proprietary algorithm, patented by RSA Security.

## Functions

* encrypt.py and decrypt.py are used to encrypt and decrypt using user input or based on command line arguments

* rc6/helper.py contains helper functions 

* rc6/key.py contains the data structure for the Key object

* rc6/ops.py contains the encrypt() and decrypt() functions as well as several functions that contain operations common to both

* rc6/block.py contains the data structure for a Block object

## Example:

	test code:
		import rc6

		testString = "This is a test string that is more than 16 chars and spans over multiple blocks"
		testKey = "abcdefghijklmnopqrstuvqxyz"
		res, str1 = rc6.encrypt(testString, testKey)
		print "Test String: %s, Key: %s" % (testString, testKey)
		res2, str2 = rc6.decrypt(str, testKey)
		print "len(testString): %d" % len(testString)
		print "len(str1): %d" % len(str1)
		print "len(str2): %d" % len(str2)
		print "Before: ", str1
		print "After: ", str2
	
	output:
		python test.py

		Test String: This is a test string that is more than 16 chars and spans over multiple blocks, Key: abcdefghijklmnopqrstuvqxyz
		len(testString): 79
		len(str1): 80
		len(str2): 80
		Encrypted: ����ۋ��/�d�eu���T��.����P�Rw��UGϽB��Шő<&s�D~4�t�Z�!�Ӑ!�L{B~ �
		Decrypted:  This is a test string that is more than 16 chars and spans over multiple blocks