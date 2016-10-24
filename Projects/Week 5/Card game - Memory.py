# implementation of card game - Memory

import simplegui
import random

turns = 0
exposed = []
state = 0
memory_deck = []

CARD_WIDTH = 50
CARD_HEIGHT = 100

# helper function to initialize globals
def new_game():
    global turns, exposed, state, memory_deck
    state = 0
    turns = 0
    memory_deck = [(i % 8) for i in range(0, 16)]
    exposed = [False for i in range(0, 16)]
    random.shuffle(memory_deck)
    label.set_text("Turns = 0")
    pass  

     
# define event handlers
def mouseclick(pos):
    global memory_deck, turns, exposed, state, value1, value2, card1, card2
    for i in range(16):
        if state == 0:
            if pos[0] <= (i * 50 + 50) and pos[0] > (i * 50) and not exposed[i]:
                
                exposed[i] = True
                value1 = memory_deck[i]
                card1 = i
                state = 1
                
        elif state == 1:
            if pos[0] <= (i * 50 + 50) and pos[0] > (i * 50) and not exposed[i]:
                
                exposed[i] = True
                value2 = memory_deck[i]
                card2 = i
                state = 2
                turns += 1
                label.set_text("Turns =" +str(turns))
                
        elif state == 2:
            if pos[0] <= (i * 50 + 50) and pos[0] > (i * 50) and not exposed[i]:
                
                if value1 != value2:
                    exposed[card1] = False
                    exposed[card2] = False
                    
                exposed[i] = True
                value1 = memory_deck[i]
                card1 = i
                state = 1
                
    pass
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for i in range(0, len(memory_deck)):
        if (exposed[i] == 0):
            canvas.draw_polygon([(CARD_WIDTH * i, 0),
                                 (CARD_WIDTH * (i + 1), 0), 
                                 (CARD_WIDTH * (i + 1), CARD_HEIGHT),
                                 (CARD_WIDTH * i, CARD_HEIGHT)], 3, "Blue","Red")
        else:
            canvas.draw_text(str (memory_deck [i]),
                             [CARD_WIDTH * i + 10, CARD_HEIGHT - CARD_WIDTH/2],
                             60,"Green")
    pass


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
