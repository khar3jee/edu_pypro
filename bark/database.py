"""
database code for Bark app

Design:
-db connections
-CRUD methods
-prevent SQL injection

Learning Notes
Decided to rewrite everything from the ground up
so I can properly test (and understand) each part
Each numbered comment corresponds to a link at the end explaining
why something works the way it does.


https://docs.python.org/3/library/sqlite3.html
https://docs.python.org/3/library/sqlite3.html#how-to-use-connection-shortcut-methods
https://www.sqlite.org/schematab.html
https://www.sqlite.org/flextypegood.html
https://docs.python.org/3/library/sqlite3.html#sqlite3-explanation
"""

import sqlite3 as sq3

class DatabaseManager():
    """
    manages database operations for Bark app
    """
    def __init__(self, db_file):
        """creates, initializes and
        opens db connection
        """
        self.connection = sq3.connect(db_file) #1

    def __del__(self):
        """close db connection"""
        self.connection.close() #2

    def _execute(self, statement):
        """
        x-accept stmt as str
        -get cursor from db.con
        -exec stmt using cursor
        -return cursor
        """
        cursor = self.connection.cursor()
        cursor.execute(statement)
        print('_execute called')
        return cursor



"""
1. https://docs.python.org/3/library/sqlite3.html#sqlite3.connect
2. https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection
3. https://docs.python.org/3/library/sqlite3.html#how-to-use-the-connection-context-manager
4. https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor
5. https://docs.python.org/3/library/stdtypes.html#dictionary-view-objects
6. https://docs.python.org/3/reference/expressions.html#boolean-operations
7. 
8. 
9. 
10. 
"""