class Card:
    def __init__(self, color, number):
        self.color = color
        self.number = number

    def __str__(self):
        return f"color: {self.color}, number: {self.number}"

RED = "RED"
BLACK = "BLACK"
YELLOW = "YELLOW"
BLUE = "BLUE"
colors = [RED, BLACK, YELLOW, BLUE]

test_hand_1 = [Card(RED,6), Card(BLACK,5), Card(BLUE,10), Card(YELLOW,13), Card(RED,6)]
test_hand_2 = [Card(RED,6), Card(YELLOW,2), Card(BLUE,5), Card(YELLOW,5)]
test_hand_3 = [Card(BLACK,3), Card(YELLOW,2), Card(BLUE,5), Card(YELLOW,5)]
test_hand_4 = [Card(BLACK, 3), Card(BLACK, 4), Card(BLACK, 8), Card(RED, 1), Card(RED, 1), Card(BLUE, 7)]

test_board_1 = [
    [Card(RED,3), Card(RED,3), Card(RED,5)],
    [Card(BLUE,6), Card(BLUE,7), Card(BLUE,8), Card(BLUE,9)],
    [Card(BLACK,6), Card(BLACK,7), Card(BLACK,8), Card(BLACK,9)]
]

test_board_2 = [
    [Card(RED,3), Card(RED,4), Card(RED,5)],
    [Card(BLUE,6), Card(BLUE,7), Card(BLUE,8), Card(BLUE,9)],
    [Card(BLACK,6), Card(BLACK,7), Card(BLACK,8), Card(BLACK,9)],
    [Card(YELLOW,1), Card(YELLOW,2), Card(YELLOW,3), Card(YELLOW,4), Card(YELLOW,5), Card(YELLOW,6), Card(YELLOW,7), Card(YELLOW,8), Card(YELLOW,9)]
]

test_board_3 = [
    [Card(RED,3), Card(YELLOW,3), Card(BLUE,3)],
    [Card(BLUE,6), Card(BLUE,7), Card(BLUE,8), Card(BLUE,9)],
    [Card(BLACK,6), Card(BLACK,7), Card(BLACK,8), Card(BLACK,9)]
]

test_board_4 = [
    [Card(BLACK, 5), Card(BLACK, 6), Card(BLACK, 7), Card(BLACK, 8), Card(BLACK, 9), Card(BLACK, 10)],
    [Card(RED, 7), Card(BLACK, 7), Card(YELLOW, 7)],
    [Card(BLACK, 1), Card(YELLOW, 1), Card(BLUE, 1)],
    [Card(RED, 2), Card(RED, 3), Card(RED, 4)]
]