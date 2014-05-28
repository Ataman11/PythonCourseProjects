# implementation of card game - Memory

import simplegui
import random

list_1 = range(0, 8)
list_2 = range(0, 8)
deck_list = list_1 + list_2
position = [0, 70]
exposed = []
counter = 0
first_index = 0
second_index = 0

# helper function to initialize globals
def new_game():
    global game_state, exposed, counter
    random.shuffle(deck_list)
    game_state = 0
    counter = 0
    exposed = []
    for i in range(len(deck_list)):
        exposed.append(False)   
     
# define event handlers
def mouseclick(position):
    # add game game_state logic here
    global game_state, first_index, second_index, counter
    i = position[0] // 50
    if game_state == 0:
        if exposed[i] == False:
            exposed[i] = True
            game_state = 1
            first_index = i
            counter += 1
    elif game_state == 1:
        if exposed[i] == False:
            exposed[i] = True
            game_state = 2
            second_index = i
    elif game_state == 2:
        if deck_list[first_index] != deck_list[second_index]:
            exposed[first_index] = False
            exposed[second_index] = False  
        if exposed[i] == False:
            exposed[i] = True
            game_state = 1
            first_index = i
            counter += 1
                
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global position, exposed
    label.set_text("Turns = " + str(counter))
    position = [12, 70]
    for i in range(len(deck_list)):
        if exposed[i] == False:
            canvas.draw_line((position[0] + 13, 0), (position[0] + 13, 100), 49, "Green")
        else:
            canvas.draw_text(str(deck_list[i]), position, 52, "Red")
        position[0] += 50

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric