#####################################################################
# Program Name: distance_traveled.py                                #
# Module #3 Programming Assignment #3                               #
# Dwight Abrahams                                                   #
# Python Essentials                                                 #
# August 29 2021                                                    #
# Purpose: based on user input calculate distance traveled per hr   #
#####################################################################

"""
The distance a vehicle travels can be calculated as follows:

distance = speed * time

For example, if a train travels 40 miles per hour for 3 hours, the distance traveled is 120 miles.

Write a program that asks the user for the speed of a vehicle (in miles per hour) and how many hours it has traveled. 
The program should then use a loop to display the distance the vehicle has traveled for each hour of that time period. 
Here is an example of the output:

What is the speed of the vehicle in mph? 40

How many hours has it traveled? 3

Hour  Distance Traveled
--------------------------------
 1           40
 2           80
 3          120

Input Validation: Do not accept a negative number for speed and do not accept any value less than 1 for time traveled.


To submit your assignments:

    Submit your source code files (*.py) appropriately named for each assignment.
    Submit screen shots demonstrating your program works correctly. 
    Any program that requires user input should be run a minimum of three times with varying test values. 
    Screenshots may be embedded in a document for submission or submitted individually.
"""


def userSpeed(): # function that will take user input for speed and validate before storing and returning it
    while True:  # loop to receive user input and repeat request if validation fails
        try:
            speed = int(input("What is the speed of the vehicle (in mph)? "))
        except: # stops and starts loop from the top if non-integer data is entered
            print("Try again, speed must be in integer form larger than 0!") 
            continue  
        if speed < 0: # stops and starts loop from the top if negative integer is entered
            print("Your speed can not be lower than zero (0) mph.")
            continue
        return speed


def travelTime(): # function that will take user input for time and validate before storing and returning it
    while True: # loop to receive user input and repeat request if validation fails
        try:
            time = int(input("How many hours has it traveled? "))
        except: # stops and starts loop from the top if non-integer data is entered
            print("Try again, please enter time in integer form!")
            continue  
        if time < 1: # stops and starts loop from the top if integer less than 1 is entered 
            print("Your time can not be lower than one (1) hour.")
            continue
        return time

def calculateDistance(speed, time): # function will take speed and time as arguments and print to output the distance traveled per hour
    hour = 0 # used instead of 'i' and a 'for' loop to control looping

    while hour <= time:
        if hour == 0:  # provides a heading and breakline to help readability of output
            print("Hour\t\tDistance Traveled")
            print("--------------------------------")
        else: 
            print(str(hour) + "\t\t\t" + str(speed * hour)) # prints the hour in and distance traveled under appropriate headings
        
        hour += 1 # updates hour variable and keeps track to break loop

if __name__ == "__main__": # used to execute code only if the file was run directly. calls the necessary functions
    speed = userSpeed()
    time = travelTime()
    calculateDistance(speed, time)