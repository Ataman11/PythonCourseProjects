# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random

# helper functions

def name_to_number(name):
    # delete the follwing pass statement and fill in your code below
    # convert name to number using if/elif/else
    # don't forget to return the result!
    
    # 0 - rock
    if name == "rock": return 0
    # 1 - Spock
    elif name == "Spock": return 1
    # 2 - paper
    elif name == "paper": return 2
    # 3 - lizard
    elif name == "lizard": return 3
    # 4 - scissors
    elif name == "scissors": return 4
    
    else: print "Wrong input in name_to_number: ", name
    


def number_to_name(number):
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    
    # 0 - rock
    if number == 0: return "rock" 
    # 1 - Spock
    elif number == 1: return "Spock"
    # 2 - paper
    elif number == 2: return "paper"
    # 3 - lizard
    elif number == 3: return "lizard"
    # 4 - scissors
    elif number == 4: return "scissors"
    
    else: print "Wrong input in number_to_name: ", number
    

def rpsls(player_choice): 
    # print a blank line to separate consecutive games
    print " "
    
    # print out the message for the player's choice
    print "Player choses " + player_choice # + " " + str(number_player)
    
    # convert the player's choice to player_number using the function name_to_number()
    number_player = name_to_number(player_choice)
    
    # compute random guess for comp_number using random.randrange()
    number_computer = random.randrange(0,5)
    
    # convert comp_number to comp_choice using the function number_to_name()
    computer_choice = number_to_name(number_computer)
    
    # print out the message for computer's choice
    print "Computer choses " + computer_choice # + " " + str(number_computer)
    
    # compute difference of comp_number and player_number modulo five
    difference = (number_player - number_computer) % 5
    # print difference
    # use if/elif/else to determine winner, print winner message
    if (difference == 1 or difference == 2): print "Player wins!"
    elif difference > 2: print "Computer wins!"
    else: print "Player and computer tie!"

# test your code - LEAVE THESE CALLS IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


