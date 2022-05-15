class Card:
    def __init__(self, color, number, is_first = True):
        self.color = color
        self.number = number
        self.is_first = is_first

    def __str__(self):
        return f"color: {self.color}, number: {self.number}"

    def __eq__(self, other):
        return self.color == other.color and self.number == other.number




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

test_board_69 = [
    [Card(BLACK, 1), Card(BLUE, 1), Card(RED, 1)],
    [Card(BLACK, 2), Card(BLUE, 2), Card(RED, 2)],
    [Card(BLACK, 3), Card(BLUE, 3), Card(RED, 3)],
    [Card(BLACK, 4), Card(BLACK, 5), Card(BLACK, 6)]
]

test_board_70 = [
    [Card(RED, 1), Card(RED, 2), Card(RED, 3), Card(RED, 4), Card(RED, 5)]
]

really_big_board = [
    [Card(BLACK, 1), Card(BLUE , 1), Card(YELLOW, 1)],
    [Card(RED, 13), Card(BLUE , 13), Card(YELLOW, 13)],
    [Card(BLACK, 10), Card(BLUE , 10), Card(YELLOW, 10)],
    [Card(BLACK, 11), Card(BLUE , 11), Card(YELLOW, 11), Card(RED, 11)],
    [Card(YELLOW, 1), Card(YELLOW , 2), Card(YELLOW, 3)],
    [Card(BLUE,5), Card(BLUE , 6), Card(BLUE, 7), Card(BLUE, 8), Card(BLUE, 9)],
    [Card(BLUE,2), Card(BLUE , 3), Card(BLUE, 4), Card(BLUE, 5, False)],
    [Card(BLUE,9), Card(BLUE , 10), Card(BLUE, 11), Card(BLUE, 12)],
    [Card(BLUE,2), Card(BLUE , 3), Card(BLUE, 4)],
    [Card(BLACK,4), Card(BLACK , 5), Card(BLACK, 6), Card(BLACK, 7)],
    [Card(YELLOW,6), Card(YELLOW , 7), Card(YELLOW,8), Card(YELLOW, 9)],
    [Card(YELLOW,9,False), Card(YELLOW , 10, False), Card(YELLOW,11), Card(YELLOW, 12), Card(YELLOW, 13, False)],
    [Card(BLACK,7), Card(BLACK , 8), Card(BLACK, 9)],
    [Card(RED,7), Card(RED ,8), Card(RED, 9)],
    [Card(RED,1), Card(RED , 2), Card(RED, 3)],
    [Card(BLACK,2), Card(BLACK , 3), Card(BLACK, 4, False)]
]

valid_test_1 = [Card(RED, 1), Card(BLACK, 1), Card(YELLOW, 1)]
valid_test_2 = [Card(RED, 1), Card(BLACK, 1), Card(YELLOW, 1), Card(BLUE, 1)]
valid_test_3 = [Card(RED, 1), Card(BLACK, 1), Card(RED, 1), Card(BLUE, 1)]
valid_test_4 = [Card(RED, 1), Card(BLACK, 2), Card(YELLOW, 3)]
valid_test_5 = [Card(RED, 1), Card(RED, 2), Card(RED, 3)]
valid_test_6 = [Card(BLACK,5), Card(BLACK, 6), Card(BLACK, 7), Card(BLACK,8), Card(BLACK,9)]
valid_test_7 = [Card(BLACK,5), Card(BLACK, 6), Card(BLUE, 7), Card(BLACK,8), Card(BLACK,9)]
