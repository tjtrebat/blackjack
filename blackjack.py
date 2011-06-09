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
    def __init__(self):
        self.deck = Deck(count=2)
        self.deck.shuffle()
        self.my_hand = BlackjackHand()
        self.dealer_hand = BlackjackHand()

    def deal_card(self, hand):
        if len(self.deck.cards):
            hand.add(self.deck.cards.pop())

    def __str__(self):
        s = "Dealer Hand (%d): %s\n" % (self.dealer_hand.get_total(), str(self.dealer_hand))
        s += "My Hand (%d): %s\n" % (self.my_hand.get_total(), str(self.my_hand))
        return s

class BlackjackGUI:
    def __init__(self, root, blackjack):
        self.root = root
        self.root.title("Blackjack")
        self.blackjack = blackjack
        self.background = PhotoImage(file="blackjack-table-layout.gif")
        self.root.geometry("%dx%d+0+0" % (self.background.width(), self.background.height()))
        self.add_table()
        self.add_buttons()
        self.add_frames()
        self.images = {}
        self.labels = {}
        for card in self.blackjack.deck.cards:
            self.images[card] = PhotoImage(file=card.get_image())
        self.face_down_card = Card(None, None)
        self.images[self.face_down_card] = PhotoImage(file='cards/b1fv.gif')
        self.add_menu()

    def new_game(self):
        self.my_frame.destroy()
        self.dealer_frame.destroy()
        self.add_frames()
        if len(self.blackjack.deck) < 25:
            self.blackjack = Blackjack()
        else:
            self.blackjack.my_hand.cards = []
            self.blackjack.dealer_hand.cards = []
        for i in range(2):
            self.blackjack.deal_card(self.blackjack.my_hand)
            self.deal(self.my_frame, self.blackjack.my_hand.cards[i])
            self.blackjack.deal_card(self.blackjack.dealer_hand)
            if i < 1:
                self.deal(self.dealer_frame, self.blackjack.dealer_hand.cards[i])
            else:
                self.deal(self.dealer_frame, self.face_down_card)
        print self.blackjack

    def deal(self, frame, card):
        self.labels[card] = Label(frame, image=self.images[card])
        self.labels[card].photo = self.images[card]
        self.labels[card].pack(side='left')

    def hit_me(self):
        self.blackjack.deal_card(self.blackjack.my_hand)
        self.deal(self.my_frame, self.blackjack.my_hand.cards[-1])

    def stand(self):
        pass

    def add_table(self):
        self.table = Canvas(self.root)
        self.table.create_image(0, 0, image=self.background, anchor="nw")
        self.table.pack(side='top', fill='both', expand='yes')

    def add_frames(self):
        self.my_frame = Frame(self.table)
        self.my_frame.pack(side='bottom')
        self.dealer_frame = Frame(self.table)
        self.dealer_frame.pack(side='top')

    def add_buttons(self):
        self.buttons = Frame(self.table)
        self.buttons.pack(side='bottom', pady=10)
        self.hit_button = Button(self.buttons, text='Hit', command=self.hit_me)
        self.hit_button.pack(side='left')
        self.stand_button = Button(self.buttons, text='Stand', command=self.stand)
        self.stand_button.pack(side='right')

    def add_menu(self):
        menu = Menu(self.root)
        file_menu = Menu(menu, tearoff=0)
        file_menu.add_command(label="New Game", command=self.new_game)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=quit)
        menu.add_cascade(label="File", menu=file_menu)
        self.root.config(menu=menu)

if __name__ == "__main__":
    root = Tk()
    root.resizable(0, 0)
    gui = BlackjackGUI(root, Blackjack())
    gui.new_game()
    root.mainloop()