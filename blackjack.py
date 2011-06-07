__author__ = 'Tom'

import random
from Tkinter import *

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.image = self.get_card_image()
        
    def get_card_image(self):
        try:
            rank = int(self.rank)
        except ValueError:
            rank = self.rank[0].lower() 
        return 'cards/%s.gif' % (self.suit[0].lower() + str(rank),)

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

class Hand(object):
    def __init__(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def __str__(self):
        return ",".join([str(card) for card in self.cards])
        
class BlackjackHand(Hand):
    def __init__(self):
        super(BlackjackHand, self).__init__()
        
    def get_total(self):
        total = 0
        has_ace = False
        for card in self.cards:     
            try:
                value = int(card.rank)
            except ValueError:
                if card.rank == "Ace":
                    value = 11
                    has_ace = True
                else:
                    value = 10
            total += value
            if total > 21 and has_ace:
                total -= 10
                has_ace = False
        return total
            
    def is_bust(self):
        if self.get_total() > 21:
            return True
        return False

class Blackjack:
    def __init__(self, root):
        self.root = root
        self.deck = Deck()
        self.table = self.add_background()
        self.my_cards = BlackjackHand()
        self.dealer_cards = BlackjackHand()
        self.new_game()
        print self
        
    def new_game(self):
        #self.my_frame.destroy()
        for i in range(2):
            my_card = self.deck.cards.pop()
            self.deal_card(PhotoImage(file=my_card.image))
            self.my_cards.add(my_card)
            dealer_card = self.deck.cards.pop()
            self.deal_card(PhotoImage(file=dealer_card.image))
            self.dealer_cards.add(dealer_card)
        
    def add_background(self):
        self.root.title("Blackjack")
        background = PhotoImage(file="blackjack-table-layout.gif")
        self.root.geometry("%dx%d+0+0" % (background.width(), background.height()))
        label = Label(self.root, image=background)
        label.photo = background
        label.pack(side='top', fill='both', expand='yes')
        return label
        
    def deal_card(self, image, **kwargs):
        card_label = Label(self.table, image=image)
        card_label.photo = image
        card_label.pack(**kwargs)        

    def __str__(self):
        s = "My Hand (%s): %s" % (str(self.my_cards.get_total()), str(self.my_cards))
        s += "\nDealer Hand (%s): %s" % (str(self.dealer_cards.get_total()), str(self.dealer_cards))
        return s

if __name__ == "__main__":
    root = Tk()
    blackjack = Blackjack(root)
    root.mainloop()
