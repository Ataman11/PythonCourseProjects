# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random
import simplegui

# initialize global variables used in your code
secret = 0
n_of_guesses = 0
range_high = 100


# helper function to start and restart the game
def new_game():
    global range_high, secret, n_of_guesses
    secret = generate_secret(0, range_high + 1)
    if range_high == 100:
        n_of_guesses = 7
    else:
        n_of_guesses = 10
        
    print "New Game. Number of guesses remaining:", n_of_guesses, " Range:", range_high

def generate_secret(low, high):
    return random.randrange(low, high + 1)
    
# define event handlers for control panel
def range100():
    global range_high
    # button that changes range to range [0,100) and restarts
    range_high = 100
    new_game()
    

def range1000():
    global range_high
    # button that changes range to range [0,1000) and restarts
    range_high = 1000
    new_game()
    
    
def input_guess(guess):
    global range_high, secret, n_of_guesses 
    # main game logic goes here	
    n = int(guess)
    print "Your guess:", n
    if n < secret:
        print "Higher!"
    elif n > secret:
        print "Lower!"
    else:
        print "Correct!"
        print "You won!"
        new_game()
    
    n_of_guesses = n_of_guesses - 1
    print "Number of guesses left:", n_of_guesses
    if n_of_guesses == 0:
        print "You lost."
        new_game()
    
    
# create frame
frame = simplegui.create_frame("Guess the number!",300,300)

# register event handlers for control elements
frame.add_input("Enter your guess", input_guess, 100)
frame.add_button("Range 0-100", range100, 100)
frame.add_button("Range 0-1000", range1000, 100)

# call new_game and start frame
random.seed()
new_game()
frame.start()


# always remember to check your completed program against the grading rubric
