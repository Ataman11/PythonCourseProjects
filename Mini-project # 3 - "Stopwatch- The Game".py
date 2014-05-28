# template for "Stopwatch: The Game"

import simplegui

# define global variables
t = 0
wins = 0
tries = 0
is_timer_on = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    mins = t // 600
    secs = t // 10 % 60
    if secs < 10:
       secs = "0" + str(secs)
    tenths = t % 10
    return str(mins) + ":" + str(secs) + "." + str(tenths)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_timer():
    global is_timer_on
    timer.start()
    is_timer_on = True
    
def stop_timer():
    global wins, tries, is_timer_on
    if is_timer_on:
        tries += 1
        if t % 10 == 0:
            wins += 1
    timer.stop()
    is_timer_on = False

def reset_timer():
    global t, wins, tries
    t = 0
    timer.stop()
    wins = 0
    tries = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global t
    t += 1

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(t), [120, 100], 25, "White")
    canvas.draw_text(str(wins) + "/" + str(tries), [265, 30], 16, "White")
    
# create frame
f = simplegui.create_frame("Stopwatch Game", 300, 200)
f.add_button("Start", start_timer)
f.add_button("Stop", stop_timer)
f.add_button("Reset", reset_timer)
timer = simplegui.create_timer(100, timer_handler)

# register event handlers
f.set_draw_handler(draw_handler)

# start frame
f.start()

# Please remember to review the grading rubric
