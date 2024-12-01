#Написать функцию которая возвращают случайным образом одну карту из стандартной колоды в 36 карт,
# где на первом месте номинал карты номинал (6 - 10, J, D, K, A),
# а на втором название масти (Hearts, Diamonds, Clubs, Spades).
import random
def give_random_card():
    ranks = ['6', '7', '8', '9', '10', 'J', 'D', 'K', 'A']   #номиналы
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']        #масти

    rank = random.choice(ranks)
    suit = random.choice(suits)

    return f"{rank} of {suit}"

random_card = give_random_card()
print(random_card)

