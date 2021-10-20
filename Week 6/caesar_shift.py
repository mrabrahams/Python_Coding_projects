###################################################################
# Program Name: caesar_shift.py                                   #
# Module #2 Programming Assignment #2                             #
# Dwight Abrahams                                                 #
# Python Essentials                                               #
# Octoberber 10 2021                                              #
# Purpose: This is a simple caesar encryption and decryption      #
#          program.                                               #
###################################################################

'''
1. Caesar Shift:

Create a program that can encrypt and decrypt a text message using a Caeser encryption scheme. 
The program should use two functions (one to encrypt the message and one to decrypt the message) receiving the message (plaintext or cyphertext accordingly) and the Caesar shift offset. 
Demonstrate it works by encrypting/decrypting several messages showing the original plaintext, the encrypted cyphertext, and the decrypted plain text. 
Remember to keep all characters in the printable ASCII range, when you shift an ASCII value above 127 you need to subtract 95 and when you shift an ASCII value below 32 you need to add 95.
'''

if __name__ == "__main__":
    userInput()