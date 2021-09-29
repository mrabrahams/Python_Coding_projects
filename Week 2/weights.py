#########################################################
# Module #2 Programming Assignment #2                   #
# Dwight Abrahams                                       #
# Python Essentials                                     #
# August 21 2021                                        #
#########################################################

# program that calculates user weight on other planets 
"""
Weight on Other Planet = Weight on Earth x Multiple of Earth’s Gravity

Design a Python program that asks a user for their name and weight. 
The program will greet the user by name and then calculate/display the user's weight on the other planets. 
Each item should be displayed on a line by itself.

Use the following values for the conversions
Body
	
Multiple of Earth’s Gravity
Sun         27.01
Mercury     0.38
Venus       0.91
Earth       1 (defined)
Moon        0.166
Mars        0.38
Jupiter     2.34
Saturn      1.06
Uranus      0.92
Neptune     1.19
Pluto       0.06
"""

# take in users name and weight then provide a greeting
name = input("What is your name? ")
weight = int(input("What is your weight? "))
print("Hello " + name + " I will now calculate your weight if you were on other stellar bodies...")

# calculate weight entered and convert into weight on other stellar bodies; store information in dictionary
stellarBodies = {
    "Body":     "Weight",
    "Sun":      round(weight * 27.01, 2), 
    "Mercury":  round(weight * 0.38, 2),
    "Venus":    round(weight * 0.91, 2),
    "Earth":    round(weight * 1, 2),
    "Moon":     round(weight * 0.166, 2),
    "Jupiter":  round(weight * 2.34, 2),
    "Saturn":   round(weight * 1.06, 2),
    "Uranus":   round(weight * 0.92, 2),
    "Neptune":  round(weight * 1.19, 2),
    "Pluto":    round(weight * 0.06, 2)
    }


# iterate through dictionary and print results to screen
for key in stellarBodies:
    print(key, "-->", stellarBodies[key])