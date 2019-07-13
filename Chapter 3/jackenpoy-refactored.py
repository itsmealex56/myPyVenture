# ROCK, PAPER, SCISSORS
# Passed down from the ancient Chinese Han dynasty, the game 
# shoushiling is now better known as Rock, Paper, Scissors.
# This code implements a version of the game that is you against
# the computer.

# Here we're doing some setup by importing the random module 
# and setting up the winner variable.

import random

winner = ''

# The computer randomly chooses rock, paper, scissors by 
# generating a random number from 0 to 2 and then mapping that 
# to a corresponding string.

random_choice = random.randint(0,2)

if random_choice == 0:
    computer_choice = 'rock'
elif random_choice == 1:
    computer_choice = 'paper'
else:
    computer_choice = 'scissors'

# Get the user's choice with a simple validation input statement

my_choice = ''
while (my_choice != 'rock' and 
       my_choice != 'paper' and 
       my_choice != 'scissors'):
    my_choice = input('Rock, Paper, or Scissors? ')


# Here's our game logic, which checks to see if the computer wins
# (or not), and makes the appropriate change to the winner variable.
    
if computer_choice == my_choice:
    winner = 'Tie'
elif computer_choice == 'rock' and my_choice == 'scissors':
    winner = 'Computer'
elif computer_choice == 'paper' and my_choice == 'rock':
    winner = 'Computer'
elif computer_choice == 'scissors' and my_choice =='paper':
    winner = 'Computer'
else:
    winner = 'User'


# Here we announce the game was a tie, or the winner along 
# with the computer's choice

if winner == 'Tie':
    print('Both tied! Computer also chose '+ computer_choice)
else:
    print('The', winner,'wins! the computer chose '+ computer_choice)