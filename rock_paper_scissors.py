"""
Simple terminal-based Rock, Paper, Scissors game

My notes:
Goal: Refactor functions into class

TODO
x add class
x refactor attributes
x refactor any methods to call each other correctly
x add init method and attributes
"""

import random

# options made constants as the options shouldn't change
OPTIONS = ['rock', 'paper', 'scissors']

class RpsGame():
    """Simple terminal-based Rock, Paper, Scissors game"""

    def __init__(self):
        self.human_choice = None
        self.computer_choice = None
        
    def main(self):
        """presents menu and calls other functions"""
        self.game_menu()
        self.get_human_choice()
        self.get_computer_choice()
        self.print_choices(self.human_choice, self.computer_choice)
        self.print_results(self.human_choice, self.computer_choice)

    def game_menu(self):
        """prints player choices"""
        print('Welcome to a game of Rock, Paper, Scissors:')
        for i in range(len(OPTIONS)):
            print(f'{i+1}. {OPTIONS[i]}')

    def get_human_choice(self):
        """takes user input"""
        self.human_choice = OPTIONS[int(\
            input('Enter the number of your choice: ')) - 1]

    def get_computer_choice(self):
        """generates a random choice for the computer"""
        self.computer_choice = random.choice(OPTIONS)

    def print_choices(self, human_choice, computer_choice):
        """Prints selected choices"""
        print(f'You chose {human_choice}')
        print(f'The computer chose {computer_choice}')

    def comparison(self, human_choice, computer_choice,
    computer_wins, computer_loses):
        """compares player inputs and returns game results"""
        if computer_choice == computer_wins:
            print(f'Sorry, {computer_choice} beats {human_choice}')
        elif computer_choice == computer_loses:
            print(f'Yes, {human_choice} beats {computer_choice}')

    def print_results(self, human_choice, computer_choice):
        """prints game results"""
        if human_choice == computer_choice:
            print('Draw!')

        if human_choice == 'rock':
            self.comparison(human_choice, computer_choice, 'paper', 'scissors')
        elif human_choice == 'paper':
            self.comparison(human_choice, computer_choice, 'scissors', 'rock')
        elif human_choice == 'scissors':
            self.comparison(human_choice, computer_choice, 'rock', 'paper')

if __name__ == '__main__':
    rps = RpsGame()
    rps.main()
