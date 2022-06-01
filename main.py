from board import *

board1 = Board(test_board_2)
board1.all_possible_subboards()
board1.solvexdd(board1.possible_subboards)
# print(board1.list_of_all_possibilities)
print(f"Inital board: {board1.initial_board}")
for element in board1.list_of_all_possibilities:
    print(element)
    print("\n")
print(len(board1.list_of_all_possibilities))

