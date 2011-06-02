__author__ = 'Tom'

import random
from Tkinter import *

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.image = 'cards/%s.gif' % (self.suit[0].lower() + self.rank,)

    def __str__(self):
        return "%s of %ss" % (self.rank, self.suit)

class Deck:
    def __init__(self):
        self.cards = self.get_cards()

    def get_cards(self):
        cards = []
        for rank in range(2, 11) + ["J", "Q", "K", "A"]:
            for suit in ("Spade", "Heart", "Diamond", "Club"):
                cards.append(Card(str(rank), suit))
        return cards

    def __str__(self):
        return ",".join([str(card) for card in self.cards])

class Blackjack:
    def __init__(self, root):
        root.title("Blackjack")
        self.deck = Deck()
        background = PhotoImage(file="blackjack-table-layout.gif")
        root.geometry("%dx%d+0+0" % (background.width(), background.height()))
        label = Label(root, image=background)
        label.photo = background
        label.pack(side='top', fill='both', expand='yes')
        Label(label, text="Hello World").pack()

if __name__ == "__main__":
    root = Tk()
    blackjack = Blackjack(root)
    root.mainloop()
