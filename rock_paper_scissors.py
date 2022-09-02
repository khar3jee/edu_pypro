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
x figure out intent
x refactor code-blob into functions of one concern
    x interface
    x user choice
    x computer choice
    x comparison and result
    draw paper vs paper
    win paper beats rock or rock beats scissors
    lose scissors beats paper or paper beats rock
"""

import random

# options made constants as the options shouldn't change
OPTIONS = ['rock', 'paper', 'scissors']


def main():
    """presents menu and calls other functions"""
    game_menu()
    human_choice = get_human_choice()
    computer_choice = get_computer_choice()
    print_choices(human_choice, computer_choice)
    print_results(human_choice, computer_choice)

def game_menu():
    """prints player choices"""
    print('Welcome to a game of Rock, Paper, Scissors:')
    for i in range(len(OPTIONS)):
        print(f'{i+1}. {OPTIONS[i]}')

def get_human_choice():
    """takes user input"""
    return OPTIONS[int(input('Enter the number of your choice: ')) - 1]

def get_computer_choice():
    """generates a random choice for the computer"""
    return random.choice(OPTIONS)
    
def print_choices(human_choice, computer_choice):
    """Prints selected choices"""
    print(f'You chose {human_choice}')
    print(f'The computer chose {computer_choice}')

def comparison(human_choice, computer_choice, computer_wins, computer_loses):
    """compares player inputs and returns game results"""
    if computer_choice == computer_wins:
        print(f'Sorry, {computer_choice} beats {human_choice}')
    elif computer_choice == computer_loses:
        print(f'Yes, {human_choice} beats {computer_choice}')

def print_results(human_choice, computer_choice):
    """prints game results"""
    if human_choice == computer_choice:
        print('Draw!')

    if human_choice == 'rock':
        comparison(human_choice, computer_choice, 'paper', 'scissors')
    elif human_choice == 'paper':
        comparison(human_choice, computer_choice, 'scissors', 'rock')
    elif human_choice == 'scissors':
        comparison(human_choice, computer_choice, 'rock', 'paper')
 
if __name__ == '__main__':
    main()
