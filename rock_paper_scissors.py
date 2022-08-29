"""
Simple terminal-based Rock, Paper, Scissors game

My notes:
Goal: Refactor into functions which only do one thing

What is the intent (besides refactor)?
- input
- comparison
    - win
    - lose
    - draw
- response
TODO
- figure out intent
- refactor code-blob into functions of one concern
    - interface
    - user input
    - computer choice
    - comparison
    - response
"""

import random

# options made constants as the options shouldn't change
OPTIONS = ['rock', 'paper', 'scissors']

def main():
    """presents menu and calls other functions"""
    print('Welcome to a game Rock, Paper, Scissors:\
    \n(1) Rock \n(2) Paper\n(3) Scissors')
    print(human_choice('Enter the number of your choice: '))
    

def human_choice(user_input):
    """takes user input"""
    human_choice = OPTIONS[int(input(user_input)) - 1]
    return f'You chose {human_choice}'

def computer_choice():
    """generates a random choice for the computer"""
    computer_choice = random.choice(OPTIONS)
    return f'The computer chose {computer_choice}'

if human_choice == 'rock':
    if computer_choice == 'paper':
        print('Sorry, paper beat rock')
    elif computer_choice == 'scissors':
        print('Yes, rock beat scissors!')
    else:
        print('Draw!')
elif human_choice == 'paper':
    if computer_choice == 'scissors':
        print('Sorry scissors beat paper')
    elif computer_choice == 'rock':
        print('Yes, paper beat rock!')
    else:
        print('Draw!')
elif human_choice == 'scissors':
    if computer_choice == 'rock':
        print('Sorry rock beat scissors')
    elif computer_choice == 'paper':
        print('Yes, scissors beat paper!')
    else:
        print('Draw!')

if __name__ == '__main__':
    main()