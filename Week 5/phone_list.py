#################################################################
# Program Name: phone_list.py                                   #
# Module #1 Programming Assignment #1                           #
# Dwight Abrahams                                               #
# Python Essentials                                             #
# September 29 2021                                             #
# Purpose: program that provides a menu-driven digital contact  #
#          list to the user.                                    #
#################################################################


'''
Write a program that provides a menu-driven digital contact list to the user. The program should utilize a file containing names, 
phone numbers (number and type - such as Cell, Home, Work, etc.) and email addresses (address and type).

    The program should open the file (if it exists) and populate the program with the contact data.
    The user should then be able to 
        search for the data for a given contact name
        add new contacts
        delete contacts
        add/update/delete phone numbers or email addresses for a contact.
    When the program finishes it should create a file (or overwrite the existing file) with the contact information
'''

import pyinputplus as pyinpt

def userInput(): # gets the path of the file from the user and places it in a variable then calls the menu function
    fileName = input("Enter the name of the file you want to open: ")
    displayMenu(fileName)

def displayMenu(fileName):  # displays a menu to the user and gets the user selection before calling the appropriate function
    with open(fileName, 'a') as file:  # opens the file in append mode, creates if needed and closes when done.
        while True:
            userChoice = pyinpt.inputInt('''
Enter '1' to search for a contact.
Enter '2' to add a new contact.
Enter '3' to delete a contact. 
Enter '4' to add/update/delete phone numbers or email addresses for a contact.
Enter '5' to quit. 
''')

            if userChoice == 1:
                searchContact(file)
                continue
            elif userChoice == 2:
                addContact(file)
                continue
            elif userChoice == 3:
                delContact(file)
                continue
            elif userChoice == 4:
                updateContact(file)
                continue
            elif userChoice == 5:
                print("Thank you, have a nice day!")
                break

def searchContact(file): # navigates the file and locates a contact then returns the information for that specific contact 
    contact = pyinpt.inputStr("Enter a name to search for: ")
    return file

def addContact(file):
    return file

def delContact(file):
    return file

def updateContact(file):
    return file
    
if __name__ == "__main__":
    userInput()