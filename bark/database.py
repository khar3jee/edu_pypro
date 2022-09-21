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
            return cursor

    def create_table(self, table_name, columns):
        """creates database tables in sqlite"""
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
    
    def delete(self, table_name, criteria):
        """delete row in database
        DELETE FROM bookmarks,
        WHERE id = 0;
        """
        placeholders = [f'{column} = ?' for column in criteria.keys()]
        delete_criteria = ' AND '.join(placeholders)
        column_values = tuple(criteria.values())

        self._execute(
            f'''
            DELETE FROM {table_name}
            WHERE {delete_criteria}
            ''',
            column_values,
        )
        

    def select(self, table_name, criteria=None, order_by=None):
        """selects bookmarks based off of criteria"""
        criteria = criteria or {}
        query = f'SELECT * FROM {table_name}'
        column_values = tuple(criteria.values())

        if criteria:
            placeholders = [f'{column} = ?' for column in criteria.keys()]
            select_criteria = ' AND '.join(placeholders)
            query += f'WHERE {select_criteria}'

        if order_by:
            query += f'ORDER BY {order_by}'
        
        return self._execute(
            query,
            column_values,
        )
    
    def drop_table(self, table_name):
        self._execute(f'DROP TABLE {table_name}')

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