from board import *

board1 = Board(test_board_69)
board1.all_possible_subboards()
board1.solvexd(board1.possible_subboards)
print(board1.list_of_all_possibilities)
print(len(board1.list_of_all_possibilities))