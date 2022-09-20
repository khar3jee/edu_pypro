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

    def _execute(self, statement, values=None):
        """executes database methods in sqlite"""
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(statement, values or [])
            print('_execute called')
            return cursor

    def create_table(self, table_name, columns):
        """creates database tables in sqlite"""
        """
        x-determine col names for table
        x-determine col datatypes
        x-construct sql stmt
        x-must be dict type
        CREATE TABLE IF NOT EXISTS bookmarks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        url TEXT NOT NULL,
        notes TEXT NOT NULL,
        date_added TEXT NOT NULL);
        """
        column_types = [
            f'{column_name} {data_type}'
            for column_name, data_type in columns.items()
        ]
        self._execute(
            f'''
            CREATE TABLE IF NOT EXISTS {table_name}
            ({', '.join(column_types)});
            '''
        )

    def add(self, table_name, data):
        """Adds data to db
        INSERT INTO bookmarks
        (title, url, notes, date_added)
        VALUES (?, ?, ?, ?)
        """
        placeholders = ', '.join('?' * len(data))
        column_names = ', '.join(data.keys())
        column_values = tuple(data.values())
        
        self._execute(
            f'''
            INSERT INTO {table_name}
            ({column_names})
            VALUES ({placeholders});
            ''',
            column_values,
        )
    
    


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