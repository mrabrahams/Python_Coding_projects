#########################################################
# Module #2 Programming Assignment #1                   #
# Dwight Abrahams                                       #
# Python Essentials                                     #
# August 20 2021                                        #
#########################################################

# print the below to output
"""
1. Prompt the user for the amount of the meal (e.g. $32.95).
2. Compute the tax on the restaurant bill. The tax should be 6.75 percent of the meal cost. 
3. Prompt the user for the tip amount (Suggesting a value equal to 18 percent of the total).
Display the meal cost, tax amount, tip amount, and total bill on the screen.
"""

# take user input on meal price
mealPrice = float(input("Please enter the total amount of your meal: "))
# calculate tax, total with tax, and tip
tax = .0675 * mealPrice
total = tax + mealPrice
tip = .18
suggestedTip = tip * total

# receive tip amount from user and combine with total
userTip = float(input("How much would you like to tip (%18 = "+ str(round(suggestedTip, 2)) + ")? "))
mealTotal = total + userTip

# display the meal cost, tax amount, tip amount, and total
print("meal cost = $" + str(mealPrice))
print("tax amount = $" + str(round(tax,2)))
print("tip amount = $" + str(round(userTip,2)))
print("total = $" + str(round(mealTotal,2)))