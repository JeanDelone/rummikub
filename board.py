from player import *

# Board class will be dynamically changed during program's lifetime
# It will dynamically add cards, and have all possible subboards of cards on the board

class Board:
    def __init__(self, board:list):
        self.__board = board
        self.initial_board = []
        self.list_of_all_possibilities = []
        self.possible_subboards = []
    """
    ____________ Start of helper funcions ____________________
    """

    # Just make one board from sublists in big board
    def __make_one_big_board(self):
        self.initial_board = []
        for subboard in self.__board:
            for element in subboard:
                self.initial_board.append(element)
        self.initial_board = sorted(self.initial_board, key=lambda x: x.number)
    
    def __big_board(self, board):
        big_board = []
        for list in board:
            for element in list:
                big_board.append(element)
        return big_board
        

    # Function that checks if given group is valid so it can be put on the board
    def __group_validation(self, group):
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
    def __can_element_be_added_to_group(self, element, subgroup):
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

    # Used in the process of making num_sets, returned set doesn't have to be valid
    def __element_for_set_validation(self, element, set):
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
    
    # Used in the process of making color_sets, returned set doesn't have to be valid
    def __element_for_colorset_validation(self, element, set):
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

    # Checks if subgroup of cards has copy in existing list of cards, used in checking all the permutations
    def __has_copy_in_list(self, group, list):
        group = sorted(group, key = lambda x: x.color)
        for element in list:
            if sorted(element, key = lambda x: x.color) == group:
                return True
        return False

    # Function that add every possible num_set to the list
    def __all_sets(self, initial_board, starting_card = 0):
        if len(initial_board) >= starting_card + 1:
            new_list = []
            new_list.append(initial_board[starting_card])
            initial_board.pop(starting_card)
            for card in initial_board:
                if self.__element_for_set_validation(card, new_list):
                    new_list.append(card)
                if self.__group_validation(new_list):
                    if not self.__has_copy_in_list(new_list, self.possible_subboards):
                        self.possible_subboards.append(new_list.copy())
            self.__all_sets(self.initial_board.copy(), starting_card + 1)

    # Function that add every possible color_set to the list
    # starting_card is a pointer. It goes through every card in given board and tries to arrange all possibilities with that card       
    def __all_colorsets(self, initial_board, starting_card = 0):
        # Check if given board
        if len(initial_board) >= starting_card + 1:
            new_list = []
            new_list.append(initial_board[starting_card])
            initial_board.pop(starting_card)
            for card in initial_board:
                if self.__element_for_colorset_validation(card, new_list):
                    new_list.append(card)
                if self.__group_validation(new_list):
                    if not self.__has_copy_in_list(new_list, self.possible_subboards):
                        self.possible_subboards.append(new_list.copy())
                
            self.__all_colorsets(self.initial_board.copy(), starting_card + 1)

    """
        ____________ End of helper funcions ____________________
    """

    # Combines everything, changes all possible subboards
    def all_possible_subboards(self):
        self.possible_subboards = []
        self.__make_one_big_board()
        self.__all_colorsets(self.initial_board.copy())
        self.__make_one_big_board()
        self.__all_sets(self.initial_board.copy())

    # Not fully developped yet
    def print_board(self):
        print("____Start Board____")
        for group in self.possible_subboards:
            print("____________________")
            for card in group:
                print(card)
        print(f"____End Board____\nPossible outcomes: {len(self.possible_subboards)}")
    
    def __print_board(self, board):
        print("____Start Board____")
        for group in board:
            print("____________________")
            for card in group:
                print(card)
        print(f"____End Board____")


    """
    ______________ Maintaining the board _______________
    """
    def add_set_to_board(self, set):
        self.__board.append(set)

    """
    ___________ End of maintaining the board ___________
    """


    # Code below is in the testing phase, doesnt work properly yet
    # The only thing that doesn't work is going back to make other solutions, it removes 
    
    def solvexd(self, current_leftovers, current_try_list = []):

        initial_copy_of_leftovers = current_leftovers.copy()

        for element in initial_copy_of_leftovers:
            copy_of_leftovers = initial_copy_of_leftovers.copy()
            current_try_list.append(element)
            temporary_removal_list = []

            for card in element:
                for leftover in copy_of_leftovers:
                    if card in leftover:
                        temporary_removal_list.append(leftover)

            for element in temporary_removal_list:
                if element in copy_of_leftovers:
                    copy_of_leftovers.remove(element)

            
            if len(self.__big_board(current_try_list)) == len(self.initial_board):
                self.list_of_all_possibilities.append(current_try_list)
            # self.__print_board(current_leftovers)
            # self.__print_board(current_try_list)
            self.solvexd(copy_of_leftovers.copy(), current_try_list.copy())


    def solvexdd(self, initial_list, current_try_list = []):
        n = 1
        for list in initial_list:
            print(f"Iteration: {n}")
            n += 1
            current_try_list.append(list)
            temporary_removal_list = []
            initial_copy = initial_list.copy()
            for element in list:
                for sublist in initial_copy:
                    if element in sublist:
                        temporary_removal_list.append(sublist)
            for element in temporary_removal_list:
                print(f"Trying to remove {element} \nfrom\n {initial_copy}")
                print("\n\n\n")
                initial_copy.remove(element)
            if len(self.__big_board(current_try_list)) == len(self.initial_board):
                self.list_of_all_possibilities.append(current_try_list)
            # self.solvexdd(initial_copy, current_try_list)