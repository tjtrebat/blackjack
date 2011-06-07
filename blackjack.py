__author__ = 'Tom'

import random
from Tkinter import *

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.image = 'cards/%s.gif' % (self.suit[0].lower() + self.rank[0].lower(),)

    def __str__(self):
        return "%s of %ss" % (self.rank, self.suit)

class Deck:
    def __init__(self):
        self.cards = self.get_cards()

    def get_cards(self):
        cards = []
        for rank in range(2, 11) + ["Jack", "Queen", "King", "Ace"]:
            for suit in ("Spade", "Heart", "Diamond", "Club"):
                cards.append(Card(str(rank), suit))
        random.shuffle(cards)
        return cards

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        return ",".join([str(card) for card in self.cards])

class Hand:
    def __init__(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def __str__(self):
        return ",".join([str(card) for card in self.cards])

class Blackjack:
    def __init__(self, root):
        self.root = root
        self.deck = Deck()
        self.my_cards = Hand()
        self.dealer_cards = Hand()
        self.add_background()
        self.new_game()
        print self
        
    def add_background(self):
        self.root.title("Blackjack")
        background = PhotoImage(file="blackjack-table-layout.gif")
        self.root.geometry("%dx%d+0+0" % (background.width(), background.height()))
        label = Label(self.root, image=background)
        label.photo = background
        label.pack(side='top', fill='both', expand='yes')
        
    def new_game(self):
        for i in range(2):
            self.my_cards.add(self.deck.cards.pop())
            self.dealer_cards.add(self.deck.cards.pop())

    def __str__(self):
        s = "My Hand: " + str(self.my_cards)
        s += "\nDealer Hand: " + str(self.dealer_cards)
        return s

if __name__ == "__main__":
    root = Tk()
    blackjack = Blackjack(root)
    root.mainloop()
