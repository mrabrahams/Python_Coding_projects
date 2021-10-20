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

import random as rndm

card_faces = ('Ace', 'Deuce', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Knight', 'Bishop', 'Dragon') # Tuple of faces

card_suits = ('Diamonds', 'Hearts', 'Spades', 'Clubs', 'Fire', 'Ice') # Tuple of suits

# Mapping points
points = {
        'Ace': 1,
        'Deuce': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'Jack': 10,
        'Queen': 10,
        'King': 10,
        'Knight': 9,
        'Bishop': 9,
        'Dragon': 12,
}


def print_card(card): # Printing a card
        print(f'{card[0]} of {card[1]}')

def init_deck(): # Creating a deck
        deck = []
        for suit in card_suits:
                for face in card_faces:
                        deck.append((face, suit))
        rndm.shuffle(deck) # Shuffling the deck
        return deck

def main():
        deck = init_deck()
        print("\n\nYour Hand")
        hand = []
        sum_points = 0
        for i in range(7): # Dealing required number of cards
                card = rndm.choice(deck)
                deck.remove(card) # remove card fro deck after being dealt
                print_card(card)
                sum_points = sum_points + points[card[0]]  # Adding points
        print(f"\nTotal Points: {sum_points}\n")
        choice = input("Would you like to play again? (y/n): ") # Asking if user wants to play again
        if choice.lower() == "y":
            main()

if __name__ == "__main__":
    main()