#!/usr/bin/python3

import random as r

suits = ['spade', 'heart', 'club', 'diamond']
cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
card_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
card_vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

class Card:
    def __init__(self):
        self.suit = r.choice(suit)
        index = r.choice(range(len(cards)))
        self.name = cards[index]
        self.num = card_nums[index]
        self.val = card_vals[index]

    def __init__(self, suit, card_num):
        if suit not in suits:
            raise NameError("'%s' is not a valid suit" % suit)
        self.suit = suit
        if isinstance(card_num, str):
            if card_num not in cards:
                raise NameError("'%s' is not a valid card name" % card_num)
            index = cards.index(card_num)
            self.name = cards[index]
            self.num = card_nums[index]
            self.val = card_vals[index]
        else:
            if card_num > 13 or card_num < 1:
                raise NameError("'%s' is not a valid card number" % card_num)
            self.name = cards[card_num]
            self.num = card_nums[card_num]
            self.val = card_vals[card_num]

    def __str__(self):
        return self.show_card()

    def __repr__(self):
        return "Card: (%s, %s)" % (self.suit, self.name)
    
    def show_card(self):
        return "%s of %ss" % (self.name, self.suit)


class Deck:

    def __init__(self):
        self.cards = []
        self.number_cards = 0
        self.cards_left = self.number_cards
        for suit in suits:
            for card in cards:
                self.cards.append(Card(suit, card))
        self.number_cards = len(self.cards)
        self.cards_left = self.number_cards

    def __repr__(self):
        return "Deck: " + str(self.cards)

    def __str__(self):
        return str(self.cards)

    def pull_card(self):
        return self.cards.pop()

    def mix(self):
        r.shuffle(self.cards)
        return self

    def shuffle(self):
        self.cards = []
        self.number_cards = 0
        self.cards_left = self.number_cards
        self.__init__()
        r.shuffle(self.cards)
        return self


if __name__ == '__main__':
    myDeck = Deck()
    print(myDeck)
    print(myDeck.mix())
    print(myDeck.pull_card())
    print(myDeck.pull_card())
    print(myDeck.mix())
    print(myDeck.shuffle())
