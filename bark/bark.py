"""
terminal-based bookmark app

app goal:
create, read, update and delete
bookmarks

TODO
-design structure:
database, TUI/menu, commands
bark(menu), commands(fetches & responds to user input), database(db functions)
-ensure bookmark object is:
ID, Title, URL, Notes, Date added
-can do:
CRUD, list, find by ID

Run prep step if needed
Pass return value from prep step if needed to execute method
Print result of execution
https://peps.python.org/pep-0440/
"""
import commands
from collections import OrderedDict

menu = []
class Menu():
    pass

class Option:
    def __init__(self, option_title, command, prep_call=None):
        self.option_title = option_title
        self.command = command
        self.prep_call = prep_call

    def choose(self):
        data = self.prep_call() if self.prep_call else None
        message = self.command.execute(data) if data else self.command.execute()

    def __str__(self):
        return self.option_title

def menu_loop():

    options = OrderedDict({
        'A': commands.AddBookmarkCommand(),
        'B': commands.ListBookmarkCommand(),
        'T': commands.ListBookmarkCommand(),
        'D': commands.DeleteBookmarkCommand(),
        'Q': commands.QuitCommand()
    })
    print_options(options)

def print_options(options):
    for shortcut, option in options.items():
        print(f'({shortcut}) {option}')
    print()

def get_option_choice(options):
    user_input = input('Choose an option: ')
    while not user_option_is_valid(user_input, options):
        print('Invalid option')
        user_input = input('Choose an option: ')
    return options[user_input.upper()]

def user_option_is_valid(user_input, options):
    return user_input in options or user_input.upper() in options


if __name__ == '__main__':
    commands.CreateBookmarkTableCommand().execute()
    #while True:
    #    menu_loop()


#def options_list():
    options = {
        'A': Option('Add a bookmark', commands.AddBookmarkCommand(), ), 
        'B': Option('List bookmarks by date', commands.ListBookmarkCommand()),
        'T': Option('List bookmarks by title', commands.ListBookmarkCommand(order_by='title')),
        'D': Option('Delete a bookmark', commands.DeleteBookmarkCommand()),
        'Q': Option('quit', commands.QuitCommand())
    }
    print_options(options)

    user_option = get_option_choice(options)
    user_option.choose()