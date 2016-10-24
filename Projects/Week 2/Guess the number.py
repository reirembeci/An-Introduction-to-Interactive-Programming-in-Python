# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# initialize global variables used in your code

num_range = 100
secret_number = random.randrange(0, 100)
num_guesses = int(math.ceil(math.log(100, 2)))

# helper function to start and restart the game
def new_game():
    global num_guesses
    global num_range
    secret_number = random.randrange(0, num_range)
    if num_range == 100:
        num_guesses = int(math.ceil(math.log(100, 2)))
    elif num_range == 1000:
        num_guesses = int(math.ceil(math.log(1000, 2)))
    print "New game. Range is from 0 to", num_range
    print "Number of remaining guesses is ", num_guesses
    print 
    pass



# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    secret_number = random.randrange(0, 100)
    num_range = 100
    new_game()  
    pass

def range1000():
    # button that changes range to range [0,1000) and restarts
    global num_range
    global secret_number
    num_range = 1000
    secret_number = random.randrange(0, 1000)
    new_game()  
    pass
    
def input_guess(guess):
    # main game logic goes here	
    global num_guesses
    player_guess = int(guess)
    num_guesses = num_guesses - 1
    if num_guesses > 0:
        print "Guess was", player_guess
        print "Number of remaining guesses is", num_guesses
        if player_guess > secret_number:
            print "Your guess is higher"
            print           
        elif player_guess < secret_number:
            print "Your guess is lower"
            print           
        else: 
            print "You found the secret number!"
            print
            new_game()  
    else:
        print "You ran out of guesses"
        print "The secret number was", secret_number 
        print
        new_game()
    
# create frame

frame = simplegui.create_frame("Guess the number" , 200, 200)

# register event handlers for control elements

frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Enter a guess", input_guess, 200)


# call new_game and start frame

new_game()

# always remember to check your completed program against the grading rubric
