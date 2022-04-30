import random

class Card:

    def __init__(self, color, number):
        self.color = color
        self.number = number

    def __str__(self):
        return f"color: {self.color}, number: {self.number}"



def deck():
    deck.variable = []
    for _ in range(2):
        deck.append(Card(-1,-1))
        for i in range(4):
            for j in range(13):
                deck.append(Card(i,j))

my_hand = []
def start_draw(hand):
    for _ in range(14):
        hand.append(deck.pop(random.randint(0, len(deck) -1 )))
    

def can_start():
    pass

for element in deck:
    print(element)
print(len(deck))
