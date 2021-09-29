#################################################################
# Program Name: falling_distance.py                             #
# Module #4 Programming Assignment #1                           #
# Dwight Abrahams                                               #
# Python Essentials                                             #
# September 10 2021                                             #
# Purpose: based on user input calculate distance item fell     #
#################################################################

"""
When an object is falling because of gravity, the following formula can be used to determine the distance the object falls in a specific time period:

d = 1/2 gt**2

The variables in the formula are as follows: d is the distance in meters, g is 9.8, and t is the amount of time, in seconds, that the object has been falling.

Write a function named fallingDistance that accepts an object’s falling time (in seconds) as an argument. 
The function should return the distance, in meters, that the object has fallen during that time interval. 
Write a program that demonstrates the function by prompting the user for the total time and calling the function in 
a loop that passes the time values in 5 second increments as the argument and displays the elapsed time and return value. 
The output should have a header identifying the column names and tabular formatted values (values displayed are to illustrate formatting only):
Time	Distance
0	0.0
5	30.0
10	45.0
15	52.0

Input Validation: Do not accept a negative number for time.


To submit your assignments:

    Submit your source code files (*.py) appropriately named for each assignment.
    Submit screen shots demonstrating your program works correctly. 
    Any program that requires user input should be run a minimum of three times with varying test values. 
    Screenshots may be embedded in a document for submission or submitted individually.
"""
import pyinputplus as pyinp # python library with premade input-validation functions

def fallingDistance(time): # function that takes time as argument and returns distance object as moved in meters
    gravity = 9.8
    distance = (gravity * (time**2)) / 2
    return distance

def userInput():
    while True:
        time = pyinp.inputInt("Please enter the number of seconds for which the object has been falling: ", min=0) # gets the user input only if larger than negative integers
        if time < 0:  # if negative requests another number and prompts user with guidance
            print("Please enter a non negative number!")
            continue
        else:  # if user enters a positive integer the below path will be ran
            i = 0
            dist = fallingDistance(time) # gets distance
            distance = round(dist, 2) # rounds distance to two decimal places
            if i == 0: # prints header and first line with time and distance
                print("Time\t\tDistance")
                print(str(time) + "\t\t" + str(distance) + "m")
            for i in range (4): # prints remaining rows while incrementing original time and calling distance function
                time += 5
                dist = fallingDistance(time)
                distance = round(dist, 2)
                print(str(time) + "\t\t" + str(distance) + "m")

        break
            

if __name__ == "__main__":
    userInput()