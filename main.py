from player import *


def print_board(board):
    print("____Start Board____")
    for group in board:
        print("____________________")
        for card in group:
            print(card)
    print("____End Board____")

# Function that checks if given group is valid so it can be put on the board
def group_validation(group):
    # All groups must be at least 3 cards long, and cannot be longer than 13
    if len(group) < 3 or len(group) > 14:
        return False
    
    # If the colors are not matching, all of the numbers must be same, all colors must be different and subset cannot be longer than 4
    if group[0].color != group[-1].color:
        if len(group) > 4:
            return False
        # Checks if all numbers are the same
        for element in group:
            if element.number != group[0].number:
                return False
        # Checks if all colors are different
        colors_group = []
        for element in group:
            colors_group.append(element.color)
        if len(colors_group) != len(set(colors_group)):
            return False
        return True
    # If colors are matching, we check on every single color in group if it's the same, then we sort it by numbers and check if every single value is ascending exactly by 1 compared to value before that
    if group[0].color == group[-1].color:
        # Checks if all colors are the same, so basically set removes all duplicates, so there should be only 1 color in list
        colors_group = []
        for element in group:
            colors_group.append(element.color)
        if len(set(colors_group)) != 1:
            return False
        # sort group by numbers and check if they are ascending
        group.sort(key = lambda x: x.number)
        for i in range(0, len(group) - 1):
            if group[i].number + 1 != group[i+1].number:
                return False
        # By eliminating every possible outcome that would make group invalid, function returns True
        return True

# Function assumes, that subgroup is already valid group
def can_element_be_added_to_group(element, subgroup):
    if len(subgroup) == 0:
        return True
    if element.color == subgroup[0].color:
        # Check if all colors are the same
        for card in subgroup:
            if element.color != card.color:
                return False
        # sort group by numbers and check if element can be added at one of the 2 ends
        subgroup.sort(key = lambda x: x.number)
        if (element.number + 1) == subgroup[0].number or (element.number - 1) == subgroup[-1].number:
            return True
        else:
            return False
    if element.color != subgroup[0].color:
        # If at least once colors in the group are the same or numbers are different, it cannot be added
        for card in subgroup:
            if element.number != card.number:
                return False
            if element.color == card.color:
                return False
        return True

# Simply connects all the subboards to make it into 1
def make_one_big_board(board):
    one_board = []
    for subboard in board:
        for element in subboard:
            one_board.append(element)
    return one_board



"""
All code below this comment is not yet finished and currently tested

Currently I'm testing function that would make all possible subgroups out of the given board

"""

list_of_possible_colorsets = []
def make_possible_colorsets(board):
    if len(board) >= 3:
        possible_colorsets = []
        for card in board:
            if can_element_be_added_to_group(card, possible_colorsets):
                possible_colorsets.append(card)
                if group_validation(possible_colorsets):
                    list_of_possible_colorsets.append(possible_colorsets)
        list_of_possible_colorsets.append(possible_colorsets)
        board.pop(0)
        make_possible_colorsets(board)

initial_big_board = make_one_big_board(test_board_69)
def make_possible_sets(board, starting_card = 0):
    board = sorted(board, key = lambda x: x.number)
    if len(board) >= starting_card + 1:
        possible_sets = []
        possible_sets.append(board[starting_card])
        board.pop(starting_card)
        for card in board:
            if can_element_be_added_to_group(card, possible_sets):
                possible_sets.append(card)
                if group_validation(possible_sets):
                    list_of_possible_colorsets.append(card)
            list_of_possible_colorsets.append(possible_sets)
            make_possible_sets(initial_big_board, starting_card + 1)

# Used to validate sets
def element_for_set_validation(element, set):
    if len(set) == 0:
        return True
    if element.color == set[0].color:
        # Check if all colors are the same
        for card in set:
            if element.color != card.color:
                return False
        # sort group by numbers and check if element can be added at one of the 2 ends
        set.sort(key = lambda x: x.number)
        if (element.number + 1) == set[0].number or (element.number - 1) == set[-1].number:
            return True
        else:
            return False
    if element.color != set[0].color:
        return False


list_of_all_sets = []
def all_sets(board, starting_card = 0):
    if len(board) >= starting_card + 1:
        board = sorted(board, key = lambda x: x.number)
        new_list = []
        new_list.append(board[starting_card])
        board.pop(starting_card)
        for card in board:
            if can_element_be_added_to_group(card, new_list):
                new_list.append(card)
            if group_validation(new_list):
                list_of_all_sets.append(new_list)
        all_sets(initial_big_board, starting_card + 1)

group_to_remove = []
for group in list_of_possible_colorsets:
    if len(group) <= 2:
        group_to_remove.append(group)
for group in group_to_remove:
    list_of_possible_colorsets.remove(group)






testing = make_one_big_board(test_board_69) 

all_sets(testing)
# for group in list_of_possible_colorsets:
#     if len(group) <= 2:
#         group_to_remove.append(group)
# for group in group_to_remove:
#     list_of_possible_colorsets.remove(group)
print_board(list_of_all_sets)
