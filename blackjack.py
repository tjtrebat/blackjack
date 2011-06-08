__author__ = 'Tom'

from Tkinter import *
from cards import *

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
    def __init__(self, root, deck, images):
        self.root = root
        self.deck = deck
        self.images = images

    def add_menu(self):
        menu = Menu(self.root)
        file_menu = Menu(menu, tearoff=0)
        file_menu.add_command(label="New Game", command=self.new_game)
        menu.add_cascade(label="File", menu=file_menu)
        self.root.config(menu=menu)

    def new_game(self):
        self.my_cards = BlackjackHand()
        self.dealer_cards = BlackjackHand()
        self.my_frame.destroy()
        self.dealer_frame.destroy()
        self.my_frame = Frame(self.table)
        self.my_frame.pack(side='bottom')
        self.dealer_frame = Frame(self.table)
        self.dealer_frame.pack(side='top')
        for i in range(2):
            self.deal_card(self.my_frame, self.my_cards)
            self.deal_card(self.dealer_frame, self.dealer_cards)
        print self
        
    def add_table(self):
        self.root.title("Blackjack")
        background = PhotoImage(file="blackjack-table-layout.gif")
        self.root.geometry("%dx%d+0+0" % (background.width(), background.height()))
        self.table = Label(self.root, image=background)
        self.table.photo = background
        self.table.pack(side='top', fill='both', expand='yes')
        self.my_frame = Frame(self.table)
        self.my_frame.pack(side='bottom')
        self.dealer_frame = Frame(self.table)
        self.dealer_frame.pack(side='top')
        
    def deal_card(self, frame, hand):
        card = self.deck.cards.pop()
        image = self.images[len(self.deck.cards)]
        label = Label(frame, image=image)
        label.image = image
        label.pack(side='left')
        hand.add(card)

    def __str__(self):
        s = "Dealer Hand (%s): %s\n" % (str(self.dealer_cards.get_total()), str(self.dealer_cards))
        s += "My Hand (%s): %s\n" % (str(self.my_cards.get_total()), str(self.my_cards))
        return s

if __name__ == "__main__":
    root = Tk()
    root.resizable(0, 0)
    deck = Deck(count=2)
    images = [PhotoImage(file=card.get_image()) for card in deck.cards]
    blackjack = Blackjack(root, deck, images)
    blackjack.add_table()
    blackjack.add_menu()
    blackjack.new_game()
    root.mainloop()