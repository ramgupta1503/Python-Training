# Random is a module pre-defined function which we can use to select random things
# from is a keyword in python that we can use when importing functions from a module but it allows to be a little bit more specific


# from random import choice 

# coin = choice(["heads", "tails"])
# print(coin)

import random

# coin = random.choice(["heads", "tails"])
# print(coin)


# number  = random.randint(1, 10)   # randint choose an integer in between 1 to 10
# print(number)

cards = ["Jack", "Queen", "King"]

random.shuffle(cards)
# print(cards)     # This prints the whole list but we want it to produce 1 by 1 so we use loop

for card in cards:
    print(card)