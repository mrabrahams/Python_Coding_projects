#################################################################
# Program Name: area_of_a_circle.py                             #
# Module #4 Programming Assignment #2                           #
# Dwight Abrahams                                               #
# Python Essentials                                             #
# September 10 2021                                             #
# Purpose: based on user input calculate the radius, diameter,  #
#          circumference, and area.                             #
#################################################################

"""
The following formula gives the distance between two points, (x1, y1) and (x2, y2) in the Cartesian plane:

distance

Given the center and a point on the circle, you can use this formula to find the radius of the circle. 
Write a program that prompts the user to enter the center and a point on the circle (two tuples containing an x and y value). 
The program should then output the circle’s radius, diameter, circumference, and area. Your program must have at least the following functions:

calculateRadius: Receives the x-y coordinates of the center and point on the circle (as input by the user) and calculates the distance between the points. 
This value is returned as the radius of the circle.

calculateArea: Receives the radius of a circle, calculates and returns the area of the circle.

calculatePerimeter: Receives the radius of a circle, calculates and returns the perimeter of the circle.

The output should clearly display the radius, area, and perimeter of the resulting circle.

Input Validation: Do not accept a non-digit character as input.

To submit your assignments:

    Submit your source code files (*.py) appropriately named for each assignment.
    Submit screen shots demonstrating your program works correctly. 
    Any program that requires user input should be run a minimum of three times with varying test values. 
    Screenshots may be embedded in a document for submission or submitted individually.
"""

import pyinputplus as pyinp # python library with premade input-validation functions
import math as mt # python math library

def calculateRadius(x_coord1, y_coord1, x_coord2, y_coord2):
    radius = mt.sqrt((x_coord2-x_coord1)**2 + (y_coord2-y_coord1)**2)
    radius = round(radius, 2)
    return radius

def calculateArea(radius):
    area = (mt.pi*radius)**2
    area = round(area, 2)
    return area

def calculatePerimeter(radius):
    perimeter = 2*mt.pi*radius
    perimeter = round(perimeter, 2)
    return perimeter

def userInput():
    x_coord1 = pyinp.inputNum("Please enter the x coordinate for the center of the circle: ")
    y_coord1 = pyinp.inputNum("Please enter the y coordinate for the center of the circle: ")
    x_coord2 = pyinp.inputNum("Please enter the x coordinate for the a point on the circle: ")
    y_coord2 = pyinp.inputNum("Please enter the y coordinate for the previous point on the circle: ")
    circlePoints = (x_coord1, y_coord1, x_coord2, y_coord2)

    radius = calculateRadius(*circlePoints)
    area = calculateArea(radius)
    perimeter = calculatePerimeter(radius)

    main(radius, area, perimeter)

def main(radius, area, perimeter):
    
    print(f"The radius of the circle is {radius}\nThe area of the circle is {area}\nThe perimeter of the circle is {perimeter}")

if __name__ == "__main__":
    userInput()