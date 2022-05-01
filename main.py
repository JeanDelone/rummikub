import random

class Card:

    def __init__(self, color, number):
        self.color = color
        self.number = number

    def __str__(self):
        return f"color: {self.color}, number: {self.number}"


my_hand = []
deck = []

# RED = (255,255,255)
# BLACK = (0,0,0)
# YELLOW = (0,255,255)
# BLUE = (0,0,255)
RED = "RED"
BLACK = "BLACK"
YELLOW = "YELLOW"
BLUE = "BLUE"
colors = [RED, BLACK, YELLOW, BLUE]

test_hand_1 = [Card(RED,6), Card(BLACK,5), Card(BLUE,10), Card(YELLOW,13), Card(RED,6)]
test_hand_2 = [Card(RED,6), Card(YELLOW,2), Card(BLUE,5), Card(YELLOW,5)]

test_board_1 = [
    [Card(RED,3), Card(RED,4), Card(RED,5)],
    [Card(BLUE,6), Card(BLUE,7), Card(BLUE,8), Card(BLUE,9)],
    [Card(BLACK,6), Card(BLACK,7), Card(BLACK,8), Card(BLACK,9)]
]

test_board_2 = [
    [Card(RED,3), Card(RED,4), Card(RED,5)],
    [Card(BLUE,6), Card(BLUE,7), Card(BLUE,8), Card(BLUE,9)],
    [Card(BLACK,6), Card(BLACK,7), Card(BLACK,8), Card(BLACK,9)],
    [Card(YELLOW,1), Card(YELLOW,2), Card(YELLOW,3), Card(YELLOW,4), Card(YELLOW,5), Card(YELLOW,6), Card(YELLOW,7), Card(YELLOW,8), Card(YELLOW,9)]
]



def put_cards_at_the_existing_sides(hand, board):
    cards_to_remove_from_hand = []
    for hand_card in hand:
        for board_group in board:
            if board_group[0].color == board_group[-1].color and board_group[0].color == hand_card.color:
                if (hand_card.number - 1) == board_group[-1].number:
                    board_group.append(hand_card)
                    cards_to_remove_from_hand.append(hand_card)
                    break
                elif (hand_card.number + 1) == board_group[0].number:
                    board_group.insert(0, hand_card)
                    cards_to_remove_from_hand.append(hand_card)
                    break
    for card in cards_to_remove_from_hand:
        hand.remove(card)


#Create whole deck
for _ in range(2):
    #These are 2 jokers
    deck.append(Card(0,0))
    for color in colors:
        for j in range(13):
            deck.append(Card(color,j))

#Random 14 cards from deck moved to hand
def start_draw(hand):
    for _ in range(14):
        hand.append(deck.pop(random.randint(0, len(deck) -1 )))

# print(test_board)
def print_board(board):
    print("____Start Board____")
    for group in board:
        print("____________________")
        for card in group:
            print(card)
    print("____End Board____")

def print_hand(hand):
    print("____Start Hand____")
    for card in hand:
        print(card)
    print("____End Hand____")


