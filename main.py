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

# Checks if subgroup of cards has copy in existing list of cards, used in checking all the permutations
def has_copy_in_list(group, list):
    group = sorted(group, key = lambda x: x.color)
    for element in list:
        if sorted(element, key = lambda x: x.color) == group:
            return True
    return False
# Simply connects all the subboards to make it into 1
def make_one_big_board(board):
    one_board = []
    for subboard in board:
        for element in subboard:
            one_board.append(element)
    return one_board
initial_big_board = make_one_big_board(test_board_69)
list_of_all_sets = []

"""
All code below this comment is not yet finished and currently tested

Currently I'm testing function that would make all possible subgroups out of the given board

"""





# Used in the process of making sets, returned set doesn't have to be valid
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
        if (element.number - 1) == set[-1].number:
            return True
        else:
            return False
    if element.color != set[0].color:
        return False

# Used in the process of making groups with same numbers, doesn't have to be valid 
def element_for_colorset_validation(element, set):
    if len(set) == 0:
        return True
    if element.color == set[0].color:
        return False
    if element.color != set[0].color:
        for card in set:
            if card.color == element.color:
                return False
            if card.number != element.number:
                return False
        return True

def all_sets(board, starting_card = 0):
    if len(board) >= starting_card + 1:
        board = sorted(board, key = lambda x: x.number)
        new_list = []
        new_list.append(board[starting_card])
        board.pop(starting_card)
        for card in board:
            if element_for_set_validation(card, new_list):
                new_list.append(card)
            if group_validation(new_list):
                if not has_copy_in_list(new_list, list_of_all_sets):
                    list_of_all_sets.append(new_list.copy())
        all_sets(initial_big_board, starting_card + 1)

def all_colors(board, starting_card = 0):
    if len(board) >= starting_card + 1:
        board = sorted(board, key = lambda x: x.number)
        new_list = []
        new_list.append(board[starting_card])
        board.pop(starting_card)
        for card in board:
            if element_for_colorset_validation(card, new_list):
                new_list.append(card)
            if group_validation(new_list):
                if not has_copy_in_list(new_list, list_of_all_sets):
                    list_of_all_sets.append(new_list.copy())
            
        all_colors(initial_big_board, starting_card + 1)


# def every_possible_subgroup():
#     all_possibilities = []
#     testing = make_one_big_board(test_board_69) 
#     all_colors(testing)
#     all_sets(testing)
#     return all_possibilities

