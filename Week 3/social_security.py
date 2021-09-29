#################################################################
# Program Name: social_security.py                              #
# Module #3 Programming Assignment #2                           #
# Dwight Abrahams                                               #
# Python Essentials                                             #
# August 29 2021                                                #
# Purpose: based on user input calculate social security pay    #
#################################################################

"""
The full retirement age for social security has changed over the years:

            65 for those born before 1943
            66 for people born between 1943 and 1954
            66 and 2 months for those born before 1957. 
            66 and 4 months for someone born before 1958,
            66 and 6 months for someone born before 1960, and
            67 for people born 1960 or later.

While Social Security takes a user's 35 best-paid years and produces what it calls an average indexed monthly earnings (AIME), 
we will calculate "our" Social Security payout based on a user's stated current monthly income.

Social Security then applies a formula to that monthly income to determine a user's retirement benefit 
(That’s the amount they’ll get each month from Social Security at their full retirement age).

            90 percent of the first $996 of the user's monthly income;
            plus 32 percent of any amount over $996 up to $6,002
            plus 15 percent of any amount over $6,002.

Write a program that prompts the user to enter their date of birth (month, day, and year) along with their current monthly income. 
The program will output a message indicating the date they will reach full retirement and the amount they will be eligible to collect.

Input Validation: Do not accept a number <= 0 for monthly income, a value < 1 or > 12 for the month, a value < 1 or > 31 for the day 
and a value < 1940 or > 2021 for the year.

To submit your assignments:

    Submit your source code files (*.py) appropriately named for each assignment.
    Submit screen shots demonstrating your program works correctly. 
    Any program that requires user input should be run a minimum of three times with varying test values. 
    Screenshots may be embedded in a document for submission or submitted individually.
"""

import pyinputplus as pyinp # python library with premade input-validation functions
from datetime import MINYEAR, date as dt # for me to use todays date to calculate age from date of birth 

def checkRetireAge(birthDate, monthlyPay):

    age = calculateAge(birthDate, age=None)
    if birthDate.year < 1940:
        return print("please enter a birth year after 1939")
    elif age >= 65 and birthDate.year < 1943:
        return calculateSSIncome(True, monthlyPay, age = 65)
    elif age >= 66 and birthDate.year <= 1954:
        return calculateSSIncome(True, monthlyPay, age = 66)
    elif age >= 66.16 and birthDate.year < 1957:
        return calculateSSIncome(True, monthlyPay, age = 65.16)
    elif age >= 66.33 and birthDate.year < 1958:
        return calculateSSIncome(True, monthlyPay, age = 65.33)
    elif age >= 66.5 and birthDate.year < 1960:
        return calculateSSIncome(True, monthlyPay, age = 66.5)
    elif age >= 67 and birthDate.year >= 1960:
        return calculateSSIncome(True, monthlyPay, age = 67)
    else:
        return calculateSSIncome(False, monthlyPay, age)

def calculateSSIncome(bool, monthlyPay, age): # if True calculate and display monthly retirement amount/ if False calculate retirement date and retirement amount

    monthlyPay = ssiCalculator(monthlyPay)

    if bool == True:
        print(f"You are eligible to collect SSI as of age {age} and the monthly rate will be ${monthlyPay}")
    else:
        eligAge = calculateAge(None, age)
        print(f"You are not eligibile to collect SSI until {eligAge} and the monthly rate will be ${monthlyPay}")

def ssiCalculator(monthlyPay): # this function takes monthly pay as an argument and calculates the appropriate monthly SSI payment based on if current monthly payment falls within range

    if monthlyPay < 996:
        monthlyPay = .90 * monthlyPay

        return monthlyPay
    
    elif monthlyPay > 996 and  monthlyPay <= 6002:
        
        firstBend = 996 * .90
        monthlyPay = monthlyPay - 996
        secondBend = monthlyPay * .32

        return secondBend + firstBend

    elif monthlyPay > 6002:

        firstBend = 996 * .90
        monthlyPay = monthlyPay - 996
        secondBend = monthlyPay * .32
        monthlyPay = (monthlyPay + 996) - 6002
        thirdBend = monthlyPay * .15

        return thirdBend + secondBend + firstBend

def calculateAge(birthDate, age): # calculates age and eligibility age for ineligible applicants
    if age == None: # calculates user age from days into years and returns the value
        daysInYear = 365.2425   
        age = int((dt.today() - birthDate).days / daysInYear)
        return age
    else: # calculates user eligibility age from birth year and returns the value
        year = int(dt.today().year) - age
        if year < 1943:
            return 65
        elif year > 1943 and year < 1954:
            return 66
        elif year < 1957:
            return 66.16
        elif year < 1958:
            return 66.33
        elif year < 1960:
            return 66.5
        else:
            return 67

def userInput(): # collect user input and store in variables 

    birthDate = pyinp.inputDate("Please enter your date of birth in numerical form month, day, year (XX/XX/XXXX): ")
    monthlyPay = pyinp.inputInt("Please enter your current monthly income (round to the nearest dollar): ", min= 0)
    checkRetireAge(birthDate, monthlyPay)

if __name__ == "__main__":
    userInput()