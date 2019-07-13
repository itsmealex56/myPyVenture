import random

winner = ''

random_choice = random.randint(0,2)

if random_choice == 0:
    computer_choice = 'rock'
elif random_choice == 1:
    computer_choice = 'paper'
else:
    computer_choice = 'scissors'

my_choice = ''
while (my_choice != 'rock' and 
       my_choice != 'paper' and 
       my_choice != 'scissors'):
    my_choice = input('Rock, Paper, or Scissors? ')

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

if winner == 'Tie':
    print('Both tied! Computer also chose '+ computer_choice)
else:
    print('The', winner,'wins! the computer chose '+ computer_choice)