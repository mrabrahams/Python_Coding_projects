###################################################################
# Program Name: card_game.py                                      #
# Module #1 Programming Assignment #1                             #
# Dwight Abrahams                                                 #
# Python Essentials                                               #
# Septemeber 29 2021                                              #
# Purpose: This is the beginning of creating a more sophisticated #
#           card game.                                            #
###################################################################

'''
This is the beginning of creating a more sophisticated card game. Create a module for a card game. 

The module should :

    define an immutable collection (tuple) of card faces (ace, deuce ... king). Add three more faces of your own choosing (e.g. prince, knight, etc.).
    define an immutable collection (tuple) of card suits (diamonds, hearts, spades, clubs). Add two more suits of your own choosing (e.g. moons, stars, etc.).
    Create a collection (i.e. a deck of cards) consisting of one card of each face/suit. The cards should be immutable, but the deck should not (i.e. a list).
    "Deal" a hand of seven cards to a player. The cards selected should be selected randomly for each hand and be removed from the deck as they are dealt.
    Determine the value of each hand based on the accumulated value of the cards in the hand (number cards are worth their numeric value, face cards 
    (jack, queen, king) are worth 10 (assign whatever value you want to the faces you created).
    When the game is finished, the cards should be returned to the deck and prompt the user if they wish to play again.
'''

if __name__ == "__main__":
    userInput()