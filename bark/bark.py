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

https://peps.python.org/pep-0440/
"""
import commands


if __name__ == '__main__':
    commands.CreateBookmarkTableCommand().execute()
    #commands.AddBookmarkCommand().execute()
    
