###################################################################
# Program Name: stereo.py                                   #
# Module #2 Programming Assignment #3                             #
# Dwight Abrahams                                                 #
# Python Essentials                                               #
# Octoberber 10 2021                                              #
# Purpose: This is the creation of a stereo class and the use of  #
#           constructors.                                         #
###################################################################

'''
Stereo

Create a StereoReceiver class. The attributes for the StereoReceiver are:

    Manufacturer 
    Model
    Serial Number
    Band (AM/FM)
    Frequency (i.e. ‘station’)
    Volume (0-10)
    Power (i.e. On/Off)
    Two other attributes of your own choosing

Create a constructor/initializer for the class that receives a Manufacturer, Model, and Serial Number. 
The constructor should set the attributes provided and also initialize any other attributes (e.g. power = off, volume = 0, band, frequency, etc.)

Provide separate Accessor/Get Methods that will return Manufacturer, Model, Serial Number, Band, Frequency, Volume, and Power.

Provide separate Mutator/Set Methods that will allow a user to turn the receiver on/off, change the volume, change the band, set the frequency/station, etc.

Provide Accessor/Mutator methods for the attributes you provided as appropriate.

Provide a string (__str__) method that will allow you to display the attributes of the receiver in a nicely formatted string.

Create a main program that utilizes the StereoReceiver class:

    Prompt the user for the Manufacturer, Model, Serial Number, Wattage,, and Number of Channels
    Create an object for the StereoReceiver.
        Catch any exceptions thrown due to invalid/omitted parameters
    Using the Accessor Methods, display the StereoReciever’s information (manufacturer, model, etc.).
    Turn on the StereoReceiver using the appropriate method.
    Allow the user to change/set the band, frequency, and volume. Handle any exceptions caused by invalid data (should be raised in the appropriate functions).
    Allow the user to change any of the attributes you created (appropriately)
    Display the StereoReceiver’s settings using the accessor methods (power, band, station, and volume)
    Turn off the StereoReceiver.
    Display the StereoReceiver using the string method.
'''

if __name__ == "__main__":
    userInput()