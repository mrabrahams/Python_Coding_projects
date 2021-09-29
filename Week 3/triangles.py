#################################################################
# Program Name: triangles.py                                    #
# Module #3 Programming Assignment #1                           #
# Dwight Abrahams                                               #
# Python Essentials                                             #
# August 29 2021                                                #
# Purpose: based on user input validate if triangle and type    #
#################################################################

"""
A triangle has three sides where the sum of the length of any (every) two of the sides must exceed the other side.

In a right triangle, the square of the length of the longest side is equal to the sum of the squares of the lengths of the other two sides.

In an isosceles triangle the length of any two of the sides must be equal.

In an equilateral triangle the length of all three sides must be equal.

Write a program that prompts the user to enter the lengths of three sides of a triangle. The program will output a message indicating:

        whether or not the lengths form a triangle and, if so, 
        whether or not the triangle is
             a right triangle,
            an isosceles triangle, and/or 
            an equilateral triangle.

Input Validation: Do not accept a number <= 0 for any side.

To submit your assignments:

    Submit your source code files (*.py) appropriately named for each assignment.
    Submit screen shots demonstrating your program works correctly. 
    Any program that requires user input should be run a minimum of three times with varying test values. 
    Screenshots may be embedded in a document for submission or submitted individually.
"""

import pyinputplus as pyinp # python library with premade input-validation functions

def classifyTriangle(list): # takes triangle values and categorizes type based on values.  Prints to output the type or lack of if not a triangle
    # create and use variables for easier call of the values in the list
    a = list[0]
    b = list[1]
    c = list[2]

    if (a + b < c): # not a triangle
        print("Side lengths do not follow triangle length theorem, therefore it is not a true triangle!")

    elif ((a**2) + (b**2) == c**2): # right triangle
        print("The lengths form a right triangle.")

    elif (a == b): # isosceles triangle
        print("The lengths form an isosceles triangle.")

    elif (a == b == c): # equilateral triangle
        print("The lengths form an equilateral triangle.")

    else: # meets the requirement for a triangle
        print("The lengths form a triangle.")
    

def getInput(): # establishes a list with empty values and prompts the user for the specified values

    triangleSize = [None, None, None] # creates a triangle with unknown side lengths 
    index = 0
    while index < 3: # iterates through sides of triangle 
        
        triangleSize[index] = pyinp.inputNum("What is the length of side " + str(index + 1) + " of your triangle? ", min=1) # provides side of triangle with value entered by user as long as value is > 0 

        index += 1
    return triangleSize

if __name__ == "__main__":
   sides = getInput()
   sides.sort() # sort list values for easier calculation
   classifyTriangle(sides)