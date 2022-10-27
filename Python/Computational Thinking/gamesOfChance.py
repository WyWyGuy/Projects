#Imports
import random

#Variables
cardDeck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King','Ace']
coin = ("Heads", "Tails")
    
#Randomize
random.shuffle(cardDeck)

#Find card
cardIndex = random.randrange(0, 13)
card = cardDeck[cardIndex]

#Prints
print(cardDeck)
print("Card at index {0} = {1}".format(cardIndex, card))

#Coin stuff
for i in range(0,5):
    flip = random.choice(coin)
    print("Coin-flip results:", flip)