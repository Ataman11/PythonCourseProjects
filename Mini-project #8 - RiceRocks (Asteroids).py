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

    def draw(self, canvas, pos, draw_card_back):
        if draw_card_back == True:
            card_loc = CARD_BACK_CENTER
            canvas.draw_image(card_back, card_loc, CARD_BACK_SIZE, [pos[0] + CARD_BACK_CENTER[0], pos[1] + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)          	
        else:
            card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
            canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)       
        
# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.cards = []
               
    def __str__(self):
        # return a string representation of a hand
        list = ""
        for i in range(len(self.cards)):
            list += " " + str(self.cards[i])
        return "Hand contains" + list	

    def add_card(self, card):
        self.cards.append(card)
            # add a card object to a hand

    def get_value(self):
        # compute the value of the hand, see Blackjack video
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        value = 0
        has_ace = False
        for card in self.cards:
            if card.get_rank() == 'A':
                has_ace = True
            value += VALUES[card.get_rank()]      
        if has_ace == False:
            return value
        else:
            if value + 10 <= 21:
                return value + 10
            else:
                return value
        
    def draw(self, canvas, pos, dealer):
        # draw a hand on the canvas, use the draw method for cards
        for i in range(len(self.cards)):
            if dealer == True and i == 0:
                self.cards[i].draw(canvas, pos, True)
            else:
                self.cards[i].draw(canvas, pos, False)
            pos[0] += CARD_SIZE[0] + 15
        
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                card = Card(suit, rank) 
                self.cards.append(card)
                # create a Deck object
               
    def shuffle(self):
        # shuffle the deck 
        return random.shuffle(self.cards)    # use random.shuffle()
        

    def deal_card(self):
        return self.cards.pop(0) # deal a card object from the deck
    
    def __str__(self):
        list = ""
        for i in range(len(self.cards)):
            list += " " + str(self.cards[i])
        return "Deck contains" + list	# return a string representing the deck


#define event handlers for buttons
def deal():
    global outcome, in_play, deck, player_hand, dealer_hand, score
    deck = Deck()
    player_hand = Hand()
    dealer_hand = Hand()
    if in_play == True:
        outcome = "You lost. New deal: Hit or Stand?"
        score -= 1
    else:
        outcome  = "Hit or stand?"

    # your code goes here
    in_play = True
    deck.shuffle()
    player_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    print "Player: " + str(player_hand)
    print "Dealer: " + str(dealer_hand)
    

def hit():
    # replace with your code below
    # if the hand is in play, hit the player
    # if busted, assign a message to outcome, update in_play and score
    global outcome, in_play, deck, player_hand, dealer_hand, score
    if in_play == True:
        value = player_hand.get_value()
        if value <= 21:
            player_hand.add_card(deck.deal_card())
            value = player_hand.get_value()
        if value > 21:
            outcome = "You have busted. New deal?"
            in_play = False
            score -= 1
    print player_hand.get_value()
    print dealer_hand.get_value()

       
def stand():
    global outcome, in_play, deck, player_hand, dealer_hand, score
    # replace with your code below
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or mor
    # assign a message to outcome, update in_play and score
    if in_play == True:
        value = player_hand.get_value()
        in_play = False
        if value > 21:
            outcome = "You have busted. New deal?"
            score -= 1
        else:
            dealer_value = dealer_hand.get_value()
            while dealer_value <= 17:
                dealer_hand.add_card(deck.deal_card())
                dealer_value = dealer_hand.get_value()
            if dealer_value > 21:
                outcome = "Dealer has busted. New deal?"
                score += 1
            elif value <= dealer_value:
                outcome = "Dealer wins. New deal?"
                score -= 1
            else:
                outcome = "Player wins. New deal?"
                score += 1
        print value
        print dealer_value
# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text("Blackjack", [250, 50], 28, "Blue")
    canvas.draw_text(str(outcome), [50, 100], 24, "White")
    canvas.draw_text("Score " + str(score), [450, 100], 24, "Black")
    canvas.draw_text("Player", [50, 150], 22, "White")
    player_hand.draw(canvas, [50, 170], False)
    canvas.draw_text("Dealer", [50, 330], 22, "White")
    dealer_hand.draw(canvas, [50, 350], in_play)
    


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
random.seed()
deal()
frame.start()


# remember to review the gradic rubric