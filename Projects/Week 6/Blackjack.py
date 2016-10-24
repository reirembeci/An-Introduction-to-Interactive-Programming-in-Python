# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = []
        pass	# create Hand object

    def __str__(self):
        result = ""
        for c in range(0, len(self.cards)):
            result += self.cards[c].suit + self.cards[c].rank + " "
        return "Hand contains" + " " + result	# return a string representation of a hand

    def add_card(self, card):
        self.cards.append(card)
        pass	# add a card object to a hand

    def get_value(self):
        value = 0
        ace = False
        for c in range(0, len(self.cards)):
            value += VALUES[self.cards[c].rank]
            if self.cards[c].rank == "A":
                ace = True
        if ace and value + 11 <= 21:
            value += 10
        return value
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        pass	# compute the value of the hand, see Blackjack video
    
    def busted(self):
        if self.get_value() > 21:
            return True
        else:
            return False
        
    def draw(self, canvas, pos):
        for c in range (1, len(self.cards)):
            self.cards[c].draw(canvas, [pos[0] + CARD_CENTER[0] + c * (30 + CARD_SIZE[0]), pos[1] + CARD_CENTER[1]])
        
# define deck class 
class Deck:
    def __init__(self):
        self.cards = [Card(SUITS[i], RANKS[j]) for i in range (0, len(SUITS)) for j in range (0, len(RANKS))]
    # create a Deck object

    def shuffle(self):
        self.__init__()
        random.shuffle(self.cards)
        # shuffle the deck 
        pass    # use random.shuffle()

    def deal_card(self):
        card_dealt = self.cards.pop(0)
        return card_dealt
        # deal a card object from the deck
    
    def __str__(self):
        result = ""
        for c in range (0, len(self.cards)):
            result += self.cards[c].suit + self.cards[c].rank + " "
        return "Deck contains" + " " + result
        # return a string representing the deck



#define event handlers for buttons
def deal():
    global outcome, in_play, card_deck, player, dealer, score, outcome
    
    card_deck = Deck()
    card_deck.shuffle()
    outcome = ""
    
    player = Hand()
    player.add_card(card_deck.deal_card())
    player.add_card(card_deck.deal_card())
    
    dealer = Hand()
    dealer.add_card(card_deck.deal_card())
    dealer.add_card(card_deck.deal_card())
    
    if in_play:
        outcome = "You lose"
        score -= 1
# your code goes here
    
    in_play = True

def hit():
    global in_play, value, score, outcome
    # replace with your code below
 
    # if the hand is in play, hit the player
    
    if in_play:
        player.add_card(card_deck.deal_card())
   
    # if busted, assign a message to outcome, update in_play and score
    
        if player.busted():
            outcome = "You have been busted"
            score -= 1
            in_play = False
       
def stand():
    global in_play, score, outcome
    pass	# replace with your code below
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    
    if in_play:
        while dealer.get_value() < 17:
            dealer.add_card(card_deck.deal_card())

    # assign a message to outcome, update in_play and score
    
        if player.busted():
            outcome = "You have been busted!"
        else:
            if dealer.busted():
                outcome = "Dealer has been busted!"
                score += 1
            elif dealer.get_value() < player.get_value():
                outcome = "You win!"
                score += 1
            else:
                outcome = "You lose!"
                score -= 1
        in_play = False

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    global in_play, outcome
    
    canvas.draw_text("Blackjack", [100, 100], 40, "Red")
    canvas.draw_text("Dealer", [90, 180], 30, "Black")
    canvas.draw_text("Score " + str(score), [400, 100], 30, "Black")
    canvas.draw_text(outcome, [300, 180], 30, "Black")
    
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [60 + CARD_BACK_SIZE[0], 170 + CARD_BACK_SIZE[1]], CARD_SIZE)
    else:
        dealer.cards[0].draw(canvas, [60 + CARD_CENTER[0], 170 + CARD_CENTER[1]])
        
    dealer.draw(canvas, [60, 170])
    canvas.draw_text("Player", [80, 370], 25, "Black")
    
    if in_play:
        canvas.draw_text("Hit or stand?", [200, 370], 25, "Black")
    else:
        canvas.draw_text("New deal?", [200, 370], 25, "Black")
    
    player.cards[0].draw(canvas, [60 + CARD_CENTER[0], 370 + CARD_CENTER[1]])
    player.draw(canvas, [60, 370])
    
    
#    card = Card("S", "A")
#    card.draw(canvas, [300, 300])


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric