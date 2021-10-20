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

from os import sep, write
import pyinputplus as pyinpt
import os.path

def create_user(addUser): # takes self as an argument and creates a contact with the required parameters
        user = {'first name': None, 'last name': None, 'cell number': None, 'home number': None, 'work number': None, 'home email': None, 'work email': None}

        while True:
            
            try:
                for key_name, value_name in user.items():
                    user[key_name] = input(f"Please enter the {key_name} for {addUser}: ")
            except:
                print("Invalid input please try again!")
                continue
            
            return user

def user_input(): # gets the path of the file from the user and places it in a variable then calls the menu function
    fileName = input("Enter the name of the file you want to open: ")
    display_menu(fileName)

def check_file(fileName): # checks if valid file and creates if not
    if os.path.isfile(fileName):
        display_menu(fileName)
    else:
        with open(fileName, 'w') as contacts:
            display_menu(contacts)

def display_menu(fileName):  # displays a menu to the user and gets the user selection before calling the appropriate function
    while True:
        userChoice = pyinpt.inputInt('''
Enter '1' to search for a contact.
Enter '2' to add a new contact.
Enter '3' to delete a contact. 
Enter '4' to add/update/delete phone numbers or email addresses for a contact.
Enter '5' to quit. 
''')

        if userChoice == 1:
            search_user(fileName)
            continue
        elif userChoice == 2:
            add_user(fileName)
            continue
        elif userChoice == 3:
            del_user(fileName)
            continue
        elif userChoice == 4:
            update_user(fileName)
            continue
        elif userChoice == 5:
            print("Thank you, have a nice day!")
            break

def search_user(fileName): # navigates the file and locates a contact then returns the information for that specific contact 
    with open(fileName, 'r') as contactsFile:  # opens the file in read mode, creates if needed and closes when done.
        contactsFile.seek(0,0)
        while True:
            userSearch = input("Enter a name to search for (type q to exit): ")
            if userSearch.lower() == "q":
                break
            else:
                for line in contactsFile:
                    if userSearch in line:
                        print(line)
                        break
                    else:
                        print("Contact not found!")
                        break
                continue
        return

def add_user(fileName): # opens the file and adds a user with the required information 
    with open(fileName, 'r+') as contactsFile:  # opens the file in read an write mode, creates if needed and closes when done.
        
        while True:
            addUser = input("Enter the name of the user you would like to add (type q to exit): ")

            if addUser.lower() == "q":
                break
            elif addUser != "q":
                for line in contactsFile:
                    if addUser in line:
                        print(addUser + " is already added in the file please use the update function!")
                        break
                    continue
                else:
                    print(f"{addUser} not found in file. Please gather all information and prepare to add.")
                    user = create_user(addUser)
                    contactsFile.seek(0, 2)
                    pen = contactsFile.writelines
                    for value in user.values():
                        pen("{0}+', '".format(value))  #https://stackoverflow.com/questions/30499855/how-to-save-a-dictionary-in-python-to-a-text-file-separated-by-white-spaces
                    return

def del_user(fileName):
    with open(fileName, 'r') as file:  # opens the file in read mode, and closes when done.
        
        data = file.readlines()

        for line in data:
            print(line.split("\n"))

    while True:
        delUser = input("Enter the name of the user you would like to delete (type q to exit): ")

        if delUser.lower() == "q":
                break

        with open(fileName, 'w') as contactsFile:  # opens the file in write mode, creates if needed and closes when done.
            for line in data:
                if line.split("\n") != delUser:
                    contactsFile.write(line)
                    return
        
        return -1 

def update_user(): # update user information for a specific contact
    print("Updating informating in database...")
   
    
if __name__ == "__main__":
    user_input()