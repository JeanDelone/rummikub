from player import *

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

def print_board(board):
    print("____Start Board____")
    for group in board:
        print("____________________")
        for card in group:
            print(card)
    print("____End Board____")

print(group_validation(valid_test_1)) #True
print(group_validation(valid_test_2)) #True
print(group_validation(valid_test_3)) #False
print(group_validation(valid_test_4)) #False
print(group_validation(valid_test_5)) #True
print(group_validation(valid_test_6)) #True
print(group_validation(valid_test_7)) #False
