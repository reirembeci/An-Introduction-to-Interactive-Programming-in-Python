# template for "Stopwatch: The Game"
import simplegui

# define global variables
width = 300
height = 300
interval = 100
time = int()
count = 0
succes = 0


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global time
    time = int(t)
    A = time // 600
    B = time / 10 % 60 / 10
    C = (time / 10) % 60 % 10
    D = time % 600 % 10
    return str(A)+ ":" + str(B) + str(C) + "." + str(D)
    pass
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    timer.start()
  
    
def stop_handler():
    global count
    global succes
    
        
    if timer.is_running():
        if (time % 600 % 10) == 0:
            succes += 1
            count +=1 
        else:
            count +=1 
        timer.stop()
    else:
        ""      
        
def reset_handler():
    global time
    global count
    global succes
    
    time = 0
    count = 0
    succes = 0
    timer.stop()
    
    

# define event handler for timer with 0.1 sec interval

def tick():
    global interval
    global time
    time += 1
   


# define draw handler
def draw(canvas):
    text1 = str(succes) + "/" + str(count) 
    canvas.draw_text(format(time), [150, 150], 24, "White")
    canvas.draw_text(text1, [230, 30], 24, "White")

    
# create frame
frame = simplegui.create_frame("Stopwatch", width, height)

# register event handlers
frame.set_draw_handler(draw)
button1 = frame.add_button('Start', start_handler, 200)
button2 = frame.add_button('Stop', stop_handler, 200)
button3 = frame.add_button('Reset', reset_handler, 200)
timer = simplegui.create_timer(interval, tick)


# start frame
frame.start()


# Please remember to review the grading rubric
