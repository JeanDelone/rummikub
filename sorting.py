from main import *
from player import *
from cards import *

# ------ OTHER FUNCTIONS ------ 

#Function that reduces the board, by getting rid of empty lists.
def reduce_board(board):
    reduced_board = [board_group for board_group in board if board_group != []]
    return reduced_board


# ------ COLOR SORTING ------ 

# //jakiś tam pierwowzór, nieważny, bo nie tworzył setów   
#Function that sorts group by color and returns a new board.     
def sort_hand_by_colors(hand):

    #Creating new list for sorted group with 4 lists inside - each for one color
    cards_sorted_colors = [[], [], [], []] 

    #Sorting cards by number and color
    hand.sort(key = lambda card:card.number)
    hand.sort(key = lambda card:card.color)
    
    #Inserting cards
    for card in hand: 
        for board_group in cards_sorted_colors:
            #if a group is empty, the card will be inserted 
            if not board_group: 
                board_group.append(card)
                break
            else:
                #if the group is not empty inserting a card at the begging or at the end
                if board_group[-1].color == card.color:
                    if card.number >= (board_group[-1].number):
                        board_group.append(card)
                        break
                    elif card.number <= (board_group[0].number):
                        board_group.insert(0, card)
                        break 

    #reducing the board
    cards_sorted_colors = reduce_board(cards_sorted_colors)

    return cards_sorted_colors

#Sorting hand by colors and creating groups, returns new group
def create_sets_sorted_colors(group):

    group.sort(key = lambda card:(card.color,card.number))
    groups_sorted = [[]]

    #For each card we are checking whether we can insert it in existing subgroup;
    for card in group:

        # We are checking whether for each subgroup we could insert a card, if not - we insert it in new, empty subgrup 
        for subgroup in groups_sorted:

            if len(subgroup) == 0:
                subgroup.append(card)
                groups_sorted.append([])
                break

            else:
                if subgroup[0].color == card.color and subgroup[-1].number == (card.number-1):
                    subgroup.append(card)
                    break



    
    groups_sorted = reduce_board(groups_sorted)

    return groups_sorted

# ------ NUMBER SORTING ----- 

#Function that sorts hand by numbers and creates possible sets, returns new group  
def create_sets_sorted_numbers(group):

    group.sort(key = lambda card:(card.number))
    groups_sorted = [[]]

    #For each card we are checking whether we can insert it in existing subgroup; if not - we create seperate subgroup
    for card in group: 

        for subgroup in groups_sorted:

            if len(subgroup) == 0: 
                subgroup.append(card)
                groups_sorted.append([])
                break

            else:

                if subgroup[0].number == card.number:

                    #For each element in subgroup we are checking whether it already has a card in that color
                    isIn = False
                    for element in subgroup:
                        if element.color == card.color:
                            isIn = True
                    if not isIn:
                        subgroup.append(card)
                        break
                else: 
                    continue     
    
    groups_sorted = reduce_board(groups_sorted)

    return groups_sorted


# ------------TESTS------------

test10 = [Card(YELLOW, 4),Card(YELLOW, 4),Card(YELLOW, 4),Card(RED, 4),Card(BLACK, 4),Card(BLACK, 4)]
# test colors doubled
# print_board(create_sets_sorted_numbers(test10))

test11 = [Card(BLACK, 4),Card(YELLOW, 4),Card(BLACK, 11),Card(BLACK, 3),Card(RED, 4),Card(BLUE, 1),Card(YELLOW, 10),Card(BLACK, 2)]
# print_board(create_sets_sorted_colors(test11)crere)

test12 = [Card(BLACK, 1),Card(BLACK, 2),Card(BLACK, 3),Card(BLACK, 4),Card(BLACK, 1),Card(BLACK,2),Card(BLACK, 3)]
#test dla kilku szeregów, ten sam kolor
#print_board(create_sets_sorted_colors(test12))

test13 = [Card(BLACK, 1),Card(YELLOW, 1),Card(BLACK, 2),Card(BLACK, 3),Card(BLUE, 10)]
# print_board(create_sets_sorted_colors(test13))


#-----------INNE, sprawdzałam coś, nie zwracaj uwagi-------------
def check_if_exist_plus_one (card, board):
    for card_board in board:
        if card.color == card_board.color and (card.number+1) == card_board.number:
            return True
    return False

def check_if_exist_other_colors (card, board):
    num = 0
    colors = []
    color_already_in = False
    for card_board in board:
        if card.color != card_board.color and card.number == card_board.number:
            if colors != []:
                for color in colors: 
                    if card_board.color == color:
                        color_already_in = True
            if not color_already_in:
                num+=1
                colors.append(card_board.color)
    if num >1: 
        return True
    else: 
        return False

