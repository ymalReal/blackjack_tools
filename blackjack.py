#!/bin/python3

from deck import Deck

class Player:

    def __init__(self, deck, starting_money):
        self.deck = deck
        self.money = starting_money
        self.hand = []

    def __repr__(self):
        return "Player: hand|%s, money|%s" % (self.hand, self.money)

    def start_hand(self):
        self.hand = []
        self.hand.append(self.deck.pull_card())
        self.hand.append(self.deck.pull_card())
    
    def hit(self, hand=None):
        if hand == None:
            hand = self.hand
        new_card = self.deck.pull_card()
        print('%s pulls %s' % (self.__class__.__name__, new_card))
        self.hand.append(new_card)

    def show_hand(self, hand=None):
        if hand == None:
            hand = self.hand
        hand_value = 0
        aces = 0
        is_soft = False

        print("Cards in %s's hand: " % self.__class__.__name__)
        for card in self.hand:
            print(card)
            hand_value += card.val
            if card.name == 'A':
                aces += 1
        while aces > 0:
            if hand_value <= 11:
                hand_value += 10
                is_soft = True
            aces -= 1
        print("Value: %s%s" % (hand_value, ' (soft)' if is_soft else ''))

class Dealer(Player):
    
    def __init__(self, deck):
        self.deck = deck
        self.hand = []

def play():
    print("Fuck off")

def status():
    print("Fuck off")

if __name__=='__main__':
    player = Player(Deck().shuffle(), 1000)
    player.start_hand()
    print(player)
    for i in range(5):
        player.show_hand()
        player.hit()
    player.show_hand()

