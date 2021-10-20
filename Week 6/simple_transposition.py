###################################################################
# Program Name: simple_transposition.py                           #
# Module #2 Programming Assignment #2                             #
# Dwight Abrahams                                                 #
# Python Essentials                                               #
# Octoberber 10 2021                                              #
# Purpose: This is the beginning of creating a simple text encrypt#
#           and decrypt program.                                  #
###################################################################

'''
2. Simple Transposition

Create a program that can encrypt and decrypt a text message using a Simple Transposition scheme. 
The program should use two functions (one to encrypt the message and one to decrypt the message) receiving the message (plaintext or cyphertext accordingly) and the width of the grill. 
Demonstrate it works by encrypting/decrypting several messages showing the original plaintext, the encrypted cyphertext, and the decrypted plain text.

To transpose the message from 'row-wise' to 'column-wise' you need to iterate over the string with a step size of the grill width.
'''

if __name__ == "__main__":
    userInput()