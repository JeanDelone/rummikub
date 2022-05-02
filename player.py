from cards import *

class Player:
    def __init__(self, number, cards:list):
        self.number = number
        self.cards = sorted(cards, key=lambda x: x.number)
        self.can_play = False

    # Function that puts cards from hand to their valid position on board if possible
    def put_possible_cards_on_ends(self, board):
        # First function checks for numbers
        cards_to_remove_from_hand = []
        for card in self.cards:
            for board_group in board:
                if board_group[0].color == board_group[-1].color and board_group[0].color == card.color:
                    if (card.number - 1) == board_group[-1].number:
                        board_group.append(card)
                        cards_to_remove_from_hand.append(card)
                        break
                    elif (card.number + 1) == board_group[0].number:
                        board_group.insert(0, card)
                        cards_to_remove_from_hand.append(card)
                        break
        for card in cards_to_remove_from_hand:
            self.cards.remove(card)

        # Second function checks for colors
        cards_to_remove_from_hand = []
        for board_group in board:
            for card in self.cards:
                if board_group[0].color != board_group[-1].color:
                    if card.number == board_group[0].number and len(board_group) == 3:
                        if card.color != board_group[0] and card.color != board_group[1] and card.color != board_group[2]:
                            board_group.append(card)
                            cards_to_remove_from_hand.append(card)
        for card in cards_to_remove_from_hand:
            self.cards.remove(card)

    # def backtrack(self,board):
    #     board_without_breakdowns = []
    #     for set in board:
    #         for element in set:
    #             board_without_breakdowns.append(element)

    # Print hands, to help visualize if functions are working correctly, it's here currently for testing
    def print_hand(self):
        print("____Start Hand____")
        for card in self.cards:
            print(card)
        print("____End Hand____")