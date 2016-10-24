RC6-Block-Cipher
================

Implementation of RC6 encryption and decryption  in python.

## Specification

* Block size : 4*32 bit blocks

* Key size : 128bit

* Rounds: 12

## Features

* In cryptography, RC6 (Rivest Cipher 6) is a symmetric key block cipher derived from RC5. 

* It was designed by Ron Rivest, Matt Robshaw, Ray Sidney, and Yiqun Lisa Yin

* It was designed to meet the requirements of the Advanced Encryption Standard (AES) competition. 

* It is a proprietary algorithm, patented by RSA Security.

## Functions

* encrypt.py and decrypt.py are used to encrypt and decrypt using user input or based on command line input

* rc6/helper.py contains helper functions 

* rc6/key.py contains the data structure for the Key object

* rc6/ops.py contains the encrypt() and decrypt() functions as well as several functions that contain operations common to both