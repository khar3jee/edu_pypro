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
    - user choice
    - computer choice
    - comparison and result
    draw paper vs paper
    win paper beats rock
    loss scissors beats paper
"""

import random

# options made constants as the options shouldn't change
OPTIONS = ['rock', 'paper', 'scissors']


def main():
    """presents menu and calls other functions"""
    game_menu()
    print(comparison(get_human_choice(),get_computer_choice()))

def game_menu():
    """prints player choices"""
    print('Welcome to a game Rock, Paper, Scissors:\
        \n(1) Rock \n(2) Paper\n(3) Scissors')

def get_human_choice():
    """takes user input"""
    human_choice = OPTIONS[int(input('Enter the number of your choice: ')) - 1]
    print(f'You chose {human_choice}')
    return human_choice

def get_computer_choice():
    """generates a random choice for the computer"""
    computer_choice = random.choice(OPTIONS)
    print(f'The computer chose {computer_choice}')
    return computer_choice

def comparison(human_choice, computer_choice):
    """compares player inputs and returns game results"""
    if human_choice == computer_choice:
        return 'Draw!'
    elif human_choice == 'rock':
        if computer_choice == 'paper':
            return 'Sorry, paper beat rock'
        elif computer_choice == 'scissors':
            return 'Yes, rock beat scissors!'
    elif human_choice == 'paper':
        if computer_choice == 'scissors':
            return 'Sorry scissors beat paper'
        elif computer_choice == 'rock':
            return 'Yes, paper beat rock!'
    elif human_choice == 'scissors':
        if computer_choice == 'rock':
            return 'Sorry rock beat scissors'
        elif computer_choice == 'paper':
            return 'Yes, scissors beat paper!'

if __name__ == '__main__':
    main()