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

# helper functions

def number_to_name(number):
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        return 'Error'

    
def name_to_number(name):
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    else:
        return 'Error'


def rpsls(name): 
    player_number = name_to_number(name)
    
    import random
    comp_number = random.randrange(0, 5)
    
    (player_number - comp_number) % 5 
 
    if (player_number - comp_number) % 5 > 2:
        result = 'Computer wins!'
    elif  (player_number - comp_number) % 5 == 0 :
        result = 'Tie!'
    else:
        result = 'Player wins!'    
   
    name1 = number_to_name(comp_number)

    print ""
    print "Player chooses " + name
    print "Computer chooses " + name1
    print result

    
    
# test
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")



