import random

random_choice = random.randint(0,2)

if random_choice == 0:
    computer_choice = 'rock'
elif random_choice == 1:
    computer_choice = 'paper'
else:
    computer_choice = 'scissors'

my_choice = input('Rock, Paper, or Scissors? ')
while my_choice != "":
    if my_choice == 'rock':
        if computer_choice == 'scissors':
            print('You chose rock and computer chose scissors...You won')
        elif computer_choice == 'rock':
            print('You chose rock and computer chose rock...You are both tied')
        else:
            print('You chose rock and computer chose paper...You lose')
    elif my_choice == 'paper':
        if computer_choice == 'scissors':
            print('You chose paper and computer chose scissors...You lose')
        elif computer_choice == 'rock':
            print('You chose paper and computer chose rock...You won')
        else:
            print('You chose paper and computer chose paper...You are both tied')
    else:
        if computer_choice == 'scissors':
            print('You chose scissors and computer chose scissors...You are both tied')
        elif computer_choice == 'rock':
            print('You chose scissors and computer chose rock...You lose')
        else:
            print('You chose scissors and computer chose paper...You won')


    print('Computer has pick', computer_choice)
